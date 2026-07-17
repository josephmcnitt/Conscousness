# Neurophenomenology Protocol (Track C Lite)

Part VI — disciplined first-person data collection template for structural physicalism.

**Firewall:** This protocol is **NOT** FEP Track B ([`../esoteric/FIELD_EXCITATION_PRACTICE.md`](../esoteric/FIELD_EXCITATION_PRACTICE.md)). No rituals, no cosmology, no occult claims.

**Scope:** Human data collection is **out-of-repo** — this document prepares the method for future use.

---

## Purpose

Structural physicalism (Bridge tier) requires **paired first-person + third-person** data under pre-registration. This protocol adapts micro-phenomenological interview methods (Varela-style, simplified) for three qualia invariants:

| Session focus | Invariant | Research prediction |
|---------------|-----------|---------------------|
| Flow | Q4 | P10 |
| Insight | Q5 | P20 |
| Hypnagogic | Q8 | P14 / P18 |

---

## Pre-Registration Checklist

Before any session:

1. Hypothesis registered in [`../predictions.md`](../predictions.md) (P18–P20)
2. Session type selected (flow / insight / hypnagogic)
3. Third-person measure plan noted (EEG, PCI, or in-silico proxy only for repo work)
4. Label applied: **first-person data not proof**

---

## Session Structure (45 min)

| Phase | Duration | Activity |
|-------|----------|----------|
| Baseline | 5 min | Eyes open, neutral attention; note bodily state |
| Elicitation | 15 min | Task matched to session type (below) |
| Micro-phenomenological interview | 15 min | Guided report (template below) |
| Closure | 5 min | Return to baseline; debrief |
| Log | 5 min | Complete session record |

---

## Elicitation Tasks

### Flow session (Q4 / P10)

- Perform a familiar skill at varying difficulty until flow or boredom is noticed
- Note moment when effort vanishes or increases

### Insight session (Q5 / P20)

- Work on a problem with no immediate solution (word puzzle, logic, creative prompt)
- Note any "pop" or reorganization **before** you can articulate the answer

### Hypnagogic session (Q8 / P14)

- Rest supine in dim light; allow hypnagogic imagery without sleeping fully
- Note imagery vividness, body boundary, and filter/boundary sense

---

## Micro-Phenomenological Interview Template

Interviewer (or self-guided written form) asks:

1. **Where** did you notice the experience — body, mind, visual field, elsewhere?
2. **When** exactly did it start and shift? (timeline to nearest few seconds)
3. **Quality** — texture, intensity, valence (1–5), unity (1–5)
4. **Before report** — was there content before you could name it? (insight sessions)
5. **Transparency** — did experience feel direct or mediated?
6. **Contrast** — how did this differ from ordinary waking focus?

Record verbatim where possible. Avoid leading questions.

---

## Session Log Schema

```json
{
  "protocol": "neurophenomenology_v1",
  "session_type": "flow | insight | hypnagogic",
  "timestamp": "ISO-8601",
  "label": "first_person_data_not_proof",
  "self_report": {
    "valence": 0,
    "unity": 0,
    "transparency": 0,
    "boundary_clarity": 0,
    "pre_report_content": true,
    "notes": ""
  },
  "third_person_proxy": {
    "phi_proxy": null,
    "creative_flow_index": null,
    "astral_band_index": null,
    "note": "Optional in-silico proxy from consciousness_metrics — simulation only"
  }
}
```

Optional repo hook: append to `research/empirical/neurophen_sessions.jsonl` (human-initiated only).

---

## Pairing Rules

| Rule | Rationale |
|------|-----------|
| First-person and third-person logged same session | Neurophenomenology core |
| Never cite FEP practice as third-person measure | Track B firewall |
| Never update adversarial ledger from n=1 session | M14 report humility |
| Pre-register which invariant is tested | HPP tournament rules |

---

## Stop Conditions

Pause protocol and seek support if:

- Dissociation or depersonalization persists > 30 min post-session
- Distress without recovery after closure phase
- Sleep disruption for 3+ nights after hypnagogic sessions

Not a clinical protocol — for research scaffolding only.

---

## Cross-Links

- Qualia targets: [`../qualia_cartography.md`](../qualia_cartography.md)
- Tournament rules: [`../hard_problem_protocol.md`](../hard_problem_protocol.md)
- Adversarial tests: [`dissociation_hunt.py`](dissociation_hunt.py), [`access_collapse_model.py`](access_collapse_model.py)
