"""Prepare corrected NER, text-to-ODRL, and audit-diff records."""

from __future__ import annotations

from typing import Any

from odrl_correct_agent.odrl_correct_process.agent.state import ODRLCorrectionState


TEXT_ODRL_FIELDS = (
    "policy_rule_id",
    "assignee",
    "action",
    "asset",
    "rule_type",
    "constraint",
    "purpose",
)


def _entity_view(text: str, entity: dict[str, Any]) -> dict[str, Any]:
    """Add the annotated source quote to an entity for human review."""
    start = int(entity["start"])
    end = int(entity["end"])
    return {
        "start": start,
        "end": end,
        "label": str(entity["label"]),
        "text": text[start:end],
    }


def _overlap_size(left: dict[str, Any], right: dict[str, Any]) -> int:
    return max(
        0,
        min(int(left["end"]), int(right["end"]))
        - max(int(left["start"]), int(right["start"])),
    )


def _changed_pair_score(
    text: str,
    original: dict[str, Any],
    corrected: dict[str, Any],
) -> tuple[float, str] | None:
    """Score plausible old/new versions of the same annotation.

    Exact entities are handled as unchanged before this function is called.
    A changed pair must share a span, overlap, or quote the same text with the
    same label. Unrelated entities remain explicit additions/deletions.
    """
    same_span = (
        int(original["start"]) == int(corrected["start"])
        and int(original["end"]) == int(corrected["end"])
    )
    same_label = str(original["label"]) == str(corrected["label"])
    overlap = _overlap_size(original, corrected)
    original_quote = text[int(original["start"]):int(original["end"])]
    corrected_quote = text[int(corrected["start"]):int(corrected["end"])]
    same_quote = original_quote.casefold() == corrected_quote.casefold()

    if same_span:
        return (1000.0 + (100.0 if same_label else 0.0), "same_span")
    if overlap:
        union = max(int(original["end"]), int(corrected["end"])) - min(
            int(original["start"]), int(corrected["start"])
        )
        return (
            500.0 + (200.0 if same_label else 0.0) + (overlap / union),
            "overlapping_span",
        )
    if same_label and same_quote:
        return (300.0, "same_label_and_text")
    return None


def build_diff_record(state: ODRLCorrectionState) -> dict[str, Any]:
    """Build a detailed, deterministic comparison for one corrected record."""
    text = str(state.get("source_text") or "")
    original_entities = [
        dict(entity) for entity in state.get("original_entities") or []
    ]
    corrected_entities = [
        dict(entity) for entity in state.get("corrected_entities") or []
    ]

    unmatched_original = set(range(len(original_entities)))
    unmatched_corrected = set(range(len(corrected_entities)))
    unchanged: list[dict[str, Any]] = []

    # Pair exact duplicates first so only genuine changes reach fuzzy pairing.
    for original_index, original in enumerate(original_entities):
        original_key = (
            int(original["start"]),
            int(original["end"]),
            str(original["label"]),
        )
        for corrected_index in sorted(unmatched_corrected):
            corrected = corrected_entities[corrected_index]
            corrected_key = (
                int(corrected["start"]),
                int(corrected["end"]),
                str(corrected["label"]),
            )
            if original_key == corrected_key:
                unchanged.append(_entity_view(text, original))
                unmatched_original.discard(original_index)
                unmatched_corrected.discard(corrected_index)
                break

    candidates: list[tuple[float, int, int, str]] = []
    for original_index in unmatched_original:
        for corrected_index in unmatched_corrected:
            scored = _changed_pair_score(
                text,
                original_entities[original_index],
                corrected_entities[corrected_index],
            )
            if scored is not None:
                score, reason = scored
                candidates.append((score, original_index, corrected_index, reason))

    changed: list[dict[str, Any]] = []
    for _, original_index, corrected_index, match_reason in sorted(
        candidates,
        key=lambda item: (-item[0], item[1], item[2]),
    ):
        if (
            original_index not in unmatched_original
            or corrected_index not in unmatched_corrected
        ):
            continue
        original = original_entities[original_index]
        corrected = corrected_entities[corrected_index]
        field_changes = {
            field: {"from": original[field], "to": corrected[field]}
            for field in ("start", "end", "label")
            if original[field] != corrected[field]
        }
        change_types: list[str] = []
        if "label" in field_changes:
            change_types.append("label_changed")
        if "start" in field_changes or "end" in field_changes:
            change_types.append("boundary_changed")
        changed.append({
            "change_types": change_types,
            "match_reason": match_reason,
            "original_entity": _entity_view(text, original),
            "correct_entity": _entity_view(text, corrected),
            "field_changes": field_changes,
        })
        unmatched_original.remove(original_index)
        unmatched_corrected.remove(corrected_index)

    deleted = [
        {"original_entity": _entity_view(text, original_entities[index])}
        for index in sorted(unmatched_original)
    ]
    added = [
        {"correct_entity": _entity_view(text, corrected_entities[index])}
        for index in sorted(unmatched_corrected)
    ]
    changed.sort(key=lambda item: (
        item["original_entity"]["start"],
        item["correct_entity"]["start"],
    ))
    unchanged.sort(key=lambda item: (item["start"], item["end"], item["label"]))

    return {
        "record_index": int(state.get("record_index") or 0),
        # Keep the requested key spelling for compatibility with the proposed
        # downstream format.
        "origion_version": {"text": text, "entities": original_entities},
        "correct_version": {"text": text, "entities": corrected_entities},
        "diffs": {
            "has_changes": bool(added or deleted or changed),
            "summary": {
                "original_entity_count": len(original_entities),
                "correct_entity_count": len(corrected_entities),
                "unchanged_count": len(unchanged),
                "added_count": len(added),
                "deleted_count": len(deleted),
                "changed_count": len(changed),
            },
            "added": added,
            "deleted": deleted,
            "changed": changed,
            "unchanged": unchanged,
        },
        "correction_evidence": {
            "selected_from": str(state.get("selected_from") or ""),
            "endpoint_rules": list(state.get("endpoint_rules") or []),
            "validated_policy_rules": list(
                state.get("validated_policy_rules") or []
            ),
            "warnings": list(state.get("correction_warnings") or []),
        },
    }


async def node_odrl_output(state: ODRLCorrectionState) -> dict[str, Any]:
    """Create stable training schemas and a human-auditable diff schema."""
    text = str(state.get("source_text") or "")
    entities = [dict(entity) for entity in state.get("corrected_entities") or []]
    rules = [
        {
            field: str(rule.get(field) or "")
            for field in TEXT_ODRL_FIELDS
        }
        for rule in state.get("validated_policy_rules") or []
        if isinstance(rule, dict)
    ]
    output = {
        "corrected_record": {"text": text, "entities": entities},
        "text_odrl_record": {"text": text, "odrl": rules},
    }
    diff_state = dict(state)
    diff_state.update(output)
    output["diff_record"] = build_diff_record(diff_state)
    return output
