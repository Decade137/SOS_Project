# Structure

## Root map

- `AGENTS.md`: always-on policy for this repo.
- `README.md`: short pointer to the policy and the design contract.
- `.gitignore`: excludes generated `Game/bin/`, `Game/obj/`, and root `SOS_Project.exe` outputs.
- `SOS_Project.exe`: Windows x64 self-contained single-file release copied to the repository root.
- `Docs/AI_PROJECT_HANDOFF_RULES.md`: portable handoff spec. Not this game's design.
- `Docs/MEMORY.md`: durable facts and decisions.
- `Docs/PROCESS.md`: workflow and session log.
- `Docs/STRUCTURE.md`: this map.
- `Docs/TODO.md`: backlog.
- `Docs/GAME_DESIGN.md`: console loop, CoC-like module contract, Haruhi fiction boundaries.
- `Game/SOS_Project.csproj`: `net10.0` console project; compiles the playable scenario data into the program.
- `Game/Program.cs`: console entry point.
- `Game/Story.cs`: scenes, choices, clues, handouts, and outcomes.
- `Game/GameState.cs`: current scene, discovered material, flags, text choices, and completed outcome.
- `Game/SaveStore.cs`: the versioned single-slot local save and its integrity check.
- `Game/StoryRunner.cs`: separate start/scene/action/journal/ending pages, variable-height Unicode story frames with terminal-buffer scrolling on interactive terminals, sequentially rendered option frames, and a fixed-frame PageUp/PageDown fallback, wrapped story output with dialogue cues, bullet-marked W/S and Enter menus with full-choice selection color, state effects, immediate re-reading, and optional color pictures.
- `Game/OwnFileCleanup.cs`: scoped send-back ending cleanup for this game's save and published exe.
- `Scenarios/00-zero-floor.md`: authored first-person Chinese scenario 0, “异世界人入团考试”, with the eight-stage story circle and full module sections. The file name is historical.
- `Scenarios/ZeroFloor.Play.cs`: compiled player-facing data for the full first scenario, Hook through S16, K01–K10, H01–H04 plus H01_REVISED, and E01–E03. The class name `ZeroFloor` is historical.
- `Docs/LOGS/`: deep session notes. Empty except `.gitkeep`.
- `.git/`: repository metadata. Do not hand-edit.

Chinese mirrors use the same path plus `.zh-CN.md`. There is no `AGENTS.zh-CN.md`.

## Feature → files

- Handoff policy: `AGENTS.md`, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Product contract: `Docs/GAME_DESIGN.md`, `Docs/GAME_DESIGN.zh-CN.md`
- First-scenario decisions: `Docs/MEMORY.md`, `Docs/GAME_DESIGN.md`, and their Chinese mirrors.
- Scenario 0 prose and keeper notes: `Scenarios/00-zero-floor.md` (Chinese source of truth; no English translation yet).
- Scenario 0 playable data: `Scenarios/ZeroFloor.Play.cs` (derived from the Markdown; no keeper-only notes in player output).
- Console runtime: `Game/Program.cs`, `Game/Story.cs`, `Game/GameState.cs`, `Game/SaveStore.cs`, `Game/StoryRunner.cs`, `Game/OwnFileCleanup.cs`, `Game/SOS_Project.csproj`.
- Console presentation, start screen, and menu input: `Game/StoryRunner.cs`; interaction contract: `Docs/GAME_DESIGN.md` and `Docs/GAME_DESIGN.zh-CN.md`.
- Build output policy: `.gitignore` excludes generated `Game/bin/`, `Game/obj/`, and root `SOS_Project.exe` files.
- Durable decisions: `Docs/MEMORY.md`, `Docs/MEMORY.zh-CN.md`
- Next work: `Docs/TODO.md`, `Docs/TODO.zh-CN.md`
- Runtime decision: .NET 10 C# console with a Windows x64 self-contained single-file exe, in `Docs/GAME_DESIGN.md`. Source is under `Game/`; a local publish is at `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`, and a copy is at the repository root as `SOS_Project.exe`.

`Scenarios/` contains the full scenario 0 module and compiled story data. Scenario 0 assumes the player knows the SOS Brigade and its story, including the Endless Eight loop; player output conveys that familiarity through details, records, and character reactions instead of explaining its source. The C# project is in `Game/`. The start screen and page layout passed a Release build and Windows x64 single-file publish earlier.

The scenario Markdown and compiled story data were rewritten together on 2026-09-30 and match. `Game/SaveStore.cs` now writes save version 2, so older saves are rejected. The published and repository-root exe files predate this rewrite; it has not been built or played.

## Documentation index

- `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` is not created. Add it only when an evidence artifact exists.
