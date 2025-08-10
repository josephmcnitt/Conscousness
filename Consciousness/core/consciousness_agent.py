from __future__ import annotations

import time
from dataclasses import asdict
from typing import Dict, List

from .deep_listener import DeepListener
from .readiness_assessor import ReadinessAssessor
from .recursive_generator import RecursiveGenerator, GenerationStrategy
from .consciousness_evolution import ConsciousnessEvolution, RewardEvaluator
from .memory import LocalMemoryStore, MemoryRecord


class ConsciousnessAgent:
    def __init__(self) -> None:
        self.listener = DeepListener()
        self.assessor = ReadinessAssessor()
        self.generator = RecursiveGenerator()
        self.reward_eval = RewardEvaluator()
        self.evolution = ConsciousnessEvolution(self.reward_eval)
        self.memory = LocalMemoryStore()
        self.current_strategy = GenerationStrategy()

    def run_cycle(self, prompt: str) -> Dict[str, any]:
        stimulus = self.listener.preprocess(prompt)
        avg = self.memory.average_recent_rewards(n=10)
        decision = self.assessor.assess(stimulus, recent_average_correctness=avg.get("correctness"))
        if not decision.proceed:
            return {
                "proceed": False,
                "reason": decision.reason,
                "response": "",
                "plan_steps": [],
                "scores": {},
                "strategy": asdict(self.current_strategy),
            }

        result = self.generator.generate(
            prompt=prompt,
            stimulus=stimulus,
            strategy=self.current_strategy,
            memory=self.memory,
            depth=1,
        )

        scores = self.reward_eval.evaluate(prompt=prompt, response=result.text, plan_steps=result.plan_steps, stimulus=stimulus)
        # Update strategy based on rewards
        new_strategy_dict = self.evolution.update_strategy(scores, asdict(self.current_strategy))
        self.current_strategy = GenerationStrategy(**new_strategy_dict)

        # Persist memory
        rec = MemoryRecord(
            timestamp=time.time(),
            prompt=prompt,
            response=result.text,
            rewards={
                "correctness": scores.correctness,
                "efficiency": scores.efficiency,
                "creativity": scores.creativity,
                "coherence": scores.coherence,
                "overall": scores.overall,
            },
            strategy=new_strategy_dict,
        )
        self.memory.append(rec)

        return {
            "proceed": True,
            "reason": decision.reason,
            "response": result.text,
            "plan_steps": result.plan_steps,
            "scores": asdict(scores),
            "traces": result.traces,
            "strategy": asdict(self.current_strategy),
        }