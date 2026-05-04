from __future__ import annotations

import re


SECTION_HEADER = re.compile(
    r"^(chief complaint|history|assessment|plan|medications|diagnosis|procedure|findings|impression)\s*:\s*$",
    re.IGNORECASE,
)


def split_sections(text: str) -> dict[str, str]:
    """Split a clinical note into simple heading-based sections."""
    sections: dict[str, list[str]] = {"note": []}
    current = "note"

    for raw_line in text.splitlines():
        line = raw_line.strip()
        match = SECTION_HEADER.match(line)
        if match:
            current = match.group(1).lower().replace(" ", "_")
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(raw_line)

    return {
        section: "\n".join(lines).strip()
        for section, lines in sections.items()
        if "\n".join(lines).strip()
    }

