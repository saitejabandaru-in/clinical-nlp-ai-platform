from __future__ import annotations

import re


TOKEN_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9-]*")


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_PATTERN.finditer(text)]


def sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]

