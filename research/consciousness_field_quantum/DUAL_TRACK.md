# Dual Track: Unitary vs Collapse-Clumping

**Part VIII** | Adversarial comparison with physics-weighted scoring

---

## Tracks

### Track U — Unitary / Decoherence (Primary, ~70%)

**Claim:** Clumps select which outcome is *experienced*. Quantum dynamics remain unitary. Decoherence + pointer basis explain classical appearance. Closest to mainstream interpretive practice (Everett / relational / decoherence-first).

**Dynamics:**

\[
\dot\rho = -i[H,\rho] + \mathcal{D}_\mathrm{env}[\rho]
\]

Clump amplitude \(A\) correlates with *definiteness of experience relative to a pointer basis*, not with an extra collapse term.

### Track C — Collapse-Clumping (Adversary, ~30%)

**Claim:** Clump localization participates in producing definite outcomes. Collapse/localization rate rises with clump density (CSL-inspired):

\[
\lambda(A) = \lambda_0 \cdot A^\alpha
\]

Must still match Born frequencies and no-signaling.

---

## Why U is Weighted Higher

| Reason | Effect on scoreboard |
|--------|----------------------|
| Decoherence + unitary evolution is textbook practice | Higher base prior for U |
| Consciousness-collapse is fringe in physics | Occam / acceptance penalty for C |
| Objective collapse (GRW/CSL) is more respectable than Wigner-consciousness | C modeled as CSL-like, not “mind magic” — still secondary |
| Born + no-signaling are non-negotiable | Equal hard constraints for both |

---

## Scoreboard Metrics

| Metric | Weight | Notes |
|--------|--------|-------|
| Born fit | 0.30 | \(\mathrm{TV}(P_\mathrm{sim}, P_\mathrm{Born})\) small |
| No-signaling | 0.25 | Marginal of distant party independent of local choice |
| Decoherence match | 0.20 | Off-diagonal decay with \(\gamma\) (U native; C must not contradict) |
| Classical limit | 0.10 | High env coupling → pointer purity / low coherence |
| Preferred-basis alignment | 0.10 | Clump basis vs \(H_\mathrm{int}\) |
| Occam / physics-acceptance | 0.05 | Flat bonus to U; C pays penalty unless it outperforms |

Total score ∈ [0, 1]. Winner = higher weighted score. Ties broken by Born + no-signaling.

---

## Kill Conditions

- **Either track:** Born violation beyond tolerance; signaling detected
- **Track U:** Cannot operationalize “selection” without preferred-basis cheat that fails `preferred_basis_lab`
- **Track C:** Only fits Born for pathological λ; or λ must be tuned per experiment with no unifying rule

---

## Implementation Map

| Component | Track U | Track C |
|-----------|---------|---------|
| `equations/decoherence.py` | Primary | Shared env channel |
| `equations/collapse_csl.py` | Unused / baseline λ=0 | Primary |
| `equations/clumping.py` | Selection weight | λ(A) input |
| Labs | Both | Both |
| `track_comparison_scoreboard.py` | Head-to-head | Head-to-head |

---

## Honest Framing

Track U is **favored a priori** by physics acceptance, not by proof of a consciousness field. Track C is kept alive to be **scored and possibly eliminated**, not to be sneered out of the arena without equations.
