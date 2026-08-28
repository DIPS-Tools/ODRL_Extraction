"""Reconcile original NER labels, endpoint rules, and an AI review."""

from __future__ import annotations

import json
import os
import re
from typing import Any, Iterable

from openai import AsyncOpenAI

from odrl_correct_agent.odrl_correct_process.agent.state import ODRLCorrectionState


RULE_FIELDS = (
    "source_text",
    "assignee",
    "action",
    "asset",
    "attributed_party",
    "rule_type",
    "constraint",
    "purpose",
)
TEXT_FIELD_TO_LABEL = {
    "assignee": "ASSIGNEE",
    "action": "ACTION",
    "asset": "ASSET",
    "constraint": "CONSTRAINT",
    "purpose": "PURPOSE",
}
RULE_TYPE_PATTERNS = {
    "prohibition": re.compile(
        r"\b(?:may\s+not|must\s+not|shall\s+not|should\s+not|"
        r"will\s+not|cannot|can\s+not|prohibited\s+from|forbidden\s+to)\b",
        re.IGNORECASE,
    ),
    "permission": re.compile(
        r"\b(?:may(?!\s+not)|can(?!\s+not)|is\s+permitted\s+to|"
        r"are\s+permitted\s+to|permitted\s+to|authorized\s+to|"
        r"authorised\s+to|allowed\s+to)\b",
        re.IGNORECASE,
    ),
    "obligation": re.compile(
        r"\b(?:shall(?!\s+not)|must(?!\s+not)|should(?!\s+not)|"
        r"is\s+required\s+to|are\s+required\s+to|will(?!\s+not))\b",
        re.IGNORECASE,
    ),
}


def _compact(value: Any) -> str:
    return " ".join(str(value or "").split())


def _normalize_rule_type(value: Any) -> str:
    normalized = _compact(value).lower().replace("rule_type-", "")
    aliases = {
        "permit": "permission",
        "permitted": "permission",
        "permission": "permission",
        "oblige": "obligation",
        "obliged": "obligation",
        "obligation": "obligation",
        "prohibit": "prohibition",
        "prohibited": "prohibition",
        "prohibition": "prohibition",
    }
    return aliases.get(normalized, normalized if normalized in RULE_TYPE_PATTERNS else "")


def normalize_rules(raw_rules: Any, source_text: str) -> list[dict[str, str]]:
    """Normalize AI/endpoint rules into one stable schema."""
    if not isinstance(raw_rules, list):
        return []
    rules: list[dict[str, str]] = []
    for raw in raw_rules:
        if not isinstance(raw, dict):
            continue
        rule = {field: _compact(raw.get(field)) for field in RULE_FIELDS}
        rule["source_text"] = rule["source_text"] or source_text
        rule["rule_type"] = _normalize_rule_type(rule["rule_type"])
        rule["selected_from"] = _compact(raw.get("selected_from"))
        if any(rule[field] for field in RULE_FIELDS if field != "source_text"):
            rules.append(rule)
    return rules


def normalize_endpoint_rules(raw_rules: Any, source_text: str) -> list[dict[str, str]]:
    """Normalize endpoint rules and remove their modal prefix from ACTION."""
    rules = normalize_rules(raw_rules, source_text)
    modal_prefix = re.compile(
        r"^(?:may\s+not|must\s+not|shall\s+not|should\s+not|will\s+not|"
        r"cannot|may|can|shall|must|should|will)\s+",
        re.IGNORECASE,
    )
    for rule in rules:
        rule["action"] = modal_prefix.sub("", rule["action"], count=1).strip()
    return rules


def _strip_code_fence(content: str) -> str:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def parse_ai_response(content: Any) -> dict[str, Any]:
    """Parse the required JSON object from an OpenAI-compatible response."""
    if isinstance(content, dict):
        payload = content
    else:
        try:
            payload = json.loads(_strip_code_fence(str(content or "")))
        except json.JSONDecodeError as exc:
            raise ValueError(f"AI correction returned invalid JSON: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise ValueError("AI correction must return one JSON object.")
    if not isinstance(payload.get("validated_policy_rules"), list):
        raise ValueError("AI response must contain 'validated_policy_rules' as a list.")
    return payload


def render_correction_prompt(
    template: str,
    source_text: str,
    original_entities: list[dict[str, Any]],
    endpoint_rules: list[dict[str, str]],
) -> str:
    """Fill the prompt using explicit markers that do not conflict with JSON."""
    # Compact evidence matters for large datasets: the prompt is sent once per
    # record, so indentation and repeated empty keys have a material cost.
    original_with_quotes = [
        {
            "s": entity["start"],
            "e": entity["end"],
            "l": entity["label"],
            "v": source_text[entity["start"]:entity["end"]],
        }
        for entity in original_entities
    ]
    compact_model_rules: list[dict[str, str]] = []
    for rule in endpoint_rules:
        compact_rule = {
            field: str(rule.get(field) or "")
            for field in RULE_FIELDS
            if rule.get(field)
        }
        # The full source is already present once above. Keep source_text only
        # when the endpoint provides a useful atomic clause boundary.
        if compact_rule.get("source_text") == source_text:
            compact_rule.pop("source_text", None)
        compact_model_rules.append(compact_rule)
    replacements = {
        "{{SOURCE_TEXT}}": source_text,
        "{{ORIGINAL_ENTITIES}}": json.dumps(
            original_with_quotes,
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        "{{MODEL_RULES}}": json.dumps(
            compact_model_rules,
            ensure_ascii=False,
            separators=(",", ":"),
        ),
    }
    prompt = template
    for marker, value in replacements.items():
        prompt = prompt.replace(marker, value)
    return prompt


async def _call_ai(prompt: str, model_name: str) -> dict[str, Any]:
    api_key = str(os.getenv("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required for dataset correction.")
    base_url = str(
        os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE") or ""
    ).strip()
    client = AsyncOpenAI(api_key=api_key, base_url=base_url or None)
    request = build_chat_completion_request(prompt, model_name)
    response = await client.chat.completions.create(**request)
    if not response.choices:
        raise ValueError("AI correction returned no choices.")
    return parse_ai_response(response.choices[0].message.content)


def build_chat_completion_request(prompt: str, model_name: str) -> dict[str, Any]:
    """Build the identical request body used by synchronous and Batch calls."""
    request: dict[str, Any] = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
    }
    reasoning_effort = str(
        os.getenv("ODRL_CORRECTION_REASONING_EFFORT") or ""
    ).strip().lower()
    if reasoning_effort:
        allowed_efforts = {"none", "low", "medium", "high", "xhigh", "max"}
        if reasoning_effort not in allowed_efforts:
            raise ValueError(
                "ODRL_CORRECTION_REASONING_EFFORT must be one of: "
                + ", ".join(sorted(allowed_efforts))
            )
        request["reasoning_effort"] = reasoning_effort
    temperature = str(os.getenv("ODRL_CORRECTION_TEMPERATURE") or "").strip()
    if temperature:
        request["temperature"] = float(temperature)
    max_output_tokens = str(
        os.getenv("ODRL_CORRECTION_MAX_OUTPUT_TOKENS") or ""
    ).strip()
    if max_output_tokens:
        request["max_completion_tokens"] = int(max_output_tokens)
    if os.getenv("ODRL_CORRECTION_JSON_MODE", "true").lower() == "true":
        request["response_format"] = {"type": "json_object"}
    return request


def _quote_pattern(quote: str) -> re.Pattern[str] | None:
    parts = quote.strip().split()
    if not parts:
        return None
    return re.compile(r"\s+".join(re.escape(part) for part in parts), re.IGNORECASE)


def _find_quote_spans(
    text: str,
    quote: str,
    scope: tuple[int, int] | None = None,
) -> list[tuple[int, int]]:
    pattern = _quote_pattern(quote)
    if pattern is None:
        return []
    start, end = scope or (0, len(text))
    return [
        (start + match.start(), start + match.end())
        for match in pattern.finditer(text[start:end])
    ]


def _source_scope(text: str, source_quote: str) -> tuple[int, int]:
    spans = _find_quote_spans(text, source_quote)
    return spans[0] if spans else (0, len(text))


def _distance(span: tuple[int, int], anchor: tuple[int, int] | None) -> int:
    if anchor is None:
        return span[0]
    return abs(((span[0] + span[1]) // 2) - ((anchor[0] + anchor[1]) // 2))


def _pick_span(
    candidates: Iterable[tuple[int, int]],
    anchor: tuple[int, int] | None,
) -> tuple[int, int] | None:
    values = list(candidates)
    return min(values, key=lambda span: (_distance(span, anchor), span[0])) if values else None


def _original_rule_type_candidates(
    original_entities: list[dict[str, Any]],
    rule_type: str,
) -> list[tuple[int, int]]:
    label = f"RULE_TYPE-{rule_type.upper()}"
    return [
        (entity["start"], entity["end"])
        for entity in original_entities
        if entity["label"] == label
    ]


def rules_to_entities(
    source_text: str,
    rules: list[dict[str, str]],
    original_entities: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Ground corrected component strings back to exact character offsets."""
    entities: list[dict[str, Any]] = []
    warnings: list[str] = []
    used_rule_type_spans: set[tuple[int, int]] = set()

    for rule_index, rule in enumerate(rules, start=1):
        scope = _source_scope(source_text, rule.get("source_text", ""))
        action_candidates = _find_quote_spans(
            source_text,
            rule.get("action", ""),
            scope,
        )
        action_anchor = _pick_span(action_candidates, None)

        for field, label in TEXT_FIELD_TO_LABEL.items():
            quote = rule.get(field, "")
            if not quote:
                continue
            span = _pick_span(
                _find_quote_spans(source_text, quote, scope),
                action_anchor,
            )
            if span is None:
                # A valid component must be a source quote. Do not invent an
                # approximate offset that would corrupt the training data.
                warnings.append(
                    f"rule {rule_index}: {field} is not an exact source quote: {quote!r}"
                )
                continue
            entities.append({"start": span[0], "end": span[1], "label": label})

        rule_type = rule.get("rule_type", "")
        if not rule_type:
            continue
        pattern = RULE_TYPE_PATTERNS.get(rule_type)
        candidates: list[tuple[int, int]] = []
        if pattern is not None:
            candidates = [
                (scope[0] + match.start(), scope[0] + match.end())
                for match in pattern.finditer(source_text[scope[0]:scope[1]])
                if (scope[0] + match.start(), scope[0] + match.end())
                not in used_rule_type_spans
            ]
        if not candidates:
            candidates = [
                span
                for span in _original_rule_type_candidates(original_entities, rule_type)
                if scope[0] <= span[0] < span[1] <= scope[1]
                and span not in used_rule_type_spans
            ]
        span = _pick_span(candidates, action_anchor)
        if span is None:
            warnings.append(
                f"rule {rule_index}: cannot locate the {rule_type} marker in source text"
            )
            continue
        used_rule_type_spans.add(span)
        entities.append({
            "start": span[0],
            "end": span[1],
            "label": f"RULE_TYPE-{rule_type.upper()}",
        })

    unique = {
        (entity["start"], entity["end"], entity["label"]): entity
        for entity in entities
    }
    ordered = sorted(
        unique.values(),
        key=lambda entity: (entity["start"], entity["end"], entity["label"]),
    )
    return ordered, warnings


def _original_entities_to_rules(
    source_text: str,
    entities: list[dict[str, Any]],
) -> list[dict[str, str]]:
    """Build a lossless fallback rule view when both extractors are absent."""
    fields: dict[str, list[str]] = {
        "assignee": [], "action": [], "asset": [], "constraint": [], "purpose": []
    }
    rule_types: list[str] = []
    for entity in entities:
        label = entity["label"]
        value = source_text[entity["start"]:entity["end"]]
        if label.startswith("RULE_TYPE-"):
            candidate = _normalize_rule_type(label[len("RULE_TYPE-"):])
            if candidate and candidate not in rule_types:
                rule_types.append(candidate)
        else:
            field = label.lower()
            if field in fields:
                fields[field].append(value)
    if not entities:
        return []
    return [{
        "source_text": source_text,
        "assignee": " ".join(fields["assignee"]),
        "action": " ".join(fields["action"]),
        "asset": " ".join(fields["asset"]),
        "attributed_party": "",
        "rule_type": rule_types[0] if len(rule_types) == 1 else "",
        "constraint": " ".join(fields["constraint"]),
        "purpose": " ".join(fields["purpose"]),
        "selected_from": "original_ner_fallback",
    }]


def compare_entity_sets(
    original_entities: list[dict[str, Any]],
    corrected_entities: list[dict[str, Any]],
) -> dict[str, Any]:
    """Return an auditable summary of what correction changed."""
    def key(entity: dict[str, Any]) -> tuple[int, int, str]:
        return (int(entity["start"]), int(entity["end"]), str(entity["label"]))

    original = {key(entity) for entity in original_entities}
    corrected = {key(entity) for entity in corrected_entities}
    to_dict = lambda item: {"start": item[0], "end": item[1], "label": item[2]}
    return {
        "original_entity_count": len(original),
        "corrected_entity_count": len(corrected),
        "unchanged_entity_count": len(original & corrected),
        "added_entities": [to_dict(item) for item in sorted(corrected - original)],
        "removed_entities": [to_dict(item) for item in sorted(original - corrected)],
    }


async def node_odrl_correct(state: ODRLCorrectionState) -> dict[str, Any]:
    """Use AI reconciliation, then convert the validated rules into NER spans."""
    source_text = str(state.get("source_text") or "")
    original_entities = list(state.get("original_entities") or [])
    endpoint_rules = normalize_endpoint_rules(state.get("endpoint_rules"), source_text)
    prompt = render_correction_prompt(
        str(state.get("prompt_template") or ""),
        source_text,
        original_entities,
        endpoint_rules,
    )

    warnings = list(state.get("correction_warnings") or [])
    override = state.get("ai_response_override")
    try:
        ai_result = (
            parse_ai_response(override)
            if override is not None
            else await _call_ai(prompt, str(state.get("model_name") or ""))
        )
        rules = normalize_rules(ai_result["validated_policy_rules"], source_text)
        selected_from = "ai_reconciliation"
        if not rules:
            raise ValueError("AI reconciliation returned no grounded policy rules.")
    except Exception as exc:
        warnings.append(f"AI reconciliation fallback: {type(exc).__name__}: {exc}")
        rules = endpoint_rules or _original_entities_to_rules(source_text, original_entities)
        selected_from = (
            "odrl_endpoint_fallback" if endpoint_rules else "original_ner_fallback"
        )

    for index, rule in enumerate(rules, start=1):
        rule["policy_rule_id"] = f"policy-rule-{index}"
        rule["selected_from"] = selected_from

    if selected_from == "original_ner_fallback":
        corrected_entities = list(original_entities)
        grounding_warnings: list[str] = []
    else:
        corrected_entities, grounding_warnings = rules_to_entities(
            source_text,
            rules,
            original_entities,
        )
    warnings.extend(grounding_warnings)

    # If neither AI nor endpoint produced a groundable entity, retain the
    # validated original record instead of emitting an empty training sample.
    if not corrected_entities and original_entities:
        corrected_entities = list(original_entities)
        selected_from = "original_ner_fallback"
        for rule in rules:
            rule["selected_from"] = selected_from
        warnings.append("No corrected components could be grounded; original entities retained.")

    return {
        "ai_prompt": prompt,
        "ai_rules": rules if selected_from == "ai_reconciliation" else [],
        "validated_policy_rules": rules,
        "selected_from": selected_from,
        "corrected_entities": corrected_entities,
        "correction_comparison": compare_entity_sets(
            original_entities,
            corrected_entities,
        ),
        "correction_warnings": warnings,
    }
