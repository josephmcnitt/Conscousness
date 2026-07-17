"""Part VIII equation modules: density matrix, decoherence, clumping, Born, CSL, no-signaling, awareness matter."""

from research.consciousness_field_quantum.equations.awareness_matter import (
    AwarenessMatterState,
    awareness_density,
    classical_lock,
    factory_mpe,
    factory_pmir,
    factory_psm,
    is_mpe_active,
    is_pmir_active,
    is_psm_active,
    pointer_alignment_strength,
)
from research.consciousness_field_quantum.equations.born_rule import (
    born_probabilities,
    born_total_variation,
    sample_outcomes,
)
from research.consciousness_field_quantum.equations.clumping import (
    ClumpState,
    clump_selection_weights,
    definiteness_from_clump,
    gaussian_localization_profile,
)
from research.consciousness_field_quantum.equations.collapse_csl import (
    csl_localize_step,
    csl_rate,
    run_csl_trajectory,
)
from research.consciousness_field_quantum.equations.decoherence import (
    amplitude_damping_like_dephasing,
    off_diagonal_mean,
    pointer_entropy,
    purity,
)
from research.consciousness_field_quantum.equations.density_matrix import (
    apply_unitary,
    computational_basis_projectors,
    expect,
    ket_to_dm,
    normalize_dm,
    qubit_bloch_dm,
    reduce_qubit_pair,
)
from research.consciousness_field_quantum.equations.metzinger_constraints import (
    constraint_vector,
    mpe_profile_match,
    psm_profile_match,
)
from research.consciousness_field_quantum.equations.no_signaling import (
    chsh_correlator,
    local_marginal,
    signaling_score,
)

__all__ = [
    "AwarenessMatterState",
    "awareness_density",
    "classical_lock",
    "factory_mpe",
    "factory_pmir",
    "factory_psm",
    "is_mpe_active",
    "is_pmir_active",
    "is_psm_active",
    "pointer_alignment_strength",
    "born_probabilities",
    "born_total_variation",
    "sample_outcomes",
    "ClumpState",
    "clump_selection_weights",
    "definiteness_from_clump",
    "gaussian_localization_profile",
    "csl_localize_step",
    "csl_rate",
    "run_csl_trajectory",
    "amplitude_damping_like_dephasing",
    "off_diagonal_mean",
    "pointer_entropy",
    "purity",
    "apply_unitary",
    "computational_basis_projectors",
    "expect",
    "ket_to_dm",
    "normalize_dm",
    "qubit_bloch_dm",
    "reduce_qubit_pair",
    "constraint_vector",
    "mpe_profile_match",
    "psm_profile_match",
    "chsh_correlator",
    "local_marginal",
    "signaling_score",
]
