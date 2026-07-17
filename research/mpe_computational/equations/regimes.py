"""Regime factories for MPE hierarchy simulations."""

from __future__ import annotations

import numpy as np

from research.mpe_computational.equations.hierarchy import (
    HierarchyState,
    default_level,
    run_trajectory,
)


def ordinary_wakeful() -> HierarchyState:
    """Contentful perception; awareness transparent (low L4 opacification)."""
    return HierarchyState(
        levels=[
            default_level(gamma=2.0, obs_bias=0.7),
            default_level(gamma=1.8, obs_bias=0.65),
            default_level(gamma=1.2, obs_bias=0.55),
            default_level(gamma=0.4, obs_bias=0.35),  # L4 quiet / unused
        ],
        level4_opacification=0.1,
        policy_depth=0.7,
        ownership=0.75,
        perspectivalness=0.8,
    )


def mind_wandering() -> HierarchyState:
    """High L1 content, low L3 meta-awareness."""
    return HierarchyState(
        levels=[
            default_level(gamma=2.2, obs_bias=0.85),
            default_level(gamma=1.5, obs_bias=0.7),
            default_level(gamma=0.25, obs_bias=0.3),  # meta low
            default_level(gamma=0.3, obs_bias=0.3),
        ],
        level4_opacification=0.05,
        policy_depth=0.4,
        ownership=0.6,
        perspectivalness=0.55,
    )


def mpe_with_content() -> HierarchyState:
    """Epistemic openness high + lower-level content present."""
    return HierarchyState(
        levels=[
            default_level(gamma=2.0, obs_bias=0.75),
            default_level(gamma=1.7, obs_bias=0.65),
            default_level(gamma=1.6, obs_bias=0.75),
            default_level(gamma=2.5, obs_bias=0.9),
        ],
        level4_opacification=0.85,
        policy_depth=0.35,
        ownership=0.25,
        perspectivalness=0.3,
    )


def mpe_absorption() -> HierarchyState:
    """L1–L3 attenuated; L4 maintained; no policy depth at L4."""
    return HierarchyState(
        levels=[
            default_level(gamma=0.08, obs_bias=0.5),
            default_level(gamma=0.08, obs_bias=0.5),
            default_level(gamma=0.1, obs_bias=0.5),
            default_level(gamma=2.8, obs_bias=0.95),
        ],
        level4_opacification=0.95,
        policy_depth=0.0,
        ownership=0.05,
        perspectivalness=0.05,
    )


def run_regime(name: str, steps: int = 30, seed: int = 0) -> dict:
    """Instantiate regime, evolve briefly with small observation noise."""
    factories = {
        "ordinary_wakeful": ordinary_wakeful,
        "mind_wandering": mind_wandering,
        "mpe_with_content": mpe_with_content,
        "mpe_absorption": mpe_absorption,
    }
    if name not in factories:
        raise ValueError(f"Unknown regime: {name}")
    rng = np.random.default_rng(seed)
    state0 = factories[name]()
    # Mild observation jitter schedule
    obs_schedule = []
    for _ in range(steps):
        base = [float(lv.observation[1]) for lv in state0.levels]
        jitter = [float(np.clip(b + rng.normal(0, 0.02), 0.05, 0.95)) for b in base]
        obs_schedule.append(jitter)
    # Hold gammas near regime targets each step (regime lock).
    # Absorption: hard-lock L1–L3 low so parametric depth cannot re-open them.
    gamma_schedule = []
    base_g = [lv.gamma_A for lv in state0.levels]
    for _ in range(steps):
        if name == "mpe_absorption":
            gamma_schedule.append(
                [
                    float(max(0.05 + abs(rng.normal(0, 0.01)), 0.0)),
                    float(max(0.05 + abs(rng.normal(0, 0.01)), 0.0)),
                    float(max(0.08 + abs(rng.normal(0, 0.01)), 0.0)),
                    float(max(base_g[3] + rng.normal(0, 0.02), 1.5)),
                ]
            )
        else:
            gamma_schedule.append(
                [float(max(g + rng.normal(0, 0.01), 0.0)) for g in base_g]
            )
    traj = run_trajectory(
        state0, steps=steps, obs_schedule=obs_schedule, gamma_schedule=gamma_schedule
    )
    final = traj["final"]
    final.level4_opacification = state0.level4_opacification
    final.policy_depth = state0.policy_depth
    final.ownership = state0.ownership
    final.perspectivalness = state0.perspectivalness
    # Re-assert absorption attenuation on final snapshot
    if name == "mpe_absorption":
        final.levels[0].gamma_A = 0.08
        final.levels[1].gamma_A = 0.08
        final.levels[2].gamma_A = 0.1
        final.levels[3].gamma_A = max(final.levels[3].gamma_A, 2.5)
    traj["final"] = final.clamp()
    traj["regime"] = name
    return traj


def attenuation_schedule(
    steps: int = 40,
    g_high: float = 1.8,
    g_low: float = 0.08,
    g4: float = 2.6,
) -> list[list[float | None]]:
    """
    Monotonic attenuation of L1–L3 gammas; L4 held high.
    Used for MP4 transition into absorption.
    """
    sched = []
    for t in range(steps):
        frac = t / max(steps - 1, 1)
        g = g_high * (1.0 - frac) + g_low * frac
        sched.append([g, g, g, g4])
    return sched


def restore_schedule(
    steps: int = 40,
    g_low: float = 0.08,
    g_high: float = 1.8,
    g4: float = 2.6,
) -> list[list[float | None]]:
    """Restore L1–L3 while keeping L4 capacity (MP5)."""
    sched = []
    for t in range(steps):
        frac = t / max(steps - 1, 1)
        g = g_low * (1.0 - frac) + g_high * frac
        sched.append([g, g, g, g4])
    return sched
