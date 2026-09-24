# Process

## Workflow rules

- Pre-edit reading order: `AGENTS.md` → `Docs/MEMORY.md` → `Docs/PROCESS.md` → `Docs/STRUCTURE.md` → `Docs/GAME_DESIGN.md` → other feature docs.
- Prefer static verification. Do not start an engine, tests, or a build without an explicit ask.
- One concise dated session entry per work session.
- Create `Docs/LOGS/YYYY-MM-DD-topic.md` and a Chinese mirror only when one PROCESS line is not enough.
- Do not reorder historical session entries.
- English is canonical when mirrors disagree. Fix mirrors in the same session.
- Do not run Unity, create a Unity project, or treat the parent folder name as an engine choice unless the user asks.

## Session history

- 2026-09-24: Bootstrapped the handoff set and `Docs/GAME_DESIGN.md` for a console text game whose modules follow a CoC-like TRPG shape and whose fiction is Haruhi Suzumiya. Verification: files created and checked for the required headings. Not run: no engine, tests, or builds exist.
- 2026-09-24: Recorded the C# console runtime, prose-first `■` color pictures, numbered options, the player as themself, and deduction as the primary play. The first incident stays undecided. Verification: English docs and Chinese mirrors updated together and re-read for those decisions. Not run: no C# project, tests, or builds.
- 2026-09-24: Restored attribute checks. At a clue hint the player chooses which attribute to test, and the result selects the next plot options. Attribute names and the roll procedure stay open. Verification: English docs and Chinese mirrors updated together. Not run: no C# project, tests, or builds.
- 2026-09-24: Some beats offer options directly, and some require an attribute check. A beat is one or the other. Verification: English docs and Chinese mirrors updated together. Not run: no C# project, tests, or builds.
- 2026-09-24: An attribute check may decide which of the current beat's plot options are displayed. The options stay on that beat. Verification: English docs and Chinese mirrors updated together. Not run: no C# project, tests, or builds.
- 2026-09-24: Chose the ship target: .NET 10, Windows x64, self-contained single-file console exe. Verification: support dates checked against Microsoft's .NET policy ( .NET 10 LTS through 2028-11-14; .NET 8 and .NET 9 end 2026-11-10). English docs and Chinese mirrors updated together. Not run: no C# project, publish, or build.
- 2026-09-24: The user asked for scenario frameworks to choose from. The ideas and themes were not in the message, so no incident was invented and no scenario file was added. Verification: prior docs still list the first incident as open. Not run: no C# project, tests, or builds.
- 2026-09-24: Recorded the user's first-scenario premise, comedy-to-serious tone, temporal/otherworldly/alien-AI elements, fair-play deduction preference, and pending outline choice. Verification: reviewed the design contract and checked the English/Chinese edits for alignment. Not run: no C# project, tests, or builds.
- 2026-09-24: Added the player's prior anime knowledge and made the philosophical questions personal to the player; the mystery now tests that knowledge instead of hiding Haruhi's power. Verification: static bilingual review and diff whitespace check. Not run: no C# project, tests, or builds.
- 2026-09-24: Authored `Scenarios/00-zero-floor.md` as the first-person Chinese full module in an unnamed city, with an eight-stage story circle, repeat time travel, clue-gated self-origin deduction, character arcs, and two endings. Updated the contract and bilingual handoff docs. Verification: editorial review, targeted static checks, and diff whitespace check. Not run: no game runtime, tests, or build.
- 2026-09-24: Began the `net10.0` console program and compiled story-data slice for the Hook through S05, including numbered choices, clue/flag state, re-reading, and optional colored `■` pictures. Updated the bilingual design and handoff docs. Verification: static source and documentation review. Not run: build, tests, or publish.
