# -*- coding: utf-8 -*-
import logging
import os
import argparse
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

import torch
import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from src.hybrid_bias import decode_with_rule_bias
from src.hybrid_rules import postprocess_tags
from model.config import Config
from odrl_output import format_odrl_output, split_sentences
from src.utils import _words_from_text

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)  # Only show errors, not warnings

app = FastAPI(title="ODRL Extraction Demo with Rule Bias")
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

config: Optional[Config] = None
model: Optional[torch.nn.Module] = None


class ODRLGenerationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Policy or contract text to label.")


class ODRLRule(BaseModel):
    source_text: str
    assignee: str
    action: str
    asset: str
    rule_type: str
    constraint: str
    purpose: str


class ODRLGenerationResponse(BaseModel):
    rules: List[ODRLRule]

def get_input(config, sample):
    """
    Build a single-sample batch (input_ids, attention_mask) for inference.
    Mirrors _encode_sample's "keep first subword" policy, but no labels needed.
    Returns:
        input_ids: LongTensor [1, max_length]
        masks:     LongTensor [1, max_length]
        words:     List[str]  (the truncated word-level tokens used)
    """
    tokenizer  = config.tokenizer
    max_length = config.max_length

    # Special token ids with safe fallbacks
    cls_id = tokenizer.cls_token_id if tokenizer.cls_token_id is not None else (
        tokenizer.bos_token_id if tokenizer.bos_token_id is not None else 101
    )
    sep_id = tokenizer.sep_token_id if tokenizer.sep_token_id is not None else (
        tokenizer.eos_token_id if tokenizer.eos_token_id is not None else 102
    )
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0

    # Word-level tokens (your own helper that splits words/punct like in training)
    words = _words_from_text(sample, tokenizer)

    # keep room for [CLS] and [SEP]
    max_words = max_length - 2
    words = words[:max_words]

    # Build ids/masks (keep only the FIRST subword for each word)
    input_ids = [cls_id]
    masks     = [1]

    for w in words:
        sub_tokens = tokenizer.tokenize(w)
        if not sub_tokens:
            sub_tokens = [tokenizer.unk_token or "[UNK]"]
        first_piece = sub_tokens[0]
        tok_id = tokenizer.convert_tokens_to_ids(first_piece)
        if tok_id is None:
            tok_id = tokenizer.unk_token_id if tokenizer.unk_token_id is not None else 100
        input_ids.append(tok_id)
        masks.append(1)

    # [SEP]
    input_ids.append(sep_id)
    masks.append(1)

    # pad to max_length
    if len(input_ids) < max_length:
        pad_len = max_length - len(input_ids)
        input_ids.extend([pad_id] * pad_len)
        masks.extend([0] * pad_len)
    else:
        input_ids = input_ids[:max_length]
        masks     = masks[:max_length]

    # to tensors (batch=1)
    input_ids = torch.tensor([input_ids], dtype=torch.long)
    masks     = torch.tensor([masks],     dtype=torch.long)

    return input_ids, masks, words

def _sanitize_paths(pred_ids, label2id):
    """Clamp any id outside label map width to 'O'."""
    C = len(label2id)
    o = int(label2id.get("O", 0))
    clean = []
    for seq in pred_ids:
        row = []
        for t in seq:
            ti = int(t) if not isinstance(t, int) else t
            row.append(ti if 0 <= ti < C else o)
        clean.append(row)
    return clean


def model2predict(model, config, sample, apply_post_rules=True):
    """
    Run the model on a single sentence using rule-biased decoding and return:
        tokens_used (word-level, truncated to fit),
        pred_labels (BIO tags aligned 1:1 to tokens_used)
    """
    model.eval()
    device = config.device

    # Build inputs (word-level tokens; 1st subword policy)
    input_ids, masks, words = get_input(config, sample)
    input_ids = input_ids.to(device)
    masks     = masks.to(device)

    # Build the features object Hybrid Bias expects.
    # It only needs .text; including specials is fine (they're stripped internally).
    features = [SimpleNamespace(text=["[CLS]", *words, "[SEP]"])]

    # Try rule-biased decode; fall back to plain decode on error
    with torch.no_grad():
        try:
            pred_ids = decode_with_rule_bias(
                model,
                batch=(input_ids, masks),
                batch_features=features,
                device=device,
                label2id=config.l2i,
                alpha_pos=getattr(config, "rule_bias_alpha", 3.0),  # tweakable
            )
        except Exception:
            logger.exception("Rule-biased decoding failed; using plain CRF decoding.")
            # Fallback: vanilla CRF decode via your forward
            tag_seq = model(input_ids, masks)  # (batch, seq_len) as list or tensor
            if isinstance(tag_seq, torch.Tensor):
                tag_seq = tag_seq.tolist()
            pred_ids = tag_seq

    # Sanitize any ids that aren’t in your map (e.g., CRF START/STOP)
    pred_ids = _sanitize_paths(pred_ids, config.l2i)

    # Take the first (and only) sample, trim to real tokens, drop [CLS]/[SEP]
    seq = pred_ids[0]
    valid_len = int(masks[0].sum().item())          # includes [CLS] + [SEP]
    seq = seq[:valid_len]
    seq = seq[1:-1]                                  # drop specials
    seq = seq[:len(words)]                           # align to word count

    # Map ids -> labels (unknowns → "O")
    i2l = config.i2l
    pred_labels = [i2l.get(int(t), "O") for t in seq]

    # (Optional) deterministic post-rules if you have them wired
    if apply_post_rules:
        try:
            model_labels = list(pred_labels)
            rule_labels = postprocess_tags(words, model_labels)
            # Older rules can emit labels from a different ODRL schema (for
            # example B-DUTY or B-RULE_TYPE). Keep only labels supported by
            # the checkpoint and retain the model prediction otherwise.
            pred_labels = [
                rule_label if rule_label in config.l2i else model_label
                for rule_label, model_label in zip(rule_labels, model_labels)
            ]
        except Exception:
            logger.exception("Deterministic post-processing failed; using biased CRF labels.")

    return {"text": words, "labels": pred_labels}



def load_model(cfg):
    """Build the inference model and load its best available checkpoint once."""
    print('do testing ...')
    logger.info('do testing ...')

    print('device: {}'.format(cfg.device))

    inference_model = cfg.build_model()

    best_model_path = cfg.save_path + '_best_f1.pth'
    last_model_path = cfg.save_path + '_last_model.pth'

    # Check if best_f1.pth exists, otherwise load last_model.pth
    if os.path.isfile(best_model_path):
        print(f"Loading best model from {best_model_path}")
        logger.info(f"Loading best model from {best_model_path}")
        inference_model.load_state_dict(torch.load(best_model_path, map_location=cfg.device, weights_only=True))
    elif os.path.isfile(last_model_path):
        print(f"Loading last model from {last_model_path}")
        logger.info(f"Loading last model from {last_model_path}")
        inference_model.load_state_dict(torch.load(last_model_path, map_location=cfg.device, weights_only=True))
    else:
        raise FileNotFoundError(f"Neither {best_model_path} nor {last_model_path} exists.")

    inference_model.eval()
    return inference_model


def query_test(inference_model, cfg, text):
    """Run one rule-assisted prediction using the startup-loaded model."""
    result = model2predict(inference_model, cfg, text)
    logger.info('------------------test result------------------')
    logger.info(result)

    # 结果输出
    print(f"text : {result['text']}")
    print(f"label : {result['labels']}")
    return result


def build_parser():
    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument("--model", required=True)
    parser.add_argument("--data_path", required=True, default="./data/")
    parser.add_argument("--save_dir", required=True, default="./save_models/")
    parser.add_argument("--word_embedding_model_path", required=True)  # e.g., "/home/.../bert-base-cased"
    parser.add_argument("--label_type", choices=["BIO", "BIOES"], default="BIO",
                        help="Tagging scheme to use for labels.")
    parser.add_argument("--trust_remote_code", action="store_true")

    # Training settings
    parser.add_argument("--num_epochs", type=int, default=2)
    parser.add_argument("--batch_size", type=int, default=16)
    # parser.add_argument("--pad_size", type=int, default=32)
    parser.add_argument("--learning_rate", type=float, default=5e-5)
    parser.add_argument("--device", default="cuda")

    # IDCNN hyperparams
    parser.add_argument("--num_filters", type=int, default=64)
    parser.add_argument("--cnn_dropout", type=float, default=0.4)
    parser.add_argument("--kernel_size", type=int, default=3)
    parser.add_argument("--num_block", type=int, default=4)



    # LSTM hyperparams
    parser.add_argument("--hidden_dim", type=int, default=768)
    parser.add_argument("--rnn_layers", type=int, default=2)
    parser.add_argument("--rnn_dropout", type=float, default=0.1)
    parser.add_argument("--proj_dropout", type=float, default=0.4)


    parser.add_argument("--max_length", type=int, default=400)
    parser.add_argument("--rule_bias_alpha", type=float, default=3.0,
                        help="Positive emission bias applied where extraction rules match.")

    # Labels handling
    parser.add_argument("--include_special_labels", action="store_true", default=True)


    parser.add_argument("--do_train",
                        action='store_true',
                        help="Whether to run training.")

    parser.add_argument("--do_test",
                        action='store_true',
                        help="Whether to run eval on the test set.")

    parser.add_argument("--host", default="0.0.0.0",
                        help="Host interface used by the FastAPI server.")
    parser.add_argument("--port", type=int, default=5000,
                        help="Port used by the FastAPI server.")

    return parser


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={'question': None, 'result': None},
    )


@app.post('/')
def predict(request: Request, text: str = Form(...)):
    if config is None or model is None:
        raise RuntimeError(
            "The inference model is not initialized. Start the service with "
            "`python app_rule_bias.py` and the required model arguments."
        )

    result = query_test(model, config, text)
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={'question': text, 'result': result},
    )


@app.post('/odrl_generation', response_model=ODRLGenerationResponse)
def odrl_generation(payload: ODRLGenerationRequest):
    """Return rule-assisted ODRL components for use by other tools.


     curl -X POST "http://10.22.12.250:5001/odrl_generation" \
    -H "Content-Type: application/json" \
    -d '{
      "text": "The document may be downloaded once and retained for 30 days."
    }'


    """
    if config is None or model is None:
        raise HTTPException(
            status_code=503,
            detail=(
                "The inference model is not initialized. Start the service with "
                "`python app_rule_bias.py` and the required model arguments."
            ),
        )

    rules = []
    for sentence in split_sentences(payload.text):
        result = query_test(model, config, sentence)
        rules.append({
            "source_text": sentence,
            **format_odrl_output(result["text"], result["labels"]),
        })
    return {"rules": rules}


if __name__ == '__main__':
    args = build_parser().parse_args()
    config = Config(args)
    config.rule_bias_alpha = args.rule_bias_alpha
    model = load_model(config)
    uvicorn.run(app, host=args.host, port=args.port)

    # Run the FastAPI rule-bias application with Contract-BERT:
    # python app_rule_bias.py --model contract-bert-lstm-crf --data_path ./data/ --save_dir ./save_model --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-uncased-contracts --do_test --num_epochs 20 --batch_size 16 --rnn_layers 1 --max_length 400 --label_type BIO --rule_bias_alpha 3.0 --device cpu --port 5001
