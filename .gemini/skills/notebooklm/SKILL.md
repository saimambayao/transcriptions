---
name: notebooklm
description: |
  Use Google NotebookLM from Gemini CLI via the notebooklm-py CLI. Offloads heavy analysis
  to Google's servers for free — no token cost on your side. Use when user mentions "notebooklm",
  "notebook lm", "research with notebooklm", "generate podcast", "generate audio",
  "analyze these videos", "create an infographic from", "add to notebook", "generate slides",
  "generate quiz", "generate flashcards", "mind map from", or wants to analyze YouTube videos,
  PDFs, or web sources through NotebookLM. Also trigger when user wants deliverables like
  podcasts, slide decks, infographics, or quizzes generated from research sources.
allowed-tools: Bash, Read, Write
---

# NotebookLM CLI

Control Google NotebookLM from the terminal. Analysis runs on Google's servers — free tokens.

## Prerequisites

- CLI installed via `pipx install "notebooklm-py[browser]"`
- Authenticated at `~/.notebooklm/storage_state.json`
- If auth fails, run `notebooklm login` (opens browser for Google sign-in)

## Quick Reference

### Notebooks

**CRITICAL: Always use `--json` when you need notebook IDs.** The table view truncates UUIDs,
and truncated IDs cause `RPC GET_NOTEBOOK failed` errors that look like auth failures but aren't.

```bash
notebooklm list --json             # ALWAYS use --json to get full UUIDs
notebooklm list                    # Table view (for display only — IDs are truncated!)
notebooklm create "Research Topic" # Create new notebook
notebooklm use <full-uuid>         # Set active notebook — MUST be full UUID
notebooklm metadata --json         # Export notebook metadata
```

### Notebook ID Resolution

When you need to `use` a notebook, follow this pattern:

```bash
# Step 1: Get full ID via --json
NOTEBOOK_ID=$(notebooklm list --json 2>/dev/null | python3 -c "
import sys, json
data = json.load(sys.stdin)
for nb in data.get('notebooks', []):
    if 'TARGET_NAME' in nb.get('title', ''):
        print(nb['id'])
        break
")

# Step 2: Use full ID
notebooklm use "$NOTEBOOK_ID"
```

Replace `TARGET_NAME` with a substring of the notebook title (e.g., `AI Engineering`).

### Sources (up to 50 per notebook)
```bash
notebooklm source add "https://youtube.com/watch?v=..."  # YouTube URLs
notebooklm source add "./document.pdf"                    # Local files
notebooklm source add-research "Topic" --mode deep --import-all  # Default: deep research
notebooklm source add-research "Topic keywords"                  # Fast mode (only if user requests)
notebooklm source add-research "docs" --from drive        # Search Google Drive
notebooklm source list                                    # List current sources
```

### Research Management (for deep mode)
```bash
notebooklm source add-research "Topic" --mode deep --no-wait  # Start async deep research
notebooklm research status                                     # Check progress
notebooklm research wait --import-all                          # Wait and auto-import results
```

### Chat & Analysis
```bash
notebooklm ask "What are the key takeaways?"    # Query sources
```

### Generate Deliverables
```bash
notebooklm generate audio                             # Podcast
notebooklm generate video --style whiteboard           # Video (9 styles available)
notebooklm generate slide-deck                         # Presentation
notebooklm generate infographic --orientation portrait  # Infographic
notebooklm generate mind-map                           # Mind map
notebooklm generate quiz --difficulty hard              # Assessment
notebooklm generate flashcards --quantity more          # Study cards
notebooklm generate data-table "structure description"  # Structured data
```

### Download Artifacts
```bash
notebooklm download audio ./podcast.mp3
notebooklm download video ./video.mp4
notebooklm download slide-deck ./slides.pdf
notebooklm download quiz --format json ./quiz.json
```

## Workflow Selection

Choose the workflow based on user input:

| User Provides | Workflow | When |
|--------------|----------|------|
| YouTube URLs | YouTube Research Pipeline | Analyzing video content |
| Local files (PDF, docs) | Document Analysis | Extracting insights from documents |
| Topic/question (no sources) | Topic Deep Dive | Broad research with `--mode deep` |
| Topic + needs background processing | Async Deep Research | Long investigations, non-blocking |

If ambiguous, ask: "Do you have specific sources, or should I research the topic broadly?"

## Completion Report

After finishing any workflow, always report back to the user:

```
**NotebookLM Complete**
- **Notebook**: [name] ([source count] sources)
- **Sources added**: [list of source names/URLs]
- **Queries answered**: [count]
- **Deliverables generated**: [list with file paths if downloaded]
- **Next steps**: [suggest follow-up actions — generate podcast, add more sources, etc.]
```

**Filled-in example:**
```
**NotebookLM Complete**
- **Notebook**: Research: Cooperative Development (4 sources)
- **Sources added**: RA 9520 full text, CDA Annual Report 2024, 2 YouTube interviews
- **Queries answered**: 3
- **Deliverables generated**: infographic (~/Downloads/260323-cooperative-dev.png)
- **Next steps**: Generate podcast for deeper synthesis, or add more sources from BARMM cooperatives
```

Save downloaded artifacts to `~/Downloads/` or the user's specified location.
Use naming convention: `yymmdd-topic-slug.{ext}` (e.g., `260323-cooperative-frameworks.mp3`).

**Timeout syntax for long-running commands:** When using Bash tool, set `timeout: 300000`
(5 minutes) for `source add-research`, `generate audio`, `generate video`, `generate slide-deck`.
Default 120s will kill these prematurely.

## Typical Workflows

### YouTube Research Pipeline
1. `notebooklm create "Research: [Topic]"`
2. `notebooklm source add "https://youtube.com/watch?v=..."` (repeat for multiple videos)
3. **VERIFY**: `notebooklm source list` — confirm all sources loaded (count matches expected)
4. `notebooklm ask "What are the key themes across these videos?"`
5. `notebooklm generate infographic` or `generate slide-deck` (use `timeout: 300000`)
6. Download the artifact and save to vault or project
7. Print **Completion Report** (see template above)

### Document Analysis
1. `notebooklm create "Analysis: [Document Name]"`
2. `notebooklm source add "./path/to/document.pdf"`
3. **VERIFY**: `notebooklm source list` — confirm document loaded
4. `notebooklm ask "Summarize the key findings"`
5. Generate any deliverables needed
6. Print **Completion Report**

### Topic Deep Dive (Deep Research Mode)
1. `notebooklm create "Deep Dive: [Topic]"`
2. `notebooklm source add-research "topic keywords" --mode deep --import-all` (use `timeout: 300000`)
3. **VERIFY**: `notebooklm source list` — if 0 sources, deep research failed silently. Retry or fall back.
4. `notebooklm ask "What are the main arguments and counterarguments?"`
5. `notebooklm generate audio` for a podcast summary
6. `notebooklm generate report` for a structured research report
7. Print **Completion Report**

### Async Deep Research (for longer investigations)
1. `notebooklm create "Research: [Topic]"`
2. `notebooklm source add-research "topic" --mode deep --no-wait` (starts research in background)
3. `notebooklm research status` (check progress)
4. `notebooklm research wait --import-all` (wait and auto-import when done)
5. **VERIFY**: `notebooklm source list` — confirm sources imported
6. `notebooklm ask "Synthesize the key findings"`
7. Print **Completion Report**

## Error Handling

| Error | Actual Cause | Fix |
|-------|-------------|-----|
| `RPC GET_NOTEBOOK failed` / `null result data` | **Truncated notebook ID** — NOT auth | Use `notebooklm list --json` to get full UUID |
| `API returned no data for URL` | Notebook not properly selected | Re-run `notebooklm use <full-uuid>` first |
| `Failed to get SOURCE_ID` | Source add failed (bad URL, or notebook not selected) | Verify notebook is selected with `notebooklm metadata --json` |
| `Authentication required` / `storage_state.json not found` | Actual auth issue | Run `notebooklm login` (opens browser) |
| `Session expired` | Google session timed out | Run `notebooklm login` to re-authenticate |

**The #1 gotcha**: Most "auth-looking" errors are actually truncated ID errors.
Always use `--json` when fetching IDs. Never copy-paste IDs from the table view.

**Good vs bad UUID example:**
```
BAD  (from table view):  a1b2c3d4-e5f6-...        ← truncated, causes RPC failure
GOOD (from --json):      a1b2c3d4-e5f6-7890-abcd-ef1234567890  ← full UUID, works
```

## Limits & Scaling

- **Max 50 sources per notebook** — create separate notebooks for separate research topics
- **Deep research takes 2-5 minutes** — always run in foreground with `timeout: 300000`
- **Deliverable generation times**: text analysis ~30s, slide decks up to 15 min, audio/video slower
- **Session timeout**: Google sessions expire after extended periods — re-auth with `notebooklm login`
- **Source add-research silent failure**: can return 0 sources in background mode (known bug). Always verify with `notebooklm source list` after adding sources

## Used By

These skills build on `/notebooklm` as infrastructure:
- `/research-pipeline` — Phase 2 (source ingestion + deep research + querying)
- `/youtube-transcriber` — Step 6 (adds videos to topic notebooks)
- `/expert-builder` — builds domain experts from NotebookLM research

## Caveats

- Uses **undocumented Google APIs** — best for research and prototyping, not production workflows
- All processing happens on Google's infrastructure — **zero Gemini CLI token cost** for analysis
