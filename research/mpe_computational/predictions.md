# MPE Computational Predictions (MP1–MP8)

In-silico predictions for the 4-level parametric-depth simulator.

**Status key:** Pending | Supported (sim) | Failed (sim)

All support is **simulation only** — not empirical MPE confirmation.

---

## MP1 — Absorption Profile

Absorption regime: low content / agency / perspectival; high epistemicity + non-egoic.

- **Lab:** `regime_lab.py`
- **Pass:** `contentfulness` and `mental_agency` low; `epistemicity` and `non_egoicity` high; `absorption_score` > 0.25
- **Fail:** absorption looks like ordinary wakeful

## MP2 — MPE With Content

With-content MPE: high level-4 openness **and** nonzero lower-level content.

- **Lab:** `regime_lab.py`
- **Pass:** `awareness_of_awareness` high **and** `contentfulness` ≥ 0.25
- **Fail:** either pure absorption (no content) or ordinary (no L4 opacification)

## MP3 — Ordinary Wakeful Transparency

Ordinary wakeful: level-4 opacification low → low awareness-of-awareness.

- **Lab:** `regime_lab.py`
- **Pass:** `awareness_of_awareness` ≪ absorption / with-content regimes
- **Fail:** ordinary scores as MPE absorption

## MP4 — Attenuation → Absorption

Increasing L1–L3 attenuation schedule → monotonic rise in absorption score.

- **Lab:** `transition_lab.py`
- **Pass:** `absorption_score` nondecreasing over schedule (within noise tolerance)
- **Fail:** attenuation lowers absorption score

## MP5 — Restore Exits Absorption

Restoring L1–L3 \(\gamma_A\) exits absorption profile without destroying L4 capacity (\(\gamma_A^{(4)}\) stays high).

- **Lab:** `transition_lab.py`
- **Pass:** final `contentfulness` rises; final `gamma_L4` remains high; absorption score falls from peak
- **Fail:** restoring lower levels collapses L4

## MP6 — Mind-Wandering

Mind-wandering: high L1 content, low L3 meta-awareness.

- **Lab:** `regime_lab.py`
- **Pass:** `contentfulness` high and `meta_awareness` low relative to with-content MPE
- **Fail:** mind-wandering indistinguishable from meta-aware MPE-with-content

## MP7 — Factor Map Clusters

Absorption correlates with epistemic-openness / pure-awareness cluster; anti-correlates with Mental Agency.

- **Lab:** `regime_lab.py`
- **Pass:** absorption `epistemic_openness_pure_awareness` > ordinary; absorption `mental_agency_factor` < ordinary
- **Fail:** factor proxies invert

## MP8 — Non-Claim Check

Package docs/runtime summary assert no substrate / field ontology claim.

- **Lab:** `run_mpe_program.py` / summary flag
- **Pass:** `ontology_claims_asserted` is false; disclaimer present
- **Fail:** summary asserts physical consciousness field

---

## Summary Table

| ID | Focus | Lab |
|----|-------|-----|
| MP1 | Absorption profile | regime |
| MP2 | With-content MPE | regime |
| MP3 | Ordinary transparency | regime |
| MP4 | Attenuation schedule | transition |
| MP5 | Restore exit | transition |
| MP6 | Mind-wandering | regime |
| MP7 | Factor clusters | regime |
| MP8 | Non-claim firewall | runner |
