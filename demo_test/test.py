import json
import os
import sys
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

default_manifest = (
  project_root / "data" / "batch_jobs"
  / "odrl_gpt-5.6-luna_20260828T155820Z_3d8be82a"
  / "manifest.json"
)
manifest_path = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else default_manifest
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
client = OpenAI(
  api_key=api_key,
  organization=str(os.getenv("OPENAI_ORG_ID") or "").strip() or None,
  project=str(os.getenv("OPENAI_PROJECT_ID") or "").strip() or None,
)
file_id = manifest["input_file_id"]

try:
  raw_file = client.files.with_raw_response.retrieve(file_id)
  result = raw_file.parse()
  print("File accessible:", result.id, result.status)
  print("File response scope:", {
    name: raw_file.headers.get(name)
    for name in ("openai-organization", "openai-project", "x-request-id")
  })
  batch_id = str(manifest.get("batch_id") or "")
  if batch_id:
    raw_batch = client.batches.with_raw_response.retrieve(batch_id)
    batch = raw_batch.parse()
    print("Batch accessible:", batch.id, batch.status)
    print("Batch response scope:", {
      name: raw_batch.headers.get(name)
      for name in ("openai-organization", "openai-project", "x-request-id")
    })
except Exception as exc:
  print("File access failed:", exc)
