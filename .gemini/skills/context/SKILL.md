---
name: context
description: |
  Load full context about the user's life, work, and current state from the Obsidian vault.
  Reads context files, recent daily notes, project files, and follows backlinks to build
  a complete picture. Use when user says "load context", "context", "catch me up",
  "what are we working on", or at the start of a complex work session.
allowed-tools: Read, Glob, Grep
---

# Context Loader

Preload all relevant context from the Obsidian vault in one shot.

## Process

1. Read `~/Vault/INDEX.md` for the vault overview

2. Read the most recent 3 daily notes from `~/Vault/daily/` (sorted by date)

3. Read all active project files from `~/Vault/projects/` (where status is "active")

4. Read `~/Vault/references/gemini-cli-preferences.md` for behavioral preferences

5. Scan `~/Vault/inbox/` for any unprocessed items

6. Present a brief summary to the user:
   - What you're currently working on (from projects)
   - Recent progress (from daily notes)
   - Pending items (from inbox)
   - Key preferences loaded

7. Do NOT output the full contents of files — just summarize what context has been loaded and what's relevant.

This is a read-only operation. Do not modify any files.
