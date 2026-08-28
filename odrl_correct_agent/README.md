# ODRL dataset correction agent

This package corrects JSONL NER datasets by reconciling:

1. the original character-offset entities;
2. rules from the local `odrl-extraction` service; and
3. an independent AI review using `prompt/odrl_extraction.prompt`.

The focused workflow is:

```text
__start__
  -> node_initialize
  -> node_odrl_extraction
  -> node_odrl_correct
  -> node_odrl_output
  -> __end__
```

`node_odrl_serialization` is intentionally absent. Formal ODRL JSON-LD is not
needed to correct NER training spans.

## Configuration

Copy `.env.example` to either the project `.env` or
`odrl_correct_agent/.env`. `MODEL_NAME` controls both the AI request and the
corrected dataset filename. `OPENAI_MODEL_NAME` is accepted as a compatibility
fallback.

## Offline example

From the `odrl_extraction` project directory:

```bash
python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph
```

This uses a built-in AI response and prints both the corrected NER record and
the `text_odrl` record without making network calls.

## Token usage

The prompt keeps stable instructions before record-specific evidence, uses
compact JSON, omits empty endpoint fields, avoids repeating the complete source
inside model rules, and lets code generate rule IDs and provenance. An optional
completion cap can be configured when the selected provider supports it:

```text
ODRL_CORRECTION_MAX_OUTPUT_TOKENS=1200
```

Do not set this too low for records containing many atomic rules, or the JSON
response may be truncated.

## Correct a dataset

```bash
python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
  --dataset data/test.txt
```

Correct all three standard splits and create a model-specific ODRL file for
each split:

```bash
python -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
  --all-splits \
  --data-dir data
```

Useful options:

```text
--output-dir PATH    write outputs elsewhere
--model-name NAME    override MODEL_NAME
--endpoint URL       override ODRL_EXTRACTION_ENDPOINT
--skip-endpoint      reconcile original NER with AI only
--limit N            process the first N records
--strict             stop instead of retaining a record after an error
--log-level LEVEL    set DEBUG, INFO, WARNING, ERROR, or CRITICAL
```

## Progress logs

The command logs every dataset record and workflow node at `INFO` level. Each
record includes its split-local position, a short text preview, the selected
correction source, and rule/entity/warning counts. Node messages include their
elapsed processing time. Full prompts and credentials are never logged.

```text
2026-08-28 10:15:03 INFO odrl_correct_agent dataset=test.txt record=3/120 status=started text='The document may be...'
2026-08-28 10:15:03 INFO odrl_correct_agent record=3/120 node=node_initialize status=started
2026-08-28 10:15:03 INFO odrl_correct_agent record=3/120 node=node_initialize status=completed elapsed_ms=2.1
```

To keep the progress log while the process runs in the background:

```bash
nohup python -u -m odrl_correct_agent.query_process.agent.odrl_correct_main_graph \
  --dataset data/test.txt \
  --log-level INFO \
  > odrl_correction.log 2>&1 &
```

Follow it with `tail -f odrl_correction.log`. Set
`ODRL_CORRECTION_LOG_LEVEL=WARNING` or pass `--log-level WARNING` to show only
problems.

For `data/test.txt` and `MODEL_NAME=gpt-4o-mini`, outputs are:

```text
data/test_correct_with_agent_gpt-4o-mini.txt
data/test_odrl_with_agent_gpt-4o-mini.txt
```

The first file preserves the input training schema:

```json
{"text": "...", "entities": [{"start": 20, "end": 25, "label": "RULE_TYPE-OBLIGATION"}]}
```

The second is suitable for text-to-ODRL post-training:

```json
{"text": "...", "odrl": [{"policy_rule_id": "policy-rule-1", "assignee": "...", "action": "...", "asset": "...", "rule_type": "obligation", "constraint": "...", "purpose": "..."}]}
```

Outputs are written atomically. By default, a failed record is retained in the
NER output and reported as a warning rather than silently disappearing. Use
`--strict` for evaluation runs where any fallback should fail the job.

The `--all-splits` mode generates six files:

```text
train_correct_with_agent_{MODEL_NAME}.txt
valid_correct_with_agent_{MODEL_NAME}.txt
test_correct_with_agent_{MODEL_NAME}.txt
train_odrl_with_agent_{MODEL_NAME}.txt
valid_odrl_with_agent_{MODEL_NAME}.txt
test_odrl_with_agent_{MODEL_NAME}.txt
```
