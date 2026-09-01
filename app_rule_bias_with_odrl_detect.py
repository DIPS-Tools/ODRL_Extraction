"""FastAPI service that gates ODRL extraction with ODRL classification."""

from __future__ import annotations

import threading
from pathlib import Path
from typing import List, Optional

import torch
import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app_rule_bias import (
    ODRLGenerationRequest,
    ODRLRule,
    build_parser as build_extraction_parser,
    load_model,
    query_test,
)
from model.config import Config
from odrl_classification.app_odrl_classification import (
    DEFAULT_CHECKPOINT,
    ClassificationResponse,
    ODRLClassifier,
)
from odrl_output import format_odrl_rules, split_sentences


ORDINARY_TEXT_WARNING = (
    "The input appears to be an ordinary description, not an ODRL rule description. "
    "ODRL extraction was not run."
)


class DetectedODRLGenerationResponse(BaseModel):
    is_odrl: bool
    classification: ClassificationResponse
    warning: Optional[str]
    rules: List[ODRLRule]


app = FastAPI(
    title="ODRL Classification and Extraction API",
    description=(
        "Classify input first, then run rule-biased ODRL extraction only for "
        "ODRL-related descriptions."
    ),
)
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

classification_model: Optional[ODRLClassifier] = None
extraction_config: Optional[Config] = None
extraction_model: Optional[torch.nn.Module] = None
odrl_threshold: float = 0.5
_classification_lock = threading.Lock()
_extraction_lock = threading.Lock()


def _ensure_models_ready() -> None:
    if classification_model is None or extraction_config is None or extraction_model is None:
        raise HTTPException(
            status_code=503,
            detail=(
                "The classification and extraction models are not initialized. "
                "Start this service with its classifier and extractor arguments."
            ),
        )


def _classify(text: str) -> dict:
    _ensure_models_ready()
    assert classification_model is not None
    with _classification_lock:
        return classification_model.classify(text)


def _accepted_as_odrl(classification: dict) -> bool:
    return float(classification["probabilities"]["odrl"]) >= odrl_threshold


def _extract(text: str) -> List[dict]:
    _ensure_models_ready()
    assert extraction_model is not None and extraction_config is not None
    rules: List[dict] = []
    with _extraction_lock:
        for sentence in split_sentences(text):
            prediction = query_test(extraction_model, extraction_config, sentence)
            rules.extend(
                format_odrl_rules(
                    sentence,
                    prediction["text"],
                    prediction["labels"],
                )
            )
    return rules


@app.get("/")
def index():
    return RedirectResponse(url="/odrl-ner-label", status_code=307)


@app.get("/classifier")
def classifier_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="odrl-classification.html",
        context={"question": None, "result": None},
    )


@app.post("/classifier")
def classifier_page_predict(request: Request, text: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="odrl-classification.html",
        context={"question": text, "result": _classify(text)},
    )


@app.get("/prediction/")
def legacy_prediction_page():
    return RedirectResponse(url="/classifier", status_code=307)


@app.get("/health")
def health():
    _ensure_models_ready()
    return {
        "status": "ok",
        "classification_model": "bert-odrl-classifier",
        "extraction_checkpoint": extraction_config.save_path,
        "odrl_threshold": odrl_threshold,
    }


@app.get("/odrl-ner-label")
def odrl_ner_label_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="odrl-ner-label.html",
        context={
            "question": None,
            "result": None,
            "classification": None,
            "warning": None,
        },
    )


@app.post("/")
@app.post("/odrl-ner-label")
def predict(request: Request, text: str = Form(...)):
    classification = _classify(text)
    accepted = _accepted_as_odrl(classification)
    result = None
    # The GUI displays token labels, so invoke the extractor once for the full
    # submitted text only when the classification gate accepts it.
    if accepted:
        assert extraction_model is not None and extraction_config is not None
        with _extraction_lock:
            result = query_test(extraction_model, extraction_config, text)
    return templates.TemplateResponse(
        request=request,
        name="odrl-ner-label.html",
        context={
            "question": text,
            "result": result,
            "classification": classification,
            "warning": None if accepted else ORDINARY_TEXT_WARNING,
        },
    )


@app.get("/visulize-records")
def visulize_records(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="visulize-records.html",
        context={},
    )


@app.get("/visualize-records")
def visualize_records_alias():
    return RedirectResponse(url="/visulize-records", status_code=307)


@app.post("/classify", response_model=ClassificationResponse)
def classify_only(payload: ODRLGenerationRequest):
    return _classify(payload.text)


@app.post("/odrl_generation", response_model=DetectedODRLGenerationResponse)
def odrl_generation(payload: ODRLGenerationRequest):
    classification = _classify(payload.text)
    accepted = _accepted_as_odrl(classification)
    if not accepted:
        return {
            "is_odrl": False,
            "classification": classification,
            "warning": ORDINARY_TEXT_WARNING,
            "rules": [],
        }

    return {
        "is_odrl": True,
        "classification": classification,
        "warning": None,
        "rules": _extract(payload.text),
    }


def build_parser():
    parser = build_extraction_parser()
    parser.description = __doc__
    parser.add_argument(
        "--classification_word_embedding_model_path",
        required=True,
        help="Local bert-base-cased directory for the ODRL classifier.",
    )
    parser.add_argument(
        "--classification_checkpoint_path",
        default=str(DEFAULT_CHECKPOINT),
        help="Trained binary ODRL-classification checkpoint.",
    )
    parser.add_argument(
        "--classification_pad_size",
        type=int,
        default=190,
        help="Classifier input length; 190 matches bertep5bz16mq190.pt.",
    )
    parser.add_argument(
        "--classification_device",
        default="cpu",
        help="Device for the classification model, normally cpu.",
    )
    parser.add_argument(
        "--odrl_threshold",
        type=float,
        default=0.5,
        help="Minimum classifier P(odrl) required before extraction runs.",
    )
    return parser


def main() -> None:
    global classification_model, extraction_config, extraction_model, odrl_threshold

    args = build_parser().parse_args()
    if not 0.0 <= args.odrl_threshold <= 1.0:
        raise ValueError("--odrl_threshold must be between 0 and 1")

    classification_model = ODRLClassifier(
        word_embedding_model_path=args.classification_word_embedding_model_path,
        checkpoint_path=args.classification_checkpoint_path,
        pad_size=args.classification_pad_size,
        device=args.classification_device,
    )
    odrl_threshold = args.odrl_threshold

    extraction_config = Config(args)
    extraction_config.rule_bias_alpha = args.rule_bias_alpha
    extraction_model = load_model(extraction_config)

    print(f"Classifier checkpoint: {Path(args.classification_checkpoint_path).resolve()}")
    print(f"Classifier ODRL threshold: {odrl_threshold}")
    print(f"Extraction checkpoint prefix: {extraction_config.save_path}")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
