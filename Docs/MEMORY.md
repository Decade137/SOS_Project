# Memory

## Stack

- Repository: git, branch `main`, remote `https://github.com/Decade137/SOS_Project.git`.
- Selected runtime: a C# console program. No source project has been created.
- The repo lives at `E:\UnityProject\SOS_Project\SOS_Project`. The parent directory only contains this repo. It is not a Unity project.

## Product

- Target: a single-player C# console game. Mostly prose, with occasional `■` pictures in console colors. The player picks numbered options and plays themself. Play is deduction and puzzle-solving. Scenario modules use a Call of Cthulhu–style TRPG shape. Fiction is the world of The Melancholy of Haruhi Suzumiya. Contract: `Docs/GAME_DESIGN.md`.
- Current implementation: the design contract and handoff docs only. No scenario prose and no executable.
- Presentation reference from 2026-09-24: a Windows `cmd` window (dark background, version banner, path prompt).

## User preferences

- The user (le) writes in Chinese and prefers to work in code.
- Keep session logs concise unless expansion is requested.
- Do not commit, compile, or start an engine unless that action is explicitly requested.
- Chinese mirrors stay fact-aligned with the English docs. English is canonical.
- The user will decide the first module's incident later. Do not invent that plot.

## Decisions

- 2026-09-24: "CoC-like" means the module shape in `Docs/GAME_DESIGN.md` (keeper brief, timeline, people, places, clues, scenes, options, outcomes, handouts). It does not adopt Chaosium's rule text, Sanity, or Mythos statistics.
- 2026-09-24: The program is the Keeper. One human player. The player plays themself, in second person, with no invented name and no canon role.
- 2026-09-24: The player selects a numbered option. Puzzle conclusions appear only after their required clues are found. No dice and no skill list.
- 2026-09-24: Usual output is prose. Optional pictures are `■` plus console colors, printed with `Console.Write`.
- 2026-09-24: Primary play is deduction and puzzle-solving.
- 2026-09-24: Scenarios are Markdown files that follow that heading contract. An engine data format waits until implementation starts.
- 2026-09-24: This is an unofficial fan project. Published prose, scripts, lyrics, and official assets are not copied into the repo.
- 2026-09-24: The runtime is a C# console program. Do not scaffold it until the user asks. Do not add Unity.

## Constraints

- No program exists yet, so behavior in `Docs/GAME_DESIGN.md` is a target, not observed play.
- Official Haruhi text and assets are copyrighted. Module prose has to be original.
- The unchosen plot blocks the first scenario. It does not leave the runtime undecided.

## Open questions

Details: `Docs/GAME_DESIGN.md`.

- Which incident the first module investigates. The user is still deciding.
- That module's tone note, chosen with the plot.
- Player-facing language.
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted. Dice are not used.
