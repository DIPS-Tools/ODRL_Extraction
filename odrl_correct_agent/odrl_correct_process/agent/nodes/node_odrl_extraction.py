"""Call the trained ODRL extraction service for one dataset record."""

from __future__ import annotations

from typing import Any

from odrl_correct_agent.odrl_correct_process.agent.state import ODRLCorrectionState
from odrl_correct_agent.tools.odrl_extraction_tool import aextract_odrl_components


async def node_odrl_extraction(state: ODRLCorrectionState) -> dict[str, Any]:
    """Extract model rules while preserving errors for AI reconciliation."""
    if not state.get("call_endpoint", True):
        return {"endpoint_rules": [], "endpoint_error": "endpoint disabled"}

    text = str(state.get("source_text") or "")
    if not text:
        raise ValueError("node_odrl_extraction must run after node_initialize.")

    try:
        result = await aextract_odrl_components(
            text,
            endpoint=str(state.get("endpoint") or "") or None,
        )
        return {
            "endpoint_rules": list(result.get("rules") or []),
            "endpoint_error": "",
        }
    except Exception as exc:
        # The original labels plus AI can still correct a record when the
        # extraction service is unavailable, so retain this as evidence rather
        # than terminating the complete dataset run.
        return {
            "endpoint_rules": [],
            "endpoint_error": f"{type(exc).__name__}: {exc}",
        }
