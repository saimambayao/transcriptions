# Universal Verification Framework — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the three-layer verification framework (Prevent, Detect, Confirm) by enhancing the existing `/fact-checker` skill, creating a reference document, and updating all content skills to use the framework.

**Architecture:** One reference document defines the framework. The `/fact-checker` skill is enhanced with 6 new capabilities. Each content skill gets a one-line addition pointing to the framework. Global CLAUDE.md gets a verification rule. Memory persists the framework across projects.

**Design spec:** `docs/superpowers/specs/2026-03-27-verification-framework-design.md`

---

## Task 1: Create the Verification Framework Reference Document

**Files:**
- Create: `~/.claude/skills/fact-checker/references/verification-framework.md`

This is the canonical document that all skills read. It contains the taxonomy, the three layers, the source paths, the subagent template, and the known fabrication patterns.

- [ ] **Step 1: Read the design spec** at `docs/superpowers/specs/2026-03-27-verification-framework-design.md` — Sections 1, 2, and 3 contain the content for this file.

- [ ] **Step 2: Read the current error log** at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` — extract the 10 known fabrication patterns with correct/incorrect examples.

- [ ] **Step 3: Write the reference document** to `~/.claude/skills/fact-checker/references/verification-framework.md`

Structure:

```markdown
# Universal Verification Framework

## Verification Taxonomy (P1-P10)
[The priority table from design spec Section 1 — all 10 categories with authoritative source paths]

## Known Fabrication Patterns
[The 10 patterns from the error log with wrong/correct columns — BOL article swaps, BAA fabrications, ministry abbreviations, Sulu status, Shari'ah court, ARMM date, program names, priority code count, BEZA source, section numbering]

## Authoritative Source File Paths
[The canonical file path table from design spec Section 2, Layer 1 — BOL, BAAs, BDP, officials, MOA structure, error log, author bio]

## Three-Layer Protocol

### Layer 1: PREVENT (before writing)
[Steps 1a-1f from design spec]

### Layer 2: DETECT (after writing)
[Steps 2a-2j from design spec]

### Layer 3: CONFIRM (before publishing)
[Steps 3a-3f from design spec]

## Depth by Output Type
[The scaling table from design spec Section 3]

## Subagent Prompt Template
[The mandatory prompt inclusion block from design spec Section 2]

## Ministry Abbreviation Whitelist
MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC
[Full names for each]

## BOL 18-Article Map
[Complete article-to-content mapping from the error log — Art. I through Art. XVIII with correct content for each]
```

- [ ] **Step 4: Verify the reference document** — check that every file path in the "Authoritative Source File Paths" table actually exists. Run `ls` on each path.

---

## Task 2: Enhance the `/fact-checker` Skill

**Files:**
- Modify: `~/.claude/skills/fact-checker/SKILL.md`

The existing skill has 7 verification categories and a 4-step workflow. We add 6 new capabilities and restructure the workflow to follow the P1-P10 priority order.

- [ ] **Step 1: Read the current skill** at `~/.claude/skills/fact-checker/SKILL.md` (194 lines). Understand the existing structure: When to Use, Verification Categories, Source Priority, Workflow (4 steps), Rules, Common Errors, Integration.

- [ ] **Step 2: Add the framework reference instruction** — at the top of the skill (after the frontmatter), add:

```markdown
## Verification Framework

This skill implements the Universal Verification Framework. Before running, read
`${CLAUDE_SKILL_DIR}/references/verification-framework.md` for the full protocol,
taxonomy (P1-P10), known fabrication patterns, and authoritative source paths.
```

- [ ] **Step 3: Update the Verification Categories table** — replace the existing 7-category table with the P1-P10 taxonomy from the framework:

| Priority | Category | What to Check | Authoritative Source |
|----------|----------|--------------|---------------------|
| P1 | Constitutional provisions | Article, section numbers; verbatim text | Constitution transcription |
| P2 | BOL provisions | Article (18 total), section numbers | `bol-key-provisions.md`, BOL transcription |
| P3 | Legislative references | BAA/RA/Resolution number-to-title mapping | `baa-quick-reference.md`, `INDEX.md` |
| P4 | Verbatim legal text | Word-for-word accuracy | BOL/BAA/RA source transcriptions |
| P5 | Proper nouns — persons | Names, titles, positions | `barmm-officials-2025-2026.md` |
| P6 | Proper nouns — institutions | Ministry names, abbreviations | `moa-structure.md`, whitelist |
| P7 | Statistical data | Percentages, ratios, counts | BDP chapter summaries, PSA |
| P8 | Temporal claims | Outdated facts | Error log patterns |
| P9 | Attributed frameworks | Author/framework names | Source material |
| P10 | Other factual claims | Dates, events, places | Multiple sources |

- [ ] **Step 4: Add the 6 new capabilities** to the Workflow section. Insert after the existing Step 1 (Scan) and before Step 2 (Verify). These are NEW verification sub-steps:

**New Sub-Step 1a: BAA Cross-Reference Check**
```
Extract every "BAA No. N" or "BAA N" reference from the document.
For each, read ~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md
and verify the number matches the claimed title.
Report: MATCH / MISMATCH (with correct title) / NOT_FOUND
```

**New Sub-Step 1b: BOL Article Map Verification**
```
Extract every BOL article/section citation.
Verify against the 18-article map in the verification framework reference.
Flag known dangerous swaps:
- Art. IX vs Art. X (Basic Rights vs Shari'ah/Justice)
- Art. V vs Art. VI (Powers vs Intergovernmental)
- Art. VII vs Art. VIII (Parliament vs Wali)
- Art. VIII vs Art. XVI (Wali vs Transition)
- Art. XII Sec. 9 vs Secs. 15-16 (Block Grant location)
```

**New Sub-Step 1c: Known Error Pattern Scan**
```
Read ~/Vault/skill-outputs/fact-checker/fact-check-error-log.md
Scan the document for any text matching documented patterns:
- Sulu listed as province without SC ruling caveat
- "Shari'ah Appellate Court" (should be "Shari'ah High Court")
- ARMM creation attributed to 1996 FPA (should be RA 6734, 1989)
- "OHRAORA" (should be "ORAOHRA")
- Ministry abbreviations not in whitelist
- Priority code count != 7
- BEZA attributed to a BAA (created by BOL Art. XII Sec. 6)
Flag with: "KNOWN ERROR PATTERN: [pattern name]"
```

**New Sub-Step 1d: Ministry Abbreviation Whitelist**
```
Extract every ministry abbreviation from the document.
Accept ONLY: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA,
             MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC
Flag any variant: MOL→MOLE, MST→MOST, MPWH→MPW, etc.
```

**New Sub-Step 1e: Citation Completeness Check**
```
Scan body text (not footnote definitions) for:
- Percentages (N%)
- Named persons with titles
- BAA/BOL/RA references
- Specific dates
Flag any that appear without a [^N] footnote on the same sentence.
Report: "[stat/name/ref] on line N has no footnote"
```

**New Sub-Step 1f: Temporal Validation**
```
Scan for known temporal issues from the error log:
- "Sulu" mentioned as BARMM territory without caveat → flag
- "6 provinces" → should be 5 (after Sulu exclusion)
- Official names/titles that may have changed since reference file date
- BAA count > 89 → verify (may be fabricated)
- "ARMM" with creation context → verify date is 1989/RA 6734
Flag with: "TEMPORAL: [description] — verify currency"
```

- [ ] **Step 5: Update the report format** — change Step 4 (Generate Verification Report) to organize findings by P1-P10 priority with severity labels:

```markdown
## Verification Report

**Document**: [filename]
**Checked**: [date]
**Framework**: Universal Verification Framework v1.0

### Summary
| Severity | Count |
|----------|-------|
| CRITICAL (P1-P4) | N |
| HIGH (P5-P8) | N |
| MEDIUM (P9-P10) | N |
| VERIFIED | N |
| Total claims | N |

### P1: Constitutional Provisions
[findings]

### P2: BOL Provisions
[findings]

### P3: Legislative References
| BAA/RA | Claimed Title | Actual Title | Status |
|--------|-------------|-------------|--------|

### P4: Verbatim Legal Text
[findings]

[... P5 through P10 ...]

### Citation Completeness
| Line | Claim | Footnote Status |
|------|-------|----------------|

### Known Error Patterns Detected
| Pattern | Location | Details |
|---------|----------|---------|
```

- [ ] **Step 6: Add the error log update instruction** — after the report is generated, add:

```markdown
### Step 5: Update Error Log

After fact-checking, if NEW error patterns are discovered (not already in the log):
1. Append to ~/Vault/skill-outputs/fact-checker/fact-check-error-log.md
2. Categorize under existing pattern or create new pattern entry
3. Include: document name, what was wrong, what is correct, source
```

- [ ] **Step 7: Update the Integration table** — add `/guidebook-writer` Phase 4b to the integration list. Update the table to note that fact-checker now implements the full P1-P10 verification framework.

---

## Task 3: Update Content Skills — Add Framework Reference

**Files:**
- Modify: `~/.claude/skills/guidebook-writer/skill.md`
- Modify: `~/.claude/skills/bill-drafter/skill.md`
- Modify: `~/.claude/skills/resolution-drafter/skill.md`
- Modify: `~/.claude/skills/speech-writer/skill.md`
- Modify: `~/.claude/skills/legislative-briefer/skill.md`
- Modify: `~/.claude/skills/policy-recommendation/skill.md`
- Modify: `~/.claude/skills/training-assistant/skill.md`
- Modify: `~/.claude/skills/csw/skill.md`
- Modify: `~/.claude/skills/youtube-transcriber/skill.md`
- Modify: `~/.claude/skills/content-research-writer/skill.md`
- Modify: `~/.claude/skills/policy-paper/skill.md`
- Modify: `~/.claude/skills/mop/skill.md`

Each skill gets a one-block addition. The block varies by output type (full/standard/light verification depth).

- [ ] **Step 1: Read the design spec Section 4** (Skill Integration Map) for the exact integration pattern per skill.

- [ ] **Step 2: For each FULL-depth skill** (`/guidebook-writer`, `/bill-drafter`, `/resolution-drafter`, `/legislative-briefer`, `/policy-recommendation`, `/csw`, `/policy-paper`), add this block at the appropriate location (after the skill's "When to Use" section or before its workflow begins):

```markdown
## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.claude/skills/fact-checker/references/verification-framework.md` for the full protocol.

**Before writing (PREVENT):**
1. Invoke `/bangsamoro` to load domain context
2. Read the fact-check error log
3. Fast research: check for recent developments on the topic
4. Read authoritative reference files relevant to the topic
5. Build a Fact Sheet from verified sources (sole source of truth for writing)
6. Include Fact Sheet + fabrication warnings in all subagent prompts

**After writing (DETECT):**
Invoke `/fact-checker` on the complete document. The enhanced fact-checker runs P1-P10 checks automatically.

**Before publishing (CONFIRM):**
Present the fact-check report to the user. Fix all CRITICAL and HIGH errors. Regenerate output only after report is clean.
```

- [ ] **Step 3: For each STANDARD-depth skill** (`/speech-writer`, `/training-assistant`, `/mop`), add:

```markdown
## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.claude/skills/fact-checker/references/verification-framework.md` for the full protocol.

**Before writing (PREVENT):**
1. Invoke `/bangsamoro` to load domain context
2. Read the fact-check error log
3. Read authoritative reference files relevant to the topic

**After writing (DETECT):**
Invoke `/fact-checker` on the complete document.

**Before delivery (CONFIRM):**
Present the fact-check report to the user. Fix all errors before delivery.
```

- [ ] **Step 4: For each LIGHT-depth skill** (`/youtube-transcriber`, `/content-research-writer`), add:

```markdown
## Verification Protocol

**After output (DETECT):**
Invoke `/fact-checker` to verify names and institutions. For transcripts, verify all person names against `barmm-officials-2025-2026.md`.

**Before publishing (CONFIRM):**
Present verification results to the user.
```

- [ ] **Step 5: Verify all modifications** — for each modified skill, confirm the verification block was added and doesn't conflict with existing content.

---

## Task 4: Update Global CLAUDE.md

**Files:**
- Modify: `~/.claude/CLAUDE.md`

- [ ] **Step 1: Read the current Global CLAUDE.md** at `~/.claude/CLAUDE.md`.

- [ ] **Step 2: Add a Verification section** under the existing "## Verify Before Claiming" section. Add:

```markdown
## Universal Verification Framework
- ALL content that makes factual claims must follow the three-layer protocol: PREVENT → DETECT → CONFIRM
- Read `~/.claude/skills/fact-checker/references/verification-framework.md` for the full framework
- PREVENT: load references + fast research + build fact sheet BEFORE writing
- DETECT: run `/fact-checker` AFTER writing (covers P1-P10 taxonomy automatically)
- CONFIRM: present report to user, fix errors, regenerate output
- Every subagent prompt for BARMM content MUST include: reference file paths, fabrication warnings, [UNVERIFIED] rule
- Known fabrication patterns (BOL article swaps, BAA number inventions, ministry abbreviation errors) are documented in the fact-check error log — read it before any BARMM writing
```

---

## Task 5: Save Memory + Update Vault

**Files:**
- Create or modify: `~/.claude/projects/-Users-saidamenmambayao-apps-transcriptions/memory/feedback_verification_framework.md`
- Modify: `~/.claude/projects/-Users-saidamenmambayao-apps-transcriptions/memory/MEMORY.md`
- Create: `~/Vault/reference/verification-framework-summary.md`

- [ ] **Step 1: Create the memory file** at `~/.claude/projects/-Users-saidamenmambayao-apps-transcriptions/memory/feedback_verification_framework.md`:

```markdown
---
name: Universal Verification Framework
description: Three-layer verification (Prevent-Detect-Confirm) for ALL content requiring accuracy; enhanced /fact-checker covers P1-P10 taxonomy
type: feedback
---

All content that makes factual claims must follow the Universal Verification Framework.

**Why:** 50 documented errors across 6 guidebooks (31 critical). AI fabricates BAA numbers, BOL articles, ministry abbreviations, and program names — then /citation formats them into authoritative-looking footnotes. The same patterns recur independently across documents.

**How to apply:**
1. PREVENT: Before writing, invoke /bangsamoro + read error log + fast research + build fact sheet + include verification template in subagent prompts
2. DETECT: After writing, invoke /fact-checker (enhanced with P1-P10 checks, BAA cross-reference, BOL article map, known pattern scan, ministry whitelist, citation completeness, temporal validation)
3. CONFIRM: Present report to user, fix all CRITICAL/HIGH errors, regenerate output

**Reference document:** ~/.claude/skills/fact-checker/references/verification-framework.md
**Error log:** ~/Vault/skill-outputs/fact-checker/fact-check-error-log.md
```

- [ ] **Step 2: Update MEMORY.md** — add under the "Feedback — Content Quality" section:

```markdown
- [feedback_verification_framework.md](feedback_verification_framework.md) — Universal Verification Framework: Prevent-Detect-Confirm for ALL factual content; P1-P10 taxonomy in enhanced /fact-checker
```

- [ ] **Step 3: Create vault summary** at `~/Vault/reference/verification-framework-summary.md` — a concise summary of the framework for quick reference:

```markdown
---
date: 2026-03-27
tags: [reference, verification, fact-checker, framework]
---

# Universal Verification Framework — Quick Reference

Three layers: PREVENT (before writing) → DETECT (after writing) → CONFIRM (before publishing)

Ten priority categories (P1-P10): Constitution → BOL → Legislation → Verbatim text → Person names → Institution names → Statistics → Temporal claims → Frameworks → Other claims

Full framework: [[~/.claude/skills/fact-checker/references/verification-framework.md]]
Error log: [[skill-outputs/fact-checker/fact-check-error-log.md]]
Design spec: [[~/apps/transcriptions/docs/superpowers/specs/2026-03-27-verification-framework-design.md]]
```

---

## Task 6: Sync to Skills Bucket + Vault Archive

**Files:**
- Sync: `~/.claude/skills/fact-checker/` → `~/apps/skills-bucket/fact-checker/`
- Sync: `~/.claude/skills/fact-checker/` → `~/Vault/Claude-Skills/fact-checker/`
- Modify: `~/Vault/Claude-Skills/USAGE-GUIDE.md`

- [ ] **Step 1: Copy enhanced SKILL.md** to skills-bucket:
```bash
cp ~/.claude/skills/fact-checker/SKILL.md ~/apps/skills-bucket/fact-checker/SKILL.md
```

- [ ] **Step 2: Copy references** to skills-bucket:
```bash
cp -r ~/.claude/skills/fact-checker/references/ ~/apps/skills-bucket/fact-checker/references/
```

- [ ] **Step 3: Sync to vault archive**:
```bash
cp ~/.claude/skills/fact-checker/SKILL.md ~/Vault/Claude-Skills/fact-checker/skill.md
cp -r ~/.claude/skills/fact-checker/references/ ~/Vault/Claude-Skills/fact-checker/references/
```

- [ ] **Step 4: Update USAGE-GUIDE.md** — find the `/fact-checker` entry and update its description to mention the Universal Verification Framework and P1-P10 taxonomy.

---

## Summary

| Task | Deliverable | Est. Time |
|------|-------------|-----------|
| 1 | Reference document (`verification-framework.md`) | 15 min |
| 2 | Enhanced `/fact-checker` skill (6 new capabilities) | 20 min |
| 3 | 12 content skills updated with framework reference | 15 min |
| 4 | Global CLAUDE.md updated | 5 min |
| 5 | Memory + vault saved | 5 min |
| 6 | Skills-bucket + vault archive synced | 5 min |
| **Total** | **6 deliverables** | **~65 min** |

## Execution Notes

- Tasks 1 and 2 must be done sequentially (Task 2 references Task 1's output)
- Task 3 can be parallelized (12 skills are independent)
- Tasks 4, 5, 6 can be parallelized after Tasks 1-3 complete
- No code to test — this is all reference documentation and skill instructions
- The verify-references.py script already exists and works; its logic is referenced by the enhanced /fact-checker but the script itself is not modified
