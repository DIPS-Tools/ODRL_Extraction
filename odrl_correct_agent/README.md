# ODRL dataset correction agent

This package corrects JSONL NER datasets by reconciling the original entities,
rules from the trained local `odrl-extraction` service, and an independent AI
review using `prompt/odrl_extraction.prompt`.

```text
__start__
  -> node_initialize
  -> node_odrl_extraction
  -> node_odrl_correct
  -> node_odrl_output
  -> __end__
```

## Configuration

Use the project `.env` or copy `.env.example` to
`odrl_correct_agent/.env`. Important settings are:

```env
MODEL_NAME=gpt-5.6-luna
ODRL_EXTRACTION_ENDPOINT=http://127.0.0.1:5001/odrl_generation
ODRL_CORRECTION_REASONING_EFFORT=medium
ODRL_CORRECTION_MAX_OUTPUT_TOKENS=2000
ODRL_BATCH_POLL_SECONDS=300
ODRL_BATCH_WATCH_TIMEOUT_HOURS=26
ODRL_BATCH_MAX_CONSECUTIVE_ERRORS=12
```

`MODEL_NAME` controls the AI request and output filename. The trained endpoint
result is evidence supplied to the AI; source text remains authoritative.

## Offline example

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph
```

This uses a built-in response and makes no network calls.

## Synchronous correction

Correct one split:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --dataset data/test.txt
```

Correct exactly `train.txt`, `valid.txt`, and `test.txt`:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --all-splits \
  --data-dir data
```

The three output types are:

```text
{split}_correct_with_agent_{MODEL_NAME}.txt
{split}_odrl_with_agent_{MODEL_NAME}.txt
{split}_diffs_from_correct_{MODEL_NAME}.txt
```

Outputs are written atomically. Diff files contain only records whose NER
annotations changed.

## Recommended discounted Batch run

First verify the trained endpoint:

```bash
curl -sS -X POST \
  http://127.0.0.1:5001/odrl_generation \
  -H 'Content-Type: application/json' \
  -d '{"text":"The document may be downloaded for research purposes."}'
```

Run the entire lifecycle in the background:

```bash
nohup .venv/bin/python -u \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-run \
  --all-splits \
  --data-dir data \
  --log-level INFO \
  > odrl_batch_run.log 2>&1 &

echo $! > odrl_batch_run.pid
```

`--batch-run` performs local endpoint extraction, prepares and uploads the
JSONL request file, submits one paid discounted Batch, polls every five minutes,
and strictly finalizes all nine output files after remote completion.

```bash
tail -f odrl_batch_run.log
```

The process saves the manifest path to the log immediately after submission.
If SSH disconnects, `nohup` keeps it running. If the machine reboots or the
process is killed, the remote Batch continues and can be resumed without a new
submission:

```bash
MANIFEST="data/batch_jobs/odrl_gpt-5.6-luna_.../manifest.json"

nohup .venv/bin/python -u \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-watch-finalize "$MANIFEST" \
  --log-level INFO \
  > odrl_batch_resume.log 2>&1 &
```

Only one watcher may own a manifest at a time. The local watcher stops after 26
hours by default but never cancels the remote job. Run the resume command again
if that happens.

## Manual Batch lifecycle

Prepare and submit, then exit:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-prepare \
  --all-splits \
  --data-dir data
```

Prepare without an OpenAI upload or charge:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-prepare-only \
  --all-splits \
  --data-dir data
```

Submit that prepared manifest:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-submit "$MANIFEST"
```

Check once or finalize manually:

```bash
.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-status "$MANIFEST"

.venv/bin/python \
  -m odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph \
  --batch-finalize "$MANIFEST"
```

## Batch safety and recovery

- The manifest checkpoints remote status, request counts, timestamps, watcher
  attempts, errors, output paths, and token usage.
- Requests, saved states, and the prompt snapshot are SHA-256 protected.
- Source split hashes and the optional endpoint model label are recorded for
  provenance.
- Input limits are checked before upload: at most 50,000 requests and a 200 MB
  JSONL request file.
- Output order is restored using unique `custom_id` values.
- Unknown, duplicate, and missing IDs are rejected.
- Transient polling errors use bounded exponential retry delays.
- `failed`, `expired`, and `cancelled` stop without writing corrected datasets.
- Missing, unsuccessful, empty, invalid, fallback, or truncated AI results stop
  strict finalization without partially replacing final datasets.
- A lock prevents two local watchers from finalizing the same manifest.
- Rerunning a finalized manifest verifies its recorded outputs and exits without
  resubmitting the paid job.

`--allow-batch-fallbacks` weakens the strict result requirement and is not
recommended when corrected training-data quality is the priority.

## Useful options

```text
--output-dir PATH
--model-name NAME
--endpoint URL
--skip-endpoint
--limit N
--strict
--log-level LEVEL
--batch-poll-seconds SECONDS
--batch-watch-timeout-hours HOURS
--batch-max-consecutive-errors N
```
