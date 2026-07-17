"""
Fragmentation Model: Cosmopsychism, MWI branching, and collective coupling.

Extends combination_model with BFC modes:
  FRAGMENTATION, BRANCHING, COLLECTIVE_COUPLING, FILTER_FAILURE

Models research hypotheses — NOT detection of real cosmic or branch experience.

Run: python research/empirical/fragmentation_model.py
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
    CROSS_COUPLING_COLLECTIVE_THRESHOLD,
    PHI_COLLECTIVE_THRESHOLD,
    PHI_UNIFIED_THRESHOLD,
    branch_isolation_index,
    cross_subject_binding_matrix,
    filter_output,
    make_internal_micros,
    phi_analog_from_binding,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "fragmentation_model_results.json"
DEFAULT_INTERNAL_NODES = 6


class FragmentationMode(str, Enum):
    FRAGMENTATION = "fragmentation"
    BRANCHING = "branching"
    COLLECTIVE_COUPLING = "collective_coupling"
    FILTER_FAILURE = "filter_failure"


@dataclass
class SubjectState:
    subject_id: str
    local_phi: float
    filter_strength: float
    local_intensity: float
    cosmic_bleed: float
    is_unified: bool
    internal_nodes: int


@dataclass
class FragmentationResult:
    mode: FragmentationMode
    n_subjects: int
    subjects: List[SubjectState]
    cross_subject_coupling: float
    branch_isolation: float
    collective_phi: float
    is_collective_unified: bool
    disorganization: float
    mean_local_phi: float


def _subject_phi(
    subject_id: str,
    local_intensity: float,
    n_nodes: int = DEFAULT_INTERNAL_NODES,
    disorganization: float = 0.0,
) -> float:
    micros = make_internal_micros(subject_id, n_nodes=n_nodes, base_intensity=local_intensity)
    phi = phi_analog_from_binding(micros) * (1.0 - disorganization)
    return float(max(0.0, phi))


def simulate_fragmentation(
    cosmic_intensity: float = 0.9,
    n_subjects: int = 3,
    filter_strength: float = 0.85,
    n_nodes: int = DEFAULT_INTERNAL_NODES,
) -> FragmentationResult:
    """F2: cosmic field filtered into local subjects (cosmopsychism)."""
    subjects: List[SubjectState] = []
    for i in range(n_subjects):
        sid = f"subject_{i}"
        f = filter_output(cosmic_intensity, filter_strength)
        phi = _subject_phi(sid, f["local_intensity"], n_nodes=n_nodes)
        subjects.append(
            SubjectState(
                subject_id=sid,
                local_phi=phi,
                filter_strength=filter_strength,
                local_intensity=f["local_intensity"],
                cosmic_bleed=f["cosmic_bleed"],
                is_unified=phi > PHI_UNIFIED_THRESHOLD and filter_strength > 0.5,
                internal_nodes=n_nodes,
            )
        )
    mean_local = float(np.mean([s.local_phi for s in subjects]))
    return FragmentationResult(
        mode=FragmentationMode.FRAGMENTATION,
        n_subjects=n_subjects,
        subjects=subjects,
        cross_subject_coupling=0.0,
        branch_isolation=1.0,
        collective_phi=mean_local,
        is_collective_unified=False,
        disorganization=0.0,
        mean_local_phi=mean_local,
    )


def simulate_branching(
    cosmic_intensity: float = 0.9,
    n_branches: int = 4,
    filter_strength: float = 0.8,
    n_nodes: int = DEFAULT_INTERNAL_NODES,
) -> FragmentationResult:
    """F3: MWI analog — split into mutually inaccessible branches."""
    branch_weights = np.random.dirichlet(np.ones(n_branches))
    isolation = branch_isolation_index(branch_weights)
    subjects: List[SubjectState] = []
    for i, weight in enumerate(branch_weights):
        sid = f"branch_{i}"
        effective = cosmic_intensity * float(weight) * n_branches
        f = filter_output(effective, filter_strength)
        phi = _subject_phi(sid, f["local_intensity"], n_nodes=n_nodes)
        subjects.append(
            SubjectState(
                subject_id=sid,
                local_phi=phi,
                filter_strength=filter_strength,
                local_intensity=f["local_intensity"],
                cosmic_bleed=f["cosmic_bleed"],
                is_unified=phi > PHI_UNIFIED_THRESHOLD * 0.85,
                internal_nodes=n_nodes,
            )
        )
    mean_local = float(np.mean([s.local_phi for s in subjects]))
    return FragmentationResult(
        mode=FragmentationMode.BRANCHING,
        n_subjects=n_branches,
        subjects=subjects,
        cross_subject_coupling=0.0,
        branch_isolation=isolation,
        collective_phi=mean_local,
        is_collective_unified=False,
        disorganization=0.0,
        mean_local_phi=mean_local,
    )


def simulate_collective_coupling(
    n_subjects: int = 3,
    filter_strength: float = 0.7,
    coupling_strength: float = 0.6,
    cosmic_intensity: float = 0.85,
    n_nodes: int = DEFAULT_INTERNAL_NODES,
) -> FragmentationResult:
    """F4: temporary cross-subject binding (P7 analog)."""
    subjects: List[SubjectState] = []
    for i in range(n_subjects):
        sid = f"subject_{i}"
        f = filter_output(cosmic_intensity, filter_strength * 0.8)
        phi = _subject_phi(sid, f["local_intensity"], n_nodes=n_nodes)
        subjects.append(
            SubjectState(
                subject_id=sid,
                local_phi=phi,
                filter_strength=filter_strength,
                local_intensity=f["local_intensity"],
                cosmic_bleed=f["cosmic_bleed"],
                is_unified=phi > PHI_UNIFIED_THRESHOLD,
                internal_nodes=n_nodes,
            )
        )
    cross = cross_subject_binding_matrix(n_subjects, coupling_strength)
    cross_coupling = float(cross.sum() / (n_subjects * n_subjects + 1e-10))
    mean_local_phi = float(np.mean([s.local_phi for s in subjects]))
    collective_phi = mean_local_phi * (1 + cross_coupling) * (1 + 0.1 * n_subjects)
    collective_phi = float(np.clip(collective_phi, 0, 1))
    return FragmentationResult(
        mode=FragmentationMode.COLLECTIVE_COUPLING,
        n_subjects=n_subjects,
        subjects=subjects,
        cross_subject_coupling=cross_coupling,
        branch_isolation=0.0,
        collective_phi=collective_phi,
        is_collective_unified=(
            cross_coupling > CROSS_COUPLING_COLLECTIVE_THRESHOLD
            and collective_phi > PHI_COLLECTIVE_THRESHOLD
        ),
        disorganization=0.0,
        mean_local_phi=mean_local_phi,
    )


def simulate_filter_failure(
    cosmic_intensity: float = 0.95,
    n_subjects: int = 1,
    filter_strength: float = 0.25,
    bleed_factor: float = 0.9,
    n_nodes: int = DEFAULT_INTERNAL_NODES,
) -> FragmentationResult:
    """F5 / P8: filter failure — high bleed, disorganized (psychosis analog)."""
    subjects: List[SubjectState] = []
    for i in range(n_subjects):
        sid = f"subject_{i}"
        f = filter_output(cosmic_intensity, filter_strength, bleed_factor=bleed_factor)
        phi = _subject_phi(
            sid, f["local_intensity"], n_nodes=n_nodes, disorganization=f["disorganization"]
        )
        subjects.append(
            SubjectState(
                subject_id=sid,
                local_phi=phi,
                filter_strength=filter_strength,
                local_intensity=f["local_intensity"],
                cosmic_bleed=f["cosmic_bleed"],
                is_unified=False,
                internal_nodes=n_nodes,
            )
        )
    disorg = float(
        np.mean([
            filter_output(cosmic_intensity, filter_strength, bleed_factor)["disorganization"]
            for _ in range(n_subjects)
        ])
    )
    mean_local = float(np.mean([s.local_phi for s in subjects]))
    return FragmentationResult(
        mode=FragmentationMode.FILTER_FAILURE,
        n_subjects=n_subjects,
        subjects=subjects,
        cross_subject_coupling=0.3 * bleed_factor,
        branch_isolation=0.0,
        collective_phi=mean_local,
        is_collective_unified=False,
        disorganization=disorg,
        mean_local_phi=mean_local,
    )


def _result_to_dict(r: FragmentationResult) -> Dict:
    return {
        "mode": r.mode.value,
        "n_subjects": r.n_subjects,
        "subjects": [asdict(s) for s in r.subjects],
        "cross_subject_coupling": round(r.cross_subject_coupling, 4),
        "branch_isolation": round(r.branch_isolation, 4),
        "collective_phi": round(r.collective_phi, 4),
        "mean_local_phi": round(r.mean_local_phi, 4),
        "is_collective_unified": r.is_collective_unified,
        "disorganization": round(r.disorganization, 4),
    }


def run_fragmentation_experiment(seed: int = 42) -> Dict:
    np.random.seed(seed)
    results = {
        FragmentationMode.FRAGMENTATION.value: _result_to_dict(simulate_fragmentation()),
        FragmentationMode.BRANCHING.value: _result_to_dict(simulate_branching()),
        FragmentationMode.COLLECTIVE_COUPLING.value: _result_to_dict(simulate_collective_coupling()),
        FragmentationMode.FILTER_FAILURE.value: _result_to_dict(simulate_filter_failure()),
    }

    collective = results["collective_coupling"]
    failure = results["filter_failure"]
    fragmented = results["fragmentation"]

    interpretation = {
        "thesis": "Branching Fragmentation Cosmopsychism (BFC)",
        "finding": (
            f"collective_phi={collective['collective_phi']:.4f} "
            f"mean_local_phi={collective['mean_local_phi']:.4f} "
            f"cross_coupling={collective['cross_subject_coupling']:.4f}; "
            f"filter_failure disorganization={failure['disorganization']:.4f}"
        ),
        "p7_analog": collective["is_collective_unified"],
        "p8_analog": failure["disorganization"] > collective["disorganization"],
        "p9_analog": fragmented["cross_subject_coupling"] == 0.0,
        "phi_fix": "Multi-node internal structure yields non-zero local_phi per subject",
        "caveat": "Computational model only; not empirical proof of cosmopsychism or MWI",
    }

    output = {
        "experiment": "fragmentation_model",
        "seed": seed,
        "internal_nodes_per_subject": DEFAULT_INTERNAL_NODES,
        "results_by_mode": results,
        "interpretation": interpretation,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Fragmentation experiment complete. Results: {OUTPUT_PATH}")
    for mode, data in results.items():
        print(
            f"  {mode:22s} collective_phi={data.get('collective_phi', 0):.4f} "
            f"mean_local={data.get('mean_local_phi', 0):.4f} "
            f"unified={data.get('is_collective_unified', False)}"
        )
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Fragmentation Model: BFC / MWI / Collective Coupling")
    print("=" * 60)
    run_fragmentation_experiment()
