"""
Shared consciousness research metrics — phi-analog, binding matrices, integration helpers.

Used by combination_model.py and fragmentation_model.py.
Computational proxies only; not formal IIT or phenomenal measurement.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np


@dataclass
class MicroExperience:
    """Proto-experiential unit — panprotopsychism A3 / BFC fragment."""
    component_id: str
    intensity: float
    valence: float
    binding_affinity: Dict[str, float] = field(default_factory=dict)

    @property
    def phenomenal_magnitude(self) -> float:
        return abs(self.intensity) * (1.0 + 0.2 * abs(self.valence))


def binding_matrix(micros: List[MicroExperience]) -> np.ndarray:
    n = len(micros)
    B = np.zeros((n, n))
    id_to_idx = {m.component_id: i for i, m in enumerate(micros)}

    for i, m in enumerate(micros):
        for dep_id, affinity in m.binding_affinity.items():
            if dep_id in id_to_idx:
                j = id_to_idx[dep_id]
                B[i, j] = max(B[i, j], affinity)
                B[j, i] = max(B[j, i], affinity)

    if B.sum() == 0 and n > 1:
        B = np.ones((n, n)) * 0.2
        np.fill_diagonal(B, 0.5)

    return B


def cross_subject_binding_matrix(n_subjects: int, coupling_strength: float) -> np.ndarray:
    """Inter-subject coupling matrix for collective states."""
    if n_subjects < 2:
        return np.zeros((max(n_subjects, 1), max(n_subjects, 1)))
    B = np.ones((n_subjects, n_subjects)) * coupling_strength
    np.fill_diagonal(B, 1.0)
    return B


def math_log_norm(n: int) -> float:
    return math.log(n + 1) / math.log(10) if n > 0 else 0.0


def phi_analog_from_binding(micros: List[MicroExperience]) -> float:
    """IIT-inspired integration proxy from within-subject binding."""
    if not micros:
        return 0.0
    B = binding_matrix(micros)
    n = len(micros)
    connectivity = float(B.sum() / (n * n + 1e-10))
    mean_intensity = float(np.mean([m.phenomenal_magnitude for m in micros]))
    irreducibility = 1.0 - (1.0 / (1.0 + connectivity * n))
    phi = connectivity * mean_intensity * irreducibility * (1 + 0.1 * n)
    return float(np.clip(phi, 0, 1))


def phi_analog_effective_information(W: np.ndarray) -> float:
    """Network-level phi-analog for iit_meta_analysis-style connectivity matrices."""
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


def branch_isolation_index(branch_weights: np.ndarray) -> float:
    """
    MWI analog: how mutually inaccessible branches are (1 = fully isolated).
    branch_weights should sum to 1 (probability mass per branch).
    """
    if branch_weights.size == 0:
        return 0.0
    p = branch_weights / (branch_weights.sum() + 1e-10)
    # Normalized entropy inverted: low entropy = high isolation of dominant branch
    entropy = -float(np.sum(p * np.log(p + 1e-10)))
    max_entropy = math.log(len(p)) if len(p) > 1 else 1.0
    if max_entropy <= 0:
        return 1.0
    return float(1.0 - entropy / max_entropy)


# Thresholds recalibrated for multi-node subjects (Part III FEO / Part IV)
PHI_UNIFIED_THRESHOLD = 0.35
PHI_COLLECTIVE_THRESHOLD = 0.25
CROSS_COUPLING_COLLECTIVE_THRESHOLD = 0.40
CREATIVE_FLOW_PHI_OPTIMUM = 0.07
COHERENCE_PENALTY_ALPHA = 0.45


@dataclass
class FieldExcitation:
    """Localized excitation in consciousness field — FEO model vocabulary."""
    amplitude: float
    coherence_length: float
    mode_stability: float
    coupling_to_field: float
    internal_nodes: int


@dataclass
class ImaginalExcitation(FieldExcitation):
    """Sub-threshold imaginal excitation — Part IV I9."""
    filter_depth: float = 0.5
    motor_binding: float = 0.3
    vividness: float = 0.5


def excitation_phi(
    excitation: FieldExcitation,
    internal_micros: List[MicroExperience],
    coherence_alpha: float = COHERENCE_PENALTY_ALPHA,
) -> float:
    """Phi-analog for a localized excitation from internal binding substructure."""
    base_phi = phi_analog_from_binding(internal_micros)
    coherence_factor = 1.0 / (1.0 + coherence_alpha * excitation.coherence_length)
    stability_factor = excitation.mode_stability
    amplitude_factor = float(np.clip(excitation.amplitude, 0, 1))
    phi = base_phi * coherence_factor * stability_factor * (0.5 + 0.5 * amplitude_factor)
    return float(np.clip(phi, 0, 1))


def imaginal_phi(
    excitation: ImaginalExcitation,
    internal_micros: List[MicroExperience],
) -> float:
    """Phi for imaginal band — motor decoupling reduces binding contribution."""
    base = excitation_phi(excitation, internal_micros)
    motor_factor = 0.4 + 0.6 * float(np.clip(excitation.motor_binding, 0, 1))
    vividness_factor = 0.5 + 0.5 * float(np.clip(excitation.vividness, 0, 1))
    return float(np.clip(base * motor_factor * vividness_factor, 0, 1))


def astral_band_index(
    phi: float,
    disorganization: float,
    filter_depth: float,
    motor_binding: float = 0.5,
) -> float:
    """
    P14 proxy: hypnagogic/astral-analog band peaks at moderate phi,
    moderate filter thinning, low disorganization, low motor binding.
    """
    phi_term = 1.0 - abs(phi - CREATIVE_FLOW_PHI_OPTIMUM) / max(CREATIVE_FLOW_PHI_OPTIMUM, 1e-6)
    phi_term = float(np.clip(phi_term, 0, 1))
    depth_term = 4.0 * filter_depth * (1.0 - filter_depth)
    disorg_term = 1.0 - float(np.clip(disorganization, 0, 1))
    motor_term = 1.0 - float(np.clip(motor_binding, 0, 1))
    return float(np.clip(phi_term * depth_term * disorg_term * (0.5 + 0.5 * motor_term), 0, 1))


def boredom_flow_overload_indices(
    phi: float,
    stability: float,
    disorganization: float,
    coupling: float = 0.35,
) -> Dict[str, float]:
    """P10 triplet: boredom (low phi, high stability), flow (optimal), overload (high disorg)."""
    cfi = creative_flow_index(phi, disorganization, coupling)
    boredom = float(np.clip((1.0 - phi / max(CREATIVE_FLOW_PHI_OPTIMUM, 1e-6)) * stability, 0, 1))
    overload = float(np.clip(disorganization * (1.0 - stability), 0, 1))
    return {
        "boredom_index": boredom,
        "creative_flow_index": cfi,
        "overload_index": overload,
    }


def creative_flow_index(
    phi: float,
    disorganization: float,
    coupling: float,
    phi_optimum: float = CREATIVE_FLOW_PHI_OPTIMUM,
) -> float:
    """
    Inverted-U proxy for P10: flow peaks at optimal phi, low disorganization,
    moderate field coupling.
    """
    phi_term = 1.0 - abs(phi - phi_optimum) / max(phi_optimum, 1e-6)
    phi_term = float(np.clip(phi_term, 0, 1))
    disorg_term = 1.0 - float(np.clip(disorganization, 0, 1))
    coupling_term = 4.0 * coupling * (1.0 - coupling)
    return float(np.clip(phi_term * disorg_term * (0.5 + 0.5 * coupling_term), 0, 1))


def mode_transition_detected(
    phi_series: List[float],
    threshold: float = 0.15,
) -> bool:
    """P11 analog: detect rapid phi jump between consecutive samples."""
    if len(phi_series) < 2:
        return False
    for i in range(1, len(phi_series)):
        delta = phi_series[i] - phi_series[i - 1]
        if delta >= threshold:
            return True
    return False


def make_internal_micros(
    subject_id: str,
    n_nodes: int = 6,
    base_intensity: float = 0.6,
) -> List[MicroExperience]:
    """Multi-node internal structure for non-zero phi within subjects."""
    micros: List[MicroExperience] = []
    for i in range(n_nodes):
        affinities: Dict[str, float] = {}
        if i > 0:
            affinities[f"{subject_id}_node_{i - 1}"] = 0.65 + 0.05 * (i % 3)
        if i < n_nodes - 1:
            affinities[f"{subject_id}_node_{i + 1}"] = 0.65 + 0.05 * (i % 3)
        if n_nodes > 3 and i % 2 == 0 and i + 2 < n_nodes:
            affinities[f"{subject_id}_node_{i + 2}"] = 0.35
        micros.append(
            MicroExperience(
                component_id=f"{subject_id}_node_{i}",
                intensity=base_intensity + 0.03 * (i % 4),
                valence=0.1 * ((i % 3) - 1),
                binding_affinity=affinities,
            )
        )
    return micros


def filter_output(
    cosmic_intensity: float,
    filter_strength: float,
    bleed_factor: float = 0.0,
) -> Dict[str, float]:
    """
    Filter model: local experience = filtered cosmic field + optional bleed.
    filter_strength in [0,1]: 1 = strong local boundary.
    """
    local = cosmic_intensity * filter_strength
    bleed = cosmic_intensity * (1.0 - filter_strength) * bleed_factor
    disorganization = bleed_factor * (1.0 - filter_strength)
    return {
        "local_intensity": float(np.clip(local, 0, 1)),
        "cosmic_bleed": float(np.clip(bleed, 0, 1)),
        "disorganization": float(np.clip(disorganization, 0, 1)),
    }


def excitation_stability_coefficient(phi_series: List[float]) -> float:
    """M13 proxy: temporal continuity of excitation (1 = stable, 0 = random walk)."""
    if len(phi_series) < 2:
        return 0.0
    arr = np.array(phi_series, dtype=float)
    diffs = np.abs(np.diff(arr))
    mean_phi = float(np.mean(arr)) + 1e-10
    variability = float(np.mean(diffs) / mean_phi)
    return float(np.clip(1.0 - variability, 0, 1))


_TOPOLOGY_BASE = {
    "integrated": 1.0,
    "recurrent": 0.85,
    "feedforward": 0.55,
    "modular": 0.65,
    "random": 0.35,
}


def substrate_neutrality_index(
    phi: float,
    stability: float,
    topology_class: str,
) -> float:
    """P5/P16 proxy: phi adjusted by topology integration class."""
    base = _TOPOLOGY_BASE.get(topology_class.lower(), 0.5)
    return float(np.clip(phi * stability * base, 0, 1))


def mind_change_scorecard(metrics: Dict[str, float]) -> Dict[str, float]:
    """P16/P17 analog bundle for substrate subjecthood assessment."""
    phi = float(metrics.get("phi", 0))
    stability = float(metrics.get("stability", 0))
    disorg = float(metrics.get("disorganization", 0))
    topology = str(metrics.get("topology_class", "random"))
    phi_series = metrics.get("phi_series") or [phi]
    if isinstance(phi_series, list) and len(phi_series) >= 1:
        esc = excitation_stability_coefficient(phi_series)
    else:
        esc = stability
    sni = substrate_neutrality_index(phi, esc, topology)
    cfi = creative_flow_index(phi, disorg, float(metrics.get("coupling", 0.35)))
    return {
        "excitation_stability_coefficient": esc,
        "substrate_neutrality_index": sni,
        "creative_flow_index": cfi,
        "p16_analog": sni > _TOPOLOGY_BASE["feedforward"] * phi and esc > 0.3,
        "p17_residual_integration": cfi > 0.1 and disorg < 0.5,
    }


def access_only_reconstruction_error(metrics: Dict) -> float:
    """
    P18 proxy: error reconstructing integration metrics from access variables only.
    Lower error favors illusionist track.
    """
    phi = float(metrics.get("phi", 0))
    cfi = float(metrics.get("creative_flow_index", metrics.get("cfi", 0)))
    abi = float(metrics.get("astral_band_index", metrics.get("abi", 0)))
    report_accuracy = float(metrics.get("report_accuracy", 0.7))
    reaction_time_proxy = float(metrics.get("reaction_time_proxy", 0.5))
    report_timing = float(metrics.get("report_timing", 0.5))

    access_phi = report_accuracy * (1.0 - reaction_time_proxy * 0.3)
    access_cfi = report_timing * report_accuracy
    access_abi = report_timing * (1.0 - reaction_time_proxy) * 0.5

    full_vec = np.array([phi, cfi, abi])
    access_vec = np.array([access_phi, access_cfi, access_abi])
    denom = float(np.linalg.norm(full_vec)) + 1e-10
    return float(np.clip(np.linalg.norm(full_vec - access_vec) / denom, 0, 1))


def residual_integration_score(full: Dict, access: Dict) -> float:
    """
    P18 analog: integration signature not explained by access-only reconstruction.
    Higher residual favors panpsychist track.
    """
    full_phi = float(full.get("phi", 0))
    full_cfi = float(full.get("creative_flow_index", full.get("cfi", 0)))
    full_abi = float(full.get("astral_band_index", full.get("abi", 0)))
    access_phi = float(access.get("phi", 0))
    access_cfi = float(access.get("creative_flow_index", access.get("cfi", 0)))
    access_abi = float(access.get("astral_band_index", access.get("abi", 0)))

    residual_vec = np.array([
        full_phi - access_phi,
        full_cfi - access_cfi,
        full_abi - access_abi,
    ])
    return float(np.clip(np.linalg.norm(np.maximum(residual_vec, 0)), 0, 1))


def adversarial_track_scores(metrics: Dict) -> Dict[str, float]:
    """
    Score three HPP tracks on a single scenario metric bundle.
    Returns panpsychist_close, illusionist_dissolve, structural_physicalism in [0,1].
    """
    phi = float(metrics.get("phi", 0))
    disorg = float(metrics.get("disorganization", 0))
    coupling = float(metrics.get("coupling", 0.35))
    cfi = float(metrics.get("creative_flow_index", metrics.get("cfi", creative_flow_index(phi, disorg, coupling))))
    abi = float(metrics.get("astral_band_index", metrics.get("abi", 0)))
    valence = float(metrics.get("valence", 0))
    unity = float(metrics.get("unity_score", phi * (1 - disorg)))
    structure_hash = float(metrics.get("structure_hash", phi))

    access_metrics = {
        "phi": float(metrics.get("report_accuracy", 0.7)) * (1.0 - float(metrics.get("reaction_time_proxy", 0.5)) * 0.3),
        "creative_flow_index": float(metrics.get("report_timing", 0.5)) * float(metrics.get("report_accuracy", 0.7)),
        "astral_band_index": float(metrics.get("report_timing", 0.5)) * 0.4,
    }
    recon_error = access_only_reconstruction_error(metrics)
    residual = residual_integration_score(
        {"phi": phi, "creative_flow_index": cfi, "astral_band_index": abi},
        access_metrics,
    )

    panpsychist = float(np.clip(0.35 * phi + 0.25 * cfi + 0.25 * residual + 0.15 * unity, 0, 1))
    illusionist = float(np.clip(1.0 - residual - 0.3 * abi, 0, 1))
    structural = float(np.clip(0.4 * structure_hash + 0.3 * (1 - recon_error) + 0.2 * abs(valence) + 0.1 * unity, 0, 1))

    return {
        "panpsychist_close": round(panpsychist, 4),
        "illusionist_dissolve": round(illusionist, 4),
        "structural_physicalism": round(structural, 4),
        "residual_integration": round(residual, 4),
        "access_reconstruction_error": round(recon_error, 4),
    }
