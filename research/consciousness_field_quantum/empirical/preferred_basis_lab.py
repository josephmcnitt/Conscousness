"""
Preferred basis lab (Q3): decoherence aligns with interaction basis.

Run: python research/consciousness_field_quantum/empirical/preferred_basis_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.equations.decoherence import (
    amplitude_damping_like_dephasing,
    off_diagonal_mean,
)
from research.consciousness_field_quantum.equations.density_matrix import (
    hadamard,
    qubit_bloch_dm,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "preferred_basis_lab_results.json"


def run_preferred_basis_lab(seed: int = 42) -> dict:
    np.random.seed(seed)
    rho0 = qubit_bloch_dm(np.pi / 2)

    in_basis = amplitude_damping_like_dephasing(rho0, gamma=1.5, steps=40, dt=0.05)
    off_in = off_diagonal_mean(in_basis["rho_final"])

    H = hadamard()
    wrong = amplitude_damping_like_dephasing(
        rho0, gamma=1.5, steps=40, dt=0.05, basis_U=H
    )
    off_wrong_comp = off_diagonal_mean(wrong["rho_final"])

    q3_pass = off_in < 0.05 and off_in <= off_wrong_comp + 1e-9

    output = {
        "experiment": "preferred_basis_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "interaction_basis": "Z_computational",
        "offdiag_after_dephase_in_interaction_basis": off_in,
        "offdiag_comp_after_dephase_in_hadamard_basis": off_wrong_comp,
        "predictions": {
            "Q3_preferred_basis_alignment": bool(q3_pass),
            "interaction_more_classicalizing": off_in <= off_wrong_comp + 1e-9,
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Preferred basis lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Preferred Basis Lab")
    print("=" * 60)
    run_preferred_basis_lab()
