from __future__ import annotations

import argparse
import json
import time

from .core.consciousness_agent import ConsciousnessAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Consciousness agent locally")
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Design a lightweight reward system and a recursive reasoning loop.",
        help="Prompt to send to the agent",
    )
    parser.add_argument(
        "--continuous",
        action="store_true",
        help="Run continuously, repeating cycles until stopped or reaching --max-cycles",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=3.0,
        help="Seconds to sleep between cycles when running in --continuous mode",
    )
    parser.add_argument(
        "--max-cycles",
        type=int,
        default=0,
        help="Maximum number of cycles to run in --continuous mode (0 means infinite)",
    )
    args = parser.parse_args()

    agent = ConsciousnessAgent()

    def _print_result(result: dict) -> None:
        print("--- Response ---")
        print(result.get("response", ""))
        print("\n--- Plan ---")
        for i, step in enumerate(result.get("plan_steps", []), 1):
            print(f"{i}. {step}")
        print("\n--- Scores ---")
        print(json.dumps(result.get("scores", {}), indent=2))
        print("\n--- Strategy ---")
        print(json.dumps(result.get("strategy", {}), indent=2))
        traces = result.get("traces") or []
        if traces:
            print("\n--- Traces ---")
            for t in traces[:10]:
                print(f"* {t}")

    if args.continuous:
        cycle = 0
        try:
            while True:
                cycle += 1
                print(f"\n=== Cycle {cycle} ===")
                result = agent.run_cycle(args.prompt)
                _print_result(result)
                if args.max_cycles and cycle >= args.max_cycles:
                    break
                time.sleep(max(0.0, float(args.interval)))
        except KeyboardInterrupt:
            print("\nStopped continuous mode.")
    else:
        result = agent.run_cycle(args.prompt)
        _print_result(result)


if __name__ == "__main__":
    main()