#!/usr/bin/env python3
"""Deduplicate synchronized ODRL datasets without modifying source files.

The script treats exact ``text`` as the sample identity, keeps each text in
exactly one split, selects one canonical agent correction for duplicate texts,
and rebuilds the NER/ODRL diff files with the new record indices.

Default split ownership is test -> valid -> train. This retains evaluation
examples and removes their duplicates from training, avoiding train/test data
leakage. Canonical corrected labels are selected from existing agent outputs;
the script never invents a new annotation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_output import (
    build_diff_record,
)
from odrl_output import build_odrl_diff_record


SPLITS = ("train", "valid", "test")
MODEL_SUFFIX = "gpt-5.6-luna"


@dataclass(frozen=True)
class Occurrence:
    split: str
    record_index: int
    original: dict[str, Any]
    original_odrl: dict[str, Any]
    corrected: dict[str, Any]
    corrected_odrl: dict[str, Any]
    correction_evidence: dict[str, Any]

    @property
    def text(self) -> str:
        return str(self.original.get("text") or "")


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected a JSON object")
            records.append(value)
    return records


def _write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = ""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = handle.name
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = ""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = handle.name
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def _text_id(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _entity_signature(record: dict[str, Any]) -> frozenset[tuple[int, int, str]]:
    return frozenset(
        (
            int(entity["start"]),
            int(entity["end"]),
            str(entity["label"]),
        )
        for entity in record.get("entities") or []
    )


def _odrl_signature(record: dict[str, Any]) -> tuple[tuple[str, ...], ...]:
    fields = (
        "source_text",
        "assignee",
        "action",
        "asset",
        "rule_type",
        "constraint",
        "purpose",
    )
    return tuple(
        tuple(" ".join(str(rule.get(field) or "").split()) for field in fields)
        for rule in record.get("odrl") or []
        if isinstance(rule, dict)
    )


def _invalid_entity_count(record: dict[str, Any]) -> int:
    text = str(record.get("text") or "")
    invalid = 0
    for entity in record.get("entities") or []:
        try:
            start = int(entity["start"])
            end = int(entity["end"])
            label = str(entity["label"])
        except (KeyError, TypeError, ValueError):
            invalid += 1
            continue
        if not (0 <= start < end <= len(text)) or not label:
            invalid += 1
    return invalid


def _overlap_count(record: dict[str, Any]) -> int:
    entities = list(record.get("entities") or [])
    count = 0
    for index, left in enumerate(entities):
        for right in entities[index + 1:]:
            if max(int(left["start"]), int(right["start"])) < min(
                int(left["end"]), int(right["end"])
            ):
                count += 1
    return count


def _symmetric_distance(left: frozenset[Any], right: frozenset[Any]) -> int:
    return len(left ^ right)


def choose_canonical_correction(
    occurrences: list[Occurrence],
    split_rank: dict[str, int],
    decision: dict[str, Any] | None = None,
) -> tuple[Occurrence, dict[str, Any]]:
    """Choose an existing correction closest to all duplicate candidates.

    A manual decision wins when supplied. Otherwise the selection score is:
    minimum total entity-set distance, highest exact-label vote, minimum ODRL
    distance, valid spans, fewer overlaps, preferred owner split, then index.
    """
    if decision:
        wanted_split = str(decision.get("split") or "")
        wanted_index = int(decision.get("record_index") or 0)
        for occurrence in occurrences:
            if occurrence.split == wanted_split and occurrence.record_index == wanted_index:
                return occurrence, {
                    "method": "manual_decision",
                    "score": None,
                    "manual_decision": decision,
                }
        raise ValueError(
            f"Manual decision {wanted_split}:{wanted_index} does not belong to "
            f"text_id={_text_id(occurrences[0].text)}"
        )

    entity_signatures = [_entity_signature(item.corrected) for item in occurrences]
    odrl_signatures = [_odrl_signature(item.corrected_odrl) for item in occurrences]
    entity_votes = Counter(entity_signatures)
    scored: list[tuple[tuple[Any, ...], int]] = []
    for index, occurrence in enumerate(occurrences):
        entity_signature = entity_signatures[index]
        odrl_signature = odrl_signatures[index]
        entity_distance = sum(
            _symmetric_distance(entity_signature, other)
            for other in entity_signatures
        )
        odrl_distance = sum(
            0 if odrl_signature == other else 1
            for other in odrl_signatures
        )
        score = (
            entity_distance,
            -entity_votes[entity_signature],
            odrl_distance,
            _invalid_entity_count(occurrence.corrected),
            _overlap_count(occurrence.corrected),
            split_rank[occurrence.split],
            occurrence.record_index,
        )
        scored.append((score, index))
    score, selected_index = min(scored)
    return occurrences[selected_index], {
        "method": "automatic_consensus_medoid",
        "score": list(score),
        "score_fields": [
            "total_entity_symmetric_difference",
            "negative_exact_entity_vote_count",
            "odrl_disagreement_count",
            "invalid_entity_count",
            "overlap_count",
            "split_priority_rank",
            "source_record_index",
        ],
    }


def _load_decisions(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("The decisions file must contain a JSON object keyed by text_id.")
    return {
        str(key): dict(decision)
        for key, decision in value.items()
        if isinstance(decision, dict) and decision.get("reviewed") is True
    }


def _paths(data_dir: Path, split: str, model_suffix: str) -> dict[str, Path]:
    return {
        "original": data_dir / f"{split}.txt",
        "original_odrl": data_dir / f"{split}_odrl.txt",
        "corrected": data_dir / f"{split}_correct_with_agent_{model_suffix}.txt",
        "corrected_odrl": data_dir / f"{split}_odrl_with_agent_{model_suffix}.txt",
        "ner_diff": data_dir / f"{split}_diffs_from_correct_{model_suffix}.txt",
        "odrl_diff": data_dir / f"{split}_odrl_diffs_from_correct_{model_suffix}.txt",
    }


def load_occurrences(data_dir: Path, model_suffix: str) -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    for split in SPLITS:
        paths = _paths(data_dir, split, model_suffix)
        for path in paths.values():
            if not path.is_file():
                raise FileNotFoundError(f"Required synchronized file is missing: {path}")
        original = _load_jsonl(paths["original"])
        original_odrl = _load_jsonl(paths["original_odrl"])
        corrected = _load_jsonl(paths["corrected"])
        corrected_odrl = _load_jsonl(paths["corrected_odrl"])
        expected = len(original)
        aligned = {
            "original_odrl": original_odrl,
            "corrected": corrected,
            "corrected_odrl": corrected_odrl,
        }
        for name, records in aligned.items():
            if len(records) != expected:
                raise ValueError(
                    f"{paths[name]} has {len(records)} rows; expected {expected} "
                    f"to align with {paths['original']}"
                )
        sparse_diff = {
            int(record.get("record_index") or 0): record
            for record in _load_jsonl(paths["ner_diff"])
        }
        for index in range(expected):
            text = str(original[index].get("text") or "")
            if not text:
                raise ValueError(f"{paths['original']}:{index + 1}: empty text")
            for name, records in aligned.items():
                if str(records[index].get("text") or "") != text:
                    raise ValueError(
                        f"{paths[name]}:{index + 1} text does not match the source split"
                    )
            diff = sparse_diff.get(index + 1) or {}
            occurrences.append(Occurrence(
                split=split,
                record_index=index + 1,
                original=original[index],
                original_odrl=original_odrl[index],
                corrected=corrected[index],
                corrected_odrl=corrected_odrl[index],
                correction_evidence=dict(diff.get("correction_evidence") or {}),
            ))
    return occurrences


def _owner_occurrence(
    occurrences: list[Occurrence], owner_split: str
) -> Occurrence:
    candidates = [item for item in occurrences if item.split == owner_split]
    if not candidates:
        raise ValueError(f"No occurrence exists in owner split {owner_split}")
    original_signatures = {
        _entity_signature(item.original) for item in occurrences
    }
    if len(original_signatures) != 1:
        raise ValueError(
            f"Original annotations conflict for text_id={_text_id(occurrences[0].text)}; "
            "manual source-data reconciliation is required."
        )
    return min(candidates, key=lambda item: item.record_index)


def deduplicate(
    *,
    data_dir: Path,
    output_dir: Path,
    model_suffix: str,
    split_priority: list[str],
    decisions_path: Path | None = None,
    require_reviewed_gold: bool = False,
) -> dict[str, Any]:
    if set(split_priority) != set(SPLITS) or len(split_priority) != len(SPLITS):
        raise ValueError("--split-priority must contain train, valid, and test once each.")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(
            f"Output directory is not empty: {output_dir}. Choose a new directory."
        )
    output_dir.mkdir(parents=True, exist_ok=True)

    all_occurrences = load_occurrences(data_dir, model_suffix)
    groups: dict[str, list[Occurrence]] = defaultdict(list)
    for occurrence in all_occurrences:
        groups[occurrence.text].append(occurrence)

    decisions = _load_decisions(decisions_path)
    split_rank = {split: index for index, split in enumerate(split_priority)}
    assigned: dict[str, list[tuple[Occurrence, Occurrence, dict[str, Any]]]] = {
        split: [] for split in SPLITS
    }
    duplicate_audit: list[dict[str, Any]] = []
    conflict_audit: list[dict[str, Any]] = []
    decisions_template: dict[str, dict[str, Any]] = {}

    # Preserve source order inside the owner split while assigning every text
    # to the highest-priority split in which it occurs.
    ordered_texts = sorted(
        groups,
        key=lambda text: min(
            (split_rank[item.split], item.record_index)
            for item in groups[text]
        ),
    )
    for text in ordered_texts:
        candidates = groups[text]
        owner_split = min(candidates, key=lambda item: split_rank[item.split]).split
        owner = _owner_occurrence(candidates, owner_split)
        text_id = _text_id(text)
        canonical, selection = choose_canonical_correction(
            candidates,
            split_rank,
            decisions.get(text_id),
        )
        assigned[owner_split].append((owner, canonical, selection))

        entity_variants = len({_entity_signature(item.corrected) for item in candidates})
        audit = {
            "text_id": text_id,
            "text": text,
            "occurrence_count": len(candidates),
            "owner_split": owner_split,
            "corrected_entity_variant_count": entity_variants,
            "has_corrected_label_conflict": entity_variants > 1,
            "requires_manual_gold_review": (
                entity_variants > 1 and selection["method"] != "manual_decision"
            ),
            "selected_gold": {
                "split": canonical.split,
                "record_index": canonical.record_index,
                "entities": canonical.corrected.get("entities") or [],
            },
            "selection": selection,
            "occurrences": [
                {
                    "split": item.split,
                    "record_index": item.record_index,
                    "entities": item.corrected.get("entities") or [],
                    "overlap_count": _overlap_count(item.corrected),
                }
                for item in candidates
            ],
        }
        if len(candidates) > 1:
            duplicate_audit.append(audit)
        if entity_variants > 1:
            conflict_audit.append(audit)
            decisions_template[text_id] = {
                "split": canonical.split,
                "record_index": canonical.record_index,
                "reviewed": False,
                "comment": "Automatic consensus suggestion; verify before setting reviewed=true.",
            }

    unresolved_conflict_count = sum(
        1 for audit in conflict_audit if audit["requires_manual_gold_review"]
    )
    if require_reviewed_gold and unresolved_conflict_count:
        review_path = decisions_path or (
            data_dir / "deduplicated_gpt-5.6-luna" / "gold_decisions_template.json"
        )
        raise RuntimeError(
            f"{unresolved_conflict_count} corrected-label conflicts still require "
            f"review in {review_path}. For each verified choice, set "
            "reviewed=true and select its split/record_index, then rerun this "
            "command. Strict validation stopped before writing any dataset files."
        )

    counts: dict[str, dict[str, int]] = {}
    output_paths: list[str] = []
    for split in SPLITS:
        rows = sorted(
            assigned[split],
            key=lambda item: item[0].record_index,
        )
        original_rows: list[dict[str, Any]] = []
        original_odrl_rows: list[dict[str, Any]] = []
        corrected_rows: list[dict[str, Any]] = []
        corrected_odrl_rows: list[dict[str, Any]] = []
        ner_diffs: list[dict[str, Any]] = []
        odrl_diffs: list[dict[str, Any]] = []

        for new_index, (owner, canonical, _) in enumerate(rows, 1):
            original_record = dict(owner.original)
            original_odrl_record = dict(owner.original_odrl)
            corrected_record = dict(canonical.corrected)
            corrected_odrl_record = dict(canonical.corrected_odrl)
            original_rows.append(original_record)
            original_odrl_rows.append(original_odrl_record)
            corrected_rows.append(corrected_record)
            corrected_odrl_rows.append(corrected_odrl_record)

            evidence = canonical.correction_evidence
            diff_state = {
                "record_index": new_index,
                "source_text": owner.text,
                "original_entities": original_record.get("entities") or [],
                "corrected_entities": corrected_record.get("entities") or [],
                "selected_from": evidence.get("selected_from") or "ai_reconciliation",
                "endpoint_rules": evidence.get("endpoint_rules") or [],
                "validated_policy_rules": evidence.get("validated_policy_rules") or [],
                "correction_warnings": evidence.get("warnings") or [],
            }
            ner_diff = build_diff_record(diff_state)
            if ner_diff["diffs"]["has_changes"]:
                ner_diffs.append(ner_diff)
            odrl_diff = build_odrl_diff_record({
                "record_index": new_index,
                "source_text": owner.text,
                "original_odrl_record": original_odrl_record,
                "corrected_odrl_record": corrected_odrl_record,
            })
            if odrl_diff["diffs"]["has_changes"]:
                odrl_diffs.append(odrl_diff)

        paths = _paths(output_dir, split, model_suffix)
        payloads = {
            "original": original_rows,
            "original_odrl": original_odrl_rows,
            "corrected": corrected_rows,
            "corrected_odrl": corrected_odrl_rows,
            "ner_diff": ner_diffs,
            "odrl_diff": odrl_diffs,
        }
        for name, records in payloads.items():
            _write_jsonl(paths[name], records)
            output_paths.append(str(paths[name]))
        counts[split] = {
            "source_rows": sum(1 for item in all_occurrences if item.split == split),
            "deduplicated_rows": len(rows),
            "removed_rows": sum(1 for item in all_occurrences if item.split == split) - len(rows),
            "ner_diff_rows": len(ner_diffs),
            "odrl_diff_rows": len(odrl_diffs),
        }

    _write_jsonl(output_dir / "duplicate_samples.jsonl", duplicate_audit)
    _write_jsonl(output_dir / "corrected_gold_conflicts.jsonl", conflict_audit)
    _write_json(output_dir / "gold_decisions_template.json", decisions_template)
    manifest = {
        "source_data_dir": str(data_dir.resolve()),
        "output_dir": str(output_dir.resolve()),
        "model_suffix": model_suffix,
        "split_priority": split_priority,
        "selection_policy": (
            "Existing correction with minimum total entity symmetric difference; "
            "ties prefer exact votes, ODRL agreement, valid/non-overlapping spans, "
            "split priority, and source index. Review conflicts before treating "
            "automatic selections as definitive human gold."
        ),
        "source_record_count": len(all_occurrences),
        "unique_text_count": len(groups),
        "removed_duplicate_count": len(all_occurrences) - len(groups),
        "duplicate_text_group_count": len(duplicate_audit),
        "corrected_gold_conflict_count": len(conflict_audit),
        "unresolved_gold_conflict_count": unresolved_conflict_count,
        "manual_decision_count": sum(
            1 for audit in conflict_audit
            if audit["selection"]["method"] == "manual_decision"
        ),
        "require_reviewed_gold": require_reviewed_gold,
        "counts": counts,
        "audit_files": {
            "duplicates": str(output_dir / "duplicate_samples.jsonl"),
            "corrected_gold_conflicts": str(output_dir / "corrected_gold_conflicts.jsonl"),
            "gold_decisions_template": str(output_dir / "gold_decisions_template.json"),
        },
        "output_files": output_paths,
    }
    _write_json(output_dir / "deduplication_manifest.json", manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Deduplicate synchronized original and agent-corrected ODRL splits."
    )
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/deduplicated_gpt-5.6-luna"),
        help="New output directory; source files are never overwritten.",
    )
    parser.add_argument("--model-suffix", default=MODEL_SUFFIX)
    parser.add_argument(
        "--split-priority",
        nargs=3,
        choices=SPLITS,
        default=["test", "valid", "train"],
        metavar=("FIRST", "SECOND", "THIRD"),
        help="Which split owns text occurring in multiple splits.",
    )
    parser.add_argument(
        "--decisions-file",
        type=Path,
        help=(
            "Optional JSON object mapping text_id to "
            "{'split': '...', 'record_index': N, 'reviewed': true} for "
            "manually reviewed gold. Unreviewed template entries are ignored."
        ),
    )
    parser.add_argument(
        "--require-reviewed-gold",
        action="store_true",
        help="Refuse to write datasets while any corrected-label conflict is unreviewed.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    manifest = deduplicate(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        model_suffix=args.model_suffix,
        split_priority=list(args.split_priority),
        decisions_path=args.decisions_file,
        require_reviewed_gold=args.require_reviewed_gold,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    print("\nOriginal files were not modified.")
    print(f"Review: {manifest['audit_files']['corrected_gold_conflicts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
