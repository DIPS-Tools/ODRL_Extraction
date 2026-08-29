"""Validate that corrected annotations are usable by a flat BIO tagger."""

from __future__ import annotations

from typing import Any

from odrl_correct_agent.odrl_correct_process.agent.state import ODRLCorrectionState


ALLOWED_ENTITY_LABELS = frozenset({
    "ASSIGNEE",
    "ACTION",
    "ASSET",
    "CONSTRAINT",
    "PURPOSE",
    "RULE_TYPE-PERMISSION",
    "RULE_TYPE-OBLIGATION",
    "RULE_TYPE-PROHIBITION",
})


def find_entity_overlaps(
    entities: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Return every pair whose half-open character spans intersect."""
    ordered = sorted(
        (dict(entity) for entity in entities),
        key=lambda item: (int(item["start"]), int(item["end"]), str(item["label"])),
    )
    overlaps: list[dict[str, Any]] = []
    for index, left in enumerate(ordered):
        for right in ordered[index + 1:]:
            if int(right["start"]) >= int(left["end"]):
                break
            if max(int(left["start"]), int(right["start"])) < min(
                int(left["end"]), int(right["end"])
            ):
                overlaps.append({"left": left, "right": right})
    return overlaps


def validate_flat_ner_entities(
    source_text: str,
    entities: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Normalize and strictly validate one flat, character-span annotation."""
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[int, int, str]] = set()
    for index, raw in enumerate(entities, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"entity {index} must be an object")
        try:
            start = int(raw["start"])
            end = int(raw["end"])
            label = str(raw["label"]).strip()
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"entity {index} has an invalid start/end/label") from exc
        if label not in ALLOWED_ENTITY_LABELS:
            raise ValueError(f"entity {index} has unsupported label {label!r}")
        if not 0 <= start < end <= len(source_text):
            raise ValueError(
                f"entity {index} span [{start}, {end}) is outside source length "
                f"{len(source_text)}"
            )
        if not source_text[start:end].strip():
            raise ValueError(f"entity {index} selects only whitespace")
        key = (start, end, label)
        if key not in seen:
            normalized.append({"start": start, "end": end, "label": label})
            seen.add(key)

    normalized.sort(key=lambda item: (item["start"], item["end"], item["label"]))
    overlaps = find_entity_overlaps(normalized)
    if overlaps:
        descriptions = []
        for pair in overlaps[:5]:
            left = pair["left"]
            right = pair["right"]
            descriptions.append(
                f"{left['label']}[{left['start']}:{left['end']}]={source_text[left['start']:left['end']]!r} "
                f"overlaps {right['label']}[{right['start']}:{right['end']}]="
                f"{source_text[right['start']:right['end']]!r}"
            )
        suffix = "" if len(overlaps) <= 5 else f"; and {len(overlaps) - 5} more"
        raise ValueError(
            "flat BIO annotations cannot overlap: " + "; ".join(descriptions) + suffix
        )
    return normalized


async def node_flat_ner_validate(state: ODRLCorrectionState) -> dict[str, Any]:
    """Reject invalid or overlapping corrected spans before output is built."""
    source_text = str(state.get("source_text") or "")
    grounding_warnings = [
        str(value) for value in state.get("grounding_warnings") or [] if value
    ]
    if grounding_warnings:
        raise ValueError(
            "not every AI component could be grounded to an exact source quote: "
            + "; ".join(grounding_warnings[:5])
        )
    rules = (
        state.get("validated_policy_rules") or []
        if state.get("selected_from") == "ai_reconciliation"
        else []
    )
    allow_partial_rules = bool(state.get("allow_partial_rules"))
    for index, rule in enumerate(rules, start=1):
        if not isinstance(rule, dict):
            raise ValueError(f"policy rule {index} must be an object")
        action = str(rule.get("action") or "").strip()
        rule_type = str(rule.get("rule_type") or "").strip()
        if not allow_partial_rules and not action:
            raise ValueError(f"policy rule {index} has no ACTION")
        if (
            (rule_type or not allow_partial_rules)
            and rule_type not in {"permission", "obligation", "prohibition"}
        ):
            raise ValueError(
                f"policy rule {index} has invalid rule_type {rule_type!r}"
            )
        source_quote = str(rule.get("source_text") or "").strip()
        if source_quote and source_quote not in source_text:
            raise ValueError(
                f"policy rule {index} source_text is not an exact source quote"
            )
    entities = validate_flat_ner_entities(
        source_text,
        [dict(entity) for entity in state.get("corrected_entities") or []],
    )
    return {
        "corrected_entities": entities,
        "flat_ner_validated": True,
        "overlap_count": 0,
    }
