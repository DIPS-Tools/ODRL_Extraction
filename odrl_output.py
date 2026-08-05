"""Convert token-aligned ODRL labels into the public API response shape."""

import re
from typing import Dict, List, Sequence


OUTPUT_FIELDS = ("assignee", "action", "asset", "rule_type", "constraint", "purpose")
ENTITY_FIELDS = {
    "ASSIGNEE": "assignee",
    "ACTION": "action",
    "ASSET": "asset",
    "CONSTRAINT": "constraint",
    "PURPOSE": "purpose",
}


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
