from __future__ import annotations

from .keywords import extract_keywords


def build_word_cloud_data(text: str, *, limit: int = 30) -> list[dict[str, int | str]]:
    return extract_keywords(text, limit=limit)

