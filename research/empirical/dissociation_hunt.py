"""
Dissociation Hunt: adversarial scenarios where HPP tracks maximally diverge.

Part VI — runs P18-P22 scenario battery and ranks by adversarial_value.

Run: python research/empirical/dissociation_hunt.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    adversarial_track_scores,
    astral_band_index,
    creative_flow_index,
    make_internal_micros,
    mode_transition_detected,
    phi_analog_from_binding,
    residual_integration_score,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "dissociation_hunt_results.json"


def _build_scenarios() -> List[Dict]:
    """P18-P22 adversarial scenario metric bundles."""
    scenarios: List[Dict] = []

    # P18 / P10 / P14 class — creative flow (high residual expected)
    micros_flow = make_internal_micros("flow", n_nodes=6, base_intensity=0.65)
    phi_flow = phi_analog_from_binding(micros_flow)
    disorg_flow = 0.12
    cfi_flow = creative_flow_index(phi_flow, disorg_flow, coupling=0.38)
    abi_flow = astral_band_index(phi_flow, disorg_flow, filter_depth=0.45, motor_binding=0.35)
    scenarios.append({
        "id": "P18_creative_flow",
        "prediction": "P18",
        "qualia_invariants": ["Q4", "Q3"],
        "phi": phi_flow,
        "creative_flow_index": cfi_flow,
        "astral_band_index": abi_flow,
        "disorganization": disorg_flow,
        "coupling": 0.38,
        "report_accuracy": 0.75,
        "reaction_time_proxy": 0.55,
        "report_timing": 0.45,
        "unity_score": phi_flow * 0.9,
        "structure_hash": phi_flow,
        "valence": 0.2,
    })

    # P18 / P14 — hypnagogic (mid abi, moderate access gap)
    micros_hyp = make_internal_micros("hyp", n_nodes=5, base_intensity=0.35)
    phi_hyp = phi_analog_from_binding(micros_hyp) * 0.5
    disorg_hyp = 0.08
    cfi_hyp = creative_flow_index(phi_hyp, disorg_hyp, coupling=0.25)
    abi_hyp = astral_band_index(phi_hyp, disorg_hyp, filter_depth=0.55, motor_binding=0.08)
    scenarios.append({
        "id": "P18_hypnagogic",
        "prediction": "P18",
        "qualia_invariants": ["Q8", "Q7"],
        "phi": phi_hyp,
        "creative_flow_index": cfi_hyp,
        "astral_band_index": abi_hyp,
        "disorganization": disorg_hyp,
        "coupling": 0.25,
        "report_accuracy": 0.5,
        "reaction_time_proxy": 0.7,
        "report_timing": 0.35,
        "unity_score": phi_hyp * 0.7,
        "structure_hash": phi_hyp * 1.1,
        "valence": 0.0,
    })

    # P19 — suffering without self-model update
    scenarios.append({
        "id": "P19_suffering_decoupled",
        "prediction": "P19",
        "qualia_invariants": ["Q9", "Q2"],
        "phi": 0.45,
        "creative_flow_index": 0.2,
        "astral_band_index": 0.15,
        "disorganization": 0.18,
        "coupling": 0.2,
        "valence": -0.85,
        "self_model_update": 0.05,
        "report_accuracy": 0.9,
        "reaction_time_proxy": 0.4,
        "report_timing": 0.8,
        "unity_score": 0.4,
        "structure_hash": 0.42,
    })

    # P20 — insight pre-report (P11 class)
    phi_series = [0.04, 0.22]
    scenarios.append({
        "id": "P20_insight_pre_report",
        "prediction": "P20",
        "qualia_invariants": ["Q5"],
        "phi": phi_series[-1],
        "phi_series": phi_series,
        "creative_flow_index": 0.78,
        "astral_band_index": 0.12,
        "disorganization": 0.1,
        "coupling": 0.42,
        "report_accuracy": 0.6,
        "reaction_time_proxy": 0.85,
        "report_timing": 0.2,
        "unity_score": 0.55,
        "structure_hash": 0.5,
        "valence": 0.4,
        "p11_analog": mode_transition_detected(phi_series, threshold=0.15),
    })

    # P21 — spectrum inversion proxy (same structure, different valence tag)
    base_hash = 0.62
    scenarios.append({
        "id": "P21_spectrum_inversion_a",
        "prediction": "P21",
        "qualia_invariants": ["Q1"],
        "phi": base_hash,
        "structure_hash": base_hash,
        "qualia_type_hash": 0.1,
        "creative_flow_index": 0.5,
        "astral_band_index": 0.2,
        "disorganization": 0.1,
        "coupling": 0.3,
        "valence": 0.3,
        "report_accuracy": 0.85,
        "reaction_time_proxy": 0.5,
        "report_timing": 0.6,
        "unity_score": 0.55,
    })
    scenarios.append({
        "id": "P21_spectrum_inversion_b",
        "prediction": "P21",
        "qualia_invariants": ["Q1"],
        "phi": base_hash,
        "structure_hash": base_hash,
        "qualia_type_hash": 0.9,
        "creative_flow_index": 0.5,
        "astral_band_index": 0.2,
        "disorganization": 0.1,
        "coupling": 0.3,
        "valence": -0.3,
        "report_accuracy": 0.85,
        "reaction_time_proxy": 0.5,
        "report_timing": 0.6,
        "unity_score": 0.55,
    })

    # P4/P10 access-only friendly — boredom (low residual expected)
    micros_bore = make_internal_micros("bore", n_nodes=6, base_intensity=0.5)
    phi_bore = phi_analog_from_binding(micros_bore) * 0.85
    disorg_bore = 0.05
    scenarios.append({
        "id": "P18_boredom_baseline",
        "prediction": "P18",
        "qualia_invariants": ["Q4"],
        "phi": phi_bore,
        "creative_flow_index": creative_flow_index(phi_bore, disorg_bore, coupling=0.1),
        "astral_band_index": astral_band_index(phi_bore, disorg_bore, filter_depth=0.8, motor_binding=0.9),
        "disorganization": disorg_bore,
        "coupling": 0.1,
        "report_accuracy": 0.95,
        "reaction_time_proxy": 0.2,
        "report_timing": 0.9,
        "unity_score": phi_bore,
        "structure_hash": phi_bore,
        "valence": -0.1,
    })

    return scenarios


def _adversarial_value(track_scores: Dict[str, float]) -> float:
    """Max pairwise divergence among three track scores."""
    vals = [
        track_scores["panpsychist_close"],
        track_scores["illusionist_dissolve"],
        track_scores["structural_physicalism"],
    ]
    return float(max(vals) - min(vals))


def run_dissociation_hunt() -> Dict:
    scenarios = _build_scenarios()
    results = []

    for sc in scenarios:
        tracks = adversarial_track_scores(sc)
        adv_val = _adversarial_value(tracks)
        entry = {
            "scenario_id": sc["id"],
            "prediction": sc["prediction"],
            "qualia_invariants": sc.get("qualia_invariants", []),
            "track_scores": tracks,
            "adversarial_value": round(adv_val, 4),
            "p18_analog": tracks["residual_integration"] > 0.15,
        }
        results.append(entry)

    ranked = sorted(results, key=lambda x: x["adversarial_value"], reverse=True)

    p18_scenarios = [r for r in results if r["prediction"] == "P18"]
    p18_analog = any(r["p18_analog"] for r in p18_scenarios if "flow" in r["scenario_id"] or "hypnagogic" in r["scenario_id"])

    interpretation = {
        "highest_adversarial_value": ranked[0]["scenario_id"] if ranked else None,
        "p18_analog": p18_analog,
        "panpsychist_leading_scenarios": [
            r["scenario_id"] for r in ranked
            if r["track_scores"]["panpsychist_close"] == max(r["track_scores"].values())
        ][:3],
        "illusionist_leading_scenarios": [
            r["scenario_id"] for r in ranked
            if r["track_scores"]["illusionist_dissolve"] == max(r["track_scores"].values())
        ][:3],
        "caveat": "Simulation proxies only; adversarial_value ranks in-silico divergence",
    }

    output = {
        "experiment": "dissociation_hunt",
        "program": "Hard Problem Protocol Part VI",
        "scenarios": results,
        "ranked_by_adversarial_value": [r["scenario_id"] for r in ranked],
        "interpretation": interpretation,
    }

    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Dissociation hunt complete. Results: {OUTPUT_PATH}")
    for r in ranked[:5]:
        print(f"  {r['scenario_id']:<28} adv={r['adversarial_value']:.3f}  residual={r['track_scores']['residual_integration']:.3f}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Dissociation Hunt: HPP Adversarial Scenarios")
    print("=" * 60)
    run_dissociation_hunt()
