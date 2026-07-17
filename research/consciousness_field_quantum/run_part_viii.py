#!/usr/bin/env python3
"""
Part VIII entry script: Consciousness Field × Quantum Hard Problems.

Runs measurement, preferred-basis, Born, entanglement labs, Metzinger bridge
labs, and the physics-weighted Track U vs Track C scoreboard.

Run: python research/consciousness_field_quantum/run_part_viii.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.empirical.track_comparison_scoreboard import (
    run_scoreboard,
)

SUMMARY_PATH = Path(__file__).resolve().parent / "empirical" / "part_viii_summary.json"


def main(seed: int = 42) -> dict:
    print("=" * 72)
    print("Part VIII: Consciousness Field x Quantum Hard Problems")
    print("Track U (unitary/decoherence) vs Track C (collapse-clumping)")
    print("Metzinger bridge: MPE -> PSM -> PMIR awareness-matter sector")
    print("Label: simulation - not empirical QM confirmation")
    print("=" * 72)

    board = run_scoreboard(seed=seed)
    comp = board["comparison"]
    rollup = board["prediction_rollup"]
    bridge = board.get("metzinger_bridge", {})

    print("\nPrediction rollup")
    print("-" * 40)
    for k, v in rollup.items():
        print(f"  {k:<22} {v}")

    print("\nScoreboard")
    print("-" * 40)
    print(f"  Track U total: {comp['track_U_total']:.4f}")
    print(f"  Track C total: {comp['track_C_total']:.4f}")
    print(f"  Winner:        {comp['winner']}")
    if bridge:
        print(
            f"  Metzinger M*:  {bridge.get('m_pass_count', 0)}/{bridge.get('m_total', 8)}"
        )

    summary = {
        "program": "part_viii_consciousness_field_quantum",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "winner": comp["winner"],
        "track_U_total": comp["track_U_total"],
        "track_C_total": comp["track_C_total"],
        "prediction_rollup": rollup,
        "metzinger_bridge": bridge,
        "scoreboard_path": str(
            Path(__file__).resolve().parent / "empirical" / "track_comparison_scoreboard.json"
        ),
        "caveat": board["caveat"],
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written: {SUMMARY_PATH}")
    return summary


if __name__ == "__main__":
    main()
