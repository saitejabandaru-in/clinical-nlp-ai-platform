from __future__ import annotations

import re

from .schemas import ClinicalEntity


LEXICON: dict[str, tuple[str, str]] = {
    "diabetes": ("DIAGNOSIS", "diabetes mellitus"),
    "hypertension": ("DIAGNOSIS", "hypertension"),
    "pneumonia": ("DIAGNOSIS", "pneumonia"),
    "asthma": ("DIAGNOSIS", "asthma"),
    "heart failure": ("DIAGNOSIS", "heart failure"),
    "chest pain": ("SYMPTOM", "chest pain"),
    "shortness of breath": ("SYMPTOM", "dyspnea"),
    "fever": ("SYMPTOM", "fever"),
    "metformin": ("MEDICATION", "metformin"),
    "lisinopril": ("MEDICATION", "lisinopril"),
    "albuterol": ("MEDICATION", "albuterol"),
    "insulin": ("MEDICATION", "insulin"),
    "x-ray": ("PROCEDURE", "x-ray"),
    "ct scan": ("PROCEDURE", "ct scan"),
    "ekg": ("PROCEDURE", "electrocardiogram"),
}


def extract_entities(text: str) -> list[ClinicalEntity]:
    """Extract clinical entities using a transparent lexicon matcher."""
    entities: list[ClinicalEntity] = []
    lowered = text.lower()

    for phrase, (label, normalized) in LEXICON.items():
        for match in re.finditer(rf"\b{re.escape(phrase)}\b", lowered):
            entities.append(
                ClinicalEntity(
                    text=text[match.start() : match.end()],
                    label=label,
                    start=match.start(),
                    end=match.end(),
                    confidence=0.82,
                    normalized=normalized,
                )
            )

    return sorted(entities, key=lambda entity: (entity.start, entity.end))

