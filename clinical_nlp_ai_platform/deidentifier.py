from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Redaction:
    label: str
    start: int
    end: int
    placeholder: str


PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("MRN", re.compile(r"\b(?:MRN|Medical Record Number)[:#\s-]*([A-Z0-9-]{5,})\b", re.IGNORECASE)),
    ("PHONE", re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b")),
    ("EMAIL", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
    ("DATE", re.compile(r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})\b", re.IGNORECASE)),
    ("NAME", re.compile(r"\b(?:Patient|Name)[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})\b")),
)


def deidentify(text: str) -> tuple[str, list[Redaction]]:
    """Replace common PHI patterns with deterministic placeholders."""
    redactions: list[Redaction] = []
    replacements: list[tuple[int, int, str, Redaction]] = []

    for label, pattern in PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.span(1) if match.lastindex else match.span()
            placeholder = f"[{label}]"
            redaction = Redaction(label=label, start=start, end=end, placeholder=placeholder)
            replacements.append((start, end, placeholder, redaction))

    replacements.sort(key=lambda item: item[0])
    filtered: list[tuple[int, int, str, Redaction]] = []
    last_end = -1
    for replacement in replacements:
        if replacement[0] >= last_end:
            filtered.append(replacement)
            last_end = replacement[1]

    output_parts: list[str] = []
    cursor = 0
    for start, end, placeholder, redaction in filtered:
        output_parts.append(text[cursor:start])
        output_parts.append(placeholder)
        redactions.append(redaction)
        cursor = end
    output_parts.append(text[cursor:])

    return "".join(output_parts), redactions
