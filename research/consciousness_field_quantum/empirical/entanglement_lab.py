"""
Entanglement lab (Q4, Q6): CHSH, no-signaling, naive collapse signaling flag.

Run: python research/consciousness_field_quantum/empirical/entanglement_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.equations.density_matrix import bell_phi_plus
from research.consciousness_field_quantum.equations.no_signaling import (
    chsh_correlator,
    naive_local_collapse_signaling,
    signaling_score,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "entanglement_lab_results.json"


def run_entanglement_lab(seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    rho = bell_phi_plus()

    chsh = chsh_correlator(rho)
    # Ideal 2√2 ≈ 2.828
    chsh_ok = abs(chsh) > 2.0  # violates classical bound

    sig_u = signaling_score(rho, party="A")
    sig_u_b = signaling_score(rho, party="B")
    naive_sig = naive_local_collapse_signaling(rho, rng)

    q4_u_pass = sig_u < 0.05 and sig_u_b < 0.05
    q4_c_naive_fails = naive_sig > 0.2  # flags pathological Track C

    # Q6 multi-clump: two parties' correlated records — CHSH as proxy for shared correlation
    q6_pass = chsh_ok and q4_u_pass

    output = {
        "experiment": "entanglement_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "chsh": chsh,
        "chsh_classical_bound": 2.0,
        "chsh_quantum_max": float(2 * np.sqrt(2)),
        "signaling_score_A_track_U": sig_u,
        "signaling_score_B_track_U": sig_u_b,
        "naive_collapse_signaling_score": naive_sig,
        "predictions": {
            "Q4_track_U_no_signaling": bool(q4_u_pass),
            "Q4_naive_C_flags_signaling": bool(q4_c_naive_fails),
            "Q6_multi_clump_correlations": bool(q6_pass),
            "bell_violation": bool(chsh_ok),
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Entanglement lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Entanglement Lab")
    print("=" * 60)
    run_entanglement_lab()
