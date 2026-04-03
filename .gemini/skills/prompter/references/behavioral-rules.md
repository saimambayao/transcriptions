# Behavioral Rules for /prompter

Compiled from 20+ feedback memories, error logs, lab notes, and session corrections.
Read during Phase 3 (Intent Extraction) to identify which rules apply to the current task.
This is a living document — append new rules when mistakes occur.

---

## Always (every task)

- **Pre-action gate:** Before every edit, answer: "Did the user ask for this specific change?" If not a clear yes, stop.
- **One change per cycle:** Edit → verify → report → wait for next instruction. Do not fire cascading changes.
- **Verify before claiming done:** Screenshot the PDF, read the file, check the output. Never say "done" without evidence.
- **Related issues:** When you discover a problem the user didn't ask about, TELL them. Do not silently fix it.
- **No session-end suggestions:** Never suggest ending the session, deferring to a "fresh session," or recommending a new session. The user has a 1M context window.

## When editing existing content

- **Remove = delete.** Do not replace it with something new. Do not fill the gap. If the result looks wrong, ask.
- **Rewrite = fix what is broken.** List the specific problems first. Do not add sections, restructure, or expand scope.
- **Check everything = everything.** Every paragraph, every claim, every page. Do not stop at the easy checks.
- **Fix X = change X only.** Do not also fix Y and Z "while you're at it."
- **Never change content for styling.** If asked for CSS/PDF changes, touch only CSS/HTML. If content changes are needed, explain why and get confirmation.
- **No sub-step numbering.** Never create 2b, 3b, 4b — renumber sequentially.

## When producing BARMM content

- **Read the fact-check error log FIRST:** `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` — 16 known patterns.
- **Invoke /bangsamoro** for domain context before writing.
- **"Shari'ah" not "Islamic governance."** The BOL creates Shari'ah provisions, not "Islamic governance." Never use "Islamic principles" generically.
- **Name specific audience roles.** Not "administrative staff" or "government staff." Name the people who would actually open the document and use it: bill drafters, legal researchers, policy analysts, ministry directors.
- **No internal jargon in external documents.** "Institutional boundary," "pipeline enforcement," "context rot" mean nothing to external readers. Rewrite in plain language.
- **Verify BOL articles** against the 18-article map. Most dangerous swaps: Art. IX/X, Art. V/VI, Art. VII/VIII.
- **Verify BAA numbers** against `~/Vault/bangsamoro/bangsamoro-laws/index.md`. Never trust BAA numbers from memory.
- **Verify ministry names** against the 15-ministry whitelist: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC.
- **Verify goal/framework names verbatim** against the source document. Never paraphrase BDP goal names from memory.
- **For institutional roles:** Read the creating law's exact language. Never elevate "consultative body" to "supreme authority."
- **For each article cited:** Verify it contains the claimed provision. Art. X = courts/justice only, not Hajj/halal/banking/BDI.
- **Never cite guidebooks as primary sources.** Trace all factual claims to enacted law, BOL, BAA, BDP, or official documents.

## When delivering external documents

- **Run pre-delivery scan:** Grep for banned phrases before delivering.
  - `Islamic governance|Islamic principles`
  - `guidebook series|this series`
  - `Co-Authored-By`
  - `institutional boundary|pipeline enforcement|context rot`
  - `supreme authority|sole authority` (near BARMM institutions)
  - `administrative staff|government staff` (as audience)
- **Verify author framing:** Independent practitioner, NOT the Bangsamoro Government.
- **Strip internal artifacts:** No file paths, skill names, methodology sections, error counts, pipeline steps, or QA details in published content.
- **Describe accurately what exists.** Do not claim "the draft manuscript is ready" if it's an AI-assisted working sample.
- **No drafts as policy.** Never cite internal plans as existing policy. Only cite enacted law, official regulations, published plans.

## When generating PDFs

- **Visual verification loop:** After generating any PDF, screenshot it, identify issues (layout, wrapping, overflow, missing content), fix, regenerate, screenshot again. Loop until clean.
- **Do not present to user before catching visual issues yourself.** The user should not have to send screenshots for you to find problems.
- **Tables:** Use `table-layout: auto`. Never `white-space: nowrap` on general columns.
- **Diagrams:** Use Mermaid PNG, never ASCII art.
- **Footnotes:** Separate page with page-break-before.

## When doing legal work

- **Follow the 7-step pipeline:** prompter → plan → legal-researcher → legal-assistant → legal-reviewer QA-REVIEW → fact-checker VALIDATE → deliver.
- **Run verify-references.py BEFORE /citation.** Subagents fabricate BAA numbers that /citation then makes look authoritative.
- **Legal QA loop:** Iterate until 0 CRITICAL errors. Auto-research is for skills, not legal QA.
- **Invoke /citation after EVERY chapter.** Feliciano 10th Ed. format.
- **All published docs must have footnotes.** No unfootnoted legal claims in published material.

## When citing sources

- **Never cite guidebooks as primary sources.** They are in development and may contain errors.
- **Verify BAA numbers** against the index before citing.
- **Verify BOL article numbers** against the 18-article map.
- **Mark uncitable claims `[UNVERIFIED]`** with a reason.
- **No Bernas/Golden Notes/bar review** references exposed in published documents.
- **Use only BOL terminology** for power classifications. Banned: "Exclusive," "Shared," "Concurrent."

---

*Last updated: 2026-03-31. Source: 20+ feedback memories, fact-check error log (16 patterns), session corrections (260323-260331).*
