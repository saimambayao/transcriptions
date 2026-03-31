---
name: guide-drafter
description: |
  Create or update topic GUIDE files that synthesize video transcript knowledge into actionable
  application patterns. Two modes: CREATE (generate a fresh GUIDE from all transcripts in a group)
  and UPDATE (incrementally add a new transcript's insights to an existing GUIDE).
  Use this skill when: (1) a new transcript is added to a topic group and the GUIDE needs updating,
  (2) the user says "update guide", "refresh guide", "create guide", "guide drafter",
  (3) invoked automatically by /youtube-transcriber after saving a new transcript,
  (4) the user wants to regenerate all guides or a specific topic's guide.
argument-hint: "[topic-folder] [optional: new-transcript-path]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Guide Drafter

Creates and maintains topic-level GUIDE files with a **two-layer structure**:

1. **The Guide** (publishable) — authoritative, third-person knowledge synthesis written like
   a professional blog post. Shareable, universal, no personal references.
2. **For Your Work** (personal) — specific applications to the user's projects, roles, and
   workflows, including Priority Actions with timeboxed next steps.

## Citation Format

All GUIDE files use **Chicago/Turabian footnote style** for video transcript citations:

```
[^1]: Author Last, First. "Video Title." *Channel Name*, Duration. Platform, Date.
      URL
```

**Examples:**

```
[^1]: Milo, Nick. "Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork."
      *Linking Your Thinking with Nick Milo*, 21:29. YouTube, March 2026.
      https://youtube.com/watch?v=s3ccD6m6WKc

[^2]: Maurya, Ash. "Capture Your Business Model in 20 Minutes."
      *LEANSTACK*, 19:45. YouTube, January 2025.
      https://youtube.com/watch?v=abc123
```

**Extracting citation data from transcripts:**
Each transcript has a metadata header block with the required fields:
```markdown
# Video Title                    ← Title (remove any leading/trailing quotes)
**Channel**: Channel Name        ← Channel (use as-is, italicize in citation)
**Duration**: 12:34              ← Duration
**URL**: https://youtube.com/... ← URL
**Transcribed**: 2026-03-24 10:40 ← Use for approximate date
```

**Author extraction rules:**
- If the channel name IS a person's name → use as author (e.g., "Nick Milo" → Milo, Nick)
- If the channel name is a brand → extract the host/creator from the transcript content or
  use the channel name as author (e.g., "LEANSTACK" by Ash Maurya → Maurya, Ash)
- Common channels and their authors:
  - *Linking Your Thinking with Nick Milo* → Milo, Nick
  - *LEANSTACK* or *Ash Maurya - LEANFoundry* → Maurya, Ash
  - *Y Combinator* → use speaker name from transcript
  - *Fireship* → Delaney, Jeff
  - For unknown channels: use channel name as corporate author

## GUIDE File Structure

```markdown
# {Topic Name}

{Hook — 1-2 sentences that frame the problem or opportunity this guide addresses.
Not "this guide covers..." but a compelling statement about why this matters.}

{Context paragraph — what the reader will learn, written in third person.
Authoritative but accessible, like an Anthropic blog post.}

---

## {Pattern Name as Descriptive Header}

{Opening paragraph — 2-3 sentences explaining the concept and why it matters.
Written in third person ("developers should...", "teams can...", "the key insight is...").
No "I" or "my experience". Authoritative, educational tone.}

> **Key insight**: {One-line blockquote capturing the core principle} [^1]

{Explanation paragraph — concrete details, frameworks, or steps. Can include:}

- **Bold term** — explanation of how it works [^1][^2]
- **Another concept** — with specific examples or metrics [^3]
- **Practical application** — what this looks like in practice [^1]

{Optional: code block, command, or structured example if relevant}

**The takeaway**: {One sentence distilling the actionable wisdom.}

## {Next Pattern}

{Same structure...}

---

## For Your Work

{1-2 sentences transitioning from universal knowledge to personal application.
This section is NOT for publishing — it's the user's private action layer.}

### Applications

- **{Project name}** — specific way to apply pattern X to this project [^N]
- **{Another project}** — specific way to apply pattern Y [^N]
- **{Skill name}** — how to enhance or create a skill based on pattern Z [^N]

### Priority Actions

1. **This week**: {concrete action tied to a specific project}
2. **This week**: {another action}
3. **This month**: {larger action}
4. **This quarter**: {strategic action}
...

---

## References

[^1]: Last, First. "Title." *Channel*, Duration. Platform, Date. URL
[^2]: Last, First. "Title." *Channel*, Duration. Platform, Date. URL
...
```

## Writing Voice — The Guide Section

The publishable section uses a **professional third-person voice** modeled on Anthropic's
blog and developer documentation:

### Do:
- Write in **third person**: "developers can...", "teams should...", "the pattern works by..."
- Use **authoritative but accessible** tone — explain concepts without condescension
- Open each pattern with a **problem statement** before the solution
- Include **concrete examples** with specific numbers, tools, or frameworks
- Use **blockquotes** for key insights and core principles
- Reference **established concepts** by name (Lean Canvas, Red-Green-Refactor, Kano Model)
- End each pattern with **"The takeaway:"** — one sentence of distilled wisdom
- Write **complete paragraphs** (2-4 sentences) for explanations, not just bullets
- Keep total Guide section to **1,500-2,500 words** (readable in 8-12 minutes)

### Don't:
- Use "I", "my", "we", or any first-person voice in the Guide section
- Reference the user's specific projects (e-Bangsamoro, MoroTech) — those go in "For Your Work"
- Write dense walls of bullets — mix paragraphs and bullets
- Use generic filler ("it's important to note that...")
- Start sections with "This section covers..." — start with the insight

### Tone examples:

**Good** (Anthropic blog style):
> The most common mistake in business model design is building before validating.
> Experienced founders reverse this sequence: they demonstrate the solution, sell it
> to early adopters, and only then build the full product. This Demo-Sell-Build pattern
> reduces waste by ensuring demand exists before engineering begins. [^1][^2]

**Bad** (generic AI summary):
> In this section, we'll explore how to validate your business model. It's important
> to note that many founders make the mistake of building too early. Here are some
> key takeaways from the research.

## Writing Voice — For Your Work Section

The personal section uses **direct, actionable second person** ("you", "your"):
- Name specific projects, skills, and initiatives
- Reference the user profile from `~/Vault/about-saidamen.md`
- Include timeboxed Priority Actions (this week / this month / this quarter)
- Cross-reference specific Gemini CLI skills by name (e.g., /bill-drafter, /lean-canvas)

## Format Rules

- **Filename**: `{Topic-Name}-GUIDE.md` (Title-Case, singular GUIDE)
- **Patterns by theme**, NOT by video — synthesize across multiple transcripts
- **Footnote markers** `[^N]` inline after each claim, reuse same number for same source
- **Multiple sources** on one bullet: `[^1][^3]` (no comma between)
- **References section** at the bottom with full Chicago citations
- **Guide section**: third-person, publishable, universal
- **For Your Work section**: second-person, personal, actionable

## Modes

### CREATE Mode

Triggered when no GUIDE exists for the topic group, or user explicitly asks to regenerate.

1. Read `~/Vault/about-saidamen.md` (first 100 lines) for personalization context
2. List all `.md` transcript files in the topic folder (exclude GUIDE files)
3. Read each transcript's **metadata header** (first 10 lines) and **Organized Notes** section
   - Do NOT read the full Transcript section — Organized Notes has the synthesized content
4. Extract citation metadata (title, channel, duration, URL, date) from each header
5. Identify **application patterns** that emerge across multiple transcripts
6. Write the GUIDE file with both layers:
   - **The Guide** (publishable, third-person, universal)
   - **For Your Work** (personal, second-person, project-specific)
7. Save to BOTH:
   - `docs/video-transcripts/{topic}/{Topic-Name}-GUIDE.md`
   - `~/Vault/transcripts/{topic}/{Topic-Name}-GUIDE.md`

### UPDATE Mode

Triggered when a new transcript is added to a group that already has a GUIDE.

**Input**: topic folder path + new transcript path

1. Read the existing GUIDE file
2. Read the new transcript's **metadata header** and **Organized Notes**
3. Extract citation metadata from the new transcript
4. Analyze what the new transcript adds:
   - **New patterns** not already covered → add new pattern section to The Guide
   - **New evidence** for existing patterns → add content to existing sections with new footnote
   - **New project applications** → add to For Your Work section
   - **Nothing new** → add the transcript to References only
5. Assign the next available footnote number to the new transcript
6. Update the GUIDE:
   - Enrich The Guide section (maintain third-person voice)
   - Update For Your Work if new insights change priorities
   - Add new footnote to References section
7. Save to BOTH locations (repo + vault)

### BATCH Mode

Triggered when user asks to update/regenerate all guides.

1. List all topic folders in `docs/video-transcripts/`
2. For each folder that contains transcripts:
   - If no GUIDE exists → CREATE mode
   - If GUIDE exists → check if any transcripts are missing from References → UPDATE for each
3. Run as parallel agents (one per topic group)

## Topic Folder Mapping

| Folder | GUIDE Filename | Topic Name |
|--------|---------------|------------|
| `ai-claude-cowork/` | `AI-Claude-Cowork-GUIDE.md` | Claude Cowork |
| `ai-gemini-cli/` | `AI-Claude-Code-GUIDE.md` | Gemini CLI |
| `ai-design/` | `AI-Design-GUIDE.md` | AI Design Tools |
| `bangsamoro-governance/` | `Bangsamoro-Governance-GUIDE.md` | Bangsamoro Governance |
| `lean-startup/business-model/` | `Business-Model-GUIDE.md` | Business Model Design |
| `lean-startup/founder-mindset/` | `Founder-Mindset-GUIDE.md` | Founder Mindset |
| `lean-startup/mvp-and-validation/` | `MVP-and-Validation-GUIDE.md` | MVP & Validation |
| `lean-startup/sales-and-growth/` | `Sales-and-Growth-GUIDE.md` | Sales & Growth |
| `lean-startup/startup-strategy/` | `Startup-Strategy-GUIDE.md` | Startup Strategy |
| New topic → derive from folder name | `{Topic-Name}-GUIDE.md` | Derive from folder |

## Integration with /youtube-transcriber

After /youtube-transcriber completes steps 1-10 (transcribe, organize, vault, knowledge note,
index, NotebookLM, fact-check), it invokes /guide-drafter in UPDATE mode:

```
/guide-drafter {topic-folder} {new-transcript-path}
```

The guide-drafter reads the existing GUIDE and the new transcript, determines what's new,
and updates incrementally. This keeps GUIDEs as living documents that grow with each
new transcript.
