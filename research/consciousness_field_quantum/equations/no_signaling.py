"""Bell / no-signaling diagnostics for entangled toys."""

from __future__ import annotations

import numpy as np

from research.consciousness_field_quantum.equations.density_matrix import (
    apply_unitary,
    expect,
    embed_single_qubit_op,
    normalize_dm,
    pauli_x,
    pauli_z,
    reduce_qubit_pair,
    rotation_u,
)


def measure_pauli_prob(rho_qubit: np.ndarray, axis: str) -> float:
    """P(+1) for measuring σ along x or z on a single qubit."""
    op = pauli_x() if axis.lower() == "x" else pauli_z()
    e = np.real(expect(rho_qubit, op))
    # P(+1) = (1 + ⟨σ⟩) / 2
    return float(np.clip((1.0 + e) / 2.0, 0.0, 1.0))


def local_marginal(rho_ab: np.ndarray, party: str, axis: str) -> float:
    """Marginal P(+1) for one party — should be independent of the other's setting."""
    rho_ab = normalize_dm(rho_ab)
    keep = "A" if party.upper() == "A" else "B"
    # Rotate the measured party into Z basis if measuring X
    if axis.lower() == "x":
        # Apply Hadamard-like: measure X = H Z H; rotate state
        H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
        if keep == "A":
            U = embed_single_qubit_op(H, 0, 2)
        else:
            U = embed_single_qubit_op(H, 1, 2)
        rho_ab = apply_unitary(rho_ab, U)
    reduced = reduce_qubit_pair(rho_ab, keep=keep)
    return measure_pauli_prob(reduced, "z")


def signaling_score(
    rho_ab: np.ndarray,
    party: str = "A",
    other_settings: tuple[str, str] = ("z", "x"),
) -> float:
    """
    |P(outcome|setting1) - P(outcome|setting2)| for local party when other
    'chooses' a setting. For a shared entangled state without collapse feedback,
    local reduced state is independent of distant measurement → score ~ 0.

    Toy construction: compare local marginals after applying different
    unitaries on the distant qubit (setting choice as local unitary).
    """
    rho = normalize_dm(rho_ab)
    other = 1 if party.upper() == "A" else 0
    scores = []
    for setting in other_settings:
        if setting.lower() == "z":
            U_other = np.eye(2, dtype=complex)
        else:
            U_other = rotation_u("x", np.pi / 2)
        U = embed_single_qubit_op(U_other, other, 2)
        rho_set = apply_unitary(rho, U)
        marg = local_marginal(rho_set, party, "z")
        scores.append(marg)
    return float(abs(scores[0] - scores[1]))


def chsh_correlator(rho_ab: np.ndarray) -> float:
    """
    CHSH expectation for standard Bell angles on Φ+.
    Ideal |⟨CHSH⟩| = 2√2 for Φ+.
    """
    rho = normalize_dm(rho_ab)
    # A0=Z, A1=X, B0=(Z+X)/√2, B1=(Z-X)/√2
    def corr(ax: str, bx_angle: float) -> float:
        # ⟨A⊗B⟩ via rotated Paulis
        A = pauli_z() if ax == "z" else pauli_x()
        # B = cosθ Z + sinθ X
        B = np.cos(bx_angle) * pauli_z() + np.sin(bx_angle) * pauli_x()
        op = np.kron(A, B)
        return float(np.real(expect(rho, op)))

    e00 = corr("z", np.pi / 4)
    e01 = corr("z", -np.pi / 4)
    e10 = corr("x", np.pi / 4)
    e11 = corr("x", -np.pi / 4)
    return float(e00 + e01 + e10 - e11)


def naive_local_collapse_signaling(
    rho_ab: np.ndarray,
    rng: np.random.Generator,
) -> float:
    """
    Pathological Track C: collapse Bob's qubit based on a 'clump choice'
    then check Alice's marginal shift — should flag signaling risk.
    """
    rho = normalize_dm(rho_ab)
    # Choice 0: project Bob to |0>; Choice 1: project Bob to |1|
    margs = []
    for k in (0, 1):
        # Project Bob
        proj_b = np.zeros((2, 2), dtype=complex)
        proj_b[k, k] = 1.0
        P = np.kron(np.eye(2), proj_b)
        # Unnormalized post-measure
        rho_post = P @ rho @ P
        tr = np.trace(rho_post)
        if abs(tr) < 1e-12:
            # impossible branch — use random
            margs.append(0.5)
            continue
        rho_post = rho_post / tr
        from research.consciousness_field_quantum.equations.density_matrix import reduce_qubit_pair

        rho_a = reduce_qubit_pair(rho_post, keep="A")
        margs.append(measure_pauli_prob(rho_a, "z"))
    return float(abs(margs[0] - margs[1]))
