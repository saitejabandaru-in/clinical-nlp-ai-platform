from __future__ import annotations


TOPIC_TERMS: dict[str, set[str]] = {
    "cardiometabolic": {"diabetes", "hypertension", "metformin", "lisinopril", "insulin"},
    "respiratory": {"pneumonia", "asthma", "albuterol", "shortness", "breath", "fever"},
    "diagnostics": {"x-ray", "ct", "scan", "ekg", "imaging", "findings"},
}


def infer_topics(text: str) -> list[dict[str, float | str]]:
    lowered = text.lower()
    scored: list[dict[str, float | str]] = []
    for topic, terms in TOPIC_TERMS.items():
        hits = sum(1 for term in terms if term in lowered)
        if hits:
            scored.append({"topic": topic, "score": round(hits / len(terms), 3)})
    return sorted(scored, key=lambda item: item["score"], reverse=True)

