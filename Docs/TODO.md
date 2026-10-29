# Backlog

Status legend: `Not started`, `Blocked by product choice`, `Ready for design`, `Ready for implementation`, `Implemented; validation pending`, `Complete`.

## P0

### DOC-001 Handoff and design contract
- Status: Complete
- Dependencies: none
- Current files: `AGENTS.md`, `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`, `Docs/GAME_DESIGN.md`, Chinese mirrors, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: keep the English docs and Chinese mirrors fact-aligned.
- Done when: a fresh session can read the product target, the module shape, and the open questions without guessing (met through the bilingual handoff review).

### DES-002 Choices that block the first module
- Status: Complete
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` open questions, `Docs/MEMORY.md`
- Work: the first module, rewritten 2026-09-30, is an Endless Eight branch on 2009-08-31: an otherworlder entrance exam, elimination deduction, and a written-in past. It is Chinese first person and follows the eight-stage story circle. Attribute names, values, and check resolution remain open for future modules; this one uses direct options.
- Done when: the selected story direction and first-person language are recorded in `Docs/MEMORY.md` and `Docs/GAME_DESIGN.md` and reviewed against the completed module (met).

## P1

### DES-003 Scenario 0 full module
- Status: Complete
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: one Chinese first-person Markdown module with the full story circle, original prose, three endings, clue-gated deduction, and direct options.
- Done when: all contracted sections, reveal conditions, clue gates, and beat options are present, with editorial review and all ending paths played through. Met for the previous version. The 2026-09-30 rewrite still needs a build and playthrough of E01, E02, and E03.

### ENG-001 Ren'Py window runtime
- Status: Implemented; validation pending
- Dependencies: the user asked to leave the console and use Ren'Py. Ship target is a Windows build produced by `pack.bat`.
- Current files: `Play/game/script.rpy`, `Play/game/options.rpy`, `Play/game/story_data.py`, `Play/game/engine.rpy`, `Play/game/screens.rpy`, `pack.bat`, `pack.ps1`.
- Work: the source advances choices, applies clue and flag gates and effects, re-reads found material, shows occasional colored `■` pictures, resumes a single save, and handles the three outcomes with scoped cleanup for the send-back ending. Keeper notes stay out of player output. On 2026-10-21, `pack.ps1` produced the exe and the packed window opened; a story playthrough is still pending.
- Done when: static review confirms the source follows the design contract, `pack.bat` produces `Build/SOS_Project/SOS_Project.exe`, and a playthrough confirms E01, E02, and E03. No automated test suite is run. Do not add Unity.

### ENG-002 Connect the rest of scenario 0
- Status: Complete
- Dependencies: ENG-001, DES-003; resolve their validation findings as the remaining content is connected.
- Current files: `Scenarios/00-zero-floor.md`, `Play/game/story_data.py`, `Play/game/engine.rpy`.
- Work: connect S06–S16, the remaining clues and handouts, gated deduction, and both ending paths without exposing keeper notes. Preserve direct options and stage handout additions to avoid early clues.
- Done when: static flow review confirms both endings are reachable through documented conditions and feedback, and an authorized play run confirms both paths in the program (met).

### REL-001 Windows Ren'Py build
- Status: Implemented; validation pending
- Dependencies: ENG-001, ENG-002. The user asked for a packager they can run without asking again.
- Current files: `pack.bat`, `pack.ps1`, `Play/game/options.rpy`, `README.md`, local ignored output `Build/SOS_Project/SOS_Project.exe`.
- Work: `pack.bat` builds the Windows game folder. E01 deletes the save and schedules deletion of only that folder's `SOS_Project.exe`. On 2026-10-21, `pack.ps1` produced `dist/SOS_Project/SOS_Project.exe` and the window opened. E01 cleanup on a disposable copy is still pending.
- Done when: `pack.bat` has produced the exe, and a playthrough has confirmed E01, E02, and E03, including E01 cleanup on a disposable copy.
