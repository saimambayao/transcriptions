---
name: vault-update
description: |
  Review the Obsidian vault and generate a recommendation document for improving GEMINI.md files.
  Does NOT auto-edit any GEMINI.md — produces a review document for the user to apply manually.
  Use when user says "vault update", "review my vault", "improve claude md", "update conventions",
  "refine my setup", or wants to audit how Gemini CLI is configured based on recent usage patterns.
  Run this periodically (weekly or after heavy usage) to keep the system improving.
allowed-tools: Read, Glob, Grep, Write
---

# Vault Update

Generate a recommendation document for improving GEMINI.md files based on recent vault activity. This skill NEVER edits any GEMINI.md directly — it produces a review document for the user to evaluate and apply.

## Process

### 1. Read current configuration

Read these files to understand the current state:
- `~/.gemini/GEMINI.md` (global rules)
- `~/Vault/GEMINI.md` (vault conventions)
- `~/Vault/INDEX.md` (what's in the vault)

### 2. Scan recent vault activity

- List all files in `~/Vault/` modified in the last 7 days
- Read recent notes in `inbox/`, `research/`, `projects/`
- Look for patterns: recurring topics, new tags, new project areas, new tools mentioned

### 3. Analyze conversation patterns

From the current session and recent vault notes, identify:
- **Conventions that worked well** — things Gemini CLI did right
- **Conventions that are missing** — patterns that should be codified
- **Conventions that are outdated** — rules no longer relevant
- **New preferences** — things the user corrected or requested repeatedly
- **Vault structure gaps** — folders that might be needed, INDEX.md entries that are stale

### 4. Generate recommendation document

Save to `~/Vault/inbox/claude-md-review-YYMMDD.md` with this structure:

```markdown
---
date: YYYY-MM-DD
tags: [vault-update, claude-md, review]
---

# GEMINI.md Review — YYYY-MM-DD

## What's Working Well
- [conventions to keep, with evidence from recent usage]

## Suggested Additions
For each suggestion:
- **What:** the proposed addition
- **Why:** evidence from recent sessions/notes
- **Where:** which GEMINI.md file (global or vault)
- **Proposed text:**
  ```
  the exact line(s) to add
  ```

## Suggested Removals
- [outdated rules with reasoning]

## Vault Structure Suggestions
- [new folders, INDEX.md updates, stale notes to archive]

## INDEX.md Updates
- [new entries to add, stale entries to remove]
```

### 5. Present to the user

Show a brief summary of the recommendations and tell the user where the full document is saved. Do NOT apply any changes — the user decides what to keep.
