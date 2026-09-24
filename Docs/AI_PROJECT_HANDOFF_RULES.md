# AI Project Handoff Rules (Portable)

Copy this file into any new project, then create the files listed under **Bootstrap**. Point the agent at `AGENTS.md` (and this doc if needed). English files are canonical; Chinese mirrors are optional but must stay fact-aligned when used.

## Why this exists

Chat context resets. Git diffs do not record *decisions*, *preferences*, or *ownership maps*. This handoff system is a small, tool-neutral memory layer so the next AI session (or developer) can:

1. Read constraints before editing.
2. Avoid re-deciding settled product/tech choices.
3. Find the right files without a full codebase tour.
4. Leave a short trail of what changed and what was *not* validated.

It is documentation for agents, not a second product backlog tool.

## File map (what / why)

| File | Role | Update when |
|------|------|-------------|
| `AGENTS.md` (repo root) | Always-on policy: hard rules, style, ownership, session routine | Rarely; only when workflow policy changes |
| `Docs/MEMORY.md` | Durable facts: stack versions, user preferences, product decisions, known constraints, open mismatches | New durable fact or decision; rewrite/update in place |
| `Docs/PROCESS.md` | Workflow rules + concise dated session log | Every work session (one short entry) |
| `Docs/STRUCTURE.md` | Directory map + feature → file index | Code, ownership, or navigation-relevant paths change |
| `Docs/TODO.md` | Prioritized backlog with status | Scope/priority changes; optional per session |
| `Docs/LOGS/YYYY-MM-DD-topic.md` | Optional deep session write-up | Only substantial investigations / multi-day threads |
| `Docs/*_DESIGN.md` / plans | Feature contracts and phased plans | Designing or implementing that feature |
| `Docs/Reports/` | Generated audits, measurements, one-off evidence | After producing evidence artifacts |
| `*.zh-CN.md` mirrors | Same facts in Chinese for human reading | Same session as English when mirrors exist |

### What belongs where (critical)

- **MEMORY** = still true tomorrow without knowing *who did what today*. Examples: “WebGL, no `Task.Delay`”, “vendor folder X is read-only”, “portrait is target but landscape is current”.
- **PROCESS** = *how* we work + *what happened this session* (outcome, verification, unvalidated items). Not a design dump.
- **STRUCTURE** = *where* things live. Paths and ownership, not play-by-play history.
- **TODO** = *what remains*. Status + done-when, not session diary.
- **LOGS** = long form when one PROCESS line is not enough. Do not duplicate full LOGS text into MEMORY.

### Anti-patterns (learned the hard way)

- Do **not** turn MEMORY into a reverse-chronological dump of every session. That causes huge merge conflicts and buries durable facts.
- Do **not** paste the same paragraph into MEMORY, PROCESS, and STRUCTURE. One home per fact.
- Do **not** run engines, editors, tests, or builds just because the docs mention a target that differs from the current project state—unless the user asks.
- Do **not** “clean” generated/serialized assets as part of a docs session.

## Recommended session workflow

```text
Start:
  AGENTS.md
    → Docs/MEMORY.md
    → Docs/PROCESS.md   (workflow + recent entries)
    → Docs/STRUCTURE.md
    → relevant feature docs / LOGS if the task needs them
  git status (preserve unrelated dirty files)

Work:
  smallest useful change inside ownership boundaries
  static checks by default

End:
  update MEMORY only if a durable fact/decision changed
  always append one short PROCESS entry (+ zh-CN if mirrors exist)
  update STRUCTURE if paths/ownership/navigation changed
  optional LOGS pair for large investigations
  report: changed files, verification done, anything not validated
```

### PROCESS entry shape (keep short)

```text
- YYYY-MM-DD: <outcome in one or two sentences>. Verification: <static checks / none>. Not run: <Unity/tests/builds/device as applicable>.
```

### MEMORY entry shape (durable only)

Prefer stable sections over endless dated bullets:

```markdown
## Stack
## Product targets vs current state
## User preferences
## Decisions (keep; mark superseded clearly)
## Known constraints / risks
## Open questions
```

Dated bullets are fine for *new durable facts*, not for routine “fixed bug X today” logs (those go to PROCESS).

## Bootstrap for a new project

Create at least:

```text
AGENTS.md
Docs/MEMORY.md
Docs/PROCESS.md
Docs/STRUCTURE.md
Docs/TODO.md
Docs/LOGS/.gitkeep
```

Optional but useful:

```text
Docs/MEMORY.zh-CN.md
Docs/PROCESS.zh-CN.md
Docs/STRUCTURE.zh-CN.md
Docs/TODO.zh-CN.md
```

Then fill templates below with *this* project's facts. Delete Unity/WebGL-specific rules if the stack differs; keep the handoff *shape*.

---

## Template: `AGENTS.md`

```markdown
# AGENTS.md

<one-sentence product/tech target>. Keep every change small, explicit, and easy for the next AI or developer to inspect.

## Hard Rules

- Prefer the smallest working change. Avoid speculative abstractions.
- Do not use reflection unless the user explicitly asks.
- <platform constraints, e.g. WebGL: no Task.Delay for gameplay timing; no thread/Compute/async GPU assumptions>
- Do not run the IDE/engine, automated tests, or a dev server unless the user explicitly asks.
- Do not invoke skills unless the user explicitly asks for that skill.
- Preserve existing user changes in a dirty worktree. Never revert unrelated files.
- Every work session must update Docs/MEMORY.md (if durable facts changed) and Docs/PROCESS.md (+ Chinese mirrors if present).
- After code, ownership, or feature-file changes, update Docs/STRUCTURE.md (+ mirror if present).
- Do not change production settings merely because docs describe a future target.

## Product Direction

- <targets>
- <current vs target mismatches, if any>

## Code Style

- Prefer small compositional units with one responsibility.
- Cache hot-path references; avoid repeated searches/allocations.
- Prefer project-owned code over editing vendor trees.
- Patch vendor code only when public APIs are insufficient; record the reason in MEMORY.

## Ownership

- <vendor / generated / project-owned paths>

## Documentation Routine

- Docs/MEMORY.md: durable facts, preferences, decisions, constraints
- Docs/PROCESS.md: workflow rules + concise dated session history
- Docs/STRUCTURE.md: directory map and feature-to-file index
- Docs/TODO.md: prioritized backlog
- Docs/LOGS/: optional deep session notes (YYYY-MM-DD-topic.md)
- English core docs are canonical; Chinese mirrors must match facts in the same session

## Default Workflow

1. Read AGENTS.md, MEMORY, PROCESS, STRUCTURE, and relevant feature docs.
2. Inspect git status; preserve unrelated changes.
3. Make the smallest useful change within ownership boundaries.
4. Static checks by default; heavy verification only when asked.
5. Update docs as required above.
6. Report changed files, verification performed, and anything not validated.
```

---

## Template: `Docs/MEMORY.md`

```markdown
# Memory

## Stack
- <engine/framework/language versions>

## Product
- Target: <...>
- Current implementation: <...>

## User preferences
- Keep logs concise unless expansion is requested.
- <other preferences>

## Decisions
- <decision>: <rationale / date if useful>

## Constraints
- <hard technical or platform limits>

## Open questions
- <unresolved product/tech choices>
```

---

## Template: `Docs/PROCESS.md`

```markdown
# Process

## Workflow rules
- Pre-edit reading order: AGENTS.md → MEMORY → PROCESS → STRUCTURE → feature docs.
- Prefer static verification; do not start heavy tooling without explicit ask.
- One concise dated session entry per work session.
- Create Docs/LOGS/YYYY-MM-DD-topic.md (+ .zh-CN.md) only when a short PROCESS line is insufficient.
- Do not reorder historical session entries.
- English is canonical when mirrors disagree; fix mirrors in the same session.

## Session history
- YYYY-MM-DD: Initialized AI handoff documentation. Static file checks only; no engine/tests run.
```

---

## Template: `Docs/STRUCTURE.md`

```markdown
# Structure

## Root map
- `AGENTS.md`: AI policy
- `Docs/`: handoff, plans, reports
- `<src>/`: project-owned code
- `<vendor>/`: imported; prefer not to extend here

## Feature → files
- <Feature>: `<path>`, `<path>`

## Documentation index
- `Docs/MEMORY.md`, `PROCESS.md`, `STRUCTURE.md`, `TODO.md`
- `Docs/LOGS/`: deep session notes
- `Docs/Reports/`: generated evidence (optional)
```

---

## Template: `Docs/TODO.md`

```markdown
# Backlog

Status legend: `Not started`, `Blocked by product choice`, `Ready for design`, `Ready for implementation`, `Implemented; validation pending`.

## P0
### ID-001 Title
- Status:
- Dependencies:
- Current files:
- Work:
- Done when:
```

---

## Template: deep log `Docs/LOGS/YYYY-MM-DD-topic.md`

```markdown
# Session: <Topic>

- Scope:
- Outcome:
- Evidence / key paths:
- Verification:
- Not validated:
- Follow-ups:
```

---

## Conflict and failure handling

- If English and Chinese disagree, English + `AGENTS.md` win until mirrors are fixed in-session.
- If a fact is unverified, label it as target / open question, not current behavior.
- If a task needs broad generated-file rewrites, stop and get explicit approval.
- If verification needs the engine/tests/device, do not run them without ask; state the limitation.

## Minimal vs full

| Project size | Use |
|--------------|-----|
| Tiny script / one-off | `AGENTS.md` + short `MEMORY` + `PROCESS` only |
| Normal app/game | Full set above |
| Multi-contributor / long-lived | Full set + LOGS for large threads + bilingual mirrors if the team needs them |

## How to hand this to the next project

1. Copy `Docs/templates/AI_PROJECT_HANDOFF_RULES.md` (this file) into the new repo (e.g. `Docs/AI_PROJECT_HANDOFF_RULES.md`).
2. Create files from **Bootstrap** using the templates.
3. Replace placeholders with real stack/product/ownership facts.
4. Tell the agent: “Follow `AGENTS.md` and the Docs handoff routine.”
5. Optionally add a Cursor project rule or user rule that says: always read `AGENTS.md` and update MEMORY/PROCESS/STRUCTURE per that file.
