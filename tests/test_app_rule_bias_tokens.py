import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app_rule_bias import _clean_output_token, get_input


class FakeTokenizer:
    cls_token_id = 1
    sep_token_id = 2
    pad_token_id = 0
    bos_token_id = None
    eos_token_id = None
    unk_token = "<unk>"
    unk_token_id = 3

    def __init__(self):
        self.tokenized = []

    def tokenize(self, token):
        self.tokenized.append(token)
        return [token]

    def convert_tokens_to_ids(self, token):
        return {
            "▁The": 10,
            "▁audio": 11,
            "▁publicly.\r\n": 12,
        }.get(token, self.unk_token_id)


class OutputTokenTests(unittest.TestCase):
    def test_cleans_sentencepiece_and_byte_bpe_markers(self):
        self.assertEqual(_clean_output_token("▁audio"), "audio")
        self.assertEqual(_clean_output_token("Ġrecording"), "recording")
        self.assertEqual(_clean_output_token("▁publicly.\r\n"), "publicly.")
        self.assertEqual(_clean_output_token("may"), "may")

    @patch(
        "app_rule_bias._words_from_text",
        return_value=["▁The", "▁audio", "▁publicly.\r\n"],
    )
    def test_get_input_preserves_raw_tokens_for_encoder_but_returns_clean_tokens(self, words):
        tokenizer = FakeTokenizer()
        config = SimpleNamespace(tokenizer=tokenizer, max_length=8)

        input_ids, mask, output_words = get_input(config, "  ignored text\r\n")

        words.assert_called_once_with("ignored text", tokenizer)
        self.assertEqual(tokenizer.tokenized, ["▁The", "▁audio", "▁publicly.\r\n"])
        self.assertEqual(input_ids[0, :5].tolist(), [1, 10, 11, 12, 2])
        self.assertEqual(mask[0].tolist(), [1, 1, 1, 1, 1, 0, 0, 0])
        self.assertEqual(output_words, ["The", "audio", "publicly."])


if __name__ == "__main__":
    unittest.main()
