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
    _create_client,
    _read_jsonl,
    _read_manifest,
    _safe_model_name,
    _sha256_file,
    _verify_artifact_integrity,
    _write_json_atomic,
    _write_jsonl_atomic,
    submit_batch_job,
    watch_and_finalize_batch_job,
)


OUTPUT_GROUPS = (
    ("ner_outputs", "correct_with_agent"),
    ("odrl_outputs", "odrl_with_agent"),
    ("diff_outputs", "diffs_from_correct"),
    ("odrl_diff_outputs", "odrl_diffs_from_correct"),
)


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
            split = str(state.get("split") or "")
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
            records: list[dict[str, Any]] = []
            filename = f"{split}_{name_part}_{model_suffix}.txt"
            for shard in shard_manifests:
                candidate = Path(str(shard["output_dir"])) / filename
                if candidate.is_file():
                    records.extend(_read_jsonl(candidate))
            destination = output_dir / filename
            _write_jsonl_atomic(destination, records)
            merged_paths[manifest_key].append(str(destination))
            if manifest_key in {"ner_outputs", "odrl_outputs"}:
                expected = int(split_info.get("record_count") or 0)
                if len(records) != expected:
                    raise RuntimeError(
                        f"Merged {filename} has {len(records)} records; expected {expected}."
                    )

    usage = {name: 0 for name in ("prompt_tokens", "completion_tokens", "reasoning_tokens", "total_tokens")}
    for shard in shard_manifests:
        for name in usage:
            usage[name] += int((shard.get("usage") or {}).get(name) or 0)
    parent.update(merged_paths)
    parent["usage"] = usage
    parent["status"] = "finalized"
    parent["finalized_at"] = datetime.now(timezone.utc).isoformat()
    parent["shard_statuses"] = [
        {"manifest": str(path), "status": manifest.get("status")}
        for path, manifest in zip(shard_paths, shard_manifests)
    ]
    _write_json_atomic(parent_path, parent)
    _assert_finalized_outputs_exist(parent)
    return parent


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
    """Run token-bounded shards sequentially and merge final outputs."""
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
        if shard.get("status") == "finalized":
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
        )
        _, parent = _read_manifest(parent_path)
        parent["active_shard"] = index
        parent["completed_shards"] = index
        _write_json_atomic(parent_path, parent)
    return _merge_shard_outputs(parent_path, shard_paths)
