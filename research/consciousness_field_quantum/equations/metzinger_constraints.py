"""Scalar constraint scores for Metzinger MPE PCs + SMT targets."""

from __future__ import annotations

from typing import Any

import numpy as np

from research.consciousness_field_quantum.equations.awareness_matter import (
    AwarenessMatterState,
    is_mpe_active,
    is_pmir_active,
    is_psm_active,
)


def _clip01(x: float) -> float:
    return float(np.clip(x, 0.0, 1.0))


def score_wakefulness(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().wakefulness)


def score_low_complexity(state: AwarenessMatterState) -> float:
    """1 = minimal content (MPE-friendly); 0 = rich content."""
    return _clip01(1.0 - state.clamp().content_complexity)


def score_epistemicity(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().epistemicity)


def score_introspective_availability(state: AwarenessMatterState) -> float:
    """Opacity of awareness-as-such (can attend to knowingness)."""
    return _clip01(state.clamp().opacity_mpe)


def score_transparency(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().transparency)


def score_ownership(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().ownership)


def score_perspectivalness(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().perspectivalness)


def score_selfhood(state: AwarenessMatterState) -> float:
    return _clip01(state.clamp().selfhood)


def constraint_vector(state: AwarenessMatterState) -> dict[str, float]:
    """Named scalar scores for labs / JSON."""
    a = state.clamp()
    return {
        "wakefulness": score_wakefulness(a),
        "low_complexity": score_low_complexity(a),
        "epistemicity": score_epistemicity(a),
        "introspective_availability": score_introspective_availability(a),
        "transparency": score_transparency(a),
        "ownership": score_ownership(a),
        "perspectivalness": score_perspectivalness(a),
        "selfhood": score_selfhood(a),
        "intentional_arrow": _clip01(a.intentional_arrow),
        "diachronic": _clip01(a.diachronic),
    }


def mpe_profile_match(state: AwarenessMatterState, tol: float = 0.25) -> dict[str, Any]:
    """
    M1: MPE factory should match high wakefulness, high low_complexity,
    low selfhood / perspectivalness.
    """
    v = constraint_vector(state)
    checks = {
        "wakefulness_high": v["wakefulness"] >= 0.7,
        "complexity_low": v["low_complexity"] >= 0.7,
        "selfhood_low": v["selfhood"] <= 0.25,
        "perspectival_low": v["perspectivalness"] <= 0.25,
        "mpe_predicate": is_mpe_active(state),
    }
    score = float(sum(checks.values()) / len(checks))
    return {
        "vector": v,
        "checks": checks,
        "match_score": score,
        "pass": score >= 1.0 - 1e-9 and is_mpe_active(state),
        "tol": tol,
    }


def psm_profile_match(state: AwarenessMatterState) -> dict[str, Any]:
    """PSM-active: selfhood + transparency (+ ownership rises)."""
    v = constraint_vector(state)
    checks = {
        "selfhood_high": v["selfhood"] >= 0.6,
        "transparency_high": v["transparency"] >= 0.5,
        "ownership_up": v["ownership"] >= 0.5,
        "psm_predicate": is_psm_active(state),
    }
    score = float(sum(checks.values()) / len(checks))
    return {
        "vector": v,
        "checks": checks,
        "match_score": score,
        "pass": is_psm_active(state) and v["ownership"] >= 0.5,
    }


def layer_flags(state: AwarenessMatterState) -> dict[str, bool]:
    return {
        "mpe_active": is_mpe_active(state),
        "psm_active": is_psm_active(state),
        "pmir_active": is_pmir_active(state),
    }
