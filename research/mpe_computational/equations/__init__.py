"""MPE computational equation modules."""

from research.mpe_computational.equations.hierarchy import (
    HierarchyState,
    apply_parametric_depth,
    run_trajectory,
    step_hierarchy,
)
from research.mpe_computational.equations.phenomenology import (
    absorption_score,
    phenomenology_vector,
    summarize_state,
)
from research.mpe_computational.equations.regimes import (
    mind_wandering,
    mpe_absorption,
    mpe_with_content,
    ordinary_wakeful,
    run_regime,
)

__all__ = [
    "HierarchyState",
    "apply_parametric_depth",
    "run_trajectory",
    "step_hierarchy",
    "absorption_score",
    "phenomenology_vector",
    "summarize_state",
    "mind_wandering",
    "mpe_absorption",
    "mpe_with_content",
    "ordinary_wakeful",
    "run_regime",
]
