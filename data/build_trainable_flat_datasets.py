#!/usr/bin/env python3
"""Create explicit flat-BIO datasets from corrected span JSONL files.

The source correction files remain unchanged. When two entities overlap, the
entity with the stronger ODRL training priority is retained and the other is
written to an audit file. No records are deleted.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


LABEL_PRIORITY = {
    "RULE_TYPE-PERMISSION": 0,
    "RULE_TYPE-OBLIGATION": 0,
    "RULE_TYPE-PROHIBITION": 0,
    "ACTION": 1,
    "ASSIGNEE": 2,
    "ASSET": 3,
    "CONSTRAINT": 4,
    "PURPOSE": 5,
}


def _overlaps(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return max(int(left["start"]), int(right["start"])) < min(
        int(left["end"]), int(right["end"])
    )


def flatten_entities(
    text: str,
    entities: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[int, int, str]] = set()
    for index, raw in enumerate(entities, start=1):
        start = int(raw["start"])
        end = int(raw["end"])
        label = str(raw["label"])
        if label not in LABEL_PRIORITY:
            raise ValueError(f"entity {index} has unsupported label {label!r}")
        if not 0 <= start < end <= len(text):
            raise ValueError(
                f"entity {index} span [{start}, {end}) is outside source text"
            )
        key = (start, end, label)
        if key not in seen:
            normalized.append({"start": start, "end": end, "label": label})
            seen.add(key)

    # Core deontic/action labels win over broad contextual spans. Within one
    # label, prefer the more specific (shorter) span, then source order.
    candidates = sorted(
        normalized,
        key=lambda item: (
            LABEL_PRIORITY[item["label"]],
            int(item["end"]) - int(item["start"]),
            int(item["start"]),
            int(item["end"]),
            item["label"],
        ),
    )
    retained: list[dict[str, Any]] = []
    removed: list[dict[str, Any]] = []
    for candidate in candidates:
        conflicts = [item for item in retained if _overlaps(candidate, item)]
        if conflicts:
            removed.append({
                "removed_entity": {
                    **candidate,
                    "text": text[candidate["start"]:candidate["end"]],
                },
                "retained_conflicts": [
                    {
                        **item,
                        "text": text[item["start"]:item["end"]],
                    }
                    for item in conflicts
                ],
                "policy": "rule_type>action>assignee>asset>constraint>purpose",
            })
            continue
        retained.append(candidate)
    retained.sort(key=lambda item: (item["start"], item["end"], item["label"]))
    return retained, removed


def build_split(
    source: Path,
    destination: Path,
    audit_path: Path,
) -> dict[str, int]:
    records = 0
    changed = 0
    removed_count = 0
    audits: list[dict[str, Any]] = []
    outputs: list[dict[str, Any]] = []
    with source.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            text = str(record.get("text") or "")
            retained, removed = flatten_entities(
                text, [dict(item) for item in record.get("entities") or []]
            )
            output = dict(record)
            output["entities"] = retained
            outputs.append(output)
            records += 1
            if removed:
                changed += 1
                removed_count += len(removed)
                audits.append({
                    "record_index": line_number,
                    "text": text,
                    "original_entities": record.get("entities") or [],
                    "flat_entities": retained,
                    "removed_overlaps": removed,
                })
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        for record in outputs:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    with audit_path.open("w", encoding="utf-8") as handle:
        for record in audits:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return {
        "records": records,
        "changed_records": changed,
        "removed_entities": removed_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build non-overlapping flat-BIO datasets without deleting records."
    )
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--model-name", default="gpt-5.6-luna")
    parser.add_argument("--output-tag", default="flat")
    args = parser.parse_args()
    root = Path(args.data_dir)
    summary: dict[str, dict[str, int]] = {}
    for split in ("train", "valid", "test"):
        stem = f"{split}_correct_with_agent_{args.model_name}"
        source = root / f"{stem}.txt"
        destination = root / f"{stem}_{args.output_tag}.txt"
        audit = root / f"{stem}_{args.output_tag}_overlap_audit.jsonl"
        summary[split] = build_split(source, destination, audit)
        print(f"{split}: {destination} {summary[split]}")
        print(f"{split} overlap audit: {audit}")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
