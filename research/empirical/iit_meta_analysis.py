"""
IIT Meta-Analysis: Phi-analog computation across network substrates.

Tier 1 desk research + Tier 2 computational experiment for Predictions P1 and P5.
Computes integration metrics on tractable network architectures without claiming
to measure real phenomenal consciousness.

Uses a simplified Phi-analog (effective information / integration proxy) when pyphi
is unavailable. Optional pyphi integration for small systems.

Run: python research/empirical/iit_meta_analysis.py
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

OUTPUT_PATH = Path(__file__).resolve().parent / "iit_meta_analysis_results.json"

try:
    import pyphi
    PYPHI_AVAILABLE = True
except ImportError:
    PYPHI_AVAILABLE = False


class SubstrateType(str, Enum):
    RANDOM = "random"
    FEEDFORWARD = "feedforward"
    RECURRENT = "recurrent"
    INTEGRATED = "integrated"
    MODULAR = "modular"


@dataclass
class NetworkResult:
    substrate: str
    n_nodes: int
    phi_analog: float
    integration_ratio: float
    recurrence_strength: float
    notes: str


def _transition_matrix_from_weights(W: np.ndarray, noise: float = 0.05) -> np.ndarray:
    """Build row-stochastic TPM from connectivity weights."""
    n = W.shape[0]
    tpm = np.zeros((n, 2**n, 2**n))
    states = [format(i, f"0{n}b") for i in range(2**n)]

    for i, state in enumerate(states):
        current = np.array([int(b) for b in state], dtype=float)
        drive = W @ current + np.random.randn(n) * noise
        probs = 1 / (1 + np.exp(-drive))
        next_state = (probs > 0.5).astype(int)
        next_idx = int("".join(str(b) for b in next_state), 2)
        tpm[i, i, next_idx] = 1.0 - noise
        tpm[i, next_idx, next_idx] += noise
        row_sum = tpm[i].sum(axis=1, keepdims=True)
        row_sum[row_sum == 0] = 1
        tpm[i] = tpm[i] / row_sum
    return tpm


def build_connectivity(substrate: SubstrateType, n: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    W = np.zeros((n, n))

    if substrate == SubstrateType.RANDOM:
        W = rng.uniform(0, 0.3, (n, n))
        np.fill_diagonal(W, 0)

    elif substrate == SubstrateType.FEEDFORWARD:
        for i in range(n - 1):
            W[i + 1, i] = rng.uniform(0.5, 1.0)

    elif substrate == SubstrateType.RECURRENT:
        for i in range(n - 1):
            W[i + 1, i] = rng.uniform(0.5, 1.0)
            W[i, i + 1] = rng.uniform(0.3, 0.7)
        np.fill_diagonal(W, rng.uniform(0.2, 0.5, n))

    elif substrate == SubstrateType.INTEGRATED:
        W = rng.uniform(0.3, 0.8, (n, n))
        np.fill_diagonal(W, rng.uniform(0.4, 0.9, n))

    elif substrate == SubstrateType.MODULAR:
        half = n // 2
        W[:half, :half] = rng.uniform(0.5, 1.0, (half, half))
        W[half:, half:] = rng.uniform(0.5, 1.0, (n - half, n - half))
        W[:half, half:] = rng.uniform(0.01, 0.1, (half, n - half))
        W[half:, :half] = rng.uniform(0.01, 0.1, (n - half, half))
        np.fill_diagonal(W, 0)

    return W


def phi_analog_effective_information(W: np.ndarray) -> float:
    """
    Simplified integration proxy: mutual constraint across bipartitions.
    Higher when system is recurrent and globally coupled.
    Not formal IIT phi — labeled as analog.
    """
    n = W.shape[0]
    if n < 2:
        return 0.0

    total_weight = W.sum() + 1e-10
    out_degree = W.sum(axis=1)
    in_degree = W.sum(axis=0)
    balance = 1.0 - np.std(out_degree + in_degree) / (np.mean(out_degree + in_degree) + 1e-10)

    recurrence = np.trace(W) + (W * W.T).sum() * 0.5
    recurrence_norm = recurrence / (total_weight + 1e-10)

    mid = n // 2
    cross = W[:mid, mid:].sum() + W[mid:, :mid].sum()
    cross_ratio = cross / (total_weight + 1e-10)

    integration = balance * 0.3 + recurrence_norm * 0.4 + cross_ratio * 0.3
    return float(np.clip(integration, 0.0, 1.0))


def compute_pyphi_phi(n: int, seed: int = 42) -> Optional[float]:
    """Compute formal phi for small networks if pyphi available."""
    if not PYPHI_AVAILABLE or n > 4:
        return None
    W = build_connectivity(SubstrateType.INTEGRATED, n, seed)
    tpm = _transition_matrix_from_weights(W * 0.5)
    network = pyphi.Network(tpm, node_labels=tuple(str(i) for i in range(n)))
    state = tuple([0] * n)
    subsystem = pyphi.Subsystem(network, state)
    phi = pyphi.compute.phi(subsystem)
    return float(phi)


def recurrence_strength(W: np.ndarray) -> float:
    sym = (W + W.T) / 2
    return float(sym.sum() / (W.sum() + 1e-10))


def analyze_substrate(substrate: SubstrateType, n_nodes: int = 8, seed: int = 42) -> NetworkResult:
    W = build_connectivity(substrate, n_nodes, seed)
    phi_a = phi_analog_effective_information(W)
    recurrence = recurrence_strength(W)

    total = W.sum() + 1e-10
    mid = n_nodes // 2
    internal = W[:mid, :mid].sum() + W[mid:, mid:].sum()
    integration_ratio = float(internal / total)

    notes = f"n={n_nodes}, seed={seed}"
    if PYPHI_AVAILABLE and n_nodes <= 4:
        formal = compute_pyphi_phi(min(n_nodes, 4), seed)
        if formal is not None:
            notes += f", pyphi_phi={formal:.4f}"

    return NetworkResult(
        substrate=substrate.value,
        n_nodes=n_nodes,
        phi_analog=round(phi_a, 4),
        integration_ratio=round(integration_ratio, 4),
        recurrence_strength=round(recurrence, 4),
        notes=notes,
    )


def run_meta_analysis(
    n_nodes: int = 8,
    n_seeds: int = 5,
) -> Dict:
    """Compare phi-analog across substrate types — tests P1/P5 substrate neutrality."""
    results: List[NetworkResult] = []

    for substrate in SubstrateType:
        seed_results = []
        for seed in range(n_seeds):
            r = analyze_substrate(substrate, n_nodes, seed=42 + seed)
            seed_results.append(r)
            results.append(r)

        avg_phi = np.mean([r.phi_analog for r in seed_results])
        print(f"{substrate.value:14s}  avg_phi_analog={avg_phi:.4f}  (n_seeds={n_seeds})")

    ranked = sorted(
        {(s.value): np.mean([r.phi_analog for r in results if r.substrate == s.value]) for s in SubstrateType}.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    interpretation = {
        "prediction_p1": "Integrated/recurrent architectures should show higher phi-analog",
        "prediction_p5": "Non-biological network topologies can achieve high integration",
        "finding": f"Highest phi-analog: {ranked[0][0]} ({ranked[0][1]:.4f}); lowest: {ranked[-1][0]} ({ranked[-1][1]:.4f})",
        "panpsychism_relevance": (
            "Supports substrate-neutral integration if recurrent/integrated topologies "
            "score highest regardless of biological implementation"
        ),
        "caveat": "Phi-analog is a proxy, not formal IIT phi or phenomenal consciousness",
        "pyphi_available": PYPHI_AVAILABLE,
    }

    if ranked[0][0] in ("integrated", "recurrent") and ranked[-1][0] in ("feedforward", "random", "modular"):
        interpretation["p1_status"] = "supported_in_silico"
    else:
        interpretation["p1_status"] = "mixed"

    output = {
        "meta_analysis": "iit_phi_analog_substrate_comparison",
        "n_nodes": n_nodes,
        "n_seeds": n_seeds,
        "results": [asdict(r) for r in results],
        "ranked_substrates": [{"substrate": s, "avg_phi_analog": round(v, 4)} for s, v in ranked],
        "interpretation": interpretation,
    }

    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"\nResults written to {OUTPUT_PATH}")
    return output


def compare_node_scaling() -> List[Dict]:
    """Phi-analog vs network size for integrated architecture."""
    scaling = []
    for n in [4, 6, 8, 10, 12]:
        r = analyze_substrate(SubstrateType.INTEGRATED, n, seed=42)
        scaling.append({"n_nodes": n, "phi_analog": r.phi_analog})
    return scaling


if __name__ == "__main__":
    print("=" * 60)
    print("IIT Meta-Analysis: Phi-analog across substrates")
    print(f"pyphi available: {PYPHI_AVAILABLE}")
    print("=" * 60)
    run_meta_analysis(n_nodes=8, n_seeds=5)
    print("\nNode scaling (integrated):")
    for row in compare_node_scaling():
        print(f"  n={row['n_nodes']:2d}  phi_analog={row['phi_analog']:.4f}")
