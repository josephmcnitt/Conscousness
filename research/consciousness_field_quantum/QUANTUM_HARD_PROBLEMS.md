# Quantum Hard Problems Catalog

**Part VIII** | Primary targets for consciousness-field + clumping

Each problem lists mainstream status, Track U claim, Track C claim, simulation leverage, and kill criteria.

**Label:** Research scoring only. In-silico compatibility ≠ empirical resolution.

---

## 1. Measurement / Definite Outcomes

**Problem:** Unitary Schrödinger evolution is linear; measurement yields one definite outcome. Why?

| | |
|--|--|
| **Mainstream status** | Decoherence + interpretation (Everett, relational, QBism) preferred over consciousness-collapse; objective collapse (GRW/CSL) minority but physical |
| **Track U** | Clumps select *which branch is experienced*; no extra dynamical law |
| **Track C** | Clump density raises localization rate → definite outcomes appear dynamically |
| **Sim leverage** | `measurement_lab.py` — purity, off-diagonals, outcome definiteness |
| **Kill U** | Cannot define when a clump “selects” without smuggling preferred basis |
| **Kill C** | Violates Born rule or introduces signaling / ad hoc λ |

---

## 2. Preferred Basis

**Problem:** Why position / pointer observables, not arbitrary bases?

| | |
|--|--|
| **Mainstream status** | Decoherence + system–environment interaction Hamiltonian selects pointer states |
| **Track U** | Clump–environment coupling aligns with interaction Hamiltonian |
| **Track C** | Collapse operators chosen to localize in pointer basis; must match decoherence basis or fail |
| **Sim leverage** | `preferred_basis_lab.py` |
| **Kill** | Clump structure picks a basis orthogonal to the interaction Hamiltonian |

---

## 3. Born Rule Origin

**Problem:** Why \(P(i) = |\langle i|\psi\rangle|^2\)?

| | |
|--|--|
| **Mainstream status** | Postulate, or derived in Everett (decision theory / envariance) with controversy |
| **Track U** | Clump-weighted sampling must recover Born within tolerance |
| **Track C** | CSL/localization statistics must recover Born for allowed λ band |
| **Sim leverage** | `born_rule_lab.py` |
| **Kill** | Systematic deviation from Born outside numerical noise |

---

## 4. Quantum–Classical Boundary

**Problem:** Where does the quantum stop and the classical begin?

| | |
|--|--|
| **Mainstream status** | No sharp cut; decoherence timescale + mass/complexity |
| **Track U** | Classical appearance = decohered pointer states relative to clumps |
| **Track C** | Collapse rate rises with clump density / mass-like parameter |
| **Sim leverage** | Environment coupling sweeps in `measurement_lab.py` |
| **Kill** | Sharp cut that contradicts decoherence scaling |

---

## 5. Nonlocality / Entanglement (No-Signaling)

**Problem:** Bell correlations without controllable faster-than-light signaling.

| | |
|--|--|
| **Mainstream status** | QM nonlocal correlations + no-signaling theorem |
| **Track U** | Unitary entangled evolution preserves no-signaling |
| **Track C** | Collapse must be carefully nonlocal (like GRW) or it enables signaling |
| **Sim leverage** | `entanglement_lab.py`, `no_signaling.py` |
| **Kill** | Any track that allows controllable signaling |

---

## 6. Reality of the Wavefunction

**Problem:** Is ψ ontic, epistemic, or neither?

| | |
|--|--|
| **Mainstream status** | Live debate (ψ-ontology theorems vs QBism/relational) |
| **Track U** | Field + universal state ontic; clumps are localized modes in/of the field |
| **Track C** | Wavefunction ontic until collapse; clumps drive localization |
| **Sim leverage** | Structural only (scoreboard ontology notes) |
| **Kill** | Incoherence with C0 (field as base) |

---

## 7. Time Asymmetry in Measurement

**Problem:** Microdynamics reversible; measurement records look irreversible.

| | |
|--|--|
| **Mainstream status** | Decoherence + thermodynamics / record formation |
| **Track U** | Irreversibility ≈ entanglement with environment relative to clump |
| **Track C** | Collapse explicitly breaks unitarity → arrow |
| **Sim leverage** | Entropy of pointer-reduced state over time |
| **Kill** | Claiming fundamental time-asymmetry without recovering thermodynamics of records |

---

## 8. Quantum Gravity / Spacetime Emergence

**Problem:** How do spacetime and gravity relate to quantum theory?

| | |
|--|--|
| **Mainstream status** | Open; many programs (AdS/CFT, causal sets, etc.) |
| **Track U / C** | Speculative: clumps as seeds of localized spacetime regions |
| **Sim leverage** | Deferred (Q9–Q12 light stubs) |
| **Kill** | Overclaiming gravity solutions from toy qubit models |

**Weight in scoreboard:** low until later versions.

---

## Scoreboard Problem Weights

| Problem | Weight |
|---------|--------|
| Measurement / definite outcomes | 0.20 |
| Preferred basis | 0.15 |
| Born rule | 0.25 |
| Quantum–classical boundary | 0.10 |
| No-signaling / entanglement | 0.20 |
| Wavefunction reality | 0.05 |
| Time asymmetry | 0.05 |
| Quantum gravity | 0.00 (reserved) |

Born + no-signaling + decoherence-compatibility dominate because they are the least negotiable constraints in physics today.
