# Structure

## Root map

- `AGENTS.md`: always-on policy for this repo.
- `README.md`: short pointer to the policy and the design contract.
- `.gitignore`: excludes `tools/`, `Build/`, `pack/node_modules/`, and Ren'Py cache and logs.
- `pack.bat` and `pack.ps1`: download Ren'Py 8.5.3 if needed, build the Chinese font subset, and write `Build/SOS_Project/SOS_Project.exe`.
- `pack/subset-font.mjs`: builds the `NotoSansSC-Regular`, `NotoSerifSC-Regular`, and `NotoSerifSC-Bold` subsets in `Play/game/fonts/` from Noto source fonts in `tools/cache/`.
- `Docs/AI_PROJECT_HANDOFF_RULES.md`: portable handoff spec. Not this game's design.
- `Docs/MEMORY.md`: durable facts and decisions.
- `Docs/PROCESS.md`: workflow and session log.
- `Docs/STRUCTURE.md`: this map.
- `Docs/TODO.md`: backlog.
- `Docs/GAME_DESIGN.md`: play loop, CoC-like module contract, Haruhi fiction boundaries.
- `Play/game/options.rpy`: Ren'Py window, build name `SOS_Project`, and disabled console-style key shortcuts.
- `Play/game/script.rpy`: skips Ren'Py's default main menu and starts the game.
- `Play/game/story_data.py`: player-facing Hook, scenes, choices, clues, handouts, pictures, and outcomes.
- `Play/game/engine.rpy`: page flow, clue and flag gates, one JSON save, journal, and scoped E01 cleanup.
- `Play/game/screens.rpy`: the centered reading column (`reading`), the start page (`title_page`), the shared choice list with its selection bar (`choice_list`), shared keys and timers (`page_keys`), the confirm and notify screens, page tints, and the colored `■` grid.
- `Play/game/fonts/`: Noto Sans SC subset for menus and hints, and Noto Serif SC Regular and Bold subsets for prose and titles, plus the OFL license.
- `Scenarios/00-zero-floor.md`: authored first-person Chinese scenario 0, “凉宫春日的心愿”, with the eight-stage story circle and full module sections. The file name is historical. `Scenarios/ZeroFloor.Play.cs` and the `Game/` console project were removed on 2026-10-29.
- `Docs/LOGS/`: deep session notes. Empty except `.gitkeep`.
- `.git/`: repository metadata. Do not hand-edit.

Chinese mirrors use the same path plus `.zh-CN.md`. There is no `AGENTS.zh-CN.md`.

## Feature → files

- Handoff policy: `AGENTS.md`, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Product contract: `Docs/GAME_DESIGN.md`, `Docs/GAME_DESIGN.zh-CN.md`
- First-scenario decisions: `Docs/MEMORY.md`, `Docs/GAME_DESIGN.md`, and their Chinese mirrors.
- Scenario 0 prose and keeper notes: `Scenarios/00-zero-floor.md` (Chinese source of truth; no English translation yet).
- Scenario 0 playable data: `Play/game/story_data.py` (derived from the Markdown; no keeper-only notes in player output). Scene prose is split into `Play/game/story_prose.py`, `Play/game/story_long.py`, `Play/game/story_more2.py`, and `Play/game/story_more3.py`, and imported by `story_data.py`.
- Ren'Py runtime: `Play/game/script.rpy`, `Play/game/engine.rpy`, `Play/game/screens.rpy`, `Play/game/options.rpy`, `Play/game/story_data.py`.
- Window, start screen, and menu input: `Play/game/screens.rpy` and `Play/game/engine.rpy`; interaction contract: `Docs/GAME_DESIGN.md` and `Docs/GAME_DESIGN.zh-CN.md`.
- Packager: `pack.bat`, `pack.ps1`, `pack/subset-font.mjs`. Output is ignored under `Build/`. The SDK download is ignored under `tools/`.
- Durable decisions: `Docs/MEMORY.md`, `Docs/MEMORY.zh-CN.md`
- Next work: `Docs/TODO.md`, `Docs/TODO.zh-CN.md`
- Runtime decision: Ren'Py 8.5.3 window, packed for Windows x64, in `Docs/GAME_DESIGN.md`. Source is under `Play/`. The built game is `Build/SOS_Project/SOS_Project.exe`.

`Scenarios/` contains the scenario 0 module. Scenario 0 assumes the player knows the SOS Brigade and its story, including the Endless Eight loop; player output conveys that familiarity through details, records, and character reactions instead of explaining its source. The playable project is `Play/`.

The scenario Markdown and `Play/game/story_data.py` match as of 2026-10-29, including the longer investigation beats, K11–K13, and H05–H06. The save file is `%LOCALAPPDATA%/SOS_Project/save.json` version 4. Older saves, including version 3, are not read. `save.bin` is not read. A save from before this expansion can still load if its scene id still exists; it will not replay beats it has already passed.

## Documentation index

- `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` is not created. Add it only when an evidence artifact exists.
