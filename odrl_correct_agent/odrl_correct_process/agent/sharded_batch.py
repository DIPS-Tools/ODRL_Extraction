"""Sequential, resumable Batch sharding for queued prompt-token limits."""

from __future__ import annotations

import json
import math
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from odrl_correct_agent.odrl_correct_process.agent.batch_processing import (
    BATCH_SCHEMA_VERSION,
    _assert_finalized_outputs_exist,
    _accumulate_usage,
    _batch_result_error,
    _create_client,
    _download_batch_files,
    _read_jsonl,
    _read_manifest,
    _safe_model_name,
    _sha256_file,
    _verify_artifact_integrity,
    _write_json_atomic,
    _write_jsonl_atomic,
    build_flat_ner_recovery_request,
    finalize_batch_job,
    refresh_batch_status,
    submit_batch_job,
    watch_and_finalize_batch_job,
)


OUTPUT_GROUPS = (
    ("ner_outputs", "correct_with_agent"),
    ("odrl_outputs", "odrl_with_agent"),
    ("diff_outputs", "diffs_from_correct"),
    ("odrl_diff_outputs", "odrl_diffs_from_correct"),
)


def _prepare_recovery_batch(
    parent_path: Path,
    shard_paths: list[Path],
) -> Path | None:
    """Combine all deferred failures into one discounted recovery Batch."""
    _, parent = _read_manifest(parent_path)
    queued: list[dict[str, Any]] = []
    for shard_path in shard_paths:
        _, shard = _read_manifest(shard_path)
        queue_path = Path(str(shard.get("deferred_recovery_path") or ""))
        if queue_path.is_file():
            for item in _read_jsonl(queue_path):
                item["shard_manifest_path"] = str(shard_path)
                queued.append(item)
    if not queued:
        return None

    effort = str(os.getenv(
        "ODRL_CORRECTION_BATCH_RECOVERY_REASONING_EFFORT", "medium"
    )).strip().lower()
    max_tokens = int(os.getenv(
        "ODRL_CORRECTION_BATCH_RECOVERY_MAX_OUTPUT_TOKENS", "16000"
    ))
    for item in queued:
        old_request = dict(item.get("request") or {})
        old_body = dict(old_request.get("body") or {})
        messages = list(old_body.get("messages") or [])
        old_content = str((messages[0] if messages else {}).get("content") or "")
        base_prompt = old_content.split("\n\nFLAT-NER RECOVERY:", 1)[0]
        model_name = str(old_body.get("model") or parent["model_name"])
        item["request"] = {
            "custom_id": str(item["custom_id"]),
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": build_flat_ner_recovery_request(
                base_prompt,
                str(item.get("validation_error") or ""),
                model_name,
                reasoning_effort=effort,
                max_output_tokens=max_tokens,
            ),
        }

    recovery_dir = parent_path.parent / "recovery_batch"
    recovery_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = recovery_dir / "manifest.json"
    if manifest_path.is_file():
        _, existing = _read_manifest(manifest_path)
        if existing.get("batch_id"):
            return manifest_path
    requests_path = recovery_dir / "requests.jsonl"
    states_path = recovery_dir / "states.jsonl"
    prompt_path = recovery_dir / "odrl_extraction.prompt"
    shutil.copyfile(Path(str(parent["prompt_snapshot_path"])), prompt_path)
    _write_jsonl_atomic(requests_path, (dict(item["request"]) for item in queued))
    _write_jsonl_atomic(
        states_path,
        ({key: value for key, value in item.items() if key != "request"} for item in queued),
    )
    manifest = {
        "schema_version": BATCH_SCHEMA_VERSION,
        "job_id": f"{parent.get('job_id')}_recovery",
        "job_type": "flat_ner_recovery",
        "status": "prepared",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "parent_manifest_path": str(parent_path),
        "model_name": parent["model_name"],
        "request_count": len(queued),
        "requests_path": str(requests_path),
        "states_path": str(states_path),
        "prompt_snapshot_path": str(prompt_path),
        "results_path": str(recovery_dir / "results.jsonl"),
        "errors_path": str(recovery_dir / "errors.jsonl"),
        "output_dir": str(recovery_dir / "outputs"),
        "splits": [],
        "artifact_sha256": {
            "requests": _sha256_file(requests_path),
            "states": _sha256_file(states_path),
            "prompt": _sha256_file(prompt_path),
        },
    }
    _write_json_atomic(manifest_path, manifest)
    parent["recovery_manifest_path"] = str(manifest_path)
    parent["recovery_request_count"] = len(queued)
    parent["status"] = "recovery_prepared"
    _write_json_atomic(parent_path, parent)
    return manifest_path


async def _run_recovery_batch(
    recovery_path: Path,
    *,
    api: Any,
    poll_interval_seconds: float,
    timeout_hours: float,
) -> None:
    """Submit one recovery Batch and distribute its responses to source shards."""
    _, recovery = _read_manifest(recovery_path)
    if not recovery.get("batch_id"):
        recovery = submit_batch_job(recovery_path, client=api)
    started = datetime.now(timezone.utc)
    while str(recovery.get("status") or "") != "completed":
        status = str(recovery.get("status") or "")
        if status in {"failed", "expired", "cancelled"}:
            raise RuntimeError(
                f"Recovery Batch {recovery.get('batch_id')} ended with {status}."
            )
        elapsed = (datetime.now(timezone.utc) - started).total_seconds()
        if elapsed >= timeout_hours * 3600:
            raise TimeoutError(
                "Recovery Batch watcher timed out locally; resume the parent manifest."
            )
        await __import__("asyncio").sleep(poll_interval_seconds)
        recovery = refresh_batch_status(recovery_path, client=api)

    _download_batch_files(recovery_path, recovery, api)
    results = {
        str(item.get("custom_id") or ""): item
        for item in _read_jsonl(Path(str(recovery["results_path"])))
    }
    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "reasoning_tokens": 0,
        "total_tokens": 0,
    }
    for result in results.values():
        _accumulate_usage(usage, result)
    queued = _read_jsonl(Path(str(recovery["states_path"])))
    by_shard: dict[str, list[dict[str, Any]]] = {}
    failed: list[dict[str, Any]] = []
    for item in queued:
        custom_id = str(item.get("custom_id") or "")
        result = results.get(custom_id)
        error = _batch_result_error(result)
        if error:
            failed.append({"custom_id": custom_id, "error": error})
            continue
        body = ((result or {}).get("response") or {}).get("body") or {}
        content = body["choices"][0]["message"]["content"]
        by_shard.setdefault(str(item["shard_manifest_path"]), []).append({
            "custom_id": custom_id,
            "content": content,
        })
    for shard, records in by_shard.items():
        _write_jsonl_atomic(Path(shard).parent / "batch_recovery_responses.jsonl", records)
    failed_path = recovery_path.parent / "failed_recovery_responses.jsonl"
    _write_jsonl_atomic(failed_path, failed)
    _, recovery = _read_manifest(recovery_path)
    recovery["status"] = "distributed"
    recovery["distributed_at"] = datetime.now(timezone.utc).isoformat()
    recovery["successful_response_count"] = sum(len(items) for items in by_shard.values())
    recovery["failed_response_count"] = len(failed)
    recovery["failed_responses_path"] = str(failed_path)
    recovery["usage"] = usage
    _write_json_atomic(recovery_path, recovery)


def _estimated_prompt_tokens(request: dict[str, Any]) -> int:
    """Conservatively estimate English prompt tokens without extra packages."""
    messages = (request.get("body") or {}).get("messages") or []
    characters = sum(len(str(message.get("content") or "")) for message in messages)
    # Legal English is commonly above three characters/token. Dividing by two
    # deliberately overestimates and leaves room for message framing tokens.
    return max(1, math.ceil(characters / 2) + 32 * len(messages) + 32)


def _partition_indices(
    requests: list[dict[str, Any]],
    maximum_tokens: int,
) -> list[tuple[int, int, int]]:
    if maximum_tokens <= 0:
        raise ValueError("Shard maximum prompt tokens must be greater than zero.")
    partitions: list[tuple[int, int, int]] = []
    start = 0
    running = 0
    for index, request in enumerate(requests):
        estimate = _estimated_prompt_tokens(request)
        if estimate > maximum_tokens:
            raise ValueError(
                f"Request {request.get('custom_id')!r} is estimated at {estimate} "
                f"prompt tokens, above the shard maximum {maximum_tokens}."
            )
        if index > start and running + estimate > maximum_tokens:
            partitions.append((start, index, running))
            start = index
            running = 0
        running += estimate
    if start < len(requests):
        partitions.append((start, len(requests), running))
    return partitions


def prepare_batch_shards(
    parent_manifest_path: str | Path,
    *,
    maximum_prompt_tokens: int | None = None,
) -> list[Path]:
    """Split a prepared/failed manifest into resumable local shard manifests."""
    parent_path, parent = _read_manifest(parent_manifest_path)
    recorded = [Path(str(value)) for value in parent.get("shard_manifests") or []]
    if recorded:
        missing = [str(path) for path in recorded if not path.is_file()]
        if missing:
            raise FileNotFoundError("Recorded shard manifests are missing: " + ", ".join(missing))
        return recorded

    _verify_artifact_integrity(parent)
    requests = _read_jsonl(Path(str(parent["requests_path"])))
    states = _read_jsonl(Path(str(parent["states_path"])))
    if len(requests) != len(states):
        raise RuntimeError("Batch requests and persisted states have different lengths.")
    for request, state in zip(requests, states):
        if request.get("custom_id") != state.get("custom_id"):
            raise RuntimeError("Batch requests and states are not in identical custom_id order.")

    limit = int(
        maximum_prompt_tokens
        if maximum_prompt_tokens is not None
        else os.getenv("ODRL_BATCH_SHARD_MAX_PROMPT_TOKENS", "1500000")
    )
    partitions = _partition_indices(requests, limit)
    shard_root = parent_path.parent / "shards"
    shard_root.mkdir(parents=True, exist_ok=True)
    source_splits = {
        str(item["split"]): dict(item) for item in parent.get("splits") or []
    }
    prompt_source = Path(str(parent["prompt_snapshot_path"]))
    shard_paths: list[Path] = []
    estimates: list[int] = []

    for number, (start, end, estimate) in enumerate(partitions, start=1):
        shard_dir = shard_root / f"shard-{number:04d}"
        shard_dir.mkdir(parents=True, exist_ok=True)
        request_path = shard_dir / "requests.jsonl"
        state_path = shard_dir / "states.jsonl"
        prompt_path = shard_dir / "odrl_extraction.prompt"
        manifest_path = shard_dir / "manifest.json"
        _write_jsonl_atomic(request_path, requests[start:end])
        _write_jsonl_atomic(state_path, states[start:end])
        shutil.copyfile(prompt_source, prompt_path)

        split_counts: dict[str, int] = {}
        for state in states[start:end]:
            occurrences = state.get("occurrences") or [
                {"split": str(state.get("split") or "")}
            ]
            for occurrence in occurrences:
                split = str(occurrence.get("split") or "")
                split_counts[split] = split_counts.get(split, 0) + 1
        splits = []
        for split in source_splits:
            if split not in split_counts:
                continue
            split_info = dict(source_splits[split])
            split_info["record_count"] = split_counts[split]
            splits.append(split_info)

        shard_manifest = {
            "schema_version": BATCH_SCHEMA_VERSION,
            "job_id": f"{parent.get('job_id')}_shard_{number:04d}",
            "status": "prepared",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "parent_manifest_path": str(parent_path),
            "shard_number": number,
            "shard_count": len(partitions),
            "estimated_prompt_tokens": estimate,
            "model_name": parent["model_name"],
            "request_count": end - start,
            "request_settings": parent.get("request_settings") or {},
            "requests_path": str(request_path),
            "states_path": str(state_path),
            "prompt_snapshot_path": str(prompt_path),
            "results_path": str(shard_dir / "results.jsonl"),
            "errors_path": str(shard_dir / "errors.jsonl"),
            "output_dir": str(shard_dir / "outputs"),
            "splits": splits,
            "artifact_sha256": {
                "requests": _sha256_file(request_path),
                "states": _sha256_file(state_path),
                "prompt": _sha256_file(prompt_path),
            },
            "odrl_extraction": parent.get("odrl_extraction") or {},
        }
        _write_json_atomic(manifest_path, shard_manifest)
        shard_paths.append(manifest_path)
        estimates.append(estimate)

    parent["status"] = "sharded"
    parent["shard_manifests"] = [str(path) for path in shard_paths]
    parent["shard_count"] = len(shard_paths)
    parent["shard_maximum_prompt_tokens"] = limit
    parent["shard_estimated_prompt_tokens"] = estimates
    parent["sharded_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(parent_path, parent)
    return shard_paths


def _merge_shard_outputs(parent_path: Path, shard_paths: list[Path]) -> dict[str, Any]:
    _, parent = _read_manifest(parent_path)
    output_dir = Path(str(parent["output_dir"]))
    model_suffix = _safe_model_name(str(parent["model_name"]))
    shard_manifests = [_read_manifest(path)[1] for path in shard_paths]
    for shard in shard_manifests:
        if shard.get("status") != "finalized":
            raise RuntimeError(f"Shard is not finalized: {shard.get('job_id')}")
        _assert_finalized_outputs_exist(shard)

    merged_paths: dict[str, list[str]] = {key: [] for key, _ in OUTPUT_GROUPS}
    for split_info in parent.get("splits") or []:
        split = str(split_info["split"])
        for manifest_key, name_part in OUTPUT_GROUPS:
            indexed_records: list[tuple[int, dict[str, Any]]] = []
            filename = f"{split}_{name_part}_{model_suffix}.txt"
            for shard in shard_manifests:
                candidate = Path(str(shard["output_dir"])) / filename
                if candidate.is_file():
                    shard_records = _read_jsonl(candidate)
                    if manifest_key in {"ner_outputs", "odrl_outputs"}:
                        occurrence_indices: list[int] = []
                        for saved in _read_jsonl(Path(str(shard["states_path"]))):
                            occurrences = saved.get("occurrences") or [{
                                "split": saved.get("split"),
                                "record_index": (saved.get("state") or {}).get("record_index"),
                            }]
                            occurrence_indices.extend(
                                int(item.get("record_index") or 0)
                                for item in occurrences
                                if str(item.get("split") or "") == split
                            )
                        occurrence_indices.sort()
                        if len(occurrence_indices) != len(shard_records):
                            raise RuntimeError(
                                f"Shard {shard.get('job_id')} produced "
                                f"{len(shard_records)} {filename} rows for "
                                f"{len(occurrence_indices)} recorded occurrences."
                            )
                        indexed_records.extend(zip(occurrence_indices, shard_records))
                    else:
                        indexed_records.extend(
                            (int(record.get("record_index") or 0), record)
                            for record in shard_records
                        )
            indexed_records.sort(key=lambda item: item[0])
            records = [record for _, record in indexed_records]
            destination = output_dir / filename
            _write_jsonl_atomic(destination, records)
            merged_paths[manifest_key].append(str(destination))
            if manifest_key in {"ner_outputs", "odrl_outputs"}:
                expected = int(split_info.get("record_count") or 0)
                if len(records) != expected:
                    raise RuntimeError(
                        f"Merged {filename} has {len(records)} records; expected {expected}."
                    )

    primary_usage = {
        name: 0
        for name in ("prompt_tokens", "completion_tokens", "reasoning_tokens", "total_tokens")
    }
    for shard in shard_manifests:
        for name in primary_usage:
            primary_usage[name] += int((shard.get("usage") or {}).get(name) or 0)
    recovery_usage = {name: 0 for name in primary_usage}
    recovery_path = parent.get("recovery_manifest_path")
    if recovery_path and Path(str(recovery_path)).is_file():
        _, recovery = _read_manifest(Path(str(recovery_path)))
        for name in recovery_usage:
            recovery_usage[name] = int((recovery.get("usage") or {}).get(name) or 0)
    usage = {
        name: primary_usage[name] + recovery_usage[name]
        for name in primary_usage
    }
    parent.update(merged_paths)
    parent["usage"] = usage
    parent["primary_batch_usage"] = primary_usage
    parent["recovery_batch_usage"] = recovery_usage
    parent["expanded_record_count"] = int(parent.get("source_record_count") or 0)
    parent["duplicate_gold_verified"] = all(
        bool(shard.get("duplicate_gold_verified")) for shard in shard_manifests
    )
    parent["flat_ner_validation"] = {
        "required": True,
        "validated_record_count": sum(
            int((shard.get("flat_ner_validation") or {}).get("validated_record_count") or 0)
            for shard in shard_manifests
        ),
        "remaining_overlap_count": sum(
            int((shard.get("flat_ner_validation") or {}).get("remaining_overlap_count") or 0)
            for shard in shard_manifests
        ),
    }
    parent["status"] = "finalized"
    parent["finalized_at"] = datetime.now(timezone.utc).isoformat()
    parent["shard_statuses"] = [
        {"manifest": str(path), "status": manifest.get("status")}
        for path, manifest in zip(shard_paths, shard_manifests)
    ]
    _write_json_atomic(parent_path, parent)
    _assert_finalized_outputs_exist(parent)
    return parent


async def run_primary_sharded_batch_job(
    parent_manifest_path: str | Path,
    *,
    maximum_prompt_tokens: int | None = None,
    poll_interval_seconds: float = 300.0,
    timeout_hours: float = 26.0,
    max_consecutive_errors: int = 12,
    strict: bool = True,
    client: Any = None,
) -> dict[str, Any]:
    """Run primary shards and stop before spending on the recovery Batch."""
    parent_path, parent = _read_manifest(parent_manifest_path)
    if parent.get("status") == "finalized" and parent.get("shard_manifests"):
        _assert_finalized_outputs_exist(parent)
        return parent
    shard_paths = prepare_batch_shards(
        parent_path,
        maximum_prompt_tokens=maximum_prompt_tokens,
    )
    api = client or _create_client()
    for index, shard_path in enumerate(shard_paths, start=1):
        _, shard = _read_manifest(shard_path)
        if shard.get("status") in {"finalized", "finalized_pending_recovery"}:
            continue
        if not shard.get("batch_id"):
            submit_batch_job(shard_path, client=api)
        await watch_and_finalize_batch_job(
            shard_path,
            poll_interval_seconds=poll_interval_seconds,
            timeout_hours=timeout_hours,
            max_consecutive_errors=max_consecutive_errors,
            strict=strict,
            client=api,
            recovery_policy="defer",
        )
        _, parent = _read_manifest(parent_path)
        parent["active_shard"] = index
        parent["completed_shards"] = index
        _write_json_atomic(parent_path, parent)

    recovery_path = _prepare_recovery_batch(parent_path, shard_paths)
    if recovery_path is None:
        return _merge_shard_outputs(parent_path, shard_paths)
    _, parent = _read_manifest(parent_path)
    return parent


async def run_recovery_batch_job(
    parent_manifest_path: str | Path,
    *,
    poll_interval_seconds: float = 300.0,
    timeout_hours: float = 26.0,
    client: Any = None,
) -> dict[str, Any]:
    """Submit/resume the one recovery Batch, revalidate, and merge outputs."""
    parent_path, parent = _read_manifest(parent_manifest_path)
    if parent.get("status") == "finalized":
        _assert_finalized_outputs_exist(parent)
        return parent
    shard_paths = [Path(str(value)) for value in parent.get("shard_manifests") or []]
    if not shard_paths:
        raise ValueError(
            "No primary shard manifests exist. Run --batch-shard-primary-run first."
        )
    unfinished = []
    for shard_path in shard_paths:
        _, shard = _read_manifest(shard_path)
        if shard.get("status") not in {"finalized", "finalized_pending_recovery"}:
            unfinished.append(str(shard_path))
    if unfinished:
        raise RuntimeError(
            "Primary shards are not finished; recovery was not submitted: "
            + ", ".join(unfinished)
        )
    recovery_path = _prepare_recovery_batch(parent_path, shard_paths)
    if recovery_path is None:
        return _merge_shard_outputs(parent_path, shard_paths)
    api = client or _create_client()
    await _run_recovery_batch(
        recovery_path,
        api=api,
        poll_interval_seconds=poll_interval_seconds,
        timeout_hours=timeout_hours,
    )

    remaining_sync = int(os.getenv("ODRL_CORRECTION_FINAL_SYNC_LIMIT", "0"))
    if remaining_sync < 0:
        raise ValueError("ODRL_CORRECTION_FINAL_SYNC_LIMIT cannot be negative")
    for shard_path in shard_paths:
        _, shard = _read_manifest(shard_path)
        if shard.get("status") == "finalized" and not shard.get("deferred_recovery_count"):
            continue
        policy = "batch_then_sync" if remaining_sync > 0 else "batch_only"
        await finalize_batch_job(
            shard_path,
            strict=False,
            client=api,
            recovery_policy=policy,
            synchronous_recovery_limit=remaining_sync,
        )
        _, shard = _read_manifest(shard_path)
        used = int(shard.get("synchronous_recovery_records") or 0)
        remaining_sync = max(0, remaining_sync - used)
    return _merge_shard_outputs(parent_path, shard_paths)


async def refinalize_recovery_batch_job(
    parent_manifest_path: str | Path,
) -> dict[str, Any]:
    """Revalidate saved primary/recovery results locally without API calls."""
    parent_path, parent = _read_manifest(parent_manifest_path)
    shard_paths = [Path(str(value)) for value in parent.get("shard_manifests") or []]
    if not shard_paths:
        raise ValueError("Parent manifest has no shard manifests.")
    recovery_path = Path(str(parent.get("recovery_manifest_path") or ""))
    if not recovery_path.is_file():
        raise FileNotFoundError("Parent manifest has no saved recovery manifest.")
    _, recovery = _read_manifest(recovery_path)
    if recovery.get("status") != "distributed":
        raise RuntimeError(
            "Recovery results have not been distributed; run --batch-recovery-run first."
        )
    for shard_path in shard_paths:
        results_path = shard_path.parent / "results.jsonl"
        recovery_responses = shard_path.parent / "batch_recovery_responses.jsonl"
        if not results_path.is_file() or not recovery_responses.is_file():
            raise FileNotFoundError(
                f"Saved local results are incomplete for {shard_path.parent}."
            )
        await finalize_batch_job(
            shard_path,
            strict=False,
            recovery_policy="batch_only",
            reuse_downloaded_results=True,
        )
    parent["status"] = "refinalizing"
    _write_json_atomic(parent_path, parent)
    merged = _merge_shard_outputs(parent_path, shard_paths)
    merged["offline_refinalized_at"] = datetime.now(timezone.utc).isoformat()
    _write_json_atomic(parent_path, merged)
    return merged


async def run_sharded_batch_job(
    parent_manifest_path: str | Path,
    *,
    maximum_prompt_tokens: int | None = None,
    poll_interval_seconds: float = 300.0,
    timeout_hours: float = 26.0,
    max_consecutive_errors: int = 12,
    strict: bool = True,
    client: Any = None,
) -> dict[str, Any]:
    """Run primary shards, one recovery Batch, and merge final outputs."""
    primary = await run_primary_sharded_batch_job(
        parent_manifest_path,
        maximum_prompt_tokens=maximum_prompt_tokens,
        poll_interval_seconds=poll_interval_seconds,
        timeout_hours=timeout_hours,
        max_consecutive_errors=max_consecutive_errors,
        strict=strict,
        client=client,
    )
    if primary.get("status") == "finalized":
        return primary
    return await run_recovery_batch_job(
        parent_manifest_path,
        poll_interval_seconds=poll_interval_seconds,
        timeout_hours=timeout_hours,
        client=client,
    )
