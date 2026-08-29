"""Focused workflow for correcting ODRL NER JSONL datasets.

Workflow:
    __start__
      -> node_initialize
      -> node_odrl_extraction
      -> node_odrl_correct
      -> node_flat_ner_validate
      -> node_odrl_output
      -> __end__

Run without arguments for an offline example, or pass ``--dataset`` to process
train.txt, valid.txt, or test.txt using the configured endpoint and AI model.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import re
import tempfile
import time
from pathlib import Path
from typing import Any, Awaitable, Callable, Iterable

from dotenv import load_dotenv

from odrl_correct_agent.odrl_correct_process.agent.batch_processing import (
    finalize_batch_job,
    prepare_batch_job,
    refresh_batch_status,
    submit_batch_job,
    watch_and_finalize_batch_job,
)
from odrl_correct_agent.odrl_correct_process.agent.sharded_batch import (
    refinalize_recovery_batch_job,
    run_primary_sharded_batch_job,
    run_recovery_batch_job,
    run_sharded_batch_job,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_initialize import node_initialize
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_correct import (
    compare_entity_sets,
    node_odrl_correct,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_extraction import node_odrl_extraction
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_flat_ner_validate import (
    node_flat_ner_validate,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_output import (
    build_diff_record,
    node_odrl_output,
)
from odrl_correct_agent.odrl_correct_process.agent.state import (
    ODRLCorrectionState,
    create_correction_state,
    default_prompt_path,
)
from odrl_output import build_odrl_diff_record, build_odrl_record_from_entities

from odrl_correct_agent.utils.draw_mermaid_png import draw_mermaid_png

Node = Callable[[ODRLCorrectionState], Awaitable[dict[str, Any]]]
logger = logging.getLogger("odrl_correct_agent")
WORKFLOW_NODE_NAMES = (
    "__start__",
    "node_initialize",
    "node_odrl_extraction",
    "node_odrl_correct",
    "node_flat_ner_validate",
    "node_odrl_output",
    "__end__",
)
WORKFLOW_NODES: tuple[Node, ...] = (
    node_initialize,
    node_odrl_extraction,
    node_odrl_correct,
    node_flat_ner_validate,
    node_odrl_output,
)


DEMO_INPUT = {
    "text": (
        "The Data Controller shall consult the Data Processor regarding "
        "commercial or other confidentiality issues in relation to the Contract."
    ),
    "entities": [
        {"start": 4, "end": 19, "label": "ASSIGNEE"},
        {"start": 20, "end": 25, "label": "RULE_TYPE-OBLIGATION"},
        {"start": 34, "end": 42, "label": "ASSET"},
    ],
}
DEMO_AI_RESPONSE = {
    "validated_policy_rules": [
        {
            "policy_rule_id": "policy-rule-1",
            "source_text": DEMO_INPUT["text"],
            "assignee": "Data Controller",
            "action": "consult",
            "asset": "Data Processor",
            "attributed_party": "",
            "rule_type": "obligation",
            "constraint": (
                "regarding commercial or other confidentiality issues in relation "
                "to the Contract"
            ),
            "purpose": "",
            "selected_from": "ai_reconciliation",
        }
    ]
}


class ODRLCorrectionWorkflow:
    """Small ordered async graph with independently testable nodes."""

    node_names = WORKFLOW_NODE_NAMES

    def __init__(self, nodes: Iterable[Node] = WORKFLOW_NODES):
        self.nodes = tuple(nodes)

    async def ainvoke(
        self,
        input_record: dict[str, Any],
        **overrides: Any,
    ) -> ODRLCorrectionState:
        state = create_correction_state(input_record, **overrides)
        record_index = int(state.get("record_index") or 0)
        record_total = int(state.get("record_total") or 0)
        record_label = (
            f"{record_index}/{record_total}"
            if record_index and record_total
            else "single"
        )
        for node in self.nodes:
            node_name = getattr(node, "__name__", node.__class__.__name__)
            started = time.perf_counter()
            logger.info("record=%s node=%s status=started", record_label, node_name)
            try:
                update = await node(state)
                if not isinstance(update, dict):
                    raise TypeError(f"{node_name} must return a dictionary update.")
            except Exception:
                elapsed_ms = (time.perf_counter() - started) * 1000
                logger.exception(
                    "record=%s node=%s status=failed elapsed_ms=%.1f",
                    record_label,
                    node_name,
                    elapsed_ms,
                )
                raise
            state.update(update)
            elapsed_ms = (time.perf_counter() - started) * 1000
            logger.info(
                "record=%s node=%s status=completed elapsed_ms=%.1f",
                record_label,
                node_name,
                elapsed_ms,
            )
        return state


def configure_logging(level: str = "INFO") -> None:
    """Configure concise progress logs for command-line runs."""
    normalized_level = str(level or "INFO").upper()
    numeric_level = getattr(logging, normalized_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Unsupported log level: {level}")
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )


def _load_cli_environment() -> None:
    """Load project and agent .env files before CLI defaults are resolved."""
    project_root = Path(__file__).resolve().parents[3]
    load_dotenv(project_root / ".env", override=False)
    load_dotenv(project_root / "odrl_correct_agent" / ".env", override=False)


def build_workflow() -> ODRLCorrectionWorkflow:
    """Build the focused ODRL correction graph."""
    return ODRLCorrectionWorkflow()


# The immutable application instance used for execution and visualization.
correct_agent_app = build_workflow()


def _safe_model_name(model_name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", model_name.strip())
    return value.strip("._-") or "unknown_model"


def corrected_output_path(
    dataset_path: Path,
    output_dir: Path,
    model_name: str,
) -> Path:
    """Return ``test_correct_with_agent_{MODEL_NAME}.txt`` style output."""
    return output_dir / (
        f"{dataset_path.stem}_correct_with_agent_{_safe_model_name(model_name)}.txt"
    )


def odrl_output_path(
    dataset_path: Path,
    output_dir: Path,
    model_name: str,
) -> Path:
    """Return ``test_odrl_with_agent_{MODEL_NAME}.txt`` style output."""
    return output_dir / (
        f"{dataset_path.stem}_odrl_with_agent_{_safe_model_name(model_name)}.txt"
    )


def diff_output_path(
    dataset_path: Path,
    output_dir: Path,
    model_name: str,
) -> Path:
    """Return ``test_diffs_from_correct_{MODEL_NAME}.txt`` style output."""
    return output_dir / (
        f"{dataset_path.stem}_diffs_from_correct_{_safe_model_name(model_name)}.txt"
    )


def odrl_diff_output_path(
    dataset_path: Path,
    output_dir: Path,
    model_name: str,
) -> Path:
    """Return ``test_odrl_diffs_from_correct_{MODEL_NAME}.txt`` style output."""
    return output_dir / (
        f"{dataset_path.stem}_odrl_diffs_from_correct_{_safe_model_name(model_name)}.txt"
    )


def _read_jsonl(path: Path, limit: int | None = None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{path}:{line_number} contains invalid JSON: {exc.msg}"
                ) from exc
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number} must contain a JSON object.")
            records.append(record)
            if limit is not None and len(records) >= limit:
                break
    return records


def _write_jsonl_atomic(path: Path, records: Iterable[dict[str, Any]]) -> None:
    """Replace a JSONL output only after every line has been serialized."""
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


async def correct_dataset(
    dataset_path: str | Path,
    *,
    output_dir: str | Path | None = None,
    prompt_path: str | Path | None = None,
    model_name: str = "",
    endpoint: str = "",
    call_endpoint: bool = True,
    limit: int | None = None,
    strict: bool = False,
    ai_response_override: dict[str, Any] | None = None,
    gold_cache: dict[str, dict[str, Any]] | None = None,
    duplicate_variants_by_text: dict[str, list[list[dict[str, Any]]]] | None = None,
) -> tuple[Path, Path, list[ODRLCorrectionState]]:
    """Correct one JSONL dataset and write NER plus text-to-ODRL files."""
    source_path = Path(dataset_path).expanduser().resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {source_path}")
    destination = Path(output_dir).expanduser().resolve() if output_dir else source_path.parent
    records = _read_jsonl(source_path, limit=limit)
    original_odrl_path = source_path.with_name(f"{source_path.stem}_odrl.txt")
    original_odrl_records = (
        _read_jsonl(original_odrl_path, limit=limit)
        if original_odrl_path.is_file()
        else []
    )
    if original_odrl_records and len(original_odrl_records) != len(records):
        raise ValueError(
            f"{original_odrl_path} has {len(original_odrl_records)} records; "
            f"expected {len(records)} to align with {source_path}"
        )
    workflow = correct_agent_app
    states: list[ODRLCorrectionState] = []

    requested_model = (
        model_name
        or os.getenv("MODEL_NAME")
        or os.getenv("OPENAI_MODEL_NAME")
        or "gpt-4o-mini"
    )
    logger.info(
        "dataset=%s status=started records=%d model=%s endpoint=%s",
        source_path.name,
        len(records),
        requested_model,
        "enabled" if call_endpoint else "disabled",
    )

    for index, record in enumerate(records, start=1):
        source_preview = " ".join(str(record.get("text") or "").split())
        if len(source_preview) > 120:
            source_preview = source_preview[:117] + "..."
        logger.info(
            "dataset=%s record=%d/%d status=started text=%r",
            source_path.name,
            index,
            len(records),
            source_preview,
        )
        try:
            source_text = str(record.get("text") or "")
            cached = (gold_cache or {}).get(source_text)
            if cached is None:
                state = await workflow.ainvoke(
                    record,
                    record_index=index,
                    record_total=len(records),
                    dataset_path=str(source_path),
                    output_dir=str(destination),
                    prompt_path=str(prompt_path or default_prompt_path()),
                    model_name=model_name,
                    endpoint=endpoint,
                    call_endpoint=call_endpoint,
                    ai_response_override=ai_response_override,
                    duplicate_original_variants=list(
                        (duplicate_variants_by_text or {}).get(source_text) or []
                    ),
                )
                if gold_cache is not None:
                    gold_cache[source_text] = {
                        "validated_policy_rules": [
                            dict(rule) for rule in state.get("validated_policy_rules") or []
                        ],
                        "corrected_entities": [
                            dict(entity) for entity in state.get("corrected_entities") or []
                        ],
                        "selected_from": state.get("selected_from"),
                        "correction_warnings": list(
                            state.get("correction_warnings") or []
                        ),
                    }
            else:
                state = create_correction_state(
                    record,
                    record_index=index,
                    record_total=len(records),
                    dataset_path=str(source_path),
                    output_dir=str(destination),
                    model_name=requested_model,
                )
                state.update({
                    "source_text": source_text,
                    "original_entities": [
                        dict(entity) for entity in record.get("entities") or []
                    ],
                    "validated_policy_rules": [
                        dict(rule) for rule in cached.get("validated_policy_rules") or []
                    ],
                    "corrected_entities": [
                        dict(entity) for entity in cached.get("corrected_entities") or []
                    ],
                    "selected_from": "duplicate_gold_reuse",
                    "correction_warnings": list(
                        cached.get("correction_warnings") or []
                    ),
                    "flat_ner_validated": True,
                    "overlap_count": 0,
                })
                state["correction_comparison"] = compare_entity_sets(
                    list(state.get("original_entities") or []),
                    list(state.get("corrected_entities") or []),
                )
                state.update(await node_odrl_output(state))
        except Exception as exc:
            if strict:
                raise RuntimeError(
                    f"Correction failed for record {index} in {source_path}: {exc}"
                ) from exc
            logger.warning(
                "dataset=%s record=%d/%d status=retained_after_error error=%s: %s",
                source_path.name,
                index,
                len(records),
                type(exc).__name__,
                exc,
            )
            state = create_correction_state(
                record,
                record_index=index,
                record_total=len(records),
            )
            state.update({
                "source_text": str(record.get("text") or ""),
                "corrected_record": record,
                "text_odrl_record": {
                    "text": str(record.get("text") or ""),
                    "odrl": [],
                },
                "correction_warnings": [f"{type(exc).__name__}: {exc}"],
            })
        states.append(state)
        if original_odrl_records:
            state["original_odrl_record"] = original_odrl_records[index - 1]
        if not state.get("diff_record"):
            state["diff_record"] = build_diff_record(state)
        corrected_record = state.get("corrected_record") or {}
        corrected_entities = (
            corrected_record.get("entities") or []
            if isinstance(corrected_record, dict)
            else []
        )
        logger.info(
            "dataset=%s record=%d/%d status=completed selected_from=%s "
            "rules=%d entities=%d warnings=%d",
            source_path.name,
            index,
            len(records),
            state.get("selected_from") or "error_fallback",
            len(state.get("validated_policy_rules") or []),
            len(corrected_entities),
            len(state.get("correction_warnings") or []),
        )

    effective_model = next(
        (str(state.get("model_name") or "") for state in states if state.get("model_name")),
        model_name or os.getenv("MODEL_NAME") or os.getenv("OPENAI_MODEL_NAME") or "gpt-4o-mini",
    )
    ner_path = corrected_output_path(source_path, destination, effective_model)
    text_odrl_path = odrl_output_path(source_path, destination, effective_model)
    diff_path = diff_output_path(source_path, destination, effective_model)
    _write_jsonl_atomic(ner_path, (state["corrected_record"] for state in states))
    _write_jsonl_atomic(text_odrl_path, (state["text_odrl_record"] for state in states))
    changed_states = [
        state
        for state in states
        if (state.get("diff_record") or {}).get("diffs", {}).get("has_changes")
    ]
    _write_jsonl_atomic(
        diff_path,
        (state["diff_record"] for state in changed_states),
    )
    odrl_diff_path = odrl_diff_output_path(source_path, destination, effective_model)
    for state in states:
        original_record = state.get("input_record") or {}
        state["original_odrl_record"] = dict(
            state.get("original_odrl_record")
            or build_odrl_record_from_entities(
                str(original_record.get("text") or state.get("source_text") or ""),
                list(original_record.get("entities") or []),
            )
        )
        state["corrected_odrl_record"] = dict(state["text_odrl_record"] or {})
        state["odrl_diff_record"] = build_odrl_diff_record(state)
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
        state["diff_output_path"] = str(diff_path)
        state["odrl_diff_output_path"] = str(odrl_diff_path)
    logger.info(
        "dataset=%s status=completed records=%d changed_records=%d "
        "ner_output=%s odrl_output=%s diff_output=%s odrl_diff_output=%s",
        source_path.name,
        len(states),
        len(changed_states),
        ner_path,
        text_odrl_path,
        diff_path,
        odrl_diff_path,
    )
    return ner_path, text_odrl_path, states


async def correct_all_splits(
    data_dir: str | Path,
    **options: Any,
) -> tuple[list[Path], list[Path], list[ODRLCorrectionState]]:
    """Correct train/valid/test and write model-specific files per split."""
    source_dir = Path(data_dir).expanduser().resolve()
    source_paths = [source_dir / name for name in ("train.txt", "valid.txt", "test.txt")]
    variants_by_text: dict[str, list[list[dict[str, Any]]]] = {}
    variant_signatures: dict[str, set[tuple[tuple[int, int, str], ...]]] = {}
    for source_path in source_paths:
        for record in _read_jsonl(source_path, limit=options.get("limit")):
            text_value = str(record.get("text") or "")
            entities = [dict(entity) for entity in record.get("entities") or []]
            signature = tuple(sorted(
                (int(entity["start"]), int(entity["end"]), str(entity["label"]))
                for entity in entities
            ))
            seen = variant_signatures.setdefault(text_value, set())
            if signature not in seen:
                variants_by_text.setdefault(text_value, []).append(entities)
                seen.add(signature)

    gold_cache: dict[str, dict[str, Any]] = {}
    ner_paths: list[Path] = []
    odrl_paths: list[Path] = []
    all_states: list[ODRLCorrectionState] = []
    for filename in ("train.txt", "valid.txt", "test.txt"):
        ner_path, odrl_path, states = await correct_dataset(
            source_dir / filename,
            gold_cache=gold_cache,
            duplicate_variants_by_text=variants_by_text,
            **options,
        )
        ner_paths.append(ner_path)
        odrl_paths.append(odrl_path)
        all_states.extend(states)
    return ner_paths, odrl_paths, all_states


async def run_demo() -> ODRLCorrectionState:
    """Run the documented example without endpoint or API access."""
    state = await correct_agent_app.ainvoke(
        DEMO_INPUT,
        model_name="demo-model",
        call_endpoint=False,
        ai_response_override=DEMO_AI_RESPONSE,
    )
    print("Workflow:", " -> ".join(WORKFLOW_NODE_NAMES))
    print("Input:")
    print(json.dumps(DEMO_INPUT, ensure_ascii=False, indent=2))
    print("\nCorrected NER format:")
    print(json.dumps(state["corrected_record"], ensure_ascii=False, indent=2))
    print("\ntext_odrl format:")
    print(json.dumps(state["text_odrl_record"], ensure_ascii=False, indent=2))
    return state


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Correct an ODRL NER JSONL dataset using endpoint and AI evidence."
    )
    parser.add_argument(
        "--dataset",
        help="Input JSONL file, for example data/test.txt. Omit to run the offline demo.",
    )
    parser.add_argument(
        "--all-splits",
        action="store_true",
        help="Correct train.txt, valid.txt, and test.txt from --data-dir.",
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Directory used by --all-splits (default: data).",
    )
    parser.add_argument("--output-dir", help="Output directory; defaults to the dataset directory.")
    parser.add_argument("--prompt", default=str(default_prompt_path()), help="Correction prompt path.")
    parser.add_argument("--model-name", default="", help="Override MODEL_NAME from .env.")
    parser.add_argument("--endpoint", default="", help="Override ODRL_EXTRACTION_ENDPOINT.")
    parser.add_argument("--skip-endpoint", action="store_true", help="Use original NER plus AI only.")
    parser.add_argument("--limit", type=int, help="Process only the first N records.")
    parser.add_argument("--strict", action="store_true", help="Stop on the first failed record.")
    parser.add_argument(
        "--batch-prepare",
        action="store_true",
        help=(
            "Prepare local evidence, upload requests, and submit a paid discounted "
            "OpenAI Batch job."
        ),
    )
    parser.add_argument(
        "--batch-run",
        action="store_true",
        help=(
            "Prepare and submit a paid Batch, wait resumably for its remote "
            "completion, then strictly finalize all outputs."
        ),
    )
    parser.add_argument(
        "--batch-prepare-only",
        action="store_true",
        help="Prepare Batch artifacts locally without uploading or making a paid API call.",
    )
    parser.add_argument(
        "--batch-submit",
        metavar="MANIFEST",
        help="Submit a manifest created with --batch-prepare-only.",
    )
    parser.add_argument(
        "--batch-status",
        metavar="MANIFEST",
        help="Refresh the remote status stored in a Batch manifest.",
    )
    parser.add_argument(
        "--batch-finalize",
        metavar="MANIFEST",
        help="Download a completed Batch and write corrected split outputs.",
    )
    parser.add_argument(
        "--batch-watch-finalize",
        metavar="MANIFEST",
        help=(
            "Resume polling a submitted Batch manifest and automatically "
            "finalize it after completion."
        ),
    )
    parser.add_argument(
        "--batch-shard-run",
        metavar="MANIFEST",
        help=(
            "Split an already prepared manifest into prompt-token-bounded "
            "primary shards, run them sequentially, recover invalid records "
            "with one discounted Batch, and merge all final outputs."
        ),
    )
    parser.add_argument(
        "--batch-shard-primary-run",
        metavar="MANIFEST",
        help=(
            "Run/finalize all primary shards and prepare local recovery Batch "
            "artifacts, but do not submit the recovery Batch."
        ),
    )
    parser.add_argument(
        "--batch-recovery-run",
        metavar="MANIFEST",
        help=(
            "Submit/resume the prepared recovery Batch from a sharded parent "
            "manifest, validate its results, and merge final outputs."
        ),
    )
    parser.add_argument(
        "--batch-recovery-refinalize",
        metavar="MANIFEST",
        help=(
            "Revalidate already downloaded primary and recovery results with "
            "the current local rules; makes no OpenAI API calls."
        ),
    )
    parser.add_argument(
        "--batch-shard-max-prompt-tokens",
        type=int,
        default=int(os.getenv("ODRL_BATCH_SHARD_MAX_PROMPT_TOKENS", "1500000")),
        help="Conservative estimated prompt-token ceiling per shard (default: 1500000).",
    )
    parser.add_argument(
        "--batch-poll-seconds",
        type=float,
        default=float(os.getenv("ODRL_BATCH_POLL_SECONDS", "300")),
        help="Seconds between successful Batch status polls (default: 300).",
    )
    parser.add_argument(
        "--batch-watch-timeout-hours",
        type=float,
        default=float(os.getenv("ODRL_BATCH_WATCH_TIMEOUT_HOURS", "26")),
        help=(
            "Local watcher timeout; it never cancels the remote Batch "
            "(default: 26 hours)."
        ),
    )
    parser.add_argument(
        "--batch-max-consecutive-errors",
        type=int,
        default=int(os.getenv("ODRL_BATCH_MAX_CONSECUTIVE_ERRORS", "12")),
        help="Stop the local watcher after this many polling errors (default: 12).",
    )
    parser.add_argument(
        "--batch-job-dir",
        help="Directory for request, state, result, and manifest Batch artifacts.",
    )
    parser.add_argument(
        "--allow-batch-fallbacks",
        action="store_true",
        help="Allow failed/truncated Batch records to use endpoint/original fallback data.",
    )
    parser.add_argument(
        "--log-level",
        default=os.getenv("ODRL_CORRECTION_LOG_LEVEL", "INFO").upper(),
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        help="Progress log level (default: INFO).",
    )
    return parser


async def _async_main(args: argparse.Namespace) -> int:
    batch_actions = [
        args.batch_prepare,
        args.batch_run,
        args.batch_prepare_only,
        bool(args.batch_submit),
        bool(args.batch_status),
        bool(args.batch_finalize),
        bool(args.batch_watch_finalize),
        bool(args.batch_shard_run),
        bool(args.batch_shard_primary_run),
        bool(args.batch_recovery_run),
        bool(args.batch_recovery_refinalize),
    ]
    if sum(bool(action) for action in batch_actions) > 1:
        raise ValueError("Select only one Batch action at a time.")
    if args.dataset and args.all_splits:
        raise ValueError("Use either --dataset or --all-splits, not both.")
    if args.limit is not None and args.limit <= 0:
        raise ValueError("--limit must be greater than zero.")
    if args.batch_shard_max_prompt_tokens <= 0:
        raise ValueError("--batch-shard-max-prompt-tokens must be greater than zero.")
    if args.batch_recovery_refinalize:
        manifest = await refinalize_recovery_batch_job(
            args.batch_recovery_refinalize
        )
        print(
            f"Offline re-finalization completed for "
            f"{manifest.get('expanded_record_count') or 0} source record(s)."
        )
        print("No OpenAI API call was made.")
        print(f"Parent manifest: {Path(args.batch_recovery_refinalize).expanduser().resolve()}")
        return 0
    if args.batch_shard_primary_run:
        manifest = await run_primary_sharded_batch_job(
            args.batch_shard_primary_run,
            maximum_prompt_tokens=args.batch_shard_max_prompt_tokens,
            poll_interval_seconds=args.batch_poll_seconds,
            timeout_hours=args.batch_watch_timeout_hours,
            max_consecutive_errors=args.batch_max_consecutive_errors,
            strict=not args.allow_batch_fallbacks,
        )
        print(f"Primary shards completed: {manifest.get('completed_shards') or 0}")
        print(f"Recovery candidates: {manifest.get('recovery_request_count') or 0}")
        recovery_manifest = manifest.get("recovery_manifest_path")
        if recovery_manifest:
            recovery = json.loads(Path(str(recovery_manifest)).read_text(encoding="utf-8"))
            print(f"Recovery manifest: {recovery_manifest}")
            print(f"Recovery requests: {recovery.get('requests_path')}")
            print("No recovery API call was made.")
        else:
            print("No recovery candidates were found; final outputs are complete.")
        print(f"Parent manifest: {Path(args.batch_shard_primary_run).expanduser().resolve()}")
        return 0
    if args.batch_recovery_run:
        manifest = await run_recovery_batch_job(
            args.batch_recovery_run,
            poll_interval_seconds=args.batch_poll_seconds,
            timeout_hours=args.batch_watch_timeout_hours,
        )
        print(
            f"Finalized {manifest.get('expanded_record_count') or manifest.get('source_record_count') or 0} "
            "source record(s) after recovery."
        )
        print(f"Recovery candidates: {manifest.get('recovery_request_count') or 0}")
        for key, label in (
            ("ner_outputs", "NER dataset"),
            ("odrl_outputs", "Text-to-ODRL dataset"),
            ("diff_outputs", "Correction diff dataset"),
            ("odrl_diff_outputs", "ODRL correction diff dataset"),
        ):
            for output_path in manifest.get(key) or []:
                print(f"{label}: {output_path}")
        print(f"Parent manifest: {Path(args.batch_recovery_run).expanduser().resolve()}")
        return 0
    if args.batch_shard_run:
        manifest = await run_sharded_batch_job(
            args.batch_shard_run,
            maximum_prompt_tokens=args.batch_shard_max_prompt_tokens,
            poll_interval_seconds=args.batch_poll_seconds,
            timeout_hours=args.batch_watch_timeout_hours,
            max_consecutive_errors=args.batch_max_consecutive_errors,
            strict=not args.allow_batch_fallbacks,
        )
        print(
            f"Finalized {manifest.get('expanded_record_count') or manifest.get('source_record_count') or 0} "
            f"source record(s) from {manifest.get('request_count') or 0} unique-text request(s)."
        )
        print(f"Shards: {manifest.get('shard_count') or 0}")
        for key, label in (
            ("ner_outputs", "NER dataset"),
            ("odrl_outputs", "Text-to-ODRL dataset"),
            ("diff_outputs", "Correction diff dataset"),
            ("odrl_diff_outputs", "ODRL correction diff dataset"),
        ):
            for output_path in manifest.get(key) or []:
                print(f"{label}: {output_path}")
        print(f"Manifest: {Path(args.batch_shard_run).expanduser().resolve()}")
        return 0
    if args.batch_submit:
        manifest = submit_batch_job(args.batch_submit)
        print(f"Batch submitted: {manifest['batch_id']}")
        print(f"Status: {manifest['status']}")
        print(f"Manifest: {Path(args.batch_submit).expanduser().resolve()}")
        return 0
    if args.batch_status:
        manifest = refresh_batch_status(args.batch_status)
        print(f"Batch ID: {manifest['batch_id']}")
        print(f"Status: {manifest['status']}")
        print(f"Request counts: {manifest.get('request_counts') or {}}")
        return 0
    if args.batch_watch_finalize:
        manifest = await watch_and_finalize_batch_job(
            args.batch_watch_finalize,
            poll_interval_seconds=args.batch_poll_seconds,
            timeout_hours=args.batch_watch_timeout_hours,
            max_consecutive_errors=args.batch_max_consecutive_errors,
            strict=not args.allow_batch_fallbacks,
        )
        print(
            f"Finalized {manifest.get('expanded_record_count') or manifest.get('source_record_count') or 0} "
            f"source record(s) from {manifest.get('request_count') or 0} unique-text request(s)."
        )
        for key, label in (
            ("ner_outputs", "NER dataset"),
            ("odrl_outputs", "Text-to-ODRL dataset"),
            ("diff_outputs", "Correction diff dataset"),
            ("odrl_diff_outputs", "ODRL correction diff dataset"),
        ):
            for output_path in manifest.get(key) or []:
                print(f"{label}: {output_path}")
        print(
            f"Manifest: {Path(args.batch_watch_finalize).expanduser().resolve()}"
        )
        return 0
    if args.batch_finalize:
        ner_paths, odrl_paths, states = await finalize_batch_job(
            args.batch_finalize,
            strict=not args.allow_batch_fallbacks,
        )
        finalized_manifest = json.loads(
            Path(args.batch_finalize).expanduser().resolve().read_text(
                encoding="utf-8"
            )
        )
        print(f"Finalized {len(states)} Batch record(s).")
        for output_path in ner_paths:
            print(f"NER dataset: {output_path}")
        for output_path in odrl_paths:
            print(f"Text-to-ODRL dataset: {output_path}")
        for output_path in finalized_manifest.get("diff_outputs") or []:
            print(f"Correction diff dataset: {output_path}")
        for output_path in finalized_manifest.get("odrl_diff_outputs") or []:
            print(f"ODRL correction diff dataset: {output_path}")
        print(f"Manifest: {Path(args.batch_finalize).expanduser().resolve()}")
        return 0
    if args.batch_prepare or args.batch_prepare_only or args.batch_run:
        if not args.dataset and not args.all_splits:
            raise ValueError(
                "Batch preparation requires --dataset or --all-splits."
            )
        dataset_paths = (
            [Path(args.data_dir) / name for name in ("train.txt", "valid.txt", "test.txt")]
            if args.all_splits
            else [Path(args.dataset)]
        )
        manifest_path = await prepare_batch_job(
            dataset_paths,
            output_dir=args.output_dir,
            job_dir=args.batch_job_dir,
            prompt_path=args.prompt,
            model_name=args.model_name,
            endpoint=args.endpoint,
            call_endpoint=not args.skip_endpoint,
            limit=args.limit,
            submit=args.batch_prepare or args.batch_run,
        )
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        print(
            f"Prepared {manifest['request_count']} unique-text Batch request(s) "
            f"for {manifest.get('source_record_count', manifest['request_count'])} source record(s).",
            flush=True,
        )
        print(f"Manifest: {manifest_path}", flush=True)
        print(f"Requests: {manifest['requests_path']}", flush=True)
        if args.batch_prepare or args.batch_run:
            print(f"Batch submitted: {manifest['batch_id']}", flush=True)
            print(f"Status: {manifest['status']}", flush=True)
        else:
            print("No API call was made. Use --batch-submit MANIFEST to submit it.")
        if args.batch_run:
            finalized = await watch_and_finalize_batch_job(
                manifest_path,
                poll_interval_seconds=args.batch_poll_seconds,
                timeout_hours=args.batch_watch_timeout_hours,
                max_consecutive_errors=args.batch_max_consecutive_errors,
                strict=not args.allow_batch_fallbacks,
            )
            print(
                f"Finalized {finalized.get('expanded_record_count') or finalized.get('source_record_count') or 0} "
                f"source record(s) from {finalized.get('request_count') or 0} unique-text request(s)."
            )
            for key, label in (
                ("ner_outputs", "NER dataset"),
                ("odrl_outputs", "Text-to-ODRL dataset"),
                ("diff_outputs", "Correction diff dataset"),
                ("odrl_diff_outputs", "ODRL correction diff dataset"),
            ):
                for output_path in finalized.get(key) or []:
                    print(f"{label}: {output_path}")
        return 0
    if not args.dataset and not args.all_splits:
        await run_demo()
        return 0
    options = {
        "output_dir": args.output_dir,
        "prompt_path": args.prompt,
        "model_name": args.model_name,
        "endpoint": args.endpoint,
        "call_endpoint": not args.skip_endpoint,
        "limit": args.limit,
        "strict": args.strict,
    }
    if args.all_splits:
        ner_paths, text_odrl_paths, states = await correct_all_splits(
            args.data_dir,
            **options,
        )
    else:
        ner_path, text_odrl_path, states = await correct_dataset(
            args.dataset,
            **options,
        )
        ner_paths = [ner_path]
        text_odrl_paths = [text_odrl_path]
    warnings = sum(len(state.get("correction_warnings") or []) for state in states)
    print(f"Corrected {len(states)} record(s).")
    for ner_path in ner_paths:
        print(f"NER dataset: {ner_path}")
    for text_odrl_path in text_odrl_paths:
        print(f"Text-to-ODRL dataset: {text_odrl_path}")
    diff_paths = dict.fromkeys(
        str(state.get("diff_output_path") or "")
        for state in states
        if state.get("diff_output_path")
    )
    for diff_path in diff_paths:
        print(f"Correction diff dataset: {diff_path}")
    for state in states:
        if state.get("odrl_diff_output_path"):
            print(f"ODRL correction diff dataset: {state['odrl_diff_output_path']}")
    print(f"Warnings: {warnings}")
    return 0


def main(argv: list[str] | None = None) -> int:
    _load_cli_environment()
    args = build_parser().parse_args(argv)
    configure_logging(args.log_level)
    return asyncio.run(_async_main(args))


if __name__ == "__main__":
    # draw_mermaid_png(correct_agent_app, "odrl_correct_main_graph")
    raise SystemExit(main())


# python -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --all-splits \
#     --data-dir data
#
#   python -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph
#
#   Correct only test.txt:
#
#   python -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --dataset data/test.txt
#
#   Correct all splits:
#
#   python -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --all-splits \
#     --data-dir data

#   ### 1. Verify the old ODRL model endpoint
#
#   curl -sS -X POST \
#     http://127.0.0.1:5001/odrl_generation \
#     -H 'Content-Type: application/json' \
#     -d '{"text":"The document may be downloaded for research purposes."}'
#
#   Do not begin Batch preparation until this returns a valid "rules" result.
#
#   ### 2. Prepare and submit the Batch in the background
#
#   nohup .venv/bin/python -u \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-prepare \
#     --all-splits \
#     --data-dir data \
#     --log-level INFO \
#     > odrl_batch_prepare.log 2>&1 &
#
#   echo $! > odrl_batch_prepare.pid
#
#   Monitor preparation:
#
#   tail -f odrl_batch_prepare.log
#
#   Stop following the log with Ctrl+C. This does not stop the background process.
#
#   When finished successfully, the log will contain:
#
#   Prepared 4834 Batch request(s).
#   Manifest: /.../data/batch_jobs/odrl_gpt-5.6-luna_.../manifest.json
#   Batch submitted: batch_...
#   Status: validating
#
#   Extract the manifest path:
#
#   MANIFEST="$(awk -F'Manifest: ' '/^Manifest: /{path=$2} END{print path}' odrl_batch_prepare.log)"
#   echo "$MANIFEST"
#
#   ### 3. Check the OpenAI Batch status
#
  # .venv/bin/python \
  #   -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  #   --batch-status "$MANIFEST"
#
#   Run this periodically until it reports:
#
#   Status: completed
#
#   The preparation process exits after submission; this is expected. OpenAI continues processing the Batch remotely.
#
#   ### 4. Finalize in the background
#
#   After the status is completed:
#
#   nohup .venv/bin/python -u \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-finalize "$MANIFEST" \
#     --log-level INFO \
#     > odrl_batch_finalize.log 2>&1 &
#
#   echo $! > odrl_batch_finalize.pid
#
#   Monitor finalization:
#
#   tail -f odrl_batch_finalize.log
#
#   ### 5. Check the final files
#
#   ls -lh \
#     data/*_correct_with_agent_gpt-5.6-luna.txt \
#     data/*_odrl_with_agent_gpt-5.6-luna.txt \
#     data/*_diffs_from_correct_gpt-5.6-luna.txt
#
#   The final outputs will be:
#
#   data/train_correct_with_agent_gpt-5.6-luna.txt
#   data/valid_correct_with_agent_gpt-5.6-luna.txt
#   data/test_correct_with_agent_gpt-5.6-luna.txt
#
#   data/train_odrl_with_agent_gpt-5.6-luna.txt
#   data/valid_odrl_with_agent_gpt-5.6-luna.txt
#   data/test_odrl_with_agent_gpt-5.6-luna.txt
#
#   data/train_diffs_from_correct_gpt-5.6-luna.txt
#   data/valid_diffs_from_correct_gpt-5.6-luna.txt
#   data/test_diffs_from_correct_gpt-5.6-luna.txt
#
#   Do not add --allow-batch-fallbacks if maximum corrected-dataset quality is the priority.
# --------------------------------------------
#  echo $! > odrl_batch_run.pid
#
#   saves the process ID of the most recently started background command into odrl_batch_run.pid.
#
#   - $! — PID of the last background process
#   - > — writes to a file, replacing existing content
#   - odrl_batch_run.pid — file containing that PID
#
#   For example:
#
#   18432
#
#   You can later check whether it is running:
#
#   ps -p "$(cat odrl_batch_run.pid)" -f
#
#   Or stop the local process:
#
#   kill "$(cat odrl_batch_run.pid)"
#
#   Stopping it does not cancel an OpenAI Batch that has already been submitted.

# The cause is that $MANIFEST was empty, so the program did not recognize a valid --batch-finalize action.
#
#   Check it:
#
#   echo "$MANIFEST"
#
#   Recover the manifest from your log:
#
#   MANIFEST="$(sed -n 's/^Manifest: //p' odrl_batch_run.log | tail -1)"
#   echo "$MANIFEST"
#   test -f "$MANIFEST" && echo "Manifest found"
#
#   Check the Batch status:
#
#   .venv/bin/python \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-status "$MANIFEST"
#
#   Only when it reports Status: completed, finalize with:
#
#   .venv/bin/python \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-finalize "$MANIFEST"
#
#   However, if you started with --batch-run, it already waits and finalizes automatically. You normally only need:
#
#   tail -f odrl_batch_run.log


# $MANIFEST is not automatically created as a shell variable. The manifest file is created only after all records have completed local endpoint preparation.
#
#   Check progress:
#
#   tail -f odrl_batch_run.log
#
#   Check whether the process is still running:
#
#   ps -p "$(cat odrl_batch_run.pid)" -f
#
#   Eventually the log will show:
#
#   Prepared 4834 Batch request(s).
#   Manifest: /.../data/batch_jobs/odrl_gpt-5.6-luna_.../manifest.json
#   Batch submitted: batch_...
#
#   Then you can extract it:
#
#   MANIFEST="$(sed -n 's/^Manifest: //p' odrl_batch_run.log | tail -1)"
#   echo "$MANIFEST"
#
#   With --batch-run, you do not need to run --batch-finalize manually. It will wait and finalize automatically. If the background process has stopped, inspect the error with:
#
#   tail -n 100 odrl_batch_run.log


#   MANIFEST="$(sed -n 's/^Manifest: //p' odrl_gold_prepare.log | tail -1)"
#   echo "$MANIFEST"
#
#   Then, for the real run:
#
#   nohup .venv/bin/python -u \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-shard-run "$MANIFEST" \
#     --batch-poll-seconds 300 \
#     --log-level INFO \
#     > odrl_gold_sharded.log 2>&1 &
#
#   echo $! > odrl_gold_sharded.pid



# ------------The workflow is now separated into two explicit stages------------
# ### Stage 1: Complete eight primary shards
#
#   Use this command instead of --batch-shard-run:
#
#   MANIFEST="data/batch_jobs/odrl_gpt-5.6-luna_20260829T144210Z_67a01c9c/manifest.json"
#
#   nohup .venv/bin/python -u \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-shard-primary-run "$MANIFEST" \
#     --batch-poll-seconds 300 \
#     --log-level INFO \
#     > odrl_primary_shards.log 2>&1 &
#
#   echo $! > odrl_primary_shards.pid
#
#   Monitor it:
#
#   tail -f odrl_primary_shards.log
#
#   This stage:
#
#   - Completes all eight primary shards.
#   - Accepts valid records.
#   - Collects invalid records.
#   - Prepares recovery JSONL locally.
#   - Does not submit or charge for a recovery Batch.
#
#   ### Inspect recovery candidates
#
#   After Stage 1 finishes:
#
#   RECOVERY_MANIFEST="$(jq -r '.recovery_manifest_path // empty' "$MANIFEST")"
#
#   echo "$RECOVERY_MANIFEST"
#
#   jq '{status,request_count,requests_path,states_path}' \
#     "$RECOVERY_MANIFEST"
#
#   Count exception records:
#
#   RECOVERY_STATES="$(jq -r '.states_path' "$RECOVERY_MANIFEST")"
#
#   wc -l "$RECOVERY_STATES"
#
#   Inspect the first exceptions:
#
#   head -n 5 "$RECOVERY_STATES" | jq .
#
#   The recovery Batch has not been submitted when:
#
#   {
#     "status": "prepared"
#   }
#
#   and the recovery manifest has no batch_id.
#
#   ### Stage 2: Submit the recovery Batch
#
#   When you are satisfied with the exception count:
#
#   nohup env \
#     ODRL_CORRECTION_BATCH_RECOVERY_REASONING_EFFORT=medium \
#     ODRL_CORRECTION_BATCH_RECOVERY_MAX_OUTPUT_TOKENS=16000 \
#     ODRL_CORRECTION_FINAL_SYNC_LIMIT=0 \
#     .venv/bin/python -u \
#     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
#     --batch-recovery-run "$MANIFEST" \
#     --batch-poll-seconds 300 \
#     --log-level INFO \
#     > odrl_recovery_batch.log 2>&1 &
#
#   echo $! > odrl_recovery_batch.pid
#
#   Monitor it:
#
#   tail -f odrl_recovery_batch.log
#
#   After recovery:
#
#   - Valid recovery results replace provisional originals.
#   - Failed recovery results retain their original labels.
#   - Unresolved records are written to each shard’s manual_review.jsonl.
#   - Final train, valid, test, ODRL, and diff files are merged.
#
#   The previous --batch-shard-run command remains available, but it runs both stages
#   automatically without pausing.

# 29/8/2026:
# command history:
#   MANIFEST="data/batch_jobs/odrl_gpt-5.6-luna_20260829T144210Z_67a01c9c/manifest.json"

#   using gpt correct   nohup .venv/bin/python -u     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph     --batch-shard-primary-run "$MANIFEST"     --batch-poll-seconds 300     --log-level INFO     > odrl_primary_shards.log 2>&1 &
#      echo $! > odrl_primary_shards.pid
#    tail odrl_primary_shards.log -f
#    RECOVERY_MANIFEST="$(jq -r '.recovery_manifest_path // empty' "$MANIFEST")"
#    echo "$RECOVERY_MANIFEST"
#    jq '{status,request_count,requests_path,states_path}'     "$RECOVERY_MANIFEST"
#    RECOVERY_STATES="$(jq -r '.states_path' "$RECOVERY_MANIFEST")"
#    wc -l "$RECOVERY_STATES"
#    head -n 5 "$RECOVERY_STATES" | jq .
#    jq -r '[.custom_id, .validation_error] | @tsv'     "$RECOVERY_STATES"     | less

##    recovery:   nohup env     ODRL_CORRECTION_BATCH_RECOVERY_REASONING_EFFORT=medium     ODRL_CORRECTION_BATCH_RECOVERY_MAX_OUTPUT_TOKENS=16000     ODRL_CORRECTION_FINAL_SYNC_LIMIT=0     .venv/bin/python -u     -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph     --batch-recovery-run "$MANIFEST"     --batch-poll-seconds 300     --log-level INFO     > odrl_recovery_batch.log 2>&1 &
#      echo $! > odrl_recovery_batch.pid
#    tail odrl_recovery_batch.log -f
