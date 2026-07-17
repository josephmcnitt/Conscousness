# MPE Model Formalism

Architecture-faithful simplification of MPE Project Subproject 3 (Metzinger + Sandved-Smith parametric-depth proposal).

**Label:** Toy NumPy dynamics — not full active-inference / `pymdp`.

---

## Levels

| Level | Computational role | Phenomenological gloss |
|-------|--------------------|------------------------|
| **1** | Sensory / interoceptive state inference | Seeing, hearing, bodily sensation |
| **2** | Attention = precision over level-1 likelihood | “Where is attention allocated?” |
| **3** | Meta-awareness = precision over level-2 | “How aware am I of my attentional state?” |
| **4** | Epistemic openness = precision over the precision hierarchy | Awareness of awareness / pure awareness capacity |

Higher level **parameterizes** likelihood precision \(\gamma_A\) of the level below (parametric depth).

---

## State per level \(\ell\)

- Belief / posterior mass \(q^{(\ell)}_t\) over a small discrete latent set (toy: 2–3 states)
- Likelihood precision \(\gamma_A^{(\ell)} \ge 0\)
- Observation / drive \(o^{(\ell)}_t\) (synthetic for simulation)

### Precision-weighted update (toy)

At each level, evidence is precision-scaled against a prior \(D^{(\ell)}\):

\[
\tilde{q}^{(\ell)} \propto \exp\bigl(\log D^{(\ell)} + \gamma_A^{(\ell)}\,\log \mathcal{L}(o^{(\ell)} \mid \cdot)\bigr)
\]

then normalize to \(q^{(\ell)}\).

**Parametric depth link:** level \(\ell+1\)’s posterior summary sets a target for \(\gamma_A^{(\ell)}\) (higher “awareness of X” → higher precision gain on X), with optional smoothing.

---

## Regimes

### Ordinary wakeful

- Levels 1–3 high and contentful  
- Level 4 **transparent** (low opacification): awareness used but not attended as such → low “awareness of awareness” readout  

### Mind-wandering

- Level 1 high content / volatile  
- Level 3 meta-awareness **low** (unaware of attentional drift)  

### MPE with content

- All levels active  
- Level 4 high (epistemic openness opacified) **and** levels 1–2 nonzero content  

### MPE absorption

- \(\gamma_A^{(1)}, \gamma_A^{(2)}, \gamma_A^{(3)} \to\) low (sensory / attentional attenuation)  
- \(\gamma_A^{(4)}\) remains high  
- No policy depth at level 4 → non-agentive, atemporal, aperspectival scores rise  
- Reportable phenomenology dominated by level-4 epistemic openness  

---

## Absorption vs “zeroing posteriors”

**Implementation choice (v1):** attenuation collapses **contribution of L1–L3 to reportable content** via low precision (posteriors may remain numerically defined but weakly driven). Contact note asks whether MPE team prefers hard-zeroing of lower posteriors instead.

---

## Implementation

- `equations/hierarchy.py` — updates + parametric depth  
- `equations/regimes.py` — regime factories  
- `equations/phenomenology.py` — readouts  

See [`FACTOR_MAP.md`](FACTOR_MAP.md) and [`predictions.md`](predictions.md).
