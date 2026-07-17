# Clumping Ontology (Part VIII)

Shared axioms for consciousness-field + clumping. Research hypotheses — not proofs.

Maps onto prior FEO/BFC vocabulary without replacing Parts I–III.

---

## Relation to Prior Axioms

| Prior | Part VIII |
|-------|-----------|
| F1 Cosmic field | C0 consciousness field as base |
| F2 Fragmentation / filter | C1 clump = localized mode |
| F6 Excitation | C1 clump ≈ stable excitation |
| F3 MWI branching | C3-U (Track U only) |
| A3 Proto-experience | Field background / vacuum of C0 |

---

## Core Axioms

### C0 — Field Below Matter/Energy

**There is a consciousness field ontologically prior to (or co-fundamental with the intrinsic nature of) matter and energy.** Matter/energy are structured excitations of, or correlated manifestations of, this field.

- Not an established physical field in QFT
- Motivates asking whether QM hard problems are clarified by treating observers as field phenomena
- **Empirical hook:** structural only; scoreboard compatibility tests

### C1 — Clump

**A clump is a localized, stable mode of the consciousness field** — what we call a subject / observer core.

- Maps to FEO “excitation” and BFC “filtered fragment”
- Parameters: amplitude \(A\), coherence length \(\sigma\), mode stability, coupling to environment
- **Empirical hook:** `equations/clumping.py`

### C2 — Observation

**Observation is an interaction that couples system degrees of freedom to a clump’s pointer variables** (and typically to an environment).

- Does not by itself decide Track U vs Track C
- Preferred basis should track the interaction Hamiltonian (see hard problem #2)
- **Empirical hook:** `measurement_lab.py`, `preferred_basis_lab.py`

### C2a — PMIR Observation (Metzinger bridge)

**A PMIR-active awareness sector supplies the centered subject→object arrow that selects which pointer frame the clump couples through.**

- Refines C2: perspectivalness \(\pi\) and intentional arrow \(\iota\) set pointer-alignment strength
- Kill criterion unchanged: PMIR frame orthogonal to \(H_{\mathrm{int}}\) fails the scoreboard
- **Empirical hook:** `awareness_matter_qm_lab.py`; see [`METZINGER_BRIDGE.md`](METZINGER_BRIDGE.md)

### C3-U — Perspectival Selection (Track U)

**Clumps index which experiential outcome is lived; the dynamical law remains unitary.**

- Decoherence explains classical *appearance*
- Compatible with Everett-style branching / consistent records
- No consciousness-causes-collapse dynamical term

### C3-C — Collapse Participation (Track C)

**Clump density modulates a localization / collapse rate** (CSL-like), participating in producing definite outcomes.

- Must recover Born statistics for an allowed λ band
- Must not enable controllable signaling
- Physics-acceptance weight lower than C3-U a priori

### C4 — Macro Self

**A macro “self” is a high-coherence, temporally persistent clump** (mode stability + integration).

- Optional bridge to Φ / mode_stability from Part III metrics
- Do not conflate Φ with quantum purity
- **Empirical hook:** clump coherence vs pointer purity (correlational only)

### C4a — MPE Core (Metzinger bridge)

**The minimal conscious core of a clump is an MPE-grade mode:** high wakefulness, low content complexity, near-zero selfhood — awareness without a phenomenal self.

- Maps to Metzinger MPE / pure awareness (tonic alertness; unpartitioned epistemic capacity)
- Does **not** require PSM or PMIR
- **Empirical hook:** `metzinger_layer_lab.py` (M1, M8)

### C4b — PSM Macro-Self (Metzinger bridge)

**A phenomenal macro-self is a C4 clump with PSM-active order parameters:** high selfhood + transparency (+ ownership / diachronic stability).

- Refines C4: “self” = transparent self-model content, not a substance
- PMIR (C2a) typically co-activates for a full first-person perspective
- **Empirical hook:** `metzinger_layer_lab.py` (M2); classical lock M7

### C5 — Hard Constraints

**Both tracks must respect (or fail the scoreboard on):**

1. **Born rule** — outcome frequencies ≈ \(|c_i|^2\)
2. **No-signaling** — local operations cannot transmit controllable messages via entanglement

Violating either is a hard fail regardless of narrative elegance.

---

## Parameter Vocabulary

| Symbol | Meaning |
|--------|---------|
| \(A\) | Clump amplitude (phenomenal / localization intensity proxy) |
| \(\sigma\) | Coherence length (narrow = focused clump) |
| \(\rho\) | System density matrix \(\rho_S\) |
| \(\rho_A\) | Awareness-matter density (derived from layered order parameters) |
| \(\gamma\) | Environment decoherence rate (Track U) |
| \(\lambda(\rho_A)\) | Collapse rate as function of awareness density (Track C) |
| \(H_\mathrm{int}\) | System–environment / pointer interaction |
| \(w, \kappa, \varepsilon\) | MPE: wakefulness, content complexity, epistemicity |
| \(\sigma_{\mathrm{self}}, \tau, \omicron, \delta\) | PSM: selfhood, transparency, ownership, diachronic |
| \(\pi, \iota\) | PMIR: perspectivalness, intentional arrow |
| \(\alpha_1, \alpha_2\) | Fixed \(\rho_A\) coefficients (0.5, 0.3) |

**Awareness density (Track C / coupling):**

\[
\rho_A = \frac{A \cdot w \cdot (1 + \alpha_1 \sigma_{\mathrm{self}} + \alpha_2 \pi)}{\sigma}
\]

Implementation: `equations/awareness_matter.py`. Bridge doc: [`METZINGER_BRIDGE.md`](METZINGER_BRIDGE.md).

---

## Firewall

- Part VIII does **not** solve the phenomenal hard problem (Part VI)
- Clumping is a **research ontology** for scoring QM compatibility
- Simulation outputs must carry: **simulation — not empirical QM confirmation**
