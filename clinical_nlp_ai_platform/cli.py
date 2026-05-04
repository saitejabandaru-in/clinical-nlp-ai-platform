from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import analyze_note


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze a clinical note with the NLP pipeline.")
    parser.add_argument("--input", type=Path, help="Path to a clinical note text file.")
    parser.add_argument("--text", help="Clinical note text to analyze directly.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.input:
        text = args.input.read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        raise SystemExit("Provide --input or --text")

    result = analyze_note(text)
    indent = 2 if args.pretty else None
    print(json.dumps(result.to_dict(), indent=indent))
    return 0

