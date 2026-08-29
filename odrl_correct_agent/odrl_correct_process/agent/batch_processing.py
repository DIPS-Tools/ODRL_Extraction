"""OpenAI Batch API lifecycle for large ODRL dataset-correction jobs."""

from __future__ import annotations

import asyncio
import fcntl
import hashlib
import json
import logging
import os
import re
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Awaitable, Callable, Iterable

from openai import OpenAI

from odrl_correct_agent.odrl_correct_process.agent.nodes.node_initialize import node_initialize
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_correct import (
    build_chat_completion_request,
    compare_entity_sets,
    node_odrl_correct,
    normalize_endpoint_rules,
    normalize_rules,
    parse_ai_response,
    render_correction_prompt,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_flat_ner_validate import (
    node_flat_ner_validate,
    validate_flat_ner_entities,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_extraction import (
    node_odrl_extraction,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_output import node_odrl_output
from odrl_correct_agent.odrl_correct_process.agent.state import (
    ODRLCorrectionState,
    create_correction_state,
    default_prompt_path,
)
from odrl_output import build_odrl_diff_record, build_odrl_record_from_entities


logger = logging.getLogger("odrl_correct_agent.batch")
BATCH_SCHEMA_VERSION = 1
MAX_BATCH_REQUESTS = 50_000
MAX_BATCH_INPUT_BYTES = 200 * 1024 * 1024
TERMINAL_FAILURE_STATUSES = frozenset({"failed", "expired", "cancelled"})
REMOTE_ACTIVE_STATUSES = frozenset({
    "validating",
    "in_progress",
    "finalizing",
    "cancelling",
})
PERSISTED_STATE_KEYS = (
    "input_record",
    "record_index",
    "record_total",
    "dataset_path",
    "output_dir",
    "prompt_path",
    "model_name",
    "endpoint",
    "call_endpoint",
    "source_text",
    "original_entities",
    "endpoint_rules",
    "endpoint_error",
    "correction_warnings",
    "duplicate_original_variants",
)


def _entity_signature(record: dict[str, Any]) -> tuple[tuple[int, int, str], ...]:
    return tuple(sorted(
        (
            int(entity["start"]),
            int(entity["end"]),
            str(entity["label"]),
        )
        for entity in record.get("entities") or []
    ))


def _canonical_occurrence(
    occurrences: list[dict[str, Any]],
) -> dict[str, Any]:
    """Choose the most frequent original annotation as AI evidence."""
    counts: dict[tuple[tuple[int, int, str], ...], int] = {}
    for occurrence in occurrences:
        signature = _entity_signature(dict(occurrence["input_record"]))
        counts[signature] = counts.get(signature, 0) + 1
    return min(
        occurrences,
        key=lambda item: (
            -counts[_entity_signature(dict(item["input_record"]))],
            int(item["source_order"]),
        ),
    )


def _safe_model_name(model_name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", model_name.strip())
    return value.strip("._-") or "unknown_model"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _verify_artifact_integrity(manifest: dict[str, Any]) -> None:
    """Reject changed local evidence before producing training datasets."""
    expected_hashes = manifest.get("artifact_sha256") or {}
    artifact_paths = {
        "requests": Path(str(manifest["requests_path"])),
        "states": Path(str(manifest["states_path"])),
        "prompt": Path(str(manifest["prompt_snapshot_path"])),
    }
    for name, expected_hash in expected_hashes.items():
        path = artifact_paths.get(str(name))
        if path is None:
            continue
        if not path.is_file():
            raise FileNotFoundError(f"Batch {name} artifact is missing: {path}")
        actual_hash = _sha256_file(path)
        if actual_hash != expected_hash:
            raise RuntimeError(
                f"Batch {name} artifact changed after preparation: {path}. "
                "Refusing to mix different evidence into the final dataset."
            )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{path}:{line_number} contains invalid JSON: {exc.msg}"
                ) from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number} must be a JSON object.")
            records.append(value)
    return records


def _write_jsonl_atomic(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = ""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = ""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name

            json.dump(payload, handle, ensure_ascii=False, indent=2)

            handle.write("\n")
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def _read_manifest(path: str | Path) -> tuple[Path, dict[str, Any]]:
    manifest_path = Path(path).expanduser().resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Batch manifest not found: {manifest_path}")
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Batch manifest must contain a JSON object: {manifest_path}")
    if payload.get("schema_version") != BATCH_SCHEMA_VERSION:
        raise ValueError(
            f"Unsupported batch manifest schema: {payload.get('schema_version')!r}"
        )
    return manifest_path, payload


def _create_client() -> OpenAI:
    api_key = str(os.getenv("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required to submit or retrieve a batch.")
    base_url = str(
        os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE") or ""
    ).strip()
    organization = str(os.getenv("OPENAI_ORG_ID") or "").strip()
    project = str(os.getenv("OPENAI_PROJECT_ID") or "").strip()
    return OpenAI(
        api_key=api_key,
        organization=organization or None,
        project=project or None,
        base_url=base_url or None,
    )


def _get_value(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def _json_safe(value: Any) -> Any:
    """Convert OpenAI SDK/Pydantic objects into manifest-safe JSON values.

    The SDK exposes ``batch.errors`` as an ``Errors`` model rather than a
    plain dictionary.  Persisting that object directly makes ``json.dump``
    fail while updating status, so normalize SDK models recursively here.
    """
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item) for item in value]
    for method_name in ("model_dump", "to_dict"):
        method = getattr(value, method_name, None)
        if callable(method):
            try:
                return _json_safe(method())
            except TypeError:
                continue
    if hasattr(value, "__dict__"):
        return _json_safe(vars(value))
    return str(value)


def _batch_error_summaries(batch_errors: Any) -> list[str]:
    """Flatten the Batch ``errors`` payload into short human-readable lines."""
    batch_errors = _json_safe(batch_errors)
    if not isinstance(batch_errors, dict):
        return []
    data = batch_errors.get("data")
    if not isinstance(data, list):
        return []
    summaries: list[str] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        parts: list[str] = []
        for key in ("code", "line", "param", "message"):
            value = item.get(key)
            if value in (None, ""):
                continue
            parts.append(f"{key}={value}")
        if parts:
            summaries.append("; ".join(parts))
    return summaries


def _wait_for_batch_file_ready(
    api: Any,
    file_id: str,
    *,
    timeout_seconds: float | None = None,
    poll_seconds: float | None = None,
) -> dict[str, Any]:
    """Verify the uploaded file is visible and processed before Batch creation."""
    retrieve = getattr(getattr(api, "files", None), "retrieve", None)
    # Lightweight test doubles and compatible providers may omit retrieval.
    if not callable(retrieve):
        return {"id": file_id, "status": "verification_unavailable"}

    timeout = float(
        timeout_seconds
        if timeout_seconds is not None
        else os.getenv("ODRL_BATCH_FILE_READY_TIMEOUT_SECONDS", "180")
    )
    interval = float(
        poll_seconds
        if poll_seconds is not None
        else os.getenv("ODRL_BATCH_FILE_READY_POLL_SECONDS", "2")
    )
    deadline = time.monotonic() + max(timeout, 0.0)
    last_error = ""
    while True:
        try:
            remote_file = retrieve(file_id)
            status = str(_get_value(remote_file, "status", "") or "").lower()
            purpose = str(_get_value(remote_file, "purpose", "") or "").lower()
            if purpose and purpose != "batch":
                raise RuntimeError(
                    f"Uploaded file {file_id} has purpose {purpose!r}, not 'batch'."
                )
            if status in {"processed", "ready"}:
                logger.info(
                    "batch_submit status=file_ready file_id=%s file_status=%s",
                    file_id,
                    status,
                )
                details = _json_safe(remote_file)
                return details if isinstance(details, dict) else {
                    "id": file_id,
                    "status": status,
                }
            if status in {"error", "failed", "cancelled", "deleted"}:
                raise RuntimeError(
                    f"Uploaded Batch file {file_id} entered terminal status {status!r}."
                )
            last_error = f"file status is {status or 'unknown'}"
        except RuntimeError:
            raise
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"

        if time.monotonic() >= deadline:
            raise RuntimeError(
                f"Uploaded Batch file {file_id} was not ready after {timeout:.0f}s: "
                f"{last_error}. The Batch was not submitted. Check that the API "
                "key, OPENAI_ORG_ID, and OPENAI_PROJECT_ID use the same project."
            )
        logger.info(
            "batch_submit status=waiting_for_file file_id=%s detail=%s",
            file_id,
            last_error,
        )
        time.sleep(max(interval, 0.1))


async def _run_preparation_nodes(state: ODRLCorrectionState) -> None:
    record_label = f"{state.get('record_index', 0)}/{state.get('record_total', 0)}"
    for node in (node_initialize, node_odrl_extraction):
        started = time.perf_counter()
        logger.info("record=%s node=%s status=started", record_label, node.__name__)
        try:
            update = await node(state)
        except Exception:
            logger.exception(
                "record=%s node=%s status=failed elapsed_ms=%.1f",
                record_label,
                node.__name__,
                (time.perf_counter() - started) * 1000,
            )
            raise
        state.update(update)
        logger.info(
            "record=%s node=%s status=completed elapsed_ms=%.1f",
            record_label,
            node.__name__,
            (time.perf_counter() - started) * 1000,
        )


def _persisted_state(custom_id: str, split: str, state: ODRLCorrectionState) -> dict[str, Any]:
    return {
        "custom_id": custom_id,
        "split": split,
        "state": {
            key: state.get(key)
            for key in PERSISTED_STATE_KEYS
        },
    }


async def prepare_batch_job(
    dataset_paths: Iterable[str | Path],
    *,
    output_dir: str | Path | None = None,
    job_dir: str | Path | None = None,
    prompt_path: str | Path | None = None,
    model_name: str = "",
    endpoint: str = "",
    call_endpoint: bool = True,
    limit: int | None = None,
    submit: bool = False,
    client: Any = None,
) -> Path:
    """Prepare all records and optionally submit one discounted OpenAI batch."""
    sources = [Path(path).expanduser().resolve() for path in dataset_paths]
    if not sources:
        raise ValueError("At least one dataset path is required for Batch preparation.")
    for source in sources:
        if not source.is_file():
            raise FileNotFoundError(f"Dataset not found: {source}")
    split_names = [source.stem for source in sources]
    if len(set(split_names)) != len(split_names):
        raise ValueError("Batch dataset filenames must have unique stems.")

    resolved_model = str(
        model_name
        or os.getenv("MODEL_NAME")
        or os.getenv("OPENAI_MODEL_NAME")
        or "gpt-4o-mini"
    ).strip()
    final_output_dir = (
        Path(output_dir).expanduser().resolve()
        if output_dir
        else sources[0].parent
    )
    artifacts_root = (
        Path(job_dir).expanduser().resolve()
        if job_dir
        else final_output_dir / "batch_jobs"
    )
    job_id = (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "_"
        + str(uuid.uuid4())[:8]
    )
    job_path = artifacts_root / f"odrl_{_safe_model_name(resolved_model)}_{job_id}"
    job_path.mkdir(parents=True, exist_ok=False)
    requests_path = job_path / "requests.jsonl"
    states_path = job_path / "states.jsonl"
    manifest_path = job_path / "manifest.json"
    source_prompt_path = Path(prompt_path or default_prompt_path()).expanduser().resolve()
    if not source_prompt_path.is_file():
        raise FileNotFoundError(f"ODRL correction prompt not found: {source_prompt_path}")
    prompt_snapshot_path = job_path / "odrl_extraction.prompt"
    prompt_snapshot_path.write_text(
        source_prompt_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    request_records: list[dict[str, Any]] = []
    state_records: list[dict[str, Any]] = []
    split_metadata: list[dict[str, Any]] = []
    grouped: dict[str, list[dict[str, Any]]] = {}
    source_order = 0
    for source, split in zip(sources, split_names):
        records = _read_jsonl(source)
        original_odrl_path = source.with_name(f"{source.stem}_odrl.txt")
        original_odrl_records = (
            _read_jsonl(original_odrl_path) if original_odrl_path.is_file() else []
        )
        if limit is not None:
            records = records[:limit]
            original_odrl_records = original_odrl_records[:limit]
        if original_odrl_records and len(original_odrl_records) != len(records):
            raise ValueError(
                f"{original_odrl_path} has {len(original_odrl_records)} records; "
                f"expected {len(records)} to align with {source}"
            )
        split_metadata.append({
            "split": split,
            "source_path": str(source),
            "record_count": len(records),
            "source_sha256": _sha256_file(source),
            "original_odrl_path": (
                str(original_odrl_path) if original_odrl_path.is_file() else ""
            ),
            "original_odrl_sha256": (
                _sha256_file(original_odrl_path) if original_odrl_path.is_file() else ""
            ),
        })
        logger.info("batch_prepare split=%s status=grouping records=%d", split, len(records))
        for index, record in enumerate(records, start=1):
            source_text = str(record.get("text") or "")
            if not source_text:
                raise ValueError(f"{source}:{index} has empty text")
            source_order += 1
            grouped.setdefault(source_text, []).append({
                "split": split,
                "record_index": index,
                "record_total": len(records),
                "dataset_path": str(source),
                "input_record": record,
                "original_odrl_record": (
                    original_odrl_records[index - 1]
                    if original_odrl_records
                    else None
                ),
                "source_order": source_order,
            })

    total_occurrences = sum(len(items) for items in grouped.values())
    duplicate_text_group_count = sum(1 for items in grouped.values() if len(items) > 1)
    conflicting_original_gold_group_count = sum(
        1
        for items in grouped.values()
        if len({
            _entity_signature(dict(item["input_record"])) for item in items
        }) > 1
    )
    for unique_index, (source_text, occurrences) in enumerate(grouped.items(), start=1):
        canonical = _canonical_occurrence(occurrences)
        split = str(canonical["split"])
        index = int(canonical["record_index"])
        custom_id = f"{split}-{index:07d}"
        canonical_record = dict(canonical["input_record"])
        signatures_seen: set[tuple[tuple[int, int, str], ...]] = set()
        duplicate_variants: list[list[dict[str, Any]]] = []
        canonical_signature = _entity_signature(canonical_record)
        for occurrence in occurrences:
            record = dict(occurrence["input_record"])
            signature = _entity_signature(record)
            if signature == canonical_signature or signature in signatures_seen:
                continue
            signatures_seen.add(signature)
            duplicate_variants.append([
                dict(entity) for entity in record.get("entities") or []
            ])
        state = create_correction_state(
            canonical_record,
            record_index=index,
            record_total=int(canonical["record_total"]),
            dataset_path=str(canonical["dataset_path"]),
            output_dir=str(final_output_dir),
            prompt_path=str(prompt_snapshot_path),
            model_name=resolved_model,
            endpoint=endpoint,
            call_endpoint=call_endpoint,
            duplicate_original_variants=duplicate_variants,
        )
        await _run_preparation_nodes(state)
        if call_endpoint and state.get("endpoint_error"):
            raise RuntimeError(
                f"{custom_id}: local ODRL extraction failed; Batch submission "
                f"stopped to protect correction quality: {state['endpoint_error']}"
            )
        endpoint_rules = normalize_endpoint_rules(
            state.get("endpoint_rules"), source_text
        )
        prompt = render_correction_prompt(
            str(state.get("prompt_template") or ""),
            source_text,
            list(state.get("original_entities") or []),
            endpoint_rules,
            duplicate_variants,
        )
        request_records.append({
            "custom_id": custom_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": build_chat_completion_request(prompt, resolved_model),
        })
        persisted = _persisted_state(custom_id, split, state)
        persisted["occurrences"] = [
            {
                key: occurrence[key]
                for key in (
                    "split",
                    "record_index",
                    "record_total",
                    "dataset_path",
                    "input_record",
                    "original_odrl_record",
                    "source_order",
                )
            }
            for occurrence in occurrences
        ]
        state_records.append(persisted)
        logger.info(
            "batch_prepare unique=%d/%d custom_id=%s duplicates=%d status=prepared",
            unique_index,
            len(grouped),
            custom_id,
            len(occurrences) - 1,
        )

    if not request_records:
        raise ValueError("The selected datasets contain no records.")
    if len(request_records) > MAX_BATCH_REQUESTS:
        raise ValueError(
            f"Batch contains {len(request_records)} requests; the supported "
            f"maximum is {MAX_BATCH_REQUESTS}. Split it into multiple jobs."
        )
    _write_jsonl_atomic(requests_path, request_records)
    _write_jsonl_atomic(states_path, state_records)
    if requests_path.stat().st_size > MAX_BATCH_INPUT_BYTES:
        raise ValueError(
            f"Batch input is {requests_path.stat().st_size} bytes; the supported "
            f"maximum is {MAX_BATCH_INPUT_BYTES} bytes. Split it into multiple jobs."
        )
    request_settings = {
        key: value
        for key, value in request_records[0]["body"].items()
        if key != "messages"
    }
    manifest: dict[str, Any] = {
        "schema_version": BATCH_SCHEMA_VERSION,
        "job_id": job_id,
        "status": "prepared",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model_name": resolved_model,
        "request_count": len(request_records),
        "source_record_count": total_occurrences,
        "unique_text_count": len(grouped),
        "duplicate_occurrence_count": total_occurrences - len(grouped),
        "duplicate_text_group_count": duplicate_text_group_count,
        "conflicting_original_gold_group_count": conflicting_original_gold_group_count,
        "duplicate_policy": "one_ai_gold_per_exact_text_then_expand_to_all_occurrences",
        "request_settings": request_settings,
        "requests_path": str(requests_path),
        "states_path": str(states_path),
        "prompt_snapshot_path": str(prompt_snapshot_path),
        "results_path": str(job_path / "results.jsonl"),
        "errors_path": str(job_path / "errors.jsonl"),
        "output_dir": str(final_output_dir),
        "splits": split_metadata,
        "artifact_sha256": {
            "requests": _sha256_file(requests_path),
            "states": _sha256_file(states_path),
            "prompt": _sha256_file(prompt_snapshot_path),
        },
        "odrl_extraction": {
            "enabled": bool(call_endpoint),
            "endpoint_override": str(endpoint or ""),
            "configured_model": str(
                os.getenv("ODRL_EXTRACTION_MODEL_NAME") or ""
            ),
        },
    }
    _write_json_atomic(manifest_path, manifest)
    logger.info(
        "batch_prepare status=completed requests=%d manifest=%s",
        len(request_records),
        manifest_path,
    )
    if submit:
        submit_batch_job(manifest_path, client=client)
    return manifest_path


def submit_batch_job(manifest_path: str | Path, *, client: Any = None) -> dict[str, Any]:
    """Upload prepared requests and submit the paid 24-hour Batch job."""
    path, manifest = _read_manifest(manifest_path)
    if manifest.get("batch_id"):
        raise ValueError(
            f"This manifest was already submitted as {manifest['batch_id']}."
        )
    api = client or _create_client()
    requests_path = Path(str(manifest["requests_path"]))
    if not manifest.get("input_file_id"):
        logger.info("batch_submit status=uploading requests=%s", requests_path)
        with requests_path.open("rb") as handle:
            uploaded = api.files.create(file=handle, purpose="batch")
        manifest["input_file_id"] = str(_get_value(uploaded, "id"))
        manifest["status"] = "uploaded"
        _write_json_atomic(path, manifest)
    else:
        logger.info(
            "batch_submit status=reusing_upload input_file_id=%s",
            manifest["input_file_id"],
        )

    file_details = _wait_for_batch_file_ready(
        api,
        str(manifest["input_file_id"]),
    )
    manifest["input_file_status"] = str(file_details.get("status") or "unknown")
    manifest["input_file_verified_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(path, manifest)

    batch = api.batches.create(
        input_file_id=manifest["input_file_id"],
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={
            "description": "ODRL dataset correction",
            "job_id": str(manifest.get("job_id") or "")[:512],
        },
    )
    manifest["batch_id"] = str(_get_value(batch, "id"))
    manifest["status"] = str(_get_value(batch, "status", "validating"))
    manifest["submitted_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(path, manifest)
    logger.info(
        "batch_submit status=%s batch_id=%s manifest=%s",
        manifest["status"],
        manifest["batch_id"],
        path,
    )
    return manifest


def refresh_batch_status(
    manifest_path: str | Path,
    *,
    client: Any = None,
) -> dict[str, Any]:
    """Retrieve remote Batch status and persist it in the manifest."""
    path, manifest = _read_manifest(manifest_path)
    batch_id = str(manifest.get("batch_id") or "")
    if not batch_id:
        raise ValueError("The prepared manifest has not been submitted yet.")
    api = client or _create_client()
    batch = api.batches.retrieve(batch_id)
    manifest["status"] = str(_get_value(batch, "status", "unknown"))
    manifest["output_file_id"] = _get_value(batch, "output_file_id")
    manifest["error_file_id"] = _get_value(batch, "error_file_id")
    batch_errors = _get_value(batch, "errors")
    if batch_errors is not None:
        manifest["batch_errors"] = _json_safe(batch_errors)
    counts = _get_value(batch, "request_counts")
    if counts is not None:
        manifest["request_counts"] = {
            "total": int(_get_value(counts, "total", 0) or 0),
            "completed": int(_get_value(counts, "completed", 0) or 0),
            "failed": int(_get_value(counts, "failed", 0) or 0),
        }
    manifest["remote_timestamps"] = {
        name: _get_value(batch, name)
        for name in (
            "created_at",
            "in_progress_at",
            "expires_at",
            "finalizing_at",
            "completed_at",
            "failed_at",
            "expired_at",
            "cancelling_at",
            "cancelled_at",
        )
        if _get_value(batch, name) is not None
    }
    manifest["status_checked_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(path, manifest)
    logger.info(
        "batch_status batch_id=%s status=%s counts=%s",
        batch_id,
        manifest["status"],
        manifest.get("request_counts") or {},
    )
    return manifest


def _acquire_watch_lock(manifest_path: Path) -> Any:
    """Prevent two local watchers from finalizing the same manifest."""
    lock_path = manifest_path.with_name(f"{manifest_path.name}.watch.lock")
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        handle.close()
        raise RuntimeError(
            f"Another watcher already owns this Batch manifest: {manifest_path}"
        ) from exc
    handle.seek(0)
    handle.truncate()
    handle.write(
        json.dumps({
            "pid": os.getpid(),
            "acquired_at": datetime.now(timezone.utc).isoformat(),
        })
        + "\n"
    )
    handle.flush()
    return handle


def _release_watch_lock(handle: Any) -> None:
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    finally:
        handle.close()


def _assert_finalized_outputs_exist(manifest: dict[str, Any]) -> None:
    output_paths = [
        Path(str(value))
        for key in ("ner_outputs", "odrl_outputs", "diff_outputs")
        for value in manifest.get(key) or []
    ] + [
        Path(str(value))
        for value in manifest.get("odrl_diff_outputs") or []
    ]
    if not output_paths:
        raise RuntimeError(
            "Manifest says finalized but contains no recorded output paths."
        )
    missing = [str(path) for path in output_paths if not path.is_file()]
    if missing:
        raise RuntimeError(
            "Manifest says finalized but output files are missing: "
            + ", ".join(missing)
        )


def _original_odrl_record_from_state(state: ODRLCorrectionState) -> dict[str, Any]:
    input_record = dict(state.get("input_record") or {})
    text = str(input_record.get("text") or state.get("source_text") or "")
    entities = [
        dict(entity) for entity in input_record.get("entities") or []
        if isinstance(entity, dict)
    ]
    if not text:
        return {"text": "", "odrl": []}
    return build_odrl_record_from_entities(text, entities)


async def watch_and_finalize_batch_job(
    manifest_path: str | Path,
    *,
    poll_interval_seconds: float = 300.0,
    timeout_hours: float = 26.0,
    max_consecutive_errors: int = 12,
    strict: bool = True,
    recovery_policy: str = "synchronous",
    synchronous_recovery_limit: int | None = None,
    client: Any = None,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    monotonic: Callable[[], float] = time.monotonic,
) -> dict[str, Any]:
    """Resumably poll a submitted Batch and strictly finalize on completion.

    The manifest is checkpointed after every successful poll and transient
    polling failure. A local timeout never cancels the remote Batch; rerunning
    this function with the same manifest resumes from remote state.
    """
    if poll_interval_seconds <= 0:
        raise ValueError("Batch poll interval must be greater than zero.")
    if timeout_hours <= 0:
        raise ValueError("Batch watch timeout must be greater than zero.")
    if max_consecutive_errors <= 0:
        raise ValueError("Maximum consecutive Batch errors must be greater than zero.")

    path, manifest = _read_manifest(manifest_path)
    if manifest.get("status") == "finalized":
        _assert_finalized_outputs_exist(manifest)
        logger.info("batch_watch status=already_finalized manifest=%s", path)
        return manifest
    if not manifest.get("batch_id"):
        raise ValueError(
            "The manifest has not been submitted. Use --batch-submit first."
        )

    lock_handle = _acquire_watch_lock(path)
    started = monotonic()
    consecutive_errors = 0
    api = client or _create_client()
    try:
        # Read once more after taking the lock in case another process completed
        # immediately before this watcher acquired ownership.
        path, manifest = _read_manifest(path)
        if manifest.get("status") == "finalized":
            _assert_finalized_outputs_exist(manifest)
            return manifest
        watch = dict(manifest.get("watch") or {})
        now = datetime.now(timezone.utc).isoformat()
        watch.setdefault("first_started_at", now)
        watch.update({
            "last_started_at": now,
            "run_count": int(watch.get("run_count") or 0) + 1,
            "pid": os.getpid(),
            "poll_interval_seconds": poll_interval_seconds,
            "timeout_hours": timeout_hours,
            "max_consecutive_errors": max_consecutive_errors,
            "outcome": "watching",
        })
        manifest["watch"] = watch
        _write_json_atomic(path, manifest)

        while True:
            elapsed_seconds = monotonic() - started
            if elapsed_seconds >= timeout_hours * 3600:
                watch.update({
                    "outcome": "local_timeout",
                    "stopped_at": datetime.now(timezone.utc).isoformat(),
                    "elapsed_seconds": elapsed_seconds,
                    "message": (
                        "Local watcher timed out; the remote Batch was not "
                        "cancelled. Resume with the same manifest."
                    ),
                })
                manifest["watch"] = watch
                _write_json_atomic(path, manifest)
                raise TimeoutError(
                    f"Local Batch watcher exceeded {timeout_hours:g} hours. "
                    "The remote job was not cancelled; rerun the watcher with "
                    f"the same manifest: {path}"
                )

            try:
                manifest = refresh_batch_status(path, client=api)
            except Exception as exc:
                consecutive_errors += 1
                watch = dict(manifest.get("watch") or watch)
                watch.update({
                    "last_poll_at": datetime.now(timezone.utc).isoformat(),
                    "consecutive_errors": consecutive_errors,
                    "last_error": f"{type(exc).__name__}: {exc}",
                    "outcome": "poll_retry",
                })
                manifest["watch"] = watch
                _write_json_atomic(path, manifest)
                if consecutive_errors >= max_consecutive_errors:
                    watch.update({
                        "outcome": "poll_failed",
                        "stopped_at": datetime.now(timezone.utc).isoformat(),
                    })
                    manifest["watch"] = watch
                    _write_json_atomic(path, manifest)
                    raise RuntimeError(
                        "Batch status polling repeatedly failed. The remote job "
                        f"was not cancelled; resume with manifest {path}."
                    ) from exc
                delay = min(
                    poll_interval_seconds * (2 ** (consecutive_errors - 1)),
                    900.0,
                )
                logger.warning(
                    "batch_watch status=poll_retry error=%s:%s retry_in_seconds=%.1f",
                    type(exc).__name__,
                    exc,
                    delay,
                )
                await sleep(delay)
                continue

            consecutive_errors = 0
            watch = dict(manifest.get("watch") or watch)
            watch.update({
                "last_poll_at": datetime.now(timezone.utc).isoformat(),
                "poll_count": int(watch.get("poll_count") or 0) + 1,
                "consecutive_errors": 0,
                "last_remote_status": str(manifest.get("status") or "unknown"),
                "elapsed_seconds": monotonic() - started,
                "outcome": "watching",
            })
            watch.pop("last_error", None)
            manifest["watch"] = watch
            _write_json_atomic(path, manifest)
            status = str(manifest.get("status") or "unknown")

            if status == "completed":
                logger.info(
                    "batch_watch status=completed action=strict_finalize manifest=%s",
                    path,
                )
                try:
                    await finalize_batch_job(
                        path,
                        strict=strict,
                        client=api,
                        recovery_policy=recovery_policy,
                        synchronous_recovery_limit=synchronous_recovery_limit,
                    )
                except Exception as exc:
                    _, failed_manifest = _read_manifest(path)
                    failed_watch = dict(failed_manifest.get("watch") or watch)
                    failed_watch.update({
                        "outcome": "finalization_failed",
                        "stopped_at": datetime.now(timezone.utc).isoformat(),
                        "last_error": f"{type(exc).__name__}: {exc}",
                    })
                    failed_manifest["watch"] = failed_watch
                    _write_json_atomic(path, failed_manifest)
                    raise
                _, finalized = _read_manifest(path)
                finalized_watch = dict(finalized.get("watch") or watch)
                finalized_watch.update({
                    "outcome": "finalized",
                    "stopped_at": datetime.now(timezone.utc).isoformat(),
                    "last_remote_status": "completed",
                })
                finalized_watch.pop("last_error", None)
                finalized["watch"] = finalized_watch
                _write_json_atomic(path, finalized)
                _assert_finalized_outputs_exist(finalized)
                return finalized

            if status in TERMINAL_FAILURE_STATUSES:
                error_lines = _batch_error_summaries(manifest.get("batch_errors"))
                error_suffix = ""
                if error_lines:
                    error_suffix = "\nRemote batch errors:\n" + "\n".join(
                        f"- {line}" for line in error_lines[:20]
                    )
                watch.update({
                    "outcome": f"remote_{status}",
                    "stopped_at": datetime.now(timezone.utc).isoformat(),
                })
                manifest["watch"] = watch
                _write_json_atomic(path, manifest)
                raise RuntimeError(
                    f"OpenAI Batch {manifest.get('batch_id')} ended with terminal "
                    f"status {status!r}. No corrected datasets were written."
                    f"{error_suffix}"
                )

            if status not in REMOTE_ACTIVE_STATUSES:
                logger.warning(
                    "batch_watch status=unknown_remote_state remote_status=%s",
                    status,
                )
            await sleep(poll_interval_seconds)
    finally:
        _release_watch_lock(lock_handle)


def _download_batch_files(
    manifest_path: Path,
    manifest: dict[str, Any],
    client: Any,
) -> None:
    def download_atomic(file_id: str, destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary_name = ""
        try:
            with tempfile.NamedTemporaryFile(
                dir=destination.parent,
                prefix=f".{destination.name}.",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temporary_name = handle.name
            client.files.content(file_id).write_to_file(temporary_name)
            os.replace(temporary_name, destination)
        finally:
            if temporary_name and os.path.exists(temporary_name):
                os.unlink(temporary_name)

    output_file_id = str(manifest.get("output_file_id") or "")
    if not output_file_id:
        raise RuntimeError("Completed Batch response has no output_file_id.")
    results_path = Path(str(manifest["results_path"]))
    download_atomic(output_file_id, results_path)
    error_file_id = str(manifest.get("error_file_id") or "")
    if error_file_id:
        download_atomic(
            error_file_id,
            Path(str(manifest["errors_path"])),
        )
    manifest["downloaded_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(manifest_path, manifest)


def _batch_result_error(result: dict[str, Any] | None) -> str:
    if result is None:
        return "Batch output is missing this custom_id."
    if result.get("error"):
        return f"Batch request error: {result['error']}"
    response = result.get("response") or {}
    status_code = int(response.get("status_code") or 0)
    if status_code != 200:
        return f"Batch request returned HTTP {status_code}."
    body = response.get("body") or {}
    choices = body.get("choices") or []
    if not choices:
        return "Batch response contains no choices."
    if choices[0].get("finish_reason") == "length":
        return "Batch response was truncated at max_completion_tokens."
    content = ((choices[0].get("message") or {}).get("content"))
    if not content:
        return "Batch response contains empty message content."
    return ""


def _accumulate_usage(total: dict[str, int], result: dict[str, Any]) -> None:
    body = ((result.get("response") or {}).get("body") or {})
    usage = body.get("usage") or {}
    completion_details = usage.get("completion_tokens_details") or {}
    for target, source in (
        ("prompt_tokens", "prompt_tokens"),
        ("completion_tokens", "completion_tokens"),
        ("total_tokens", "total_tokens"),
    ):
        total[target] += int(usage.get(source) or 0)
    total["reasoning_tokens"] += int(completion_details.get("reasoning_tokens") or 0)


def _accumulate_chat_response_usage(total: dict[str, int], response: Any) -> None:
    """Include standard-API recovery usage in the same audit totals."""
    usage = _get_value(response, "usage") or {}
    completion_details = _get_value(usage, "completion_tokens_details") or {}
    for target, source in (
        ("prompt_tokens", "prompt_tokens"),
        ("completion_tokens", "completion_tokens"),
        ("total_tokens", "total_tokens"),
    ):
        total[target] += int(_get_value(usage, source, 0) or 0)
    total["reasoning_tokens"] += int(
        _get_value(completion_details, "reasoning_tokens", 0) or 0
    )


def _retryable_batch_result_error(error: str) -> bool:
    """Return whether a fresh request can recover a model-level empty result."""
    return error in {
        "Batch response was truncated at max_completion_tokens.",
        "Batch response contains empty message content.",
        "Batch response contains no choices.",
    }


def _positive_int_env(name: str, default: int) -> int:
    raw = str(os.getenv(name) or default).strip()
    value = int(raw)
    if value < 1:
        raise ValueError(f"{name} must be a positive integer.")
    return value


def build_flat_ner_recovery_request(
    prompt: str,
    validation_error: str,
    model_name: str,
    *,
    reasoning_effort: str = "medium",
    max_output_tokens: int = 16000,
) -> dict[str, Any]:
    """Build the same strict request for synchronous or discounted recovery."""
    retry_prompt = (
        prompt
        + "\n\nFLAT-NER RECOVERY: The following response contract replaces the "
        "earlier response-format contract. The previous answer was rejected by the "
        "training-data validator for this exact reason:\n"
        + validation_error
        + "\nReturn exactly one JSON object with keys validated_policy_rules and "
        "corrected_entities. Preserve all real policy components. Each corrected_entities "
        "item must have integer start, integer end, label, and text. start/end are "
        "zero-based Python half-open character offsets into SOURCE, and text must equal "
        "SOURCE[start:end] exactly, including case and punctuation. Allowed labels are "
        "ASSIGNEE, ACTION, ASSET, CONSTRAINT, PURPOSE, RULE_TYPE-PERMISSION, "
        "RULE_TYPE-OBLIGATION, and RULE_TYPE-PROHIBITION. Entity spans must be pairwise "
        "non-overlapping. Include shared text only once. Never put an ACTION inside an "
        "ASSIGNEE/ASSET, or an entity inside CONSTRAINT/PURPOSE. Every non-empty "
        "ACTION, CONSTRAINT, and PURPOSE entity must occur inside that rule's source_text. "
        "Repeated verbs in different numbered clauses require separate ACTION entities. "
        "Only an identical ASSIGNEE or ASSET may be reused across coordinated rules. "
        "Do not output entities that are not represented by a validated_policy_rules "
        "component. Every component is optional, including ACTION and rule_type. Use an "
        "empty string whenever a component cannot be identified confidently as an exact "
        "source span. Do not invent a rule type or any other component. A partial grounded "
        "rule, or empty arrays when no component is reliable, is valid."
    )
    request = build_chat_completion_request(retry_prompt, model_name)
    rule_properties = {
        name: {"type": "string"}
        for name in (
            "source_text", "assignee", "action", "asset",
            "attributed_party", "rule_type", "constraint", "purpose",
        )
    }
    entity_properties = {
        "start": {"type": "integer", "minimum": 0},
        "end": {"type": "integer", "minimum": 1},
        "label": {
            "type": "string",
            "enum": [
                "ASSIGNEE", "ACTION", "ASSET", "CONSTRAINT", "PURPOSE",
                "RULE_TYPE-PERMISSION", "RULE_TYPE-OBLIGATION",
                "RULE_TYPE-PROHIBITION",
            ],
        },
        "text": {"type": "string"},
    }
    request["response_format"] = {
        "type": "json_schema",
        "json_schema": {
            "name": "odrl_flat_ner_recovery",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "validated_policy_rules": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": rule_properties,
                            "required": list(rule_properties),
                            "additionalProperties": False,
                        },
                    },
                    "corrected_entities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": entity_properties,
                            "required": list(entity_properties),
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["validated_policy_rules", "corrected_entities"],
                "additionalProperties": False,
            },
        },
    }
    request["reasoning_effort"] = reasoning_effort
    request["max_completion_tokens"] = max_output_tokens
    return request


def _validate_recovery_alignment(
    source_text: str,
    rules: list[dict[str, Any]],
    entities: list[dict[str, Any]],
) -> None:
    """Require recovered flat entities to represent each rule coherently.

    Every component is optional. ASSIGNEE and ASSET may be inherited from an
    earlier coordinated clause. A non-empty ACTION, CONSTRAINT, or PURPOSE must
    have its own occurrence inside that rule's source_text. This prevents one
    repeated verb such as ``ensure`` from satisfying several numbered rules.
    """
    field_labels = {
        "assignee": "ASSIGNEE",
        "action": "ACTION",
        "asset": "ASSET",
        "constraint": "CONSTRAINT",
        "purpose": "PURPOSE",
    }
    reusable_fields = {"assignee", "asset"}
    represented_components: set[tuple[str, str]] = set()
    rule_types: set[str] = set()

    for rule_index, rule in enumerate(rules, start=1):
        source_quote = str(rule.get("source_text") or "")
        source_scopes: list[tuple[int, int]] = []
        cursor = 0
        while source_quote and cursor <= len(source_text) - len(source_quote):
            found = source_text.find(source_quote, cursor)
            if found < 0:
                break
            source_scopes.append((found, found + len(source_quote)))
            cursor = found + 1
        if not source_scopes:
            raise ValueError(
                f"recovery policy rule {rule_index} source_text is not an exact SOURCE quote"
            )

        rule_type = str(rule.get("rule_type") or "")
        if rule_type:
            rule_types.add(rule_type)
        for field, label in field_labels.items():
            quote = str(rule.get(field) or "")
            if not quote:
                continue
            represented_components.add((label, quote))
            matches = [
                entity
                for entity in entities
                if entity["label"] == label
                and source_text[entity["start"]:entity["end"]] == quote
            ]
            if not matches:
                raise ValueError(
                    f"recovery policy rule {rule_index} {field} has no matching "
                    "corrected entity"
                )
            if field not in reusable_fields and not any(
                scope_start <= entity["start"]
                and entity["end"] <= scope_end
                for entity in matches
                for scope_start, scope_end in source_scopes
            ):
                raise ValueError(
                    f"recovery policy rule {rule_index} {field} has no matching "
                    "entity inside its source_text"
                )

    for entity_index, entity in enumerate(entities, start=1):
        label = str(entity["label"])
        quote = source_text[entity["start"]:entity["end"]]
        if label.startswith("RULE_TYPE-"):
            expected_type = label[len("RULE_TYPE-"):].lower()
            if expected_type not in rule_types:
                raise ValueError(
                    f"recovery entity {entity_index} has an unrepresented rule marker"
                )
        elif (label, quote) not in represented_components:
            raise ValueError(
                f"recovery entity {entity_index} is not represented by any policy rule"
            )

    for rule_type in rule_types:
        expected_label = f"RULE_TYPE-{rule_type.upper()}"
        if not any(entity["label"] == expected_label for entity in entities):
            raise ValueError(
                f"recovery rules have no {expected_label} marker entity"
            )


def _recover_batch_response(
    api: Any,
    *,
    prompt: str,
    model_name: str,
    custom_id: str,
    usage: dict[str, int],
) -> tuple[Any | None, list[str], int]:
    """Retry only an unusable Batch result using constrained reasoning.

    This deliberately uses the standard synchronous API after a Batch has
    completed. It preserves every successful discounted Batch result and pays
    the standard rate only for the exceptional record. A result is returned
    only after its required JSON contract has been parsed successfully.
    """
    enabled = str(
        os.getenv("ODRL_CORRECTION_RECOVER_FAILED_BATCH", "true")
    ).strip().lower() in {"1", "true", "yes", "on"}
    if not enabled:
        return None, ["Targeted failed-record recovery is disabled."], 0

    attempts = _positive_int_env("ODRL_CORRECTION_RECOVERY_ATTEMPTS", 2)
    max_tokens = _positive_int_env(
        "ODRL_CORRECTION_RECOVERY_MAX_OUTPUT_TOKENS", 16000
    )
    effort = str(
        os.getenv("ODRL_CORRECTION_RECOVERY_REASONING_EFFORT", "low")
    ).strip().lower()
    if effort not in {"none", "low", "medium", "high", "xhigh", "max"}:
        raise ValueError(
            "ODRL_CORRECTION_RECOVERY_REASONING_EFFORT must be one of: "
            "high, low, max, medium, none, xhigh"
        )

    recovery_prompt = (
        prompt
        + "\n\nRECOVERY INSTRUCTION: The previous request exhausted its output "
        "budget while reasoning and returned no usable answer. Do not repeat "
        "extended analysis. Apply the rules above directly and return the final "
        "JSON object immediately. Keep the answer concise."
    )
    warnings: list[str] = []
    chat = getattr(getattr(api, "chat", None), "completions", None)
    create = getattr(chat, "create", None)
    if not callable(create):
        return None, ["OpenAI client does not support targeted chat recovery."], 0

    for attempt in range(1, attempts + 1):
        request = build_chat_completion_request(recovery_prompt, model_name)
        request["reasoning_effort"] = effort
        request["max_completion_tokens"] = max_tokens
        logger.warning(
            "batch_recovery custom_id=%s attempt=%d/%d status=started "
            "reasoning_effort=%s max_completion_tokens=%d",
            custom_id,
            attempt,
            attempts,
            effort,
            max_tokens,
        )
        try:
            response = create(**request)
            _accumulate_chat_response_usage(usage, response)
            choices = _get_value(response, "choices") or []
            if not choices:
                raise ValueError("Recovery response contains no choices.")
            choice = choices[0]
            finish_reason = str(_get_value(choice, "finish_reason", "") or "")
            if finish_reason == "length":
                raise ValueError("Recovery response was truncated.")
            message = _get_value(choice, "message") or {}
            content = _get_value(message, "content")
            parse_ai_response(content)
            logger.warning(
                "batch_recovery custom_id=%s attempt=%d/%d status=completed",
                custom_id,
                attempt,
                attempts,
            )
            return content, warnings, attempt
        except Exception as exc:
            detail = f"Recovery attempt {attempt}/{attempts} failed: {type(exc).__name__}: {exc}"
            warnings.append(detail)
            logger.warning(
                "batch_recovery custom_id=%s attempt=%d/%d status=failed error=%s:%s",
                custom_id,
                attempt,
                attempts,
                type(exc).__name__,
                exc,
            )
    return None, warnings, attempts


async def _recover_invalid_flat_ner(
    api: Any,
    *,
    state: ODRLCorrectionState,
    prompt: str,
    validation_error: str,
    model_name: str,
    custom_id: str,
    usage: dict[str, int],
    attempts_override: int | None = None,
) -> tuple[dict[str, Any] | None, Any | None, list[str], int]:
    """Retry only a semantically invalid flat-NER answer and revalidate it."""
    enabled = str(
        os.getenv("ODRL_CORRECTION_RECOVER_INVALID_NER", "true")
    ).strip().lower() in {"1", "true", "yes", "on"}
    if not enabled:
        return None, None, ["Invalid flat-NER recovery is disabled."], 0
    chat = getattr(getattr(api, "chat", None), "completions", None)
    create = getattr(chat, "create", None)
    if not callable(create):
        return None, None, ["OpenAI client does not support flat-NER recovery."], 0

    attempts = (
        attempts_override
        if attempts_override is not None
        else _positive_int_env("ODRL_CORRECTION_INVALID_NER_ATTEMPTS", 3)
    )
    if attempts < 1:
        raise ValueError("attempts_override must be positive")
    max_tokens = _positive_int_env(
        "ODRL_CORRECTION_INVALID_NER_MAX_OUTPUT_TOKENS", 16000
    )
    effort = str(
        os.getenv("ODRL_CORRECTION_INVALID_NER_REASONING_EFFORT", "medium")
    ).strip().lower()
    if effort not in {"none", "low", "medium", "high", "xhigh", "max"}:
        raise ValueError(
            "ODRL_CORRECTION_INVALID_NER_REASONING_EFFORT must be one of: "
            "high, low, max, medium, none, xhigh"
        )

    warnings: list[str] = [
        f"Initial Batch annotation failed flat-NER validation and was retried: "
        f"{validation_error}"
    ]
    for attempt in range(1, attempts + 1):
        request = build_flat_ner_recovery_request(
            prompt,
            validation_error,
            model_name,
            reasoning_effort=effort,
            max_output_tokens=max_tokens,
        )
        logger.warning(
            "flat_ner_recovery custom_id=%s attempt=%d/%d status=started",
            custom_id,
            attempt,
            attempts,
        )
        try:
            response = create(**request)
            _accumulate_chat_response_usage(usage, response)
            choices = _get_value(response, "choices") or []
            if not choices:
                raise ValueError("Recovery response contains no choices.")
            choice = choices[0]
            if str(_get_value(choice, "finish_reason", "") or "") == "length":
                raise ValueError("Recovery response was truncated.")
            content = _get_value(_get_value(choice, "message") or {}, "content")
            payload = parse_ai_response(content)
            raw_entities = payload.get("corrected_entities")
            if not isinstance(raw_entities, list):
                raise ValueError("Recovery response has no corrected_entities list.")
            source_text = str(state.get("source_text") or "")
            entities: list[dict[str, Any]] = []
            offset_adjustments: list[str] = []
            for entity_index, raw in enumerate(raw_entities, start=1):
                if not isinstance(raw, dict):
                    raise ValueError(f"recovery entity {entity_index} is not an object")
                start = int(raw.get("start"))
                end = int(raw.get("end"))
                quoted = str(raw.get("text") or "")
                if not 0 <= start < end <= len(source_text):
                    start = end = -1
                if start < 0 or source_text[start:end] != quoted:
                    # Models are much better at quoting a component than at
                    # counting long-string character offsets. Relocate only an
                    # exact, case-sensitive quote and choose the occurrence
                    # nearest the proposed start. The ordinary overlap and
                    # semantic checks still run below.
                    matches: list[tuple[int, int]] = []
                    cursor = 0
                    while quoted and cursor <= len(source_text) - len(quoted):
                        found = source_text.find(quoted, cursor)
                        if found < 0:
                            break
                        matches.append((found, found + len(quoted)))
                        cursor = found + 1
                    if not matches:
                        raise ValueError(
                            f"recovery entity {entity_index} text is not an exact SOURCE quote"
                        )
                    proposed_start = int(raw.get("start") or 0)
                    start, end = min(
                        matches,
                        key=lambda span: (abs(span[0] - proposed_start), span[0]),
                    )
                    offset_adjustments.append(
                        f"entity {entity_index} relocated to exact SOURCE offsets "
                        f"[{start}, {end})"
                    )
                entities.append({
                    "start": start,
                    "end": end,
                    "label": str(raw.get("label") or ""),
                })
            entities = validate_flat_ner_entities(source_text, entities)
            rules = normalize_rules(payload["validated_policy_rules"], source_text)
            entity_quotes = {
                (entity["label"], source_text[entity["start"]:entity["end"]])
                for entity in entities
            }
            component_labels = {
                "assignee": "ASSIGNEE",
                "action": "ACTION",
                "asset": "ASSET",
                "constraint": "CONSTRAINT",
                "purpose": "PURPOSE",
            }
            for rule_index, rule in enumerate(rules, start=1):
                if rule.get("rule_type") and rule.get("rule_type") not in {
                    "permission", "obligation", "prohibition",
                }:
                    raise ValueError(
                        f"recovery policy rule {rule_index} has invalid rule_type"
                    )
                for field, label in component_labels.items():
                    quote = str(rule.get(field) or "")
                    if quote and (label, quote) not in entity_quotes:
                        raise ValueError(
                            f"recovery policy rule {rule_index} {field} has no "
                            "matching corrected entity"
                        )
                if rule.get("rule_type"):
                    rule_label = f"RULE_TYPE-{str(rule['rule_type']).upper()}"
                    if not any(entity["label"] == rule_label for entity in entities):
                        raise ValueError(
                            f"recovery policy rule {rule_index} has no matching rule marker entity"
                        )
                rule["policy_rule_id"] = f"policy-rule-{rule_index}"
                rule["selected_from"] = "ai_reconciliation"
            _validate_recovery_alignment(source_text, rules, entities)
            retry_state = dict(state)
            retry_state.update({
                "validated_policy_rules": rules,
                "ai_rules": rules,
                "selected_from": "ai_reconciliation",
                "corrected_entities": entities,
                "grounding_warnings": [],
                "correction_warnings": [],
                "correction_comparison": compare_entity_sets(
                    list(state.get("original_entities") or []), entities
                ),
                "flat_ner_validated": True,
                "overlap_count": 0,
                "allow_partial_rules": True,
            })
            validation = await node_flat_ner_validate(retry_state)
            update = {
                key: retry_state[key]
                for key in (
                    "validated_policy_rules", "ai_rules", "selected_from",
                    "corrected_entities", "grounding_warnings",
                    "correction_warnings", "correction_comparison",
                    "flat_ner_validated", "overlap_count",
                    "allow_partial_rules",
                )
            }
            update.update(validation)
            if offset_adjustments:
                warnings.append(
                    "Recovery offsets were deterministically corrected: "
                    + "; ".join(offset_adjustments)
                )
            logger.warning(
                "flat_ner_recovery custom_id=%s attempt=%d/%d status=completed",
                custom_id,
                attempt,
                attempts,
            )
            return update, content, warnings, attempt
        except Exception as exc:
            detail = (
                f"Flat-NER recovery attempt {attempt}/{attempts} failed: "
                f"{type(exc).__name__}: {exc}"
            )
            warnings.append(detail)
            logger.warning(
                "flat_ner_recovery custom_id=%s attempt=%d/%d status=failed "
                "error=%s:%s",
                custom_id,
                attempt,
                attempts,
                type(exc).__name__,
                exc,
            )
    return None, None, warnings, attempts


async def finalize_batch_job(
    manifest_path: str | Path,
    *,
    strict: bool = True,
    client: Any = None,
    recovery_policy: str = "synchronous",
    synchronous_recovery_limit: int | None = None,
    reuse_downloaded_results: bool = False,
) -> tuple[list[Path], list[Path], list[ODRLCorrectionState]]:
    """Download Batch results, reconcile them, and write all split outputs."""
    if recovery_policy not in {
        "synchronous", "defer", "batch_only", "batch_then_sync"
    }:
        raise ValueError(
            "recovery_policy must be synchronous, defer, batch_only, or batch_then_sync"
        )
    if synchronous_recovery_limit is not None and synchronous_recovery_limit < 0:
        raise ValueError("synchronous_recovery_limit cannot be negative")
    path, manifest = _read_manifest(manifest_path)
    results_path = Path(str(manifest["results_path"]))
    api = client
    if not (reuse_downloaded_results and results_path.is_file()):
        api = api or _create_client()
        if manifest.get("status") != "completed" or not manifest.get("output_file_id"):
            manifest = refresh_batch_status(path, client=api)
        if manifest.get("status") != "completed":
            raise RuntimeError(
                f"Batch {manifest.get('batch_id')} is {manifest.get('status')}; "
                "finalize only after it is completed."
            )
    _verify_artifact_integrity(manifest)
    if not (reuse_downloaded_results and results_path.is_file()):
        _download_batch_files(path, manifest, api)

    result_records = _read_jsonl(results_path)
    results_by_id: dict[str, dict[str, Any]] = {}
    for result in result_records:
        custom_id = str(result.get("custom_id") or "")
        if not custom_id:
            raise ValueError("A Batch output line has no custom_id.")
        if custom_id in results_by_id:
            raise ValueError(f"Duplicate Batch output custom_id: {custom_id}")
        results_by_id[custom_id] = result

    state_records = _read_jsonl(Path(str(manifest["states_path"])))
    expected_ids = [str(item.get("custom_id") or "") for item in state_records]
    if any(not custom_id for custom_id in expected_ids):
        raise ValueError("A persisted Batch state has no custom_id.")
    if len(set(expected_ids)) != len(expected_ids):
        raise ValueError("Persisted Batch states contain duplicate custom_id values.")
    request_count = int(manifest.get("request_count") or 0)
    if len(expected_ids) != request_count:
        raise RuntimeError(
            f"Manifest expects {request_count} records but states.jsonl contains "
            f"{len(expected_ids)}."
        )
    unexpected_ids = sorted(set(results_by_id) - set(expected_ids))
    if unexpected_ids:
        preview = ", ".join(unexpected_ids[:20])
        suffix = "" if len(unexpected_ids) <= 20 else ", ..."
        raise RuntimeError(
            "Batch output contains custom_id values not present in the saved "
            f"input state: {preview}{suffix}"
        )
    prompt_template = Path(str(manifest["prompt_snapshot_path"])).read_text(
        encoding="utf-8"
    )
    split_states: dict[str, list[ODRLCorrectionState]] = {
        str(item["split"]): [] for item in manifest.get("splits") or []
    }
    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "reasoning_tokens": 0,
        "total_tokens": 0,
    }
    failures: list[str] = []
    recovery_count = 0
    flat_ner_recovery_count = 0
    recovery_attempt_count = 0
    recovered_custom_ids: list[str] = []
    synchronous_recovery_records = 0
    deferred_recoveries: list[dict[str, Any]] = []
    manual_review_records: list[dict[str, Any]] = []
    deferred_path = path.parent / "deferred_recovery.jsonl"
    batch_recovery_path = path.parent / "batch_recovery_responses.jsonl"
    batch_recovery_responses = {
        str(item.get("custom_id") or ""): item
        for item in (
            _read_jsonl(batch_recovery_path) if batch_recovery_path.is_file() else []
        )
        if item.get("custom_id")
    }
    flat_recovery_cache_path = path.parent / "flat_ner_recovery_cache.jsonl"
    flat_recovery_cache = {
        str(item.get("custom_id") or ""): item
        for item in (
            _read_jsonl(flat_recovery_cache_path)
            if flat_recovery_cache_path.is_file()
            else []
        )
        if item.get("custom_id")
    }

    for state_record in state_records:
        custom_id = str(state_record.get("custom_id") or "")
        split = str(state_record.get("split") or "")
        stored = state_record.get("state") or {}
        result = results_by_id.get(custom_id)
        error = _batch_result_error(result)
        override: Any = None
        recovered: Any = None
        if result is not None:
            # Count paid Batch usage even when the result is unusable. This is
            # especially important for a 128k reasoning-only truncation.
            _accumulate_usage(usage, result)
        recovery_warnings: list[str] = []
        if (
            error
            and _retryable_batch_result_error(error)
            and recovery_policy == "synchronous"
            and (
                synchronous_recovery_limit is None
                or synchronous_recovery_records < synchronous_recovery_limit
            )
        ):
            source_text = str(stored.get("source_text") or "")
            endpoint_rules = normalize_endpoint_rules(
                stored.get("endpoint_rules"), source_text
            )
            retry_prompt = render_correction_prompt(
                prompt_template,
                source_text,
                list(stored.get("original_entities") or []),
                endpoint_rules,
                list(stored.get("duplicate_original_variants") or []),
            )
            # Finalization already performs synchronous SDK file/status calls.
            # Keep this exceptional one-record call synchronous as well; using
            # a default executor here can delay IsolatedAsyncio loop teardown.
            recovered, recovery_warnings, attempts_used = _recover_batch_response(
                api,
                prompt=retry_prompt,
                model_name=str(stored.get("model_name") or manifest["model_name"]),
                custom_id=custom_id,
                usage=usage,
            )
            recovery_attempt_count += attempts_used
            if attempts_used:
                synchronous_recovery_records += 1
            if recovered is not None:
                override = recovered
                recovery_count += 1
                recovered_custom_ids.append(custom_id)
                error = ""
        if error:
            detail = error
            if recovery_warnings:
                detail += " " + " ".join(recovery_warnings)
            failures.append(f"{custom_id}: {detail}")
            if strict and recovery_policy == "synchronous":
                continue
            override: Any = {"validated_policy_rules": []}
        else:
            if recovered is None:
                assert result is not None
                body = ((result.get("response") or {}).get("body") or {})
                override = body["choices"][0]["message"]["content"]

        input_record = stored.get("input_record") or {}
        state = create_correction_state(input_record)
        state.update(stored)
        state["prompt_template"] = prompt_template
        state["ai_response_override"] = override
        if recovery_warnings:
            state["correction_warnings"] = list(
                state.get("correction_warnings") or []
            ) + recovery_warnings
        if error:
            state["correction_warnings"] = list(
                state.get("correction_warnings") or []
            ) + [error]
        correction_update = await node_odrl_correct(state)
        reconciliation_error = ""
        if correction_update.get("selected_from") != "ai_reconciliation":
            warnings = correction_update.get("correction_warnings") or []
            reconciliation_error = (
                str(warnings[-1]) if warnings else "AI reconciliation fallback used."
            )
            if strict and recovery_policy == "synchronous":
                failures.append(f"{custom_id}: {reconciliation_error}")
                continue
        state.update(correction_update)
        try:
            if error or reconciliation_error:
                raise ValueError(error or reconciliation_error)
            state.update(await node_flat_ner_validate(state))
        except Exception as exc:
            validation_error = f"{type(exc).__name__}: {exc}"
            cached_recovery = flat_recovery_cache.get(custom_id)
            recovered_update = None
            recovered_override = None
            validation_warnings: list[str] = []
            attempts_used = 0
            if cached_recovery:
                candidate = dict(cached_recovery.get("update") or {})
                candidate_state = dict(state)
                candidate_state.update(candidate)
                try:
                    _validate_recovery_alignment(
                        str(candidate_state.get("source_text") or ""),
                        list(candidate_state.get("validated_policy_rules") or []),
                        list(candidate_state.get("corrected_entities") or []),
                    )
                    candidate.update(await node_flat_ner_validate(candidate_state))
                    recovered_update = candidate
                    recovered_override = cached_recovery.get("response")
                    validation_warnings = [
                        "Reused a previously validated flat-NER recovery checkpoint."
                    ]
                    logger.warning(
                        "flat_ner_recovery custom_id=%s status=cache_hit",
                        custom_id,
                    )
                except Exception as cache_exc:
                    logger.warning(
                        "flat_ner_recovery custom_id=%s status=cache_invalid error=%s:%s",
                        custom_id,
                        type(cache_exc).__name__,
                        cache_exc,
                    )
                    flat_recovery_cache.pop(custom_id, None)
            if recovered_update is None:
                recovery_prompt = render_correction_prompt(
                    prompt_template,
                    str(state.get("source_text") or ""),
                    list(state.get("original_entities") or []),
                    normalize_endpoint_rules(
                        state.get("endpoint_rules"),
                        str(state.get("source_text") or ""),
                    ),
                    list(state.get("duplicate_original_variants") or []),
                )
                batch_item = batch_recovery_responses.get(custom_id)
                if batch_item and batch_item.get("content"):
                    content = batch_item["content"]

                    class _StaticCompletions:
                        def create(self, **_: Any) -> dict[str, Any]:
                            return {
                                "choices": [{
                                    "message": {"content": content},
                                    "finish_reason": "stop",
                                }]
                            }

                    class _StaticAPI:
                        chat = type("Chat", (), {"completions": _StaticCompletions()})()

                    recovered_update, recovered_override, validation_warnings, _ = (
                        await _recover_invalid_flat_ner(
                            _StaticAPI(),
                            state=state,
                            prompt=recovery_prompt,
                            validation_error=validation_error,
                            model_name=str(stored.get("model_name") or manifest["model_name"]),
                            custom_id=custom_id,
                            usage=usage,
                            attempts_override=1,
                        )
                    )
                    attempts_used = 0
                if recovered_update is None and recovery_policy in {
                    "synchronous", "batch_then_sync"
                } and (
                    synchronous_recovery_limit is None
                    or synchronous_recovery_records < synchronous_recovery_limit
                ):
                    recovered_update, recovered_override, validation_warnings, attempts_used = (
                        await _recover_invalid_flat_ner(
                            api,
                            state=state,
                            prompt=recovery_prompt,
                            validation_error=validation_error,
                            model_name=str(stored.get("model_name") or manifest["model_name"]),
                            custom_id=custom_id,
                            usage=usage,
                        )
                    )
                    if attempts_used:
                        synchronous_recovery_records += 1
                elif recovery_policy == "defer":
                    effort = str(os.getenv(
                        "ODRL_CORRECTION_BATCH_RECOVERY_REASONING_EFFORT", "medium"
                    )).strip().lower()
                    max_tokens = _positive_int_env(
                        "ODRL_CORRECTION_BATCH_RECOVERY_MAX_OUTPUT_TOKENS", 16000
                    )
                    deferred_recoveries.append({
                        "custom_id": custom_id,
                        "validation_error": validation_error,
                        "state": stored,
                        "request": {
                            "custom_id": custom_id,
                            "method": "POST",
                            "url": "/v1/chat/completions",
                            "body": build_flat_ner_recovery_request(
                                recovery_prompt,
                                validation_error,
                                str(stored.get("model_name") or manifest["model_name"]),
                                reasoning_effort=effort,
                                max_output_tokens=max_tokens,
                            ),
                        },
                    })
            recovery_attempt_count += attempts_used
            if recovered_update is not None:
                flat_recovery_cache[custom_id] = {
                    "custom_id": custom_id,
                    "response": recovered_override,
                    "update": recovered_update,
                }
                _write_jsonl_atomic(
                    flat_recovery_cache_path,
                    flat_recovery_cache.values(),
                )
                state.update(recovered_update)
                override = recovered_override
                recovery_count += 1
                flat_ner_recovery_count += 1
                if custom_id not in recovered_custom_ids:
                    recovered_custom_ids.append(custom_id)
                state["correction_warnings"] = list(
                    state.get("correction_warnings") or []
                ) + validation_warnings
            else:
                detail = validation_error
                if validation_warnings:
                    detail += " " + " ".join(validation_warnings)
                if recovery_policy == "synchronous":
                    failures.append(f"{custom_id}: {detail}")
                if strict and recovery_policy == "synchronous":
                    continue
                original_entities = [
                    dict(entity) for entity in state.get("original_entities") or []
                ]
                original_odrl = _original_odrl_record_from_state(state)
                state.update({
                    "corrected_entities": original_entities,
                    "validated_policy_rules": [
                        dict(rule) for rule in original_odrl.get("odrl") or []
                    ],
                    "ai_rules": [],
                    "selected_from": "original_manual_review",
                    "flat_ner_validated": False,
                    "overlap_count": 0,
                })
                warning = f"flat NER validation failed; original labels retained: {detail}"
                state["correction_warnings"] = list(
                    state.get("correction_warnings") or []
                ) + [warning]
                manual_review_records.append({
                    "custom_id": custom_id,
                    "text": str(state.get("source_text") or ""),
                    "original_entities": original_entities,
                    "reason": detail,
                    "recovery_status": (
                        "queued_for_batch" if recovery_policy == "defer"
                        else "batch_recovery_failed"
                    ),
                })

        occurrences = state_record.get("occurrences") or [{
            "split": split,
            "record_index": int(stored.get("record_index") or 0),
            "record_total": int(stored.get("record_total") or 0),
            "dataset_path": str(stored.get("dataset_path") or ""),
            "input_record": input_record,
        }]
        for occurrence in occurrences:
            occurrence_record = dict(occurrence.get("input_record") or {})
            expanded = create_correction_state(occurrence_record)
            expanded.update(stored)
            expanded.update({
                "input_record": occurrence_record,
                "source_text": str(occurrence_record.get("text") or ""),
                "original_entities": [
                    dict(entity) for entity in occurrence_record.get("entities") or []
                ],
                "record_index": int(occurrence.get("record_index") or 0),
                "record_total": int(occurrence.get("record_total") or 0),
                "dataset_path": str(occurrence.get("dataset_path") or ""),
                "prompt_template": prompt_template,
                "ai_response_override": override,
                "validated_policy_rules": [
                    dict(rule) for rule in state.get("validated_policy_rules") or []
                ],
                "corrected_entities": [
                    dict(entity) for entity in state.get("corrected_entities") or []
                ],
                "selected_from": state.get("selected_from"),
                "correction_warnings": list(state.get("correction_warnings") or []),
                "flat_ner_validated": state.get("flat_ner_validated", False),
                "overlap_count": state.get("overlap_count", 0),
                "duplicate_gold_custom_id": custom_id,
                "duplicate_group_size": len(occurrences),
                "original_odrl_record": occurrence.get("original_odrl_record"),
            })
            expanded["correction_comparison"] = compare_entity_sets(
                list(expanded.get("original_entities") or []),
                list(expanded.get("corrected_entities") or []),
            )
            expanded.update(await node_odrl_output(expanded))
            split_states.setdefault(str(occurrence.get("split") or split), []).append(
                expanded
            )
        logger.info(
            "batch_finalize custom_id=%s status=completed selected_from=%s "
            "expanded_records=%d warnings=%d",
            custom_id,
            state.get("selected_from") or "",
            len(occurrences),
            len(state.get("correction_warnings") or []),
        )

    if failures and strict and recovery_policy == "synchronous":
        preview = "\n".join(failures[:20])
        suffix = "" if len(failures) <= 20 else f"\n... and {len(failures) - 20} more"
        raise RuntimeError(
            "Batch finalization stopped to protect dataset quality. "
            "Fix or resubmit the failed records:\n" + preview + suffix
        )

    gold_by_text: dict[str, tuple[tuple[int, int, str], ...]] = {}
    for states in split_states.values():
        for expanded in states:
            text_value = str(expanded.get("source_text") or "")
            signature = tuple(
                (int(entity["start"]), int(entity["end"]), str(entity["label"]))
                for entity in expanded.get("corrected_entities") or []
            )
            previous = gold_by_text.setdefault(text_value, signature)
            if previous != signature:
                raise RuntimeError(
                    "Duplicate-gold invariant failed: identical source text received "
                    "different corrected entities. No datasets were written."
                )

    output_dir = Path(str(manifest["output_dir"]))
    model_suffix = _safe_model_name(str(manifest["model_name"]))
    ner_paths: list[Path] = []
    odrl_paths: list[Path] = []
    diff_paths: list[Path] = []
    odrl_diff_paths: list[Path] = []
    all_states: list[ODRLCorrectionState] = []
    for split_info in manifest.get("splits") or []:
        split = str(split_info["split"])
        states = sorted(
            split_states.get(split) or [],
            key=lambda item: int(item.get("record_index") or 0),
        )
        expected_count = int(split_info.get("record_count") or 0)
        if len(states) != expected_count:
            raise RuntimeError(
                f"Expanded split {split} has {len(states)} records; expected "
                f"{expected_count}. No partial dataset should be trusted."
            )
        ner_path = output_dir / f"{split}_correct_with_agent_{model_suffix}.txt"
        odrl_path = output_dir / f"{split}_odrl_with_agent_{model_suffix}.txt"
        diff_path = output_dir / f"{split}_diffs_from_correct_{model_suffix}.txt"
        odrl_diff_path = output_dir / f"{split}_odrl_diffs_from_correct_{model_suffix}.txt"
        _write_jsonl_atomic(ner_path, (state["corrected_record"] for state in states))
        _write_jsonl_atomic(odrl_path, (state["text_odrl_record"] for state in states))
        for state in states:
            original_odrl_record = dict(
                state.get("original_odrl_record")
                or _original_odrl_record_from_state(state)
            )
            state["original_odrl_record"] = original_odrl_record
            state["corrected_odrl_record"] = dict(state["text_odrl_record"] or {})
            state["odrl_diff_record"] = build_odrl_diff_record(state)
        changed_states = [
            state
            for state in states
            if (state.get("diff_record") or {}).get("diffs", {}).get("has_changes")
        ]
        _write_jsonl_atomic(
            diff_path,
            (state["diff_record"] for state in changed_states),
        )
        for state in states:
            state["diff_output_path"] = str(diff_path)
        changed_odrl_states = [
            state
            for state in states
            if (state.get("odrl_diff_record") or {}).get("diffs", {}).get("has_changes")
        ]
        _write_jsonl_atomic(
            odrl_diff_path,
            (state["odrl_diff_record"] for state in changed_odrl_states),
        )
        for state in states:
            state["odrl_diff_output_path"] = str(odrl_diff_path)
        ner_paths.append(ner_path)
        odrl_paths.append(odrl_path)
        diff_paths.append(diff_path)
        odrl_diff_paths.append(odrl_diff_path)
        all_states.extend(states)

    if deferred_recoveries:
        _write_jsonl_atomic(deferred_path, deferred_recoveries)
    elif deferred_path.is_file() and recovery_policy == "defer":
        _write_jsonl_atomic(deferred_path, [])
    manual_review_path = path.parent / "manual_review.jsonl"
    _write_jsonl_atomic(manual_review_path, manual_review_records)
    manifest["status"] = (
        "finalized_pending_recovery" if deferred_recoveries else "finalized"
    )
    manifest["finalized_at"] = datetime.now(timezone.utc).isoformat()
    manifest["usage"] = usage
    manifest["fallback_count"] = len(failures)
    manifest["recovery_count"] = recovery_count
    manifest["flat_ner_recovery_count"] = flat_ner_recovery_count
    manifest["recovery_attempt_count"] = recovery_attempt_count
    manifest["synchronous_recovery_records"] = synchronous_recovery_records
    manifest["deferred_recovery_count"] = len(deferred_recoveries)
    manifest["deferred_recovery_path"] = str(deferred_path)
    manifest["manual_review_count"] = len(manual_review_records)
    manifest["manual_review_path"] = str(manual_review_path)
    manifest["recovered_custom_ids"] = recovered_custom_ids
    manifest["flat_ner_recovery_cache_path"] = str(flat_recovery_cache_path)
    manifest["expanded_record_count"] = len(all_states)
    manifest["duplicate_gold_verified"] = True
    manifest["flat_ner_validation"] = {
        "required": True,
        "validated_record_count": sum(
            bool(state.get("flat_ner_validated")) for state in all_states
        ),
        "manual_review_record_count": sum(
            not bool(state.get("flat_ner_validated")) for state in all_states
        ),
        "remaining_overlap_count": sum(
            not bool(state.get("flat_ner_validated")) for state in all_states
        ),
    }
    manifest["ner_outputs"] = [str(item) for item in ner_paths]
    manifest["odrl_outputs"] = [str(item) for item in odrl_paths]
    manifest["diff_outputs"] = [str(item) for item in diff_paths]
    manifest["odrl_diff_outputs"] = [str(item) for item in odrl_diff_paths]
    _write_json_atomic(path, manifest)
    logger.info(
        "batch_finalize status=completed records=%d unique_requests=%d "
        "failures=%d usage=%s",
        len(all_states),
        request_count,
        len(failures),
        usage,
    )
    return ner_paths, odrl_paths, all_states
