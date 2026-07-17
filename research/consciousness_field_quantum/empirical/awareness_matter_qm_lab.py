"""
Awareness-matter QM lab (M3, M4, M5): preferred basis, Born, no-signaling under layers.

Run: python research/consciousness_field_quantum/empirical/awareness_matter_qm_lab.py
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
    AwarenessMatterState,
    awareness_density,
    factory_mpe,
    factory_pmir,
    factory_psm,
    pointer_alignment_strength,
    selection_weights_awareness,
)
from research.consciousness_field_quantum.equations.born_rule import (
    born_probabilities,
    born_total_variation,
    empirical_frequencies,
    sample_outcomes,
)
from research.consciousness_field_quantum.equations.collapse_csl import csl_rate, run_csl_trajectory
from research.consciousness_field_quantum.equations.decoherence import (
    amplitude_damping_like_dephasing,
    off_diagonal_mean,
)
from research.consciousness_field_quantum.equations.density_matrix import (
    bell_phi_plus,
    hadamard,
    qubit_bloch_dm,
)
from research.consciousness_field_quantum.equations.no_signaling import (
    naive_local_collapse_signaling,
    signaling_score,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "awareness_matter_qm_lab_results.json"


def _pmir_off_state() -> AwarenessMatterState:
    """PSM-ish content but PMIR off — weak pointer alignment (M3)."""
    return AwarenessMatterState(
        amplitude=1.0,
        coherence_length=1.0,
        mode_stability=0.9,
        wakefulness=0.9,
        content_complexity=0.5,
        epistemicity=0.7,
        opacity_mpe=0.2,
        selfhood=0.8,
        transparency=0.85,
        ownership=0.7,
        diachronic=0.7,
        perspectivalness=0.05,
        intentional_arrow=0.05,
    ).clamp()


def run_awareness_matter_qm_lab(seed: int = 42, n_samples: int = 4000) -> dict:
    rng = np.random.default_rng(seed)
    rho0 = qubit_bloch_dm(np.pi / 2)
    pmir = factory_pmir()
    pmir_off = _pmir_off_state()
    mpe = factory_mpe()
    psm = factory_psm()

    # --- M3: preferred basis / pointer alignment ---
    align_on = pointer_alignment_strength(pmir)
    align_off = pointer_alignment_strength(pmir_off)

    in_basis = amplitude_damping_like_dephasing(rho0, gamma=1.5, steps=40, dt=0.05)
    off_in = off_diagonal_mean(in_basis["rho_final"])
    wrong = amplitude_damping_like_dephasing(
        rho0, gamma=1.5, steps=40, dt=0.05, basis_U=hadamard()
    )
    off_wrong = off_diagonal_mean(wrong["rho_final"])
    interaction_aligns = off_in <= off_wrong + 1e-9

    # Effective preferred-basis score: interaction alignment * PMIR lock
    pref_score_on = float(interaction_aligns) * align_on
    pref_score_off = float(interaction_aligns) * align_off
    m3_pass = align_on > align_off + 0.3 and pref_score_on > pref_score_off

    # --- M4: Track U Born TV across layer regimes ---
    theta = 2 * np.arccos(np.sqrt(0.7))
    rho_born = qubit_bloch_dm(theta)
    p_born = born_probabilities(rho_born)
    tol = 0.08
    layer_tvs = {}
    for name, state in (("mpe", mpe), ("psm", psm), ("pmir", pmir)):
        weights = selection_weights_awareness(p_born, state)
        samples = sample_outcomes(weights, n_samples, rng)
        p_emp = empirical_frequencies(samples, len(p_born))
        # Compare empirical from selection weights to Born — mild blend must stay near Born
        tv = born_total_variation(p_emp, p_born)
        # Also pure Born sampling control
        samples_b = sample_outcomes(p_born, n_samples, rng)
        tv_born_pure = born_total_variation(
            empirical_frequencies(samples_b, len(p_born)), p_born
        )
        layer_tvs[name] = {
            "tv_selection_vs_born": tv,
            "tv_pure_born": tv_born_pure,
            "rho_A": awareness_density(state),
            "ok": tv <= tol,
        }
    m4_pass = all(v["ok"] for v in layer_tvs.values())

    # --- M5: Track C with rho_A still flags naive collapse signaling ---
    lam_mpe = csl_rate(mpe, lambda0=0.08)
    lam_pmir = csl_rate(pmir, lambda0=0.08)
    traj = run_csl_trajectory(rho_born, pmir, steps=40, lambda0=0.08, seed=seed)
    rho_bell = bell_phi_plus()
    sig_u = signaling_score(rho_bell, party="A")
    naive_sig = naive_local_collapse_signaling(rho_bell, rng)
    m5_pass = sig_u < 0.05 and naive_sig > 0.2

    output = {
        "experiment": "awareness_matter_qm_lab",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "m3_preferred_basis": {
            "pointer_alignment_pmir_on": align_on,
            "pointer_alignment_pmir_off": align_off,
            "offdiag_interaction_basis": off_in,
            "offdiag_wrong_basis": off_wrong,
            "interaction_aligns": bool(interaction_aligns),
            "pref_score_on": pref_score_on,
            "pref_score_off": pref_score_off,
        },
        "m4_born_across_layers": layer_tvs,
        "m5_track_c_rho_A": {
            "lambda_mpe": lam_mpe,
            "lambda_pmir": lam_pmir,
            "observer_density_pmir": traj["observer_density"],
            "signaling_score_U": sig_u,
            "naive_collapse_signaling_score": naive_sig,
            "rho_A_boosts_lambda": lam_pmir > lam_mpe,
        },
        "predictions": {
            "M3_pmir_off_weakens_pointer_alignment": bool(m3_pass),
            "M4_track_u_born_across_layers": bool(m4_pass),
            "M5_track_c_naive_signaling_hard_fail": bool(m5_pass),
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Awareness-matter QM lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Awareness-Matter QM Lab")
    print("=" * 60)
    run_awareness_matter_qm_lab()
