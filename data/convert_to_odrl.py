#!/usr/bin/env python3
"""Convert span-annotated dataset splits into ODRL JSONL files.

The input files are expected to contain one JSON object per line with at least:

    {"text": "...", "entities": [{"start": 0, "end": 4, "label": "ASSET"}, ...]}

Each output line is written as:

    {"text": "...", "odrl": [{"policy_rule_id": "policy-rule-1", ...}, ...]}

This reuses the repository's tokenization and ODRL formatting rules so the
generated files stay consistent with the API and correction workflow.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

# Make the repository root importable when the script is run directly.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from odrl_output import build_odrl_record_from_entities


ODRL_FIELDS = (
    "policy_rule_id",
    "source_text",
    "assignee",
    "action",
    "asset",
    "rule_type",
    "constraint",
    "purpose",
)


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number}: expected a JSON object")
            records.append(record)
    return records


def _normalize_record(record: dict[str, Any], *, record_number: int) -> dict[str, Any]:
    text = str(record.get("text") or "").strip()
    if not text:
        raise ValueError(f"record {record_number}: missing text")

    entities = record.get("entities") or []
    if not isinstance(entities, list):
        raise ValueError(f"record {record_number}: 'entities' must be a list")

    cleaned_entities: list[dict[str, Any]] = []
    for entity in entities:
        if not isinstance(entity, dict):
            raise ValueError(f"record {record_number}: malformed entity {entity!r}")
        if not all(key in entity for key in ("start", "end", "label")):
            raise ValueError(f"record {record_number}: entity missing start/end/label")
        cleaned_entities.append({
            "start": int(entity["start"]),
            "end": int(entity["end"]),
            "label": str(entity["label"]),
        })

    return {"text": text, "entities": cleaned_entities}


def convert_record(record: dict[str, Any], *, record_number: int) -> dict[str, Any]:
    """Convert one span-annotated record into the ODRL output structure."""
    normalized = _normalize_record(record, record_number=record_number)
    text = normalized["text"]
    entities = normalized["entities"]
    return build_odrl_record_from_entities(text, entities)


def convert_file(input_path: Path, output_path: Path) -> int:
    records = _load_jsonl(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    converted: list[str] = []
    for record_number, record in enumerate(records, 1):
        converted.append(json.dumps(
            convert_record(record, record_number=record_number),
            ensure_ascii=False,
        ))

    output_path.write_text("\n".join(converted) + "\n", encoding="utf-8")
    return len(converted)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert train/valid/test span annotations into ODRL JSONL.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Directory containing train.txt, valid.txt, and test.txt.",
    )
    parser.add_argument(
        "--suffix",
        default="_odrl",
        help="Output filename suffix before .txt (default: _odrl).",
    )
    parser.add_argument(
        "--splits",
        nargs="+",
        default=["train", "valid", "test"],
        help="Dataset splits to convert.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    total = 0
    for split in args.splits:
        input_path = args.data_dir / f"{split}.txt"
        output_path = args.data_dir / f"{split}{args.suffix}.txt"
        if not input_path.exists():
            raise FileNotFoundError(f"Missing input file: {input_path}")
        count = convert_file(input_path, output_path)
        print(f"Wrote {count} record(s) to {output_path}")
        total += count

    print(f"Converted {total} record(s) across {len(args.splits)} split(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
