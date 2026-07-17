"""
Field Excitation Model: 1D lattice wavepacket scenarios for FEO (Part III).

Scenarios: SOLO_FOCUSED, BOREDOM, CREATIVE_FLOW, OVERLOAD, DUET_IMPROV,
           FILTER_FAILURE, MWI_BRANCH

Run: python research/empirical/field_excitation_model.py
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
    boredom_flow_overload_indices,
    creative_flow_index,
    excitation_phi,
    FieldExcitation,
    make_internal_micros,
    mode_transition_detected,
    phi_analog_from_binding,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "field_excitation_results.json"


class ExcitationScenario(str, Enum):
    SOLO_FOCUSED = "solo_focused"
    BOREDOM = "boredom"
    CREATIVE_FLOW = "creative_flow"
    OVERLOAD = "overload"
    DUET_IMPROV = "duet_improv"
    FILTER_FAILURE = "filter_failure"
    MWI_BRANCH = "mwi_branch"


@dataclass
class WavepacketResult:
    scenario: ExcitationScenario
    peak_amplitude: float
    coherence_length: float
    mode_stability: float
    coupling_to_field: float
    local_phi: float
    creative_flow_index: float
    boredom_index: float
    overload_index: float
    cross_coupling: float
    branch_isolation: float
    disorganization: float
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


def _simulate_field(
    centers: List[float],
    amplitudes: List[float],
    sigmas: List[float],
    well_depth: float = 0.8,
    well_width: float = 2.0,
    noise: float = 0.0,
    grid_size: int = 128,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.linspace(0, 10, grid_size)
    field = np.zeros_like(x)
    for c, a, s in zip(centers, amplitudes, sigmas):
        field += _gaussian_field(x, c, a, s)
    if centers:
        well = sum(_potential_well(x, c, well_depth, well_width) for c in centers)
        field = field * (0.3 + 0.7 * well / (well.max() + 1e-10))
    if noise > 0:
        field += noise * np.random.randn(grid_size)
    field = np.clip(field, 0, None)
    return x, field, x


def _metrics_from_wavepacket(
    amplitude: float,
    sigma: float,
    stability: float,
    coupling: float,
    disorganization: float,
    n_nodes: int,
    subject_id: str,
    cross_coupling: float = 0.0,
    branch_isolation: float = 0.0,
    phi_series: List[float] | None = None,
) -> WavepacketResult:
    micros = make_internal_micros(subject_id, n_nodes=n_nodes, base_intensity=amplitude * 0.9)
    excitation = FieldExcitation(
        amplitude=amplitude,
        coherence_length=sigma,
        mode_stability=stability,
        coupling_to_field=coupling,
        internal_nodes=n_nodes,
    )
    local_phi = excitation_phi(excitation, micros)
    triplet = boredom_flow_overload_indices(local_phi, stability, disorganization, coupling)
    series = phi_series or [local_phi * 0.85, local_phi]
    return WavepacketResult(
        scenario=ExcitationScenario.SOLO_FOCUSED,
        peak_amplitude=float(amplitude),
        coherence_length=float(sigma),
        mode_stability=float(stability),
        coupling_to_field=float(coupling),
        local_phi=float(local_phi),
        creative_flow_index=float(triplet["creative_flow_index"]),
        boredom_index=float(triplet["boredom_index"]),
        overload_index=float(triplet["overload_index"]),
        cross_coupling=float(cross_coupling),
        branch_isolation=float(branch_isolation),
        disorganization=float(disorganization),
        mode_transition=mode_transition_detected(series),
    )


def simulate_solo_focused() -> WavepacketResult:
    _, field, _ = _simulate_field([5.0], [0.85], [0.8], well_depth=0.9)
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=0.8,
        stability=0.85,
        coupling=0.25,
        disorganization=0.05,
        n_nodes=6,
        subject_id="solo_focused",
    )
    r.scenario = ExcitationScenario.SOLO_FOCUSED
    return r


def simulate_boredom() -> WavepacketResult:
    _, field, _ = _simulate_field([5.0], [0.7], [0.5], well_depth=0.95, well_width=1.5)
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=0.5,
        stability=0.92,
        coupling=0.15,
        disorganization=0.03,
        n_nodes=6,
        subject_id="boredom",
    )
    r.scenario = ExcitationScenario.BOREDOM
    return r


def simulate_creative_flow() -> WavepacketResult:
    _, field, _ = _simulate_field([5.0], [0.78], [1.0], well_depth=0.78, well_width=2.2)
    amp = float(field.max())
    micros = make_internal_micros("creative_flow", n_nodes=7, base_intensity=0.72)
    excitation = FieldExcitation(
        amplitude=amp,
        coherence_length=1.0,
        mode_stability=0.78,
        coupling_to_field=0.48,
        internal_nodes=7,
    )
    local_phi = excitation_phi(excitation, micros)
    phi_series = [max(0.01, local_phi * 0.45), local_phi + 0.16]
    r = _metrics_from_wavepacket(
        amplitude=amp,
        sigma=1.0,
        stability=0.78,
        coupling=0.48,
        disorganization=0.08,
        n_nodes=7,
        subject_id="creative_flow",
        phi_series=phi_series,
    )
    r.scenario = ExcitationScenario.CREATIVE_FLOW
    return r


def simulate_overload() -> WavepacketResult:
    _, field, _ = _simulate_field([5.0], [0.82], [0.6], well_depth=0.88, well_width=1.8, noise=0.08)
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=0.6,
        stability=0.55,
        coupling=0.65,
        disorganization=0.45,
        n_nodes=6,
        subject_id="overload",
    )
    r.scenario = ExcitationScenario.OVERLOAD
    return r


def simulate_duet_improv() -> WavepacketResult:
    _, field, _ = _simulate_field(
        [3.5, 6.5], [0.7, 0.7], [1.0, 1.0], well_depth=0.5, well_width=3.0
    )
    overlap = float(field[int(len(field) * 0.45)] / (field.max() + 1e-10))
    cross = float(np.clip(0.55 + overlap * 0.3, 0, 1))
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=1.0,
        stability=0.68,
        coupling=0.55,
        disorganization=0.08,
        n_nodes=6,
        subject_id="duet_improv",
        cross_coupling=cross,
    )
    r.scenario = ExcitationScenario.DUET_IMPROV
    return r


def simulate_filter_failure() -> WavepacketResult:
    np.random.seed(7)
    _, field, _ = _simulate_field(
        [5.0], [0.6], [2.5], well_depth=0.2, well_width=4.0, noise=0.15
    )
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=2.5,
        stability=0.25,
        coupling=0.82,
        disorganization=0.68,
        n_nodes=5,
        subject_id="filter_failure",
    )
    r.scenario = ExcitationScenario.FILTER_FAILURE
    return r


def simulate_mwi_branch() -> WavepacketResult:
    _, field, _ = _simulate_field([3.0, 7.0], [0.65, 0.65], [0.9, 0.9], well_depth=0.85)
    peaks = sorted(field, reverse=True)[:2]
    isolation = float(abs(peaks[0] - peaks[1]) / (peaks[0] + 1e-10)) if len(peaks) >= 2 else 1.0
    r = _metrics_from_wavepacket(
        amplitude=float(field.max()),
        sigma=0.9,
        stability=0.7,
        coupling=0.15,
        disorganization=0.05,
        n_nodes=6,
        subject_id="mwi_branch",
        branch_isolation=isolation,
    )
    r.scenario = ExcitationScenario.MWI_BRANCH
    return r


def _result_to_dict(r: WavepacketResult) -> Dict:
    d = asdict(r)
    d["scenario"] = r.scenario.value
    return d


def run_field_excitation_experiment(seed: int = 42) -> Dict:
    np.random.seed(seed)
    scenarios = {
        ExcitationScenario.SOLO_FOCUSED.value: simulate_solo_focused(),
        ExcitationScenario.BOREDOM.value: simulate_boredom(),
        ExcitationScenario.CREATIVE_FLOW.value: simulate_creative_flow(),
        ExcitationScenario.OVERLOAD.value: simulate_overload(),
        ExcitationScenario.DUET_IMPROV.value: simulate_duet_improv(),
        ExcitationScenario.FILTER_FAILURE.value: simulate_filter_failure(),
        ExcitationScenario.MWI_BRANCH.value: simulate_mwi_branch(),
    }
    results = {k: _result_to_dict(v) for k, v in scenarios.items()}

    flow = results["creative_flow"]
    boredom = results["boredom"]
    overload = results["overload"]
    failure = results["filter_failure"]
    duet = results["duet_improv"]
    focused = results["solo_focused"]

    interpretation = {
        "thesis": "Field Excitation Ontology (FEO)",
        "finding": (
            f"creative_flow_index={flow['creative_flow_index']:.4f} "
            f"boredom={boredom['boredom_index']:.4f} "
            f"overload={overload['overload_index']:.4f}; "
            f"duet cross_coupling={duet['cross_coupling']:.4f}"
        ),
        "p10_analog": (
            flow["creative_flow_index"] > boredom["creative_flow_index"]
            and flow["creative_flow_index"] > overload["creative_flow_index"]
        ),
        "p11_analog": flow["mode_transition"],
        "p12_analog": duet["cross_coupling"] > focused["cross_coupling"],
        "modes_discriminable": (
            flow["creative_flow_index"] > failure["creative_flow_index"]
            and duet["cross_coupling"] > focused["cross_coupling"]
            and failure["disorganization"] > flow["disorganization"]
        ),
        "caveat": "Computational metaphor only; not empirical proof of consciousness field",
    }

    output = {
        "experiment": "field_excitation_model",
        "seed": seed,
        "results_by_scenario": results,
        "interpretation": interpretation,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Field excitation experiment complete. Results: {OUTPUT_PATH}")
    for name, data in results.items():
        print(
            f"  {name:18s} phi={data['local_phi']:.4f} "
            f"cfi={data['creative_flow_index']:.4f} "
            f"cross={data['cross_coupling']:.4f}"
        )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Field Excitation Model: FEO Wavepacket Scenarios")
    print("=" * 60)
    run_field_excitation_experiment()
