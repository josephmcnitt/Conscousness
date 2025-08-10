import enum
import math
import re
from dataclasses import dataclass
from typing import Dict, Optional, Any


class RewardDimensions(str, enum.Enum):
    """Enumeration of reward dimensions.

    Using ``str`` as base class allows JSON serialization out of the box.
    """

    CORRECTNESS = "correctness"
    EFFICIENCY = "efficiency"
    CREATIVITY = "creativity"
    COHERENCE = "coherence"


@dataclass
class RewardScores:
    """Container holding multi-dimensional reward scores in ``[0, 1]`` range."""

    correctness: float
    efficiency: float
    creativity: float
    coherence: float

    def as_dict(self) -> Dict[str, float]:
        return {
            RewardDimensions.CORRECTNESS: self.correctness,
            RewardDimensions.EFFICIENCY: self.efficiency,
            RewardDimensions.CREATIVITY: self.creativity,
            RewardDimensions.COHERENCE: self.coherence,
        }

    def overall(self, weights: Optional[Dict[str, float]] = None) -> float:
        """Weighted sum of individual scores.

        Args:
            weights: Optional custom weight mapping for each dimension. If not
                provided every dimension is weighted equally.
        """
        weights = weights or {
            RewardDimensions.CORRECTNESS: 0.25,
            RewardDimensions.EFFICIENCY: 0.25,
            RewardDimensions.CREATIVITY: 0.25,
            RewardDimensions.COHERENCE: 0.25,
        }
        return sum(self.as_dict()[dim] * weight for dim, weight in weights.items())


class RewardEvaluator:
    """Light-weight heuristic evaluator for agent responses.

    The evaluator purposefully avoids expensive external calls (LLM, web APIs)
    so it can run entirely on modest local hardware.
    """

    _TOKEN_RE = re.compile(r"[A-Za-z0-9']+")

    def __init__(self, *, max_length: int = 200):
        # Max length (in tokens) considered before efficiency score bottoms out.
        self.max_length = max_length

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------
    def evaluate(self, response: str, *, context: Optional[Dict[str, Any]] = None) -> RewardScores:
        """Evaluate *response* producing ``RewardScores``.

        Args:
            response: The generated text.
            context: Optional context dict. Supported keys:
                * ``expected_answer`` – reference answer string to compare against.
                * ``prompt`` – original prompt/question.

        Returns:
            RewardScores
        """
        context = context or {}
        tokens = self._tokenize(response)
        token_count = len(tokens)

        # 1) Correctness
        correctness = self._score_correctness(tokens, context.get("expected_answer"))

        # 2) Efficiency (brevity without sacrificing completeness)
        efficiency = self._score_efficiency(token_count)

        # 3) Creativity (lexical diversity)
        creativity = self._score_creativity(tokens)

        # 4) Coherence (simple sentence-level heuristic)
        coherence = self._score_coherence(response)

        return RewardScores(
            correctness=correctness,
            efficiency=efficiency,
            creativity=creativity,
            coherence=coherence,
        )

    # ------------------------------------------------------------------
    # Individual dimension scorers (private)
    # ------------------------------------------------------------------
    def _tokenize(self, text: str):
        return [t.lower() for t in self._TOKEN_RE.findall(text)]

    def _score_correctness(self, response_tokens, expected_answer: Optional[str]):
        if not expected_answer:
            # Without a reference the evaluator assumes partial correctness.
            return 0.5
        expected_tokens = set(self._tokenize(expected_answer))
        if not expected_tokens:
            return 0.5
        overlap = len([t for t in response_tokens if t in expected_tokens])
        return overlap / max(len(expected_tokens), 1)

    def _score_efficiency(self, token_count: int):
        # Full score for <=50 tokens, linearly decreasing to 0 at max_length.
        if token_count <= 50:
            return 1.0
        elif token_count >= self.max_length:
            return 0.0
        # Linear interpolation between 50 and max_length.
        return 1.0 - (token_count - 50) / (self.max_length - 50)

    def _score_creativity(self, tokens):
        unique = len(set(tokens))
        total = len(tokens)
        if total == 0:
            return 0.0
        # Diversity ratio scaled to [0,1]
        return unique / total

    def _score_coherence(self, text: str):
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]
        if not sentences:
            return 0.0
        # Basic heuristic: proportion of sentences that have 4+ words.
        coherent = len([s for s in sentences if len(s.split()) >= 4])
        return coherent / len(sentences)