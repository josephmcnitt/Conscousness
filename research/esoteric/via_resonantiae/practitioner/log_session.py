#!/usr/bin/env python3
"""
Log Via Resonantiae practice session — Pathos only, NOT research evidence.

Run: python research/esoteric/via_resonantiae/practitioner/log_session.py
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

SESSIONS_PATH = Path(__file__).resolve().parent / "sessions.jsonl"
LABEL = "practitioner_pathos_not_research_evidence"


def log_session(
    grade: str,
    ritual_id: str,
    epistemic_mode: str,
    boundary: float,
    coherence: float,
    coupling: float,
    disorganization: float,
    notes: str = "",
    veil: int | None = None,
) -> dict:
    entry = {
        "timestamp": time.time(),
        "grade": grade,
        "ritual_id": ritual_id,
        "epistemic_mode": epistemic_mode,
        "label": LABEL,
        "scores": {
            "boundary_clarity": boundary,
            "mode_coherence": coherence,
            "coupling_sense": coupling,
            "disorganization": disorganization,
        },
        "veil_reached": veil,
        "notes": notes,
        "firewall": "NOT research evidence; does not update evidence_ledger",
    }
    SESSIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SESSIONS_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def main() -> None:
    parser = argparse.ArgumentParser(description="Log VR practice session (Pathos only)")
    parser.add_argument("--grade", default="0", help="Grade 0-V")
    parser.add_argument("--ritual", default="14", help="Ritual ID e.g. 14")
    parser.add_argument("--mode", default="Pathos", choices=["Logos", "Pistis", "Pathos", "Gnosis"])
    parser.add_argument("--boundary", type=float, default=3.0)
    parser.add_argument("--coherence", type=float, default=3.0)
    parser.add_argument("--coupling", type=float, default=3.0)
    parser.add_argument("--disorganization", type=float, default=2.0)
    parser.add_argument("--veil", type=int, default=None)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    entry = log_session(
        grade=args.grade,
        ritual_id=args.ritual,
        epistemic_mode=args.mode,
        boundary=args.boundary,
        coherence=args.coherence,
        coupling=args.coupling,
        disorganization=args.disorganization,
        notes=args.notes,
        veil=args.veil,
    )
    print(f"Logged to {SESSIONS_PATH}")
    print(f"Label: {LABEL}")
    print(json.dumps(entry, indent=2))


if __name__ == "__main__":
    main()
