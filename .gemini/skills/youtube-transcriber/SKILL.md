---
name: youtube-transcriber
description: |
  Transcribes videos from YouTube, Facebook, Instagram, TikTok, and other platforms to clean
  markdown text. Uses a 3-tier strategy: YouTube caption API (fastest), yt-dlp subtitle
  extraction (any platform with captions), and Whisper fallback (universal).
  Use this skill whenever the user wants to: transcribe a video, get text from a YouTube/Facebook/
  Instagram/TikTok video, extract captions or subtitles, convert a video to text, get a
  transcript, or turn a video into readable text. Also triggers on phrases like "what did they
  say in this video", "summarize this video" (transcribe first, then summarize), or any request
  involving video URLs where the user needs the spoken content as text.
argument-hint: "[video-url]"
allowed-tools: Read, Bash, Write, Glob, Grep
---

# Video Transcriber

Transcribes videos from YouTube, Facebook, and other platforms to markdown text.

## How It Works

The skill uses a three-tier approach:

1. **Tier 1 — YouTube caption API** (`youtube-transcript-api`): Fetches the same captions
   you see in YouTube's "Show transcript" panel. Works for ~95% of public YouTube videos.
   Takes about 2 seconds. YouTube only.

2. **Tier 2 — yt-dlp subtitle extraction**: Extracts captions from any platform (Facebook,
   Instagram, TikTok, Twitter, etc.) using `yt-dlp --write-auto-sub --skip-download`.
   No video download needed. Takes 3-5 seconds. Works on any platform where captions exist.

3. **Tier 3 — Audio extraction + Whisper**: Downloads just the audio track via `yt-dlp`,
   then transcribes locally using OpenAI's Whisper. Slower but works on any video with audio,
   even without captions. Universal fallback.

**Platform support**: YouTube, Facebook (videos + reels), Instagram, TikTok, Twitter/X,
and any of the 1000+ sites supported by yt-dlp.

## Verification Protocol

**After output (DETECT):**
Invoke `/fact-checker` to verify names, institutions, and legislation references.
For transcripts, verify all person names against `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`.

**Before publishing (CONFIRM):**
Present verification results to the user.

## Prerequisites

The transcribe script handles dependency checking and will tell you what's missing. The required tools:

```bash
# Primary (required)
pip3 install youtube-transcript-api

# Fallback (optional — only needed for videos without YouTube captions)
brew install yt-dlp          # or: pip3 install yt-dlp
pip3 install openai-whisper  # requires ffmpeg: brew install ffmpeg
```

## Usage

Run the transcription script from this skill's directory:

```bash
SKILL_DIR="/Users/saidamenmambayao/.gemini/skills/youtube-transcriber"
"$SKILL_DIR/venv/bin/python3" "$SKILL_DIR/scripts/transcribe.py" [OPTIONS] URL [URL ...]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--lang LANG` | Preferred transcript language (ISO code) | `en` |
| `--output PATH` | Save transcript to file instead of stdout | stdout |
| `--fallback` | Enable Whisper fallback for videos without captions | Off |
| `--whisper-model` | Whisper model size: tiny, base, small, medium, large | `base` |

### Examples

```bash
# Basic transcription
python3 scripts/transcribe.py "https://youtube.com/watch?v=abc123"

# Filipino language transcript
python3 scripts/transcribe.py --lang fil "https://youtube.com/watch?v=abc123"

# Save to file
python3 scripts/transcribe.py --output transcript.md "https://youtube.com/watch?v=abc123"

# With Whisper fallback enabled
python3 scripts/transcribe.py --fallback "https://youtube.com/watch?v=abc123"

# Batch — multiple videos
python3 scripts/transcribe.py URL1 URL2 URL3

# Batch — save each to separate files
python3 scripts/transcribe.py --output transcripts/ URL1 URL2 URL3
```

## Output Format

The final document has THREE sections:

1. **Organized Notes** (top) — A detailed, AI-generated summary organized by topic with bold
   section headers and clean prose. NO timestamps in this section. Claude generates this AFTER
   transcription by reading the Transcript section.
2. **What This Means for Your Work** (middle) — A personalized evaluation of how the video's
   knowledge applies to the user's actual work. Before writing this section, read
   `~/Vault/about-saidamen.md` for the user's full profile — roles, projects, competencies,
   and what drives the work. Reference specific projects, roles, and initiatives from the
   profile (not generic advice). Analytical and actionable — not a summary, but an assessment
   of what changes, validates, or challenges the user's current approach. Include concrete
   next steps tied to specific projects or workflows the user actually has.

   **Required subsection — "How This Can Improve Your Gemini Skills and Workflows"**:
   After the main analysis, add an `### How This Can Improve Your Gemini Skills and Workflows`
   subsection. This evaluates how the video's ideas could enhance, refine, or challenge the
   user's existing Gemini CLI skill system and AI-augmented workflows. Before writing, consult
   `~/Vault/Gemini-Skills/index.md` for the full 124-skill library and `~/Vault/about-saidamen.md`
   for the user's Gemini CLI setup (129 skills, Obsidian vault memory, NotebookLM integration,
   parallel agents, frontend-first development, fact-checking pipeline).

   Reference specific skills and projects by name. The subsection should cover any combination of:
   - **Skill improvements** — which existing skills (e.g., /research-pipeline, /expert-builder,
     /skill-optimizer, /fact-checker, /bangsamoro, /bill-drafter) could benefit from ideas in the video
   - **New skill opportunities** — does the video suggest a skill the user doesn't have yet?
     Check ~/Vault/Gemini-Skills/index.md to verify it doesn't already exist before recommending
   - **Workflow changes** — how could the video's patterns change the user's development workflow
     (frontend-first dev, parallel agents, Obsidian vault sync, NotebookLM pipeline, skills-bucket)
   - **Project-specific applications** — which of the 9+ active projects (e-Bangsamoro,
     MoroMarket, Parliamentarian, OBCMS, Tarbiyyah-MS, BangsamoroHR, IPP, SBP, MoroTech)
     would benefit from implementing the video's ideas
   - **Cross-pollination** — connections between the video's domain and the user's Bangsamoro
     governance, cooperative development, or legislative capacity work

   Keep it analytical and specific — name the skills, name the projects, describe the concrete
   change. No generic "this could improve your workflow" statements.
3. **Transcript** (bottom) — Verbatim `[MM:SS]` timestamped idea-grouped paragraphs, produced
   by the script. Each timestamp marks a complete idea (a sentence or paragraph), not a raw
   caption fragment.

```markdown
# Video Title

**Channel**: Channel Name
**Duration**: 12:34
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=abc123

---

## Organized Notes

**Introduction**

- Key idea expressed as a **concise bullet** with bold keywords
- Another key point with **specific examples** preserved

**Key Concept Name**

- Main idea of this concept in a **scannable bullet**
- Steps or sub-points as a **numbered list**:
  1. First step
  2. Second step
- Takeaway: **bold the key insight**

**Another Topic**

- More key ideas as **bullets, not paragraphs**

---

## What This Means for Your Work

Personalized evaluation of how this video's knowledge applies to the user's
specific work context. Analytical, not summary. Includes concrete next steps.

### How This Can Improve Your Gemini Skills and Workflows

Specific analysis of how the video's ideas map to existing skills (by name),
active projects, and AI-augmented workflows. References skills from
~/Vault/Gemini-Skills/index.md and projects from ~/Vault/about-saidamen.md.

---

## Transcript

[00:00] Complete sentences grouped into idea-sized paragraphs.
Multiple caption fragments are merged into coherent blocks.

[00:13] Another complete idea with its own timestamp. Each block
represents a logical thought, not a raw caption segment.
```

## Workflow

When the user provides a YouTube URL:

0. **Duplicate check**: Before transcribing, extract the video ID from the URL and grep
   `docs/video-transcripts/index.md` for it. The index is a markdown file with tables
   organized by topic subfolder, where each row has `| VIDEO_ID | Title | Filename |`.
   ```bash
   grep "VIDEO_ID" docs/video-transcripts/index.md
   ```
   - If found: tell the user "This video has already been transcribed" and show the existing
     file path. Ask if they want to re-transcribe (overwrite) or skip.
   - If not found: proceed to step 1.
   - Extract video ID from URL: `youtube.com/watch?v=VIDEO_ID` or `youtu.be/VIDEO_ID`

1. Run the transcribe script with the user's URL and any preferences (language, output path).
   The script produces the metadata header + placeholder Organized Notes + idea-grouped Transcript.

2. **Generate Organized Notes**: After the script saves the file, read the Transcript section
   and generate the Organized Notes to replace the `<!-- PLACEHOLDER -->` comment. Follow these rules:
   - Create meaningful **bold section headers** that group content by topic
   - Use **bullet points** and **numbered lists** — NOT dense paragraphs
   - **Bold key words** and key phrases within bullets for scannability
   - NO timestamps in this section
   - Capture every key idea, example, and argument — but keep each bullet concise
   - Preserve specific names, tools, frameworks, and examples mentioned
   - **First mention rule**: When a person is first mentioned, provide their **complete name and full position/title** (e.g., "Interim Chief Minister **Abdulraof A. Macacua**", "CEO **John Smith** of Acme Corp"). Subsequent mentions can use shortened forms. Research correct names/titles if auto-captions garble them.
   - Organize by topic, not chronologically
   - **Language cleanup**: Remove garbled characters from non-expected scripts (Thai, Bengali, Hindi, etc.) — these are auto-caption noise. Only English, Filipino, and Arabic are expected.
   - **Arabic translation**: When Arabic text appears (prayers, Quranic verses, formal greetings), preserve the Arabic and provide an English translation in brackets immediately after (e.g., `[Translation: O Allah, guide our leaders...]`)
   - **Quotable Quotes**: Place quotes **inline within each speaker's section** (NOT as a separate bottom section). Add up to 5 quotes per speaker labeled `*Quotable Quotes:*`. Each quote should be standalone and complete (1-5 sentences), meeting 3+ criteria: standalone clarity, emotional punch, policy significance, quotable length, attributable, shareable on social media. Format:
     ```
     *Quotable Quotes:*
     > "Standalone complete quote here." [MM:SS]
     ```
     Clean up filler words but preserve the speaker's voice.
   - Use the Edit tool to replace the placeholder with the generated content

3. If transcription fails and `--fallback` is not set, suggest re-running with `--fallback`

4. Save the output to the appropriate subfolder in `docs/video-transcripts/`:

   **File naming convention**: `YYMMDD-HHMM-slugified-title.md`
   - `YYMMDD` = transcription date (from the `**Transcribed**` metadata line)
   - `HHMM` = transcription time (24h format, from the `**Transcribed**` metadata line)
   - `slugified-title` = video title in lowercase, spaces replaced with hyphens, special chars removed
   - Example: `260323-0155-stop-fixing-your-gemini-skills-autoresearch-does-it-for-you.md`

   **Subfolder routing** — choose the BEST match, not just "ai-engineering" for everything:

5. **Save full transcript to vault**: Copy the complete transcript file to
   `~/Vault/transcripts/{topic}/yymmdd-hhmm-slugified-title.md` where `{topic}` mirrors
   the transcript subfolder routing. Create the subfolder if it doesn't exist yet.
   This is an exact copy of the file saved in step 4 — same content, same filename.

6. **Save vault knowledge note**: After generating Organized Notes, create a condensed
   knowledge note at `~/Vault/knowledge-areas/{topic}/yymmdd-short-title.md` where `{topic}`
   mirrors the transcript subfolder (e.g., `ai-design/`, `ai-engineering/`, `lean-startup/business-model/`).
   Create the subfolder if it doesn't exist yet.

   The note should contain:
   - YAML frontmatter: date, tags, source (video URL)
   - **3-5 key takeaways only** — the most actionable insights, not everything
   - [[links]] to related vault notes if they exist
   - This is much shorter than the full Organized Notes — just the signal

   **Important**: Do NOT save to `~/Vault/research/` — that folder is reserved for
   /deep-research, /notebooklm, and Claude Cowork outputs.

7. **Update knowledge area index.md**: After saving the knowledge note, update the topic's
   `~/Vault/knowledge-areas/{topic}/index.md` living document:

   a. If the index.md doesn't exist yet, create it with the standard 3-section format:
      - **Executive Summary** — comprehensive synthesis of all knowledge in this area
      - **What It Means For You** — personalized implications for the user's work
        (e-Bangsamoro, Bangsamoro governance, solo dev workflow, cooperatives/SEs)
      - **Change Log** — append-only table (date, source link, type, what was added)

   b. If it exists, update all 3 sections:
      - Incorporate new insights into the **Executive Summary** (don't just append — synthesize)
      - Reassess **What It Means For You** if new insights change the calculus
      - Append a new row to the **Change Log** table
      - Update the `updated:` and `sources:` count in YAML frontmatter

8. **Add to NotebookLM notebook**: Add the YouTube URL and transcript file to a topic-based
   NotebookLM notebook. This builds up research notebooks organically over time.

   Topic-to-notebook mapping (matches subfolder routing):
   - `ai-gemini-cli/` → `"AI Engineering"`
   - `ai-claude-cowork/` → `"AI Engineering"`
   - `ai-design/` → `"AI Design"`
   - `lean-startup/business-model/` → `"Lean Startup: Business Model"`
   - `lean-startup/mvp-and-validation/` → `"Lean Startup: MVP & Validation"`
   - `lean-startup/sales-and-growth/` → `"Lean Startup: Sales & Growth"`
   - `lean-startup/founder-mindset/` → `"Lean Startup: Founder Mindset"`
   - `lean-startup/startup-strategy/` → `"Lean Startup: Strategy"`
   - New topics → create a notebook with a descriptive name

   Steps:
   a. Run `notebooklm list --json` to get full notebook UUIDs (table view truncates IDs!)
   b. Parse the JSON to find the topic notebook by title substring
   c. If it exists: `notebooklm use <full-uuid>`
   d. If not: `notebooklm create "Topic Name"` then **immediately** `notebooklm use <new-uuid>` (create does NOT reliably set active notebook)
   e. Verify with `notebooklm metadata --json` that the correct notebook is active
   f. Add both sources:
      ```bash
      notebooklm source add "https://youtube.com/watch?v=..."
      notebooklm source add "./path/to/saved/transcript.md"
      ```
   f. If NotebookLM errors, skip silently — don't block the transcription

   **CRITICAL**: Always use `--json` for `notebooklm list`. The table view truncates UUIDs,
   and truncated IDs cause `RPC GET_NOTEBOOK failed` errors that look like auth failures.
   - `ai-gemini-cli/` — Gemini CLI CLI, skills, agent teams, Obsidian+Code, NotebookLM+Code, GEMINI.md, Karpathy agents
   - `ai-claude-cowork/` — Claude Cowork (Desktop), plugins, scheduled tasks, MCP connectors, non-developer AI workflows
   - `ai-design/` — AI design tools (Stitch, v0, Bolt), vibe design, UI generation, Figma AI
   - `lean-startup/business-model/` — Lean Canvas, business plans, pricing, product-market fit
   - `lean-startup/mvp-and-validation/` — MVP strategy, experiments, testing ideas
   - `lean-startup/sales-and-growth/` — selling, customers, metrics, content strategy
   - `lean-startup/founder-mindset/` — lessons, mindset, competition, founder stories
   - `lean-startup/startup-strategy/` — frameworks, launch blueprints, startup playbooks
   - Create a new subfolder if the topic doesn't fit existing categories
   - **Choose the BEST match** — don't default to ai-engineering for everything AI-related

9. **Update transcript index**: After saving the transcript, add a new row to the appropriate
   topic table in `docs/video-transcripts/index.md`. Each table has columns:
   `| Video ID | Title | File |`. Also update the **Total** count at the top of the file.
   If the topic subfolder doesn't have a section in the index yet, create one.

10. **Fact-check the output.** Run `/fact-checker` on the saved transcript file. Whisper and
   auto-captions routinely garble names, titles, and organizations — especially Filipino Muslim
   names in Bangsamoro content. The fact-checker verifies all people, titles, legislation
   references, and organizations against local reference files and web sources.

11. **Update the topic GUIDE.** Invoke `/guide-drafter` in UPDATE mode to incrementally update
   the topic group's application guide with insights from the new transcript. Pass the topic
   folder and new transcript path:
   ```
   /guide-drafter {topic-folder} {new-transcript-path}
   ```
   The guide-drafter reads the existing GUIDE, determines what the new transcript adds (new
   patterns or new evidence for existing patterns), updates with proper Chicago/Turabian
   footnote citations, and saves to both repo and vault. If no GUIDE exists yet for this
   topic group, guide-drafter runs in CREATE mode to generate one from scratch.

## Gotchas

- Filipino Muslim names from auto-captions are ALWAYS garbled — verify every person name against ~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md
- Thai, Bengali, Hindi, and other non-expected script characters are auto-caption noise — delete them; only English, Filipino, and Arabic are expected
- Arabic prayers and Quranic verses should be preserved in Arabic with English translation in brackets
- Channel names are not always the speaker's name — extract the actual host/creator from transcript content for citation metadata
- Whisper model "base" is the default fallback — for long videos (1h+), the primary YouTube caption API method is instant while Whisper takes minutes
- Auto-generated captions frequently merge words or split them incorrectly — always proofread proper nouns, legislation references, and technical terms

## Error Handling

| Error | What happens |
|-------|-------------|
| No captions available | Reports the issue; suggests `--fallback` to use Whisper |
| Private/age-restricted video | Reports access error; suggests the user try a different URL |
| Invalid URL | Reports the error with the problematic URL |
| Missing dependencies | Lists exactly what to install |
| Whisper not installed (fallback requested) | Gives install command |

## Tips

- Most YouTube videos have auto-generated English captions — the primary method works almost always
- For non-English videos, try `--lang` with the video's language code first
- The `base` Whisper model is a good balance of speed and accuracy for the fallback
- For long videos (1h+), the primary method is instant; Whisper fallback will take several minutes
- Batch mode with `--output transcripts/` creates one `.md` file per video, named after the video title
- YouTube chapters (when set by the creator) can inform section header choices in Organized Notes
