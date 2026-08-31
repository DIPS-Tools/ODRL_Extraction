"""Diagnose a local ModernBERT checkpoint before launching full NER training."""

import argparse
from pathlib import Path

import torch
import transformers
from transformers import AutoConfig, AutoModel, AutoTokenizer

from src.utils import _encode_sample, _read_jsonl, _words_from_text


ENTITY_TYPES = (
    "ASSIGNEE",
    "ACTION",
    "ASSET",
    "RULE_TYPE-PERMISSION",
    "RULE_TYPE-OBLIGATION",
    "RULE_TYPE-PROHIBITION",
    "CONSTRAINT",
    "PURPOSE",
)


def label_map():
    labels = ["O"]
    for entity_type in ENTITY_TYPES:
        labels.extend((f"B-{entity_type}", f"I-{entity_type}"))
    labels.extend(("<pad>", "<start>", "<eos>"))
    return {label: index for index, label in enumerate(labels)}


def tensor_from_output(output):
    if isinstance(output, torch.Tensor):
        return output
    if isinstance(output, (tuple, list)):
        for item in output:
            tensor = tensor_from_output(item)
            if tensor is not None:
                return tensor
    return getattr(output, "last_hidden_state", None)


def report_tensor(name, tensor):
    finite = torch.isfinite(tensor)
    count = int((~finite).sum().item())
    finite_values = tensor[finite]
    minimum = float(finite_values.min().item()) if finite_values.numel() else float("nan")
    maximum = float(finite_values.max().item()) if finite_values.numel() else float("nan")
    print(
        f"{name}: shape={tuple(tensor.shape)} dtype={tensor.dtype} "
        f"nonfinite={count}/{tensor.numel()} min={minimum:.6g} max={maximum:.6g}"
    )
    return count == 0


def run_forward(model, inputs, name, training=False):
    model.train(training)
    with torch.no_grad():
        output = model(**inputs, return_dict=True)
    hidden = output.last_hidden_state
    if not report_tensor(name, hidden):
        raise FloatingPointError(f"{name} produced non-finite hidden states")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", required=True)
    parser.add_argument("--dataset", default="")
    parser.add_argument("--max-length", type=int, default=400)
    parser.add_argument("--device", default="cuda")
    parser.add_argument(
        "--attention",
        choices=("eager", "sdpa", "flash_attention_2"),
        default="eager",
    )
    args = parser.parse_args()

    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA was requested but is not available")

    print(f"torch={torch.__version__} transformers={transformers.__version__} device={device}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, use_fast=True)
    config = AutoConfig.from_pretrained(args.model_path)
    config.reference_compile = False
    model = AutoModel.from_pretrained(
        args.model_path,
        config=config,
        attn_implementation=args.attention,
    )
    print(
        f"model_type={model.config.model_type} "
        f"reference_compile={getattr(model.config, 'reference_compile', 'n/a')} "
        f"attention={getattr(model.config, '_attn_implementation', 'unknown')} "
        f"vocab_size={model.config.vocab_size} pad_token_id={tokenizer.pad_token_id}"
    )

    model.to(device).eval()

    bad_parameters = []
    for name, parameter in model.named_parameters():
        if not torch.isfinite(parameter).all().item():
            bad_parameters.append(name)
    print(f"nonfinite_parameter_tensors={len(bad_parameters)}")
    if bad_parameters:
        raise FloatingPointError(f"Checkpoint contains non-finite parameters: {bad_parameters[:10]}")

    official = tokenizer(
        [
            "The document may be downloaded and retained for 30 days.",
            "The Data Controller shall consult the Data Processor.",
        ],
        padding="max_length",
        truncation=True,
        max_length=64,
        return_tensors="pt",
    )
    official = {key: value.to(device) for key, value in official.items()}
    print(
        f"official_input_ids=[{int(official['input_ids'].min())}, "
        f"{int(official['input_ids'].max())}] valid_tokens={int(official['attention_mask'].sum())}"
    )
    run_forward(model, official, "official_tokenizer_eval_forward")
    run_forward(model, official, "official_tokenizer_train_forward", training=True)

    if args.dataset:
        dataset = Path(args.dataset)
        if not dataset.is_file():
            raise FileNotFoundError(dataset)
        samples = _read_jsonl(str(dataset), tokenizer=tokenizer)
        l2i = label_map()
        features = []
        for text, labels in samples[:8]:
            words = _words_from_text(text, tokenizer)
            features.append(
                _encode_sample(
                    words,
                    labels,
                    tokenizer,
                    l2i,
                    args.max_length,
                    tokenizer.cls_token_id,
                    tokenizer.sep_token_id,
                    tokenizer.pad_token_id,
                    l2i["<pad>"],
                )
            )
        input_ids = torch.tensor([feature.input_id for feature in features], device=device)
        attention_mask = torch.tensor([feature.input_mask for feature in features], device=device)
        print(
            f"project_input_ids=[{int(input_ids.min())}, {int(input_ids.max())}] "
            f"valid_tokens={int(attention_mask.sum())} "
            f"padding_is_correct={bool(torch.all(input_ids[attention_mask == 0] == tokenizer.pad_token_id))}"
        )
        run_forward(
            model,
            {"input_ids": input_ids, "attention_mask": attention_mask},
            "project_preprocessing_eval_forward",
        )
        run_forward(
            model,
            {"input_ids": input_ids, "attention_mask": attention_mask},
            "project_preprocessing_train_forward",
            training=True,
        )

    print("ModernBERT forward diagnostics passed.")


if __name__ == "__main__":
    main()
