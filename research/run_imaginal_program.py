#!/usr/bin/env python3
"""
Part IV entry script: Imaginal Excitation, Idealism, and FEP context.

Runs P10 fix verification, imaginal excitation model, optional Phase B extension.
Prints comparison table.

Run: python research/run_imaginal_program.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.field_excitation_model import run_field_excitation_experiment
from research.empirical.imaginal_excitation_model import run_imaginal_experiment


def _print_table(title: str, rows: list[tuple[str, str, str, str]]) -> None:
    print(f"\n{title}")
    print("-" * 76)
    print(f"{'Mode':<22} {'Phi/ABI':<14} {'Motor/CFI':<14} {'Disorg':<12}")
    print("-" * 76)
    for mode, col1, col2, disorg in rows:
        print(f"{mode:<22} {col1:<14} {col2:<14} {disorg:<12}")


def main() -> None:
    print("=" * 76)
    print("Part IV: Imaginal Excitation & Idealism Program")
    print("=" * 76)

    feo = run_field_excitation_experiment()
    imaginal = run_imaginal_experiment()

    p10_rows = []
    for scenario in ("boredom", "creative_flow", "overload"):
        data = feo["results_by_scenario"][scenario]
        p10_rows.append((
            scenario,
            f"phi={data['local_phi']:.3f}",
            f"cfi={data['creative_flow_index']:.3f}",
            f"b={data['boredom_index']:.3f}",
        ))
    _print_table("P10 Triplet (boredom / flow / overload)", p10_rows)
    print(f"  P10 analog: {feo['interpretation']['p10_analog']}")

    imag_rows = []
    for scenario, data in imaginal["results_by_scenario"].items():
        imag_rows.append((
            scenario,
            f"abi={data['astral_band_index']:.3f}",
            f"motor={data['motor_binding']:.2f}",
            f"{data['disorganization']:.3f}",
        ))
    _print_table("Imaginal Excitation Model (Part IV)", imag_rows)

    phase_a_ok = imaginal["interpretation"].get("modes_discriminable", False)
    print(f"\nImaginal modes discriminable: {phase_a_ok}")
    print(f"  P13 analog: {imaginal['interpretation']['p13_analog']}")
    print(f"  P14 analog: {imaginal['interpretation']['p14_analog']}")
    print(f"  P15 analog: {imaginal['interpretation']['p15_analog']}")

    physics_output = None
    if phase_a_ok:
        from research.empirical.field_excitation_physics import run_physics_experiment
        physics_output = run_physics_experiment(include_imaginal=True)
        print("\nPhase B Kuramoto re-run: see field_excitation_physics_results.json")

    summary_path = ROOT / "research" / "empirical" / "imaginal_program_summary.json"
    summary = {
        "program": "Imaginal Excitation Ontology Part IV",
        "p10_triplet": feo["interpretation"],
        "imaginal_interpretation": imaginal["interpretation"],
        "phase_b_ran": physics_output is not None,
        "fep_track": "research/esoteric/ — constructed practice, not evidence",
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written: {summary_path}")
    print("\nTrack A (research): imagination as sub-threshold excitation; P13-P15.")
    print("Track B (FEP): research/esoteric/ — novel practice system, explicit firewall.")


if __name__ == "__main__":
    main()
