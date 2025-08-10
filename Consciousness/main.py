from __future__ import annotations

import argparse
import json

from .core.consciousness_agent import ConsciousnessAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Consciousness agent locally")
    parser.add_argument("prompt", nargs="?", default="Design a lightweight reward system and a recursive reasoning loop.", help="Prompt to send to the agent")
    args = parser.parse_args()

    agent = ConsciousnessAgent()
    result = agent.run_cycle(args.prompt)

    print("--- Response ---")
    print(result["response"])
    print("\n--- Plan ---")
    for i, step in enumerate(result["plan_steps"], 1):
        print(f"{i}. {step}")
    print("\n--- Scores ---")
    print(json.dumps(result["scores"], indent=2))
    print("\n--- Strategy ---")
    print(json.dumps(result["strategy"], indent=2))
    if result.get("traces"):
        print("\n--- Traces ---")
        for t in result["traces"][:10]:
            print(f"* {t}")


if __name__ == "__main__":
    main()