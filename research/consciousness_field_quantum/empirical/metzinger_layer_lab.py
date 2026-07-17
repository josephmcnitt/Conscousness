"""
Metzinger layer lab (M1, M2, M6, M7, M8): MPE → PSM → PMIR transitions.

Run: python research/consciousness_field_quantum/empirical/metzinger_layer_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.equations.awareness_matter import (
    awareness_density,
    classical_lock,
    factory_high_complexity_no_self,
    factory_mpe,
    factory_pmir,
    factory_psm,
    is_mpe_active,
    is_pmir_active,
    is_psm_active,
    promote_mpe_to_psm,
    promote_psm_to_pmir,
)
from research.consciousness_field_quantum.equations.decoherence import (
    amplitude_damping_like_dephasing,
    classicality_score,
    off_diagonal_mean,
)
from research.consciousness_field_quantum.equations.density_matrix import qubit_bloch_dm
from research.consciousness_field_quantum.equations.metzinger_constraints import (
    constraint_vector,
    layer_flags,
    mpe_profile_match,
    psm_profile_match,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "metzinger_layer_lab_results.json"


def _wigner_grade_split(seed: int = 0) -> dict:
    """
    M6: MPE-grade vs PSM-grade friend under Track U interference proxy.

    MPE friend: awareness without PSM — weaker classical lock on friend's record.
    PSM+PMIR friend: strong transparency lock — friend's record more classical;
    Wigner's residual interference proxy treated as lower for nested classical record.
    """
    rho0 = qubit_bloch_dm(np.pi / 2)
    mpe = factory_mpe()
    psm = factory_pmir()

    # Shared decoherence environment
    deco = amplitude_damping_like_dephasing(rho0, gamma=1.2, steps=40, dt=0.05)
    class_score = classicality_score(deco["rho_final"])
    off = off_diagonal_mean(deco["rho_final"])

    lock_mpe = classical_lock(mpe, class_score)
    lock_psm = classical_lock(psm, class_score)

    # Interference proxy for Wigner: higher when friend's lock is weaker
    # (less "definite friend outcome" in the experiential sector)
    interference_mpe = float(off + (1.0 - lock_mpe) * 0.35)
    interference_psm = float(off + (1.0 - lock_psm) * 0.35)

    return {
        "friend_classicality": class_score,
        "lock_mpe": lock_mpe,
        "lock_psm": lock_psm,
        "interference_proxy_mpe_friend": interference_mpe,
        "interference_proxy_psm_friend": interference_psm,
        "grades_diverge": interference_mpe > interference_psm + 0.05,
        "rho_A_mpe": awareness_density(mpe),
        "rho_A_psm": awareness_density(psm),
    }


def run_metzinger_layer_lab(seed: int = 42) -> dict:
    np.random.seed(seed)

    mpe = factory_mpe()
    psm = factory_psm()
    pmir = factory_pmir()
    promoted = promote_mpe_to_psm(mpe)
    promoted_pmir = promote_psm_to_pmir(promoted)
    rich_no_self = factory_high_complexity_no_self()

    m1 = mpe_profile_match(mpe)
    m2_before = constraint_vector(mpe)
    m2_after = constraint_vector(promoted)
    m2_pass = (
        (not is_psm_active(mpe))
        and is_psm_active(promoted)
        and m2_after["ownership"] > m2_before["ownership"]
        and m2_after["selfhood"] > m2_before["selfhood"]
    )

    # M7: high transparency + high decoherence classicality → high classical lock
    rho0 = qubit_bloch_dm(np.pi / 2)
    low_g = amplitude_damping_like_dephasing(rho0, gamma=0.05, steps=40, dt=0.05)
    high_g = amplitude_damping_like_dephasing(rho0, gamma=2.0, steps=40, dt=0.05)
    class_low = classicality_score(low_g["rho_final"])
    class_high = classicality_score(high_g["rho_final"])
    lock_low = classical_lock(pmir, class_low)
    lock_high = classical_lock(pmir, class_high)
    m7_pass = lock_high > lock_low + 0.15 and lock_high >= 0.5

    # M8: high complexity without selfhood is not PSM
    m8_pass = (
        rich_no_self.content_complexity >= 0.8
        and (not is_psm_active(rich_no_self))
        and (not is_mpe_active(rich_no_self) or rich_no_self.content_complexity > 0.3)
    )
    # Stricter: must not be PSM-active
    m8_pass = (not is_psm_active(rich_no_self)) and rich_no_self.content_complexity >= 0.8

    wf = _wigner_grade_split(seed=seed)
    m6_pass = bool(wf["grades_diverge"])

    output = {
        "experiment": "metzinger_layer_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "layers": {
            "mpe": {**constraint_vector(mpe), **layer_flags(mpe), "rho_A": awareness_density(mpe)},
            "psm": {**constraint_vector(psm), **layer_flags(psm), "rho_A": awareness_density(psm)},
            "pmir": {
                **constraint_vector(pmir),
                **layer_flags(pmir),
                "rho_A": awareness_density(pmir),
            },
            "promoted_mpe_to_psm": {
                **constraint_vector(promoted),
                **layer_flags(promoted),
            },
            "promoted_to_pmir": {
                **constraint_vector(promoted_pmir),
                **layer_flags(promoted_pmir),
                "pmir_active": is_pmir_active(promoted_pmir),
            },
            "high_complexity_no_self": {
                **constraint_vector(rich_no_self),
                **layer_flags(rich_no_self),
            },
        },
        "m1_mpe_profile": m1,
        "classical_lock": {
            "class_low_gamma": class_low,
            "class_high_gamma": class_high,
            "lock_low": lock_low,
            "lock_high": lock_high,
        },
        "wigner_grade_split": wf,
        "predictions": {
            "M1_mpe_profile_match": bool(m1["pass"]),
            "M2_mpe_to_psm_rises": bool(m2_pass),
            "M6_wigner_grades_diverge": m6_pass,
            "M7_classical_lock": bool(m7_pass),
            "M8_complexity_without_self_not_psm": bool(m8_pass),
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Metzinger layer lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Metzinger Layer Lab")
    print("=" * 60)
    run_metzinger_layer_lab()
