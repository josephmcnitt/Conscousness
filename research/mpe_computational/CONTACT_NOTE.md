# Contact Note — MPE Computational Phenomenology Simulator

**To:** MPE Project (`mpe@uni-mainz.de`)  
**Re:** Runnable NumPy implementation of Subproject 3’s published 4-level architecture  
**Status:** Discussion starter — **not** a Computational Phenomenology Prize submission

---

## What this is

A small, substrate-independent simulator that implements the **parametric-depth likelihood-precision hierarchy** described on the MPE Project Subproject 3 page (Metzinger + Sandved-Smith):

- Level 1: sensory / interoceptive inference  
- Level 2: attention as precision over level 1  
- Level 3: meta-awareness as precision over level 2  
- Level 4: epistemic openness / awareness-of-awareness  

It includes explicit regimes for **MPE with content** and **MPE absorption** (lower-level \(\gamma_A\) attenuated; level 4 maintained; no policy depth at level 4), named phenomenological readouts, approximate factor-cluster proxies, and falsifiable in-silico predictions (MP1–MP8).

Entry point:

```bash
python research/mpe_computational/run_mpe_program.py
```

Docs: `README.md`, `MPE_MODEL.md`, `FACTOR_MAP.md`, `predictions.md`.

---

## What this is not

- Not an official MPE Project model  
- Not a full active-inference / `pymdp` agent  
- Not empirical validation of meditation reports or neural correlates  
- Not a physical ontology of consciousness (no “consciousness field” claim in this package)

---

## One technical question

In absorption, Subproject 3 text attenuates lower-level likelihood precisions so that reportable phenomenology is dominated by level 4.

**Should absorption hard-zero lower-level posteriors, or is it enough (as in our v1) to collapse their contribution to reportable content via low \(\gamma_A\) while leaving numerically defined posteriors?**

We chose the second option for numerical continuity of transition schedules (MP4–MP5) and would gladly revise if the preferred semantics is hard-zeroing.

---

## Invitation

Corrections to the mapping between hierarchy quantities and MPE phenomenological dimensions are welcome. Happy to align naming with the MPE-92M factor solution more tightly if useful.

Thank you for publishing the architecture so clearly — this package exists to make that proposal executable and criticizable.
