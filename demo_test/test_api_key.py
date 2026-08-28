"""Minimal OpenAI authentication check.

Run from the repository root with:
    .venv/bin/python demo_test/test_api_key.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env", override=False)
api_key = str(os.getenv("OPENAI_API_KEY") or "").strip()
if not api_key:
    raise SystemExit(
        f"OPENAI_API_KEY is missing. Set it in {project_root / '.env'} "
        "or export it before running this script."
    )

try:
    client = OpenAI(api_key=api_key)
    models = client.models.list()
    model_count = len(getattr(models, "data", []) or [])
    print(f"OpenAI authentication succeeded; {model_count} model(s) visible.")
except Exception as exc:
    raise SystemExit(f"OpenAI authentication/API check failed: {exc}") from exc
