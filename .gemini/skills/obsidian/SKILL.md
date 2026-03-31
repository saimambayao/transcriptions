---
name: obsidian
description: Create, append, and manage notes in the user's Obsidian vault at ~/Vault/. Use this skill
  whenever the user says "obsidian", "vault note", "save to vault", "note to vault", "add to vault",
  "write to vault", "obsidian note", "save this to obsidian", "capture this", "quick note",
  or wants to save any knowledge, idea, or reference to their Obsidian vault. Also trigger when
  the user asks to update INDEX.md, link vault notes, or organize vault content. This is the
  go-to skill for all Obsidian vault write operations — use it even if the user just says
  "save this" or "remember this" in a context where vault storage makes sense.
  Do NOT trigger for: reading/loading vault context (use /context), session summaries (use /session-summary),
  surfacing patterns (use /emerge), or connecting topics (use /connect).
---

# Obsidian Vault Note Creator

Fast note creation for the user's Obsidian vault. No analysis, no research — just write the note.

## Vault Location

`~/Vault/`

## Vault Structure

| Directory | Purpose | When to use |
|-----------|---------|-------------|
| `inbox/` | Unsorted ideas, quick captures | Default for quick notes, fleeting thoughts, things to process later |
| `projects/` | Active and completed projects | Project plans, status updates, architecture notes |
| `research/` | Deep investigation outputs | Output from /deep-research, /notebooklm, Claude Cowork, investigation-driven workflows |
| `research/deep-research/` | Full research reports | Output from /research-pipeline |
| `knowledge-areas/{topic}/` | Condensed learning notes by subject | Video transcription summaries, learning content, organized by topic |
| `bangsamoro/bangsamoro-govt/` | Bangsamoro governance | Officials, parliament, executive branch, LGU coordination |
| `bangsamoro/bangsamoro-laws/` | Bangsamoro legislation | BAAs, bills, codes, legal analysis |
| `bangsamoro/bangsamoro-resolutions/` | Bangsamoro resolutions | Parliamentary resolutions, committee reports |
| `daily/` | Daily notes | Day-specific logs, what happened today |
| `references/` | Saved articles, preferences, configs | Stable reference material, how-to guides |
| `templates/` | Reusable note templates | Template files only — never write regular notes here |

If the user doesn't specify a directory, choose based on content:
- Ideas, thoughts, fleeting captures → `inbox/`
- Deep investigation, multi-source research → `research/`
- Video summaries, learning content → `knowledge-areas/{topic}/`
- Bangsamoro governance, officials, forums → `bangsamoro/bangsamoro-govt/`
- Bangsamoro legislation, BAAs → `bangsamoro/bangsamoro-laws/`
- Bangsamoro resolutions → `bangsamoro/bangsamoro-resolutions/`
- Project-related → `projects/`
- Reference material, stable docs → `references/`
- Today's log → `daily/`

For full routing rules, read `~/Vault/GEMINI.md` — it is the authoritative source for vault conventions.

## Note Format

Every note MUST have YAML frontmatter and use Obsidian conventions:

```markdown
---
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
source: (URL or description, if applicable)
---

# Note Title

Content here using **bold for emphasis** and [[double bracket links]] to related notes.

## Related Notes

- [[link-to-related-note]]
```

### Frontmatter Rules
- `date` — always today's date (YYYY-MM-DD format)
- `tags` — lowercase, descriptive, 2-5 tags. Use existing tag conventions from the vault
- `source` — URL, book title, video link, or omit if original thought
- Additional fields are fine when relevant (e.g., `status: active` for projects)

### Content Rules
- Use `[[double bracket links]]` to connect to existing vault notes — check INDEX.md for known notes
- Bold key terms with `**double asterisks**`
- Bullet points for lists, not paragraphs
- Keep notes concise — capture the signal, not the noise
- No emojis (use icons if needed, per user preference)

## Filename Convention

`YYMMDD-short-descriptive-slug.md`

Examples:
- `260323-fuel-crisis-barmm-response.md`
- `260323-react-19-migration-notes.md`
- `260323-lean-canvas-workshop-ideas.md`

For daily notes: `YYMMDD.md` (e.g., `260323.md`)
For project notes: descriptive name without date prefix (e.g., `e-bangsamoro.md`)

## Existing Templates

The vault has templates in `~/Vault/templates/`. Use them as structural guides:

**Research note** (`research-note.md`): Key ideas, how it applies to work, follow-up questions
**Daily note** (`daily-note.md`): Working on today, decisions made, ideas, follow-ups
**Project note** (`project-note.md`): Overview, goals, current status, key links

You don't need to copy templates verbatim — adapt the structure to fit the content. The templates
show the user's preferred section patterns.

## After Creating a Note

1. **Tell the user** the file path and a one-line summary
2. **Update INDEX.md** if the note is significant enough to be findable later:
   - Add to the appropriate section (Projects, Research, References, Recent Notes)
   - Keep Recent Notes to the 5 most recent — remove oldest if needed
   - Update the `updated` date in INDEX.md frontmatter
3. **Link from related notes** if obvious connections exist and the related note is already open or recently accessed — don't go hunting through the whole vault

## Quick Capture Mode

When the user says something brief like "save this to vault" or "note: [idea]", just write it
to `inbox/` with minimal structure. Don't over-engineer a quick capture — speed matters more
than perfect organization. The user can always move it later.

```markdown
---
date: 2026-03-23
tags: [inbox, quick-capture]
---

# [The idea or content]

[Content as provided by the user]
```

## Appending to Existing Notes

If the user wants to add content to an existing note:
1. Read the existing note first
2. Append in a way that fits the existing structure
3. Don't modify existing content unless asked
4. Add new [[links]] if the appended content introduces new connections
