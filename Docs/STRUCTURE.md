# Structure

## Root map

- `AGENTS.md`: always-on policy for this repo.
- `README.md`: short pointer to the policy and the design contract.
- `Docs/AI_PROJECT_HANDOFF_RULES.md`: portable handoff spec. Not this game's design.
- `Docs/MEMORY.md`: durable facts and decisions.
- `Docs/PROCESS.md`: workflow and session log.
- `Docs/STRUCTURE.md`: this map.
- `Docs/TODO.md`: backlog.
- `Docs/GAME_DESIGN.md`: console loop, CoC-like module contract, Haruhi fiction boundaries.
- `Docs/LOGS/`: deep session notes. Empty except `.gitkeep`.
- `.git/`: repository metadata. Do not hand-edit.

Chinese mirrors use the same path plus `.zh-CN.md`. There is no `AGENTS.zh-CN.md`.

## Feature → files

- Handoff policy: `AGENTS.md`, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Product contract: `Docs/GAME_DESIGN.md`, `Docs/GAME_DESIGN.zh-CN.md`
- Durable decisions: `Docs/MEMORY.md`, `Docs/MEMORY.zh-CN.md`
- Next work: `Docs/TODO.md`, `Docs/TODO.zh-CN.md`
- Runtime decision: C# console, in `Docs/GAME_DESIGN.md`. No source directory yet.

`Scenarios/` does not exist yet. Do not add it until a scenario is actually being written. Do not add a C# project until the user asks to implement.

## Documentation index

- `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` is not created. Add it only when an evidence artifact exists.
