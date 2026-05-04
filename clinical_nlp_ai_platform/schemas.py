from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ClinicalEntity:
    text: str
    label: str
    start: int
    end: int
    confidence: float
    normalized: str | None = None


@dataclass(frozen=True)
class ICD10Suggestion:
    code: str
    description: str
    evidence: str
    confidence: float


@dataclass(frozen=True)
class SentimentResult:
    label: str
    score: float
    evidence: list[str] = field(default_factory=list)

