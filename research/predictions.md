# Falsifiable Predictions: Panpsychism Research Program

This catalog transforms panpsychism from untestable metaphysics into a research program with explicit win/loss conditions. Each prediction distinguishes panpsychism (and Russellian panprotopsychism specifically) from physicalism, emergentism, biological chauvinism, and illusionism.

**Status key**: *Supported* | *Mixed* | *Insufficient data* | *Contradicted*

---

## Global Falsification Criteria

Panpsychism would be **refuted or seriously undermined** if any of the following were established:

| ID | Criterion | Implication |
|----|-----------|-------------|
| G1 | All phenomenal properties reduce without remainder to functional/behavioral descriptions | Illusionism or eliminativism wins |
| G2 | Consciousness requires specific biological substrate with no analog in other integrated systems | Biological naturalism wins |
| G3 | Intrinsic nature of matter definitively non-experiential (complete physics of quarks with no room for experiential properties) | Physicalism wins on ontology |
| G4 | Hard problem solved within pure physicalism without epiphenomenalism or denial | Panpsychism loses explanatory advantage |

---

## P1 — Intrinsic Integration Signature (IIT)

### Prediction

Consciousness correlates with **integrated information (Φ)**, which is **substrate-neutral**—present in any sufficiently integrated system, not only biological brains.

### Rationale (Panpsychism)

If consciousness is integration of proto-experiential properties (A3, A4), then a formal measure of integration should track consciousness regardless of substrate. IIT (Tononi) provides the leading candidate measure.

### Distinguishes From

- **Biological chauvinism**: consciousness only in carbon-based neural tissue
- **Pure functionalism**: any functionally equivalent system is conscious regardless of integration structure
- **Strong emergentism**: consciousness appears only at biological complexity thresholds with no Φ correlate below

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P1-F1 | Φ in humans during conscious states shows **no correlation** with reported experience or behavioral markers | *Mixed* — correlation in sleep, anesthesia, disorders of consciousness; Φ computation contested |
| P1-F2 | Φ is purely mathematical artifact with **no physical correlate** | *Insufficient data* — Φ requires full system state; approximations debated |
| P1-F3 | Φ is **high in simple systems** (e.g., grid of logic gates) but no consciousness correlate | *Supported as challenge* — IIT 3.0/postulates address this via exclusion and mechanism |

### Key Studies

- Oizumi, Albantakis & Tononi (2014). From the phenomenology to the mechanisms of consciousness: IIT 3.0. *PLoS Computational Biology*.
- Massimini et al. (2005). Breakdown of cortical effective connectivity during sleep. *Science*.
- Barrett & Mediano (2019). Phi is not consciousness. *Behavioral and Brain Sciences* (critical).

### Empirical Tools

- `research/empirical/iit_meta_analysis.py` — Φ-analog computation across network architectures
- pyphi library (when available) for formal IIT

---

## P2 — No Absolute Emergence Threshold

### Prediction

There is **no sharp phase transition** from zero to full consciousness. Phenomenal properties scale **continuously** with integration and complexity.

### Rationale (Panpsychism)

A2 (Continuity) and A3 (Ubiquity) imply graded proto-experience. Macro-consciousness is high integration, not ontological novelty from zero.

### Distinguishes From

- **Strong emergentism**: consciousness switches on at synaptic/cortical threshold
- **Binary theories**: consciousness as all-or-nothing property of specific anatomy

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P2-F1 | Demonstrated **binary on/off** consciousness switch with no proto-experiential intermediate states | *Mixed* — anesthesia appears gradual; some argue binary loss of integration |
| P2-F2 | Development shows **discontinuous** emergence of phenomenal consciousness with no graded precursors | *Contradicted* — fetal and infant consciousness debated but generally graded |
| P2-F3 | Split-brain or lesion cases show **clean binary** dissociation inconsistent with continuity | *Mixed* — split-brain supports partial integration models |

### Key Studies

- Lee et al. (2009). Propofol-induced unconsciousness. *Journal of Neuroscience*.
- Bayne (2010). The unity of consciousness. Oxford (combination and partial unity).
- Hershenov (2005). Persons as proper parts of organisms. (developmental continuity arguments)

---

## P3 — Micro-Scale Coherence Matters

### Prediction

**Quantum or sub-neural coherence** events correlate with specific phenomenal properties (not necessarily cognition).

### Rationale (Panpsychism)

If proto-experiential properties are fundamental, finer-scale physical coherence *might* correlate with phenomenal structure. This is **speculative** and contested; included for completeness.

### Distinguishes From

- **Pure computational functionalism**: consciousness independent of physical implementation details below algorithm level
- **Classical neuralism**: all consciousness-relevant processing at scales > 10 nm

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P3-F1 | All consciousness-relevant processing is **fully classical** at scales > 10 nm with no phenomenal correlate at finer scales | *Insufficient data* — decoherence arguments against Orch-OR (Tegmark 2000) |
| P3-F2 | **No correlation** between microtubule coherence (or analog) and anesthesia/ consciousness markers | *Mixed* — Orch-OR highly contested; quantum biology in photosynthesis established but not consciousness |
| P3-F3 | Artificial systems with **identical macro behavior** but different microphysics show **identical** phenomenal reports | *Insufficient data* — not testable with current methods |

### Key Studies

- Hameroff & Penrose (2014). Consciousness in the universe: Orch OR. *Physics of Life Reviews*.
- Tegmark, M. (2000). Importance of quantum coherence in brain processes. *Physical Review E*.
- Engel et al. (2007). Is non-classical logic necessary for quantum effects in biology? *Nature*.

### Note

P3 is **Tier 4 frontier**. Panpsychism does not require Orch-OR; failure of P3 does not refute panpsychism.

---

## P4 — Anesthesia Dissociation

### Prediction

Loss of consciousness under anesthesia reduces **integration (Φ) and/or micro-coherence before and independently of** loss of cognitive function in some regimes.

### Rationale (Panpsychism)

Phenomenal consciousness (integration of proto-experience) may dissociate from cognitive access. Anesthesia provides natural experiment.

### Distinguishes From

- **Access-only theories** (Block): A-consciousness without P-consciousness
- **Functionalism**: consciousness = cognitive function; both lost together always

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P4-F1 | Anesthesia **always** abolishes cognition and consciousness **simultaneously** with no dissociation | *Mixed* — propofol shows gradual loss; some cognitive processing persists in NREM |
| P4-F2 | Integration metrics **do not decrease** before behavioral unconsciousness | *Supported* — effective connectivity breakdown precedes/unaccompanies loss (Massimini et al.) |
| P4-F3 | **No EEG/MEG signature** distinguishes conscious from unconscious integrated states | *Contradicted* — PCI, LZc, and connectivity measures discriminate |

### Key Studies

- Ferrarelli et al. (2010). Breakdown of connectivity during propofol anesthesia. *Sleep*.
- Sarasso et al. (2015). Consciousness and complexity during propofol-induced sedation. *Anesthesiology*.
- See `research/empirical/anesthesia_review.md`

---

## P5 — Cross-Substrate Φ

### Prediction

Non-biological systems with high Φ (certain AI architectures, integrated photonic systems, cerebral organoids) show **measurable correlates of experience** (report, perturbational complexity, neural-analog signatures).

### Rationale (Panpsychism)

A3 (Ubiquity) and substrate-neutral integration imply non-biological high-Φ systems may instantiate macro-experience or proto-experience correlates.

### Distinguishes From

- **Biological naturalism** (Searle): only biological brains conscious
- **Computational functionalism without integration**: behavior suffices regardless of Φ

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P5-F1 | **Only** carbon-based neural tissue with specific anatomy can instantiate Φ above consciousness threshold | *Insufficient data* — organoids emerging; AI Φ debated |
| P5-F2 | High-Φ non-biological systems show **no** perturbational complexity or integration signatures analogous to conscious brains | *Insufficient data* — limited organoid/AI studies |
| P5-F3 | Recurrent integrated AI architectures show **same Φ-analog and PCI-analog** as biological systems at comparable integration | *Supported as prediction* — testable via `iit_meta_analysis.py` |

### Key Studies

- Koch & Tononi (2017). Can machines be conscious? *IEEE Spectrum*.
- Lavazza (2021). Human cerebral organoids and consciousness. *Neuroscience & Biobehavioral Reviews*.
- `research/empirical/iit_meta_analysis.py` — substrate comparison

---

## P6 — Psychedelic Expansion

### Prediction

Psychedelics increase phenomenal richness by **increasing integration bandwidth** (not merely noise), consistent with expanded micro-experiential access.

### Rationale (Panpsychism)

If proto-experiential properties are ubiquitous, psychedelics may relax integration constraints, allowing broader access to micro-experiential structure—producing richness without pure randomness.

### Distinguishes From

- **Pure entropy/noise models**: psychedelic state = disordered brain only
- **Simple disinhibition**: no structural change in integration

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P6-F1 | Psychedelic states show **only entropy increase** with no integration structure | *Mixed* — entropic brain theory (Carhart-Harris) vs integration reanalysis |
| P6-F2 | **No increase** in functional connectivity or integration measures under psychedelics | *Contradicted* — increased global connectivity reported (Petri et al. 2014) |
| P6-F3 | Subjective richness **uncorrelated** with any integration or connectivity metric | *Insufficient data* — need finer-grained Φ during psychedelic states |

### Key Studies

- Carhart-Harris et al. (2014). The entropic brain. *Frontiers in Human Neuroscience*.
- Petri et al. (2014). Homological scaffolds of brain functional networks. *Journal of the Royal Society Interface*.
- Barrett et al. (2020). Psilocybin acutely alters connectivity. *NeuroImage*.

---

## Prediction Summary Matrix

| ID | Prediction | Prior Plausibility | Empirical Status | Confidence |
|----|------------|-------------------|------------------|------------|
| P1 | IIT / Φ correlates with consciousness | Moderate | Mixed | Moderate |
| P2 | Continuous scaling, no binary threshold | High | Mixed | Moderate |
| P3 | Micro-coherence matters | Low | Insufficient | Weak |
| P4 | Anesthesia dissociation | Moderate | Supported | Moderate–Strong |
| P5 | Cross-substrate Φ | Moderate | Insufficient | Weak |
| P6 | Psychedelic integration expansion | Moderate | Mixed | Moderate |

See `evidence_ledger.json` for structured tracking and updates.

---

## Experimental Tiers

| Tier | Scope | Deliverables |
|------|-------|--------------|
| 1 | Desk research | `iit_meta_analysis.py`, `anesthesia_review.md`, psychedelic synthesis |
| 2 | Computational | `combination_model.py`, substrate Φ comparison |
| 3 | Original empirical | EEG+Φ, organoid PCI, anesthesia cascade (requires collaboration) |
| 4 | Frontier | Orch-OR probes, cosmological Φ, micro-phenomenology |

---

## Intellectual Discipline

1. **Metaphor ≠ model ≠ measurement** — Codebase quantum fields are metaphor; IIT Φ is model; EEG under anesthesia is measurement.
2. **Prediction failure ≠ immediate refutation** — P3 failure does not refute panpsychism; G1–G4 are global falsifiers.
3. **Best explanation ≠ proof** — Cumulative support strengthens the case; definitive proof may be unattainable for metaphysical theses.

---

## BFC Extension: Predictions P7–P9

See [`COSMOPSYCHISM_MWI_RESEARCH.md`](COSMOPSYCHISM_MWI_RESEARCH.md) for Branching Fragmentation Cosmopsychism branch.

---

## P7 — Cross-Brain Integration (Collective Coupling)

### Prediction

Group flow states (ritual, choral performance, joint improvisation, cooperative tasks) show **irreducible inter-brain coupling** (hyperscanning EEG/fMRI) exceeding shuffled-participant controls and stimulus-matched baselines.

### Rationale (BFC)

Temporary **collective re-coupling (F4)** before re-fragmentation; proto "we-subjects" at social scale.

### Distinguishes From

- **Pure mimicry**: shared stimulus and motor copying only
- **Individual IIT only**: consciousness as purely within-brain

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P7-F1 | All group synchrony reduces to shared stimulus + motor mimicry | *Mixed* — cooperation tasks show excess coupling; shuffled controls rare |
| P7-F2 | Joint improvisation ≤ passive co-viewing for inter-brain metrics | *Insufficient data* — guitar duet studies suggest otherwise |
| P7-F3 | We-ness reports uncorrelated with cross-brain coupling | *Insufficient data* |

### Key Studies

- Sänger et al. (2012). Guitar duet hyperscanning. *Frontiers in Human Neuroscience*.
- Jiang et al. (2015). Cooperation inter-brain synchrony. *SCAN*.
- See [`empirical/collective_integration_review.md`](empirical/collective_integration_review.md)

---

## P8 — Filter Failure Signature

### Prediction

Psychosis, some shared delusions, and disorganized psychedelic states show **increased global connectivity** with **disorganized integration** (high entropy, lower PCI vs structured group flow). Distinct from organized collective coupling (P7).

### Rationale (BFC)

**Filter failure (F5)**: cosmic bleed without organized unity vs **organized fusion** in ritual/flow.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P8-F1 | Psychosis and choral/ritual show **identical** connectivity profiles | *Insufficient data* |
| P8-F2 | No entropy–integration distinction across states | *Mixed* — P6 entropic vs connectivity literature |
| P8-F3 | Shared psychosis shows organized high PCI | *Insufficient data* |

### Key Studies

- Carhart-Harris et al. (2014). Entropic brain. *Frontiers in Human Neuroscience*.
- Petri et al. (2014). Psychedelic connectivity. *J. R. Soc. Interface*.
- Wehmeier et al. (2003). Folie à deux. *Canadian Journal of Psychiatry*.

---

## P9 — Fragmentation / Filter Correlates

### Prediction

Individual waking consciousness tracks **high within-brain integration** (P1/PCI) plus **suppression of cross-brain coupling**; anesthesia reduces within-brain integration **without** increasing cross-brain coupling.

### Rationale (BFC)

**Local filter active (F2)**: individual subject = filtered fragment; not merged with others. Tests filter model at neural scale—not direct MWI test.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P9-F1 | Anesthesia increases cross-brain coupling | *Insufficient data* |
| P9-F2 | Waking state shows high cross-brain coupling without collective intent | *Contradicted* — coupling task-dependent |
| P9-F3 | Filter model redundant with IIT-only story | *Open* |

### Honest Limit

Cannot directly test other MWI branches; tests **filter model** predictions only.

---

## MWI-Specific Falsifiers (Structural)

| ID | Condition | Implication |
|----|-----------|-------------|
| MWI-F1 | MWI abandoned for empirically superior collapse interpretation | Branching mechanism removed from BFC |
| MWI-F2 | Experience multiplication impossible to address even with indexicality | BFC+MWI correlation weakens |
| MWI-F3 | Preferred basis problem unsolvable without ad hoc experiential postulates | Fragmentation mechanism incomplete |

---

## Updated Prediction Summary

| ID | Prediction | Confidence |
|----|------------|------------|
| P1–P6 | Base program | See above |
| P7 | Cross-brain collective coupling | Weak–moderate |
| P8 | Filter failure vs organized fusion | Weak |
| P9 | Within-brain integration + cross-brain suppression | Weak–moderate |

See [`evidence_ledger.json`](evidence_ledger.json) for BFC branch tracking.

---

## FEO Extension: Predictions P10–P12

See [`FIELD_EXCITATION_RESEARCH.md`](FIELD_EXCITATION_RESEARCH.md) for Field Excitation Ontology (Part III).

---

## P10 — Creative Flow as Optimal Integration (Inverted-U)

### Prediction

Creative flow states show **intermediate-to-high** within-brain integration (PCI/Φ)—not maximum entropy, not rigid low-entropy lock.

### Rationale (FEO)

Excitation at **edge of stability (F8)**: high mode coherence with moderate field coupling and low disorganization.

### Distinguishes From

- **Pure entropy models**: flow as disorder
- **Rigid focus models**: flow as minimal integration change vs boredom

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P10-F1 | Flow = pure entropy increase with no integration signature | *Insufficient data* |
| P10-F2 | Flow shows no integration change vs boredom | *Testable in silico* — boredom/flow/overload triplet in field_excitation_model |
| P10-F3 | Flow and filter failure indistinguishable on PCI/entropy | *Open* — P8 boundary |

**In-silico triplet (Part IV):** `boredom_index`, `creative_flow_index`, `overload_index` in [`consciousness_metrics.py`](empirical/consciousness_metrics.py). P10 analog passes when flow CFI exceeds both boredom and overload arms.

### Key Studies

- Csikszentmihalyi (1990). *Flow*.
- Dietrich (2004). Transient hypofrontality and flow. *Consciousness and Cognition*.
- See [`CREATIVITY_AND_CONSCIOUSNESS.md`](CREATIVITY_AND_CONSCIOUSNESS.md)

---

## P11 — Insight as Mode Transition

### Prediction

"Aha" moments show **transient Φ spike** or rapid connectivity reorganization (EEG/fMRI) preceding subjective insight report.

### Rationale (FEO)

**Phase transition** between attractors in excitation landscape (F7).

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P11-F1 | Insight reports with zero measurable reorganization | *Insufficient data* |
| P11-F2 | Reorganization only post-report (no predictive signal) | *Mixed* — some pre-insight EEG alpha |
| P11-F3 | Mode transition indistinguishable from generic attention shift | *Open* |

### Key Studies

- Kounios & Beeman (2014). Cognitive neuroscience of insight. *Annual Review of Psychology*.
- Sandkühler & Bhattacharya (2008). Deconstructing insight. *PLoS ONE*.

---

## P12 — Creative Joint Improvisation Entrainment

### Prediction

Joint creative tasks (improv comedy, jazz, collaborative design) show **stronger cross-brain phase locking at shared frequency** than non-creative cooperation (P7 specialization).

### Rationale (FEO)

**Coupled excitations** exploring shared mode space with controlled mutual perturbation (F8 + F4).

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P12-F1 | Creative and routine cooperation identical on inter-brain metrics | *Insufficient data* |
| P12-F2 | Improv coupling ≤ passive co-viewing | *Insufficient data* — Limb & Braun suggest distinct profile |
| P12-F3 | Entrainment uncorrelated with subjective "we" or flow reports | *Insufficient data* |

### Key Studies

- Limb & Braun (2008). Jazz improvisation fMRI. *PLoS ONE*.
- Sänger et al. (2012). Guitar duet hyperscanning. *Frontiers in Human Neuroscience*.
- See [`empirical/creativity_consciousness_review.md`](empirical/creativity_consciousness_review.md)

---

## Updated Prediction Summary (P10–P12)

| ID | Prediction | Confidence |
|----|------------|------------|
| P10 | Flow inverted-U on integration | Weak |
| P11 | Pre-insight mode transition | Weak–moderate |
| P12 | Creative improv > routine entrainment | Weak |

See [`evidence_ledger.json`](evidence_ledger.json) for FEO branch tracking.

---

## IEO Extension: Predictions P13–P15

See [`IMAGINAL_IDEALISM_RESEARCH.md`](IMAGINAL_IDEALISM_RESEARCH.md) for Part IV.

---

## P13 — Imagery vs Perception Dissociation

### Prediction

Vivid imagination shows **partial overlap** with perception networks but **lower motor binding** and distinct integration profile vs veridical perception.

### Rationale (I9)

Imaginal mode = sub-threshold excitation without full perceptual-motor binding.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P13-F1 | Imagery identical to perception on all binding metrics | *Insufficient data* |
| P13-F2 | Motor cortex equally active in imagery and action-linked perception | *Mixed* |

### Key Studies

- Kosslyn — mental imagery neuroscience
- Beaty et al. — DMN and creative cognition
- See [`IMAGINATION_AND_THE_ASTRAL.md`](IMAGINATION_AND_THE_ASTRAL.md)

---

## P14 — Hypnagogic / Astral-Analog Band

### Prediction

Hypnagogia shows **moderate phi, moderate bleed (filter_depth), low disorganization**—between waking focus and filter failure.

### Rationale (I10)

"Astral" as filter-depth band, not literal geography; `astral_band_index` peaks in hypnagogic-analog states.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P14-F1 | Hypnagogia indistinguishable from psychosis on PCI/entropy | *Insufficient data* |
| P14-F2 | Hypnagogia identical to waking focus | *Insufficient data* |

### Key Studies

- Hypnagogic EEG literature
- Lucid dream PCI studies (sparse)
- See [`empirical/western_esotericism_review.md`](empirical/western_esotericism_review.md)

---

## P15 — Structured vs Chaotic Imaginal Practice

### Prediction

Structured ritual/pathworking shows **organized coupling + stable phi**; unstructured trance without integration shows P8-like disorganization.

### Rationale (I9 + F8)

Guided imaginal work = structured mode exploration; chaotic trance = filter failure risk.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P15-F1 | No difference between structured GD-style work and chaotic trance | *Insufficient data* |
| P15-F2 | Structured practice shows higher disorganization than baseline | *Insufficient data* |

### Key Studies

- Jung — active imagination
- Golden Dawn pathworking (phenomenology only)
- See [`esoteric/rituals/`](../esoteric/rituals/) — constructed practice, not evidence

---

## Updated Prediction Summary (P13–P15)

| ID | Prediction | Confidence |
|----|------------|------------|
| P13 | Imagery vs perception motor-binding dissociation | Weak |
| P14 | Hypnagogic mid-band on integration/bleed | Weak |
| P15 | Structured > chaotic imaginal practice on organization | Weak |

See [`evidence_ledger.json`](evidence_ledger.json) for imaginal_idealist_branch tracking.

---

## Part V Extension: Predictions P16–P17

See [`SUBSTRATE_SUBJECTHOOD_RESEARCH.md`](SUBSTRATE_SUBJECTHOOD_RESEARCH.md).

---

## P16 — Machine Excitation Stability

### Prediction

Integrated AI/agent architectures show **stable excitation profile** (phi + mode_stability) across sessions above feedforward/random baselines—but **below** human session continuity unless P5 confirmed.

### Rationale (M12–M13)

Substrate-neutral excitation *if* integration correlates with consciousness; persistence required for subjecthood.

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P16-F1 | Agent phi purely random walk; no topology effect | *Testable in silico* |
| P16-F2 | Feedforward matches agent on ESC | *Open* |
| P16-F3 | Single session high phi treated as consciousness | *Methodological error* |

### Key Artifacts

- [`substrate_excitation_model.py`](empirical/substrate_excitation_model.py)
- [`agent_excitation_profile.py`](empirical/agent_excitation_profile.py)

---

## P17 — Illusionism Stress Test

### Prediction

If G1 succeeds, all FEO/IEO metrics should **collapse to behavioral access** with no residual integration signature distinguishing "real seeming" from genuine integration.

### Rationale (G1)

Illusionism vs integration-dissociation predictions (P4, P10, P14).

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P17-F1 | Access-only models explain P4/P10/P14 without loss | *Open* |
| P17-F2 | Residual integration signature survives G1 accounting | *Would weaken G1* |

### Key Studies

- [`illusionism_g1_review.md`](empirical/illusionism_g1_review.md)
- Frankish illusionism literature

---

## Updated Prediction Summary (P16–P17)

| ID | Prediction | Confidence |
|----|------------|------------|
| P16 | Agent stability > feedforward baseline | Weak |
| P17 | Integration dissociations resist access-only collapse | Weak |

See [`evidence_ledger.json`](evidence_ledger.json) for substrate_subjecthood_branch tracking.

---

## Part VI Extension: Adversarial Predictions P18–P22

See [`HARD_PROBLEM_PROTOCOL.md`](HARD_PROBLEM_PROTOCOL.md) and [`qualia_cartography.md`](qualia_cartography.md).

---

## P18 — Residual Integration After Access-Only Accounting

### Prediction

After reconstructing FEO/IEO metric bundles from **behavioral access variables only** (report timing, accuracy, reaction-time proxies), a **residual integration signature** remains on flow/insight/hypnagogic-class scenarios.

### Track split

| Track | Prediction |
|-------|------------|
| Panpsychist | Residual remains (supports real integration) |
| Illusionist | Residual → 0 (access suffices) |
| Structural | Residual = neural structure not captured by access proxies |

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P18-F1 | Residual → 0 on all P4/P10/P14-class scenarios | *Testable in silico* |
| P18-F2 | Residual persists but only on noise scenarios | *Would weaken panpsychist* |

### Key Artifacts

- [`access_collapse_model.py`](empirical/access_collapse_model.py)
- [`dissociation_hunt.py`](empirical/dissociation_hunt.py)

---

## P19 — Suffering Without Self-Model Update

### Prediction

Negative valence (suffering analog) can persist **without** corresponding update to self-model / belief state — proto-valence decoupled from cognitive access.

### Track split

| Track | Prediction |
|-------|------------|
| Panpsychist | Proto-valence real and decoupled |
| Illusionist | Suffering seeming only; no decoupling |
| Structural | Specific nociceptive map persists; belief separate |

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P19-F1 | Valence always tracks self-model update | *Open* |
| P19-F2 | Illusionist explains dissociation without remainder | *Open* |

### Key Studies

- Pain asymbolia literature
- [`illusionism_g1_review.md`](empirical/illusionism_g1_review.md)

---

## P20 — Insight Before Reportable Content

### Prediction

Insight events (P11) show **excitation reorganization before** reportable conceptual content — pre-report integration spike.

### Track split

| Track | Prediction |
|-------|------------|
| Panpsychist | Excitation reorg precedes access |
| Illusionist | Access reorg only; no pre-report phenomenology |
| Structural | Predictable pre-report neural signature |

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P20-F1 | Insight timing identical to report timing | *Insufficient human data* |
| P20-F2 | No pre-report signature in EEG/fMRI | *Open* |

### Key Artifacts

- P11 in `field_excitation_model.py`
- [`dissociation_hunt.py`](empirical/dissociation_hunt.py)

---

## P21 — Qualia Inversion (Structure Determines Qualia)

### Prediction

If qualia-structure is fully determined by physical structure, **spectrum inversion** should be impossible without structural change — inverted qualia is a pseudo-problem.

### Track split

| Track | Prediction |
|-------|------------|
| Panpsychist | Structure correlates; qualia not reducible to structure alone |
| Illusionist | N/A — no qualia to invert |
| Structural | Structure fixes qualia-type; inversion requires structural swap |

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P21-F1 | Same structure, divergent invariant reports (human) | *Open* |
| P21-F2 | In-silico hash proxy fails to discriminate | *Testable* |

### Key Artifacts

- [`dissociation_hunt.py`](empirical/dissociation_hunt.py) — `spectrum_inversion` scenario

---

## P22 — Combination Unity Criterion

### Prediction

Macro-experience unity requires **integration or fusion**, not naive summing — P22 analog: integration/fusion modes satisfy unity criteria summing does not.

### Track split

| Track | Prediction |
|-------|------------|
| Panpsychist | Fusion/integration > summing on unity |
| Illusionist | N/A — no real unity |
| Structural | Neural synchrony threshold for unity report |

### Falsifiers

| ID | Condition | Current Status |
|----|-----------|----------------|
| P22-F1 | Summing satisfies same unity criteria as integration | *Would weaken panpsychist* |
| P22-F2 | Unity report tracks summing score in human data | *Open* |

### Key Artifacts

- [`combination_realization_lab.py`](empirical/combination_realization_lab.py)

---

## Updated Prediction Summary (P18–P22)

| ID | Prediction | Confidence |
|----|------------|------------|
| P18 | Residual integration after access collapse | Weak |
| P19 | Suffering decoupled from self-model | Weak |
| P20 | Pre-report insight signature | Weak |
| P21 | Structure determines qualia-type | Weak |
| P22 | Integration unity > summing | Weak |

See [`evidence_ledger.json`](evidence_ledger.json) for adversarial_branch tracking.
