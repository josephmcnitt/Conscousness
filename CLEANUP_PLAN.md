# Cleanup Plan — 7/17/26

## Tier 1 — safe, do now (low risk, clearly superseded)

1. **Retire `research/esoteric/rituals/`** (old pre-VR ritual folder, 01–05 + README). Its own README already says "Canonical copies: `via_resonantiae/rituals/grade_0/`" and `curriculum.md` calls the whole old path superseded. Not linked from `VIA_RESONANTIAE.md` or `GRADE_SYSTEM.md`. Two of its five files (01, 04) have already drifted from the canonical version — a live hazard if anyone edits the wrong copy.
   `git rm -r research/esoteric/rituals/`
2. **Delete `Journal.txt`** at repo root — the unfilled 7/9 prep entry, superseded by `Journal.md`.
   `git rm Journal.txt`

## Tier 2 — needs your call (real code, higher stakes)

Both `/core/` (17 files) and the nested `/Consciousness/` (which includes its own `Consciousness/core/`, 7 files, a subset of core's filenames) were introduced in the *same single commit* (`cd166f0 "Cursor: Apply local changes for cloud agent"`) — this has the signature of a cloud-agent dump that landed both an older, smaller copy and a newer, fuller one. `/core/` has everything `/Consciousness/core/` has plus more (`ethical_safeguards.py`, `feedback_loop.py`, `reward_system.py`, `quantum_consciousness.py`, etc.), but the shared filenames aren't identical — they've diverged, not just been extended. There's also a triple-nested `Consciousness/Consciousness/.memory/memory.jsonl` (1.8MB of old test-run logs) that looks like an accidental copy-of-a-copy.

Before I'd touch this: worth you (or me, if you want) diffing the handful of shared files to confirm `/core/` really is the superset, then archiving or removing the nested `/Consciousness/` tree. I didn't do this yet since it's functioning code, not docs.

## Tier 3 — housekeeping (low risk, your call on priority)

- Five SQLite `.db` files at root (`Luminara_consciousness_memory.db`, `consciousness_memory.db`, `test_memory.db`, etc.) are runtime artifacts currently tracked in git. Add `*.db` to `.gitignore` and `git rm --cached` them (keeps them on disk, stops bloating history).
- Five loose `test_*.py` files at root with no `tests/` folder — cosmetic, move whenever convenient.

## Status

Tier 1 not yet executed — waiting on your go-ahead in chat.
