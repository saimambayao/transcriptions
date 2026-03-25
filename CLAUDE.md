# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
A documentation and transcription repository — no build system, no tests. Content is markdown files organized by topic. Python scripts are standalone utilities (run with `python3 <script>.py`).

### Repository Structure
- `docs/video-transcripts/` — YouTube video transcripts organized by topic subfolder
- `docs/` (other) — Legislative documents: BAAs, Bills, Resolutions, national laws, BDP chapters
- `PDFs/` — Source PDF documents (Parliament assignments, RA 11054, etc.)
- `PR-1-70/` — Parliamentary records
- Root `.py` files — standalone utilities for markdown processing (no dependencies beyond stdlib)

### Python Utilities
- `generate_indexes.py` — generates index files from legislative markdown documents
- `standardize_md.py` — standardizes markdown formatting across files
- `apply_standardization.py` — batch applies standardization rules
- `audit_files.py` / `debug_baa.py` — diagnostic scripts for content auditing

## Bangsamoro Content Pipeline
For any Bangsamoro governance transcript or document:
1. `/bangsamoro` — invoke FIRST to load domain context (officials, governance, BOL)
2. `/youtube-transcriber` — transcribe with name verification against officials reference
3. `/fact-checker` — runs automatically after transcription (built into workflow)
4. `/humanizer` — optional, for converting to prose format

## Video Transcripts
- Transcripts live in docs/video-transcripts/ organized by topic subfolder
- Topic subfolders: ai-engineering/, ai-design/, ai-agent/, bangsamoro-governance/, lean-startup/{business-model,mvp-and-validation,sales-and-growth,founder-mindset,startup-strategy}/
- Some transcripts sit directly in video-transcripts/ (lean-startup topic, not yet sorted into subfolders)
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
- `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` — Republic Act 11054 (Bangsamoro Organic Law) verbatim transcription (5 chapter files)
  - Fallback: `PDFs/RA 11054.pdf` (original PDF if transcription is incomplete)
- `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` — 2nd Bangsamoro Development Plan 2023-2028 (15 chapters)
- `PDFs/Parliament-and-Committee-2025.pdf` — BTA Parliament and Committee assignments
- `.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md` — Verified BARMM officials

## Transcript Language Rules
- Only **English, Filipino, and Arabic** are expected languages in Bangsamoro transcripts
- Remove garbled characters from other scripts (Thai, Bengali, Hindi, etc.) — these are auto-caption noise
- When Arabic text appears in the transcript, provide an **English translation** in brackets immediately after (e.g., `[Translation: O Allah, guide our leaders...]`)
- Arabic prayers, Quranic verses, and formal Islamic greetings should be preserved in Arabic with translation
