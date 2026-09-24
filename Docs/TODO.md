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
- Status: Blocked by product choice
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` open questions, `Docs/MEMORY.md`
- Work: the user will decide the first incident. With it, record that module's tone note. Player-facing language is still open. Already decided: numbered options, the player plays themself, deduction puzzles, C# console, optional `■` color pictures.
- Done when: the first incident and its tone note are decisions in `Docs/MEMORY.md`, and `Docs/GAME_DESIGN.md` matches. Language can stay open only if the scenario's language is explicitly deferred there too.

## P1

### DES-003 Scenario 0 outline
- Status: Not started
- Dependencies: DES-002
- Current files: none. Future file belongs in `Scenarios/` only when writing starts.
- Work: one Markdown module that fills every heading in the design contract. Original prose. No engine.
- Done when: header, keeper brief, timeline, hook, people, places, clues, scenes, options, outcomes, and handouts are present. Each clue has a reveal condition. Each concluding option lists its required clue ids.

### ENG-001 C# console runtime
- Status: Not started
- Dependencies: the user asks to implement. Runtime choice is already C# console.
- Current files: none. Do not add a project directory as a placeholder.
- Work: when asked, a C# console program that prints one scene's prose, prints a `■` color picture only if that scene has one, and accepts one numbered option.
- Done when: that program does those three things with authored text. Not started until the user asks. Do not add Unity.
