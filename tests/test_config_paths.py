import unittest

from model.config import resolve_dataset_path, safe_checkpoint_tag


class DatasetCheckpointConfigTests(unittest.TestCase):
    def test_bare_dataset_filename_is_resolved_under_data_path(self):
        self.assertEqual(
            resolve_dataset_path("./data/", "train_correct.txt", "train.txt"),
            "./data/train_correct.txt",
        )

    def test_explicit_dataset_path_is_preserved(self):
        self.assertEqual(
            resolve_dataset_path("./data/", "other/train.txt", "train.txt"),
            "other/train.txt",
        )

    def test_checkpoint_tag_is_readable_and_path_safe(self):
        self.assertEqual(
            safe_checkpoint_tag("correct data/with agent:gpt-5.6-luna"),
            "correct_data_with_agent_gpt-5.6-luna",
        )


if __name__ == "__main__":
    unittest.main()
