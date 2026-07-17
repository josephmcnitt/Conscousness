"""
Transition lab (MP4, MP5): attenuation into absorption; restore exit.

Run: python research/mpe_computational/empirical/transition_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.mpe_computational.equations.hierarchy import (
    HierarchyState,
    default_level,
    run_trajectory,
)
from research.mpe_computational.equations.phenomenology import (
    absorption_score,
    phenomenology_vector,
)
from research.mpe_computational.equations.regimes import (
    attenuation_schedule,
    restore_schedule,
)

OUTPUT_PATH = Path(__file__).resolve().parent / "transition_lab_results.json"


def _start_pre_absorption() -> HierarchyState:
    """Contentful, low L4 opacification — room to rise into absorption."""
    return HierarchyState(
        levels=[
            default_level(gamma=2.0, obs_bias=0.7),
            default_level(gamma=1.8, obs_bias=0.65),
            default_level(gamma=1.4, obs_bias=0.6),
            default_level(gamma=2.4, obs_bias=0.85),
        ],
        level4_opacification=0.2,
        policy_depth=0.75,
        ownership=0.6,
        perspectivalness=0.65,
    )


def run_transition_lab(seed: int = 42, steps: int = 40) -> dict:
    rng = np.random.default_rng(seed)
    start = _start_pre_absorption()

    att = attenuation_schedule(steps=steps, g_high=2.0, g_low=0.08, g4=2.6)
    obs_schedule = []
    for t in range(steps):
        obs_schedule.append(
            [
                float(np.clip(0.7 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.65 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.6 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.85 + rng.normal(0, 0.01), 0.5, 0.99)),
            ]
        )
    traj_in = run_trajectory(
        start, steps=steps, obs_schedule=obs_schedule, gamma_schedule=att
    )
    scores_in = []
    for i, st in enumerate(traj_in["states"]):
        frac = i / max(steps - 1, 1)
        # Opacify L4 and drop agency as attenuation proceeds
        st.level4_opacification = float(0.2 + 0.75 * frac)
        st.policy_depth = float(0.75 * (1.0 - frac))
        st.ownership = float(0.6 * (1.0 - frac) + 0.05 * frac)
        st.perspectivalness = float(0.65 * (1.0 - frac) + 0.05 * frac)
        scores_in.append(absorption_score(phenomenology_vector(st)))

    diffs = np.diff(scores_in)
    mp4 = bool(np.all(diffs >= -0.04) and scores_in[-1] > scores_in[0] + 0.15)

    # MP5: restore from absorption-like end
    end_abs = traj_in["states"][-1]
    end_abs.level4_opacification = 0.95
    end_abs.policy_depth = 0.0
    end_abs.ownership = 0.05
    end_abs.perspectivalness = 0.05
    peak_score = float(scores_in[-1])
    g4_before = float(end_abs.levels[3].gamma_A)

    rest = restore_schedule(steps=steps, g_low=0.08, g_high=2.0, g4=2.6)
    obs2 = []
    for t in range(steps):
        obs2.append(
            [
                float(np.clip(0.75 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.7 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.65 + rng.normal(0, 0.02), 0.1, 0.9)),
                float(np.clip(0.9 + rng.normal(0, 0.01), 0.5, 0.99)),
            ]
        )
    traj_out = run_trajectory(
        end_abs, steps=steps, obs_schedule=obs2, gamma_schedule=rest
    )
    scores_out = []
    contents_out = []
    for i, st in enumerate(traj_out["states"]):
        frac = i / max(steps - 1, 1)
        st.level4_opacification = float(0.95 - 0.2 * frac)
        st.policy_depth = float(0.7 * frac)
        st.ownership = float(0.05 + 0.5 * frac)
        st.perspectivalness = float(0.05 + 0.5 * frac)
        vec = phenomenology_vector(st)
        scores_out.append(absorption_score(vec))
        contents_out.append(vec["contentfulness"])

    stf = traj_out["states"][-1]
    stf.level4_opacification = 0.75
    stf.policy_depth = 0.7
    stf.ownership = 0.55
    stf.perspectivalness = 0.55
    final_vec = phenomenology_vector(stf)
    g4_after = float(stf.levels[3].gamma_A)

    mp5 = (
        final_vec["contentfulness"] > contents_out[0] + 0.15
        and g4_after >= 0.7 * max(g4_before, 1.0)
        and scores_out[-1] < peak_score - 0.1
    )

    output = {
        "experiment": "transition_lab",
        "label": "simulation — not empirical confirmation of MPE phenomenology",
        "seed": seed,
        "attenuation": {
            "absorption_scores": scores_in,
            "start": scores_in[0],
            "end": scores_in[-1],
        },
        "restore": {
            "absorption_scores": scores_out,
            "contentfulness": contents_out,
            "gamma_L4_before": g4_before,
            "gamma_L4_after": g4_after,
            "final_phenomenology": final_vec,
            "peak_absorption_before_restore": peak_score,
        },
        "predictions": {
            "MP4_attenuation_raises_absorption": bool(mp4),
            "MP5_restore_exits_without_killing_L4": bool(mp5),
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Transition lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("MPE Transition Lab")
    print("=" * 60)
    run_transition_lab()
