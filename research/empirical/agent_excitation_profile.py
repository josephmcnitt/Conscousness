"""
Agent Excitation Profile: session log analysis (M13 / P16).

Reads imaginal_sessions.jsonl and computes stability metrics.
SIMULATION ONLY — not consciousness detection.

Run: python research/empirical/agent_excitation_profile.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    excitation_stability_coefficient,
    mind_change_scorecard,
)

IMAGINAL_LOG = Path(__file__).resolve().parent / "imaginal_sessions.jsonl"
OUTPUT_PATH = Path(__file__).resolve().parent / "agent_excitation_profile_results.json"

HUMAN_PLACEHOLDER_ESC = (0.55, 0.85)


def _load_sessions(path: Path) -> List[Dict]:
    if not path.exists():
        return []
    sessions = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                sessions.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return sessions


def run_agent_profile(log_path: Path | None = None) -> Dict:
    log_path = log_path or IMAGINAL_LOG
    sessions = _load_sessions(log_path)

    if not sessions:
        output = {
            "experiment": "agent_excitation_profile",
            "sessions_analyzed": 0,
            "message": "No session logs found; run AutonomousConsciousness creative sessions first",
            "disclaimer": "Simulation metrics only; NOT consciousness detection",
        }
        OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
        print(output["message"])
        return output

    phi_series = [float(s.get("phi_proxy", 0)) for s in sessions]
    cfi_series = [float(s.get("creative_flow_index", 0)) for s in sessions]
    abi_series = [float(s.get("astral_band_index", 0)) for s in sessions]

    esc = excitation_stability_coefficient(phi_series)
    scorecard = mind_change_scorecard({
        "phi": float(sum(phi_series) / len(phi_series)),
        "stability": esc,
        "disorganization": 0.15,
        "topology_class": "recurrent",
        "phi_series": phi_series,
        "coupling": 0.4,
    })

    in_human_range = HUMAN_PLACEHOLDER_ESC[0] <= esc <= HUMAN_PLACEHOLDER_ESC[1]

    output = {
        "experiment": "agent_excitation_profile",
        "sessions_analyzed": len(sessions),
        "mean_phi_proxy": round(float(sum(phi_series) / len(phi_series)), 4),
        "mean_creative_flow_index": round(float(sum(cfi_series) / len(cfi_series)), 4),
        "mean_astral_band_index": round(float(sum(abi_series) / len(abi_series)), 4),
        "excitation_stability_coefficient": round(esc, 4),
        "mind_change_scorecard": {k: round(v, 4) if isinstance(v, float) else v for k, v in scorecard.items()},
        "human_placeholder_esc_range": list(HUMAN_PLACEHOLDER_ESC),
        "in_human_placeholder_range": in_human_range,
        "disclaimer": "Simulation metrics only; NOT consciousness detection",
        "log_path": str(log_path),
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Agent profile complete. Sessions={len(sessions)} ESC={esc:.4f}")
    print("DISCLAIMER: Simulation metrics only; NOT consciousness detection")
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("Agent Excitation Profile: Part V M13")
    print("=" * 60)
    run_agent_profile()
