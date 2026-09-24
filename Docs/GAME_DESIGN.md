# Game Design Contract

Status: partially implemented. Scenario 0 is authored in Markdown; its opening slice is being connected to a C# console program. English is canonical.

## Product

SOS_Project is a single-player text game presented as a console session. The player reads narration and picks a numbered option. Each story is a scenario module shaped like a Call of Cthulhu tabletop module. The fiction uses the world of *The Melancholy of Haruhi Suzumiya* (涼宮ハルヒの憂鬱). Play is deduction and puzzle-solving.

This is an unofficial fan project. Do not copy novel text, anime scripts, lyrics, or official assets.

## Decisions

- The runtime is a C# console program on .NET 10 (`net10.0`), which is the active LTS release through 2028-11-14. Text and pictures are printed with `Console.Write` / `Console.WriteLine`. The ship target is a Windows x64 self-contained single-file console exe, so a player does not install .NET. The user has asked to begin implementation; `Game/SOS_Project.csproj` is the C# project. This repository is not a Unity project. Do not add Unity files.
- The usual frame is prose. A scene may also show one picture made of `■` and console colors. Pictures are occasional. They do not replace the read-aloud.
- The program is the Keeper. There is one player. The player character is the player themself, not a canon member, and does not receive an invented name. The first module uses first-person Chinese narration and options; the earlier second-person direction is superseded for that module.
- A scene shows a numbered list. The player selects one option.
- An option that solves or concludes a puzzle lists the clue ids it requires, and it is offered only after those clues are found. Other options may be offered without clues. Every selected option changes the situation.
- Some beats show their plot options immediately. On other beats, an attribute check decides which of the current plot options are displayed. The options stay on that beat. The check only chooses the visible ones.
- On a check beat, the player chooses which attribute to check. Success and failure each name a subset of that beat's options. The player then picks one displayed option. There is no skill list. The attribute names, the player's values, and the roll or target procedure are still open. Superseded the same day: a check beat has no option list, and a check jumps straight to a branch.
- "CoC-like" means the module shape in this file. It does not mean using Chaosium's rulebook, Sanity, or Mythos statistics.
- The scenario source of truth is Markdown with the headings below. The first runtime slice uses `Scenarios/ZeroFloor.Play.cs` as explicit, compiled story data derived from that Markdown; it does not parse keeper notes at runtime.

## Module shape

Every scenario uses these sections, in this order. Leave an unused section in place and write `None.` under it.

1. **Header** — title, one-line pitch, estimated play time, player-character assumption (the player themself), tone note.
2. **Keeper brief** — what is actually happening. Player text must not include this.
3. **Timeline** — facts already true when play starts, in order.
4. **Hook** — the player-facing reason the situation starts.
5. **People** — one subsection per character.
6. **Places** — one subsection per location.
7. **Clues** — one subsection per clue.
8. **Scenes** — playable beats. Entry can depend on a place, a clue, or a clock.
9. **Options** — the plot choices that belong to a beat.
10. **Checks** — optional. The player chooses which attribute to test. The result decides which of the current options are displayed.
11. **Outcomes** — endings or major turns. Each names the condition that selects it.
12. **Handouts** — text the player can read again, such as a flyer, note, or article.

### Person

- Name and relationship to the situation
- What they want
- What they know (clue or timeline ids)
- What they will say in public
- What they will not volunteer (keeper-only)

### Place

- First impression (player)
- Keeper notes
- Who is here
- Which clues can be found here
- Where the player can go next

### Clue

- Player-facing summary, written as it appears when found
- Where it is found
- Which option reveals it, when a choice is the reveal
- What it points to
- Keeper meaning
- If the player chooses an attribute here: the check id

A clue counts only when it has an id and a reveal condition. A hint buried in prose is not a clue. A direct option may reveal it. A check beat that reveals it also names a check.

### Scene

- Entry condition
- Read-aloud
- Optional picture note (what the `■` picture shows, or `None.`)
- Keeper notes
- The plot options on this beat, and where each goes
- Display: `direct options` or `attribute check`
- If direct: show that list. No check.
- If a check: the check id. The check decides which of these options are displayed.

### Option

- Text the player sees
- Clue ids required before it appears, or none
- Where it leads
- What it changes

An offered option, once selected, changes the situation. A conclusion stays off the list until its required clues are found.

### Check

- Which beat offers it
- Attributes the player may choose
- For each of those attributes: which of the beat's current options are displayed on success, and which are displayed on failure

The roll, target number, and full attribute list are not set. Each result names options that already belong to the beat. Options left off that result stay hidden.

### Outcome

- Condition
- Read-aloud
- What remains true afterward

## Console loop (target)

1. Show the hook, or the current scene's read-aloud.
2. If this beat has a picture, print it with `■` and console colors. Skip the picture when the scene has none.
3. If this beat says `direct options`, show its numbered plot options.
4. If this beat says `attribute check`, show the attribute choices. The player picks one attribute. Resolve the check, then show only the current plot options that result displays.
5. The player selects one plot option.
6. Resolve it into narration plus a state change: a clue, a new scene, a changed relationship, or an outcome.
7. Let the player re-read handouts and clues already found.
8. Stop when an outcome is reached.

### First runtime slice

`Game/Program.cs`, `Game/Story.cs`, and `Game/StoryRunner.cs` provide the console entry point, story data types, and runner. The runner advances scenes through numbered options, applies clue and flag conditions and effects, lets the player re-read discovered clues and handouts, and prints an optional colored `■` picture. `Scenarios/ZeroFloor.Play.cs` is compiled into the program and currently supplies the Hook, S00–S05, K01–K03, and an initial H01. At S05, the player can use `0` to re-read the handout before either numbered option ends the preview. Player output contains no keeper-only notes.

The rest of scenario 0, attribute-check rules, saves, and the ending's exe/save deletion are not implemented. No build, test, or publish has been run for this slice.

## Fiction boundaries

These are available as setting. A future scenario is not official canon.

- North High, the SOS Brigade club room, and the town around the school
- Haruhi Suzumiya, Kyon, Yuki Nagato, Mikuru Asahina, Itsuki Koizumi
- Phenomena already native to that world, including closed space, and facts the club's non-ordinary members already understand

The player plays themself. The first module uses first-person narration. Do not cast the player as a canon character or invent a name or personal biography for them.

Every scenario is a deduction puzzle: the player gathers clues and then chooses a conclusion that those clues unlock. The header tone note states the prose's balance of comedy and investigative pressure. For the first module, lively comedy leads and the tone turns serious near the truth.

Canon characters, when present, speak in original lines written for the module.

The first module is `Scenarios/00-zero-floor.md`, set in an unnamed fictional Chinese mountain city inspired by Chongqing's terrain without real place names. An abnormal Endless Eight branch brings the SOS Brigade to 2026, then repeatedly across 2009–2026. Time travel, otherworldly space, and an AI connected to alien technology / the Information Integration Thought Entity lead toward the player's origin in a worldline created by Haruhi. Comedy dominates until the investigation nears the truth. The selected route mystery includes cross-era changes in people's relationships and an AI observation puzzle. It follows the eight-stage story circle around the player's identity, origin, and destination, returning to the opening corridor for the final choice. The endings return the Brigade and close the branch, deleting this game's local exe and saves, or remain in the apparently real created world. Deletion is a target ending behavior, not implemented functionality.

The player has watched the Haruhi anime and knows Haruhi may shape worlds. Build the three questions around the player's own identity, origin, and chosen destination. Treat that anime knowledge as evidence to test and a possible false assumption, rather than saving Haruhi's ability as the twist. Do not assign the player a fabricated personal history.

## Authoring rules

- Do not put player-facing sentences and keeper-only sentences in the same paragraph.
- Write original sentences. Do not transcribe published fiction, scripts, or dialogue.
- Do not add `Scenarios/` until a module is actually being written.
- Do not put a puzzle's concluding option on the list before its clue ids are found.
- Seed hints in natural scene prose and dialogue. Track discoverable clues with keeper-facing ids and reveal conditions; the player should be able to infer the final answer from evidence across eras before any character explains it.
- Each beat lists its plot options. Mark the display `direct options` or `attribute check`. A direct beat shows the whole list and has no check. A check beat lists the attributes the player may choose. For each attribute, success and failure each name which of those current options are displayed.

## Out of scope

- Save format
- A skill list, Sanity, or Chaosium's character sheet
- Multiplayer, or a screen for a human Keeper

## Open questions

These remain open for future system design. The first authored module uses direct options only, so attribute rules do not block its prose.

- Which attributes exist, how the player gets those values, and how a check is resolved (die and target, or another comparison).
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted.
