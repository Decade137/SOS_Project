# Game Design Contract

Status: target. No scenario prose and no C# project exist yet. English is canonical.

## Product

SOS_Project is a single-player text game presented as a console session. The player reads narration and picks a numbered option. Each story is a scenario module shaped like a Call of Cthulhu tabletop module. The fiction uses the world of *The Melancholy of Haruhi Suzumiya* (涼宮ハルヒの憂鬱). Play is deduction and puzzle-solving.

This is an unofficial fan project. Do not copy novel text, anime scripts, lyrics, or official assets.

## Decisions

- The runtime is a C# console program. Text and pictures are printed with `Console.Write` / `Console.WriteLine`. This repository is not a Unity project. Do not add Unity files. Do not create the C# project until the user asks to implement.
- The usual frame is prose. A scene may also show one picture made of `■` and console colors. Pictures are occasional. They do not replace the read-aloud.
- The program is the Keeper. There is one player. The player character is the player themself, addressed in second person. The player is not a canon member and does not receive an invented name.
- A scene shows a numbered list. The player selects one option. There are no dice and no skill list.
- An option that solves or concludes a puzzle lists the clue ids it requires, and it is offered only after those clues are found. Other options may be offered without clues. Every selected option changes the situation.
- "CoC-like" means the module shape in this file. It does not mean using Chaosium's rulebook, Sanity, or Mythos statistics.
- The scenario source of truth is Markdown with the headings below. An engine data format waits until implementation starts.

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
9. **Options** — numbered choices shown in a scene. No die roll.
10. **Outcomes** — endings or major turns. Each names the condition that selects it.
11. **Handouts** — text the player can read again, such as a flyer, note, or article.

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

A clue counts only when it has an id and a reveal condition. A hint buried in prose is not a clue.

### Scene

- Entry condition
- Read-aloud
- Optional picture note (what the `■` picture shows, or `None.`)
- Keeper notes
- Options offered
- Where each option goes

### Option

- Text the player sees
- Clue ids required before it appears, or none
- Where it leads
- What it changes

An offered option, once selected, changes the situation. A conclusion stays off the list until its required clues are found.

### Outcome

- Condition
- Read-aloud
- What remains true afterward

## Console loop (target)

1. Show the hook, or the current scene's read-aloud.
2. If this beat has a picture, print it with `■` and console colors. Skip the picture when the scene has none.
3. Show the numbered options.
4. The player selects one option.
5. Resolve it into narration plus a state change: a clue, a new scene, a changed relationship, or an outcome.
6. Let the player re-read handouts and clues already found.
7. Stop when an outcome is reached.

## Fiction boundaries

These are available as setting. A future scenario is not official canon.

- North High, the SOS Brigade club room, and the town around the school
- Haruhi Suzumiya, Kyon, Yuki Nagato, Mikuru Asahina, Itsuki Koizumi
- Phenomena already native to that world, including closed space, and facts the club's non-ordinary members already understand

The player plays themself. Address them in second person. Do not cast them as a canon character, and do not invent a name for them.

Every scenario is a deduction puzzle: the player gathers clues and then chooses a conclusion that those clues unlock. The header tone note still says whether the prose leans toward the series' comedy or toward investigative pressure. That note is chosen with the plot.

Canon characters, when present, speak in original lines written for the module.

## Authoring rules

- Do not put player-facing sentences and keeper-only sentences in the same paragraph.
- Write original sentences. Do not transcribe published fiction, scripts, or dialogue.
- Do not add `Scenarios/` until a module is actually being written.
- Do not put a puzzle's concluding option on the list before its clue ids are found.

## Out of scope

- Save format
- Character-sheet mathematics and dice
- Multiplayer, or a screen for a human Keeper
- The plot of the first scenario

## Open questions

These block the first scenario outline (`Docs/TODO.md` DES-003). The runtime choice does not.

- First situation: the user is still deciding which incident the first module investigates.
- Tone note for that module (comedy or investigative pressure), chosen with the plot.
- Player-facing language. The design conversation is in Chinese.
- Whether any trackable resource exists (stress, weirdness, reputation). Sanity is not adopted. Dice are not used.
