"""Phenomenological readouts from hierarchy state."""

from __future__ import annotations

from typing import Any

import numpy as np

from research.mpe_computational.equations.hierarchy import (
    HierarchyState,
    level_content_strength,
)


def _clip01(x: float) -> float:
    return float(np.clip(x, 0.0, 1.0))


def phenomenology_vector(state: HierarchyState) -> dict[str, float]:
    """
    Named phenomenological scores in [0,1].
    See FACTOR_MAP.md.
    """
    s = state.clamp()
    assert len(s.levels) == 4
    l1, l2, l3, l4 = s.levels

    c1 = level_content_strength(l1)
    c2 = level_content_strength(l2)
    c3 = level_content_strength(l3)
    c4 = level_content_strength(l4)

    contentfulness = _clip01(0.7 * c1 + 0.3 * c2)
    meta_awareness = _clip01(c3)
    # Epistemicity: L4 strength × opacification (aware of openness)
    epistemicity = _clip01(c4 * (0.35 + 0.65 * s.level4_opacification))
    awareness_of_awareness = _clip01(s.level4_opacification * c4)

    mental_agency = _clip01(
        0.5 * c2 * s.policy_depth + 0.5 * c3 * s.policy_depth
    )
    effortlessness = _clip01(1.0 - 0.6 * mental_agency - 0.2 * contentfulness + 0.4 * epistemicity)
    nonconceptuality = _clip01(1.0 - contentfulness)
    atemporality = _clip01(1.0 - s.policy_depth)
    aperspectivalness = _clip01(1.0 - s.perspectivalness)
    non_egoicity = _clip01(
        0.5 * (1.0 - s.ownership) + 0.3 * aperspectivalness + 0.2 * (1.0 - mental_agency)
    )

    return {
        "epistemicity": epistemicity,
        "nonconceptuality": nonconceptuality,
        "atemporality": atemporality,
        "aperspectivalness": aperspectivalness,
        "non_egoicity": non_egoicity,
        "effortlessness": _clip01(effortlessness),
        "awareness_of_awareness": awareness_of_awareness,
        "contentfulness": contentfulness,
        "meta_awareness": meta_awareness,
        "mental_agency": mental_agency,
        # extras for diagnostics
        "gamma_L1": float(l1.gamma_A),
        "gamma_L2": float(l2.gamma_A),
        "gamma_L3": float(l3.gamma_A),
        "gamma_L4": float(l4.gamma_A),
        "level4_opacification": float(s.level4_opacification),
    }


def absorption_score(vec: dict[str, float]) -> float:
    """Composite S_abs from FACTOR_MAP.md."""
    pos = np.mean(
        [
            vec["epistemicity"],
            vec["non_egoicity"],
            vec["effortlessness"],
            vec["awareness_of_awareness"],
        ]
    )
    neg = np.mean([vec["contentfulness"], vec["mental_agency"]])
    return float(pos - neg)


def factor_cluster_scores(vec: dict[str, float]) -> dict[str, float]:
    """Approximate MPE-92M-style cluster proxies."""
    return {
        "time_effort_desire": _clip01(1.0 - vec["effortlessness"]),
        "sensory_body_space": vec["contentfulness"],
        "mental_agency_factor": vec["mental_agency"],
        "epistemic_openness_pure_awareness": _clip01(
            0.5 * vec["epistemicity"] + 0.5 * vec["awareness_of_awareness"]
        ),
        "non_egoic_unbounded": _clip01(
            0.5 * vec["non_egoicity"] + 0.5 * vec["aperspectivalness"]
        ),
        "meta_awareness_factor": vec["meta_awareness"],
    }


def summarize_state(state: HierarchyState) -> dict[str, Any]:
    vec = phenomenology_vector(state)
    return {
        "phenomenology": vec,
        "factors": factor_cluster_scores(vec),
        "absorption_score": absorption_score(vec),
    }
