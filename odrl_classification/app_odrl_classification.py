"""Standalone FastAPI service and reusable runtime for ODRL classification."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, Optional

import torch
import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from transformers import BertConfig, BertTokenizer

try:
    from odrl_classification.src.models.bert import Model
except ModuleNotFoundError:  # Support: python odrl_classification/app_....py
    from src.models.bert import Model


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHECKPOINT = (
    Path(__file__).resolve().parent / "odrl_save_dic" / "bertep5bz16mq190.pt"
)
LABELS = {0: "non", 1: "odrl"}


class ClassificationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to classify.")
    uid: Optional[str] = Field(default=None, description="Optional caller record ID.")


class ClassificationResponse(BaseModel):
    uid: Optional[str]
    text: str
    category: str
    is_odrl: bool
    confidence: float
    probabilities: Dict[str, float]


class ODRLClassifier:
    """Load the trained BERT binary classifier and expose stable inference."""

    def __init__(
        self,
        word_embedding_model_path: str,
        checkpoint_path: str,
        pad_size: int = 190,
        device: str = "cpu",
    ) -> None:
        if pad_size < 2:
            raise ValueError("pad_size must be at least 2")

        embedding_path = Path(word_embedding_model_path).expanduser().resolve()
        checkpoint = Path(checkpoint_path).expanduser().resolve()
        if not embedding_path.is_dir():
            raise FileNotFoundError(
                f"Classifier pretrained-model directory not found: {embedding_path}"
            )
        if not checkpoint.is_file():
            raise FileNotFoundError(f"Classifier checkpoint not found: {checkpoint}")

        requested_device = str(device).lower()
        if requested_device.startswith("cuda") and not torch.cuda.is_available():
            raise RuntimeError(
                f"classification_device={device!r} requested, but CUDA is unavailable"
            )

        self.device = torch.device(device)
        self.pad_size = int(pad_size)
        self.tokenizer = BertTokenizer.from_pretrained(str(embedding_path))
        bert_config = BertConfig.from_pretrained(str(embedding_path))
        model_config = SimpleNamespace(
            bert_path=str(embedding_path),
            bert_config=bert_config,
            hidden_size=int(bert_config.hidden_size),
            num_classes=len(LABELS),
        )
        self.model = Model(model_config).to(self.device)

        try:
            state = torch.load(
                str(checkpoint), map_location=self.device, weights_only=True
            )
        except TypeError:  # Compatibility with older PyTorch installations.
            state = torch.load(str(checkpoint), map_location=self.device)
        if isinstance(state, dict) and "state_dict" in state:
            state = state["state_dict"]
        self.model.load_state_dict(state)
        self.model.eval()

    def classify(self, text: str, uid: Optional[str] = None) -> Dict[str, object]:
        source_text = str(text).strip()
        if not source_text:
            raise ValueError("text must not be empty")

        # Match the preprocessing used to train the saved checkpoint exactly:
        # WordPiece tokens with a leading [CLS], no trailing [SEP], ID 0
        # padding, and truncation to pad_size.
        tokens = [self.tokenizer.cls_token or "[CLS]"] + self.tokenizer.tokenize(
            source_text
        )
        token_ids = self.tokenizer.convert_tokens_to_ids(tokens)
        if len(token_ids) < self.pad_size:
            attention_mask_values = [1] * len(token_ids) + [0] * (
                self.pad_size - len(token_ids)
            )
            token_ids.extend([0] * (self.pad_size - len(token_ids)))
        else:
            token_ids = token_ids[: self.pad_size]
            attention_mask_values = [1] * self.pad_size
        input_ids = torch.tensor(
            [token_ids], dtype=torch.long, device=self.device
        )
        attention_mask = torch.tensor(
            [attention_mask_values], dtype=torch.long, device=self.device
        )

        # The original classifier model expects (input_ids, sequence_length,
        # attention_mask). It only consumes positions 0 and 2.
        model_input = (input_ids, None, attention_mask)
        with torch.inference_mode():
            logits = self.model(model_input)
            probabilities = torch.softmax(logits, dim=-1)[0].detach().cpu()

        predicted_id = int(torch.argmax(probabilities).item())
        category = LABELS[predicted_id]
        probability_map = {
            LABELS[index]: float(probabilities[index].item())
            for index in sorted(LABELS)
        }
        return {
            "uid": uid,
            "text": source_text,
            "category": category,
            "is_odrl": category == "odrl",
            "confidence": probability_map[category],
            "probabilities": probability_map,
        }


app = FastAPI(
    title="ODRL Description Classification API",
    description="Classify text as an ODRL rule description or ordinary text.",
)
templates = Jinja2Templates(directory=str(PROJECT_ROOT / "templates"))
classifier: Optional[ODRLClassifier] = None


def _require_classifier() -> ODRLClassifier:
    if classifier is None:
        raise HTTPException(
            status_code=503,
            detail="The ODRL classification model has not been initialized.",
        )
    return classifier


@app.get("/")
def index():
    return RedirectResponse(url="/classifier", status_code=307)


@app.get("/classifier")
def classifier_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="odrl-classification.html",
        context={"question": None, "result": None},
    )


@app.post("/classifier")
def classifier_page_predict(request: Request, text: str = Form(...)):
    try:
        result = _require_classifier().classify(text)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return templates.TemplateResponse(
        request=request,
        name="odrl-classification.html",
        context={"question": text, "result": result},
    )


@app.get("/prediction/")
def legacy_prediction_page():
    """Give browser users a useful page instead of a 405 response."""
    return RedirectResponse(url="/classifier", status_code=307)


@app.get("/health")
def health():
    if classifier is None:
        raise HTTPException(status_code=503, detail="Classifier not initialized")
    return {"status": "ok", "model": "bert-odrl-classifier"}


@app.post("/classify", response_model=ClassificationResponse)
def classify(payload: ClassificationRequest):
    try:
        return _require_classifier().classify(payload.text, payload.uid)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/prediction/", response_model=ClassificationResponse)
def legacy_prediction(text: str = Form(...), uid: Optional[str] = Form(default=None)):
    """Compatibility endpoint for clients of the previous Flask application."""
    try:
        return _require_classifier().classify(text, uid)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--word_embedding_model_path",
        default=os.getenv(
            "ODRL_CLASSIFICATION_MODEL_PATH",
            "/home/mh1f25/scratch/llms_model/bert-base-cased",
        ),
        help="Local bert-base-cased directory used to build the classifier.",
    )
    parser.add_argument(
        "--checkpoint_path",
        default=os.getenv("ODRL_CLASSIFICATION_CHECKPOINT", str(DEFAULT_CHECKPOINT)),
        help="Trained ODRL classifier checkpoint.",
    )
    parser.add_argument("--pad_size", type=int, default=190)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)
    return parser


def main() -> None:
    global classifier
    args = build_parser().parse_args()
    classifier = ODRLClassifier(
        word_embedding_model_path=args.word_embedding_model_path,
        checkpoint_path=args.checkpoint_path,
        pad_size=args.pad_size,
        device=args.device,
    )
    print(f"Classifier checkpoint: {Path(args.checkpoint_path).resolve()}")
    print(f"Classifier pad size: {args.pad_size}")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
