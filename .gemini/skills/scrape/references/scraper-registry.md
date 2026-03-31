# Scraper Registry

All existing scrapers in this repository. When running `/scrape RUN`, match the user's request to the correct entry.

## Active Scrapers

| Name | Script | Source | Output Dir | File Count | CLI Usage |
|------|--------|--------|------------|------------|-----------|
| `republic-acts` | `scripts/scrape_lawphil.py` | lawphil.net | `legislation/national-laws/` | 11,866 RAs | `python3 scripts/scrape_lawphil.py --start-ra 12300 --end-ra 12313` |
| `jurisprudence` | `scripts/scrape_jurisprudence.py` | lawphil.net | `jurisprudence/` | 38,857 decisions | `python3 scripts/scrape_jurisprudence.py --year 2024 [--month jan]` |
| `executive-orders` | `scripts/scrape_executive_orders.py` | lawphil.net | `legislation/executive-orders/` | 2,572 EOs | `python3 scripts/scrape_executive_orders.py --year 2024` |
| `quran` | `scripts/scrape_quran.py` | api.quran.com (v4) | `shari'ah/quran/` | 114 surahs | `python3 scripts/scrape_quran.py` |
| `quran-metadata` | `scripts/update_quran_metadata.py` | api.quran.com (v4) | `shari'ah/quran/` | updates 114 files | `python3 scripts/update_quran_metadata.py` |
| `quran-tafsir` | `scripts/append_quran_tafsir.py` | api.quran.com (v4) | `shari'ah/quran/` | appends to 114 files | `python3 scripts/append_quran_tafsir.py` |
| `hadith-bukhari` | `scripts/process_bukhari.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/bukhari/` | 97 books | `python3 scripts/process_bukhari.py` |
| `hadith-muslim` | `scripts/process_muslim.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/muslim/` | 57 books | `python3 scripts/process_muslim.py` |
| `hadith-nasai` | `scripts/process_nasai.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/nasai/` | 51 books | `python3 scripts/process_nasai.py` |
| `hadith-abudawud` | `scripts/process_abudawud.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/abudawud/` | 43 books | `python3 scripts/process_abudawud.py` |
| `hadith-tirmidhi` | `scripts/process_tirmidhi.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/tirmidhi/` | 49 books | `python3 scripts/process_tirmidhi.py` |
| `hadith-ibnmajah` | `scripts/process_ibnmajah.py` | hadith-api (fawazahmed0) CDN | `shari'ah/hadith/ibnmajah/` | 38 books | `python3 scripts/process_ibnmajah.py` |

## Scraper Dependencies

All scrapers require Python 3 with:
- `requests` — HTTP client
- `beautifulsoup4` — HTML parsing (lawphil scrapers only)
- `markdownify` — HTML-to-markdown conversion (lawphil scrapers only)

Install: `pip3 install requests beautifulsoup4 markdownify`

## Scraper Patterns (Template for CREATE Mode)

Every scraper in this repo follows these conventions:

### Structure
```
1. Index phase — discover all items (year page, API listing, sitemap)
2. Download phase — fetch each item with retry logic
3. Transform phase — extract metadata + body, convert to markdown
4. Save phase — write markdown file with metadata header
5. Index generation — generate INDEX.md for the collection
```

### Mandatory Features
- **Skip-if-exists**: Check `os.path.exists(filepath)` and file size > threshold before downloading
- **Rate limiting**: `time.sleep(0.1)` minimum between requests
- **Retry logic**: 3 attempts per item, handle 404s gracefully (skip, don't fail)
- **Progress logging**: `[N/total] item_name: status` format
- **User-Agent header**: Set a browser-like User-Agent string
- **Session reuse**: Use `requests.Session()` for connection pooling

### Markdown Output Format
```markdown
# [Item Title]

**[Long title or description if available]**

## Metadata

- **[ID Field]**: [value]
- **Date**: [value]
- **Source**: [url]

---

[Body content in markdown]
```

### INDEX.md Format
```markdown
# [Collection Title]

Total: [N] items

## [Group heading] ([count])

- [Item link](filename.md) — [brief description]
```

## Vault Integration

After scraping, each collection should have:

| Item | Pattern | Example |
|------|---------|---------|
| Vault symlink | `~/Vault/[category]/[name]/` → output dir | `~/Vault/Ph-Laws/republic-acts/` |
| CLAUDE.md section | Archive description with file counts, naming, scraper usage | See existing sections |
| GEMINI.md section | Same content as CLAUDE.md section | Kept in sync |
| source-preload-protocol.md | Row in Tier 1 source table | Path + description |
| search-strategy.md | Row in Tier 1 sources | Path + search instructions |
