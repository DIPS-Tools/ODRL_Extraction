import unittest
from types import SimpleNamespace
from unittest.mock import patch

import torch
from torch import nn

from model.hf_crf import HF_CRF


class FakeEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.config = SimpleNamespace(hidden_size=8, is_encoder_decoder=False)
        self.embedding = nn.Embedding(32, 8)

    def forward(self, input_ids, attention_mask=None, return_dict=True):
        return SimpleNamespace(last_hidden_state=self.embedding(input_ids))


class GenericTransformerCrfTests(unittest.TestCase):
    @patch("model.hf_crf.AutoConfig.from_pretrained")
    @patch("model.hf_crf.AutoModel.from_pretrained")
    def test_emissions_and_decode_without_lstm(self, model_from_pretrained, config_from_pretrained):
        config_from_pretrained.return_value = SimpleNamespace(model_type="bert")
        model_from_pretrained.return_value = FakeEncoder()
        model = HF_CRF(
            "fake-encoder",
            tagset_size=17,
            dropout_rate=0.1,
            use_cuda=False,
        )
        input_ids = torch.tensor([[1, 2, 3, 0], [4, 5, 0, 0]])
        mask = input_ids.ne(0).long()

        emissions = model.compute_emissions(input_ids, mask)
        decoded = model(input_ids, mask)

        self.assertEqual(tuple(emissions.shape), (2, 4, 19))
        self.assertEqual(len(decoded), 2)


if __name__ == "__main__":
    unittest.main()
