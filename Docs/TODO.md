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
- Work: the selected first module uses a spatial route mystery, cross-era relationships, and an alien-AI observation puzzle. It is Chinese first person in a fictional unnamed city and follows the eight-stage story circle. Attribute names, values, and check resolution remain open for future modules; this one uses direct options.
- Done when: the selected story direction and first-person language are recorded in `Docs/MEMORY.md` and `Docs/GAME_DESIGN.md` and reviewed against the completed module (met).

## P1

### DES-003 Scenario 0 full module
- Status: Complete
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: one Chinese first-person Markdown module with the full story circle, original prose, two endings, clue-gated deduction, and direct options.
- Done when: all contracted sections, reveal conditions, clue gates, and beat options are present, with editorial review and both ending paths played through (met).

### ENG-001 C# console runtime
- Status: Complete
- Dependencies: the user asked to begin implementation. Runtime choice is a .NET 10 C# console. Ship target is a Windows x64 self-contained single-file exe.
- Current files: `Game/SOS_Project.csproj`, `Game/Program.cs`, `Game/Story.cs`, `Game/GameState.cs`, `Game/SaveStore.cs`, `Game/StoryRunner.cs`, `Game/OwnFileCleanup.cs`.
- Work: the source advances numbered choices, applies clue and flag gates and effects, re-reads found material, prints occasional colored `■` pictures, resumes a single save, and handles both outcomes with scoped cleanup for the send-back ending. Keeper notes stay out of player output.
- Done when: static review confirms the source follows the design contract and an authorized .NET 10 build and both ending runs confirm console behavior (met). No automated test suite was run. Do not add Unity.

### ENG-002 Connect the rest of scenario 0
- Status: Complete
- Dependencies: ENG-001, DES-003; resolve their validation findings as the remaining content is connected.
- Current files: `Scenarios/00-zero-floor.md`, `Scenarios/ZeroFloor.Play.cs`, `Game/Story.cs`, `Game/StoryRunner.cs`.
- Work: connect S06–S16, the remaining clues and handouts, gated deduction, and both ending paths without exposing keeper notes. Preserve direct options and stage handout additions to avoid early clues.
- Done when: static flow review confirms both endings are reachable through documented conditions and feedback, and an authorized play run confirms both paths in the program (met).

### REL-001 Windows single-file release
- Status: Complete
- Dependencies: ENG-001, ENG-002, and explicit user authorization to build and publish (fulfilled).
- Current files: `Game/SOS_Project.csproj`, `README.md`, local ignored output `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`.
- Work: built and played both paths, published the Windows x64 self-contained single-file exe, and verified E01 self-deletion on a disposable copy.
- Done when: the resulting exe and both endings have been observed on the target platform and the local release file is ready to hand over (met).
