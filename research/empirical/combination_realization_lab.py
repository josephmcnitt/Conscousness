"""
Combination Realization Lab: P22 unity deathmatch + specification problem proxy.

Extends combination_model.py for Part VI adversarial track.

Run: python research/empirical/combination_realization_lab.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.combination_model import (
    combine_fusion,
    combine_integration,
    combine_summing,
    problem_component_to_micro,
)
from research.empirical.consciousness_metrics import MicroExperience

OUTPUT_PATH = Path(__file__).resolve().parent / "combination_realization_lab_results.json"


def _specification_hash(micros: List[MicroExperience]) -> float:
    """P21/P22 proxy: why THIS qualia-type — hash micro-state to [0,1]."""
    payload = "|".join(
        f"{m.component_id}:{m.intensity:.4f}:{m.valence:.4f}" for m in micros
    )
    digest = hashlib.sha256(payload.encode()).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def _build_dense_components(n: int = 8) -> list:
    """Components with chain + cross deps for reliable integration unity."""
    from core.intelligent_recursive_generator import ProblemComponent

    components = []
    for i in range(n):
        deps = [f"comp_{j}" for j in range(n) if j != i]
        components.append(
            ProblemComponent(
                id=f"comp_{i}",
                description=f"Proto-experiential unit {i}",
                complexity=0.4 + 0.08 * i,
                consciousness_level=0.35 + 0.12 * i,
                interdependencies=deps,
                emergent_properties=[f"property_{i}"] if i > 0 else [],
                transformation_potential=0.5 + 0.08 * i,
            )
        )
    return components


def _unity_score(macro_dict: Dict) -> float:
    """Unity criterion: unified flag dominates; naive summing phi must not win alone."""
    phi = macro_dict["phi_analog"]
    if macro_dict["is_unified"]:
        return float(np.clip(0.65 + 0.35 * phi, 0, 1))
    return float(np.clip(0.15 * phi, 0, 1))


def run_combination_realization_lab(n_components: int = 8) -> Dict:
    components = _build_dense_components(n_components)
    micros = [problem_component_to_micro(c) for c in components]

    summing = asdict(combine_summing(micros))
    fusion = asdict(combine_fusion(micros))
    integration = asdict(combine_integration(micros))

    spec_hash = _specification_hash(micros)

    modes = {
        "summing": summing,
        "fusion": fusion,
        "integration": integration,
    }

    unity_scores = {name: _unity_score(m) for name, m in modes.items()}
    phi_scores = {name: m["phi_analog"] for name, m in modes.items()}

    p22_analog = (
        not summing["is_unified"]
        and (integration["is_unified"] or fusion["is_unified"])
        and (
            unity_scores["integration"] > unity_scores["summing"]
            or unity_scores["fusion"] > unity_scores["summing"]
        )
    )

    interpretation = {
        "p22_analog": p22_analog,
        "specification_hash": round(spec_hash, 4),
        "unity_deathmatch": unity_scores,
        "phi_by_mode": {k: round(v, 4) for k, v in phi_scores.items()},
        "panpsychist_prediction": "Integration/fusion unity > summing",
        "finding": (
            f"Integration unity={unity_scores['integration']:.3f}, "
            f"summing unity={unity_scores['summing']:.3f}, "
            f"spec_hash={spec_hash:.4f}"
        ),
        "caveat": "Specification hash is computational proxy, not real qualia specification",
    }

    output = {
        "experiment": "combination_realization_lab",
        "program": "Hard Problem Protocol Part VI",
        "n_components": n_components,
        "macro_by_mode": modes,
        "unity_scores": {k: round(v, 4) for k, v in unity_scores.items()},
        "specification_hash": round(spec_hash, 4),
        "interpretation": interpretation,
    }

    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Combination realization lab complete. Results: {OUTPUT_PATH}")
    for name, score in unity_scores.items():
        print(f"  {name:<14} unity={score:.4f}  phi={phi_scores[name]:.4f}")
    print(f"  P22 analog: {p22_analog}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Combination Realization Lab: P22 Unity Deathmatch")
    print("=" * 60)
    run_combination_realization_lab(n_components=8)
