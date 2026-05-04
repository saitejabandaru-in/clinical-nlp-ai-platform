from __future__ import annotations

from collections import Counter

from .tokenizer import tokenize


STOPWORDS = {
    "the", "and", "with", "for", "from", "this", "that", "patient", "notes", "note",
    "was", "were", "has", "have", "had", "are", "is", "to", "of", "in", "on", "at",
    "name", "mrn", "date",
}


def extract_keywords(text: str, *, limit: int = 12) -> list[dict[str, int | str]]:
    tokens = [token for token in tokenize(text) if len(token) > 2 and token not in STOPWORDS]
    counts = Counter(tokens)
    return [{"term": term, "score": count} for term, count in counts.most_common(limit)]
