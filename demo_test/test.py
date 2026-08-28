import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env", override=False)
api_key = str(os.getenv("OPENAI_API_KEY") or "").strip()
if not api_key:
  raise RuntimeError(
    f"OPENAI_API_KEY is missing. Set it in {project_root / '.env'} "
    "or export it before running this test."
  )

manifest_path = (
  project_root / "data" / "batch_jobs"
  / "odrl_gpt-5.6-luna_20260828T142956Z_da44329a"
  / "manifest.json"
)
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
client = OpenAI(api_key=api_key)
file_id = manifest["input_file_id"]

try:
  result = client.files.retrieve(file_id)
  print("File accessible:", result.id, result.status)
except Exception as exc:
  print("File access failed:", exc)
