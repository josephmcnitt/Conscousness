"""Decoherence / pointer diagnostics for Track U."""

from __future__ import annotations

import numpy as np

from research.consciousness_field_quantum.equations.density_matrix import normalize_dm


def purity(rho: np.ndarray) -> float:
    rho = np.asarray(rho, dtype=complex)
    return float(np.real(np.trace(rho @ rho)))


def off_diagonal_mean(rho: np.ndarray) -> float:
    """Mean absolute off-diagonal magnitude."""
    rho = np.asarray(rho, dtype=complex)
    n = rho.shape[0]
    if n < 2:
        return 0.0
    mask = ~np.eye(n, dtype=bool)
    return float(np.mean(np.abs(rho[mask])))


def pointer_entropy(rho: np.ndarray) -> float:
    """Von Neumann entropy of ρ (nats)."""
    rho = normalize_dm(rho)
    eig = np.clip(np.real(np.linalg.eigvalsh(rho)), 0.0, 1.0)
    eig = eig[eig > 1e-15]
    return float(-np.sum(eig * np.log(eig)))


def dephase_in_basis(rho: np.ndarray, gamma: float, dt: float, basis_U: np.ndarray | None = None) -> np.ndarray:
    """
    Exponential damping of off-diagonals in a preferred basis.

    If basis_U is provided, dephase in U† ρ U then rotate back
    (columns of U = basis vectors in computational basis).
    """
    rho = np.asarray(rho, dtype=complex)
    if basis_U is not None:
        Ub = np.asarray(basis_U, dtype=complex)
        rho_b = Ub.conj().T @ rho @ Ub
        rho_b = _dephase_computational(rho_b, gamma, dt)
        return normalize_dm(Ub @ rho_b @ Ub.conj().T)
    return normalize_dm(_dephase_computational(rho, gamma, dt))


def _dephase_computational(rho: np.ndarray, gamma: float, dt: float) -> np.ndarray:
    factor = np.exp(-gamma * dt)
    out = rho.copy()
    n = out.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i, j] *= factor
    return out


def amplitude_damping_like_dephasing(
    rho: np.ndarray,
    gamma: float,
    steps: int,
    dt: float = 0.05,
    basis_U: np.ndarray | None = None,
) -> dict:
    """
    Track purity, off-diagonals, and entropy under repeated dephasing.
    Track U primary channel.
    """
    rho_t = normalize_dm(rho)
    purities = [purity(rho_t)]
    offdiags = [off_diagonal_mean(rho_t)]
    ents = [pointer_entropy(rho_t)]
    for _ in range(steps):
        rho_t = dephase_in_basis(rho_t, gamma, dt, basis_U=basis_U)
        purities.append(purity(rho_t))
        offdiags.append(off_diagonal_mean(rho_t))
        ents.append(pointer_entropy(rho_t))
    return {
        "rho_final": rho_t,
        "purity": purities,
        "off_diagonal_mean": offdiags,
        "pointer_entropy": ents,
        "gamma": gamma,
        "steps": steps,
        "dt": dt,
    }


def classicality_score(rho: np.ndarray) -> float:
    """1 = fully classical diagonal mixture in computational basis; 0 = max coherent."""
    n = rho.shape[0]
    max_off = (n - 1) / n if n > 1 else 1.0
    # normalize offdiag mean roughly into [0,1]
    od = off_diagonal_mean(rho)
    return float(np.clip(1.0 - od / max(max_off, 1e-9), 0.0, 1.0))
