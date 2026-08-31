import unittest

from src.utils import _encode_sample


class FakeTokenizer:
    unk_token = "[UNK]"
    unk_token_id = 7

    def tokenize(self, word):
        return [word.lower()]

    def convert_tokens_to_ids(self, token):
        return {"alpha": 11, "beta": 12}.get(token, self.unk_token_id)


class TokenPaddingTests(unittest.TestCase):
    def test_token_and_label_padding_use_separate_ids(self):
        labels = {
            "O": 0,
            "B-ACTION": 1,
            "<pad>": 17,
            "<start>": 18,
            "<eos>": 19,
        }
        feature = _encode_sample(
            ["Alpha", "Beta"],
            ["O", "B-ACTION"],
            FakeTokenizer(),
            labels,
            max_length=8,
            cls_id=101,
            sep_id=102,
            token_pad_id=50283,
            label_pad_id=17,
        )

        self.assertEqual(
            feature.input_id,
            [101, 11, 12, 102, 50283, 50283, 50283, 50283],
        )
        self.assertEqual(feature.label_id, [18, 0, 1, 19, 17, 17, 17, 17])
        self.assertEqual(feature.input_mask, [1, 1, 1, 1, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
