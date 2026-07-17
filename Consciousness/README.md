# Consciousness – A Recursive AI Agent Ecosystem (Local)

This repository contains a minimal, local, and extensible proof-of-concept that composes lightweight components into a recursive reasoning system. It avoids any external API calls and focuses on rule-based evaluation, simple heuristics, and self-improving feedback.

## Components

| Module | Purpose |
| ------ | ------- |
| `core.deep_listener.DeepListener` | Captures & pre-processes input stimuli. |
| `core.readiness_assessor.ReadinessAssessor` | Decides whether the agent should proceed. |
| `core.recursive_generator.RecursiveGenerator` | Generates (recursive) content via heuristic decomposition. |
| `core.consciousness_evolution.RewardEvaluator` | Multi-dimensional reward system (correctness, efficiency, creativity, coherence). |
| `core.consciousness_evolution.ConsciousnessEvolution` | Adjusts strategy from feedback. |
| `core.memory.LocalMemoryStore` | Simple JSONL memory and similarity retrieval. |
| `core.consciousness_agent.ConsciousnessAgent` | Orchestrates the whole cycle. |

## Quickstart

```bash
python -m Consciousness.main
```

Example output (truncated):

```
--- Response ---
[depth=1] Clarify the objective and constraints:  Keep it concise.
[depth=2] Clarify the objective and constraints:  Keep it concise.
[depth=1] Break the problem into smaller components:  Keep it concise.
[depth=2] Break the problem into smaller components:  Keep it concise.
...

--- Plan ---
1. Clarify the objective and constraints
2. Break the problem into smaller components
3. Solve each component
4. Synthesize the overall solution

--- Scores ---
{
  "correctness": 0.7,
  "efficiency": 0.6,
  "creativity": 0.5,
  "coherence": 0.7,
  "overall": 0.63
}

--- Strategy ---
{
  "max_depth": 2,
  "max_children_per_node": 3,
  "prefer_concise": true,
  "use_memory": true
}
```

## Notes
- Fully local and cost-effective; no cloud APIs.
- Reward system is heuristic-based and easily extensible.
- Memory grows with usage and informs future reasoning.
- Evolution nudges strategy towards higher scores over time.
