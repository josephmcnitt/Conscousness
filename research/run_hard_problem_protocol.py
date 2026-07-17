#!/usr/bin/env python3
"""
Part VI entry script: Hard Problem Protocol (adversarial triangulation).

Runs Parts I–V baseline plus dissociation hunt, access collapse, combination lab.

Run: python research/run_hard_problem_protocol.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.access_collapse_model import run_access_collapse_experiment
from research.empirical.combination_realization_lab import run_combination_realization_lab
from research.empirical.dissociation_hunt import run_dissociation_hunt


def _run_parts_baseline() -> dict | None:
    """Run Parts I–V unified program as subprocess; return summary if available."""
    script = ROOT / "research" / "run_consciousness_program.py"
    print("[HPP] Running Parts I–V baseline...")
    subprocess.run([sys.executable, str(script)], check=False, cwd=str(ROOT))
    summary_path = ROOT / "research" / "empirical" / "consciousness_program_summary.json"
    if summary_path.exists():
        return json.loads(summary_path.read_text(encoding="utf-8"))
    return None


def _track_wins(hunt: dict, collapse: dict, combo: dict) -> dict:
    wins = {
        "panpsychist_close": 0,
        "illusionist_dissolve": 0,
        "structural_physicalism": 0,
    }
    for sc in hunt.get("scenarios", []):
        scores = sc.get("track_scores", {})
        if scores:
            winner = max(
                (k for k in wins if k in scores),
                key=lambda k: scores[k],
            )
            wins[winner] += 1

    if collapse.get("interpretation", {}).get("p18_analog"):
        wins["panpsychist_close"] += 1
    elif collapse.get("interpretation", {}).get("illusionist_wins_count", 0) >= 3:
        wins["illusionist_dissolve"] += 1

    if combo.get("interpretation", {}).get("p22_analog"):
        wins["panpsychist_close"] += 1

    standings = {k: "open" for k in wins}
    leader = max(wins, key=wins.get)
    if wins[leader] >= 3:
        standings[leader] = "leading"

    return {"wins": wins, "standings": standings}


def run_hpp_experiments(include_baseline: bool = True) -> dict:
    """Run HPP adversarial experiments; optionally skip Parts I–V baseline."""
    baseline = None
    if include_baseline:
        baseline = _run_parts_baseline()

    print("\n[Part VI] Dissociation hunt (P18–P22 scenarios)")
    hunt = run_dissociation_hunt()

    print("\n[Part VI] Access-only collapse model (P18)")
    collapse = run_access_collapse_experiment()

    print("\n[Part VI] Combination realization lab (P22)")
    combo = run_combination_realization_lab()

    scoreboard = _track_wins(hunt, collapse, combo)

    print("\n" + "=" * 76)
    print("HPP Track Scoreboard (in-silico)")
    print("=" * 76)
    for track, wins in scoreboard["wins"].items():
        print(f"  {track}: {wins} scenario wins  [{scoreboard['standings'][track]}]")

    analog_flags = {
        "P18": collapse.get("interpretation", {}).get("p18_analog", False),
        "P22": combo.get("interpretation", {}).get("p22_analog", False),
        "highest_adversarial": hunt.get("interpretation", {}).get("highest_adversarial_value"),
    }
    print(f"\n  P18 analog: {'PASS' if analog_flags['P18'] else 'FAIL'}")
    print(f"  P22 analog: {'PASS' if analog_flags['P22'] else 'FAIL'}")
    print(f"  Highest adversarial scenario: {analog_flags['highest_adversarial']}")

    summary = {
        "program": "Hard Problem Protocol Part VI",
        "disclaimer": "Tournament simulation — hard problem NOT solved",
        "parts_i_v_baseline": baseline is not None,
        "dissociation_hunt": hunt.get("interpretation"),
        "access_collapse": collapse.get("interpretation"),
        "combination_lab": combo.get("interpretation"),
        "track_scoreboard": scoreboard,
        "analog_flags": analog_flags,
        "strongest_honest_claim": (
            "We cannot derive qualia from physics yet — but rival theories "
            "now fight on shared predictions with explicit loss conditions."
        ),
    }

    out_path = ROOT / "research" / "empirical" / "hard_problem_protocol_summary.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written: {out_path}")
    return summary


def main() -> None:
    print("=" * 76)
    print("Part VI: Hard Problem Protocol — Adversarial Triangulation")
    print("=" * 76)
    print("DISCLAIMER: Tournament simulation — NOT hard problem solved.\n")
    run_hpp_experiments(include_baseline=True)


if __name__ == "__main__":
    main()
