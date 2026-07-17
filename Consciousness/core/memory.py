from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _trigrams(text: str) -> set:
    text = text.lower()
    tokens = text.split()
    grams = set()
    for i in range(len(tokens) - 2):
        grams.add((tokens[i], tokens[i + 1], tokens[i + 2]))
    return grams


@dataclass
class MemoryRecord:
    timestamp: float
    prompt: str
    response: str
    rewards: Dict[str, float]
    strategy: Dict[str, Any]


class LocalMemoryStore:
    """Very small JSONL memory for conversation turns and rewards.

    - Append-only JSONL at `Consciousness/.memory/memory.jsonl` by default
    - Simple trigram Jaccard similarity for retrieval
    """

    def __init__(self, memory_dir: str = "Consciousness/.memory", filename: str = "memory.jsonl") -> None:
        self.memory_dir = memory_dir
        self.filename = filename
        _ensure_dir(self.memory_dir)
        self.path = os.path.join(self.memory_dir, self.filename)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                f.write("")

    def append(self, record: MemoryRecord) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    def _iter_records(self) -> List[MemoryRecord]:
        records: List[MemoryRecord] = []
        if not os.path.exists(self.path):
            return records
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    records.append(
                        MemoryRecord(
                            timestamp=data.get("timestamp", time.time()),
                            prompt=data.get("prompt", ""),
                            response=data.get("response", ""),
                            rewards=data.get("rewards", {}),
                            strategy=data.get("strategy", {}),
                        )
                    )
                except Exception:
                    # Skip malformed lines
                    continue
        return records

    def recent(self, n: int = 5) -> List[MemoryRecord]:
        records = self._iter_records()
        return records[-n:]

    def find_similar(self, prompt: str, k: int = 3) -> List[Tuple[float, MemoryRecord]]:
        target = _trigrams(prompt)
        if not target:
            return []
        results: List[Tuple[float, MemoryRecord]] = []
        for rec in self._iter_records():
            grams = _trigrams(rec.prompt)
            if not grams:
                continue
            inter = len(target & grams)
            union = len(target | grams)
            if union == 0:
                continue
            sim = inter / union
            results.append((sim, rec))
        results.sort(key=lambda x: x[0], reverse=True)
        return results[:k]

    def average_recent_rewards(self, n: int = 10) -> Dict[str, float]:
        recs = self.recent(n)
        accum: Dict[str, Tuple[float, int]] = {}
        for r in recs:
            for k, v in r.rewards.items():
                total, cnt = accum.get(k, (0.0, 0))
                accum[k] = (total + float(v), cnt + 1)
        return {k: (total / cnt if cnt else 0.0) for k, (total, cnt) in accum.items()}

    def snapshot(self) -> List[Dict[str, Any]]:
        return [asdict(r) for r in self._iter_records()]
