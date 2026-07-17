"""Clumping model: localized modes as observer/subject proxies."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class ClumpState:
    """Localized mode parameters (C1)."""

    amplitude: float = 1.0
    coherence_length: float = 1.0
    mode_stability: float = 0.8
    center: float = 0.0

    def clamp(self) -> "ClumpState":
        return ClumpState(
            amplitude=float(np.clip(self.amplitude, 0.0, 10.0)),
            coherence_length=float(max(self.coherence_length, 1e-6)),
            mode_stability=float(np.clip(self.mode_stability, 0.0, 1.0)),
            center=float(self.center),
        )


def gaussian_localization_profile(
    n_outcomes: int,
    clump: ClumpState,
    outcome_positions: np.ndarray | None = None,
) -> np.ndarray:
    """
    Soft localization weights over discrete pointer outcomes.
    Narrow σ → peaked clump; used by Track U selection and Track C λ(A).
    """
    clump = clump.clamp()
    if outcome_positions is None:
        outcome_positions = np.linspace(-1.0, 1.0, n_outcomes)
    pos = np.asarray(outcome_positions, dtype=float)
    w = np.exp(-0.5 * ((pos - clump.center) / clump.coherence_length) ** 2)
    w *= clump.amplitude * clump.mode_stability
    s = w.sum()
    if s < 1e-15:
        return np.ones(n_outcomes) / n_outcomes
    return w / s


def clump_selection_weights(
    born_probs: np.ndarray,
    clump: ClumpState,
    blend: float = 0.15,
) -> np.ndarray:
    """
    Track U: experiential selection weights.

    Primarily Born; mild reweight by localization profile (does not alter
    physics Born predictions used for scoring — see born_rule_lab).
    For physics Born fit we still compare to |c|^2; selection weights are
    an experiential overlay for definiteness diagnostics.
    """
    born = np.asarray(born_probs, dtype=float)
    born = born / born.sum()
    profile = gaussian_localization_profile(len(born), clump)
    blend = float(np.clip(blend, 0.0, 1.0))
    mixed = (1.0 - blend) * born + blend * profile
    return mixed / mixed.sum()


def definiteness_from_clump(clump: ClumpState, classicality: float) -> float:
    """
    Proxy for 'how definite an outcome feels' given clump + classical pointer.
    Track U: rises with A, stability, and decohered classicality — without λ.
    """
    clump = clump.clamp()
    a = np.tanh(clump.amplitude)
    return float(np.clip(a * clump.mode_stability * classicality, 0.0, 1.0))


def clump_density(clump: ClumpState) -> float:
    """Effective density for Track C rate λ(A). Legacy geometric form."""
    clump = clump.clamp()
    return float(clump.amplitude / max(clump.coherence_length, 1e-6))


def clump_from_awareness_projection(amplitude: float, coherence_length: float,
                                    mode_stability: float, center: float = 0.0) -> ClumpState:
    """Build ClumpState from geometric fields (awareness_matter adapter)."""
    return ClumpState(
        amplitude=amplitude,
        coherence_length=coherence_length,
        mode_stability=mode_stability,
        center=center,
    ).clamp()