"""
Measurement lab (Q1, Q5, Q7, Q8): Track U decoherence vs Track C CSL.

Run: python research/consciousness_field_quantum/empirical/measurement_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.equations.clumping import (
    ClumpState,
    definiteness_from_clump,
)
from research.consciousness_field_quantum.equations.collapse_csl import run_csl_trajectory
from research.consciousness_field_quantum.equations.decoherence import (
    amplitude_damping_like_dephasing,
    classicality_score,
    off_diagonal_mean,
)
from research.consciousness_field_quantum.equations.density_matrix import qubit_bloch_dm

OUTPUT_PATH = Path(__file__).resolve().parent / "measurement_lab_results.json"


def _wigner_friend_toy(seed: int = 0) -> dict:
    """
    Q8 stub: friend measures (decoherence), Wigner still assigns coherence
    if he has not coupled — Track U keeps Wigner interference parameter;
    Track C forces friend outcome early → lower Wigner interference proxy.
    """
    rng = np.random.default_rng(seed)
    rho0 = qubit_bloch_dm(np.pi / 2)  # |+⟩
    clump = ClumpState(amplitude=1.2, coherence_length=0.8, mode_stability=0.9)

    # Friend decoheres strongly (Track U record)
    u = amplitude_damping_like_dephasing(rho0, gamma=2.0, steps=40, dt=0.05)
    friend_classical = classicality_score(u["rho_final"])

    # Wigner interference proxy: residual off-diag if he undoes weak coupling only
    wigner_u_interference = off_diagonal_mean(rho0)  # still coherent in Wigner's description
    # Track C: CSL localizes before Wigner measures — interference dies
    c = run_csl_trajectory(rho0, clump, steps=60, lambda0=1.0, seed=seed)
    wigner_c_interference = off_diagonal_mean(c["rho_final"])

    return {
        "friend_classicality_U": friend_classical,
        "wigner_interference_proxy_U": float(wigner_u_interference),
        "wigner_interference_proxy_C": float(wigner_c_interference),
        "tracks_diverge": wigner_u_interference > wigner_c_interference + 0.15,
        "noise": float(rng.normal(0, 1e-6)),
    }


def run_measurement_lab(seed: int = 42) -> dict:
    np.random.seed(seed)
    rho0 = qubit_bloch_dm(np.pi / 2)  # equal superposition
    clump = ClumpState(amplitude=1.0, coherence_length=1.0, mode_stability=0.85)

    gamma_grid = [0.0, 0.2, 0.5, 1.0, 2.0]
    track_u_rows = []
    for g in gamma_grid:
        out = amplitude_damping_like_dephasing(rho0, gamma=g, steps=50, dt=0.05)
        class_score = classicality_score(out["rho_final"])
        definite = definiteness_from_clump(clump, class_score)
        track_u_rows.append(
            {
                "gamma": g,
                "final_purity": out["purity"][-1],
                "final_offdiag": out["off_diagonal_mean"][-1],
                "final_entropy": out["pointer_entropy"][-1],
                "classicality": class_score,
                "definiteness": definite,
                "entropy_nondecreasing": all(
                    out["pointer_entropy"][i] <= out["pointer_entropy"][i + 1] + 1e-9
                    for i in range(len(out["pointer_entropy"]) - 1)
                )
                or g == 0.0,
            }
        )

    # Q1: offdiag falls with gamma
    offdiags = [r["final_offdiag"] for r in track_u_rows]
    q1_pass = all(offdiags[i] >= offdiags[i + 1] - 1e-9 for i in range(len(offdiags) - 1))

    # Q5: classicality rises with gamma
    classics = [r["classicality"] for r in track_u_rows]
    q5_pass = classics[-1] >= classics[0]

    # Q7: entropy tends up for gamma > 0
    q7_pass = all(r["entropy_nondecreasing"] or r["gamma"] == 0.0 for r in track_u_rows)

    track_c = run_csl_trajectory(rho0, clump, steps=50, lambda0=0.08, seed=seed)
    track_c_summary = {
        "lambda": track_c["lambda"],
        "final_purity": track_c["purity"][-1],
        "final_offdiag": track_c["off_diagonal_mean"][-1],
        "requires_collapse_for_classicality": track_c["off_diagonal_mean"][-1]
        < track_u_rows[0]["final_offdiag"],
    }

    # Track U does not need λ for classicality at high gamma
    high_g = track_u_rows[-1]
    q1_u_no_lambda_needed = high_g["classicality"] > 0.7

    wf = _wigner_friend_toy(seed=seed)

    output = {
        "experiment": "measurement_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "track_u_gamma_sweep": track_u_rows,
        "track_c_summary": track_c_summary,
        "wigner_friend_toy": wf,
        "predictions": {
            "Q1_offdiag_decay_with_gamma": q1_pass,
            "Q1_U_classical_without_lambda": q1_u_no_lambda_needed,
            "Q5_classical_limit": q5_pass,
            "Q7_entropy_arrow_proxy": q7_pass,
            "Q8_tracks_diverge": wf["tracks_diverge"],
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Measurement lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Measurement Lab")
    print("=" * 60)
    run_measurement_lab()
