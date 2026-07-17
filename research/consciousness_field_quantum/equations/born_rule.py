"""Born rule consistency checks."""

from __future__ import annotations

import numpy as np

from research.consciousness_field_quantum.equations.density_matrix import normalize_dm


def born_probabilities(rho: np.ndarray, projectors: list[np.ndarray] | None = None) -> np.ndarray:
    """Diagonal probabilities in computational basis, or custom projectors."""
    rho = normalize_dm(rho)
    if projectors is None:
        return np.clip(np.real(np.diag(rho)), 0.0, 1.0)
    probs = []
    for p in projectors:
        probs.append(float(np.real(np.trace(rho @ p))))
    probs = np.asarray(probs, dtype=float)
    probs = np.clip(probs, 0.0, None)
    s = probs.sum()
    if s < 1e-15:
        return np.ones(len(probs)) / len(probs)
    return probs / s


def born_total_variation(p: np.ndarray, q: np.ndarray) -> float:
    """Total variation distance (1/2) Σ |p-q|."""
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p = p / p.sum()
    q = q / q.sum()
    return float(0.5 * np.sum(np.abs(p - q)))


def sample_outcomes(probs: np.ndarray, n_samples: int, rng: np.random.Generator) -> np.ndarray:
    probs = np.asarray(probs, dtype=float)
    probs = probs / probs.sum()
    return rng.choice(len(probs), size=n_samples, p=probs)


def empirical_frequencies(samples: np.ndarray, n_outcomes: int) -> np.ndarray:
    counts = np.bincount(samples, minlength=n_outcomes).astype(float)
    return counts / max(counts.sum(), 1.0)


def born_fit_score(p_emp: np.ndarray, p_born: np.ndarray, tol: float = 0.08) -> float:
    """
    Score in [0,1]: 1 if TV <= tol, linearly down to 0 at TV >= 0.5.
    """
    tv = born_total_variation(p_emp, p_born)
    if tv <= tol:
        return 1.0
    if tv >= 0.5:
        return 0.0
    return float(1.0 - (tv - tol) / (0.5 - tol))
