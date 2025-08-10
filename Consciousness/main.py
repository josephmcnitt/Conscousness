"""Simple script showcasing the interaction between the ecosystem components."""

from __future__ import annotations

from core import (
    ConsciousnessAgent,
    DeepListener,
    ReadinessAssessor,
    RecursiveGenerator,
    ConsciousnessEvolution,
)


def main() -> None:
    listener = DeepListener()
    assessor = ReadinessAssessor()
    generator = RecursiveGenerator(depth=2)
    evolution = ConsciousnessEvolution()

    agent = ConsciousnessAgent(
        listener=listener,
        assessor=assessor,
        generator=generator,
        evolution=evolution,
    )

    user_prompt = "Hello, consciousness!"
    response = agent.think(user_prompt)
    print("--- Response ---")
    print(response)


if __name__ == "__main__":
    main()