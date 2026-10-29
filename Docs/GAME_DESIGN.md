# Game Design Contract

Status: scenario 0 plays in a Ren'Py 8.5.3 window. The 2026-09-30 story is the current module. `pack.bat` builds `Build/SOS_Project/SOS_Project.exe`. English is canonical.

## Product

SOS_Project is a single-player text game in a window. The player reads narration, moves through bullet-marked options with W/S or the arrow keys, and confirms with Enter or a click. Each story is a scenario module shaped like a Call of Cthulhu tabletop module. The fiction uses the world of *The Melancholy of Haruhi Suzumiya* (涼宮ハルヒの憂鬱). Play is deduction and puzzle-solving.

This is an unofficial fan project. Do not copy novel text, anime scripts, lyrics, or official assets.

## Decisions

- The runtime is Ren'Py 8.5.3. The project is `Play/`. Text is drawn in a dark window. `pack.bat` downloads the Ren'Py SDK when it is missing and builds a Windows x64 game folder; the player runs `Build/SOS_Project/SOS_Project.exe` and does not install Ren'Py. This repository is not a Unity project. Do not add Unity files, and do not move the playable game back to a C# console.
- The usual frame is prose. A scene may also show one picture made of colored squares in the `■` pattern. Pictures are occasional. They do not replace the read-aloud.
- The program is the Keeper. There is one player. The player character is the player themself, not a canon member, and does not receive an invented name. The first module uses first-person Chinese narration and options; the earlier second-person direction is superseded for that module.
- Player-facing story text is revealed character by character before the options appear. Any key or click completes the current text block immediately; re-reading found material is immediate. The start screen offers New Game, Load Save, and Exit; Load Save is disabled without a valid save. Scene, action feedback, journal, and ending each replace the page. Text sits in one centered column on a blue-black page, and story prose uses a serif face. Dialogue is cyan and narration is warm off-white. Each ending page has its own background tint. The page scrolls with the mouse wheel. A continue prompt follows the body, and leftover space stays below that prompt. All visible menu choices start with `·`; W/S or the arrow keys turn the full selected choice cyan, and Enter confirms. A click also confirms a choice.
- An option that solves or concludes a puzzle lists the clue ids it requires, and it is offered only after those clues are found. Other options may be offered without clues. Every selected option changes the situation.
- Some beats show their plot options immediately. On other beats, an attribute check decides which of the current plot options are displayed. The options stay on that beat. The check only chooses the visible ones.
- On a check beat, the player chooses which attribute to check. Success and failure each name a subset of that beat's options. The player then picks one displayed option. There is no skill list. The attribute names, the player's values, and the roll or target procedure are still open. Superseded the same day: a check beat has no option list, and a check jumps straight to a branch.
- "CoC-like" means the module shape in this file. It does not mean using Chaosium's rulebook, Sanity, or Mythos statistics.
- The scenario source of truth is Markdown with the headings below. The runtime uses `Play/game/story_data.py` as explicit player-facing story data derived from it; it does not parse keeper notes at runtime.
- The first playable release contains the complete scenario 0 with direct options. Attribute checks and trackable resources remain future system questions because this module uses neither.
- One local save slot lives at `%LOCALAPPDATA%/SOS_Project/save.json`, format version 4. The program saves after each plot choice except final confirmation of the send-back ending: the preceding confirmation-page save stays available until cleanup, so an interrupted ending can be confirmed again. At startup, the separate screen offers new game, load save, or exit; a new game replaces that slot, and load save is disabled when unavailable. The versioned save stores the current scene, discovered material, flags, text choices, and any completed stay outcome. Older `save.bin` files are not read.
- The send-back ending requires the module's two explicit confirmations. Those confirmations are in-story: the player sends the five back, knowing this August closes with them inside. Player-facing narration, choices, handouts, and ending pages do not name the save, Windows, or the executable. After the ending text is shown, the program deletes this game's save and does not open a report page. On the packed Windows build, a narrowly scoped helper then attempts to delete only `SOS_Project.exe` in that build's folder after exit, after a SHA-256 check. It must never target another file. If that step cannot be arranged, the game still ends without asking the player to delete a file. SDK runs and non-Windows runs delete only the save. The stay ending and the reset ending keep both.

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

## Play loop

1. Reveal the hook or current scene's read-aloud character by character. Let a key press or click finish the current text block.
2. If this beat has a picture, show it as colored squares. Skip the picture when the scene has none.
3. After the text finishes, if this beat says `direct options`, show its bullet-marked plot options.
4. If this beat says `attribute check`, show the attribute choices. The player picks one attribute. Resolve the check, then show only the current plot options that result displays.
5. The player moves through the displayed options with W/S or the arrow keys and confirms one with Enter or a click.
6. Resolve it into narration plus a state change: a clue, a new scene, a changed relationship, or an outcome.
7. Let the player re-read handouts and clues already found.
8. Stop when an outcome is reached.

### Scenario 0 runtime

`Play/game/script.rpy` starts the game. `Play/game/story_data.py` holds the Hook, the scene chain, K01–K13, H01–H06 (plus H01_REVISED), and E01–E03. Longer player prose is imported from `story_prose.py`, `story_long.py`, `story_more2.py`, and `story_more3.py`. `Play/game/engine.rpy` reveals story text, advances choices, applies clue and flag conditions and effects, saves one JSON slot, re-reads found material, and after E01 deletes the save and asks Windows to delete only the packed `SOS_Project.exe`, without showing that step. `Play/game/screens.rpy` draws the page. Player output contains no keeper-only notes. Only E01 may request file cleanup; E02 and E03 keep the save and exe.

The first module uses direct options only. No automated test suite is run. Pack from the repository root with `pack.bat`.

## Fiction boundaries

These are available as setting. A future scenario is not official canon.

- North High, the SOS Brigade club room, and the town around the school
- Haruhi Suzumiya, Kyon, Yuki Nagato, Mikuru Asahina, Itsuki Koizumi
- Phenomena already native to that world, including closed space, and facts the club's non-ordinary members already understand

The player plays themself. The first module uses first-person narration. Do not cast the player as a canon character or invent a name or personal biography for them.

Before a brigade member introduces themself to the player, player-facing scene text and choice feedback identify that person through visible features and actions rather than a name. Names may be used after the introductions.

Nagato, Mikuru, and Koizumi never reveal their identities or discuss anomalies in front of Haruhi; Kyon keeps the same silence. Write from what each character knows: the brigade does not know the player already knows them. Until the player makes that known, members investigate the player covertly and report to one another (in scenario 0, to Kyon) out of Haruhi's hearing. They do not explain their powers to the player. The player learns their findings by overhearing, not because a member volunteers them. Player options must not raise insider topics in front of Haruhi.

Every scenario is a deduction puzzle: the player gathers clues and then chooses a conclusion that those clues unlock. The header tone note states the prose's balance of comedy and investigative pressure. For the first module, lively comedy leads and the tone turns serious near the truth.

Canon characters, when present, speak in original lines written for the module.

The first module is `Scenarios/00-zero-floor.md`, titled “凉宫春日的心愿” (The Wish of Haruhi Suzumiya); the in-story exam is still called “异世界人入团考试”, and the file name is historical. It takes place on 2009-08-31, from 15:17 to midnight, inside one branch of the Endless Eight loop, in the brigade's unnamed town. The player steps out of the club room's metal cabinet. Haruhi declares them the “otherworlder” her brigade lacked and runs a comic three-stage entrance exam. Behind each stage, Nagato, Mikuru, and Koizumi covertly rule out alien, time traveler, and esper and report to Kyon; the player overhears each report. After Haruhi leaves at S08, Kyon starts to tell the player, and the player reveals they already know who the members are. Clues then show the branch writing the player in: Haruhi's Aug 20 notebook list matching the player's belongings, a new line appearing in that notebook, Kyon's déjà vu of a phrase the player just chose, and the player's own memory of an armband Haruhi made that evening. Nagato's unrewritable record is the independent control. The player deduces that Haruhi's wish produced them, including their memory of coming from another world. Haruhi never learns the truth. Comedy dominates until the notebook changes. The story follows the eight-stage circle, returning to the cabinet for the final choice. There are three endings. Choices now change how the brigade treats the player: the opening answer, the calendar reply, which member the player follows, the on-site fork, the 20:10 sentence, the goldfish stall, and whether the missing calendar marks are shown to Haruhi. Send-back writes Mikuru, Kyon, and Koizumi's farewells separately. The player attends one exam site and hears the other two while Haruhi is out buying juice. Clues K01–K09 still arrive before the deduction at S12C. K11 is the sixth cup, K12 the empty drawer, and K13 the 15:16 photo from inside the cabinet. Wrong conclusions can be tried once and are answered with those clues; they do not lock the route. Different choices recover different planted details: who poured the cup, whether the station name matches the ticket, the empty chair, the red thread in the drawer, and whether Kyon says “不许弄丢” before the armband exists. A shortest pass is about 39,000 characters across 34 choices, written to be about two hours of careful reading. That count was not timed in a window. Reports the player did not overhear in person are given at the juice-run debrief, not first dumped at S08. E01 sends the five back and closes the branch. Player-facing text does not say that files will be removed; scoped cleanup still runs after the ending text, with no report page. E02 stays into a real September while the five vanish from their original line. E03 makes no choice, and the summer resets to Aug 17 with the player inside.

The player is assumed to know the Haruhi story and the SOS Brigade, including that Haruhi may shape worlds. Player-facing narration and choices should not explain where that familiarity came from; show it through character reactions, lived details, time traces, and gaps in the records. Build the three questions around the player's own identity, origin, and chosen destination. Treat that prior knowledge as evidence to test and a possible false assumption, rather than saving Haruhi's ability as the twist. Do not assign the player a fabricated personal history.

## Authoring rules

- Do not put player-facing sentences and keeper-only sentences in the same paragraph.
- Write original sentences. Do not transcribe published fiction, scripts, or dialogue.
- Do not add `Scenarios/` until a module is actually being written.
- Do not put a puzzle's concluding option on the list before its clue ids are found.
- Seed hints in natural scene prose and dialogue. Track discoverable clues with keeper-facing ids and reveal conditions; the player should be able to infer the final answer from evidence across eras before any character explains it.
- Each beat lists its plot options. Mark the display `direct options` or `attribute check`. A direct beat shows the whole list and has no check. A check beat lists the attributes the player may choose. For each attribute, success and failure each name which of those current options are displayed.

## Out of scope

- A skill list, Sanity, or Chaosium's character sheet
- Multiplayer, or a screen for a human Keeper

## Open questions

These remain open for future system design. The first authored module uses direct options only, so attribute rules do not block its prose.

- Which attributes exist, how the player gets those values, and how a check is resolved (die and target, or another comparison).
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted.
