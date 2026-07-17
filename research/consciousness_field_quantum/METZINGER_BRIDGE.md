# Metzinger Bridge (Part VIII Extension)

Layered Metzinger stack → **awareness-matter sector** wedged into Part VIII QM toys.

**Status:** Research ontology + in-silico diagnostics. Not a proof of a consciousness field. Not a phenomenal hard-problem solution (Part VI firewall).

---

## Thesis

Upgrade the thin Part VIII clump (amplitude / σ / stability) into a **typed auxiliary sector** whose order parameters encode Metzinger’s minimal-to-selfhood stack:

1. **MPE** — minimal phenomenal experience (awareness without self)
2. **PSM** — phenomenal self-model (transparent “being someone”)
3. **PMIR** — phenomenal model of the intentionality relation (centered subject→object)

Ordinary QM still acts on system density matrix \(\rho_S\). The observer is no longer an unexplained classical cut: it is an order-parameter sector \(A\) whose derived density \(\rho_A\) and pointer frame enter the same coupling rules already used by Tracks U and C.

---

## Mapping to Clumping Axioms

| Metzinger | Part VIII | Notes |
|-----------|-----------|-------|
| Unpartitioned epistemic capacity / tonic alertness | C0–C1 + **C4a** | MPE core of a clump |
| Transparent PSM | **C4b** (refines C4) | Macro self = high selfhood + transparency |
| PMIR / 1PP | **C2a** (refines C2) | Observation = PMIR-aligned pointer coupling |
| Transparency \(\tau\) | Track U experiential lock | Classical appearance when decoherence × \(\tau\) high |
| MPE without PSM | Wigner-friend grades | MPE-grade vs PSM-grade observers |

Full axioms: [`CLUMPING_ONTOLOGY.md`](CLUMPING_ONTOLOGY.md).

---

## Awareness Matter State

Geometric (C1) plus layered order parameters. See `equations/awareness_matter.py`.

| Symbol | Layer | Meaning |
|--------|-------|---------|
| \(A, \sigma, x, s\) | field | Amplitude, coherence length, center, mode stability |
| \(w\) | MPE | Wakefulness / tonic alertness |
| \(\kappa\) | MPE | Content complexity (low ≈ MPE) |
| \(\varepsilon\) | MPE | Epistemicity / epistemic-space model strength |
| \(\omega_m\) | MPE | Opacity of awareness-as-such (introspective availability) |
| \(\sigma_{\mathrm{self}}\) | PSM | Selfhood (0 = no-self MPE) |
| \(\tau\) | PSM | Transparency (1 = cannot see model as model) |
| \(\omicron\) | PSM | Ownership / mine-ness |
| \(\delta\) | PSM | Diachronic self-stability |
| \(\pi\) | PMIR | Perspectivalness (immovable center) |
| \(\iota\) | PMIR | Intentional arrow strength |

### Composite matter density \(\rho_A\)

\[
\rho_A = \frac{A \cdot w \cdot \bigl(1 + \alpha_1 \sigma_{\mathrm{self}} + \alpha_2 \pi\bigr)}{\sigma}
\]

with fixed coefficients \(\alpha_1 = 0.5\), \(\alpha_2 = 0.3\) (documented here; not free fit parameters per run).

- **MPE-only** (\(\sigma_{\mathrm{self}} = \pi = 0\)): \(\rho_A = A w / \sigma\) — recovers the spirit of `clump_density` when \(w \approx 1\).
- **Track C:** \(\lambda = \lambda_0 \rho_A^{\alpha}\) (same form as before).
- **Track U:** selection / definiteness use \(\rho_A\), \(\tau\), \(\pi\) as experiential overlays; physics Born fit still uses \(|c_i|^2\).

**v1 does not** introduce a Hilbert factor \(H_A\). Order parameters + coupling functionals are the QM-compatible wedge.

---

## Layer Predicates

| Predicate | Operational condition |
|-----------|------------------------|
| **MPE-active** | \(w \ge 0.7\), \(\kappa \le 0.3\), \(\sigma_{\mathrm{self}} \le 0.2\) |
| **PSM-active** | \(\sigma_{\mathrm{self}} \ge 0.6\), \(\tau \ge 0.5\) |
| **PMIR-active** | \(\pi \ge 0.6\), \(\iota \ge 0.5\) |

Constraint scorers: `equations/metzinger_constraints.py`. Labs: M1–M8 in [`predictions.md`](predictions.md).

---

## QM Coupling Rules

1. **Preferred basis** — PMIR sets observer pointer-frame alignment strength; kill if frame is orthogonal to \(H_{\mathrm{int}}\).
2. **Born** — Track U experiential weights may use \((\rho_A, \tau, \pi)\); TV vs Born must stay within existing tolerance.
3. **Classical lock** — classical appearance \(\propto\) decoherence × \(\tau\) × mode stability.
4. **Wigner grades** — MPE-grade friend (no PSM) vs PSM-grade friend (PSM+PMIR) diverge on interference proxies under Track U.
5. **Track C λ** — driven by \(\rho_A\); naive local collapse still hard-fails no-signaling.

---

## Literature Anchors

| Source | Use here |
|--------|----------|
| Metzinger — *Being No One* | PSM, PMIR, transparency, first-person perspective |
| Metzinger — MPE (2020); *The Elephant and the Blind* (2024) | Minimal model; pure awareness without self |
| Blanke & Metzinger — bodily self / minimal self | Ownership / self-location vocabulary |
| Sandved-Smith et al. — computational MPE (FEP) | Parallel computational neurophenomenology; **not** a dependency |

See [`literature_map.md`](literature_map.md).

---

## Firewall

- Simulations ≠ empirical QM confirmation
- Awareness matter ≠ Standard Model field
- No AI consciousness claim
- Part VI hard problem remains firewalled
- Track U vs C scoring stays adversarial; Metzinger layers do not force Track C to win
