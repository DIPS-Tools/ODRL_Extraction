import torch
import torch.nn as nn
from transformers import AutoConfig, AutoModel

from model.crf import CRF


class HF_CRF(nn.Module):
    """Generic pretrained Transformer encoder with a linear CRF head."""

    def __init__(
        self,
        encoder_name_or_path,
        tagset_size,
        dropout_rate,
        use_cuda,
        trust_remote_code=False,
    ):
        super().__init__()
        encoder_config = AutoConfig.from_pretrained(
            encoder_name_or_path,
            trust_remote_code=trust_remote_code,
        )
        is_modernbert = str(getattr(encoder_config, "model_type", "")).lower() == "modernbert"
        model_load_kwargs = {}
        if is_modernbert:
            # Some ModernBERT checkpoints enable compiled reference MLP layers in
            # their saved config. TorchInductor can return all-NaN hidden states
            # with particular PyTorch/Triton stacks, so use the ordinary layers.
            encoder_config.reference_compile = False
            # Flash Attention has a documented ModernBERT NaN-output failure in
            # some environments. SDPA is slower but is the stable HF backend.
            model_load_kwargs["attn_implementation"] = "sdpa"

        self.encoder = AutoModel.from_pretrained(
            encoder_name_or_path,
            config=encoder_config,
            trust_remote_code=trust_remote_code,
            **model_load_kwargs,
        )
        print(
            "[HF_CRF] "
            f"encoder_model_type={getattr(self.encoder.config, 'model_type', 'unknown')} "
            f"reference_compile={getattr(self.encoder.config, 'reference_compile', 'n/a')} "
            f"attention={getattr(self.encoder.config, '_attn_implementation', 'unknown')}"
        )
        self.backbone_param_prefixes = ("encoder.",)

        encoder_hidden = getattr(
            self.encoder.config,
            "hidden_size",
            getattr(self.encoder.config, "d_model", None),
        )
        if encoder_hidden is None:
            raise ValueError(
                f"Could not determine hidden size for {encoder_name_or_path}. "
                "Expected `hidden_size` or `d_model` in config."
            )

        self.tagset_size = tagset_size
        self.dropout = nn.Dropout(p=dropout_rate)
        self.classifier = nn.Linear(encoder_hidden, tagset_size + 2)
        self.crf = CRF(
            target_size=tagset_size,
            average_batch=True,
            use_cuda=use_cuda,
        )

    @property
    def _is_encoder_decoder(self):
        return bool(getattr(self.encoder.config, "is_encoder_decoder", False))

    def _encode(self, input_ids, attention_mask=None):
        if self._is_encoder_decoder:
            encoder = getattr(self.encoder, "encoder", None)
            if encoder is None:
                raise AttributeError(
                    "Encoder-decoder model is missing `.encoder`. "
                    "Please load a supported architecture."
                )
            outputs = encoder(
                input_ids=input_ids,
                attention_mask=attention_mask,
                return_dict=True,
            )
        else:
            outputs = self.encoder(
                input_ids=input_ids,
                attention_mask=attention_mask,
                return_dict=True,
            )
        return outputs.last_hidden_state

    def get_output_score(self, sentence, attention_mask=None):
        embeddings = self._encode(sentence, attention_mask=attention_mask)
        return self.classifier(self.dropout(embeddings))

    def compute_emissions(self, input_ids, attention_mask):
        return self.get_output_score(input_ids, attention_mask=attention_mask)

    def forward(self, sentence, masks, return_emissions=False):
        emissions = self.get_output_score(sentence, attention_mask=masks)
        if return_emissions:
            return type("Out", (), {"emissions": emissions})
        # Keep CRF dynamic programming in FP32 even when the encoder uses AMP.
        _, tag_seq = self.crf._viterbi_decode(emissions.float(), masks.bool())
        return tag_seq

    def neg_log_likelihood_loss(self, sentence, mask, tags):
        emissions = self.get_output_score(sentence, attention_mask=mask)
        # Long CRF recurrences are numerically fragile in FP16/BF16.
        loss_value = self.crf.neg_log_likelihood_loss(emissions.float(), mask, tags)
        if not torch.isfinite(loss_value).item():
            finite_emissions = torch.isfinite(emissions)
            nonfinite_count = int((~finite_emissions).sum().item())
            if nonfinite_count:
                raise FloatingPointError(
                    "CRF received non-finite encoder/classifier emissions: "
                    f"{nonfinite_count}/{emissions.numel()} values are NaN or Inf; "
                    f"emission_dtype={emissions.dtype}."
                )
            raise FloatingPointError(
                "CRF loss became non-finite even though all encoder/classifier "
                f"emissions were finite; emission_dtype={emissions.dtype}."
            )
        return loss_value / float(emissions.size(0))
