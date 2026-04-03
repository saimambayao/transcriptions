# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
A documentation and transcription repository — no build system, no tests. Content is markdown files organized by topic. Python scripts are standalone utilities (run with `python3 <script>.py`).

### Repository Structure
See [INDEX.md](INDEX.md) for the full directory listing with file counts and links. Summary:
- `legislation/` — BAAs, Bills (enacted/proposed), Resolutions (enacted/proposed), national laws
- `guidebooks/` — All BARMM guidebooks (bill-drafting, CSW, MOP, supervision, etc.) with `_archive/` for older versions; each guidebook is an independent publication
- `transcripts/` — YouTube video transcripts organized by topic subfolder
- `reference/` — Constitution, BDP, systems-ebooks, BAA No. 85 breakdown
- `source-pdfs/` — Source PDF documents (BAA PDFs, Resolution PDFs, Parliament assignments)
- `parliamentary/` — Parliamentary records
- `planning/` — Planning, evaluation, and fact-check documents
- `presentations/` — PowerPoint presentations
- `scripts/` — Python/shell utilities for markdown processing
- `docs/superpowers/` — Claude superpowers specs

### Python Utilities (in `scripts/`)
- `scripts/generate_indexes.py` — generates index files from legislative markdown documents
- `scripts/standardize_md.py` — standardizes markdown formatting across files
- `scripts/apply_standardization.py` — batch applies standardization rules
- `scripts/audit_files.py` / `scripts/debug_baa.py` — diagnostic scripts for content auditing

## National Laws Archive
- `legislation/national-laws/` — 11,866 Republic Acts (RA 1 to RA 12313) scraped from lawphil.net
- **INDEX.md** — master index with all RA numbers and titles; grep by keyword to find RAs
- **Subfolders**: `RA-0001-0499/` through `RA-12000-12499/` (25 folders) + `GAA/` (General Appropriations Acts)
- **Vault symlink**: `~/Vault/Ph-Laws/republic-acts/` points here
- **Source pre-load protocol**: `~/.claude/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY for all content skills
- **Guidebooks are NOT authoritative sources**: Never cite BARMM guidebooks as primary sources for factual claims. They are in development and may contain errors. Trace all factual claims back to enacted law, BOL, BAA, BDP, or official documents.

## Constitution Archive
- `legislation/Constitution/` — 1987 Philippine Constitution scraped from lawphil.net
- **INDEX.md** — index with links to the Constitution text
- **Vault symlink**: `~/Vault/Ph-Laws/Constitution/`
- **Scraper**: `scripts/scrape_constitution.py`

## Executive Orders Archive
- `legislation/executive-orders/` — 2,572 Executive Orders (1987-2025) scraped from lawphil.net
- **INDEX.md** — master index with year-by-year counts
- **Per-year folders**: `executive-orders/1987/` through `executive-orders/2025/`, each with INDEX.md
- **File naming**: `EO-{number}.md`
- **Vault symlink**: `~/Vault/Ph-Laws/executive-orders/`
- **Scraper**: `scripts/scrape_executive_orders.py --year YYYY`

## Jurisprudence Archive
- `jurisprudence/` — 38,857 Supreme Court decisions (1987-2025) scraped from lawphil.net
- **INDEX.md** — master index with year-by-year counts and links
- **Per-year folders**: `jurisprudence/1987/` through `jurisprudence/2025/`, each with its own INDEX.md
- **File naming**: `GR-{number}.md`, `AM-{identifier}.md`, `AC-{number}.md`, `BM-{number}.md`
- **Metadata**: case number, title, date, ponente, division, source URL + full verbatim decision text
- **Vault symlink**: `~/Vault/Ph-Laws/jurisprudence/`
- **MISSING.md**: 214 decisions listed on lawphil but returning 404 (documented)
- **Scraper**: `scripts/scrape_jurisprudence.py --year YYYY [--month mon]`

## Bangsamoro Content Pipeline
For any Bangsamoro governance transcript or document:
1. `/bangsamoro` — invoke FIRST to load domain context (officials, governance, BOL)
2. `/youtube-transcriber` — transcribe with name verification against officials reference
3. `/fact-checker` — runs automatically after transcription (built into workflow)
4. `/humanizer` — optional, for converting to prose format

## Legal Reference Pipeline (MANDATORY for all legal content)
For legal references, legal memos, legal opinions, legislative briefers, and any document with legal claims:
1. `/prompter` — refine what we're researching (which power, which aspects, which questions)
2. `/plan` — design the research strategy (which local files to read, which INDEX terms to search, which BOL articles are relevant)
3. `/legal-researcher REFERENCE` — execute the research (local source files + verified online sources ONLY — NEVER training data)
4. `/legal-assistant REFERENCE` — write the document (evidence-first — every claim cites a local file path or verified URL)
5. `/legal-reviewer QA-REVIEW` — review every Q&A pair (6 dimensions: Relevance, Evidence, Verbatim, Inclusiveness, Assumptions, Effectiveness)
6. `/fact-checker` — final P0-P10 verification

**No training data for legal claims.** If a claim cannot be sourced from a local file or verified URL, mark it `[UNVERIFIED]`. Training data produces hallucinations — fabricated BAA numbers, fiqh terms presented as enacted law, wrong article citations.

## Video Transcripts
- Transcripts live in transcripts/ organized by topic subfolder
- Topic subfolders: ai-claude-code/, ai-claude-cowork/, ai-design/, ai-engineering/, bangsamoro-governance/, lean-startup/{business-model,mvp-and-validation,sales-and-growth,founder-mindset,startup-strategy}/
- Use /youtube-transcriber skill for all transcriptions
- Filename format: yymmdd-hhmm-title-slug.md
- Each transcript has three sections: Organized Notes (bulleted summary) + What This Means for Your Work (personalized application with "How This Can Improve Your Claude Skills and Workflows" subsection) + Transcript (verbatim [MM:SS])
- Metadata header block (before the `---` separator): Title (H1), Channel, Duration, Language, URL, Transcribed date

## Organized Notes Format
- Bold section headers by topic
- Bullet points and numbered lists — NOT paragraphs
- Bold key words for scannability
- No timestamps in notes section
- **First mention rule**: When a person is first mentioned, provide their **complete name and full position/title** (e.g., "Interim Chief Minister **Abdulraof A. Macacua**", "BTA Parliament Deputy Speaker **Atty. Nabil A. Tan**"). Subsequent mentions can use shortened forms. This applies to both Organized Notes and Transcript sections.

## Quotable Quotes
- Place quotes **inline within each speaker's section**, NOT as a separate section at the bottom
- Add up to **5 quotable quotes per speaker** under their section, labeled `*Quotable Quotes:*`
- Each quote should be **standalone and complete** — 1-3 sentences or 1-3 small paragraphs that make sense without surrounding context
- Selection criteria (meet **3+ of these**):
  - **Standalone clarity** — makes sense without surrounding context
  - **Emotional punch** — inspires, challenges, or convicts
  - **Policy significance** — announces a decision, commitment, or direction
  - **Quotable length** — fits in a social media post (1-5 sentences)
  - **Attributable** — clearly said by a named speaker with a title
  - **Shareable** — would make someone stop scrolling
- Format: blockquote with timestamp (attribution comes from the section header)
  ```
  *Quotable Quotes:*

  > "Quote text here. Can be multiple sentences for completeness." [MM:SS]

  > "Another standalone quote." [MM:SS]
  ```
- Clean up filler words and minor grammar — preserve the speaker's voice but make it read well on social media

## Claude Desktop Cowork Documents
- Path: `~/Library/Application Support/Claude/local-agent-mode-sessions/`
- Draft bills and analysis documents from Claude Desktop sessions live here
- Example: Bangsamoro ECCD Bill and Localization Analysis in session `a64cd36d-ce2e-4ca8-b5fb-9e609ea531d3`

## Local Reference Files (Tier 1 Sources)
These files are authoritative local sources. Check them BEFORE running web searches:
- `legislation/Constitution/1987-constitution.md` — 1987 Constitution of the Republic of the Philippines
- `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` — Republic Act 11054 (Bangsamoro Organic Law) verbatim transcription (5 chapter files)
  - Fallback: `source-pdfs/other/RA 11054.pdf` (original PDF if transcription is incomplete)
- `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` — 2nd Bangsamoro Development Plan 2023-2028 (15 chapters)
- `source-pdfs/other/Parliament-and-Committee-2025.pdf` — BTA Parliament and Committee assignments
- `.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md` — Verified BARMM officials

## Transcript Language Rules
- Only **English, Filipino, and Arabic** are expected languages in Bangsamoro transcripts
- Remove garbled characters from other scripts (Thai, Bengali, Hindi, etc.) — these are auto-caption noise
- When Arabic text appears in the transcript, provide an **English translation** in brackets immediately after (e.g., `[Translation: O Allah, guide our leaders...]`)
- Arabic prayers, Quranic verses, and formal Islamic greetings should be preserved in Arabic with translation

## Lab Notes

When you make a mistake or try an approach that fails, append it below with the date, what was tried, and why it failed. Keep entries to 1-2 lines each. This section is auto-maintained — do not delete entries.
