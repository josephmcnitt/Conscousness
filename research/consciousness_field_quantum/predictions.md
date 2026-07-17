# Part VIII Predictions (Q1–Q12, M1–M8)

Quantitative / structural predictions for consciousness-field + clumping + Metzinger awareness-matter bridge.

**Status key:** Pending | Supported (sim) | Failed (sim) | Deferred

All sim support is **in-silico only**.

---

## Q1 — Track U Off-Diagonal Decay

Under Track U, off-diagonal elements of ρ in the pointer basis decay with environment coupling γ; clump amplitude A correlates with experiential/pointer definiteness, **not** with an extra dynamical collapse term.

- **Lab:** `measurement_lab.py`
- **Pass:** purity ↓ / offdiag ↓ as γ ↑; A modulates selection weights only
- **Fail:** requiring λ > 0 to get classical pointer statistics

## Q2 — Track C Born Band

Track C recovers Born statistics only inside a finite λ band (function of A). Outside the band, Born total variation exceeds tolerance.

- **Lab:** `born_rule_lab.py`, `collapse_csl.py`
- **Pass:** sweet-spot λ; failure outside
- **Fail:** Born fit for all λ (unfalsifiable) or none

## Q3 — Preferred Basis Alignment

Preferred / pointer basis aligns with clump–environment interaction structure, not with an arbitrary rotated basis.

- **Lab:** `preferred_basis_lab.py`
- **Pass:** decoherence in interaction basis ≫ rotated basis
- **Fail:** clump “selects” a basis orthogonal to Hint

## Q4 — Entanglement No-Signaling

For entangled pairs, Track U preserves no-signaling. Track C fails if collapse is naively clump-triggered on one wing without proper nonlocal CSL structure.

- **Lab:** `entanglement_lab.py`
- **Pass U:** signaling score ≈ 0
- **Pass C:** carefully constructed CSL-like update also ≈ 0; naive local collapse flagged

## Q5 — Classical Limit

High environment coupling → high pointer classicality (low off-diagonals, high pointer purity of reduced mixtures).

- **Lab:** `measurement_lab.py`
- **Pass:** monotonic classicality vs γ

## Q6 — Multi-Clump Coupling

Two clumps coupled to the same system share correlated records without enabling signaling between clump “agents” beyond QM correlations.

- **Lab:** `entanglement_lab.py` (Wigner-friend lite / two-observer)
- **Pass:** correlated outcomes; no-signaling holds

## Q7 — Time Asymmetry Proxy

Pointer-basis von Neumann entropy of the system (or system+clump record) increases under decoherence even though underlying unitary+env model is CPTP.

- **Lab:** `measurement_lab.py`
- **Pass:** entropy_pointer non-decreasing with time under γ > 0

## Q8 — Wigner-Friend Toy

Nested observer (friend measures, Wigner describes superposition) yields Track U branch structure vs Track C definite friend outcome before Wigner measures — different predictions for Wigner’s expected interference.

- **Lab:** stub in `measurement_lab.py` / scoreboard notes
- **Pass:** tracks diverge on interference visibility parameter

## Q9 — Gravity Stub (Deferred)

Clumps as seeds of localized spacetime regions — qualitative only until a concrete model exists.

- **Status:** Deferred
- **Kill:** claiming QG resolution from qubit toys

## Q10 — Field Excitation Bridge

Clump amplitude A and FEO mode stability should be correlationally mappable (optional import from Part III metrics) without identifying Φ with Tr(ρ²).

- **Status:** Light stub / documentation bridge
- **Fail:** silently equating purity with phenomenal Φ

## Q11 — Mind-Change Link (Part V)

Evidence that would raise/lower credence in C0: sustained Born+no-signaling survival of U; empirical collapse signatures favoring C; or G1-style elimination of experience.

- **Doc bridge:** [`../mind_change_criteria.md`](../mind_change_criteria.md)
- **Status:** Structural

## Q12 — Scoreboard Winner Stability

Across seeds, Track U weighted score ≥ Track C unless C shows clear Born+signaling superiority (unexpected).

- **Lab:** `track_comparison_scoreboard.py`
- **Pass:** U wins or ties on hard constraints; C only wins if it beats U on Born+signaling without occult λ tuning

---

## Summary Table

| ID | Focus | Primary lab |
|----|-------|-------------|
| Q1 | U off-diagonals | measurement |
| Q2 | C Born band | born_rule |
| Q3 | Preferred basis | preferred_basis |
| Q4 | No-signaling | entanglement |
| Q5 | Classical limit | measurement |
| Q6 | Multi-clump | entanglement |
| Q7 | Time asymmetry | measurement |
| Q8 | Wigner-friend | measurement |
| Q9 | Gravity | deferred |
| Q10 | FEO bridge | docs |
| Q11 | Mind-change | docs |
| Q12 | Scoreboard stability | scoreboard |

---

## Metzinger Bridge Predictions (M1–M8)

Layered awareness-matter sector. See [`METZINGER_BRIDGE.md`](METZINGER_BRIDGE.md).

### M1 — MPE Profile Match

MPE factory (high \(w\), low \(\kappa\), \(\sigma_{\mathrm{self}}\approx 0\)) matches MPE constraint profile and `is_mpe_active`.

- **Lab:** `metzinger_layer_lab.py`
- **Pass:** wakefulness high, low-complexity high, selfhood/perspectival low, MPE predicate true
- **Fail:** MPE factory scores as PSM-active

### M2 — MPE → PSM Transition

Raising \(\sigma_{\mathrm{self}}\) and \(\tau\) from an MPE seed activates PSM; ownership rises.

- **Lab:** `metzinger_layer_lab.py`
- **Pass:** not PSM before; PSM after; ownership increases
- **Fail:** promotion leaves selfhood near zero

### M3 — PMIR Off Weakens Pointer Alignment

PMIR-off (low \(\pi,\iota\)) yields weaker pointer-alignment score than PMIR-on; preferred-basis interaction alignment still required.

- **Lab:** `awareness_matter_qm_lab.py`
- **Pass:** `pointer_alignment(PMIR) > pointer_alignment(PMIR-off) + 0.3`
- **Fail:** PMIR order parameters do not affect alignment strength

### M4 — Track U Born Across Layers

Selection-weight sampling under MPE / PSM / PMIR stays within Born TV tolerance (0.08).

- **Lab:** `awareness_matter_qm_lab.py`
- **Pass:** TV ≤ 0.08 for all three layer factories
- **Fail:** any layer regime systematically breaks Born

### M5 — Track C \(\rho_A\) Preserves Signaling Hard-Fail

Using \(\rho_A\) for \(\lambda\) still leaves Track U no-signaling intact and naive local collapse flagged as signaling.

- **Lab:** `awareness_matter_qm_lab.py`
- **Pass:** signaling_U ≈ 0 and naive collapse score high (continuity with Q4)
- **Fail:** \(\rho_A\) coupling invents controllable signaling under Track U

### M6 — Wigner Grades Diverge

MPE-grade vs PSM-grade friend diverge on Track U interference / classical-lock proxies.

- **Lab:** `metzinger_layer_lab.py`
- **Pass:** interference proxy (MPE friend) > interference proxy (PSM friend) by margin
- **Fail:** grades identical under shared decoherence

### M7 — Classical Lock

High transparency + high decoherence classicality → high classical-lock score.

- **Lab:** `metzinger_layer_lab.py`
- **Pass:** lock(high γ) > lock(low γ) + margin; lock(high) ≥ 0.5
- **Fail:** transparency does not modulate classical appearance proxy

### M8 — Complexity Without Self ≠ PSM

High \(\kappa\) with \(\sigma_{\mathrm{self}}\) near 0 is **not** PSM-active (guards false self-ascription).

- **Lab:** `metzinger_layer_lab.py`
- **Pass:** `is_psm_active` false for high-complexity no-self factory
- **Fail:** content richness alone triggers PSM predicate

---

## Summary Table (M)

| ID | Focus | Primary lab |
|----|-------|-------------|
| M1 | MPE profile | metzinger_layer |
| M2 | MPE→PSM | metzinger_layer |
| M3 | PMIR pointer | awareness_matter_qm |
| M4 | Born layers | awareness_matter_qm |
| M5 | Track C signaling | awareness_matter_qm |
| M6 | Wigner grades | metzinger_layer |
| M7 | Classical lock | metzinger_layer |
| M8 | No false PSM | metzinger_layer |

