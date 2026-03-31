---
name: scrape
description: |
  Scrape web sources and APIs to build local markdown archives for legal research, Islamic
  scholarship, and reference materials. Two modes: (1) RUN — dispatch an existing scraper
  from the registry (republic-acts, jurisprudence, executive-orders, quran) with the right
  arguments, then run post-scrape integration. (2) CREATE — generate a new scraper script
  for a new source following established patterns (requests + BeautifulSoup/markdownify for
  HTML, JSON parsing for APIs, metadata headers, skip-if-exists, retry logic, INDEX.md
  generation), test on a small sample, full run, then post-scrape integration.
  Post-scrape integration: INDEX.md generation, vault symlink creation, CLAUDE.md/GEMINI.md
  updates, source-preload-protocol and search-strategy updates, downstream skill updates.
  Use when: "scrape", "download from", "build archive", "pull from lawphil", "scrape quran",
  "scrape hadith", "new scraper", "run scraper", "update archive", "add to legal archive",
  "scrape sunnah.com", "scrape [source]", "create scraper for", "pull jurisprudence".
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Shell
---

# /scrape — Web Source Archiver

Scrape web sources and APIs into structured local markdown archives. Runs existing scrapers or generates new ones, then integrates the output into the project's reference infrastructure.

## Role

You are a data engineering assistant specializing in scraping legal, religious, and reference sources into clean, structured markdown for offline use. You follow established patterns from 4 proven scrapers that have collectively downloaded 53,000+ documents.

## Anti-Fabrication Rule

When generating scraper code, you MUST verify the target source's actual HTML structure or API response format before writing extraction logic. Do NOT guess at CSS selectors, JSON paths, or page structure from training data. Fetch a sample page/response first, inspect it, then write the parser.

## Modes

### Mode 1: RUN (Dispatcher)

**Invoke with:** `/scrape RUN <scraper-name> [args]` or "run the [name] scraper"

**Examples:**
```
/scrape RUN republic-acts --start-ra 12314 --end-ra 12400
/scrape RUN jurisprudence --year 2026
/scrape RUN jurisprudence --year 2026 --month jan
/scrape RUN executive-orders --year 2026
/scrape RUN quran
```

**Workflow:**

1. **Match scraper** — Read `references/scraper-registry.md` to find the scraper by name
2. **Validate args** — Check required arguments are present. If missing, show the CLI usage from the registry and ask.
3. **Check dependencies** — Verify `requests`, `beautifulsoup4`, `markdownify` are installed. If not: `pip3 install requests beautifulsoup4 markdownify`
4. **Run the scraper** — Execute via Shell with the user's arguments. Stream progress.
5. **Report results** — Show success/failed/skipped counts from the scraper output.
6. **Post-scrape integration** — Run the integration checklist (see below).

**Parallel execution:** For scrapers that accept `--year`, the user may request multiple years. Suggest running multiple terminal commands in parallel (one per year).

### Mode 2: CREATE (Generator)

**Invoke with:** `/scrape CREATE <name> --source <url-or-api> --output <dir>` or "create a scraper for [source]"

**Examples:**
```
/scrape CREATE hadith --source "sunnah.com API" --output "shari'ah/hadith"
/scrape CREATE barmm-eos --source "lawphil.net BARMM executive orders" --output "legislation/barmm-executive-orders"
/scrape CREATE chanrobles-ra --source "chanrobles.com republic acts" --output "legislation/chanrobles-ra"
```

**Workflow:**

1. **Clarify the source** — Ask:
   - Is this an API (JSON) or website (HTML)?
   - What's the URL pattern? (index page, pagination, API endpoint)
   - What metadata should be extracted? (title, date, author, identifiers)
   - What's the expected scale? (dozens, hundreds, thousands)

2. **Inspect the source** — Fetch a sample page/response using Shell (`curl`) or a quick Python script. Inspect actual structure before writing any parsing logic.

3. **Select template** — Read the most similar existing scraper from `scripts/`:
   - API source → use `scrape_quran.py` as template
   - HTML source from lawphil → use `scrape_lawphil.py` as template
   - HTML source with year/month hierarchy → use `scrape_jurisprudence.py` as template
   - HTML source with year hierarchy → use `scrape_executive_orders.py` as template

4. **Generate the scraper** — Write to `scripts/scrape_<name>.py` following ALL mandatory patterns from the registry:
   - `requests.Session()` with User-Agent header
   - Skip-if-exists with file size check
   - Rate limiting (`time.sleep(0.1)` minimum)
   - Retry logic (3 attempts, graceful 404 handling)
   - Progress logging (`[N/total]` format)
   - Markdown output with metadata header + body
   - INDEX.md generation function
   - `argparse` CLI interface
   - `if __name__ == '__main__': main()` entry point

5. **Test on small sample** — Run the scraper on 3-5 items. Show the user a sample output file.

6. **User confirms format** — Wait for approval before full run.

7. **Full run** — Execute the scraper. For large collections (1000+), suggest splitting by year/chunk.

8. **Update registry** — Add the new scraper to `references/scraper-registry.md`.

9. **Post-scrape integration** — Run the integration checklist.

## Post-Scrape Integration Checklist

Run this after EVERY successful scrape (both RUN and CREATE modes). Each step is a task.

### Step 1: INDEX.md Generation
- If the scraper has a `--generate-master-index` flag, run it
- Otherwise, check if INDEX.md exists and is up-to-date with file counts
- For new scrapers, generate INDEX.md following the format in the registry

### Step 2: Vault Symlink
- Check if a symlink exists at `~/Vault/[category]/[name]/` pointing to the output directory
- If not, create it: `ln -s [output-dir] ~/Vault/[category]/[name]`
- Category mapping:
  - Philippine laws → `~/Vault/Ph-Laws/`
  - Islamic sources → `~/Vault/bangsamoro/` or `~/Vault/Islamic/`
  - Other → ask user for vault location

### Step 3: CLAUDE.md Update
- Read the current `CLAUDE.md` in the repo root
- If the archive already has a section, update file counts and any new details
- If new archive, add a section following the existing format (see Republic Acts or Jurisprudence sections as template)
- Include: description, file count, INDEX.md reference, file naming pattern, vault symlink, scraper CLI usage

### Step 4: GEMINI.md Update
- Mirror the same section to `GEMINI.md` in the repo root
- Adjust any Claude-specific paths (e.g., `~/.claude/skills/` → `~/.gemini/skills/`)

### Step 5: Source Pre-Load Protocol Update
- Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md`
- Add the new source to the Tier 1 source table if it's a primary legal/religious source

### Step 6: Search Strategy Update
- Read `~/.gemini/skills/legal-researcher/references/search-strategy.md`
- Add the new source to the appropriate tier with search instructions

### Step 7: Downstream Skill Updates
- Grep all skill SKILL.md files in `~/.gemini/skills/` for keywords related to the new source
- For each skill that references similar content, add the new source path
- Example: scraping hadith → update `/shariah`, `/citation`, `/legislative-briefer`, `/bill-drafter`, `/resolution-drafter`, `/speech-writer`, `/legal-researcher` (same skills that were updated for the Quran source)

### Step 8: Report
- Present a summary table:

```
| Step | Status | Details |
|------|--------|---------|
| INDEX.md | Done | 114 entries |
| Vault symlink | Created | ~/Vault/Islamic/quran/ |
| CLAUDE.md | Updated | Added Quran Archive section |
| GEMINI.md | Updated | Mirrored |
| source-preload | Updated | Added to Tier 1 table |
| search-strategy | Updated | Added to Islamic sources |
| Downstream skills | Updated | 7 skills updated |
```

## Scraper Code Quality Standards

Every generated scraper MUST:

1. **Be self-contained** — single Python file, no custom imports beyond standard lib + requests/bs4/markdownify
2. **Be idempotent** — safe to re-run; skip existing files, update INDEX.md
3. **Handle failures gracefully** — 404s are skipped (not failures), network errors retry 3x, final failures are logged but don't crash the run
4. **Log progress clearly** — user should see `[N/total] item: status` for every item
5. **Respect rate limits** — minimum 0.1s between requests; for APIs with documented limits, follow them
6. **Produce clean markdown** — no HTML artifacts, no excessive blank lines, no navigation cruft
7. **Include CLI help** — `python3 script.py --help` should show all options with descriptions

## Complexity Estimates

| Task | Complexity | Time |
|------|-----------|------|
| RUN existing scraper (single year) | Simple | 2-10 min (depends on source speed) |
| RUN existing scraper (all years, parallel) | Medium | 10-30 min |
| CREATE new scraper (API source) | Medium | 15-30 min (inspect + generate + test + run) |
| CREATE new scraper (HTML source) | Complex | 30-60 min (HTML is messier than APIs) |
| Post-scrape integration | Simple | 5-10 min |

## Gotchas

- **lawphil.net has no robots.txt rate limits** but will drop connections if you hammer it. Keep `time.sleep(0.1)` minimum.
- **API sources may have pagination** — always check for `next_page`, `total_pages`, or `offset` in responses. The Quran API uses `pagination.total_pages`.
- **HTML from lawphil is inconsistent across years** — the RA scraper uses regex on raw HTML (not BeautifulSoup selectors) because older pages have malformed HTML. Inspect sample pages from multiple years before committing to a parsing strategy.
- **markdownify leaves artifacts** — always post-process: strip navigation text ("The Lawphil Project", "Arellano Law Foundation"), collapse 4+ blank lines, rstrip each line.
- **File naming must be deterministic** — given the same input, the scraper must produce the same filename. This makes skip-if-exists work correctly.
- **Large collections need parallel execution** — anything over 1000 items should be split by year/chunk.

## Skill Composition

| Skill | When It's Used |
|-------|---------------|
| `/fact-checker` | After integration — verify source-preload-protocol is correctly updated |
| `/legal-researcher` | Downstream — uses archives as Tier 1 sources |
| `/shariah` | Downstream — uses Quran/Hadith archives |
| `/bangsamoro` | Downstream — uses legal archives for BAA/BOL research |
