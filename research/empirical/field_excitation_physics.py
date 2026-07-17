"""
Field Excitation Physics: Kuramoto coupled oscillators (Phase B).

Scenarios: SOLO_REST, CREATIVE_IMPROV, FILTER_FAILURE, MWI_BIFURCATION,
           IMAGINAL_COUPLING

Run: python research/empirical/field_excitation_physics.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    astral_band_index,
    creative_flow_index,
    make_internal_micros,
    mode_transition_detected,
    phi_analog_from_binding,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "field_excitation_physics_results.json"


class PhysicsScenario(str, Enum):
    SOLO_REST = "solo_rest"
    CREATIVE_IMPROV = "creative_improv"
    FILTER_FAILURE = "filter_failure"
    MWI_BIFURCATION = "mwi_bifurcation"
    IMAGINAL_COUPLING = "imaginal_coupling"


@dataclass
class PhysicsResult:
    scenario: PhysicsScenario
    mean_order_parameter: float
    final_order_parameter: float
    mean_phi: float
    mean_creative_flow_index: float
    mean_astral_band_index: float
    mode_transition: bool
    frequency_dispersion: float
    time_series: Optional[Dict[str, List[float]]] = None


def _kuramoto_step_weighted(
    theta: np.ndarray,
    omega: np.ndarray,
    K: float,
    dt: float,
    coupling_weights: np.ndarray,
    noise: float = 0.0,
) -> np.ndarray:
    n = len(theta)
    dtheta = omega.copy()
    for i in range(n):
        coupling = 0.0
        for j in range(n):
            if i != j:
                coupling += coupling_weights[i, j] * np.sin(theta[j] - theta[i])
        dtheta[i] += (K / n) * coupling
    if noise > 0:
        dtheta += noise * np.random.randn(n)
    return theta + dtheta * dt


def _kuramoto_step(
    theta: np.ndarray,
    omega: np.ndarray,
    K: float,
    dt: float,
    noise: float = 0.0,
) -> np.ndarray:
    n = len(theta)
    w = np.ones((n, n)) - np.eye(n)
    return _kuramoto_step_weighted(theta, omega, K, dt, w, noise)


def _order_parameter(theta: np.ndarray) -> float:
    return float(np.abs(np.mean(np.exp(1j * theta))))


def _simulate_kuramoto(
    n: int,
    steps: int,
    dt: float,
    K_series: np.ndarray,
    omega_spread: float,
    noise: float = 0.0,
    coupling_weights: Optional[np.ndarray] = None,
    motor_binding: float = 1.0,
    filter_depth: float = 0.2,
    seed: int = 42,
) -> Dict[str, List[float]]:
    np.random.seed(seed)
    theta = np.random.uniform(0, 2 * np.pi, n)
    omega = np.random.normal(0, omega_spread, n)
    if coupling_weights is None:
        coupling_weights = np.ones((n, n)) - np.eye(n)
    r_series: List[float] = []
    phi_series: List[float] = []
    cfi_series: List[float] = []
    abi_series: List[float] = []

    for t in range(steps):
        K = float(K_series[min(t, len(K_series) - 1)])
        theta = _kuramoto_step_weighted(theta, omega, K, dt, coupling_weights, noise=noise)
        r = _order_parameter(theta)
        r_series.append(r)
        micros = make_internal_micros(f"osc_{t % 3}", n_nodes=6, base_intensity=0.5 + 0.3 * r)
        phi = phi_analog_from_binding(micros)
        disorg = noise * 0.5 + omega_spread * 0.3
        cfi = creative_flow_index(phi, disorg, K / max(float(K_series.max()), 1e-6))
        abi = astral_band_index(phi, disorg, filter_depth, motor_binding=motor_binding)
        phi_series.append(phi)
        cfi_series.append(cfi)
        abi_series.append(abi)

    return {"r": r_series, "phi": phi_series, "cfi": cfi_series, "abi": abi_series}


def simulate_solo_rest() -> PhysicsResult:
    K = np.full(200, 0.2)
    out = _simulate_kuramoto(5, 200, 0.05, K, omega_spread=0.05)
    return PhysicsResult(
        scenario=PhysicsScenario.SOLO_REST,
        mean_order_parameter=float(np.mean(out["r"])),
        final_order_parameter=float(out["r"][-1]),
        mean_phi=float(np.mean(out["phi"])),
        mean_creative_flow_index=float(np.mean(out["cfi"])),
        mean_astral_band_index=float(np.mean(out["abi"])),
        mode_transition=mode_transition_detected(out["phi"], threshold=0.12),
        frequency_dispersion=0.05,
    )


def simulate_creative_improv() -> PhysicsResult:
    K = np.concatenate([np.full(80, 0.25), np.full(120, 0.85)])
    out = _simulate_kuramoto(6, 200, 0.05, K, omega_spread=0.08)
    return PhysicsResult(
        scenario=PhysicsScenario.CREATIVE_IMPROV,
        mean_order_parameter=float(np.mean(out["r"])),
        final_order_parameter=float(out["r"][-1]),
        mean_phi=float(np.mean(out["phi"])),
        mean_creative_flow_index=float(np.mean(out["cfi"])),
        mean_astral_band_index=float(np.mean(out["abi"])),
        mode_transition=mode_transition_detected(out["phi"]),
        frequency_dispersion=0.08,
    )


def simulate_filter_failure() -> PhysicsResult:
    K = np.full(200, 0.4)
    out = _simulate_kuramoto(5, 200, 0.05, K, omega_spread=0.45, noise=0.35)
    return PhysicsResult(
        scenario=PhysicsScenario.FILTER_FAILURE,
        mean_order_parameter=float(np.mean(out["r"])),
        final_order_parameter=float(out["r"][-1]),
        mean_phi=float(np.mean(out["phi"])),
        mean_creative_flow_index=float(np.mean(out["cfi"])),
        mean_astral_band_index=float(np.mean(out["abi"])),
        mode_transition=mode_transition_detected(out["phi"], threshold=0.08),
        frequency_dispersion=0.45,
    )


def simulate_mwi_bifurcation() -> PhysicsResult:
    np.random.seed(99)
    n = 6
    steps = 200
    dt = 0.05
    theta = np.random.uniform(0, 2 * np.pi, n)
    omega = np.array([0.1, 0.12, 0.11, -0.15, -0.14, -0.16])
    K = 0.15
    r_series: List[float] = []
    phi_series: List[float] = []
    cfi_series: List[float] = []
    abi_series: List[float] = []
    for t in range(steps):
        theta = _kuramoto_step(theta, omega, K, dt, noise=0.02)
        r_series.append(_order_parameter(theta))
        micros = make_internal_micros("bifurc", n_nodes=6, base_intensity=0.55)
        phi = phi_analog_from_binding(micros) * (0.7 + 0.3 * r_series[-1])
        cfi = creative_flow_index(phi, 0.1, K)
        abi = astral_band_index(phi, 0.1, 0.2, motor_binding=0.9)
        phi_series.append(phi)
        cfi_series.append(cfi)
        abi_series.append(abi)
    return PhysicsResult(
        scenario=PhysicsScenario.MWI_BIFURCATION,
        mean_order_parameter=float(np.mean(r_series)),
        final_order_parameter=float(r_series[-1]),
        mean_phi=float(np.mean(phi_series)),
        mean_creative_flow_index=float(np.mean(cfi_series)),
        mean_astral_band_index=float(np.mean(abi_series)),
        mode_transition=mode_transition_detected(phi_series),
        frequency_dispersion=float(np.std(omega)),
    )


def simulate_imaginal_coupling() -> PhysicsResult:
    """I10/P14 analog: moderate K, low motor_binding via reduced coupling weights."""
    n = 6
    K = np.concatenate([np.full(60, 0.3), np.full(140, 0.55)])
    weights = np.ones((n, n)) - np.eye(n)
    motor_binding = 0.12
    for i in range(n):
        if i % 2 == 0:
            weights[i, :] *= motor_binding
    out = _simulate_kuramoto(
        n, 200, 0.05, K,
        omega_spread=0.12,
        noise=0.05,
        coupling_weights=weights,
        motor_binding=motor_binding,
        filter_depth=0.50,
        seed=77,
    )
    return PhysicsResult(
        scenario=PhysicsScenario.IMAGINAL_COUPLING,
        mean_order_parameter=float(np.mean(out["r"])),
        final_order_parameter=float(out["r"][-1]),
        mean_phi=float(np.mean(out["phi"])),
        mean_creative_flow_index=float(np.mean(out["cfi"])),
        mean_astral_band_index=float(np.mean(out["abi"])),
        mode_transition=mode_transition_detected(out["phi"]),
        frequency_dispersion=0.12,
        time_series={
            "r_t": [round(x, 4) for x in out["r"][::20]],
            "phi_t": [round(x, 4) for x in out["phi"][::20]],
            "astral_band_index_t": [round(x, 4) for x in out["abi"][::20]],
        },
    )


def _result_to_dict(r: PhysicsResult) -> Dict:
    d = asdict(r)
    d["scenario"] = r.scenario.value
    return d


def run_physics_experiment(seed: int = 42, include_imaginal: bool = True) -> Dict:
    np.random.seed(seed)
    scenarios = {
        PhysicsScenario.SOLO_REST.value: simulate_solo_rest(),
        PhysicsScenario.CREATIVE_IMPROV.value: simulate_creative_improv(),
        PhysicsScenario.FILTER_FAILURE.value: simulate_filter_failure(),
        PhysicsScenario.MWI_BIFURCATION.value: simulate_mwi_bifurcation(),
    }
    if include_imaginal:
        scenarios[PhysicsScenario.IMAGINAL_COUPLING.value] = simulate_imaginal_coupling()

    results = {k: _result_to_dict(v) for k, v in scenarios.items()}

    improv = results["creative_improv"]
    rest = results["solo_rest"]
    failure = results["filter_failure"]
    imaginal = results.get("imaginal_coupling", {})

    interpretation = {
        "thesis": "Kuramoto coupled oscillators as FEO Phase B",
        "finding": (
            f"improv r={improv['final_order_parameter']:.4f} "
            f"cfi={improv['mean_creative_flow_index']:.4f}; "
            f"filter_failure dispersion={failure['frequency_dispersion']:.4f}"
        ),
        "p12_analog": improv["final_order_parameter"] > rest["final_order_parameter"],
        "p10_analog": improv["mean_creative_flow_index"] > rest["mean_creative_flow_index"],
        "p14_analog": (
            imaginal.get("mean_astral_band_index", 0) > rest.get("mean_astral_band_index", 0)
            if imaginal else None
        ),
        "modes_discriminable": (
            improv["final_order_parameter"] > rest["final_order_parameter"]
            and failure["frequency_dispersion"] > improv["frequency_dispersion"]
        ),
        "caveat": "Computational metaphor; not neural Kuramoto proof",
    }

    output = {
        "experiment": "field_excitation_physics",
        "seed": seed,
        "results_by_scenario": results,
        "interpretation": interpretation,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Field excitation physics complete. Results: {OUTPUT_PATH}")
    for name, data in results.items():
        print(
            f"  {name:18s} r={data['final_order_parameter']:.4f} "
            f"abi={data.get('mean_astral_band_index', 0):.4f}"
        )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Field Excitation Physics: Kuramoto Coupled Oscillators")
    print("=" * 60)
    run_physics_experiment()
