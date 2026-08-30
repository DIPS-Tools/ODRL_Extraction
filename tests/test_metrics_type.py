import unittest

from src.utils import (
    compute_token_metrics_by_tag,
    get_selected_fmeasure,
    get_token_fmeasure,
)


class TokenMetricTests(unittest.TestCase):
    def setUp(self):
        self.gold = [["<start>", "O", "B-ACTION", "I-ACTION", "O"]]
        self.pred = [["<start>", "O", "B-ACTION", "O", "B-ASSET"]]

    def test_token_accuracy_and_non_o_micro_f1(self):
        accuracy, precision, recall, f1 = get_token_fmeasure(
            self.gold,
            self.pred,
        )
        self.assertEqual(accuracy, 0.5)
        self.assertEqual(precision, 0.5)
        self.assertEqual(recall, 0.5)
        self.assertEqual(f1, 0.5)

    def test_selected_metric_dispatches_to_token_metric(self):
        selected = get_selected_fmeasure(
            self.gold,
            self.pred,
            metrics_type="token",
            label_type="BIO",
        )
        self.assertEqual(selected, (0.5, 0.5, 0.5, 0.5))

    def test_per_tag_table_excludes_sequence_markers(self):
        table = compute_token_metrics_by_tag(
            self.gold,
            self.pred,
            ["O", "B-ACTION", "I-ACTION", "B-ASSET"],
        )
        self.assertNotIn("<start>", set(table["tag"]))


if __name__ == "__main__":
    unittest.main()
