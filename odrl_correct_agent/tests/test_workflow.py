from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from odrl_correct_agent.query_process.agent.nodes.node_odrl_correct import (
    normalize_endpoint_rules,
    render_correction_prompt,
    rules_to_entities,
)
from odrl_correct_agent.query_process.agent.odrl_correct_main_graph import (
    DEMO_AI_RESPONSE,
    DEMO_INPUT,
    WORKFLOW_NODE_NAMES,
    build_workflow,
    correct_agent_app,
    correct_all_splits,
    correct_dataset,
    corrected_output_path,
    odrl_output_path,
)
from odrl_correct_agent.utils.draw_mermaid_png import draw_mermaid_png


class ODRLCorrectionWorkflowTests(unittest.IsolatedAsyncioTestCase):
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


if __name__ == "__main__":
    unittest.main()
