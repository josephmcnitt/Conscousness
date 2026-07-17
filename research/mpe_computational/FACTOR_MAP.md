# Factor Map (Model → MPE Phenomenology)

Approximate mapping from simulator quantities to MPE-92M-style / book-cluster themes.

**Not** a re-analysis of the MPE-92M dataset. Heuristic readouts for computational phenomenology.

---

## Core phenomenological vector

| Readout key | High when… | Low when… |
|-------------|------------|-----------|
| `epistemicity` | Level-4 posterior mass on “open / knowing” + high \(\gamma_A^{(4)}\) | Level 4 transparent / inactive |
| `nonconceptuality` | Lower-level content entropy / complexity low | Rich L1 categorical content |
| `atemporality` | Policy/agency proxy low; level-4 stable | Strong L2–L3 action / effort dynamics |
| `aperspectivalness` | Self/center proxy low | High ownership / perspectival proxy |
| `non_egoicity` | No egoic self-model proxy; absorption-like | High mental agency + ownership |
| `effortlessness` | Low effort/desire proxy; high \(\gamma_A^{(4)}\) without L2 struggle | High Time/Effort/Desire proxy |
| `awareness_of_awareness` | Level-4 opacification high | Ordinary wakeful transparency |
| `contentfulness` | L1 (and L2) posterior certainty × precision | Absorption attenuation |
| `meta_awareness` | L3 precision / posterior on “aware of attention” | Mind-wandering |
| `mental_agency` | L2–L3 controllable precision gains | Absorption (no policy at L4) |

---

## MPE-92M-style clusters (approximate)

| Factor theme (illustrative) | Primary model hooks |
|-----------------------------|---------------------|
| Time, Effort, Desire | inverse `effortlessness`; L2 control effort |
| Sensory Perception in Body and Space | `contentfulness` / L1 |
| Mental Agency | `mental_agency` |
| Epistemic openness / pure awareness | `epistemicity`, `awareness_of_awareness` |
| Non-egoic / unbounded | `non_egoicity`, `aperspectivalness` |
| Meta-awareness | `meta_awareness` |

Absorption profile target: high epistemic / non-egoic / effortless; low content / agency / perspectival.

With-content MPE target: high epistemic **and** nonzero contentfulness.

---

## Absorption score (composite)

\[
S_{\mathrm{abs}} = \mathrm{mean}(\mathrm{epistemicity}, \mathrm{non\_egoicity}, \mathrm{effortlessness}, \mathrm{awareness\_of\_awareness})
- \mathrm{mean}(\mathrm{contentfulness}, \mathrm{mental\_agency})
\]

Used in transition labs (MP4–MP5).
