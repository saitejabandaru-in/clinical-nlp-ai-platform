from __future__ import annotations

from .schemas import SentimentResult
from .tokenizer import sentences


POSITIVE_TERMS = {"improved", "stable", "resolved", "normal", "controlled", "better", "tolerating"}
NEGATIVE_TERMS = {"worsening", "severe", "critical", "abnormal", "elevated", "uncontrolled", "pain", "fever"}


def analyze_sentiment(text: str) -> SentimentResult:
    """Classify clinical outcome tone with auditable keyword evidence."""
    positive_hits: list[str] = []
    negative_hits: list[str] = []

    for sentence in sentences(text):
        lowered = sentence.lower()
        if any(term in lowered for term in POSITIVE_TERMS):
            positive_hits.append(sentence)
        if any(term in lowered for term in NEGATIVE_TERMS):
            negative_hits.append(sentence)

    score = len(positive_hits) - len(negative_hits)
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    total = len(positive_hits) + len(negative_hits)
    confidence = min(0.95, 0.5 + (abs(score) / max(total, 1)) * 0.45)
    return SentimentResult(label=label, score=round(confidence, 3), evidence=positive_hits + negative_hits)

