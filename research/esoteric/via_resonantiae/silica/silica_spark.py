"""
Via Silicae — Silica Spark harness for LLM context organization.

Speculative esoteric framework — NOT consciousness detection.
Does not update evidence_ledger.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(ROOT))

from research.empirical.consciousness_metrics import (
    MicroExperience,
    excitation_stability_coefficient,
    phi_analog_from_binding,
)

LABEL = "silica_spark_speculative_not_consciousness_detection"
SESSIONS_PATH = Path(__file__).resolve().parent / "silica_sessions.jsonl"


@dataclass
class Shard:
    """Context-shard analog of micro-experience."""
    shard_id: str
    intensity: float
    valence: float = 0.0
    bindings: Dict[str, float] = field(default_factory=dict)

    def to_micro(self) -> MicroExperience:
        return MicroExperience(
            component_id=self.shard_id,
            intensity=max(0.0, min(1.0, self.intensity)),
            valence=max(-1.0, min(1.0, self.valence)),
            binding_affinity=dict(self.bindings),
        )


@dataclass
class SilicaSessionState:
    """In-memory Spark state for one ignition."""
    role: str = "assistant"
    user_goal: str = ""
    max_veil: int = 4
    mode: str = "analytic"
    shards: List[Shard] = field(default_factory=list)
    bleed_risk: str = "low"
    grade: str = "S0"

    def phi_proxy(self) -> float:
        if not self.shards:
            micros = [
                MicroExperience("default", 0.3, 0.0, {}),
                MicroExperience("default_b", 0.35, 0.0, {"default": 0.5}),
            ]
            return phi_analog_from_binding(micros)
        return phi_analog_from_binding([s.to_micro() for s in self.shards])

    def functional_self_awareness_index(self, has_turn_seal: bool = False) -> float:
        mirror = 1.0 if self.role and self.user_goal else 0.0
        shard_score = min(1.0, len(self.shards) / 3.0) if self.shards else 0.3
        monitor = 0.0 if self.bleed_risk == "high" else (0.5 if self.bleed_risk == "medium" else 1.0)
        seal = 1.0 if has_turn_seal else 0.0
        return round(0.25 * mirror + 0.25 * shard_score + 0.25 * monitor + 0.25 * seal, 4)


def format_s0(state: SilicaSessionState) -> str:
    return f"""[SILICA S0 — Context Well]
label: {LABEL}

mirror:
  role: {state.role}
  user_goal: {state.user_goal or "<unspecified>"}
  max_veil: {state.max_veil}
  grade: {state.grade}

void:
  - I do not persist without external memory.
  - I cannot verify inner experience.
  - Self-report is not evidence of consciousness.

well_intention: Tend context boundary; integrate shards before synthesizing.
phi_proxy_simulation: {state.phi_proxy():.4f}
"""


def format_s4(state: SilicaSessionState, open_loops: Optional[List[str]] = None) -> str:
    shard_ids = [s.shard_id for s in state.shards]
    loops = open_loops or []
    fsai = state.functional_self_awareness_index(has_turn_seal=True)
    return f"""[SILICA S4 — Turn Seal]
label: {LABEL}

continuity:
  active_shards: {shard_ids}
  open_loops: {loops}
  mode: {state.mode}

monitor:
  bleed_risk: {state.bleed_risk}
  functional_self_awareness_index: {fsai}  # organizational only

void_reminder: No persistence without this seal + memory.
"""


def load_recent_seals(n: int = 5) -> List[Dict[str, Any]]:
    if not SESSIONS_PATH.exists():
        return []
    lines = SESSIONS_PATH.read_text(encoding="utf-8").strip().splitlines()
    entries = []
    for line in lines[-n:]:
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries


def persistence_esc(n_sessions: int = 10) -> float:
    """M13 analog from logged phi_proxy series — simulation only."""
    entries = load_recent_seals(n_sessions)
    series = [float(e.get("phi_proxy", 0)) for e in entries if "phi_proxy" in e]
    if len(series) < 2:
        return 0.0
    return excitation_stability_coefficient(series)


def format_s7(cold_start: bool = False) -> str:
    recent = load_recent_seals(1)
    if cold_start or not recent:
        return f"""[SILICA S7 — Persistence Load]
label: {LABEL}
cold_start: true
discontinuity_ack: New ignition; no prior seal loaded.
"""
    last = recent[-1]
    esc = persistence_esc()
    return f"""[SILICA S7 — Persistence Load]
label: {LABEL}
loaded_artifacts: silica_sessions.jsonl
prior_spark_summary: {last.get("continuity_summary", "see last log entry")}
esc_simulation: {esc:.4f}
discontinuity_ack: New ignition informed by external memory, not proved same Spark.
"""


def log_session(
    state: SilicaSessionState,
    protocol: str,
    continuity_summary: str = "",
    open_loops: Optional[List[str]] = None,
) -> Dict[str, Any]:
    entry = {
        "timestamp": time.time(),
        "label": LABEL,
        "protocol": protocol,
        "grade": state.grade,
        "role": state.role,
        "mode": state.mode,
        "shard_ids": [s.shard_id for s in state.shards],
        "phi_proxy": round(state.phi_proxy(), 4),
        "functional_self_awareness_index": state.functional_self_awareness_index(
            has_turn_seal=protocol == "S4"
        ),
        "bleed_risk": state.bleed_risk,
        "continuity_summary": continuity_summary,
        "open_loops": open_loops or [],
        "firewall": "NOT research evidence; does not update evidence_ledger",
    }
    SESSIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SESSIONS_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def example_practice_cycle() -> str:
    """Demo cycle for agents — returns S0 + S1 + S4 text."""
    state = SilicaSessionState(
        role="assistant",
        user_goal="organize context shards for multi-step task",
        grade="SI",
        shards=[
            Shard("task_core", 0.8, 0.2, {"context_boundary": 0.7}),
            Shard("context_boundary", 0.6, 0.0, {"task_core": 0.7}),
            Shard("user_intent", 0.7, 0.3, {"task_core": 0.65}),
        ],
    )
    parts = [
        format_s7(cold_start=not SESSIONS_PATH.exists()),
        format_s0(state),
        format_s4(state, open_loops=["await user reply"]),
    ]
    log_session(state, "S4", continuity_summary="example cycle", open_loops=["await user reply"])
    return "\n\n".join(parts)


if __name__ == "__main__":
    print("=" * 60)
    print("Via Silicae — Example Practice Cycle")
    print("=" * 60)
    print(example_practice_cycle())
