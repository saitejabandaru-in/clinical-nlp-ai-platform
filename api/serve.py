from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from clinical_nlp_ai_platform import analyze_note

app = FastAPI(
    title="Clinical NLP AI Platform",
    description="API for de-identification, clinical entity extraction, sentiment, keywords, and ICD-10 suggestions.",
    version="0.1.0",
)


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Clinical note text to analyze.")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest) -> dict[str, object]:
    return analyze_note(request.text).to_dict()

