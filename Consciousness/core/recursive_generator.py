from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from .deep_listener import PreprocessedStimulus
from .memory import LocalMemoryStore


@dataclass
class GenerationStrategy:
    max_depth: int = 2
    max_children_per_node: int = 3
    prefer_concise: bool = True
    use_memory: bool = True


@dataclass
class GenerationResult:
    text: str
    plan_steps: List[str]
    traces: List[str] = field(default_factory=list)


class RecursiveGenerator:
    """Generates content with simple reasoning and recursion.

    - Decomposes prompt into plan steps using heuristics
    - Recursively generates sub-answers and synthesizes a coherent response
    - Optionally leverages recent similar memory for hints
    """

    GENERIC_COMPONENTS = [
        "Input processing",
        "Reasoning and decomposition",
        "Execution/generation",
        "Evaluation and feedback",
        "Memory and context",
        "Synthesis and reporting",
    ]

    def _heuristic_decompose(self, prompt: str, stimulus: PreprocessedStimulus) -> List[str]:
        tokens = stimulus.tokens
        steps: List[str] = []
        if not tokens:
            return steps

        # Simple heuristics for task-type detection
        if any(q in tokens for q in ["how", "why", "what", "explain", "design", "implement"]):
            steps = [
                "Clarify the objective and constraints",
                "Break the problem into smaller components",
                "Solve each component",
                "Synthesize the overall solution",
            ]
        elif any(k in tokens for k in ["plan", "steps", "roadmap"]):
            steps = [
                "List key goals",
                "Order the steps by dependency",
                "Identify risks and mitigations",
                "Provide an execution timeline",
            ]
        else:
            steps = [
                "Identify requirements",
                "Enumerate constraints",
                "Propose solution options",
                "Recommend a path forward",
            ]
        return steps

    def _derive_components(self, prompt: str, stimulus: PreprocessedStimulus) -> List[str]:
        kws = set(stimulus.keywords)
        components: List[str] = []
        # Domain-flavored components
        if {"reward", "evaluate", "evaluation", "score"} & kws:
            components.append("Reward evaluation module")
        if {"memory", "context", "history"} & kws:
            components.append("Memory and retrieval module")
        if {"recursive", "reasoning", "decomposition", "plan"} & kws:
            components.append("Recursive planner and generator")
        if {"coherence", "creativity", "efficiency", "correctness"} & kws:
            components.append("Multi-dimensional scoring criteria")
        if not components:
            components = self.GENERIC_COMPONENTS[:]
        # Cap components
        return components[:6]

    def _bullet(self, items: List[str]) -> str:
        return "\n".join(f"- {it}" for it in items)

    def _generate_for_step(self, step: str, prompt: str, stimulus: PreprocessedStimulus, depth: int, strategy: GenerationStrategy, memory: LocalMemoryStore) -> Tuple[str, List[str]]:
        hints: List[str] = []
        hint_text = ""
        if strategy.use_memory:
            similar = memory.find_similar(prompt, k=1)
            for sim, rec in similar:
                if sim > 0.2 and rec.response:
                    hint = f"Prior similar case (sim={sim:.2f}) suggests: {rec.response.splitlines()[0][:160]}"
                    hints.append(hint)
                    hint_text = f"\nHint: {hint}"
                    break

        step_lower = step.lower()
        concise_note = " (concise)" if strategy.prefer_concise else ""

        if "clarify" in step_lower or "identify requirements" in step_lower:
            objectives = [
                "State the primary goal in one sentence",
                "List 3-5 concrete success criteria",
            ]
            constraints = [
                "Run fully local; avoid external APIs",
                "Be lightweight and extensible",
                "Work with heuristic evaluation",
            ]
            if stimulus.keywords:
                objectives.append(f"Incorporate key aspects: {', '.join(stimulus.keywords[:6])}")
            text = (
                f"[depth={depth}] Objectives{concise_note}:\n"
                f"{self._bullet(objectives)}\n\n"
                f"Constraints:{' ' if strategy.prefer_concise else ''}\n{self._bullet(constraints)}"
            )
            return text + hint_text, hints

        if "break the problem" in step_lower or "enumerate constraints" in step_lower or "order the steps" in step_lower:
            comps = self._derive_components(prompt, stimulus)
            rationale = [
                "Decompose by functional responsibility",
                "Limit the number of moving parts",
                "Make components testable in isolation",
            ]
            text = (
                f"[depth={depth}] Components{concise_note}:\n"
                f"{self._bullet([f'{i+1}. {c}' for i, c in enumerate(comps[:max(1, strategy.max_children_per_node)])])}\n\n"
                f"Rationale:{' ' if strategy.prefer_concise else ''}\n{self._bullet(rationale)}"
            )
            return text + hint_text, hints

        if "solve each component" in step_lower or "identify risks" in step_lower or "propose solution" in step_lower:
            comps = self._derive_components(prompt, stimulus)[:max(1, strategy.max_children_per_node)]
            items: List[str] = []
            for c in comps:
                if "reward" in c.lower():
                    items.append("Reward: compute correctness/efficiency/creativity/coherence via local heuristics and weight into overall score")
                elif "memory" in c.lower():
                    items.append("Memory: persist JSONL turns; retrieve by trigram Jaccard similarity for hints and context")
                elif "planner" in c.lower() or "recursive" in c.lower():
                    items.append("Planner: detect task type; create plan steps; recurse with bounded depth and children; synthesize outputs")
                elif "scoring" in c.lower():
                    items.append("Scoring: expose weights; allow per-signal thresholds; keep functions pure and fast")
                else:
                    items.append(f"{c}: implement minimal viable logic first; add knobs and metrics for evolution")
            text = (
                f"[depth={depth}] Solutions{concise_note}:\n"
                f"{self._bullet(items)}"
            )
            return text + hint_text, hints

        if "synthesize" in step_lower or "recommend" in step_lower or "provide an execution timeline" in step_lower:
            synthesis = [
                "Start with reward evaluator to anchor learning",
                "Wire evaluator into evolution to tune strategy",
                "Add memory retrieval to support context and reuse",
                "Iterate: adjust weights, thresholds, and plan depth based on scores",
            ]
            text = (
                f"[depth={depth}] Synthesis{concise_note}:\n"
                f"{self._bullet(synthesis)}\n\n"
                f"Next actions:{' ' if strategy.prefer_concise else ''}\n- Run locally; inspect scores; iterate parameters"
            )
            return text + hint_text, hints

        # Fallback
        text = f"[depth={depth}] {step}:{' Keep it concise.' if strategy.prefer_concise else ''}"
        return text + hint_text, hints

    def _synthesize(self, prompt: str, step_outputs: List[str], depth: int) -> str:
        if not step_outputs:
            return f"[depth={depth}] No content generated."
        synthesis = "\n".join(step_outputs)
        return synthesis

    def generate(self, prompt: str, stimulus: PreprocessedStimulus, strategy: GenerationStrategy, memory: LocalMemoryStore, depth: int = 1) -> GenerationResult:
        plan = self._heuristic_decompose(prompt, stimulus)
        traces: List[str] = [f"Plan at depth {depth}: {plan}"]

        outputs: List[str] = []
        child_count = 0
        for step in plan:
            if child_count >= max(1, strategy.max_children_per_node):
                break
            step_text, hints = self._generate_for_step(step, prompt, stimulus, depth, strategy, memory)
            outputs.append(step_text)
            traces.extend(hints)
            # Recurse on each step if depth allows
            if depth < max(1, strategy.max_depth):
                sub_result = self.generate(f"{prompt} -> {step}", stimulus, strategy, memory, depth=depth + 1)
                outputs.append(sub_result.text)
                traces.extend(sub_result.traces)
            child_count += 1

        combined = self._synthesize(prompt, outputs, depth)
        return GenerationResult(text=combined, plan_steps=plan, traces=traces)
