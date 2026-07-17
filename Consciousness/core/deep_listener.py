from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Set


STOPWORDS: Set[str] = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "is",
    "are",
    "be",
    "that",
    "this",
    "it",
    "as",
    "by",
    "at",
    "from",
}


@dataclass
class PreprocessedStimulus:
    raw_text: str
    tokens: List[str]
    sentences: List[str]
    keywords: List[str]
    complexity_score: float


class DeepListener:
    """Captures and pre-processes input stimuli.

    - Tokenizes text, extracts keywords, estimates complexity
    - Lightweight; avoids any external dependencies
    """

    sentence_splitter = re.compile(r"(?<=[.!?])\s+")
    token_splitter = re.compile(r"[^A-Za-z0-9_]+")

    def preprocess(self, text: str) -> PreprocessedStimulus:
        raw = text.strip()
        sentences = [s.strip() for s in self.sentence_splitter.split(raw) if s.strip()] if raw else []
        tokens = [t.lower() for t in self.token_splitter.split(raw) if t]
        keywords = [t for t in tokens if len(t) >= 4 and t not in STOPWORDS]

        # Heuristic complexity: more sentences/questions/keywords => more complex
        num_questions = sum(1 for s in sentences if s.endswith("?"))
        complexity = 0.1 * len(sentences) + 0.05 * len(tokens) + 0.2 * num_questions + 0.1 * len(set(keywords))

        return PreprocessedStimulus(
            raw_text=raw,
            tokens=tokens,
            sentences=sentences,
            keywords=keywords,
            complexity_score=float(min(1.0, complexity / 50.0)),
        )
