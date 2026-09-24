# AGENTS.md

SOS_Project is an unofficial single-player console text game. Scenario modules follow a Call of Cthulhu–style TRPG structure; the fiction is the world of The Melancholy of Haruhi Suzumiya. Keep every change small, explicit, and easy for the next AI or developer to inspect.

## Hard Rules

- Prefer the smallest working change. Avoid speculative abstractions.
- Do not use reflection unless the user explicitly asks.
- The selected runtime is a C# console program, recorded in `Docs/GAME_DESIGN.md`. Do not scaffold that program until the user asks to implement. Do not add Unity. The parent folder name `UnityProject` is not a Unity project.
- Do not run an IDE, engine, automated tests, or a dev server unless the user explicitly asks.
- Do not invoke skills unless the user explicitly asks for that skill.
- Preserve existing user changes in a dirty worktree. Never revert unrelated files.
- Do not commit unless the user explicitly asks.
- Do not copy published Haruhi prose, scripts, lyrics, or official assets into the repo. Write original module text.
- Player-facing text and keeper-only text stay in separate sections.
- Every work session must update `Docs/MEMORY.md` when a durable fact changed, and must update `Docs/PROCESS.md`, plus the Chinese mirrors of any file that changed.
- After code, ownership, or feature-file changes, update `Docs/STRUCTURE.md` and `Docs/STRUCTURE.zh-CN.md`.
- Do not implement a product choice that is still an open question. Record the decision in `Docs/MEMORY.md` and `Docs/GAME_DESIGN.md` first.

## Product Direction

- Target: a C# console session. Mostly prose, occasional `■` pictures in console colors, numbered options, the player plays themself, deduction puzzles. Module contract: `Docs/GAME_DESIGN.md`.
- Current implementation: documentation only. No scenes and no C# project.

## Code Style

- Prefer small compositional units with one responsibility.
- When implementation starts, use C# and `System.Console`. Do not add a framework unless the user asks.
- Keep scenario prose in future `Scenarios/` files, separate from engine code.
- Prefer project-owned code. There is no vendor tree yet.
- If a vendor tree is added later, patch it only when public APIs are insufficient, and record the reason in `Docs/MEMORY.md`.

## Ownership

- Project-owned: `AGENTS.md`, `README.md`, `Docs/`, and future `Scenarios/` and source directories.
- Do not hand-edit `.git/`.
- `Docs/AI_PROJECT_HANDOFF_RULES.md` is the portable handoff spec. Change this project's policy in `AGENTS.md`. Do not rewrite the portable spec unless the user asks to change the handoff system.

## Documentation Routine

- `Docs/MEMORY.md`: durable facts, preferences, decisions, constraints
- `Docs/PROCESS.md`: workflow rules and concise dated session history
- `Docs/STRUCTURE.md`: directory map and feature-to-file index
- `Docs/TODO.md`: prioritized backlog
- `Docs/GAME_DESIGN.md`: scenario module contract and product boundaries
- `Docs/LOGS/`: optional deep session notes (`YYYY-MM-DD-topic.md`)
- English core docs are canonical. Chinese `*.zh-CN.md` mirrors must match facts in the same session.

## Default Workflow

1. Read `AGENTS.md`, `Docs/MEMORY.md`, `Docs/PROCESS.md`, `Docs/STRUCTURE.md`, `Docs/GAME_DESIGN.md`, and any feature doc the task needs.
2. Inspect git status; preserve unrelated changes.
3. Make the smallest useful change within ownership boundaries.
4. Static checks by default. Heavy verification only when the user asks.
5. Update docs as required above.
6. Report changed files, verification performed, and anything not validated.
