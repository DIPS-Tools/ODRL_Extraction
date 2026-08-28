"""Initialize one ODRL dataset-correction record."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from odrl_correct_agent.odrl_correct_process.agent.state import ODRLCorrectionState


def _load_environment() -> None:
    """Load project and agent environment files without overriding the shell."""
    project_root = Path(__file__).resolve().parents[4]
    load_dotenv(project_root / ".env", override=False)
    load_dotenv(project_root / "odrl_correct_agent" / ".env", override=False)


def _validate_original_entities(
    text: str,
    raw_entities: Any,
) -> list[dict[str, Any]]:
    if not isinstance(raw_entities, list):
        raise ValueError("The input record's 'entities' field must be a list.")

    entities: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_entities):
        if not isinstance(raw, dict):
            raise ValueError(f"Entity {index} must be a JSON object.")
        try:
            start = int(raw["start"])
            end = int(raw["end"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Entity {index} has invalid start/end offsets.") from exc
        label = str(raw.get("label") or "").strip().upper()
        if not 0 <= start < end <= len(text):
            raise ValueError(
                f"Entity {index} offsets [{start}, {end}) are outside the text."
            )
        if not label:
            raise ValueError(f"Entity {index} has an empty label.")
        entities.append({"start": start, "end": end, "label": label})
    return entities


async def node_initialize(state: ODRLCorrectionState) -> dict[str, Any]:
    """Validate input, load the correction prompt, and resolve configuration."""
    _load_environment()
    record = state.get("input_record") or {}
    text = str(record.get("text") or "")
    if not text.strip():
        raise ValueError("Each dataset record requires non-empty 'text'.")

    prompt_path = Path(str(state.get("prompt_path") or "")).expanduser().resolve()
    if not prompt_path.is_file():
        raise FileNotFoundError(f"ODRL correction prompt not found: {prompt_path}")

    model_name = str(
        state.get("model_name")
        or os.getenv("MODEL_NAME")
        or os.getenv("OPENAI_MODEL_NAME")
        or "gpt-4o-mini"
    ).strip()
    if not model_name:
        raise ValueError("MODEL_NAME must not be empty.")

    return {
        "source_text": text,
        "original_entities": _validate_original_entities(
            text,
            record.get("entities", []),
        ),
        "prompt_path": str(prompt_path),
        "prompt_template": prompt_path.read_text(encoding="utf-8"),
        "model_name": model_name,
        "correction_warnings": [],
    }
