"""Awareness-matter sector: Metzinger-layered order parameters for Part VIII."""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np

from research.consciousness_field_quantum.equations.clumping import ClumpState

# Fixed rho_A coefficients (METZINGER_BRIDGE.md / CLUMPING_ONTOLOGY.md)
ALPHA_SELF = 0.5
ALPHA_PERSPECTIVAL = 0.3


@dataclass
class AwarenessMatterState:
    """
    Typed auxiliary sector A: geometric C1 fields + MPE / PSM / PMIR layers.

    Not a Hilbert factor H_A — order parameters only (v1).
    """

    # Geometric / field (C1)
    amplitude: float = 1.0
    coherence_length: float = 1.0
    mode_stability: float = 0.8
    center: float = 0.0

    # Layer 0 — MPE
    wakefulness: float = 0.8
    content_complexity: float = 0.2
    epistemicity: float = 0.7
    opacity_mpe: float = 0.3

    # Layer 1 — PSM
    selfhood: float = 0.0
    transparency: float = 0.0
    ownership: float = 0.0
    diachronic: float = 0.0

    # Layer 2 — PMIR
    perspectivalness: float = 0.0
    intentional_arrow: float = 0.0

    def clamp(self) -> "AwarenessMatterState":
        def c01(x: float) -> float:
            return float(np.clip(x, 0.0, 1.0))

        return AwarenessMatterState(
            amplitude=float(np.clip(self.amplitude, 0.0, 10.0)),
            coherence_length=float(max(self.coherence_length, 1e-6)),
            mode_stability=c01(self.mode_stability),
            center=float(self.center),
            wakefulness=c01(self.wakefulness),
            content_complexity=c01(self.content_complexity),
            epistemicity=c01(self.epistemicity),
            opacity_mpe=c01(self.opacity_mpe),
            selfhood=c01(self.selfhood),
            transparency=c01(self.transparency),
            ownership=c01(self.ownership),
            diachronic=c01(self.diachronic),
            perspectivalness=c01(self.perspectivalness),
            intentional_arrow=c01(self.intentional_arrow),
        )

    def to_clump(self) -> ClumpState:
        """Project geometric fields to legacy ClumpState."""
        a = self.clamp()
        return ClumpState(
            amplitude=a.amplitude,
            coherence_length=a.coherence_length,
            mode_stability=a.mode_stability,
            center=a.center,
        )


def awareness_density(state: AwarenessMatterState) -> float:
    """
    rho_A = A * w * (1 + alpha1 * selfhood + alpha2 * perspectivalness) / sigma
    """
    a = state.clamp()
    boost = 1.0 + ALPHA_SELF * a.selfhood + ALPHA_PERSPECTIVAL * a.perspectivalness
    return float(a.amplitude * a.wakefulness * boost / a.coherence_length)


def is_mpe_active(state: AwarenessMatterState) -> bool:
    a = state.clamp()
    return a.wakefulness >= 0.7 and a.content_complexity <= 0.3 and a.selfhood <= 0.2


def is_psm_active(state: AwarenessMatterState) -> bool:
    a = state.clamp()
    return a.selfhood >= 0.6 and a.transparency >= 0.5


def is_pmir_active(state: AwarenessMatterState) -> bool:
    a = state.clamp()
    return a.perspectivalness >= 0.6 and a.intentional_arrow >= 0.5


def factory_mpe(
    amplitude: float = 1.0,
    coherence_length: float = 1.0,
    mode_stability: float = 0.85,
) -> AwarenessMatterState:
    """Minimal phenomenal experience: wakeful, low complexity, no self."""
    return AwarenessMatterState(
        amplitude=amplitude,
        coherence_length=coherence_length,
        mode_stability=mode_stability,
        wakefulness=0.95,
        content_complexity=0.1,
        epistemicity=0.85,
        opacity_mpe=0.6,
        selfhood=0.0,
        transparency=0.0,
        ownership=0.0,
        diachronic=0.0,
        perspectivalness=0.0,
        intentional_arrow=0.0,
    ).clamp()


def factory_psm(
    amplitude: float = 1.0,
    coherence_length: float = 1.0,
    mode_stability: float = 0.9,
) -> AwarenessMatterState:
    """Phenomenal self-model on; perspectivalness mild until PMIR factory."""
    return AwarenessMatterState(
        amplitude=amplitude,
        coherence_length=coherence_length,
        mode_stability=mode_stability,
        wakefulness=0.9,
        content_complexity=0.55,
        epistemicity=0.75,
        opacity_mpe=0.25,
        selfhood=0.85,
        transparency=0.9,
        ownership=0.8,
        diachronic=0.75,
        perspectivalness=0.4,
        intentional_arrow=0.35,
    ).clamp()


def factory_pmir(
    amplitude: float = 1.0,
    coherence_length: float = 1.0,
    mode_stability: float = 0.9,
) -> AwarenessMatterState:
    """Full first-person: PSM + strong PMIR (centered intentionality)."""
    return AwarenessMatterState(
        amplitude=amplitude,
        coherence_length=coherence_length,
        mode_stability=mode_stability,
        wakefulness=0.9,
        content_complexity=0.6,
        epistemicity=0.8,
        opacity_mpe=0.2,
        selfhood=0.9,
        transparency=0.92,
        ownership=0.88,
        diachronic=0.8,
        perspectivalness=0.9,
        intentional_arrow=0.85,
    ).clamp()


def factory_high_complexity_no_self(
    amplitude: float = 1.0,
    coherence_length: float = 1.0,
) -> AwarenessMatterState:
    """Rich content without selfhood — must not count as PSM (M8)."""
    return AwarenessMatterState(
        amplitude=amplitude,
        coherence_length=coherence_length,
        mode_stability=0.7,
        wakefulness=0.75,
        content_complexity=0.9,
        epistemicity=0.5,
        opacity_mpe=0.2,
        selfhood=0.05,
        transparency=0.1,
        ownership=0.05,
        diachronic=0.05,
        perspectivalness=0.05,
        intentional_arrow=0.05,
    ).clamp()


def promote_mpe_to_psm(mpe: AwarenessMatterState) -> AwarenessMatterState:
    """Raise selfhood/transparency from an MPE seed (M2 transition)."""
    base = mpe.clamp()
    return replace(
        base,
        selfhood=0.85,
        transparency=0.9,
        ownership=0.8,
        diachronic=0.75,
        content_complexity=max(base.content_complexity, 0.45),
        perspectivalness=max(base.perspectivalness, 0.35),
        intentional_arrow=max(base.intentional_arrow, 0.3),
    ).clamp()


def promote_psm_to_pmir(psm: AwarenessMatterState) -> AwarenessMatterState:
    """Raise perspectivalness / intentional arrow (PMIR on)."""
    base = psm.clamp()
    return replace(
        base,
        perspectivalness=0.9,
        intentional_arrow=0.85,
        selfhood=max(base.selfhood, 0.7),
        transparency=max(base.transparency, 0.7),
    ).clamp()


def clump_from_awareness(state: AwarenessMatterState) -> ClumpState:
    return state.to_clump()


def awareness_from_clump(
    clump: ClumpState,
    *,
    wakefulness: float = 1.0,
    selfhood: float = 0.0,
    perspectivalness: float = 0.0,
) -> AwarenessMatterState:
    """Lift legacy ClumpState into awareness sector (MPE-like defaults)."""
    c = clump.clamp()
    return AwarenessMatterState(
        amplitude=c.amplitude,
        coherence_length=c.coherence_length,
        mode_stability=c.mode_stability,
        center=c.center,
        wakefulness=wakefulness,
        content_complexity=0.15 if selfhood < 0.3 else 0.5,
        epistemicity=0.7,
        opacity_mpe=0.4,
        selfhood=selfhood,
        transparency=0.85 if selfhood >= 0.6 else 0.0,
        ownership=0.8 if selfhood >= 0.6 else 0.0,
        diachronic=0.7 if selfhood >= 0.6 else 0.0,
        perspectivalness=perspectivalness,
        intentional_arrow=0.8 if perspectivalness >= 0.6 else 0.0,
    ).clamp()


def pointer_alignment_strength(state: AwarenessMatterState) -> float:
    """
    How strongly PMIR locks the observer to the interaction pointer frame.
    Used by preferred-basis diagnostics (M3).
    """
    a = state.clamp()
    return float(np.clip(a.perspectivalness * a.intentional_arrow * a.mode_stability, 0.0, 1.0))


def classical_lock(
    state: AwarenessMatterState,
    classicality: float,
) -> float:
    """
    Classical appearance proxy: decoherence classicality × transparency × stability.
    M7: high tau + high classicality → high lock.
    """
    a = state.clamp()
    return float(
        np.clip(float(classicality) * a.transparency * a.mode_stability, 0.0, 1.0)
    )


def selection_weights_awareness(
    born_probs: np.ndarray,
    state: AwarenessMatterState,
    blend: float | None = None,
) -> np.ndarray:
    """
    Track U experiential selection: Born-primary; mild reweight by localization
    and perspectival lock. Physics Born scoring still uses |c|^2.
    """
    from research.consciousness_field_quantum.equations.clumping import (
        gaussian_localization_profile,
    )

    a = state.clamp()
    born = np.asarray(born_probs, dtype=float)
    born = born / born.sum()
    profile = gaussian_localization_profile(len(born), a.to_clump())
    if blend is None:
        # Stronger perspectivalness → slightly more localization overlay
        blend = float(np.clip(0.1 + 0.15 * a.perspectivalness, 0.0, 0.35))
    else:
        blend = float(np.clip(blend, 0.0, 1.0))
    mixed = (1.0 - blend) * born + blend * profile
    # Soft ownership bias does not break Born TV when blend is small
    return mixed / mixed.sum()


def definiteness_from_awareness(
    state: AwarenessMatterState,
    classicality: float,
) -> float:
    """Definiteness felt under Track U: density-aware + classical lock."""
    a = state.clamp()
    dens = np.tanh(awareness_density(a))
    lock = classical_lock(a, classicality)
    return float(np.clip(dens * a.mode_stability * max(lock, classicality * 0.5), 0.0, 1.0))
