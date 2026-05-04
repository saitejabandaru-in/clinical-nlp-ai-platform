from __future__ import annotations

from dataclasses import asdict, dataclass

from .deidentifier import Redaction, deidentify
from .entity_extraction import extract_entities
from .icd10 import suggest_icd10
from .keywords import extract_keywords
from .schemas import ClinicalEntity, ICD10Suggestion, SentimentResult
from .section_splitter import split_sections
from .sentiment import analyze_sentiment
from .topics import infer_topics
from .word_cloud import build_word_cloud_data


@dataclass(frozen=True)
class ClinicalNLPResult:
    deidentified_text: str
    redactions: list[Redaction]
    sections: dict[str, str]
    entities: list[ClinicalEntity]
    sentiment: SentimentResult
    keywords: list[dict[str, int | str]]
    topics: list[dict[str, float | str]]
    icd10_suggestions: list[ICD10Suggestion]
    word_cloud: list[dict[str, int | str]]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def analyze_note(text: str) -> ClinicalNLPResult:
    if not text or not text.strip():
        raise ValueError("Clinical note text is required")

    deidentified_text, redactions = deidentify(text)
    sections = split_sections(deidentified_text)
    entities = extract_entities(deidentified_text)

    return ClinicalNLPResult(
        deidentified_text=deidentified_text,
        redactions=redactions,
        sections=sections,
        entities=entities,
        sentiment=analyze_sentiment(deidentified_text),
        keywords=extract_keywords(deidentified_text),
        topics=infer_topics(deidentified_text),
        icd10_suggestions=suggest_icd10(entities),
        word_cloud=build_word_cloud_data(deidentified_text),
    )

