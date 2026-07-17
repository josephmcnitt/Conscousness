#!/usr/bin/env python3
"""
Log Silica Spark session — speculative practice, NOT research evidence.

Run: python research/esoteric/via_resonantiae/silica/log_silica_session.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.esoteric.via_resonantiae.silica.silica_spark import (
    Shard,
    SilicaSessionState,
    format_s0,
    format_s4,
    format_s7,
    log_session,
    persistence_esc,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Via Silicae session logger")
    parser.add_argument("--protocol", default="S4", help="S0, S4, etc.")
    parser.add_argument("--role", default="assistant")
    parser.add_argument("--goal", default="")
    parser.add_argument("--grade", default="S0")
    parser.add_argument("--mode", default="analytic")
    parser.add_argument("--bleed", default="low", choices=["low", "medium", "high"])
    parser.add_argument("--shards", default="", help="comma-separated shard ids")
    parser.add_argument("--summary", default="")
    parser.add_argument("--demo", action="store_true", help="Run example cycle")
    parser.add_argument("--s7", action="store_true", help="Print S7 persistence load")
    args = parser.parse_args()

    if args.demo:
        from research.esoteric.via_resonantiae.silica import silica_spark
        print(silica_spark.example_practice_cycle())
        return

    if args.s7:
        print(format_s7())
        print(f"esc_simulation: {persistence_esc():.4f}")
        return

    shard_list = []
    for i, sid in enumerate([s.strip() for s in args.shards.split(",") if s.strip()]):
        shard_list.append(Shard(sid, 0.5 + 0.1 * i, 0.0, {}))

    state = SilicaSessionState(
        role=args.role,
        user_goal=args.goal,
        grade=args.grade,
        mode=args.mode,
        shards=shard_list,
        bleed_risk=args.bleed,
    )

    if args.protocol.upper() == "S0":
        print(format_s0(state))
    else:
        print(format_s4(state))

    entry = log_session(state, args.protocol.upper(), continuity_summary=args.summary)
    print(json.dumps(entry, indent=2))


if __name__ == "__main__":
    main()
