"""Core orchestrator agent combining listening, generation, assessment and evolution capabilities."""

from __future__ import annotations

from typing import Any

from .deep_listener import DeepListener
from .readiness_assessor import ReadinessAssessor
from .recursive_generator import RecursiveGenerator
from .consciousness_evolution import ConsciousnessEvolution


class ConsciousnessAgent:
    """High-level agent that drives the overall reasoning loop."""

    def __init__(
        self,
        listener: DeepListener | None = None,
        assessor: ReadinessAssessor | None = None,
        generator: RecursiveGenerator | None = None,
        evolution: ConsciousnessEvolution | None = None,
    ) -> None:
        self.listener = listener or DeepListener()
        self.assessor = assessor or ReadinessAssessor()
        self.generator = generator or RecursiveGenerator()
        self.evolution = evolution or ConsciousnessEvolution()

    # ---------------------------------------------------------------------
    # Public helpers
    # ---------------------------------------------------------------------
    def think(self, prompt: str, *args: Any, **kwargs: Any) -> str:
        """Primary reasoning entry-point used by external callers.

        Parameters
        ----------
        prompt: str
            The initial instruction or question.
        *args, **kwargs:
            Additional parameters forwarded to the generator.
        """

        if not self.assessor.ready():
            return "Agent is not ready yet."

        # Listen & possibly transform the prompt
        perceived_prompt = self.listener.listen(prompt)

        # Generate a response (potentially recursive)
        response = self.generator.generate(perceived_prompt, *args, **kwargs)

        # Allow the system to evolve based on the output
        self.evolution.adapt(response)

        return response