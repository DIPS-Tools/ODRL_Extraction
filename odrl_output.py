"""Convert token-aligned ODRL labels into the public API response shape."""

import re
from typing import Any, Dict, List, Sequence, Tuple


OUTPUT_FIELDS = ("assignee", "action", "asset", "rule_type", "constraint", "purpose")
ODRL_FIELDS = (
    "source_text",
    "assignee",
    "action",
    "asset",
    "rule_type",
    "constraint",
    "purpose",
)
ENTITY_FIELDS = {
    "ASSIGNEE": "assignee",
    "ACTION": "action",
    "ASSET": "asset",
    "CONSTRAINT": "constraint",
    "PURPOSE": "purpose",
}
CLAUSE_CONNECTORS = {"and", "but", "except", "however", "or", "whereas", "while", ";"}


def split_sentences(text: str) -> List[str]:
    """Split prose on sentence punctuation or line boundaries.

    Terminal quotes and brackets stay attached to the preceding sentence.
    Decimal points do not create a boundary because a boundary must be
    followed by whitespace or the end of the input.
    """
    sentence_pattern = re.compile(
        r'.+?(?:[.!?]+(?:["\u201d\u2019)\]]*)?(?=\s+|$)|\n+|$)',
        flags=re.DOTALL,
    )
    return [match.group(0).strip() for match in sentence_pattern.finditer(text) if match.group(0).strip()]


def _entity_type(label: str) -> str:
    """Remove a BIO/BIOES prefix while preserving the ODRL entity name."""
    if label == "O":
        return ""

    prefix, separator, entity_type = label.partition("-")
    if separator and prefix in {"B", "I", "E", "S"}:
        return entity_type
    return label


def _join_tokens(tokens: Sequence[str]) -> str:
    """Join word-level tokens without spaces before common punctuation."""
    text = ""
    no_space_before = set(".,;:!?%)]}")
    no_space_after = set("([{")

    for token in tokens:
        if not text:
            text = token
        elif token in no_space_before or token.startswith(("'", "’")):
            text += token
        elif text[-1] in no_space_after:
            text += token
        else:
            text += " " + token

    return text


def format_odrl_output(tokens: Sequence[str], labels: Sequence[str]) -> Dict[str, str]:
    """Aggregate token labels into the flat response used by API consumers.

    Rule-type tokens (for example ``may``) are included in ``action`` while
    the label suffix supplies the canonical rule type (for example
    ``permission``).
    """
    values: Dict[str, List[str]] = {field: [] for field in OUTPUT_FIELDS}
    rule_types: List[str] = []

    for token, label in zip(tokens, labels):
        entity_type = _entity_type(label)

        if entity_type.startswith("RULE_TYPE-"):
            values["action"].append(token)
            rule_type = entity_type[len("RULE_TYPE-"):].lower()
            if rule_type and rule_type not in rule_types:
                rule_types.append(rule_type)
            continue

        field = ENTITY_FIELDS.get(entity_type)
        if field is not None:
            values[field].append(token)

    output = {field: _join_tokens(values[field]) for field in OUTPUT_FIELDS}
    output["rule_type"] = ", ".join(rule_types)
    return output


def _rule_type_spans(labels: Sequence[str]) -> List[Tuple[int, int, str]]:
    """Return contiguous ``(start, end, type)`` rule-type anchors."""
    spans: List[Tuple[int, int, str]] = []
    for index, label in enumerate(labels):
        entity_type = _entity_type(label)
        if not entity_type.startswith("RULE_TYPE-"):
            continue

        rule_type = entity_type[len("RULE_TYPE-"):].lower()
        if spans and spans[-1][1] == index and spans[-1][2] == rule_type:
            start, _, existing_type = spans[-1]
            spans[-1] = (start, index + 1, existing_type)
        else:
            spans.append((index, index + 1, rule_type))
    return spans


def _normalize_compound_prohibitions(
    tokens: Sequence[str],
    labels: Sequence[str],
) -> List[str]:
    """Keep modal + ``not`` together when their predicted types conflict."""
    normalized = list(labels)
    low = [token.lower() for token in tokens]

    for index in range(min(len(low), len(normalized)) - 1):
        modal_type = _entity_type(normalized[index])
        next_type = _entity_type(normalized[index + 1])
        if (
            low[index] in {"may", "can", "shall", "must"}
            and low[index + 1] == "not"
            and modal_type in {"RULE_TYPE-PERMISSION", "RULE_TYPE-OBLIGATION"}
            and next_type == "RULE_TYPE-PROHIBITION"
        ):
            normalized[index] = "B-RULE_TYPE-PROHIBITION"
            normalized[index + 1] = "I-RULE_TYPE-PROHIBITION"

    return normalized


def _clause_ranges(
    tokens: Sequence[str],
    anchors: Sequence[Tuple[int, int, str]],
) -> List[Tuple[int, int]]:
    """Split at the conjunction or punctuation between rule-type anchors."""
    starts = [0]
    ends: List[int] = []
    low = [token.lower() for token in tokens]

    for previous, current in zip(anchors, anchors[1:]):
        connector = None
        for index in range(previous[1], current[0]):
            if low[index] in CLAUSE_CONNECTORS:
                connector = index

        if connector is None:
            left_end = current[0]
            right_start = current[0]
        else:
            left_end = connector
            while left_end > starts[-1] and tokens[left_end - 1] in {",", ";"}:
                left_end -= 1
            right_start = connector + 1
            while right_start < current[0] and tokens[right_start] in {",", ";"}:
                right_start += 1

        ends.append(left_end)
        starts.append(right_start)

    ends.append(len(tokens))
    return list(zip(starts, ends))


def format_odrl_rules(
    source_text: str,
    tokens: Sequence[str],
    labels: Sequence[str],
) -> List[Dict[str, str]]:
    """Create one atomic ODRL rule for every rule-type anchor.

    A sentence with one or no rule-type anchor remains one rule. When several
    anchors occur, each clause gets its own rule and a shared asset or assignee
    from the first clause is inherited by later clauses that omit it.
    """
    token_count = min(len(tokens), len(labels))
    aligned_tokens = list(tokens[:token_count])
    aligned_labels = _normalize_compound_prohibitions(
        aligned_tokens,
        labels[:token_count],
    )
    anchors = _rule_type_spans(aligned_labels)

    if len(anchors) <= 1:
        return [{
            "source_text": source_text.strip(),
            **format_odrl_output(aligned_tokens, aligned_labels),
        }]

    rules: List[Dict[str, str]] = []
    for start, end in _clause_ranges(aligned_tokens, anchors):
        clause_tokens = aligned_tokens[start:end]
        clause_labels = aligned_labels[start:end]
        rules.append({
            "source_text": _join_tokens(clause_tokens),
            **format_odrl_output(clause_tokens, clause_labels),
        })

    # Coordinated clauses commonly omit the repeated subject and asset.
    shared_assignee = rules[0]["assignee"]
    shared_asset = rules[0]["asset"]
    for rule in rules[1:]:
        if not rule["assignee"]:
            rule["assignee"] = shared_assignee
        if not rule["asset"]:
            rule["asset"] = shared_asset

    return rules


def _compact(value: Any) -> str:
    return " ".join(str(value or "").split())


def _word_pretok_with_offsets(text: str) -> tuple[list[str], list[tuple[int, int]]]:
    """Split text into word-like tokens while tracking character offsets."""
    words: list[str] = []
    spans: list[tuple[int, int]] = []
    start = None

    for index, char in enumerate(text):
        if char.isspace():
            if start is not None:
                words.append(text[start:index])
                spans.append((start, index))
                start = None
            continue
        if start is None:
            start = index

    if start is not None:
        words.append(text[start:len(text)])
        spans.append((start, len(text)))

    if not words and text:
        words = [text]
        spans = [(0, len(text))]

    return words, spans


def _build_char_mask(text: str, entities: list[dict[str, Any]]) -> list[str]:
    """Build a character-level label mask with deterministic overlap handling."""
    char_mask = ["O"] * len(text)
    priority = {
        "RULE_TYPE-PERMISSION": 0,
        "RULE_TYPE-OBLIGATION": 1,
        "RULE_TYPE-PROHIBITION": 2,
        "ASSIGNEE": 3,
        "ACTION": 4,
        "ASSET": 5,
        "CONSTRAINT": 6,
        "PURPOSE": 7,
    }
    ordered_entities = sorted(
        entities,
        key=lambda entity: priority.get(str(entity["label"]), 999),
    )
    for entity in ordered_entities:
        start = max(0, min(int(entity["start"]), len(text)))
        end = max(0, min(int(entity["end"]), len(text)))
        label = str(entity["label"])
        for index in range(start, end):
            char_mask[index] = label
    return char_mask


def _spans_to_bio_over_words(
    text: str,
    entities: list[dict[str, Any]],
) -> tuple[list[str], list[str]]:
    """Convert span entities to BIO tags over the tokenization used here."""
    words, word_spans = _word_pretok_with_offsets(text)
    char_mask = _build_char_mask(text, entities)

    labels: list[str] = []
    previous_label = "O"
    for start, end in word_spans:
        label = "O"
        for index in range(start, end):
            if 0 <= index < len(char_mask) and char_mask[index] != "O":
                label = char_mask[index]
                break
        if label == "O":
            labels.append("O")
            previous_label = "O"
            continue

        prefix = "B-" if previous_label != label else "I-"
        labels.append(prefix + label)
        previous_label = label

    return words, labels


def build_odrl_record_from_entities(
    text: str,
    entities: list[dict[str, Any]],
) -> dict[str, Any]:
    """Convert a span-annotated record into the JSONL ODRL dataset shape."""
    words, labels = _spans_to_bio_over_words(text, entities)
    rules = format_odrl_rules(text, words, labels)

    odrl_rules: list[dict[str, str]] = []
    for index, rule in enumerate(rules, 1):
        odrl_rule = {field: "" for field in ("policy_rule_id", *ODRL_FIELDS)}
        odrl_rule["policy_rule_id"] = f"policy-rule-{index}"
        for field in ODRL_FIELDS:
            odrl_rule[field] = _compact(rule.get(field))
        odrl_rules.append(odrl_rule)

    return {"text": text, "odrl": odrl_rules}


def _rule_signature(rule: dict[str, Any]) -> tuple[str, ...]:
    return tuple(_compact(rule.get(field)) for field in ODRL_FIELDS)


def _rule_view(rule: dict[str, Any]) -> dict[str, Any]:
    return {
        field: _compact(rule.get(field))
        for field in ("policy_rule_id", *ODRL_FIELDS)
    }


def build_odrl_diff_record(state: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic comparison for original vs corrected ODRL JSONL."""
    original_record = dict(state.get("original_odrl_record") or {})
    corrected_record = dict(
        state.get("corrected_odrl_record") or state.get("text_odrl_record") or {}
    )
    text = _compact(
        original_record.get("text")
        or corrected_record.get("text")
        or state.get("source_text")
    )
    original_rules = [
        dict(rule)
        for rule in original_record.get("odrl") or []
        if isinstance(rule, dict)
    ]
    corrected_rules = [
        dict(rule)
        for rule in corrected_record.get("odrl") or []
        if isinstance(rule, dict)
    ]

    unchanged: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []
    added: list[dict[str, Any]] = []
    deleted: list[dict[str, Any]] = []

    shared_count = min(len(original_rules), len(corrected_rules))
    for index in range(shared_count):
        original = original_rules[index]
        corrected = corrected_rules[index]
        if _rule_signature(original) == _rule_signature(corrected):
            unchanged.append({
                "index": index,
                "original_rule": _rule_view(original),
                "correct_rule": _rule_view(corrected),
            })
            continue
        field_changes = {
            field: {
                "from": _compact(original.get(field)),
                "to": _compact(corrected.get(field)),
            }
            for field in ODRL_FIELDS
            if _compact(original.get(field)) != _compact(corrected.get(field))
        }
        changed.append({
            "index": index,
            "change_types": sorted(field_changes),
            "original_rule": _rule_view(original),
            "correct_rule": _rule_view(corrected),
            "field_changes": field_changes,
        })

    for index in range(shared_count, len(original_rules)):
        deleted.append({
            "index": index,
            "original_rule": _rule_view(original_rules[index]),
        })

    for index in range(shared_count, len(corrected_rules)):
        added.append({
            "index": index,
            "correct_rule": _rule_view(corrected_rules[index]),
        })

    return {
        "record_index": int(state.get("record_index") or 0),
        "origion_version": {
            "text": text,
            "odrl": original_rules,
        },
        "correct_version": {
            "text": text,
            "odrl": corrected_rules,
        },
        "diffs": {
            "has_changes": bool(added or deleted or changed),
            "summary": {
                "original_rule_count": len(original_rules),
                "correct_rule_count": len(corrected_rules),
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
    }
