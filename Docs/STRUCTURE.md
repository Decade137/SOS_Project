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
- `Game/SOS_Project.csproj`: `net10.0` console project; compiles the playable scenario data into the program.
- `Game/Program.cs`: console entry point.
- `Game/Story.cs`: scenes, choices, clues, handouts, and state data.
- `Game/StoryRunner.cs`: numbered choice loop, state effects, re-reading, and optional color pictures.
- `Scenarios/00-zero-floor.md`: authored first-person Chinese scenario 0, with the eight-stage story circle and full module sections.
- `Scenarios/ZeroFloor.Play.cs`: compiled player-facing data for the Hook, S00–S05, K01–K03, and initial H01.
- `Docs/LOGS/`: deep session notes. Empty except `.gitkeep`.
- `.git/`: repository metadata. Do not hand-edit.

Chinese mirrors use the same path plus `.zh-CN.md`. There is no `AGENTS.zh-CN.md`.

## Feature → files

- Handoff policy: `AGENTS.md`, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Product contract: `Docs/GAME_DESIGN.md`, `Docs/GAME_DESIGN.zh-CN.md`
- First-scenario decisions: `Docs/MEMORY.md`, `Docs/GAME_DESIGN.md`, and their Chinese mirrors.
- Scenario 0 prose and keeper notes: `Scenarios/00-zero-floor.md` (Chinese source of truth; no English translation yet).
- Scenario 0 playable opening data: `Scenarios/ZeroFloor.Play.cs` (derived from the Markdown; no keeper-only notes in player output).
- Console runtime: `Game/Program.cs`, `Game/Story.cs`, `Game/StoryRunner.cs`, `Game/SOS_Project.csproj`.
- Durable decisions: `Docs/MEMORY.md`, `Docs/MEMORY.zh-CN.md`
- Next work: `Docs/TODO.md`, `Docs/TODO.zh-CN.md`
- Runtime decision: .NET 10 C# console, targeting a Windows x64 self-contained single-file exe, in `Docs/GAME_DESIGN.md`. Source is under `Game/`; publishing has not run.

`Scenarios/` contains the full scenario 0 draft and the compiled opening slice. The user has asked to begin implementation; the C# project is in `Game/`.

## Documentation index

- `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` is not created. Add it only when an evidence artifact exists.
