#!/usr/bin/env python3
"""
Unified Parts I–V consciousness research program runner.

Sequential orchestration of all in-silico experiments and summary output.

Run: python research/run_consciousness_program.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.agent_excitation_profile import run_agent_profile
from research.empirical.combination_model import run_combination_experiment
from research.empirical.field_excitation_model import run_field_excitation_experiment
from research.empirical.field_excitation_physics import run_physics_experiment
from research.empirical.fragmentation_model import run_fragmentation_experiment
from research.empirical.iit_meta_analysis import run_meta_analysis
from research.empirical.imaginal_excitation_model import run_imaginal_experiment
from research.empirical.substrate_excitation_model import run_substrate_experiment


def _flag(label: str, value: bool) -> str:
    return f"{label}: {'PASS' if value else 'FAIL'}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Consciousness Research Program Parts I–V")
    parser.add_argument(
        "--adversarial",
        action="store_true",
        help="After Parts I–V, run Part VI Hard Problem Protocol",
    )
    args = parser.parse_args()

    print("=" * 76)
    print("Consciousness Research Program — Parts I–V Unified Runner")
    print("=" * 76)
    print("DISCLAIMER: All outputs are simulation metrics, NOT consciousness detection.\n")

    print("[Part I] IIT meta-analysis (P1/P5 substrate comparison)")
    iit = run_meta_analysis(n_nodes=8, n_seeds=3)

    print("\n[Part I] Combination model")
    combo = run_combination_experiment(n_components=6)

    print("\n[Part II] Fragmentation model (BFC)")
    frag = run_fragmentation_experiment()

    print("\n[Part III] Field excitation model (FEO)")
    feo = run_field_excitation_experiment()

    phase_a_ok = feo["interpretation"].get("modes_discriminable", False)
    physics = None
    if phase_a_ok:
        print("\n[Part III] Kuramoto physics (Phase B)")
        physics = run_physics_experiment(include_imaginal=True)

    print("\n[Part IV] Imaginal excitation model (IEO)")
    imaginal = run_imaginal_experiment()

    print("\n[Part V] Substrate excitation model (P16)")
    substrate = run_substrate_experiment()

    print("\n[Part V] Agent excitation profile (M13)")
    agent = run_agent_profile()

    feo_interp = feo.get("interpretation", {})
    imag_interp = imaginal.get("interpretation", {})
    sub_interp = substrate.get("interpretation", {})

    comparison = [
        ("Part I P1", iit["interpretation"].get("p1_status", "unknown")),
        ("Part II BFC", frag["interpretation"].get("modes_discriminable", False)),
        ("Part III P10", feo_interp.get("p10_analog", False)),
        ("Part III P11", feo_interp.get("p11_analog", False)),
        ("Part III P12", feo_interp.get("p12_analog", False)),
        ("Part IV P13", imag_interp.get("p13_analog", False)),
        ("Part IV P14", imag_interp.get("p14_analog", False)),
        ("Part IV P15", imag_interp.get("p15_analog", False)),
        ("Part V P16", sub_interp.get("p16_analog", False)),
    ]

    print("\n" + "=" * 76)
    print("Parts I–V Key Analog Flags")
    print("=" * 76)
    for label, val in comparison:
        if isinstance(val, bool):
            print(f"  {_flag(label, val)}")
        else:
            print(f"  {label}: {val}")

    summary = {
        "program": "Consciousness Research Program Parts I-V",
        "disclaimer": "Simulation metrics only; NOT consciousness detection",
        "part_i": {
            "iit_meta_analysis": iit["interpretation"],
            "combination_model": combo.get("interpretation", {}),
        },
        "part_ii": {"fragmentation": frag["interpretation"]},
        "part_iii": {
            "field_excitation": feo_interp,
            "physics_ran": physics is not None,
            "physics_interpretation": physics["interpretation"] if physics else None,
        },
        "part_iv": {"imaginal": imag_interp},
        "part_v": {
            "substrate": sub_interp,
            "agent_profile": {
                "sessions_analyzed": agent.get("sessions_analyzed", 0),
                "excitation_stability_coefficient": agent.get("excitation_stability_coefficient"),
                "disclaimer": agent.get("disclaimer"),
            },
        },
        "comparison_table": {k: v for k, v in comparison},
        "strongest_honest_claim": (
            "We cannot prove who is conscious—but we specify what evidence would "
            "change our minds, compare substrate excitation profiles under simulation "
            "labels, and separate research from FEP practice."
        ),
    }

    out_path = ROOT / "research" / "empirical" / "consciousness_program_summary.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written: {out_path}")

    if args.adversarial:
        print("\n" + "=" * 76)
        print("Continuing with Part VI Hard Problem Protocol...")
        print("=" * 76)
        from research.run_hard_problem_protocol import run_hpp_experiments
        run_hpp_experiments(include_baseline=False)


if __name__ == "__main__":
    main()
