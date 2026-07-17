"""
Regime lab (MP1, MP2, MP3, MP6, MP7): compare ordinary / wandering / MPE regimes.

Run: python research/mpe_computational/empirical/regime_lab.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.mpe_computational.equations.phenomenology import summarize_state
from research.mpe_computational.equations.regimes import run_regime

OUTPUT_PATH = Path(__file__).resolve().parent / "regime_lab_results.json"


def run_regime_lab(seed: int = 42) -> dict:
    names = [
        "ordinary_wakeful",
        "mind_wandering",
        "mpe_with_content",
        "mpe_absorption",
    ]
    regimes = {}
    for i, name in enumerate(names):
        traj = run_regime(name, steps=30, seed=seed + i)
        regimes[name] = summarize_state(traj["final"])

    abs_ = regimes["mpe_absorption"]["phenomenology"]
    with_ = regimes["mpe_with_content"]["phenomenology"]
    ord_ = regimes["ordinary_wakeful"]["phenomenology"]
    wand = regimes["mind_wandering"]["phenomenology"]
    abs_f = regimes["mpe_absorption"]["factors"]
    ord_f = regimes["ordinary_wakeful"]["factors"]

    mp1 = (
        abs_["contentfulness"] < 0.35
        and abs_["mental_agency"] < 0.35
        and abs_["epistemicity"] >= 0.5
        and abs_["non_egoicity"] >= 0.5
        and regimes["mpe_absorption"]["absorption_score"] > 0.25
    )
    mp2 = with_["awareness_of_awareness"] >= 0.45 and with_["contentfulness"] >= 0.25
    mp3 = ord_["awareness_of_awareness"] < min(
        abs_["awareness_of_awareness"], with_["awareness_of_awareness"]
    ) - 0.15
    mp6 = wand["contentfulness"] >= 0.4 and wand["meta_awareness"] < with_["meta_awareness"] - 0.1
    mp7 = (
        abs_f["epistemic_openness_pure_awareness"] > ord_f["epistemic_openness_pure_awareness"]
        and abs_f["mental_agency_factor"] < ord_f["mental_agency_factor"]
    )

    output = {
        "experiment": "regime_lab",
        "label": "simulation — not empirical confirmation of MPE phenomenology",
        "seed": seed,
        "regimes": regimes,
        "predictions": {
            "MP1_absorption_profile": bool(mp1),
            "MP2_mpe_with_content": bool(mp2),
            "MP3_ordinary_transparency": bool(mp3),
            "MP6_mind_wandering": bool(mp6),
            "MP7_factor_clusters": bool(mp7),
        },
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Regime lab complete. Results: {OUTPUT_PATH}")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("MPE Regime Lab")
    print("=" * 60)
    run_regime_lab()
