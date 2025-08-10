from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .deep_listener import PreprocessedStimulus


@dataclass
class ReadinessDecision:
    proceed: bool
    reason: str


class ReadinessAssessor:
    """Decides whether the agent should proceed.

    Currently simple: proceed unless the input is empty.
    """

    def assess(self, stimulus: PreprocessedStimulus, recent_average_correctness: Optional[float] = None) -> ReadinessDecision:
        if not stimulus.raw_text:
            return ReadinessDecision(proceed=False, reason="No input provided")
        # If performance has been consistently poor, we could switch strategies or ask for clarification.
        if recent_average_correctness is not None and recent_average_correctness < 0.2:
            return ReadinessDecision(proceed=True, reason="Proceed with conservative strategy due to low recent correctness")
        return ReadinessDecision(proceed=True, reason="Input present; proceeding")