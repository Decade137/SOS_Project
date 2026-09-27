# Memory

## Stack

- Repository: git, branch `main`, remote `https://github.com/Decade137/SOS_Project.git`.
- Selected runtime: a C# console program on .NET 10 (`net10.0`). The ship target is a Windows x64 self-contained single-file exe. The source project is `Game/SOS_Project.csproj`; a local publish is at `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`.
- The current workspace is `D:\MyProject\SOS_Project`. It is not a Unity project.

## Product

- Target: a single-player C# console game on Windows, shipped as one exe. Mostly prose, with occasional `■` pictures in console colors. The player navigates numbered options with W/S, confirms with Enter, and plays themself. Play is deduction and puzzle-solving. Scenario modules use a Call of Cthulhu–style TRPG shape. Fiction is the world of The Melancholy of Haruhi Suzumiya. Contract: `Docs/GAME_DESIGN.md`.
- Current implementation: the full scenario 0 Markdown module and C# console program for Hook, S00–S16, K01–K10, H01–H04, and E01/E02, with a single save slot, scoped send-back cleanup, character-by-character text, and W/S choice menus. The current presentation passed a .NET 10 Release build and Windows x64 single-file publish. Both ending paths and self-deletion of a disposable published copy were validated on the earlier version; the current presentation has not been played yet.
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
- 2026-09-27: The first playable release is scoped to the complete scenario 0. It uses direct options; attribute checks and trackable resources remain future questions. A single versioned save at `%LOCALAPPDATA%/SOS_Project/save.bin` is written after each choice except final send-back confirmation, so an interrupted ending can be confirmed again. It can be continued or replaced from startup. The send-back ending, after two in-story confirmations, deletes that save after its text and attempts to delete only its own published `SOS_Project.exe` after exit; source runs and non-Windows runs delete only the save. The stay ending retains both.
- 2026-09-27: With explicit user authorization, the .NET 10 console build succeeded, both scenario 0 endings were played through, the Windows x64 self-contained single-file exe was published, and a disposable copy was observed deleting itself after E01. The publish output remains local and is ignored by Git.
- 2026-09-27: Player-facing story text appears character by character before choices. W/S moves through the numbered choices and Enter confirms; this supersedes typing a choice number during interactive play. Re-reading found material displays it immediately. Pressing a key finishes the current text reveal.
- 2026-09-27: At the user's request, the new text and menu interaction passed a Release build with .NET SDK 10.0.401 (zero warnings and errors) and was republished as the Windows x64 self-contained single-file `SOS_Project.exe`. The game and endings were not replayed for this build.

## Constraints

- Scenario 0 has been built and both endings observed locally. Attribute checks remain a future system feature because scenario 0 uses direct options throughout.
- Official Haruhi text and assets are copyrighted. Module prose has to be original.
- The first scenario and Windows exe publish target are implemented and locally validated. The send-back self-deletion was checked on a disposable published copy, leaving the primary publish output available. No automated test suite has been added.
- The character-by-character text and W/S menus have passed build and publish, but no playthrough yet. The local published exe now includes this change.

## Open questions

Details: `Docs/GAME_DESIGN.md`.

- Which attributes exist, how the player gets those values, and how a check is resolved.
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted.
