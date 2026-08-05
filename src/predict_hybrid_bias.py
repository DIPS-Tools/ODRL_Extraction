"""Evaluate a trained model with rule-biased CRF decoding and post-rules."""

import os
from typing import List, Optional

import pandas as pd
import torch
from tqdm import tqdm

from .hybrid_extraction_rules import decode_with_rule_bias, postprocess_tags
from .utils import (
    InputFeatures,
    compute_entity_metrics_by_type,
    compute_token_metrics_by_tag,
    get_ner_fmeasure,
    recover_label,
)


def _device_from_cfg(cfg):
    if isinstance(cfg.device, torch.device):
        return cfg.device
    return torch.device(str(cfg.device))


def _sanitize_paths(pred_ids, label2id):
    """Replace CRF start/stop or otherwise unknown IDs with the O label."""
    valid_ids = set(label2id.values())
    o_id = int(label2id.get("O", 0))
    return [
        [int(tag_id) if int(tag_id) in valid_ids else o_id for tag_id in sequence]
        for sequence in pred_ids
    ]


def _feature_tokens(feature):
    if isinstance(feature.text, list):
        return [token for token in feature.text if token not in ("[CLS]", "[SEP]")]
    return str(feature.text).split()


def _apply_supported_post_rules(predictions, features, label2id):
    """Apply post-rules without shifting labels around the retained <start>."""
    refined_predictions = []

    for index, sequence in enumerate(predictions):
        original = list(sequence)
        if index >= len(features):
            refined_predictions.append(original)
            continue

        tokens = _feature_tokens(features[index])
        label_offset = 1 if original and original[0] == "<start>" else 0
        token_count = min(len(tokens), len(original) - label_offset)

        model_token_labels = original[label_offset:label_offset + token_count]
        rule_token_labels = postprocess_tags(
            tokens[:token_count],
            model_token_labels,
        )

        # Older rules can propose labels from another ODRL schema. Only accept
        # labels supported by this checkpoint; otherwise retain the model label.
        supported_labels = [
            rule_label if rule_label in label2id else model_label
            for rule_label, model_label in zip(rule_token_labels, model_token_labels)
        ]

        refined = list(original)
        refined[label_offset:label_offset + token_count] = supported_labels
        refined_predictions.append(refined)

    return refined_predictions


@torch.no_grad()
def run_test(
    model,
    cfg,
    test_dataloader,
    test_features: Optional[List[InputFeatures]] = None,
    out_path: Optional[str] = None,
    return_details: bool = False,
):
    """Evaluate using the same hybrid strategy as ``app_rule_bias.py``.

    The strategy has two stages:
      1. add rule bias to model emissions before CRF Viterbi decoding;
      2. apply supported deterministic post-rules to decoded BIO labels.
    """
    if test_features is None:
        raise ValueError("Rule-biased testing requires test_features for token alignment.")
    if cfg.label_type != "BIO":
        raise ValueError("The current hybrid rule strategy supports BIO checkpoints only.")

    device = _device_from_cfg(cfg)
    alpha = float(getattr(cfg, "rule_bias_alpha", 3.0))
    apply_post_rules = bool(getattr(cfg, "apply_rule_postprocess", True))

    model.eval()
    model.to(device)

    all_pred_ids = []
    all_gold_ids = []
    offset = 0

    for batch in tqdm(test_dataloader, desc="Testing with rule bias", leave=False):
        batch_size = batch[0].size(0)
        batch_features = test_features[offset:offset + batch_size]
        if len(batch_features) != batch_size:
            raise ValueError(
                "test_features and test_dataloader are not aligned: "
                f"needed {batch_size} features at offset {offset}, got {len(batch_features)}."
            )
        offset += batch_size

        pred_ids = decode_with_rule_bias(
            model,
            batch,
            batch_features,
            device=device,
            label2id=cfg.l2i,
            alpha_pos=alpha,
        )
        all_pred_ids.extend(_sanitize_paths(pred_ids, cfg.l2i))
        all_gold_ids.extend(batch[2].tolist())

    if offset != len(test_features):
        raise ValueError(
            "test_features and test_dataloader have different sample counts: "
            f"evaluated {offset}, found {len(test_features)} features."
        )

    pred_labels, gold_labels = recover_label(
        all_pred_ids,
        all_gold_ids,
        cfg.l2i,
        cfg.i2l,
    )

    if apply_post_rules:
        pred_labels = _apply_supported_post_rules(
            pred_labels,
            test_features,
            cfg.l2i,
        )

    base_labels = [label for label in cfg.labels if not label.startswith("<")]
    per_type_df = compute_entity_metrics_by_type(gold_labels, pred_labels)
    per_tag_df = compute_token_metrics_by_tag(gold_labels, pred_labels, base_labels)

    print(per_type_df)
    print(per_tag_df)

    alpha_name = format(alpha, "g").replace(".", "p")
    result_prefix = f"{cfg.save_path}_hybrid_rule_bias_alpha{alpha_name}"
    per_type_df.to_csv(result_prefix + "_metrics_per_type.csv", index=False)
    per_tag_df.to_csv(result_prefix + "_metrics_per_tag.csv", index=False)

    accuracy, precision, recall, f1 = get_ner_fmeasure(
        gold_labels,
        pred_labels,
        label_type=cfg.label_type,
    )
    metrics_df = pd.DataFrame([{
        "prediction_strategy": "rule_bias",
        "rule_bias_alpha": alpha,
        "post_rules": apply_post_rules,
        "num_sentences": len(gold_labels),
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }])

    if out_path is None:
        out_path = result_prefix + "_predictions.txt"
    output_dir = os.path.dirname(out_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    lines = []
    for index, (gold_sequence, pred_sequence) in enumerate(zip(gold_labels, pred_labels)):
        tokens = _feature_tokens(test_features[index])
        label_offset = 1 if gold_sequence and gold_sequence[0] == "<start>" else 0
        comparable_gold = gold_sequence[label_offset:]
        comparable_pred = pred_sequence[label_offset:]
        token_count = min(len(tokens), len(comparable_gold), len(comparable_pred))
        text = " ".join(tokens[:token_count])
        lines.append(
            f"{text}-->true_label--> {' '.join(comparable_gold[:token_count])}"
            f"-->predict_label--> {' '.join(comparable_pred[:token_count])}"
        )

    with open(out_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(lines))

    if return_details:
        details_df = pd.DataFrame({
            "text": [line.split("-->true_label-->")[0] for line in lines],
            "gold_labels": [" ".join(sequence) for sequence in gold_labels],
            "pred_labels": [" ".join(sequence) for sequence in pred_labels],
        })
        return metrics_df, details_df

    return metrics_df
