# Backlog

Status legend: `Not started`, `Blocked by product choice`, `Ready for design`, `Ready for implementation`, `Implemented; validation pending`.

## P0

### DOC-001 Handoff and design contract
- Status: Implemented; validation pending
- Dependencies: none
- Current files: `AGENTS.md`, `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/TODO.md`, `Docs/GAME_DESIGN.md`, Chinese mirrors, `Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: keep the English docs and Chinese mirrors fact-aligned.
- Done when: a fresh session can read the product target, the module shape, and the open questions without guessing.

### DES-002 Choices that block the first module
- Status: Implemented; validation pending
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` open questions, `Docs/MEMORY.md`
- Work: the selected first module uses a spatial route mystery, cross-era relationships, and an alien-AI observation puzzle. It is Chinese first person in a fictional unnamed city and follows the eight-stage story circle. Attribute names, values, and check resolution remain open for future modules; this one uses direct options.
- Done when: the selected story direction and first-person language are recorded in `Docs/MEMORY.md` and `Docs/GAME_DESIGN.md` (done); confirm through editorial review.

## P1

### DES-003 Scenario 0 full module
- Status: Implemented; validation pending
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: one Chinese first-person Markdown module with the full story circle, original prose, two endings, clue-gated deduction, and direct options. No engine.
- Done when: header, keeper brief, timeline, hook, people, places, clues, scenes, options, checks, outcomes, and handouts are present. Each clue has a reveal condition. Each concluding option lists its required clue ids. Each beat lists its options and is marked direct options or an attribute check. Editorial and playflow validation remain.

### ENG-001 C# console runtime
- Status: Implemented; validation pending
- Dependencies: the user asked to begin implementation. Runtime choice is a .NET 10 C# console. Ship target is a Windows x64 self-contained single-file exe.
- Current files: `Game/SOS_Project.csproj`, `Game/Program.cs`, `Game/Story.cs`, `Game/StoryRunner.cs`, `Scenarios/ZeroFloor.Play.cs`.
- Work: the source framework advances numbered choices, applies clue and flag requirements and effects, supports re-reading found clues and handouts, and prints optional colored `■` pictures. Compiled story data covers the Hook, S00–S05, K01–K03, and an initial H01. In S05, `0` reopens the handout and either numbered choice ends the preview. Keeper notes are excluded from player output.
- Done when: static review confirms the opening slice matches the authored scenario, and a separately authorized build or play run confirms console behavior. No build, test, or publish has been run. Do not add Unity.

### ENG-002 Connect the rest of scenario 0
- Status: Ready for implementation
- Dependencies: ENG-001, DES-003; resolve their validation findings as the remaining content is connected.
- Current files: `Scenarios/00-zero-floor.md`, `Scenarios/ZeroFloor.Play.cs`, `Game/Story.cs`, `Game/StoryRunner.cs`.
- Work: connect S06–S16, the remaining clues and handouts, gated deduction, and both ending paths without exposing keeper notes. Preserve direct options for this module. Attribute rules, saves, and deletion of the game's own exe and saves remain separate decisions or later work.
- Done when: the complete authored scenario can reach both endings through its documented conditions and feedback, with the clue gates and re-reading intact. Verify by an authorized play run when requested.
