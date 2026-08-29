import unittest

from data.deduplicate_odrl_datasets import (
    Occurrence,
    choose_canonical_correction,
)


TEXT = "Alpha may use data."


def occurrence(split, index, entities):
    original = {"text": TEXT, "entities": []}
    corrected = {"text": TEXT, "entities": entities}
    odrl = {"text": TEXT, "odrl": []}
    return Occurrence(
        split=split,
        record_index=index,
        original=original,
        original_odrl=odrl,
        corrected=corrected,
        corrected_odrl=odrl,
        correction_evidence={},
    )


class CanonicalGoldSelectionTests(unittest.TestCase):
    def setUp(self):
        self.rank = {"test": 0, "valid": 1, "train": 2}
        self.asset = [{"start": 14, "end": 18, "label": "ASSET"}]
        self.action = [{"start": 10, "end": 13, "label": "ACTION"}]

    def test_consensus_selects_existing_majority_annotation(self):
        candidates = [
            occurrence("train", 1, self.asset),
            occurrence("valid", 2, self.asset),
            occurrence("test", 3, self.action),
        ]
        selected, audit = choose_canonical_correction(candidates, self.rank)
        self.assertEqual(selected.corrected["entities"], self.asset)
        self.assertEqual(audit["method"], "automatic_consensus_medoid")

    def test_manual_reviewed_choice_overrides_consensus(self):
        candidates = [
            occurrence("train", 1, self.asset),
            occurrence("test", 3, self.action),
        ]
        selected, audit = choose_canonical_correction(
            candidates,
            self.rank,
            {"split": "train", "record_index": 1, "reviewed": True},
        )
        self.assertEqual((selected.split, selected.record_index), ("train", 1))
        self.assertEqual(audit["method"], "manual_decision")

    def test_tie_prefers_non_overlapping_flat_ner_candidate(self):
        overlapping = [
            {"start": 0, "end": 18, "label": "CONSTRAINT"},
            {"start": 14, "end": 18, "label": "ASSET"},
        ]
        non_overlapping = [
            {"start": 14, "end": 18, "label": "ASSET"},
            {"start": 10, "end": 13, "label": "ACTION"},
        ]
        candidates = [
            occurrence("test", 1, overlapping),
            occurrence("train", 2, non_overlapping),
        ]
        selected, _ = choose_canonical_correction(candidates, self.rank)
        self.assertEqual(selected.corrected["entities"], non_overlapping)


if __name__ == "__main__":
    unittest.main()
