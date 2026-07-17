"""
Imaginal Excitation Model: Part IV sub-threshold mode scenarios.

Scenarios: WAKING_PERCEPTION, DAYDREAM, ACTIVE_IMAGINATION, HYPNAGOGIC,
           PATHWORKING, CHAOTIC_TRANCE, FILTER_FAILURE

Run: python research/empirical/imaginal_excitation_model.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    astral_band_index,
    boredom_flow_overload_indices,
    imaginal_phi,
    ImaginalExcitation,
    make_internal_micros,
    mode_transition_detected,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "imaginal_excitation_results.json"


class ImaginalScenario(str, Enum):
    WAKING_PERCEPTION = "waking_perception"
    DAYDREAM = "daydream"
    ACTIVE_IMAGINATION = "active_imagination"
    HYPNAGOGIC = "hypnagogic"
    PATHWORKING = "pathworking"
    CHAOTIC_TRANCE = "chaotic_trance"
    FILTER_FAILURE = "filter_failure"


@dataclass
class ImaginalResult:
    scenario: ImaginalScenario
    local_phi: float
    imaginal_phi: float
    astral_band_index: float
    filter_depth: float
    motor_binding: float
    vividness: float
    disorganization: float
    creative_flow_index: float
    mode_transition: bool


def _gaussian_field(
    x: np.ndarray,
    center: float,
    amplitude: float,
    sigma: float,
) -> np.ndarray:
    return amplitude * np.exp(-0.5 * ((x - center) / max(sigma, 1e-6)) ** 2)


def _potential_well(x: np.ndarray, center: float, depth: float, width: float) -> np.ndarray:
    return depth * np.exp(-0.5 * ((x - center) / max(width, 1e-6)) ** 2)


def _simulate_shallow_well_field(
    amplitude: float,
    sigma: float,
    well_depth: float,
    well_width: float = 2.5,
    noise: float = 0.0,
    grid_size: int = 128,
) -> float:
    x = np.linspace(0, 10, grid_size)
    field = _gaussian_field(x, 5.0, amplitude, sigma)
    well = _potential_well(x, 5.0, well_depth, well_width)
    field = field * (0.25 + 0.75 * well / (well.max() + 1e-10))
    if noise > 0:
        field += noise * np.random.randn(grid_size)
    return float(np.clip(field.max(), 0, 1))


def _build_result(
    scenario: ImaginalScenario,
    amplitude: float,
    sigma: float,
    stability: float,
    coupling: float,
    filter_depth: float,
    motor_binding: float,
    vividness: float,
    disorganization: float,
    subject_id: str,
    n_nodes: int = 6,
    phi_series: List[float] | None = None,
) -> ImaginalResult:
    micros = make_internal_micros(subject_id, n_nodes=n_nodes, base_intensity=amplitude * 0.85)
    excitation = ImaginalExcitation(
        amplitude=amplitude,
        coherence_length=sigma,
        mode_stability=stability,
        coupling_to_field=coupling,
        internal_nodes=n_nodes,
        filter_depth=filter_depth,
        motor_binding=motor_binding,
        vividness=vividness,
    )
    i_phi = imaginal_phi(excitation, micros)
    from research.empirical.consciousness_metrics import excitation_phi
    base_phi = excitation_phi(excitation, micros)
    abi = astral_band_index(i_phi, disorganization, filter_depth, motor_binding)
    triplet = boredom_flow_overload_indices(i_phi, stability, disorganization, coupling)
    series = phi_series or [i_phi * 0.88, i_phi]
    return ImaginalResult(
        scenario=scenario,
        local_phi=float(base_phi),
        imaginal_phi=float(i_phi),
        astral_band_index=float(abi),
        filter_depth=float(filter_depth),
        motor_binding=float(motor_binding),
        vividness=float(vividness),
        disorganization=float(disorganization),
        creative_flow_index=float(triplet["creative_flow_index"]),
        mode_transition=mode_transition_detected(series),
    )


def simulate_waking_perception() -> ImaginalResult:
    amp = _simulate_shallow_well_field(0.88, 0.7, well_depth=0.92, well_width=1.8)
    return _build_result(
        ImaginalScenario.WAKING_PERCEPTION, amp, 0.7, 0.88, 0.22,
        filter_depth=0.15, motor_binding=0.92, vividness=0.75,
        disorganization=0.04, subject_id="waking",
    )


def simulate_daydream() -> ImaginalResult:
    amp = _simulate_shallow_well_field(0.72, 1.1, well_depth=0.65, well_width=2.8)
    return _build_result(
        ImaginalScenario.DAYDREAM, amp, 1.1, 0.72, 0.38,
        filter_depth=0.45, motor_binding=0.35, vividness=0.55,
        disorganization=0.10, subject_id="daydream",
    )


def simulate_active_imagination() -> ImaginalResult:
    amp = _simulate_shallow_well_field(0.76, 1.0, well_depth=0.62, well_width=2.5)
    return _build_result(
        ImaginalScenario.ACTIVE_IMAGINATION, amp, 1.0, 0.76, 0.42,
        filter_depth=0.50, motor_binding=0.18, vividness=0.72,
        disorganization=0.08, subject_id="active_imagination", n_nodes=7,
    )


def simulate_hypnagogic() -> ImaginalResult:
    amp = _simulate_shallow_well_field(0.86, 0.88, well_depth=0.54, well_width=2.8)
    return _build_result(
        ImaginalScenario.HYPNAGOGIC, amp, 0.88, 0.82, 0.44,
        filter_depth=0.50, motor_binding=0.08, vividness=0.92,
        disorganization=0.09, subject_id="hypnagogic", n_nodes=8,
    )


def simulate_pathworking() -> ImaginalResult:
    amp = _simulate_shallow_well_field(0.74, 1.05, well_depth=0.68, well_width=2.4)
    return _build_result(
        ImaginalScenario.PATHWORKING, amp, 1.05, 0.80, 0.40,
        filter_depth=0.46, motor_binding=0.28, vividness=0.78,
        disorganization=0.10, subject_id="pathworking", n_nodes=7,
    )


def simulate_chaotic_trance() -> ImaginalResult:
    np.random.seed(11)
    amp = _simulate_shallow_well_field(0.62, 1.8, well_depth=0.35, well_width=4.0, noise=0.12)
    return _build_result(
        ImaginalScenario.CHAOTIC_TRANCE, amp, 1.8, 0.35, 0.58,
        filter_depth=0.72, motor_binding=0.15, vividness=0.70,
        disorganization=0.52, subject_id="chaotic_trance",
    )


def simulate_filter_failure() -> ImaginalResult:
    np.random.seed(13)
    amp = _simulate_shallow_well_field(0.58, 2.4, well_depth=0.18, well_width=4.5, noise=0.18)
    return _build_result(
        ImaginalScenario.FILTER_FAILURE, amp, 2.4, 0.22, 0.78,
        filter_depth=0.85, motor_binding=0.05, vividness=0.65,
        disorganization=0.70, subject_id="filter_failure",
    )


def _result_to_dict(r: ImaginalResult) -> Dict:
    d = asdict(r)
    d["scenario"] = r.scenario.value
    return d


def run_imaginal_experiment(seed: int = 42) -> Dict:
    np.random.seed(seed)
    scenarios = {
        ImaginalScenario.WAKING_PERCEPTION.value: simulate_waking_perception(),
        ImaginalScenario.DAYDREAM.value: simulate_daydream(),
        ImaginalScenario.ACTIVE_IMAGINATION.value: simulate_active_imagination(),
        ImaginalScenario.HYPNAGOGIC.value: simulate_hypnagogic(),
        ImaginalScenario.PATHWORKING.value: simulate_pathworking(),
        ImaginalScenario.CHAOTIC_TRANCE.value: simulate_chaotic_trance(),
        ImaginalScenario.FILTER_FAILURE.value: simulate_filter_failure(),
    }
    results = {k: _result_to_dict(v) for k, v in scenarios.items()}

    hyp = results["hypnagogic"]
    waking = results["waking_perception"]
    failure = results["filter_failure"]
    path = results["pathworking"]
    chaos = results["chaotic_trance"]

    interpretation = {
        "thesis": "Imaginal Excitation Ontology (IEO)",
        "finding": (
            f"hypnagogic astral_band_index={hyp['astral_band_index']:.4f} "
            f"imaginal_phi={hyp['imaginal_phi']:.4f}; "
            f"pathworking disorg={path['disorganization']:.4f} "
            f"chaotic_trance disorg={chaos['disorganization']:.4f}"
        ),
        "p13_analog": waking["motor_binding"] > results["active_imagination"]["motor_binding"],
        "p14_analog": hyp["astral_band_index"] > waking["astral_band_index"]
            and hyp["astral_band_index"] >= path["astral_band_index"],
        "p15_analog": path["disorganization"] < chaos["disorganization"],
        "modes_discriminable": (
            hyp["astral_band_index"] > failure["astral_band_index"]
            and path["disorganization"] < chaos["disorganization"]
            and failure["disorganization"] > hyp["disorganization"]
        ),
        "caveat": "Computational metaphor only; not empirical proof of astral planes or imaginal entities",
    }

    output = {
        "experiment": "imaginal_excitation_model",
        "seed": seed,
        "results_by_scenario": results,
        "interpretation": interpretation,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Imaginal excitation experiment complete. Results: {OUTPUT_PATH}")
    for name, data in results.items():
        print(
            f"  {name:20s} abi={data['astral_band_index']:.4f} "
            f"phi={data['imaginal_phi']:.4f} "
            f"motor={data['motor_binding']:.2f}"
        )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Imaginal Excitation Model: Part IV Scenarios")
    print("=" * 60)
    run_imaginal_experiment()
