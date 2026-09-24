# Memory

## Stack

- Repository: git, branch `main`, remote `https://github.com/Decade137/SOS_Project.git`.
- Selected runtime: a C# console program on .NET 10 (`net10.0`). The ship target is a Windows x64 self-contained single-file exe. The source project is `Game/SOS_Project.csproj`; no publish has been run.
- The repo lives at `E:\UnityProject\SOS_Project\SOS_Project`. The parent directory only contains this repo. It is not a Unity project.

## Product

- Target: a single-player C# console game on Windows, shipped as one exe. Mostly prose, with occasional `■` pictures in console colors. The player picks numbered options and plays themself. Play is deduction and puzzle-solving. Scenario modules use a Call of Cthulhu–style TRPG shape. Fiction is the world of The Melancholy of Haruhi Suzumiya. Contract: `Docs/GAME_DESIGN.md`.
- Current implementation: the full scenario 0 Markdown draft and an unvalidated C# console source slice. The compiled story data currently covers the Hook, S00–S05, K01–K03, and an initial H01. No executable has been built.
- Presentation reference from 2026-09-24: a Windows `cmd` window (dark background, version banner, path prompt).

## User preferences

- The user (le) writes in Chinese and prefers to work in code.
- Keep session logs concise unless expansion is requested.
- Do not commit, compile, or start an engine unless that action is explicitly requested.
- Chinese mirrors stay fact-aligned with the English docs. English is canonical.
- The user authorized the first full scenario; write lively, canon-consistent original dialogue and keep the player-facing perspective mainly first person.

## Decisions

- 2026-09-24: "CoC-like" means the module shape in `Docs/GAME_DESIGN.md` (keeper brief, timeline, people, places, clues, scenes, options, checks, outcomes, handouts). It does not adopt Chaosium's rule text, Sanity, or Mythos statistics.
- 2026-09-24: The program is the Keeper. One human player. The player plays themself, with no invented name or canon role. Initial second-person direction is superseded for the first module: it uses first-person Chinese narration and options. Perspective for later modules remains open.
- 2026-09-24: The player selects a numbered option. Puzzle conclusions appear only after their required clues are found. Superseded the same day: "no checks, no dice, and no skill list." Skill list stays out. Checks are back; see the next decision.
- 2026-09-24: Some beats show their plot options immediately. On other beats, an attribute check decides which of that beat's current options are displayed. The player chooses the attribute. Success and failure each name a visible subset. Attribute names, values, and the roll or target procedure are still open. Superseded the same day: a check beat has no option list.
- 2026-09-24: Usual output is prose. Optional pictures are `■` plus console colors, printed with `Console.Write`.
- 2026-09-24: Primary play is deduction and puzzle-solving.
- 2026-09-24: Scenarios are Markdown files that follow that heading contract. An engine data format waits until implementation starts.
- 2026-09-24: This is an unofficial fan project. Published prose, scripts, lyrics, and official assets are not copied into the repo.
- 2026-09-24: The runtime is a C# console program. Do not scaffold it until the user asks. Do not add Unity.
- 2026-09-24: Ship a Windows x64 self-contained single-file console exe on .NET 10. The player does not install a runtime. .NET 8 and .NET 9 both leave support on 2026-11-10. Native AOT stays unused until a later publish choice; it needs the Visual Studio C++ build tools.
- 2026-09-24: First-module premise: an abnormal branch from Endless Eight brings the SOS Brigade to a Chongqing-inspired Chinese city in 2026, where they meet the player. Repeated travel through 2009–2026, otherworldly space, and an AI tied to alien technology / the Information Integration Thought Entity expose changes in the city and its people. The story asks who the player is, where they came from, and where they will go. The final reveal is that Haruhi created the player as a person of this anomalous worldline. The endings are to return the Brigade to its normal worldline, removing this game's local exe and saves, or to remain in the apparently real created world. The tone is primarily lively comedy, turning serious near the truth. Canon-character dialogue must be original and in character.
- 2026-09-24: The first module should lead with fair-play deduction: natural prose and dialogue foreshadow the clues, cross-era evidence lets the player infer the answer, and the reveal should feel earned rather than delivered as an exposition dump. Clue ids and reveal conditions remain in the keeper-facing module structure.
- 2026-09-24: The player has watched the Haruhi anime and already knows Haruhi's godlike world-shaping ability. The three philosophical questions must address the player's own identity, origin, and destination. Prior knowledge is an investigative advantage and a potentially misleading assumption; the mystery is why this player has that knowledge and exists in the branch, not whether Haruhi has powers. Do not invent biographical facts about the real player.
- 2026-09-24: The first module is `Scenarios/00-zero-floor.md`, a complete Chinese first-person scenario in an unnamed fictional mountain city, using a spatial route mystery, cross-era family story, and alien-AI observation puzzle. It follows the eight-stage story circle around the player's journey, returns to the opening corridor for the final choice, and avoids real city/place names. The module uses direct options only while attributes remain undecided.
- 2026-09-24: The user asked to start programming against the authored scenario. `Game/SOS_Project.csproj` targets `net10.0`; `Game/Program.cs`, `Game/Story.cs`, and `Game/StoryRunner.cs` implement the console entry, scene and choice model, and runner. `Scenarios/ZeroFloor.Play.cs` is compiled story data derived from `Scenarios/00-zero-floor.md`, currently limited to the Hook, S00–S05, K01–K03, and initial H01. The runner handles numbered scene choices, clue and flag requirements and effects, re-reading found clues and handouts, and optional colored `■` pictures. At S05, `0` reopens the handout and either numbered choice ends the preview. Keeper-only notes stay out of player output. This source has not been built or tested.

## Constraints

- The console source is not yet built or tested, so its behavior is not observed play. Most of the loop in `Docs/GAME_DESIGN.md` remains a target for later slices.
- Official Haruhi text and assets are copyrighted. Module prose has to be original.
- The first scenario is authored but not playtested. The runtime and the Windows exe publish target are decided. Deleting the game's own exe and saves is a target ending behavior, not current functionality; its implementation details remain open.
- The current slice does not include attribute-check rules, the remaining scenario scenes or endings, saves, or file deletion.

## Open questions

Details: `Docs/GAME_DESIGN.md`.

- Which attributes exist, how the player gets those values, and how a check is resolved.
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted.
