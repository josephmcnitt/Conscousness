# Qualia Cartography — Periodic Table of Experiential Invariants

Part VI shared vocabulary for the Hard Problem Protocol. **Not** a claim to have mapped real qualia — a target list for adversarial tests.

Cross-links: [`IMAGINATION_AND_THE_ASTRAL.md`](IMAGINATION_AND_THE_ASTRAL.md), [`CREATIVITY_AND_CONSCIOUSNESS.md`](CREATIVITY_AND_CONSCIOUSNESS.md), [`hard_problem_protocol.md`](hard_problem_protocol.md)

---

## Purpose

The hard problem stalls when "experience" is too coarse. This document names **invariants** — stable structural features of reported experience — so panpsychist, illusionist, and structural physicalist tracks predict the **same targets**.

---

## Invariant Table

| ID | Invariant | Example / paradigm | Panpsychist (Close) | Illusionist (Dissolve) | Structural (Bridge) |
|----|-----------|-------------------|---------------------|------------------------|---------------------|
| Q1 | **Transparency** | "I see red" not "I see a sense-datum" | Real presence; filter allows directness | Meta-cognition generates seeming of directness | Transparency = processing level in perceptual hierarchy |
| Q2 | **Valence** | Pain vs pleasure without belief change | Proto-valence intrinsic to excitation | Valence seeming tracks access states | Nociceptive/limbic map determines valence report |
| Q3 | **Unity** | Binding color + shape + motion | Integration (phi) yields unified subject | Unity seeming from access broadcast | Synchrony threshold binds features |
| Q4 | **Flow** | Csikszentmihalyi gap — effort vanishes | P10 inverted-U on excitation | Flow seeming = optimal access bandwidth | DMN/TPN balance predicts flow report |
| Q5 | **Insight** | Pre-conceptual "pop" before articulation | P11 excitation reorganization | Access reorg only; no pre-report qualia | Predictable pre-report neural signature |
| Q6 | **Bodily ownership** | Rubber hand, depersonalization | Filter/boundary failure (F2/P8) | Ownership seeming from body-model access | Somatosensory map + prediction error |
| Q7 | **Imaginal vividness** | Kosslyn high vs low imagers | P13 sub-threshold excitation | Imagery as weak perceptual access | Visual cortex activation pattern |
| Q8 | **Hypnagogic band** | Edge of sleep — imagery without full wake | P14 astral_band_index mid-range | Bleed seeming at access threshold | Alpha/theta transition signature |
| Q9 | **Suffering persistence** | Pain continues despite knowing it's harmless | P19 proto-valence decoupled from belief | Suffering seeming without self-update | C-fiber map persists; cognitive override separate |
| Q10 | **Combination unity** | Many micro-states feel like one subject | P22 integration > summing | N/A — no real unity to combine | Neural synchrony threshold for unity report |

---

## Mapping to Predictions

| Invariant | Primary prediction | Model / artifact |
|-----------|-------------------|------------------|
| Q3, Q4 | P10, P4 | `field_excitation_model.py` |
| Q5 | P11, P20 | `field_excitation_model.py`, `dissociation_hunt.py` |
| Q7 | P13 | `imaginal_excitation_model.py` |
| Q8 | P14 | `imaginal_excitation_model.py` |
| Q4, Q5 | P18 | `access_collapse_model.py` |
| Q9 | P19 | `dissociation_hunt.py` |
| Q1, Q6 | P21 | `dissociation_hunt.py` (spectrum inversion proxy) |
| Q10 | P22 | `combination_realization_lab.py` |

---

## Cartography Completeness Criterion (Track 3)

Structural physicalism **wins Bridge tier** when:

1. Every invariant Q1–Q10 has a pre-registered neural/computational signature
2. Signatures predict report **without** post-hoc relabeling across ≥3 dissociation scenarios
3. No systematic case where structure matches but invariant report diverges

Current status: **incomplete** — in-silico proxies only; human neurophenomenology protocol ready ([`empirical/neurophenomenology_protocol.md`](empirical/neurophenomenology_protocol.md)).

---

## Cartography Gaps (Honest)

| Gap | Why it matters |
|-----|----------------|
| Human neuroimaging data | Structural track untested on real brains |
| Inverted spectrum (Q1/P21) | Classic philosophical challenge; in-silico uses hash proxy only |
| AI reports | M14 — untrusted as cartography data |
| Mystical/peak states | Out of scope for adversarial battery v1 |

---

## Usage in HPP

1. `dissociation_hunt.py` scores each scenario against Q1–Q10 relevance tags
2. `adversarial_track_scores()` in `consciousness_metrics.py` aggregates per track
3. Highest **adversarial_value** scenarios drive ledger updates first

See [`HARD_PROBLEM_PROTOCOL.md`](HARD_PROBLEM_PROTOCOL.md) for tournament standings.
