"""Density matrix helpers for Part VIII qubit / small-system toys."""

from __future__ import annotations

from typing import Tuple

import numpy as np


def normalize_dm(rho: np.ndarray) -> np.ndarray:
    rho = np.asarray(rho, dtype=complex)
    tr = np.trace(rho)
    if abs(tr) < 1e-15:
        raise ValueError("density matrix has zero trace")
    return rho / tr


def ket_to_dm(psi: np.ndarray) -> np.ndarray:
    psi = np.asarray(psi, dtype=complex).reshape(-1)
    n = np.linalg.norm(psi)
    if n < 1e-15:
        raise ValueError("zero state vector")
    psi = psi / n
    return np.outer(psi, psi.conj())


def qubit_bloch_dm(theta: float, phi: float = 0.0) -> np.ndarray:
    """Pure qubit |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    psi = np.array([c, np.exp(1j * phi) * s], dtype=complex)
    return ket_to_dm(psi)


def apply_unitary(rho: np.ndarray, U: np.ndarray) -> np.ndarray:
    U = np.asarray(U, dtype=complex)
    return normalize_dm(U @ rho @ U.conj().T)


def expect(rho: np.ndarray, op: np.ndarray) -> complex:
    return complex(np.trace(rho @ op))


def computational_basis_projectors(dim: int) -> list[np.ndarray]:
    projectors = []
    for i in range(dim):
        p = np.zeros((dim, dim), dtype=complex)
        p[i, i] = 1.0
        projectors.append(p)
    return projectors


def pauli_x() -> np.ndarray:
    return np.array([[0, 1], [1, 0]], dtype=complex)


def pauli_z() -> np.ndarray:
    return np.array([[1, 0], [0, -1]], dtype=complex)


def hadamard() -> np.ndarray:
    return (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)


def cnot() -> np.ndarray:
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=complex,
    )


def bell_phi_plus() -> np.ndarray:
    """(|00⟩+|11⟩)/√2 density matrix."""
    psi = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    return ket_to_dm(psi)


def reduce_qubit_pair(rho_ab: np.ndarray, keep: str = "A") -> np.ndarray:
    """Partial trace of 2-qubit state. keep 'A' or 'B'."""
    rho = np.asarray(rho_ab, dtype=complex).reshape(2, 2, 2, 2)
    if keep.upper() == "A":
        return normalize_dm(np.trace(rho, axis1=1, axis2=3))
    if keep.upper() == "B":
        return normalize_dm(np.trace(rho, axis1=0, axis2=2))
    raise ValueError("keep must be 'A' or 'B'")


def rotation_u(axis: str, angle: float) -> np.ndarray:
    """Single-qubit rotation exp(-i angle σ/2)."""
    if axis.lower() == "x":
        gen = pauli_x()
    elif axis.lower() == "z":
        gen = pauli_z()
    else:
        raise ValueError("axis must be x or z")
    return np.cos(angle / 2) * np.eye(2, dtype=complex) - 1j * np.sin(angle / 2) * gen


def kron(*ops: np.ndarray) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def embed_single_qubit_op(op: np.ndarray, qubit: int, n_qubits: int = 2) -> np.ndarray:
    eye = np.eye(2, dtype=complex)
    ops = [eye] * n_qubits
    ops[qubit] = op
    return kron(*ops)
