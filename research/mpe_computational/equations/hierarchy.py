"""4-level parametric-depth hierarchy (MPE Subproject 3 architecture, toy NumPy)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

N_LEVELS = 4
# Latent states per level: 0 = low/off-ish, 1 = high/on-ish (binary toy)
N_STATES = 2


def _softmax(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x - np.max(x)
    e = np.exp(x)
    return e / max(e.sum(), 1e-15)


def _normalize(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    p = np.clip(p, 0.0, None)
    s = p.sum()
    if s < 1e-15:
        return np.ones(len(p)) / len(p)
    return p / s


@dataclass
class LevelState:
    """One hierarchical level."""

    prior: np.ndarray  # D
    posterior: np.ndarray  # q
    gamma_A: float  # likelihood precision
    observation: np.ndarray  # likelihood scores / soft evidence over states


@dataclass
class HierarchyState:
    """Full 4-level hierarchy."""

    levels: list[LevelState] = field(default_factory=list)
    # Opacification of level 4: 0 = transparent (ordinary), 1 = aware of awareness
    level4_opacification: float = 0.0
    # Agency / policy-depth proxy (0 in absorption at L4)
    policy_depth: float = 0.5
    # Egoic / perspectival proxies (external to pure L4)
    ownership: float = 0.5
    perspectivalness: float = 0.5

    def clamp(self) -> "HierarchyState":
        out_levels = []
        for lv in self.levels:
            out_levels.append(
                LevelState(
                    prior=_normalize(lv.prior),
                    posterior=_normalize(lv.posterior),
                    gamma_A=float(max(lv.gamma_A, 0.0)),
                    observation=np.asarray(lv.observation, dtype=float),
                )
            )
        return HierarchyState(
            levels=out_levels,
            level4_opacification=float(np.clip(self.level4_opacification, 0.0, 1.0)),
            policy_depth=float(np.clip(self.policy_depth, 0.0, 1.0)),
            ownership=float(np.clip(self.ownership, 0.0, 1.0)),
            perspectivalness=float(np.clip(self.perspectivalness, 0.0, 1.0)),
        )


def default_level(
    gamma: float,
    obs_bias: float = 0.5,
    prior: np.ndarray | None = None,
) -> LevelState:
    """obs_bias in [0,1]: preference for state 1 in soft likelihood."""
    if prior is None:
        prior = np.array([0.5, 0.5], dtype=float)
    # Soft likelihood: higher obs_bias → more evidence for state 1
    like = np.array([1.0 - obs_bias, obs_bias], dtype=float) + 1e-3
    like = _normalize(like)
    return LevelState(
        prior=_normalize(prior),
        posterior=_normalize(prior.copy()),
        gamma_A=float(gamma),
        observation=like,
    )


def precision_weighted_update(level: LevelState) -> np.ndarray:
    """
    q ∝ exp(log D + γ log L(o|·))
    """
    prior = _normalize(level.prior)
    like = _normalize(np.clip(level.observation, 1e-12, None))
    log_post = np.log(prior + 1e-12) + level.gamma_A * np.log(like + 1e-12)
    return _softmax(log_post)


def apply_parametric_depth(state: HierarchyState, gain: float = 1.5) -> HierarchyState:
    """
    Higher level's 'high' posterior mass raises gamma of the level below.
    Level 4's openness mass modulates gamma_A^(3) especially when opacified.
    """
    s = state.clamp()
    # Bottom-up: update posteriors given current gammas
    for i, lv in enumerate(s.levels):
        s.levels[i].posterior = precision_weighted_update(lv)

    # Top-down precision targets from level above
    for i in range(N_LEVELS - 1):
        above = s.levels[i + 1]
        # Mass on state 1 = "high / engaged"
        mass_high = float(above.posterior[1])
        base = 0.15 + gain * mass_high
        if i == 2:
            # L3 also gated by L4 opacification (aware of meta-awareness)
            base *= 0.3 + 0.7 * s.level4_opacification
        # Blend toward target; never fully overwrite regime-set floors/ceilings
        target = base
        s.levels[i].gamma_A = float(0.5 * s.levels[i].gamma_A + 0.5 * target)

    # Recompute posteriors after gamma update
    for i, lv in enumerate(s.levels):
        s.levels[i].posterior = precision_weighted_update(lv)
    return s.clamp()


def step_hierarchy(
    state: HierarchyState,
    obs_biases: list[float] | None = None,
    gamma_overrides: list[float | None] | None = None,
) -> HierarchyState:
    """One simulation step: optional obs/gamma overrides, then parametric depth.

    Gamma overrides are applied *after* parametric depth so regime locks
    (e.g. absorption attenuation) are not undone by top-down precision boosts.
    """
    s = state.clamp()
    if obs_biases is not None:
        for i, b in enumerate(obs_biases):
            if i < len(s.levels):
                like = np.array([1.0 - b, b], dtype=float) + 1e-3
                s.levels[i].observation = _normalize(like)
    s = apply_parametric_depth(s)
    if gamma_overrides is not None:
        for i, g in enumerate(gamma_overrides):
            if g is not None and i < len(s.levels):
                s.levels[i].gamma_A = float(max(g, 0.0))
        # Refresh posteriors under locked gammas
        for i, lv in enumerate(s.levels):
            s.levels[i].posterior = precision_weighted_update(lv)
    return s.clamp()


def run_trajectory(
    state0: HierarchyState,
    steps: int = 40,
    obs_schedule: list[list[float]] | None = None,
    gamma_schedule: list[list[float | None]] | None = None,
) -> dict[str, Any]:
    """
    Evolve hierarchy; return trajectories of gammas, posterior masses, and states.
    """
    s = state0.clamp()
    hist_gamma = []
    hist_mass = []
    hist_states: list[HierarchyState] = []
    for t in range(steps):
        obs = obs_schedule[t] if obs_schedule is not None else None
        gam = gamma_schedule[t] if gamma_schedule is not None else None
        s = step_hierarchy(s, obs_biases=obs, gamma_overrides=gam)
        hist_gamma.append([lv.gamma_A for lv in s.levels])
        hist_mass.append([float(lv.posterior[1]) for lv in s.levels])
        hist_states.append(s)
    return {
        "final": s,
        "gamma": np.asarray(hist_gamma, dtype=float),
        "mass_high": np.asarray(hist_mass, dtype=float),
        "states": hist_states,
        "steps": steps,
    }


def level_content_strength(level: LevelState) -> float:
    """
    Reportable content contribution: open precision channel × content drive.

    Uses observation drive (state-1 bias) so high-γ flat posteriors still count
    as contentful when the sensory channel is open — matching Subproject 3's
    "precision enables perception" gloss.
    """
    g = float(np.tanh(level.gamma_A / 1.5))
    obs = _normalize(np.clip(level.observation, 0.0, None))
    drive = float(obs[1]) if len(obs) > 1 else float(np.max(obs))
    q = _normalize(level.posterior)
    mass = float(q[1]) if len(q) > 1 else float(np.max(q))
    return float(np.clip(g * (0.2 + 0.5 * drive + 0.3 * mass), 0.0, 1.0))
