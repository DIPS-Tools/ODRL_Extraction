"""Focused workflow for correcting ODRL NER JSONL datasets.

Workflow:
    __start__
      -> node_initialize
      -> node_odrl_extraction
      -> node_odrl_correct
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

from odrl_correct_agent.query_process.agent.nodes.node_initialize import node_initialize
from odrl_correct_agent.query_process.agent.nodes.node_odrl_correct import node_odrl_correct
from odrl_correct_agent.query_process.agent.nodes.node_odrl_extraction import node_odrl_extraction
from odrl_correct_agent.query_process.agent.nodes.node_odrl_output import node_odrl_output
from odrl_correct_agent.query_process.agent.state import (
    ODRLCorrectionState,
    create_correction_state,
    default_prompt_path,
)

from odrl_correct_agent.utils.draw_mermaid_png import draw_mermaid_png

Node = Callable[[ODRLCorrectionState], Awaitable[dict[str, Any]]]
logger = logging.getLogger("odrl_correct_agent")
WORKFLOW_NODE_NAMES = (
    "__start__",
    "node_initialize",
    "node_odrl_extraction",
    "node_odrl_correct",
    "node_odrl_output",
    "__end__",
)
WORKFLOW_NODES: tuple[Node, ...] = (
    node_initialize,
    node_odrl_extraction,
    node_odrl_correct,
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
) -> tuple[Path, Path, list[ODRLCorrectionState]]:
    """Correct one JSONL dataset and write NER plus text-to-ODRL files."""
    source_path = Path(dataset_path).expanduser().resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {source_path}")
    destination = Path(output_dir).expanduser().resolve() if output_dir else source_path.parent
    records = _read_jsonl(source_path, limit=limit)
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
            )
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
    _write_jsonl_atomic(ner_path, (state["corrected_record"] for state in states))
    _write_jsonl_atomic(text_odrl_path, (state["text_odrl_record"] for state in states))
    logger.info(
        "dataset=%s status=completed records=%d ner_output=%s odrl_output=%s",
        source_path.name,
        len(states),
        ner_path,
        text_odrl_path,
    )
    return ner_path, text_odrl_path, states


async def correct_all_splits(
    data_dir: str | Path,
    **options: Any,
) -> tuple[list[Path], list[Path], list[ODRLCorrectionState]]:
    """Correct train/valid/test and write model-specific files per split."""
    source_dir = Path(data_dir).expanduser().resolve()
    ner_paths: list[Path] = []
    odrl_paths: list[Path] = []
    all_states: list[ODRLCorrectionState] = []
    for filename in ("train.txt", "valid.txt", "test.txt"):
        ner_path, odrl_path, states = await correct_dataset(
            source_dir / filename,
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
        "--log-level",
        default=os.getenv("ODRL_CORRECTION_LOG_LEVEL", "INFO").upper(),
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        help="Progress log level (default: INFO).",
    )
    return parser


async def _async_main(args: argparse.Namespace) -> int:
    if args.dataset and args.all_splits:
        raise ValueError("Use either --dataset or --all-splits, not both.")
    if not args.dataset and not args.all_splits:
        await run_demo()
        return 0
    if args.limit is not None and args.limit <= 0:
        raise ValueError("--limit must be greater than zero.")
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


# python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
#     --all-splits \
#     --data-dir data
#
#   python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph
#
#   Correct only test.txt:
#
#   python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
#     --dataset data/test.txt
#
#   Correct all splits:
#
#   python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
#     --all-splits \
#     --data-dir data
