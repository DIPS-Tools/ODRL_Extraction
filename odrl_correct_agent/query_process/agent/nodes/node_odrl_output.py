"""Prepare corrected NER and text-to-ODRL JSONL records."""

from __future__ import annotations

from typing import Any

from odrl_correct_agent.query_process.agent.state import ODRLCorrectionState


TEXT_ODRL_FIELDS = (
    "policy_rule_id",
    "assignee",
    "action",
    "asset",
    "rule_type",
    "constraint",
    "purpose",
)


async def node_odrl_output(state: ODRLCorrectionState) -> dict[str, Any]:
    """Create the two stable output schemas consumed by training jobs."""
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
    return {
        "corrected_record": {"text": text, "entities": entities},
        "text_odrl_record": {"text": text, "odrl": rules},
    }
