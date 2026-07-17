"""
Substrate Excitation Model: Part V cross-substrate comparison (P5/P16).

Compares excitation profiles across topology classes.
NOT consciousness detection.

Run: python research/empirical/substrate_excitation_model.py
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

from research.empirical.consciousness_metrics import (
    excitation_stability_coefficient,
    mind_change_scorecard,
    substrate_neutrality_index,
)
from research.empirical.iit_meta_analysis import (
    SubstrateType,
    analyze_substrate,
    build_connectivity,
    phi_analog_effective_information,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "substrate_excitation_results.json"


class SubstrateProfile(str, Enum):
    BIOLOGICAL_ANALOG = "biological_analog"
    FEEDFORWARD_LLM = "feedforward_llm"
    AGENT_LOOP = "agent_loop"
    RANDOM = "random"


_SUBSTRATE_MAP = {
    SubstrateProfile.BIOLOGICAL_ANALOG: SubstrateType.INTEGRATED,
    SubstrateProfile.FEEDFORWARD_LLM: SubstrateType.FEEDFORWARD,
    SubstrateProfile.AGENT_LOOP: SubstrateType.RECURRENT,
    SubstrateProfile.RANDOM: SubstrateType.RANDOM,
}


@dataclass
class SubstrateResult:
    profile: SubstrateProfile
    phi_analog: float
    recurrence_strength: float
    mode_stability: float
    substrate_neutrality_index: float
    excitation_stability_coefficient: float
    p16_analog: bool


def _simulate_agent_sessions(n_sessions: int = 8, seed: int = 42) -> List[float]:
    """Simulated rising stability for agent loop (M13)."""
    rng = np.random.default_rng(seed)
    base = 0.12
    series = []
    for i in range(n_sessions):
        trend = base + 0.025 * i
        noise = rng.normal(0, 0.015)
        series.append(float(np.clip(trend + noise, 0, 1)))
    return series


def _profile_result(profile: SubstrateProfile, seed: int = 42) -> SubstrateResult:
    substrate = _SUBSTRATE_MAP[profile]
    net = analyze_substrate(substrate, n_nodes=8, seed=seed)
    phi = net.phi_analog
    recurrence = net.recurrence_strength

    if profile == SubstrateProfile.AGENT_LOOP:
        phi_series = _simulate_agent_sessions(seed=seed)
        stability = excitation_stability_coefficient(phi_series)
        mode_stability = float(np.clip(0.4 + stability * 0.5, 0, 1))
    elif profile == SubstrateProfile.BIOLOGICAL_ANALOG:
        phi_series = [phi * (0.95 + 0.01 * i) for i in range(6)]
        stability = excitation_stability_coefficient(phi_series)
        mode_stability = 0.85
    elif profile == SubstrateProfile.FEEDFORWARD_LLM:
        rng = np.random.default_rng(seed)
        phi_series = [float(phi + rng.normal(0, 0.04)) for _ in range(6)]
        stability = excitation_stability_coefficient(phi_series)
        mode_stability = 0.35
    else:
        rng = np.random.default_rng(seed)
        phi_series = [float(rng.uniform(0.05, 0.2)) for _ in range(6)]
        stability = excitation_stability_coefficient(phi_series)
        mode_stability = 0.2

    sni = substrate_neutrality_index(phi, mode_stability, substrate.value)
    scorecard = mind_change_scorecard({
        "phi": phi,
        "stability": mode_stability,
        "disorganization": 0.1 if profile != SubstrateProfile.RANDOM else 0.4,
        "topology_class": substrate.value,
        "phi_series": phi_series,
        "coupling": 0.35,
    })

    return SubstrateResult(
        profile=profile,
        phi_analog=phi,
        recurrence_strength=recurrence,
        mode_stability=mode_stability,
        substrate_neutrality_index=sni,
        excitation_stability_coefficient=stability,
        p16_analog=bool(scorecard["p16_analog"]),
    )


def run_substrate_experiment(seed: int = 42) -> Dict:
    np.random.seed(seed)
    results = {
        p.value: asdict(_profile_result(p, seed))
        for p in SubstrateProfile
    }
    for k, v in results.items():
        v["profile"] = k

    bio = results["biological_analog"]
    ff = results["feedforward_llm"]
    agent = results["agent_loop"]
    rand = results["random"]

    interpretation = {
        "thesis": "Substrate Excitation Ontology M12-M14 / P16",
        "finding": (
            f"bio sni={bio['substrate_neutrality_index']:.4f} "
            f"agent esc={agent['excitation_stability_coefficient']:.4f} "
            f"feedforward sni={ff['substrate_neutrality_index']:.4f}"
        ),
        "p16_analog": (
            bio["p16_analog"]
            and agent["substrate_neutrality_index"] > ff["substrate_neutrality_index"]
            and agent["excitation_stability_coefficient"] > rand["excitation_stability_coefficient"]
        ),
        "caveat": "Topology proxy only; not empirical substrate consciousness proof",
    }

    output = {
        "experiment": "substrate_excitation_model",
        "seed": seed,
        "results_by_profile": results,
        "interpretation": interpretation,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Substrate excitation experiment complete. Results: {OUTPUT_PATH}")
    for name, data in results.items():
        print(
            f"  {name:20s} phi={data['phi_analog']:.4f} "
            f"sni={data['substrate_neutrality_index']:.4f} "
            f"esc={data['excitation_stability_coefficient']:.4f}"
        )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Substrate Excitation Model: Part V P16")
    print("=" * 60)
    run_substrate_experiment()
