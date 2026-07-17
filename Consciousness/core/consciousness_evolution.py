from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List

from .deep_listener import PreprocessedStimulus


@dataclass
class RewardConfig:
    weight_correctness: float = 0.35
    weight_efficiency: float = 0.25
    weight_creativity: float = 0.20
    weight_coherence: float = 0.20


@dataclass
class RewardScores:
    correctness: float
    efficiency: float
    creativity: float
    coherence: float
    overall: float


class RewardEvaluator:
    """Lightweight multi-dimensional reward system.

    - No external APIs; purely heuristic and local
    - Returns individual scores and an overall weighted score in [0, 1]
    """

    def __init__(self, config: RewardConfig | None = None) -> None:
        self.config = config or RewardConfig()

    @staticmethod
    def _safe_div(a: float, b: float) -> float:
        return a / b if b != 0 else 0.0

    def _tokenize(self, text: str) -> List[str]:
        return [t.lower() for t in text.split() if t]

    def _sentences(self, text: str) -> List[str]:
        # Simple sentence split
        parts: List[str] = []
        buf = []
        for ch in text:
            buf.append(ch)
            if ch in ".!?":
                parts.append("".join(buf).strip())
                buf = []
        if buf:
            parts.append("".join(buf).strip())
        return [p for p in parts if p]

    def _correctness(self, prompt: str, response: str, plan_steps: List[str], stimulus: PreprocessedStimulus) -> float:
        if not response.strip():
            return 0.0
        tokens_resp = set(self._tokenize(response))
        # Coverage of plan keywords
        if plan_steps:
            coverage_hits = 0
            for step in plan_steps:
                step_tokens = set(self._tokenize(step))
                if step_tokens & tokens_resp:
                    coverage_hits += 1
            coverage = self._safe_div(coverage_hits, len(plan_steps))
        else:
            # Fallback: overlap with stimulus keywords
            overlap = len(set(stimulus.keywords) & tokens_resp)
            coverage = min(1.0, overlap / max(1, len(set(stimulus.keywords))))
        # Answer presence heuristic: contains concrete verbs/numbers
        has_concrete = any(ch.isdigit() for ch in response) or any(w in tokens_resp for w in {"use", "build", "do", "code", "steps", "implement", "because"})
        return 0.9 * coverage + 0.1 * (1.0 if has_concrete else 0.0)

    def _efficiency(self, prompt: str, response: str, plan_steps: List[str], stimulus: PreprocessedStimulus) -> float:
        # Target length scales with complexity and plan size
        target_len = 40 * max(1, len(plan_steps))
        prompt_len = len(prompt)
        base_target = max(target_len, int(0.6 * max(50, prompt_len)))
        resp_len = len(response)
        ratio = self._safe_div(resp_len, base_target)
        # Ideal ratio around 1.0; penalize deviations
        efficiency = math.exp(-abs(ratio - 1.0))  # ~1.0 near perfect, decays smoothly
        # Encourage lists/checklists for structure when complex
        if len(plan_steps) >= 3 and ("- " in response or "\n1" in response):
            efficiency = min(1.0, efficiency + 0.05)
        return float(max(0.0, min(1.0, efficiency)))

    def _creativity(self, prompt: str, response: str) -> float:
        tok_p = set(self._tokenize(prompt))
        tok_r = self._tokenize(response)
        if not tok_r:
            return 0.0
        uniq_ratio = len(set(tok_r)) / len(tok_r)
        novelty = len(set(tok_r) - tok_p) / max(1, len(set(tok_r)))
        bonus = 0.05 if any(w in tok_r for w in ["example", "analogy", "metaphor"]) else 0.0
        return float(max(0.0, min(1.0, 0.6 * uniq_ratio + 0.4 * novelty + bonus)))

    def _coherence(self, response: str) -> float:
        sents = self._sentences(response)
        if not sents:
            return 0.0
        lengths = [len(s.split()) for s in sents]
        avg_len = sum(lengths) / len(lengths)
        # Prefer average sentence length between ~8 and 28 words
        within = 1.0 - min(1.0, abs(avg_len - 18.0) / 18.0)
        # Transitional words bonus
        tokens = set(self._tokenize(response))
        connectors = {"therefore", "however", "because", "then", "thus", "first", "second", "finally"}
        connector_bonus = 0.05 if tokens & connectors else 0.0
        return float(max(0.0, min(1.0, within + connector_bonus)))

    def evaluate(self, prompt: str, response: str, plan_steps: List[str], stimulus: PreprocessedStimulus) -> RewardScores:
        correctness = self._correctness(prompt, response, plan_steps, stimulus)
        efficiency = self._efficiency(prompt, response, plan_steps, stimulus)
        creativity = self._creativity(prompt, response)
        coherence = self._coherence(response)
        cfg = self.config
        overall = (
            cfg.weight_correctness * correctness
            + cfg.weight_efficiency * efficiency
            + cfg.weight_creativity * creativity
            + cfg.weight_coherence * coherence
        )
        return RewardScores(
            correctness=float(correctness),
            efficiency=float(efficiency),
            creativity=float(creativity),
            coherence=float(coherence),
            overall=float(max(0.0, min(1.0, overall))),
        )


class ConsciousnessEvolution:
    """Adjusts behaviour based on feedback (rewards)."""

    def __init__(self, reward_evaluator: RewardEvaluator | None = None) -> None:
        self.reward_evaluator = reward_evaluator or RewardEvaluator()

    def update_strategy(self, scores: RewardScores, strategy: Dict[str, any]) -> Dict[str, any]:
        # Copy
        new_strategy = dict(strategy)
        # If correctness is low, increase depth; if coherence low, reduce branching; if efficiency low, prefer concise
        if scores.correctness < 0.5:
            new_strategy["max_depth"] = min(4, int(new_strategy.get("max_depth", 2)) + 1)
        if scores.coherence < 0.5:
            new_strategy["max_children_per_node"] = max(1, int(new_strategy.get("max_children_per_node", 3)) - 1)
        if scores.efficiency < 0.5:
            new_strategy["prefer_concise"] = True
        if scores.creativity < 0.4:
            # Allow a bit more branching to explore options
            new_strategy["max_children_per_node"] = min(5, int(new_strategy.get("max_children_per_node", 3)) + 1)
        return new_strategy
