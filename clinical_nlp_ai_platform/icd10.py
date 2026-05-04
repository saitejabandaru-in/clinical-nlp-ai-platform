from __future__ import annotations

from .schemas import ClinicalEntity, ICD10Suggestion


ICD10_MAP: dict[str, tuple[str, str]] = {
    "diabetes mellitus": ("E11.9", "Type 2 diabetes mellitus without complications"),
    "hypertension": ("I10", "Essential hypertension"),
    "pneumonia": ("J18.9", "Pneumonia, unspecified organism"),
    "asthma": ("J45.909", "Unspecified asthma, uncomplicated"),
    "heart failure": ("I50.9", "Heart failure, unspecified"),
}


def suggest_icd10(entities: list[ClinicalEntity]) -> list[ICD10Suggestion]:
    suggestions: list[ICD10Suggestion] = []
    seen: set[str] = set()
    for entity in entities:
        key = entity.normalized or entity.text.lower()
        if entity.label != "DIAGNOSIS" or key not in ICD10_MAP or key in seen:
            continue
        code, description = ICD10_MAP[key]
        suggestions.append(
            ICD10Suggestion(
                code=code,
                description=description,
                evidence=entity.text,
                confidence=round(min(entity.confidence, 0.88), 3),
            )
        )
        seen.add(key)
    return suggestions

