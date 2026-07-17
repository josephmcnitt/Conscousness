#!/usr/bin/env python3
"""
Part III entry script: Field Excitation Ontology research program.

Runs fragmentation model (fixed), field excitation model, and Phase B physics
if Phase A discriminates modes. Prints comparison table.

Run: python research/run_field_excitation_program.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.empirical.field_excitation_model import run_field_excitation_experiment
from research.empirical.fragmentation_model import run_fragmentation_experiment


def _print_table(title: str, rows: list[tuple[str, str, str, str]]) -> None:
    print(f"\n{title}")
    print("-" * 72)
    print(f"{'Mode':<22} {'Phi/CFI':<12} {'Coupling':<12} {'Disorg':<12}")
    print("-" * 72)
    for mode, phi_cfi, coupling, disorg in rows:
        print(f"{mode:<22} {phi_cfi:<12} {coupling:<12} {disorg:<12}")


def main() -> None:
    print("=" * 72)
    print("Part III: Field Excitation Ontology Program")
    print("=" * 72)

    frag = run_fragmentation_experiment()
    feo = run_field_excitation_experiment()

    frag_rows = []
    for mode, data in frag["results_by_mode"].items():
        frag_rows.append((
            mode,
            f"{data['collective_phi']:.4f}",
            f"{data['cross_subject_coupling']:.4f}",
            f"{data['disorganization']:.4f}",
        ))
    _print_table("BFC Fragmentation Model (multi-node phi fix)", frag_rows)

    feo_rows = []
    for scenario, data in feo["results_by_scenario"].items():
        feo_rows.append((
            scenario,
            f"phi={data['local_phi']:.3f} cfi={data['creative_flow_index']:.3f}",
            f"{data['cross_coupling']:.4f}",
            f"{data['disorganization']:.4f}",
        ))
    _print_table("Field Excitation Model (wavepacket scenarios)", feo_rows)

    phase_a_ok = feo["interpretation"].get("modes_discriminable", False)
    print(f"\nPhase A modes discriminable: {phase_a_ok}")

    physics_output = None
    if phase_a_ok:
        from research.empirical.field_excitation_physics import run_physics_experiment
        physics_output = run_physics_experiment()
        phys_rows = []
        for scenario, data in physics_output["results_by_scenario"].items():
            phys_rows.append((
                scenario,
                f"r={data['final_order_parameter']:.3f}",
                f"cfi={data['mean_creative_flow_index']:.3f}",
                f"disp={data['frequency_dispersion']:.3f}",
            ))
        _print_table("Phase B: Kuramoto Physics", phys_rows)
    else:
        print("\nPhase B skipped: Phase A did not discriminate modes sufficiently.")

    summary_path = ROOT / "research" / "empirical" / "field_excitation_program_summary.json"
    summary = {
        "program": "Field Excitation Ontology Part III",
        "fragmentation_interpretation": frag["interpretation"],
        "field_excitation_interpretation": feo["interpretation"],
        "phase_b_ran": phase_a_ok,
        "physics_interpretation": physics_output["interpretation"] if physics_output else None,
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written: {summary_path}")
    print("\nStrongest honest claim:")
    print(
        "  Subjectivity modeled as localized excitation; creativity as structured mode "
        "exploration — testable via P7-P12, not provable as fundamental physics yet."
    )


if __name__ == "__main__":
    main()
