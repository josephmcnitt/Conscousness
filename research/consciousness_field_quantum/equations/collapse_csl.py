"""Track C: CSL-inspired continuous localization with rate λ(clump | rho_A)."""

from __future__ import annotations

from typing import Union

import numpy as np

from research.consciousness_field_quantum.equations.clumping import ClumpState, clump_density
from research.consciousness_field_quantum.equations.decoherence import off_diagonal_mean, purity
from research.consciousness_field_quantum.equations.density_matrix import normalize_dm

ObserverLike = Union[ClumpState, "AwarenessMatterState"]


def _observer_density(observer: ObserverLike) -> float:
    """Prefer awareness-matter rho_A when available; else legacy clump_density."""
    # Local import avoids circular dependency at module load
    from research.consciousness_field_quantum.equations.awareness_matter import (
        AwarenessMatterState,
        awareness_density,
    )

    if isinstance(observer, AwarenessMatterState):
        return awareness_density(observer)
    return clump_density(observer)


def csl_rate(clump: ObserverLike, lambda0: float = 0.05, alpha: float = 1.0) -> float:
    """λ = λ0 * density^α with density = rho_A or clump_density."""
    dens = _observer_density(clump)
    return float(lambda0 * (dens**alpha))

def csl_localize_step(
    rho: np.ndarray,
    lam: float,
    dt: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Simplified discrete CSL-like step in computational basis:
    with probability ~ λ dt, project onto a Born-weighted outcome;
    otherwise apply continuous off-diagonal damping ∝ λ.

    Toy model for scoring — not a full field CSL continuum limit.
    """
    rho = normalize_dm(rho)
    n = rho.shape[0]
    p_diag = np.clip(np.real(np.diag(rho)), 0.0, None)
    if p_diag.sum() < 1e-15:
        p_diag = np.ones(n) / n
    else:
        p_diag = p_diag / p_diag.sum()

    # Continuous localization (always): damp coherences at rate λ
    factor = np.exp(-lam * dt)
    out = rho.copy()
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i, j] *= factor
    rho = normalize_dm(out)

    # Stochastic jump: full projection onto pointer outcome
    if rng.random() < min(lam * dt, 1.0):
        p_diag = np.clip(np.real(np.diag(rho)), 0.0, None)
        p_diag = p_diag / max(p_diag.sum(), 1e-15)
        k = int(rng.choice(n, p=p_diag))
        proj = np.zeros_like(rho)
        proj[k, k] = 1.0
        return proj

    return rho


def run_csl_trajectory(
    rho0: np.ndarray,
    clump: ObserverLike,
    steps: int = 80,
    dt: float = 0.05,
    lambda0: float = 0.05,
    alpha: float = 1.0,
    seed: int = 0,
) -> dict:
    rng = np.random.default_rng(seed)
    dens = _observer_density(clump)
    lam = csl_rate(clump, lambda0=lambda0, alpha=alpha)
    rho = normalize_dm(rho0)
    purities = [purity(rho)]
    offdiags = [off_diagonal_mean(rho)]
    for _ in range(steps):
        rho = csl_localize_step(rho, lam, dt, rng)
        purities.append(purity(rho))
        offdiags.append(off_diagonal_mean(rho))
    return {
        "rho_final": rho,
        "lambda": lam,
        "lambda0": lambda0,
        "observer_density": dens,
        "purity": purities,
        "off_diagonal_mean": offdiags,
        "steps": steps,
        "dt": dt,
    }


def scan_lambda_born_fit(
    rho0: np.ndarray,
    clump: ObserverLike,
    born_target: np.ndarray,
    lambda0_grid: np.ndarray,
    n_samples: int = 2000,
    steps: int = 60,
    seed: int = 0,
) -> list[dict]:
    """Sweep λ0 and report empirical vs Born TV after CSL evolution + sampling."""
    from research.consciousness_field_quantum.equations.born_rule import (
        born_probabilities,
        born_total_variation,
        empirical_frequencies,
        sample_outcomes,
    )

    rows = []
    for i, lam0 in enumerate(lambda0_grid):
        traj = run_csl_trajectory(
            rho0, clump, steps=steps, lambda0=float(lam0), seed=seed + i
        )
        p_final = born_probabilities(traj["rho_final"])
        rng = np.random.default_rng(seed + 1000 + i)
        samples = sample_outcomes(p_final, n_samples, rng)
        p_emp = empirical_frequencies(samples, len(born_target))
        tv = born_total_variation(p_emp, born_target)
        rows.append(
            {
                "lambda0": float(lam0),
                "lambda": traj["lambda"],
                "observer_density": traj["observer_density"],
                "tv_born": tv,
                "p_emp": p_emp.tolist(),
                "final_purity": traj["purity"][-1],
            }
        )
    return rows
