from __future__ import annotations

from clinical_nlp_ai_platform import analyze_note
from clinical_nlp_ai_platform.deidentifier import deidentify


SAMPLE_NOTE = """
Patient: Jane Smith
MRN: Z999991
Date: 04/12/2026

Assessment:
Patient has diabetes and hypertension. Chest x-ray suggests pneumonia.
Metformin is tolerated and fever is worsening.
"""


def test_deidentifier_redacts_common_phi() -> None:
    redacted, redactions = deidentify("Patient: Jane Smith MRN: Z999991 phone 555-123-4567")

    assert "Jane Smith" not in redacted
    assert "Z999991" not in redacted
    assert "555-123-4567" not in redacted
    assert {item.label for item in redactions} >= {"NAME", "MRN", "PHONE"}


def test_pipeline_extracts_entities_codes_and_sections() -> None:
    result = analyze_note(SAMPLE_NOTE)
    entity_labels = {entity.label for entity in result.entities}
    codes = {suggestion.code for suggestion in result.icd10_suggestions}

    assert "assessment" in result.sections
    assert "DIAGNOSIS" in entity_labels
    assert "PROCEDURE" in entity_labels
    assert {"E11.9", "I10", "J18.9"} <= codes
    assert result.sentiment.label in {"positive", "negative", "neutral"}
    assert result.keywords

