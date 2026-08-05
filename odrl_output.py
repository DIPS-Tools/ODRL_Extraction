"""Convert token-aligned ODRL labels into the public API response shape."""

import re
from typing import Dict, List, Sequence, Tuple


OUTPUT_FIELDS = ("assignee", "action", "asset", "rule_type", "constraint", "purpose")
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
