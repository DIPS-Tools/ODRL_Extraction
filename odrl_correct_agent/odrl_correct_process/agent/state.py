"""State definitions for the focused ODRL dataset-correction workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Any, TypedDict


class ODRLCorrectionState(TypedDict, total=False):
    """Mutable state passed through one correction workflow invocation."""

    # Inputs and initialization.
    input_record: dict[str, Any]
    record_index: int
    record_total: int
    dataset_path: str
    output_dir: str
    prompt_path: str
    prompt_template: str
    model_name: str
    endpoint: str
    call_endpoint: bool
    ai_response_override: dict[str, Any] | None

    # Extraction and correction intermediates.
    source_text: str
    original_entities: list[dict[str, Any]]
    endpoint_rules: list[dict[str, str]]
    endpoint_error: str
    ai_prompt: str
    ai_rules: list[dict[str, str]]
    validated_policy_rules: list[dict[str, str]]
    selected_from: str
    correction_warnings: list[str]
    correction_comparison: dict[str, Any]

    # Final records written by the batch runner.
    corrected_entities: list[dict[str, Any]]
    corrected_record: dict[str, Any]
    text_odrl_record: dict[str, Any]
    diff_record: dict[str, Any]
    original_odrl_record: dict[str, Any]
    corrected_odrl_record: dict[str, Any]
    odrl_diff_record: dict[str, Any]
    diff_output_path: str
    odrl_diff_output_path: str


def default_prompt_path() -> Path:
    """Return the prompt bundled with this package."""
    return Path(__file__).resolve().parents[2] / "prompt" / "odrl_extraction.prompt"


def create_correction_state(
    input_record: dict[str, Any],
    **overrides: Any,
) -> ODRLCorrectionState:
    """Create fresh state for one JSONL record."""
    state: ODRLCorrectionState = {
        "input_record": dict(input_record),
        "record_index": 0,
        "record_total": 0,
        "dataset_path": "",
        "output_dir": "",
        "prompt_path": str(default_prompt_path()),
        "prompt_template": "",
        "model_name": "",
        "endpoint": "",
        "call_endpoint": True,
        "ai_response_override": None,
        "source_text": "",
        "original_entities": [],
        "endpoint_rules": [],
        "endpoint_error": "",
        "ai_prompt": "",
        "ai_rules": [],
        "validated_policy_rules": [],
        "selected_from": "",
        "correction_warnings": [],
        "correction_comparison": {},
        "corrected_entities": [],
        "corrected_record": {},
        "text_odrl_record": {},
        "diff_record": {},
        "original_odrl_record": {},
        "corrected_odrl_record": {},
        "odrl_diff_record": {},
        "diff_output_path": "",
        "odrl_diff_output_path": "",
    }
    state.update(overrides)
    return state
