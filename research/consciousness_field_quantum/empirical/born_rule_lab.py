"""
Born rule lab (Q2): Track U sampling vs Track C λ sweep.

Run: python research/consciousness_field_quantum/empirical/born_rule_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.equations.born_rule import (
    born_fit_score,
    born_probabilities,
    born_total_variation,
    empirical_frequencies,
    sample_outcomes,
)
from research.consciousness_field_quantum.equations.clumping import ClumpState
from research.consciousness_field_quantum.equations.collapse_csl import scan_lambda_born_fit
from research.consciousness_field_quantum.equations.density_matrix import qubit_bloch_dm

OUTPUT_PATH = Path(__file__).resolve().parent / "born_rule_lab_results.json"


def run_born_rule_lab(seed: int = 42, n_samples: int = 5000) -> dict:
    rng = np.random.default_rng(seed)
    # Unequal superposition so Born is nontrivial
    theta = 2 * np.arccos(np.sqrt(0.7))
    rho0 = qubit_bloch_dm(theta)
    p_born = born_probabilities(rho0)
    clump = ClumpState(amplitude=1.0, coherence_length=1.0, mode_stability=0.9)

    # Track U: sample directly from Born (unitary/decoherence does not change diagonal
    # populations under pure dephasing)
    samples_u = sample_outcomes(p_born, n_samples, rng)
    p_emp_u = empirical_frequencies(samples_u, len(p_born))
    tv_u = born_total_variation(p_emp_u, p_born)
    score_u = born_fit_score(p_emp_u, p_born)

    lambda0_grid = np.array([0.001, 0.01, 0.05, 0.2, 1.0, 5.0])
    scan = scan_lambda_born_fit(
        rho0, clump, p_born, lambda0_grid, n_samples=n_samples, steps=50, seed=seed
    )
    tvs = [row["tv_born"] for row in scan]
    best_i = int(np.argmin(tvs))
    best = scan[best_i]
    tol = 0.08
    in_band = [row for row in scan if row["tv_born"] <= tol]
    q2_pass = best["tv_born"] <= tol and (
        max(tvs) - min(tvs) > 0.002 or len(in_band) < len(scan)
    )

    output = {
        "experiment": "born_rule_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "p_born": p_born.tolist(),
        "track_u": {
            "p_emp": p_emp_u.tolist(),
            "tv_born": tv_u,
            "born_fit_score": score_u,
        },
        "track_c_lambda_scan": scan,
        "track_c_best": best,
        "predictions": {
            "Q2_track_c_born_band": bool(q2_pass),
            "Q2_n_lambda_in_band": len(in_band),
            "track_u_born_ok": tv_u <= tol,
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Born rule lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Born Rule Lab")
    print("=" * 60)
    run_born_rule_lab()
