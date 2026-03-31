# Verification Sources — Detailed Guide

## Tier 1: Local Reference Files

These are pre-verified and maintained. Always check here first.

### BARMM Officials
- **Path**: `.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`
- **Contains**: 80 current MPs, executive leadership, cabinet ministers, commission heads,
  committee chairs, auto-caption error mapping
- **Use for**: Any person name or title in Bangsamoro governance context
- **Update policy**: Add new names when verified during fact-checking

### Bangsamoro Laws Index
- **Path**: `~/Vault/bangsamoro/bangsamoro-laws/index.md`
- **Contains**: 81 BAAs with titles, dates, and brief descriptions
- **Use for**: Verifying BAA numbers, titles, and enactment dates

### e-Bangsamoro MP Names
- **Path**: `e-bangsamoro/references/MP-names.md`
- **Contains**: Canonical list of MP names for the platform
- **Use for**: Cross-referencing MP name spellings

### Bangsamoro Organic Law (Full Text — Verbatim Transcription)
- **Path**: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 markdown chapter files)
- **Contains**: Complete Republic Act 11054 — powers, territory, fiscal autonomy, transition
- **Use for**: Verifying BOL provisions, section numbers, constitutional references
- **Priority**: Check this BEFORE web searching for RA 11054 provisions
- **Fallback**: `~/apps/transcriptions/PDFs/RA 11054.pdf` (original PDF if grep misses)

### Bangsamoro Development Plan 2023-2028
- **Path**: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/`
- **Contains**: 15 chapters covering development framework, goals, strategies, targets
- **Use for**: Verifying BDP goals, statistics, macroeconomic targets, spatial strategy
- **Priority**: Check this BEFORE web searching for BDP-related claims

### Parliament and Committee Assignments
- **Path**: `~/apps/transcriptions/PDFs/Parliament-and-Committee-2025.pdf`
- **Contains**: BTA Parliament committee memberships and assignments
- **Use for**: Verifying committee chairs, membership, parliamentary structure

### /bangsamoro Skill References
- **Path**: `.gemini/skills/bangsamoro/references/`
- **Contains**: 11 reference files covering governance, BOL, geography, economy, etc.
- **Use for**: Institutional facts (ministry names, province counts, development goals)

## Tier 2: BARMM Official Websites

Use Playwright CLI (`npx playwright`) for web access. Never use Claude in Chrome tools.

### Parliament Website
- **URL**: parliament.bangsamoro.gov.ph
- **Use for**: Current MP list, committee assignments, legislation tracker
- **Reliability**: High — official source, but sometimes lags behind appointments

### BARMM Main Portal
- **URL**: bangsamoro.gov.ph
- **Use for**: Executive appointments, ministry structure, official news
- **Reliability**: High

### BARMM Government Portal
- **URL**: barmm.gov.ph
- **Use for**: Organizational structure, program information
- **Reliability**: Medium — sometimes outdated

## Tier 3: Web Search

### Philippine Government Sources
- officialgazette.gov.ph — Republic Acts, executive orders
- senate.gov.ph — national legislation
- congress.gov.ph — House bills
- lawphil.net — compiled Philippine laws

### News Sources (for dates and events)
- Bangsamoro Information Office (BIO) releases
- Philippine News Agency (PNA) — Bangsamoro desk
- MindaNews — Mindanao coverage

### Search Strategies

For **person names**:
```
"[name fragment] BARMM [year]"
"[position title] bangsamoro [year]"
"BTA member [partial name]"
```

For **legislation**:
```
"BAA No. [X] bangsamoro" OR "bangsamoro autonomy act [X]"
"Republic Act [XXXXX]"
```

For **organizations**:
```
"[org name] Philippines" OR "[org name] BARMM"
```

## Common Verification Patterns

### Auto-Caption Name Garbles
Whisper and YouTube auto-captions consistently mangle Filipino Muslim names. Common patterns:
- Missing middle initials (always check for these)
- Swapped syllables in Arabic-origin names
- "Jr." dropped or misplaced
- Titles (Atty., Dr., Prof., Engr., Hadja) omitted or garbled
- Honorifics (Sheikh, Ustadz) dropped

### Legislation Reference Errors
- BAA vs RA confusion (BAAs are Bangsamoro, RAs are national)
- Wrong section numbers (especially when cited from memory in speeches)
- Outdated act titles (some BAAs have been amended)

### Date Errors
- Fiscal year vs calendar year confusion
- "This year" vs "last year" when transcript spans December-January
- Event dates shifted by one day (timezone issues in YouTube metadata)

### Number Errors
- Budget figures without specifying currency (PHP vs USD)
- Population figures that mix province-level with region-level
- Percentage vs absolute number confusion
