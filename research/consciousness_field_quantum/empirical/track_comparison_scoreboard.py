"""
Track U vs Track C head-to-head scoreboard (physics-weighted).

Run: python research/consciousness_field_quantum/empirical/track_comparison_scoreboard.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.consciousness_field_quantum.empirical.born_rule_lab import run_born_rule_lab
from research.consciousness_field_quantum.empirical.entanglement_lab import run_entanglement_lab
from research.consciousness_field_quantum.empirical.measurement_lab import run_measurement_lab
from research.consciousness_field_quantum.empirical.preferred_basis_lab import (
    run_preferred_basis_lab,
)
from research.consciousness_field_quantum.empirical.awareness_matter_qm_lab import (
    run_awareness_matter_qm_lab,
)
from research.consciousness_field_quantum.empirical.metzinger_layer_lab import (
    run_metzinger_layer_lab,
)
OUTPUT_PATH = Path(__file__).resolve().parent / "track_comparison_scoreboard.json"

# Weights from DUAL_TRACK.md
WEIGHTS = {
    "born_fit": 0.30,
    "no_signaling": 0.25,
    "decoherence_match": 0.20,
    "classical_limit": 0.10,
    "preferred_basis": 0.10,
    "occam_physics_acceptance": 0.05,
}


def _clip01(x: float) -> float:
    return float(max(0.0, min(1.0, x)))


def score_tracks(
    measurement: Dict[str, Any],
    preferred: Dict[str, Any],
    born: Dict[str, Any],
    entanglement: Dict[str, Any],
) -> Dict[str, Any]:
    # --- Born fit ---
    born_u = _clip01(float(born["track_u"]["born_fit_score"]))
    best_c_tv = float(born["track_c_best"]["tv_born"])
    # Map TV to score like born_fit_score
    if best_c_tv <= 0.08:
        born_c = 1.0
    elif best_c_tv >= 0.5:
        born_c = 0.0
    else:
        born_c = 1.0 - (best_c_tv - 0.08) / (0.5 - 0.08)

    # --- No-signaling ---
    sig_u = max(
        float(entanglement["signaling_score_A_track_U"]),
        float(entanglement["signaling_score_B_track_U"]),
    )
    ns_u = _clip01(1.0 - sig_u / 0.2)
    # Careful CSL not fully modeled; naive collapse fails — Track C gets partial credit
    # if we assume proper CSL (0.7) but penalize naive signaling flag
    naive = float(entanglement["naive_collapse_signaling_score"])
    ns_c = _clip01(0.7 * (1.0 - min(naive, 1.0)))  # naive path tanks the score

    # --- Decoherence match (U native) ---
    preds_m = measurement["predictions"]
    deco_u = 1.0 if preds_m.get("Q1_offdiag_decay_with_gamma") else 0.3
    # C produces classicality but via collapse — partial
    deco_c = 0.55 if measurement["track_c_summary"]["final_offdiag"] < 0.2 else 0.3

    # --- Classical limit ---
    class_u = 1.0 if preds_m.get("Q5_classical_limit") else 0.2
    class_c = 0.8 if measurement["track_c_summary"]["final_purity"] > 0.7 else 0.4

    # --- Preferred basis ---
    pref_u = 1.0 if preferred["predictions"].get("Q3_preferred_basis_alignment") else 0.2
    pref_c = 0.5  # CSL assumed in pointer basis by construction; no extra win

    # --- Occam / physics acceptance ---
    occam_u = 1.0
    occam_c = 0.25  # fringe penalty unless outperforming (applied as low base)

    def weighted(scores: Dict[str, float]) -> float:
        return sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)

    scores_u = {
        "born_fit": born_u,
        "no_signaling": ns_u,
        "decoherence_match": deco_u,
        "classical_limit": class_u,
        "preferred_basis": pref_u,
        "occam_physics_acceptance": occam_u,
    }
    scores_c = {
        "born_fit": born_c,
        "no_signaling": ns_c,
        "decoherence_match": deco_c,
        "classical_limit": class_c,
        "preferred_basis": pref_c,
        "occam_physics_acceptance": occam_c,
    }

    total_u = weighted(scores_u)
    total_c = weighted(scores_c)

    # Hard fail override
    hard_fail_u = ns_u < 0.5 or born_u < 0.5
    hard_fail_c = ns_c < 0.3 or born_c < 0.3

    if total_u > total_c + 1e-9:
        winner = "U"
    elif total_c > total_u + 1e-9:
        winner = "C"
    else:
        # tie-break Born + no-signaling
        bu = scores_u["born_fit"] + scores_u["no_signaling"]
        bc = scores_c["born_fit"] + scores_c["no_signaling"]
        winner = "U" if bu >= bc else "C"

    return {
        "weights": WEIGHTS,
        "track_U_scores": scores_u,
        "track_C_scores": scores_c,
        "track_U_total": total_u,
        "track_C_total": total_c,
        "winner": winner,
        "hard_fail_U": hard_fail_u,
        "hard_fail_C": hard_fail_c,
        "Q12_U_preferred_or_tied_on_constraints": winner == "U"
        or (scores_u["born_fit"] >= scores_c["born_fit"] and scores_u["no_signaling"] >= scores_c["no_signaling"]),
    }


def run_scoreboard(seed: int = 42) -> dict:
    measurement = run_measurement_lab(seed=seed)
    preferred = run_preferred_basis_lab(seed=seed)
    born = run_born_rule_lab(seed=seed)
    entanglement = run_entanglement_lab(seed=seed)
    metzinger = run_metzinger_layer_lab(seed=seed)
    awareness_qm = run_awareness_matter_qm_lab(seed=seed)

    comparison = score_tracks(measurement, preferred, born, entanglement)

    prediction_rollup = {
        "Q1": measurement["predictions"].get("Q1_offdiag_decay_with_gamma"),
        "Q2": born["predictions"].get("Q2_track_c_born_band"),
        "Q3": preferred["predictions"].get("Q3_preferred_basis_alignment"),
        "Q4_U": entanglement["predictions"].get("Q4_track_U_no_signaling"),
        "Q4_naive_C_flag": entanglement["predictions"].get("Q4_naive_C_flags_signaling"),
        "Q5": measurement["predictions"].get("Q5_classical_limit"),
        "Q6": entanglement["predictions"].get("Q6_multi_clump_correlations"),
        "Q7": measurement["predictions"].get("Q7_entropy_arrow_proxy"),
        "Q8": measurement["predictions"].get("Q8_tracks_diverge"),
        "Q12": comparison["Q12_U_preferred_or_tied_on_constraints"],
        "M1": metzinger["predictions"].get("M1_mpe_profile_match"),
        "M2": metzinger["predictions"].get("M2_mpe_to_psm_rises"),
        "M3": awareness_qm["predictions"].get("M3_pmir_off_weakens_pointer_alignment"),
        "M4": awareness_qm["predictions"].get("M4_track_u_born_across_layers"),
        "M5": awareness_qm["predictions"].get("M5_track_c_naive_signaling_hard_fail"),
        "M6": metzinger["predictions"].get("M6_wigner_grades_diverge"),
        "M7": metzinger["predictions"].get("M7_classical_lock"),
        "M8": metzinger["predictions"].get("M8_complexity_without_self_not_psm"),
    }

    metzinger_bridge = {
        "note": (
            "Metzinger M1–M8 are layer/diagnostics scores — separate from "
            "physics-weighted U vs C totals."
        ),
        "m_pass_count": sum(1 for k in ("M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8") if prediction_rollup.get(k)),
        "m_total": 8,
        "layer_lab": metzinger["predictions"],
        "qm_lab": awareness_qm["predictions"],
    }

    output = {
        "experiment": "track_comparison_scoreboard",
        "label": "simulation — not empirical QM confirmation",
        "seed": seed,
        "comparison": comparison,
        "prediction_rollup": prediction_rollup,
        "metzinger_bridge": metzinger_bridge,
        "lab_paths": {
            "measurement": str(Path(__file__).parent / "measurement_lab_results.json"),
            "preferred_basis": str(Path(__file__).parent / "preferred_basis_lab_results.json"),
            "born_rule": str(Path(__file__).parent / "born_rule_lab_results.json"),
            "entanglement": str(Path(__file__).parent / "entanglement_lab_results.json"),
            "metzinger_layer": str(Path(__file__).parent / "metzinger_layer_lab_results.json"),
            "awareness_matter_qm": str(
                Path(__file__).parent / "awareness_matter_qm_lab_results.json"
            ),
        },
        "caveat": (
            "Part VIII shows structural compatibility under toy models. "
            "Does not prove a consciousness field or solve the measurement problem. "
            "Metzinger bridge adds typed observer order parameters; not a Standard Model field."
        ),
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Scoreboard complete. Results: {OUTPUT_PATH}")
    print(
        f"  Winner={comparison['winner']}  "
        f"U={comparison['track_U_total']:.3f}  C={comparison['track_C_total']:.3f}"
    )
    print(
        f"  Metzinger bridge: {metzinger_bridge['m_pass_count']}/{metzinger_bridge['m_total']} M-predictions"
    )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Part VIII Track Comparison Scoreboard")
    print("=" * 60)
    run_scoreboard()
