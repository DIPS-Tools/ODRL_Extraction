from __future__ import annotations
import re
from typing import List, Sequence, Dict, Any
import torch


"""
Hybrid extraction rules for BERT+BiLSTM+CRF
============================================

This module owns both stages of hybrid extraction:
  1. add positive rule bias to emissions before CRF Viterbi decoding;
  2. refine decoded BIO labels with deterministic post-processing.

The bias stage works with `BERT_LSTM_CRF` models that expose either:
  • `compute_emissions(input_ids, attention_mask)` or
  • `forward(..., return_emissions=True)` (returns object with `.emissions`)

If neither is available, we try `get_output_score(...)` or a forward
side‑effect attribute `.emissions`.

Use in eval/predict (no retraining):

    from src.hybrid_extraction_rules import decode_with_rule_bias, postprocess_tags

    pred_ids = decode_with_rule_bias(
        model, batch, batch_features, label2id=cfg.l2i, alpha_pos=3.0
    )

Then call your existing `recover_label(...)`.
"""


# ---------------------------------------------------------------------------
# Lexicons (lowercased where noted). Extend freely.
# ---------------------------------------------------------------------------
ACTION_VERBS = {
    "allow","perform","process","use","share","disclose","collect","receive","provide",
    "transfer","transmit","send","store","retain","delete","destroy","anonymize","pseudonymize",
    "aggregate","publish","access","view","monitor","profile","sell","reidentify","export","import","distribute"
}
ASSET_HEADS = {
    "data","information","record","records","content","document","documents","file","files","dataset","datasets",
    "metadata","log","logs","metric","metrics","identifier","identifiers","email","emails","name","names",
    "address","addresses","phone","phones","location","locations","biometric","financial","health","phi","pii",
    "account","accounts","credential","credentials","password","passwords","token","tokens","ip",
    "cookie","cookies","device","devices","telemetry","analytics","report","reports",
    "recording","recordings","output","outputs","material","materials","database","databases",
    "code","software","image","images","video","videos"
}
ASSET_MODIFIERS = {
    "audio", "video", "digital", "personal", "special", "category", "confidential",
    "customer", "user", "model", "training", "source", "derived", "licensed",
    "original", "research", "health", "financial", "shared", "biometric",
}
ASSET_DETERMINERS = {"the", "a", "an", "this", "that", "these", "those", "any", "all"}
DATA_PARTY_HEADS = {
    "controller", "controllers", "discloser", "disclosers", "exporter", "exporters",
    "importer", "importers", "owner", "owners", "processor", "processors",
    "provider", "providers", "receiver", "receivers", "recipient", "recipients",
}
DUTY_VERBS = {
    "ensure","implement","maintain","provide","notify","report","cooperate","obtain","document",
    "permit","audit","comply","protect","encrypt","pseudonymize","anonymize","delete","return","certify",
    "segregate","restrict","access","log","train"
}
JURISDICTIONS = {"EU","EEA","UK","United","States","US","California","Switzerland","Canada","Brazil","China","India"}

# Party role lexicons (all lowercase for phrase matching)
ASSIGNEE_PHRASES = [
    "the data recipient","data recipient","recipient",
    "the third party","third party","the third parties","third parties",
    "both parties","each party","either party","the parties","parties",
    "the licensee","licensee",
    "the end user","end user",
    "the authorized user","authorized user",
    "the authorized users","authorized users",
    "the users","users","the user","user",
    "the data processor","data processor","processor",
    "the service provider","service provider","service providers",
    "the vendor","vendor","vendors",
    "the contractor","contractor","contractors",
    "the researcher","researcher","researchers",
    "the requester","requester","requestor","requestors",
    "the applicant","applicant","applicants",
    "the partner","partner","partners",
    "the data importer","data importer",
    "the receiving party","receiving party",
    "the data receiver","data receiver","receiver",
]
ASSIGNER_PHRASES = [
    "the data provider","data provider",
    "the data owner","data owner","owner",
    "the licensor","licensor",
    "the discloser","discloser",
    "the disclosing party","disclosing party",
    "the data discloser","data discloser",
    "the data controller","data controller","controller",
    "the authority","authority","the authorities","authorities",
    "the competent authority","competent authority",
    "the competent authorities","competent authorities",
    "the government department","government department",
    "the government departments","government departments",
    "the public authority","public authority",
    "the public authorities","public authorities",
    "the police","police",
    "the probation services","probation services",
    "the youth offending team","youth offending team",
    "the youth offending teams","youth offending teams",
    "the london fire brigade","london fire brigade",
    "the public protection desk","public protection desk","ppd",
    "the data exporter","data exporter","exporter",
]
SINGLE_ASSIGNEE = {
    "recipient","licensee","processor","researcher","contractor","vendor",
    "user","users","requester","requestors","requestor","applicant","partner","partners",
    "importer","receiver"
}
SINGLE_ASSIGNER = {
    "provider","owner","licensor","discloser","controller","exporter",
    "authority","authorities","commission","commissioner","council","agency","agencies",
    "police","department","departments","brigade"
}

# CONSEQUENCE lexicons (all lowercase)
TRIGGER_WORDS = {
    "breach","breaches","breached","breaching",
    "violation","violations","violate","violates","violated","violating",
    "non-compliance","noncompliance","noncompliant","non-compliant",
    "default","defaults","defaulted","defaulting",
    "fail","fails","failed","failing","failure",
    "nonperformance","non-performance",
}
TRIGGER_PHRASES = [
    "material breach","in the event of","in case of","in the case of",
    "upon breach","upon any breach","on breach","on any breach",
    "failure to comply","breach of this agreement","breach of confidentiality",
    "breach of contract","breach of the agreement"
]
SANCTION_VERBS = {
    "terminate","terminates","terminated","terminating",
    "suspend","suspends","suspended","suspending",
    "revoke","revokes","revoked","revoking",
    "withdraw","withdraws","withdrew","withdrawn","withdrawing",
    "disable","disables","disabled","disabling",
    "block","blocks","blocked","blocking",
    "forfeit","forfeits","forfeited","forfeiting",
    "fine","fines","fined","fining",
    "penalize","penalise","penalizes","penalises","penalized","penalised","penalizing","penalising",
    "sanction","sanctions","sanctioned","sanctioning",
    "remedy","remedies","remedied","remedying",
    "cure","cures","cured","curing",
    "indemnify","indemnifies","indemnified","indemnifying",
    "refund","refunds","refunded","refunding",
    "cease","ceases","ceased","ceasing",
}
SANCTION_PARTICIPLES = {
    "terminated","suspended","revoked","withdrawn","disabled","blocked","forfeited","fined","penalized","penalised"
}
SANCTION_NOUNS = {
    "termination","suspension","revocation","withdrawal","forfeiture",
    "damages","penalty","penalties","fine","fines","sanctions",
    "liability","indemnity","indemnification","remedy","cure","cure period"
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_special(toks: Sequence[str]) -> List[str]:
    return [t for t in toks if t not in ("[CLS]","[SEP]")]


PURPOSE_PREFIXES = (
    ("in", "order", "to"),
    ("for", "the", "purpose", "of"),
    ("for", "purposes", "of"),
    ("with", "the", "aim", "of"),
    ("with", "the", "objective", "of"),
    ("so", "that"),
    ("to", "enable"),
    ("to", "facilitate"),
    ("to", "improve"),
    ("to", "support"),
    ("to", "ensure"),
    ("to", "comply"),
    ("to", "fulfil"),
    ("to", "fulfill"),
    ("to", "protect"),
    ("to", "prevent"),
    ("for", "research"),
    ("for", "academic", "research"),
    ("for", "scientific", "research"),
    ("for", "commercial", "use"),
    ("for", "non-commercial", "use"),
    ("for", "internal", "use"),
    ("for", "marketing"),
    ("for", "analytics"),
    ("for", "training"),
    ("for", "evaluation"),
    ("for", "security"),
    ("for", "compliance"),
)
PURPOSE_SINGLE_TOKENS = {"commercially"}
CLAUSE_PUNCTUATION = {",", ";", ".", "!", "?"}


def _purpose_spans(tokens: Sequence[str], limit: int = 40) -> List[tuple[int, int]]:
    """Return high-confidence, non-overlapping purpose spans."""
    low = [token.lower() for token in tokens]
    candidates: List[tuple[int, int]] = []

    for start, token in enumerate(low):
        if token in PURPOSE_SINGLE_TOKENS:
            candidates.append((start, start + 1))

        for prefix in PURPOSE_PREFIXES:
            width = len(prefix)
            if tuple(low[start:start + width]) != prefix:
                continue

            end = start + width
            while end < min(len(tokens), start + limit):
                if tokens[end] in CLAUSE_PUNCTUATION:
                    break
                end += 1
            candidates.append((start, end))

    # Prefer the longest match at a shared start and avoid duplicate overlaps.
    selected: List[tuple[int, int]] = []
    for span in sorted(set(candidates), key=lambda item: (item[0], -(item[1] - item[0]))):
        if not any(span[0] < end and span[1] > start for start, end in selected):
            selected.append(span)
    return selected


def _asset_spans(tokens: Sequence[str]) -> List[tuple[int, int]]:
    """Find conservative noun phrases ending in a known asset head."""
    low = [token.lower() for token in tokens]
    candidates: List[tuple[int, int]] = []

    for head, token in enumerate(low):
        if token not in ASSET_HEADS:
            continue
        if token == "data" and head + 1 < len(low) and low[head + 1] in DATA_PARTY_HEADS:
            continue

        start = head
        while start > 0 and low[start - 1] in ASSET_MODIFIERS:
            start -= 1
        if start > 0 and low[start - 1] in ASSET_DETERMINERS:
            start -= 1
        candidates.append((start, head + 1))

    # Prefer complete compounds such as "The audio recording" over the
    # overlapping one-token "audio" candidate.
    selected: List[tuple[int, int]] = []
    for span in sorted(set(candidates), key=lambda item: (-(item[1] - item[0]), item[0])):
        if not any(span[0] < end and span[1] > start for start, end in selected):
            selected.append(span)
    return sorted(selected)


# ---------------------------------------------------------------------------
# Rule bias builder
# ---------------------------------------------------------------------------

def build_rule_bias_for_tokens(
    tokens: Sequence[str],
    label2id: Dict[str,int],
    alpha_pos: float = 3.0,
    num_classes: int | None = None,
) -> torch.Tensor:
    """Return bias tensor [T_no_special, C] with +alpha on suggested tags.
    PURPOSE cues use PURPOSE labels when the checkpoint supports them and fall
    back to CONSTRAINT only for older schemas.
    If num_classes is provided, indices beyond it are skipped safely.
    """
    toks = _strip_special(tokens)
    T = len(toks)
    C = num_classes if num_classes is not None else max(label2id.values())+1
    bias = torch.zeros(T, C)
    low = [t.lower() for t in toks]
    txt = " ".join(low)

    def _idx(tag: str) -> int | None:
        i = label2id.get(tag)
        if i is None: return None
        if i >= C:    return None
        return i

    def add_span(start: int, end: int, btag: str, itag: str, scale: float = 1.0):
        if start < 0 or start >= T: return
        bi = _idx(btag); ii = _idx(itag)
        if bi is None or ii is None: return
        bias[start, bi] += alpha_pos * scale
        for k in range(start+1, min(end, T)):
            bias[k, ii] += alpha_pos * scale

    # RULE_TYPE cues ---------------------------------------------------------
    for m in re.finditer(r"\b(shall not|must not|may not|cannot|prohibited from)\b", txt):
        s = txt[:m.start()].count(" ")
        l = len(m.group(1).split())
        add_span(s, s+l, "B-RULE_TYPE-PROHIBITION", "I-RULE_TYPE-PROHIBITION")
    for m in re.finditer(r"\b(may(?!\s+not)|can(?!\s+not)|permitted to|authorized to)\b", txt):
        s = txt[:m.start()].count(" ")
        l = len(m.group(1).split())
        add_span(s, s+l, "B-RULE_TYPE-PERMISSION", "I-RULE_TYPE-PERMISSION")
    for m in re.finditer(r"\b(shall(?!\s+not)|must(?!\s+not)|is required to|will ensure)\b", txt):
        s = txt[:m.start()].count(" ")
        l = len(m.group(1).split())
        add_span(s, s+l, "B-RULE_TYPE-OBLIGATION", "I-RULE_TYPE-OBLIGATION")

    # PURPOSE cues -----------------------------------------------------------
    purpose_tags = (
        ("B-PURPOSE", "I-PURPOSE")
        if "B-PURPOSE" in label2id and "I-PURPOSE" in label2id
        else ("B-CONSTRAINT", "I-CONSTRAINT")
    )
    for start, end in _purpose_spans(toks):
        add_span(start, end, *purpose_tags)

    # Temporal constraints ---------------------------------------------------
    for m in re.finditer(r"\b(within|no\s+later\s+than|at\s+least|for|up\s+to|prior\s+to|after|before)\b\s+\d{1,4}\s+(day|days|week|weeks|month|months|year|years|hour|hours)\b", txt):
        s = txt[:m.start()].count(" ")
        l = len(m.group(0).split())
        add_span(s, s+l, "B-CONSTRAINT", "I-CONSTRAINT")

    def clause_end(start: int, limit: int = 30) -> int:
        end = start + 1
        while end < min(T, start + limit) and toks[end] not in {",", ";", "."}:
            end += 1
        return end

    # Date ranges and restrictive clauses found in the FastAPI usage log.
    for i, w in enumerate(low):
        if w == "between" and "and" in low[i + 1:min(T, i + 12)]:
            add_span(i, clause_end(i, limit=14), "B-CONSTRAINT", "I-CONSTRAINT")
        elif w == "until":
            add_span(i, clause_end(i, limit=10), "B-CONSTRAINT", "I-CONSTRAINT")
        elif w == "only" and i + 1 < T and low[i + 1] in {
            "to", "with", "for", "by", "if", "when", "where", "after", "before"
        }:
            add_span(i, clause_end(i), "B-CONSTRAINT", "I-CONSTRAINT")

    for marker in ("subject to", "provided that", "on condition that"):
        marker_tokens = marker.split()
        width = len(marker_tokens)
        for i in range(0, max(0, T - width + 1)):
            if low[i:i + width] == marker_tokens:
                add_span(i, clause_end(i), "B-CONSTRAINT", "I-CONSTRAINT")

    # Location constraints ---------------------------------------------------
    for i, w in enumerate(low):
        if w in {"outside","within","in"}:
            end = i+1; found = False
            while end < min(T, i+8):
                if toks[end] in JURISDICTIONS: found = True
                if toks[end] in {",",";","."}: break
                end += 1
            if found:
                add_span(i, end, "B-CONSTRAINT", "I-CONSTRAINT")

    # DUTY cues --------------------------------------------------------------
    for m in re.finditer(r"\b(provided\s+that|so\s+long\s+as|on\s+condition\s+that)\b", txt):
        s = txt[:m.start()].count(" ")
        l = len(m.group(1).split())
        add_span(s, s+l, "B-DUTY", "I-DUTY")
    for i, w in enumerate(low):
        if w in DUTY_VERBS:
            end = i+1
            while end < T and toks[end] not in {",",";","."}:
                end += 1
            add_span(i, end, "B-DUTY", "I-DUTY")

    # CONSEQUENCE (trigger → sanction on right) ------------------------------
    HAS_CONSEQ = ("B-CONSEQUENCE" in label2id) and ("I-CONSEQUENCE" in label2id)
    if HAS_CONSEQ:
        trigger_pos = set(i for i, w in enumerate(low) if w in TRIGGER_WORDS)
        for phrase in TRIGGER_PHRASES:
            ph = phrase.split(); Lp = len(ph)
            if Lp and Lp <= T:
                for i in range(0, T - Lp + 1):
                    if low[i:i+Lp] == ph:
                        trigger_pos.add(i + Lp - 1)

        def has_trigger_within(i: int, back: int = 12) -> bool:
            left = max(0, i - back)
            return any(t >= left and t <= i for t in trigger_pos)

        # sanction verbs
        for i, w in enumerate(low):
            if w in SANCTION_VERBS and has_trigger_within(i):
                print(w)
                end = i + 1
                while end < T and toks[end] not in {",",";","."}:
                    end += 1
                add_span(i, end, "B-CONSEQUENCE", "I-CONSEQUENCE")

        # passive participles: "be terminated" etc.
        BE = {"be","is","are","was","were","been","being","shall","will","may","can","must"}
        for i in range(0, max(0, T-1)):
            if low[i] in BE and low[i+1] in SANCTION_PARTICIPLES and has_trigger_within(i+1):
                start = i+1; end = start+1
                while end < T and toks[end] not in {",",";","."}:
                    end += 1
                add_span(start, end, "B-CONSEQUENCE", "I-CONSEQUENCE")

        # sanction nouns: "termination of ..."
        for i, w in enumerate(low):
            if w in SANCTION_NOUNS and has_trigger_within(i):
                start = i; end = i+1
                if end < T and low[end] == "of":
                    end += 1
                    while end < T and toks[end] not in {",",";","."}:
                        end += 1
                add_span(start, end, "B-CONSEQUENCE", "I-CONSEQUENCE")

    # PARTY roles ------------------------------------------------------------
    dets = {"the","a","an"}
    for phrase in ASSIGNEE_PHRASES:
        ph = phrase.split(); Lp = len(ph)
        if not Lp or Lp > T: continue
        for i in range(0, T - Lp + 1):
            if low[i:i+Lp] == ph:
                off = 1 if ph[0] in dets and Lp > 1 else 0
                add_span(i+off, i+Lp, "B-PARTY_ASSIGNEE", "I-PARTY_ASSIGNEE")
    for phrase in ASSIGNER_PHRASES:
        ph = phrase.split(); Lp = len(ph)
        if not Lp or Lp > T: continue
        for i in range(0, T - Lp + 1):
            if low[i:i+Lp] == ph:
                off = 1 if ph[0] in dets and Lp > 1 else 0
                add_span(i+off, i+Lp, "B-PARTY_ASSIGNER", "I-PARTY_ASSIGNER")

    for i, w in enumerate(low):
        if w in SINGLE_ASSIGNEE:
            add_span(i, i+1, "B-PARTY_ASSIGNEE", "I-PARTY_ASSIGNEE")
        if w in SINGLE_ASSIGNER:
            add_span(i, i+1, "B-PARTY_ASSIGNER", "I-PARTY_ASSIGNER")

    # Conservative ASSET phrase prior ---------------------------------------
    for start, end in _asset_spans(toks):
        add_span(start, end, "B-ASSET", "I-ASSET", scale=0.8)

    return bias


def build_batch_rule_bias(
    features: List[Any],
    attn_mask: torch.Tensor,
    label2id: Dict[str,int],
    device: torch.device,
    alpha_pos: float = 3.0,
    num_classes: int | None = None,
) -> torch.Tensor:
    """Return bias tensor [B, T, C] aligned to batched inputs (with specials).
    If num_classes is provided, bias width is C and tags with index >= C are ignored.
    """
    B, T = attn_mask.shape
    C = num_classes if num_classes is not None else max(label2id.values())+1
    bias = torch.zeros(B, T, C, device=device)

    act = attn_mask.bool()
    for b in range(B):
        active_idx = act[b].nonzero(as_tuple=False).squeeze(1)
        if active_idx.numel() < 3:
            continue
        start = int(active_idx[1].item())     # skip CLS
        end   = int(active_idx[-2].item())+1  # include last real token; skip SEP
        toks = features[b].text if isinstance(features[b].text, list) else str(features[b].text).split()
        per = build_rule_bias_for_tokens(toks, label2id, alpha_pos=alpha_pos, num_classes=C).to(device)
        L = min(per.shape[0], end-start)
        bias[b, start:start+L, :C] += per[:L, :C]
    return bias

# ---------------------------------------------------------------------------
# Emissions getter & decode
# ---------------------------------------------------------------------------

def _get_emissions(model: Any, input_ids: torch.Tensor, attention_mask: torch.Tensor):
    """Obtain emissions [B,T,C] robustly from your model.
    Order of preference:
      1) compute_emissions(input_ids, attention_mask)
      2) forward(..., return_emissions=True)
      3) forward(...) then read model.emissions (side effect)
      4) get_output_score(input_ids, attention_mask)
    """
    # 1) Dedicated method
    if hasattr(model, "compute_emissions"):
        try:
            return model.compute_emissions(input_ids=input_ids, attention_mask=attention_mask)
        except TypeError:
            return model.compute_emissions(input_ids, attention_mask)

    # 2) Forward with return_emissions
    try:
        out = model(input_ids=input_ids, attention_mask=attention_mask, return_emissions=True)
        if hasattr(out, "emissions"):
            return out.emissions
        if isinstance(out, (tuple, list)) and len(out) >= 2 and isinstance(out[1], torch.Tensor):
            return out[1]
        if isinstance(out, torch.Tensor) and out.dim() == 3:
            return out
    except TypeError:
        try:
            out = model(input_ids, attention_mask, return_emissions=True)
            if hasattr(out, "emissions"):
                return out.emissions
            if isinstance(out, (tuple, list)) and len(out) >= 2 and isinstance(out[1], torch.Tensor):
                return out[1]
            if isinstance(out, torch.Tensor) and out.dim() == 3:
                return out
        except TypeError:
            pass

    # 3) Side‑effect attribute
    try:
        _ = model(input_ids, attention_mask)
        if hasattr(model, "emissions") and isinstance(model.emissions, torch.Tensor):
            return model.emissions
    except Exception:
        pass

    # 4) Model‑specific helper
    if hasattr(model, "get_output_score"):
        try:
            return model.get_output_score(input_ids, attention_mask=attention_mask)
        except TypeError:
            return model.get_output_score(input_ids, attention_mask)

    raise RuntimeError(
        "Could not obtain emissions from model. Expose compute_emissions(...) or forward(..., return_emissions=True)."
    )


def decode_with_rule_bias(
    model: Any,
    batch: Sequence[torch.Tensor],
    batch_features: List[Any],
    device,
    label2id: Dict[str,int],
    alpha_pos: float = 3.0,
) -> List[List[int]]:
    """Return CRF‑decoded label IDs with rule bias added to emissions.

    batch: (input_ids, attention_mask, [labels])
    batch_features: matching InputFeatures for this batch (same order)
    label2id: mapping like cfg.l2i
    alpha_pos: strength of the rule bias (+logit)
    """
    # input_ids, attention_mask = batch[0], batch[1]
    # device = input_ids.device

    input_ids, attention_mask = batch[0], batch[1]

    input_ids = input_ids.to(device)
    attention_mask = attention_mask.to(device)

    # Base emissions
    emissions = _get_emissions(model, input_ids, attention_mask)  # [B,T,C]

    # Build aligned bias (match emission width)
    num_classes = emissions.size(-1)
    bias = build_batch_rule_bias(batch_features, attention_mask, label2id, device, alpha_pos=alpha_pos, num_classes=num_classes)

    # Decode with CRF
    emissions = emissions + bias
    if not hasattr(model, "crf"):
        raise RuntimeError("Model has no `.crf` for decode().")
    if hasattr(model.crf, "decode"):
        pred_ids = model.crf.decode(emissions, mask=attention_mask.bool())
    else:
        _, pred_ids = model.crf._viterbi_decode(emissions, attention_mask.bool())

    # Sanitize: map ids outside your label map (e.g., CRF START/STOP) to 'O'
    C_map = len(label2id)
    o_idx = int(label2id.get("O", 0))
    clean_pred_ids: List[List[int]] = []
    for seq in pred_ids:
        clean_seq = []
        for tid in seq:
            t = int(tid) if not isinstance(tid, int) else tid
            if t < 0 or t >= C_map:
                t = o_idx
            clean_seq.append(t)
        clean_pred_ids.append(clean_seq)

    return clean_pred_ids


# ---------------------------------------------------------------------------
# Deterministic post-processing after CRF decoding
# ---------------------------------------------------------------------------

def _tag_range(
    tags: List[str],
    start: int,
    end: int,
    btag: str,
    itag: str,
) -> None:
    """Apply a BIO label to the half-open token range ``[start, end)``."""
    if start < 0 or start >= len(tags) or end <= start:
        return
    tags[start] = btag
    for index in range(start + 1, min(end, len(tags))):
        tags[index] = itag


def _clause_end(tokens: Sequence[str], start: int, limit: int = 40) -> int:
    end = start + 1
    while end < min(len(tokens), start + limit) and tokens[end] not in CLAUSE_PUNCTUATION:
        end += 1
    return end


def _mark_phrase_clauses(
    tokens: Sequence[str],
    tags: List[str],
    phrases: Sequence[Sequence[str]],
    btag: str,
    itag: str,
) -> None:
    low = [token.lower() for token in tokens]
    for phrase in phrases:
        width = len(phrase)
        for start in range(0, max(0, len(low) - width + 1)):
            if tuple(low[start:start + width]) == tuple(phrase):
                _tag_range(tags, start, _clause_end(tokens, start), btag, itag)


def postprocess_tags(
    tokens: Sequence[str],
    tags: Sequence[str],
    *,
    purpose_as_constraint: bool = False,
) -> List[str]:
    """Refine decoded labels using high-confidence legal-language cues.

    The returned labels remain aligned one-to-one with ``tags``. Purpose cues
    are emitted as PURPOSE for the current schema; callers supporting an older
    schema can request the historical CONSTRAINT fallback.
    """
    out = list(tags)
    tokens_view = list(tokens[:len(out)])
    low = [token.lower() for token in tokens_view]
    txt = " ".join(low)

    # Canonical rule types used by the trained Contract-BERT checkpoint.
    rule_patterns = (
        (
            r"\b(may(?!\s+not)|can(?!\s+not)|permitted to|authorized to)\b",
            "B-RULE_TYPE-PERMISSION",
            "I-RULE_TYPE-PERMISSION",
        ),
        (
            r"\b(shall(?!\s+not)|must(?!\s+not)|is required to|will ensure)\b",
            "B-RULE_TYPE-OBLIGATION",
            "I-RULE_TYPE-OBLIGATION",
        ),
        # Apply multi-token prohibitions last so they take precedence over a
        # modal's weaker standalone permission/obligation interpretation.
        (
            r"\b(shall not|must not|may not|cannot|prohibited from)\b",
            "B-RULE_TYPE-PROHIBITION",
            "I-RULE_TYPE-PROHIBITION",
        ),
    )
    for pattern, btag, itag in rule_patterns:
        for match in re.finditer(pattern, txt):
            start = txt[:match.start()].count(" ")
            end = start + len(match.group(1).split())
            _tag_range(out, start, end, btag, itag)

    # Recover high-confidence asset phrases when the model missed them. Do not
    # replace tokens already assigned to a different component.
    for start, end in _asset_spans(tokens_view):
        if all(out[index] == "O" or out[index].endswith("ASSET") for index in range(start, end)):
            _tag_range(out, start, end, "B-ASSET", "I-ASSET")

    # Expand a model-predicted asset left across an adjacent title-cased name.
    for index in range(min(len(tokens_view), len(out))):
        if not out[index].endswith("ASSET") or low[index] not in ASSET_HEADS:
            continue
        left = index
        while (
            left > 0
            and tokens_view[left - 1][:1].isupper()
            and out[left - 1] in {"O", "I-ASSET"}
        ):
            left -= 1
        if left < index:
            _tag_range(out, left, index + 1, "B-ASSET", "I-ASSET")

    # Temporal constraints.
    temporal_pattern = re.compile(
        r"\b(within|no\s+later\s+than|at\s+least|for|up\s+to|prior\s+to|after|before)\b"
        r"\s+\d{1,4}\s+(day|days|week|weeks|month|months|year|years|hour|hours)\b"
    )
    for match in temporal_pattern.finditer(txt):
        start = txt[:match.start()].count(" ")
        _tag_range(
            out,
            start,
            start + len(match.group(0).split()),
            "B-CONSTRAINT",
            "I-CONSTRAINT",
        )

    # Conditional, restrictive, date-range, and jurisdiction constraints.
    constraint_phrases = (
        ("subject", "to"),
        ("provided", "that"),
        ("on", "condition", "that"),
        ("so", "long", "as"),
    )
    _mark_phrase_clauses(
        tokens_view,
        out,
        constraint_phrases,
        "B-CONSTRAINT",
        "I-CONSTRAINT",
    )
    for index, token in enumerate(low):
        if token == "between" and "and" in low[index + 1:min(len(low), index + 12)]:
            _tag_range(out, index, _clause_end(tokens_view, index, 14), "B-CONSTRAINT", "I-CONSTRAINT")
        elif token == "until":
            _tag_range(out, index, _clause_end(tokens_view, index, 10), "B-CONSTRAINT", "I-CONSTRAINT")
        elif token == "only" and index + 1 < len(low) and low[index + 1] in {
            "to", "with", "for", "by", "if", "when", "where", "after", "before"
        }:
            _tag_range(out, index, _clause_end(tokens_view, index), "B-CONSTRAINT", "I-CONSTRAINT")
        elif token in {"outside", "within", "in"}:
            end = index + 1
            found_jurisdiction = False
            while end < min(len(tokens_view), index + 8):
                if tokens_view[end] in JURISDICTIONS:
                    found_jurisdiction = True
                if tokens_view[end] in CLAUSE_PUNCTUATION:
                    break
                end += 1
            if found_jurisdiction:
                _tag_range(out, index, end, "B-CONSTRAINT", "I-CONSTRAINT")

    # Purpose is applied last so explicit purpose cues correct PURPOSE spans
    # that the model confused with CONSTRAINT or other nested components.
    purpose_tags = (
        ("B-CONSTRAINT", "I-CONSTRAINT")
        if purpose_as_constraint
        else ("B-PURPOSE", "I-PURPOSE")
    )
    for start, end in _purpose_spans(tokens_view):
        _tag_range(out, start, end, *purpose_tags)

    return out


def apply_rules_to_predictions(
    pred_bio: List[List[str]],
    features: List[object],
) -> List[List[str]]:
    """Apply deterministic post-processing to a prediction batch."""
    fixed: List[List[str]] = []
    for index, tags in enumerate(pred_bio):
        if index >= len(features):
            fixed.append(list(tags))
            continue

        feature = features[index]
        tokens = feature.text if isinstance(feature.text, list) else str(feature.text).split()
        tokens = _strip_special(tokens)[:len(tags)]
        fixed.append(postprocess_tags(tokens, tags))
    return fixed


# ---------------------------------------------------------------------------
# Tiny self‑check
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    class _Feat:  # mimic InputFeatures
        def __init__(self, text): self.text = text

    toks = ["[CLS]","If","a","material","breach","occurs",",","the","Provider","may","terminate","this","Agreement",".","[SEP]"]
    feats = [_Feat(toks)]
    mask = torch.tensor([[1]*len(toks)])
    l2i = {k:i for i,k in enumerate([
        "<pad>","<start>","<eos>","O",
        "B-ACTION","I-ACTION","B-ASSET","I-ASSET",
        "B-PARTY_ASSIGNER","I-PARTY_ASSIGNER","B-PARTY_ASSIGNEE","I-PARTY_ASSIGNEE",
        "B-RULE_TYPE","I-RULE_TYPE","B-CONSTRAINT","I-CONSTRAINT","B-DUTY","I-DUTY",
        "B-CONSEQUENCE","I-CONSEQUENCE",
    ])}
    B,T,C = 1,len(toks),len(l2i)
    dummy_emissions = torch.zeros(B,T,C)
    bias = build_batch_rule_bias(feats, mask, l2i, device=torch.device("cpu"), alpha_pos=3.0, num_classes=C)
    print("bias shape:", bias.shape)  # [1, T, C]
