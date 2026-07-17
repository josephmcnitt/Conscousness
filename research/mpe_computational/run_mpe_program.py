#!/usr/bin/env python3
"""
MPE computational phenomenology entry script.

Run: python research/mpe_computational/run_mpe_program.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.mpe_computational.empirical.regime_lab import run_regime_lab
from research.mpe_computational.empirical.transition_lab import run_transition_lab

SUMMARY_PATH = Path(__file__).resolve().parent / "empirical" / "mpe_program_summary.json"


def main(seed: int = 42) -> dict:
    print("=" * 72)
    print("MPE Computational Phenomenology")
    print("4-level parametric-depth simulator (Subproject 3 architecture)")
    print("Label: simulation - not empirical confirmation of MPE phenomenology")
    print("Firewall: no consciousness-field / substrate ontology claims")
    print("=" * 72)

    regime = run_regime_lab(seed=seed)
    transition = run_transition_lab(seed=seed)

    rollup = {}
    rollup.update(regime["predictions"])
    rollup.update(transition["predictions"])
    # MP8: explicit non-claim
    ontology_claims_asserted = False
    rollup["MP8_no_ontology_claim"] = not ontology_claims_asserted

    n_pass = sum(1 for v in rollup.values() if v)
    n_total = len(rollup)

    print("\nPrediction rollup")
    print("-" * 40)
    for k, v in rollup.items():
        print(f"  {k:<42} {v}")

    summary = {
        "program": "mpe_computational_phenomenology",
        "label": "simulation — not empirical confirmation of MPE phenomenology",
        "seed": seed,
        "ontology_claims_asserted": ontology_claims_asserted,
        "disclaimer": (
            "Architecture-faithful toy NumPy model of MPE Project Subproject 3. "
            "Not an official MPE Project model. Not a prize submission. "
            "Does not assert a consciousness field or physical substrate."
        ),
        "prediction_rollup": rollup,
        "mp_pass_count": n_pass,
        "mp_total": n_total,
        "lab_paths": {
            "regime": str(
                Path(__file__).resolve().parent / "empirical" / "regime_lab_results.json"
            ),
            "transition": str(
                Path(__file__).resolve().parent
                / "empirical"
                / "transition_lab_results.json"
            ),
        },
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\n  MP pass: {n_pass}/{n_total}")
    print(f"Summary written: {SUMMARY_PATH}")
    return summary


if __name__ == "__main__":
    main()
