"""
Combination Model: Micro-experiential units combining via binding rules.

Tier 2 computational experiment for Prediction P1/P2 and Axiom A4 (Composition).
Extends ProblemComponent with proto-experiential properties and phi-like integration.

Models what panpsychism predicts about combination — NOT detection of real micro-experience.

Run: python research/empirical/combination_model.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.intelligent_recursive_generator import ProblemComponent
from research.empirical.consciousness_metrics import (
    MicroExperience,
    binding_matrix,
    math_log_norm,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "combination_model_results.json"


class CombinationMode(str, Enum):
    SUMMING = "summing"
    FUSION = "fusion"
    INTEGRATION = "integration"


@dataclass
class MacroExperience:
    """Combined macro-experience from micro-units."""
    mode: CombinationMode
    unified_intensity: float
    unified_valence: float
    phi_analog: float
    n_micro_units: int
    is_unified: bool
    component_ids: List[str]


def problem_component_to_micro(component: ProblemComponent) -> MicroExperience:
    """Map existing ProblemComponent to proto-experiential unit."""
    intensity = component.consciousness_level
    valence = (component.transformation_potential - 0.5) * 2
    binding = {dep: 0.7 for dep in component.interdependencies}
    return MicroExperience(
        component_id=component.id,
        intensity=intensity,
        valence=valence,
        binding_affinity=binding,
    )


def combine_summing(micros: List[MicroExperience]) -> MacroExperience:
    """Naive summing — subject-summing without fusion (problematic for unity)."""
    if not micros:
        return MacroExperience(CombinationMode.SUMMING, 0, 0, 0, 0, False, [])

    total_intensity = sum(m.phenomenal_magnitude for m in micros)
    avg_valence = np.mean([m.valence for m in micros])
    phi = min(1.0, total_intensity / len(micros))

    return MacroExperience(
        mode=CombinationMode.SUMMING,
        unified_intensity=total_intensity,
        unified_valence=float(avg_valence),
        phi_analog=float(phi),
        n_micro_units=len(micros),
        is_unified=False,
        component_ids=[m.component_id for m in micros],
    )


def combine_fusion(micros: List[MicroExperience]) -> MacroExperience:
    """Seager-style fusion — new subject, non-linear integration."""
    if not micros:
        return MacroExperience(CombinationMode.FUSION, 0, 0, 0, 0, False, [])

    magnitudes = np.array([m.phenomenal_magnitude for m in micros])
    valences = np.array([m.valence for m in micros])
    B = binding_matrix(micros)
    binding_strength = float(B.mean()) if B.size else 0.5

    unified_intensity = float(np.power(magnitudes.prod(), 1 / len(micros)) * (1 + binding_strength))
    unified_valence = float(np.tanh(valences.mean() * (1 + binding_strength)))
    phi = float(unified_intensity * binding_strength * math_log_norm(len(micros)))

    return MacroExperience(
        mode=CombinationMode.FUSION,
        unified_intensity=unified_intensity,
        unified_valence=unified_valence,
        phi_analog=min(1.0, phi),
        n_micro_units=len(micros),
        is_unified=binding_strength > 0.4 and len(micros) > 1,
        component_ids=[m.component_id for m in micros],
    )


def combine_integration(micros: List[MicroExperience]) -> MacroExperience:
    """IIT-inspired integration — phi from binding graph connectivity."""
    if not micros:
        return MacroExperience(CombinationMode.INTEGRATION, 0, 0, 0, 0, False, [])

    B = binding_matrix(micros)
    n = len(micros)
    connectivity = float(B.sum() / (n * n + 1e-10))
    mean_intensity = float(np.mean([m.phenomenal_magnitude for m in micros]))
    irreducibility = 1.0 - (1.0 / (1.0 + connectivity * n))
    phi = float(np.clip(connectivity * mean_intensity * irreducibility * (1 + 0.1 * n), 0, 1))

    return MacroExperience(
        mode=CombinationMode.INTEGRATION,
        unified_intensity=min(1.0, mean_intensity * (1 + connectivity)),
        unified_valence=float(np.mean([m.valence for m in micros])),
        phi_analog=phi,
        n_micro_units=n,
        is_unified=connectivity > 0.3 and phi > 0.2,
        component_ids=[m.component_id for m in micros],
    )


def build_sample_components(n: int = 5) -> List[ProblemComponent]:
    """Sample ProblemComponents with interdependencies for simulation."""
    components = []
    for i in range(n):
        deps = [f"comp_{j}" for j in range(max(0, i - 1), i)]
        components.append(
            ProblemComponent(
                id=f"comp_{i}",
                description=f"Proto-experiential unit {i}",
                complexity=0.3 + 0.1 * i,
                consciousness_level=0.2 + 0.15 * i,
                interdependencies=deps,
                emergent_properties=[f"property_{i}"] if i > 0 else [],
                transformation_potential=0.4 + 0.1 * i,
            )
        )
    return components


def run_combination_experiment(n_components: int = 6) -> Dict:
    components = build_sample_components(n_components)
    micros = [problem_component_to_micro(c) for c in components]

    results = {
        CombinationMode.SUMMING.value: asdict(combine_summing(micros)),
        CombinationMode.FUSION.value: asdict(combine_fusion(micros)),
        CombinationMode.INTEGRATION.value: asdict(combine_integration(micros)),
    }

    summing_phi = results["summing"]["phi_analog"]
    fusion_phi = results["fusion"]["phi_analog"]
    integration_phi = results["integration"]["phi_analog"]

    interpretation = {
        "axiom_a4": "Composition via integration/fusion, not emergence ex nihilo",
        "finding": (
            f"Integration phi={integration_phi:.4f}, fusion phi={fusion_phi:.4f}, "
            f"summing phi={summing_phi:.4f}"
        ),
        "unity_achieved": {
            "summing": results["summing"]["is_unified"],
            "fusion": results["fusion"]["is_unified"],
            "integration": results["integration"]["is_unified"],
        },
        "panpsychism_prediction": (
            "Fusion and integration modes produce unified macro-experience; "
            "naive summing does not — supports combination problem solutions"
        ),
        "caveat": "Computational model only; does not detect real phenomenal unity",
    }
    interpretation["combination_status"] = (
        "supported_in_silico"
        if integration_phi >= summing_phi and fusion_phi >= summing_phi
        else "mixed"
    )

    output = {
        "experiment": "combination_model",
        "n_components": n_components,
        "micro_units": [asdict(m) for m in micros],
        "macro_by_mode": results,
        "interpretation": interpretation,
    }

    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Combination experiment complete. Results: {OUTPUT_PATH}")
    for mode, macro in results.items():
        print(f"  {mode:14s} phi={macro['phi_analog']:.4f} unified={macro['is_unified']}")
    return output


def scaling_experiment(max_n: int = 10) -> List[Dict]:
    scaling = []
    for n in range(2, max_n + 1):
        components = build_sample_components(n)
        micros = [problem_component_to_micro(c) for c in components]
        macro = combine_integration(micros)
        scaling.append({"n_micro": n, "phi_analog": macro.phi_analog, "is_unified": macro.is_unified})
    return scaling


if __name__ == "__main__":
    print("=" * 60)
    print("Combination Model: Micro-experiential integration")
    print("=" * 60)
    run_combination_experiment(n_components=6)
    print("\nScaling (integration mode):")
    for row in scaling_experiment(8):
        print(f"  n={row['n_micro']}  phi={row['phi_analog']:.4f}  unified={row['is_unified']}")
