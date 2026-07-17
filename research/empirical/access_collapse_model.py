"""
Access-Only Collapse Model: P18 battery — can access variables explain integration metrics?

Part VI illusionist stress test.

Run: python research/empirical/access_collapse_model.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    access_only_reconstruction_error,
    astral_band_index,
    creative_flow_index,
    make_internal_micros,
    phi_analog_from_binding,
    residual_integration_score,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "access_collapse_results.json"


def _scenario_metrics(scenario_id: str) -> Dict:
    """Build full metric bundles from FEO/IEO-class scenarios."""
    configs = {
        "creative_flow": {"base": 0.65, "disorg": 0.12, "coupling": 0.38, "acc": 0.75, "rt": 0.55, "timing": 0.45},
        "hypnagogic": {"base": 0.35, "disorg": 0.08, "coupling": 0.25, "acc": 0.5, "rt": 0.7, "timing": 0.35},
        "boredom": {"base": 0.5, "disorg": 0.05, "coupling": 0.1, "acc": 0.95, "rt": 0.2, "timing": 0.9},
        "filter_failure": {"base": 0.2, "disorg": 0.85, "coupling": 0.05, "acc": 0.4, "rt": 0.9, "timing": 0.3},
        "insight": {"base": 0.55, "disorg": 0.1, "coupling": 0.42, "acc": 0.6, "rt": 0.85, "timing": 0.2},
    }
    cfg = configs.get(scenario_id, configs["creative_flow"])
    micros = make_internal_micros(scenario_id, n_nodes=6, base_intensity=cfg["base"])
    phi = phi_analog_from_binding(micros)
    if scenario_id == "hypnagogic":
        phi *= 0.5
    cfi = creative_flow_index(phi, cfg["disorg"], coupling=cfg["coupling"])
    motor = 0.35 if scenario_id == "creative_flow" else (0.08 if scenario_id == "hypnagogic" else 0.9)
    abi = astral_band_index(phi, cfg["disorg"], filter_depth=0.45, motor_binding=motor)

    return {
        "scenario": scenario_id,
        "phi": phi,
        "creative_flow_index": cfi,
        "astral_band_index": abi,
        "disorganization": cfg["disorg"],
        "coupling": cfg["coupling"],
        "report_accuracy": cfg["acc"],
        "reaction_time_proxy": cfg["rt"],
        "report_timing": cfg["timing"],
    }


def run_access_collapse_experiment() -> Dict:
    scenario_ids = ["creative_flow", "hypnagogic", "boredom", "filter_failure", "insight"]
    results: List[Dict] = []

    for sid in scenario_ids:
        full = _scenario_metrics(sid)
        recon_error = access_only_reconstruction_error(full)
        access_reconstruction = {
            "phi": full["report_accuracy"] * (1.0 - full["reaction_time_proxy"] * 0.3),
            "creative_flow_index": full["report_timing"] * full["report_accuracy"],
            "astral_band_index": full["report_timing"] * 0.4,
        }
        residual = residual_integration_score(full, access_reconstruction)

        results.append({
            "scenario": sid,
            "full_metrics": {
                "phi": round(full["phi"], 4),
                "creative_flow_index": round(full["creative_flow_index"], 4),
                "astral_band_index": round(full["astral_band_index"], 4),
            },
            "access_reconstruction": {k: round(v, 4) for k, v in access_reconstruction.items()},
            "reconstruction_error": round(recon_error, 4),
            "residual_integration_score": round(residual, 4),
            "illusionist_wins": residual < 0.08,
            "panpsychist_wins": residual > 0.15,
        })

    flow_hyp = [r for r in results if r["scenario"] in ("creative_flow", "hypnagogic", "insight")]
    p18_analog = any(r["panpsychist_wins"] for r in flow_hyp)

    interpretation = {
        "p18_analog": p18_analog,
        "illusionist_wins_count": sum(1 for r in results if r["illusionist_wins"]),
        "panpsychist_wins_count": sum(1 for r in results if r["panpsychist_wins"]),
        "mean_residual": round(sum(r["residual_integration_score"] for r in results) / len(results), 4),
        "finding": (
            "Residual integration persists on flow/hypnagogic/insight scenarios"
            if p18_analog else "Access-only collapse succeeds across battery"
        ),
        "caveat": "Simulation only; access proxies are simplified",
    }

    output = {
        "experiment": "access_collapse_model",
        "program": "Hard Problem Protocol Part VI",
        "results_by_scenario": results,
        "interpretation": interpretation,
    }

    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Access collapse experiment complete. Results: {OUTPUT_PATH}")
    for r in results:
        print(f"  {r['scenario']:<16} residual={r['residual_integration_score']:.3f}  illusionist_win={r['illusionist_wins']}")
    print(f"  P18 analog: {p18_analog}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Access-Only Collapse Model: P18 Battery")
    print("=" * 60)
    run_access_collapse_experiment()
