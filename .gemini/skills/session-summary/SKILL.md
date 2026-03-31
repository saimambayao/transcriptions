---
name: session-summary
description: |
  End-of-session processing that captures what was accomplished, decisions made, and next steps
  into a daily note in the Obsidian vault. Use when the user says "session summary", "close day",
  "wrap up", "what did we do", "save progress", or at the end of any significant work session.
  Also trigger when the user is about to end a session or says goodbye.
allowed-tools: Read, Glob, Grep, Write
---

# Session Summary

Capture the current session's progress into an Obsidian vault daily note.

## Process

1. Review the current conversation to identify:
   - What was built, fixed, or changed
   - Key decisions made and their rationale
   - Tools, skills, or commands used
   - Problems encountered and how they were resolved
   - Open questions or unfinished work

2. Write a daily note to `~/Vault/daily/YYMMDD.md`. If the file already exists, append to it under a new session header.

3. Use this format for **new daily notes**:

```markdown
---
date: YYYY-MM-DD
tags: [daily, session]
---

# Daily Note — YYYY-MM-DD

## Highlights

**[N] sessions** — [one-line description of the day's theme]

**Key deliverables:**
- [3-7 most important things built/fixed/created]

**Pending:**
- [ ] [Actionable task with enough context to resume without re-reading the session]
- [ ] [Another pending task]

---

## Session: HH:MM — [brief description]

**What was accomplished:**
- [bullet points of completed work]

**Decisions made:**
- [key decisions with brief rationale]

**Next steps:**
- [what to pick up next session]

**Related notes:**
- [[link to relevant vault notes]]
```

4. **If the daily note already exists** (appending a new session):
   - Append the new session section at the bottom
   - **Update the Highlights** at the top to reflect ALL sessions so far:
     - Increment session count
     - Add any major new deliverables to the key deliverables list
     - Update the Pending line with current status

5. Update `~/Vault/INDEX.md` if significant new notes were created during the session.

6. Keep session sections concise — the Highlights is the quick-read, individual sessions are the detail.

7. **Always include a Pickup Guide** at the very end of the daily note. This is the "where we left off" section that makes it possible to resume work without re-reading the entire session. Update it every time a new session is appended.

```markdown
---

## Pickup Guide — Where We Left Off (YYYY-MM-DD)

Use this section to resume work in the next session. Say the command to pick up any task.

### [Primary Track Name] (e.g., Guidebook Series, Feature Development)
| Command | What it does |
|---|---|
| **"[exact phrase to say]"** | [What it triggers] |
| Plan file: `[path]` | [Description] |

### Quick Tasks
- [ ] [Task with enough context to execute without asking questions]
- [ ] [Another quick task]

### Key File Locations
- [Category]: `[path]`
```

**Pickup Guide rules:**
- Every pending task must be a checkbox (`- [ ]`) so progress is visible
- Commands should be exact phrases the user can paste to resume
- Include file paths so the next session can find everything immediately
- Update the Pickup Guide when appending new sessions — remove completed items, add new ones
- The Pickup Guide replaces vague "next steps" — it must be actionable and self-contained
