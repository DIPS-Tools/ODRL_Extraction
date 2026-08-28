from __future__ import annotations

import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from odrl_correct_agent.odrl_correct_process.agent.batch_processing import (
    finalize_batch_job,
    prepare_batch_job,
    refresh_batch_status,
    watch_and_finalize_batch_job,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_correct import (
    normalize_endpoint_rules,
    render_correction_prompt,
    rules_to_entities,
)
from odrl_correct_agent.odrl_correct_process.agent.nodes.node_odrl_output import (
    build_diff_record,
)
from odrl_correct_agent.odrl_correct_process.agent.odrl_correct_main_graph import (
    DEMO_AI_RESPONSE,
    DEMO_INPUT,
    WORKFLOW_NODE_NAMES,
    build_workflow,
    correct_agent_app,
    correct_all_splits,
    correct_dataset,
    corrected_output_path,
    diff_output_path,
    odrl_output_path,
)
from odrl_correct_agent.utils.draw_mermaid_png import draw_mermaid_png


class _FakeFileContent:
    def __init__(self, content: bytes):
        self.content = content

    def write_to_file(self, path: str | Path) -> None:
        Path(path).write_bytes(self.content)


class _FakeFiles:
    def __init__(self, truncated: bool = False):
        self.requests: list[dict] = []
        self.truncated = truncated

    def create(self, *, file, purpose: str):
        self.requests = [
            json.loads(line)
            for line in file.read().decode("utf-8").splitlines()
            if line.strip()
        ]
        return SimpleNamespace(id="file-input", purpose=purpose)

    def retrieve(self, file_id: str):
        return SimpleNamespace(id=file_id, purpose="batch", status="processed")

    def content(self, file_id: str):
        if file_id == "file-errors":
            return _FakeFileContent(b"")
        results = []
        for request in reversed(self.requests):
            results.append({
                "custom_id": request["custom_id"],
                "response": {
                    "status_code": 200,
                    "body": {
                        "choices": [{
                            "message": {
                                "content": json.dumps(DEMO_AI_RESPONSE),
                            },
                            "finish_reason": "length" if self.truncated else "stop",
                        }],
                        "usage": {
                            "prompt_tokens": 100,
                            "completion_tokens": 50,
                            "completion_tokens_details": {"reasoning_tokens": 10},
                            "total_tokens": 150,
                        },
                    },
                },
                "error": None,
            })
        payload = "".join(json.dumps(item) + "\n" for item in results).encode()
        return _FakeFileContent(payload)


class _FakeBatches:
    def __init__(self, statuses: list[object] | None = None):
        self.statuses = list(statuses or ["completed"])
        self.last_status: object = "completed"

    def create(self, **kwargs):
        return SimpleNamespace(id="batch-test", status="validating", **kwargs)

    def retrieve(self, batch_id: str):
        if self.statuses:
            self.last_status = self.statuses.pop(0)
        if isinstance(self.last_status, Exception):
            raise self.last_status
        status = str(self.last_status)
        return SimpleNamespace(
            id=batch_id,
            status=status,
            output_file_id="file-output" if status == "completed" else None,
            error_file_id=None,
            request_counts=SimpleNamespace(total=3, completed=3, failed=0),
        )


class _FakeOpenAIClient:
    def __init__(
        self,
        truncated: bool = False,
        statuses: list[object] | None = None,
    ):
        self.files = _FakeFiles(truncated=truncated)
        self.batches = _FakeBatches(statuses=statuses)


class ODRLCorrectionWorkflowTests(unittest.IsolatedAsyncioTestCase):
    @staticmethod
    async def _no_wait(_: float) -> None:
        return None

    @staticmethod
    def _write_three_splits(root: Path) -> None:
        for filename in ("train.txt", "valid.txt", "test.txt"):
            (root / filename).write_text(
                json.dumps(DEMO_INPUT, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    async def test_openai_batch_lifecycle_preserves_quality_settings_and_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for filename in ("train.txt", "valid.txt", "test.txt"):
                (root / filename).write_text(
                    json.dumps(DEMO_INPUT, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
            fake_client = _FakeOpenAIClient()
            with patch.dict(
                os.environ,
                {
                    "ODRL_CORRECTION_REASONING_EFFORT": "medium",
                    "ODRL_CORRECTION_MAX_OUTPUT_TOKENS": "2000",
                },
            ):
                manifest_path = await prepare_batch_job(
                    [root / "train.txt", root / "valid.txt", root / "test.txt"],
                    output_dir=root,
                    model_name="gpt-5.6-luna",
                    call_endpoint=False,
                    submit=True,
                    client=fake_client,
                )

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["batch_id"], "batch-test")
            self.assertEqual(manifest["request_count"], 3)
            request_body = fake_client.files.requests[0]["body"]
            self.assertEqual(request_body["reasoning_effort"], "medium")
            self.assertEqual(request_body["max_completion_tokens"], 2000)

            status = refresh_batch_status(manifest_path, client=fake_client)
            self.assertEqual(status["status"], "completed")
            ner_paths, odrl_paths, states = await finalize_batch_job(
                manifest_path,
                client=fake_client,
            )
            self.assertEqual(len(states), 3)
            self.assertEqual(
                [path.name for path in ner_paths],
                [
                    "train_correct_with_agent_gpt-5.6-luna.txt",
                    "valid_correct_with_agent_gpt-5.6-luna.txt",
                    "test_correct_with_agent_gpt-5.6-luna.txt",
                ],
            )
            self.assertTrue(all(path.is_file() for path in ner_paths + odrl_paths))
            finalized = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(finalized["status"], "finalized")
            self.assertEqual(finalized["usage"]["total_tokens"], 450)
            self.assertEqual(finalized["fallback_count"], 0)
            self.assertEqual(
                [Path(path).name for path in finalized["diff_outputs"]],
                [
                    "train_diffs_from_correct_gpt-5.6-luna.txt",
                    "valid_diffs_from_correct_gpt-5.6-luna.txt",
                    "test_diffs_from_correct_gpt-5.6-luna.txt",
                ],
            )
            self.assertTrue(
                all(Path(path).is_file() for path in finalized["diff_outputs"])
            )
            self.assertEqual(
                [Path(path).name for path in finalized["odrl_diff_outputs"]],
                [
                    "train_odrl_diffs_from_correct_gpt-5.6-luna.txt",
                    "valid_odrl_diffs_from_correct_gpt-5.6-luna.txt",
                    "test_odrl_diffs_from_correct_gpt-5.6-luna.txt",
                ],
            )
            self.assertTrue(
                all(Path(path).is_file() for path in finalized["odrl_diff_outputs"])
            )

    async def test_batch_finalization_rejects_truncated_results_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "test.txt"
            source.write_text(json.dumps(DEMO_INPUT) + "\n", encoding="utf-8")
            fake_client = _FakeOpenAIClient(truncated=True)
            manifest_path = await prepare_batch_job(
                [source],
                output_dir=root,
                model_name="gpt-5.6-luna",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            with self.assertRaisesRegex(RuntimeError, "truncated"):
                await finalize_batch_job(manifest_path, client=fake_client)

    async def test_batch_watcher_polls_then_strictly_finalizes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_three_splits(root)
            fake_client = _FakeOpenAIClient(
                statuses=["validating", "in_progress", "finalizing", "completed"]
            )
            manifest_path = await prepare_batch_job(
                [root / "train.txt", root / "valid.txt", root / "test.txt"],
                output_dir=root,
                model_name="gpt-5.6-luna",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            finalized = await watch_and_finalize_batch_job(
                manifest_path,
                poll_interval_seconds=1,
                timeout_hours=1,
                client=fake_client,
                sleep=self._no_wait,
            )
            self.assertEqual(finalized["status"], "finalized")
            self.assertEqual(finalized["watch"]["outcome"], "finalized")
            self.assertEqual(finalized["watch"]["poll_count"], 4)
            self.assertTrue(
                all(
                    Path(path).is_file()
                    for key in ("ner_outputs", "odrl_outputs", "diff_outputs")
                    for path in finalized[key]
                )
            )

            # Resume is idempotent and does not call or submit another Batch.
            resumed = await watch_and_finalize_batch_job(
                manifest_path,
                client=fake_client,
                sleep=self._no_wait,
            )
            self.assertEqual(resumed["status"], "finalized")

    async def test_batch_watcher_retries_transient_status_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_three_splits(root)
            fake_client = _FakeOpenAIClient(
                statuses=[RuntimeError("temporary network failure"), "completed"]
            )
            manifest_path = await prepare_batch_job(
                [root / "train.txt", root / "valid.txt", root / "test.txt"],
                output_dir=root,
                model_name="test-model",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            delays: list[float] = []

            async def record_delay(delay: float) -> None:
                delays.append(delay)

            finalized = await watch_and_finalize_batch_job(
                manifest_path,
                poll_interval_seconds=2,
                max_consecutive_errors=2,
                client=fake_client,
                sleep=record_delay,
            )
            self.assertEqual(finalized["status"], "finalized")
            self.assertEqual(delays, [2])
            self.assertEqual(finalized["watch"]["consecutive_errors"], 0)

    async def test_batch_watcher_stops_on_expired_remote_job(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "test.txt"
            source.write_text(json.dumps(DEMO_INPUT) + "\n", encoding="utf-8")
            fake_client = _FakeOpenAIClient(statuses=["expired"])
            manifest_path = await prepare_batch_job(
                [source],
                output_dir=root,
                model_name="test-model",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            with self.assertRaisesRegex(RuntimeError, "terminal status 'expired'"):
                await watch_and_finalize_batch_job(
                    manifest_path,
                    poll_interval_seconds=1,
                    client=fake_client,
                    sleep=self._no_wait,
                )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["watch"]["outcome"], "remote_expired")
            self.assertNotIn("ner_outputs", manifest)

    async def test_batch_watcher_local_timeout_does_not_cancel_remote_job(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "test.txt"
            source.write_text(json.dumps(DEMO_INPUT) + "\n", encoding="utf-8")
            fake_client = _FakeOpenAIClient(statuses=["in_progress"])
            manifest_path = await prepare_batch_job(
                [source],
                output_dir=root,
                model_name="test-model",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            clock_values = iter([0.0, 0.0, 0.0, 3700.0])
            with self.assertRaisesRegex(TimeoutError, "was not cancelled"):
                await watch_and_finalize_batch_job(
                    manifest_path,
                    poll_interval_seconds=1,
                    timeout_hours=1,
                    client=fake_client,
                    sleep=self._no_wait,
                    monotonic=lambda: next(clock_values),
                )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["status"], "in_progress")
            self.assertEqual(manifest["watch"]["outcome"], "local_timeout")

    async def test_batch_finalization_rejects_changed_local_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "test.txt"
            source.write_text(json.dumps(DEMO_INPUT) + "\n", encoding="utf-8")
            fake_client = _FakeOpenAIClient()
            manifest_path = await prepare_batch_job(
                [source],
                output_dir=root,
                model_name="test-model",
                call_endpoint=False,
                submit=True,
                client=fake_client,
            )
            manifest = refresh_batch_status(manifest_path, client=fake_client)
            Path(manifest["prompt_snapshot_path"]).write_text(
                "changed after submission",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "artifact changed"):
                await finalize_batch_job(manifest_path, client=fake_client)

    async def test_workflow_diagram_is_rendered_without_langgraph(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            console = StringIO()
            with redirect_stdout(console):
                output_path = draw_mermaid_png(
                    correct_agent_app,
                    "odrl_correct_main_graph",
                    output_dir=directory,
                )

            self.assertTrue(output_path.is_file())
            self.assertTrue(output_path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertIn("flowchart TD", console.getvalue())
            self.assertIn("node_odrl_correct", console.getvalue())

    async def test_progress_logs_identify_record_and_each_node(self) -> None:
        with self.assertLogs("odrl_correct_agent", level="INFO") as captured:
            await build_workflow().ainvoke(
                DEMO_INPUT,
                record_index=2,
                record_total=7,
                model_name="test-model",
                call_endpoint=False,
                ai_response_override=DEMO_AI_RESPONSE,
            )

        messages = "\n".join(captured.output)
        for node_name in WORKFLOW_NODE_NAMES[1:-1]:
            self.assertIn(
                f"record=2/7 node={node_name} status=started",
                messages,
            )
            self.assertIn(
                f"record=2/7 node={node_name} status=completed",
                messages,
            )

    async def test_demo_produces_correct_ner_and_text_odrl(self) -> None:
        state = await build_workflow().ainvoke(
            DEMO_INPUT,
            model_name="test/model",
            call_endpoint=False,
            ai_response_override=DEMO_AI_RESPONSE,
        )
        self.assertEqual(
            WORKFLOW_NODE_NAMES,
            (
                "__start__",
                "node_initialize",
                "node_odrl_extraction",
                "node_odrl_correct",
                "node_odrl_output",
                "__end__",
            ),
        )
        self.assertEqual(
            state["corrected_record"]["entities"],
            [
                {"start": 4, "end": 19, "label": "ASSIGNEE"},
                {"start": 20, "end": 25, "label": "RULE_TYPE-OBLIGATION"},
                {"start": 26, "end": 33, "label": "ACTION"},
                {"start": 38, "end": 52, "label": "ASSET"},
                {"start": 53, "end": 133, "label": "CONSTRAINT"},
            ],
        )
        self.assertEqual(state["text_odrl_record"]["odrl"][0]["action"], "consult")
        self.assertEqual(
            state["text_odrl_record"]["odrl"][0]["asset"],
            "Data Processor",
        )

    async def test_original_entities_are_retained_when_ai_and_endpoint_fail(self) -> None:
        state = await build_workflow().ainvoke(
            DEMO_INPUT,
            model_name="test-model",
            call_endpoint=False,
            ai_response_override={"validated_policy_rules": []},
        )
        self.assertEqual(state["corrected_record"], DEMO_INPUT)
        self.assertEqual(state["selected_from"], "original_ner_fallback")

    async def test_batch_writes_both_jsonl_formats(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "test.txt"
            source.write_text(
                json.dumps(DEMO_INPUT, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            with self.assertLogs("odrl_correct_agent", level="INFO") as captured:
                ner_path, odrl_path, states = await correct_dataset(
                    source,
                    output_dir=root,
                    model_name="test/model",
                    call_endpoint=False,
                    ai_response_override=DEMO_AI_RESPONSE,
                    strict=True,
                )
            self.assertEqual(
                ner_path.name,
                "test_correct_with_agent_test_model.txt",
            )
            self.assertEqual(
                odrl_path.name,
                "test_odrl_with_agent_test_model.txt",
            )
            ner_record = json.loads(ner_path.read_text(encoding="utf-8"))
            odrl_record = json.loads(odrl_path.read_text(encoding="utf-8"))
            self.assertEqual(ner_record, states[0]["corrected_record"])
            self.assertEqual(odrl_record, states[0]["text_odrl_record"])
            diff_path = root / "test_diffs_from_correct_test_model.txt"
            diff_record = json.loads(diff_path.read_text(encoding="utf-8"))
            self.assertEqual(diff_record, states[0]["diff_record"])
            self.assertEqual(diff_record["origion_version"], DEMO_INPUT)
            self.assertEqual(
                diff_record["diffs"]["summary"],
                {
                    "original_entity_count": 3,
                    "correct_entity_count": 5,
                    "unchanged_count": 2,
                    "added_count": 2,
                    "deleted_count": 0,
                    "changed_count": 1,
                },
            )
            changed_asset = diff_record["diffs"]["changed"][0]
            self.assertEqual(changed_asset["change_types"], ["boundary_changed"])
            self.assertEqual(
                changed_asset["field_changes"],
                {
                    "start": {"from": 34, "to": 38},
                    "end": {"from": 42, "to": 52},
                },
            )
            self.assertEqual(
                diff_record["correction_evidence"]["selected_from"],
                "ai_reconciliation",
            )
            odrl_diff_path = root / "test_odrl_diffs_from_correct_test_model.txt"
            odrl_diff_record = json.loads(odrl_diff_path.read_text(encoding="utf-8"))
            self.assertEqual(odrl_diff_record, states[0]["odrl_diff_record"])
            self.assertEqual(odrl_diff_record["origion_version"]["text"], DEMO_INPUT["text"])
            messages = "\n".join(captured.output)
            self.assertIn("dataset=test.txt record=1/1 status=started", messages)
            self.assertIn("dataset=test.txt record=1/1 status=completed", messages)
            self.assertIn("selected_from=ai_reconciliation", messages)

    async def test_all_splits_writes_split_specific_ner_and_odrl_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for filename in ("train.txt", "valid.txt", "test.txt"):
                (root / filename).write_text(
                    json.dumps(DEMO_INPUT, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
            ner_paths, odrl_paths, states = await correct_all_splits(
                root,
                output_dir=root,
                model_name="test-model",
                call_endpoint=False,
                ai_response_override=DEMO_AI_RESPONSE,
                strict=True,
            )
            self.assertEqual(len(ner_paths), 3)
            self.assertEqual(len(odrl_paths), 3)
            self.assertEqual(len(states), 3)
            self.assertEqual(
                [path.name for path in odrl_paths],
                [
                    "train_odrl_with_agent_test-model.txt",
                    "valid_odrl_with_agent_test-model.txt",
                    "test_odrl_with_agent_test-model.txt",
                ],
            )
            self.assertTrue(all(len(path.read_text(encoding="utf-8").splitlines()) == 1 for path in odrl_paths))
            self.assertEqual(
                sorted({Path(state["diff_output_path"]).name for state in states}),
                [
                    "test_diffs_from_correct_test-model.txt",
                    "train_diffs_from_correct_test-model.txt",
                    "valid_diffs_from_correct_test-model.txt",
                ],
            )
            self.assertEqual(
                sorted({Path(state["odrl_diff_output_path"]).name for state in states}),
                [
                    "test_odrl_diffs_from_correct_test-model.txt",
                    "train_odrl_diffs_from_correct_test-model.txt",
                    "valid_odrl_diffs_from_correct_test-model.txt",
                ],
            )


class GroundingTests(unittest.TestCase):
    def test_prompt_evidence_is_compact_and_does_not_repeat_full_source(self) -> None:
        template = Path(
            "odrl_correct_agent/prompt/odrl_extraction.prompt"
        ).read_text(encoding="utf-8")
        rendered = render_correction_prompt(
            template,
            DEMO_INPUT["text"],
            DEMO_INPUT["entities"],
            [{
                "source_text": DEMO_INPUT["text"],
                "assignee": "Data Controller",
                "action": "consult",
                "asset": "Data Processor",
                "rule_type": "obligation",
            }],
        )
        self.assertEqual(rendered.count(DEMO_INPUT["text"]), 1)
        self.assertIn('\"s\":4,\"e\":19,\"l\":\"ASSIGNEE\"', rendered)
        self.assertNotIn("{{SOURCE_TEXT}}", rendered)

    def test_rule_components_are_exact_source_offsets(self) -> None:
        text = DEMO_INPUT["text"]
        rules = [dict(DEMO_AI_RESPONSE["validated_policy_rules"][0])]
        entities, warnings = rules_to_entities(text, rules, DEMO_INPUT["entities"])
        self.assertFalse(warnings)
        for entity in entities:
            self.assertTrue(text[entity["start"]:entity["end"]])

    def test_non_source_component_is_not_annotated(self) -> None:
        rules = [{
            **DEMO_AI_RESPONSE["validated_policy_rules"][0],
            "asset": "invented resource",
        }]
        entities, warnings = rules_to_entities(
            DEMO_INPUT["text"], rules, DEMO_INPUT["entities"]
        )
        self.assertTrue(any("not an exact source quote" in warning for warning in warnings))
        self.assertFalse(any(entity["label"] == "ASSET" for entity in entities))

    def test_endpoint_modal_is_removed_from_action(self) -> None:
        rules = normalize_endpoint_rules(
            [{
                "source_text": "The document may be downloaded.",
                "action": "may be downloaded",
                "asset": "The document",
                "rule_type": "permission",
            }],
            "The document may be downloaded.",
        )
        self.assertEqual(rules[0]["action"], "be downloaded")

    def test_output_filename_uses_safe_model_name(self) -> None:
        path = corrected_output_path(
            Path("/tmp/test.txt"), Path("/tmp"), "provider/model:name"
        )
        self.assertEqual(path.name, "test_correct_with_agent_provider_model_name.txt")
        odrl_path = odrl_output_path(
            Path("/tmp/test.txt"), Path("/tmp"), "provider/model:name"
        )
        self.assertEqual(
            odrl_path.name,
            "test_odrl_with_agent_provider_model_name.txt",
        )
        diff_path = diff_output_path(
            Path("/tmp/test.txt"), Path("/tmp"), "provider/model:name"
        )
        self.assertEqual(
            diff_path.name,
            "test_diffs_from_correct_provider_model_name.txt",
        )

    def test_diff_report_separates_label_change_addition_and_deletion(self) -> None:
        text = "Alpha beta gamma delta"
        diff = build_diff_record({
            "record_index": 9,
            "source_text": text,
            "original_entities": [
                {"start": 0, "end": 5, "label": "ASSET"},
                {"start": 6, "end": 10, "label": "ACTION"},
            ],
            "corrected_entities": [
                {"start": 0, "end": 5, "label": "ASSIGNEE"},
                {"start": 11, "end": 16, "label": "PURPOSE"},
            ],
            "selected_from": "ai_reconciliation",
            "endpoint_rules": [{"asset": "Alpha"}],
            "validated_policy_rules": [{"assignee": "Alpha"}],
            "correction_warnings": [],
        })
        self.assertTrue(diff["diffs"]["has_changes"])
        self.assertEqual(diff["diffs"]["summary"]["changed_count"], 1)
        self.assertEqual(diff["diffs"]["summary"]["added_count"], 1)
        self.assertEqual(diff["diffs"]["summary"]["deleted_count"], 1)
        self.assertEqual(
            diff["diffs"]["changed"][0]["change_types"],
            ["label_changed"],
        )
        self.assertEqual(
            diff["diffs"]["added"][0]["correct_entity"]["text"],
            "gamma",
        )
        self.assertEqual(
            diff["diffs"]["deleted"][0]["original_entity"]["text"],
            "beta",
        )


if __name__ == "__main__":
    unittest.main()
