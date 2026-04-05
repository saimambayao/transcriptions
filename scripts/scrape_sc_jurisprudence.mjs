#!/usr/bin/env node
/**
 * SC Jurisprudence Scraper
 * Downloads and transcribes Supreme Court decisions from sc.judiciary.gov.ph
 * Uses the WordPress REST API for discovery. No browser window needed —
 * Playwright request context handles HTTP.
 *
 * Usage:
 *   node scripts/scrape_sc_jurisprudence.mjs --year 2024
 *   node scripts/scrape_sc_jurisprudence.mjs --year 2024 --dry-run
 *   node scripts/scrape_sc_jurisprudence.mjs --year 2024 --no-transcribe
 *
 * Options:
 *   --year <YYYY>        Year to scrape (required). Supported: 2021-2026.
 *   --dry-run            List posts to download without downloading anything.
 *   --no-transcribe      Download PDFs only; skip text extraction and .md generation.
 *   --limit <N>          Stop after N posts (for testing).
 *   --help               Show this help.
 *
 * Output structure:
 *   jurisprudence/{year}/pdf/{CASE-ID}.pdf     — downloaded PDF
 *   jurisprudence/{year}/{CASE-ID}.md          — transcribed markdown
 *
 * Requirements:
 *   - npx playwright (playwright package installed)
 *   - python3 with pdfplumber and pymupdf
 *   - ~/.claude/skills/transcriber/scripts/assess_pdf.py
 *   - ~/.claude/skills/transcriber/scripts/extract_text_only.py
 *   - ~/.claude/skills/transcriber/scripts/extract_chapter.py
 */

import { request as playwrightRequest } from '/Users/saidamenmambayao/.nvm/versions/node/v22.17.0/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';
import { spawnSync } from 'child_process';
import { fileURLToPath } from 'url';
import os from 'os';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '..');
const TRANSCRIBER_SCRIPTS = path.join(os.homedir(), '.claude/skills/transcriber/scripts');

// ── WordPress category IDs per year ─────────────────────────────────────────

const CATEGORY_MAP = {
  2021: 627,
  2022: 637,
  2023: 1336,
  2024: 1409,
  2025: 1451,
  2026: 1486,
};

const API_BASE = 'https://sc.judiciary.gov.ph/wp-json/wp/v2/posts';
const RATE_LIMIT_MS = 400;

const USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';

// ── Argument parsing ─────────────────────────────────────────────────────────

const args = process.argv.slice(2);

if (args.includes('--help') || args.length === 0) {
  console.log(`SC Jurisprudence Scraper

Usage: node scripts/scrape_sc_jurisprudence.mjs --year <YYYY> [options]

Options:
  --year <YYYY>        Year to scrape. Supported: 2021-2026.
  --dry-run            List posts without downloading.
  --no-transcribe      Download PDFs only; skip markdown generation.
  --limit <N>          Stop after N posts (for testing).
  --help               Show this help.`);
  process.exit(0);
}

const yearArg = args.includes('--year') ? parseInt(args[args.indexOf('--year') + 1]) : null;
if (!yearArg || !CATEGORY_MAP[yearArg]) {
  console.error(`ERROR: --year must be one of: ${Object.keys(CATEGORY_MAP).join(', ')}`);
  process.exit(1);
}

const dryRun = args.includes('--dry-run');
const noTranscribe = args.includes('--no-transcribe');
const limitArg = args.includes('--limit') ? parseInt(args[args.indexOf('--limit') + 1]) : Infinity;

// ── Helpers ──────────────────────────────────────────────────────────────────

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Extract the case identifier from a PDF filename.
 *
 * SC PDFs use highly inconsistent naming. Strategy:
 * 1. Detect non-GR case types (AM, AC, BM, OCA, UDK) by prefix
 * 2. For all other cases: extract the first 5+ digit number as the GR number
 * 3. After the number, keep meaningful alphabetic suffixes (named opinions, opinion types)
 *    but strip page-range suffixes (e.g. -1-28), date suffixes, and -DECISION labels
 *
 * Examples:
 *   276927.pdf                               → GR-276927
 *   278353-VILLANUEVA.pdf                    → GR-278353-VILLANUEVA
 *   AM-24-01-01.pdf                          → AM-24-01-01
 *   G.R.-No.-226859.pdf                      → GR-226859
 *   G.R.-NOS.-221065-221164.pdf              → GR-221065
 *   G.R.-No.-256452.-February-25-2025-1.pdf  → GR-256452
 *   G.R.-No.184661-1-28.pdf                  → GR-184661
 *   G.R-NO.-240301.pdf                       → GR-240301
 *   G.R.-268254-2025-04-02-DECISION-1.pdf    → GR-268254
 *   G.R.-No.-260219-dis.-op.pdf              → GR-260219-DIS-OP
 *   G.R.-No.-232323-con.-op.pdf              → GR-232323-CON-OP
 */
function parseCaseId(pdfFilename) {
  const base = path.basename(pdfFilename, '.pdf');

  // Strip division/court prefix before case type detection
  // e.g. "EN-BANC-A.C.NO_.14203..." → "A.C.NO_.14203..."
  // e.g. "FIRST-DIVISION-G.R.NO_.255367..." → "G.R.NO_.255367..."
  const divPrefixRe = /^(?:EN[-_\s]BANC|FIRST[-_\s]DIVISION|SECOND[-_\s]DIVISION|THIRD[-_\s]DIVISION|FOURTH[-_\s]DIVISION|FIFTH[-_\s]DIVISION|SIXTH[-_\s]DIVISION|SEVENTH[-_\s]DIVISION|EIGHTH[-_\s]DIVISION)[-_\s]/i;
  const stripped = base.replace(divPrefixRe, '');

  // Non-GR case type prefixes: AM, AC, BM, UDK, OCA, A.M., A.C.
  // Also handles A.M.NO_.P-24-150 → AM-P-24-150 and A.C.NO_.14203 → AC-14203
  if (/^(AM[-_.]|AC[-_.]|BM[-_.]|UDK[-_.]|OCA[-_.]|A\.M\.|A\.C\.|B\.M\.|A_M_|A_C_|AMNO[-_]|ACNO[-_])/i.test(stripped)) {
    let id = stripped.toUpperCase();
    // Normalize: remove dots, replace underscores with dashes
    id = id.replace(/\./g, '').replace(/_/g, '-');
    // Remove DECISION/RESOLUTION/NOTICE/REMOVED and everything after
    // (Do NOT strip page-range numbers — AM/BM/AC case numbers often end in digits)
    id = id.replace(/[-]?(?:DECISION|RESOLUTION|NOTICE|REMOVED|DATED).*$/i, '');
    // Strip the -NO- or -NOS- infix that appears in "A.C.NO_.14203" → "ACNO-14203"
    id = id.replace(/^(AC|AM|BM|OCA|UDK)-?NOS?-/, '$1-');
    id = id.replace(/^(AC|AM|BM|OCA|UDK)NOS?-/, '$1-');
    // Clean double dashes and trailing dashes
    id = id.replace(/-{2,}/g, '-').replace(/-+$/, '');
    return { id, base };
  }

  // Extract the first 5+ digit GR case number (use stripped to skip division prefixes)
  const numMatch = stripped.match(/(\d{5,})(.*)/);
  if (!numMatch) {
    // No 5+ digit number found; use base as-is
    return { id: `GR-${base}`, base };
  }

  const num = numMatch[1];
  let rest = numMatch[2] || '';

  // Strip: leading separators/dots/spaces/underscores
  rest = rest.replace(/^[-.\s_]+/, '');

  // Strip: ISO date patterns (2025-04-02)
  rest = rest.replace(/\b\d{4}-\d{2}-\d{2}\b[-_]?/g, '');

  // Strip: month-name date patterns (February-25-2025, Feb-25-2025)
  rest = rest.replace(/\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)-\d{1,2}-\d{4}\b[-_]?/gi, '');

  // Strip: -DECISION[-N] and -RESOLUTION[-N] labels
  rest = rest.replace(/\bDECISION[-\d]*/gi, '');
  rest = rest.replace(/\bRESOLUTION[-\d]*/gi, '');

  // Strip: standalone year (e.g. "-2025")
  rest = rest.replace(/\b\d{4}\b[-_]?/g, '');

  // Clean leading/trailing separators
  rest = rest.replace(/^[-.\s_]+|[-.\s_]+$/g, '');

  // Strip "and NNNNN" consolidated case second number before page range check
  rest = rest.replace(/^and[-\s_]?\d+[-\s_]?/i, '');
  rest = rest.replace(/^[-.\s_]+|[-.\s_]+$/g, '');

  // If rest is purely digits and hyphens → page range → drop it
  if (rest !== '' && /^[\d-]+$/.test(rest)) {
    rest = '';
  }

  if (rest === '') {
    return { id: `GR-${num}`, base };
  }

  // Normalize suffix: dots/spaces → dashes, uppercase
  const suffix = rest
    .replace(/[.\s_]+/g, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-|-$/g, '')
    .toUpperCase();

  return { id: `GR-${num}-${suffix}`, base };
}

/**
 * Extract PDF URL from WordPress post content HTML.
 * Returns the first .pdf URL found.
 */
function extractPdfUrl(contentHtml) {
  const match = contentHtml.match(/https:\/\/sc\.judiciary\.gov\.ph\/wp-content\/uploads\/[\w\/\-\.]+\.pdf/);
  return match ? match[0] : null;
}

/**
 * Call Python transcriber assess_pdf.py to check if PDF has embedded text.
 * Returns true if embedded text (use extract_text_only), false if OCR needed.
 */
function assessPdf(pdfPath) {
  const result = spawnSync('python3', [
    path.join(TRANSCRIBER_SCRIPTS, 'assess_pdf.py'),
    pdfPath,
  ], { encoding: 'utf8' });

  if (result.status !== 0) {
    console.warn(`  assess_pdf failed: ${result.stderr?.trim()}`);
    return true; // default to embedded text
  }
  const output = result.stdout;
  return output.includes('has_embedded_text: True') || output.includes('Use pdfplumber');
}

/**
 * Get total page count from assess_pdf output.
 */
function getPdfPageCount(pdfPath) {
  const result = spawnSync('python3', ['-c', `
import fitz
doc = fitz.open(${JSON.stringify(pdfPath)})
print(len(doc))
doc.close()
`], { encoding: 'utf8' });
  const n = parseInt(result.stdout?.trim());
  return isNaN(n) ? 30 : n; // default 30 pages if detection fails
}

/**
 * Extract text from PDF using the appropriate transcriber script.
 * Returns extracted text string.
 */
function extractPdfText(pdfPath, hasEmbeddedText, pageCount) {
  const tmpOut = path.join(os.tmpdir(), `sc-jur-${Date.now()}.txt`);
  const script = hasEmbeddedText
    ? path.join(TRANSCRIBER_SCRIPTS, 'extract_text_only.py')
    : path.join(TRANSCRIBER_SCRIPTS, 'extract_chapter.py');

  const result = spawnSync('python3', [
    script, pdfPath, '1', String(pageCount), tmpOut,
  ], { encoding: 'utf8', timeout: 120000 });

  if (result.status !== 0) {
    console.warn(`  Text extraction failed: ${result.stderr?.trim()?.slice(0, 200)}`);
    return null;
  }

  try {
    const text = fs.readFileSync(tmpOut, 'utf8');
    fs.unlinkSync(tmpOut);
    return text;
  } catch {
    return null;
  }
}

/**
 * Parse case metadata from extracted PDF text + WP API post data.
 * postTitle is the WP API title (e.g. "276927 Janito M. Sedenio vs. People of the Philippines")
 */
function parseMetadata(rawText, postTitle, pdfUrl, postDate = null) {
  const text = rawText || '';

  // Division
  const divMatch = text.match(/\b(FIRST DIVISION|SECOND DIVISION|THIRD DIVISION|FOURTH DIVISION|FIFTH DIVISION|SIXTH DIVISION|SEVENTH DIVISION|EIGHTH DIVISION|EN BANC)\b/i);
  const division = divMatch ? divMatch[1].toUpperCase() : '[UNKNOWN]';

  // Case title: use WP API title, stripping leading case number (e.g. "276927 Foo vs Bar" → "Foo vs Bar")
  // This is more reliable than PDF text extraction
  const wpTitle = cleanHtmlTitle(postTitle);
  const caseTitle = wpTitle.replace(/^\d[\d\-,\s]*\s+/, '').trim() || wpTitle || '[UNKNOWN]';

  // Date from decision header [G.R. No. XXXXX. Month DD, YYYY] or Promulgated date
  const dateMatch = text.match(/\[\s*G\.R\.\s*No\.\s*[\d,\s]+\.\s*([A-Z][a-z]+ \d{1,2}, \d{4})\s*\]/i)
    || text.match(/\[\s*[A-Z]\.[A-Z]\.\s*No\.\s*[\d,\s]+\.\s*([A-Z][a-z]+ \d{1,2}, \d{4})\s*\]/i)
    || text.match(/Promulgated[:\s]*\n+\s*([A-Z][a-z]+ \d{1,2},?\s*\d{4})/i)
    || text.match(/\b([A-Z][a-z]+ \d{1,2}, \d{4})\b/);
  // Use post publication date (from WP API) as fallback when PDF text date is unclear
  const decisionDate = dateMatch ? dateMatch[1].trim() : postDate;

  // Ponente: look specifically for the line right after DECISION/RESOLUTION keyword
  // Pattern: DECISION\n\nLASTNAME, J.:  — \n+ separates them, name has no internal newlines
  let ponente = '[UNKNOWN]';
  const ponenteAfterDecision = text.match(
    /(?:DECISION|RESOLUTION)\s*\n+\s*([A-Z][A-Z\-\.]+(?:,\s*[A-Z]+)*)\s*,\s*(?:C\.J\.|S\.A\.J\.|J\.|JJ\.)\s*:/
  );
  const ponentePerCuriam = text.match(/\bPER CURIAM\b/i);
  if (ponenteAfterDecision) {
    ponente = ponenteAfterDecision[1].trim() + ', J.';
  } else if (ponentePerCuriam) {
    ponente = 'Per Curiam';
  } else {
    // Fallback: any line matching LASTNAME, J.: (no internal whitespace in name)
    const fallback = text.match(/\n([A-Z][A-Z\-\.]+(?:,\s*[A-Z]+)*)\s*,\s*(?:C\.J\.|S\.A\.J\.|J\.)\s*:/);
    if (fallback) ponente = fallback[1].trim() + ', J.';
  }

  // Type: Decision or Resolution
  const isResolution = text.match(/\bR\s+E\s+S\s+O\s+L\s+U\s+T\s+I\s+O\s+N\b/i)
    || (text.match(/\bRESOLUTION\b/i) && !text.match(/\bDECISION\b/i));
  const docType = isResolution ? 'Resolution' : 'Decision';

  return { division, caseTitle, decisionDate, ponente, docType };
}

function cleanHtmlTitle(html) {
  return html ? html.replace(/<[^>]+>/g, '').replace(/&#\d+;/g, '').replace(/&amp;/g, '&').trim() : '';
}

/**
 * Convert raw extracted text to blockquote markdown format.
 * Removes page markers and formats as `> line` for each line.
 */
function textToMarkdownBody(rawText) {
  if (!rawText) return '> [Text extraction failed]\n';

  const lines = rawText.split('\n');
  const cleaned = [];

  for (const line of lines) {
    // Skip page marker lines
    if (/^={10,}$/.test(line.trim())) continue;
    if (/^PAGE \d+$/.test(line.trim())) continue;

    cleaned.push(line.trimEnd());
  }

  // Collapse 3+ consecutive blank lines to 2
  const collapsed = [];
  let blankCount = 0;
  for (const line of cleaned) {
    if (line.trim() === '') {
      blankCount++;
      if (blankCount <= 2) collapsed.push('');
    } else {
      blankCount = 0;
      collapsed.push(line);
    }
  }

  // Trim leading/trailing blanks
  while (collapsed.length > 0 && collapsed[0].trim() === '') collapsed.shift();
  while (collapsed.length > 0 && collapsed[collapsed.length - 1].trim() === '') collapsed.pop();

  // Convert to blockquote
  return collapsed.map(line => line.trim() === '' ? '>' : `> ${line}`).join('\n') + '\n';
}

/**
 * Generate the full markdown for a case.
 */
function buildMarkdown(caseId, meta, bodyMarkdown, pdfUrl) {
  const { division, caseTitle, decisionDate, ponente, docType } = meta;
  const shortTitle = caseTitle.length > 80 ? caseTitle.slice(0, 80) + '...' : caseTitle;

  const dateStr = decisionDate || '[see decision text]';

  return `# ${caseId}

**${caseTitle}**

## Metadata

- **Case Title**: ${caseTitle}
- **Ponente**: ${ponente}
- **Division**: ${division}
- **Type**: ${docType}
- **Date**: ${dateStr}
- **Source**: [sc.judiciary.gov.ph](${pdfUrl})

---

${bodyMarkdown}`;
}

// ── WP API fetching ──────────────────────────────────────────────────────────

async function fetchAllPosts(apiContext, categoryId) {
  const allPosts = [];
  let page = 1;

  while (true) {
    const url = `${API_BASE}?categories=${categoryId}&per_page=100&page=${page}&_fields=id,title,date,slug,content`;
    const response = await apiContext.get(url, {
      headers: {
        'User-Agent': USER_AGENT,
        'Referer': 'https://sc.judiciary.gov.ph/',
      },
    });

    if (!response.ok()) {
      const status = response.status();
      if (status === 400 || status === 404) break; // no more pages
      throw new Error(`WP API error: HTTP ${status} on page ${page}`);
    }

    const posts = await response.json();
    if (!Array.isArray(posts) || posts.length === 0) break;

    allPosts.push(...posts);
    console.log(`  Fetched page ${page}: ${posts.length} posts (total so far: ${allPosts.length})`);

    if (posts.length < 100) break; // last page
    page++;
    await sleep(200);
  }

  return allPosts;
}

// ── Main ─────────────────────────────────────────────────────────────────────

async function main() {
  const year = yearArg;
  const categoryId = CATEGORY_MAP[year];
  const jurDir = path.join(REPO_ROOT, 'jurisprudence', String(year));
  const pdfDir = path.join(jurDir, 'pdf');

  if (!dryRun) {
    fs.mkdirSync(jurDir, { recursive: true });
    fs.mkdirSync(pdfDir, { recursive: true });
  }

  console.log(`=== SC Jurisprudence Scraper — ${year} ===`);
  console.log(`Category ID: ${categoryId}`);
  console.log(`Output: ${jurDir}`);
  console.log(`PDFs:   ${pdfDir}`);
  if (dryRun) console.log(`MODE: DRY RUN (no downloads)`);
  if (noTranscribe) console.log(`MODE: PDF-only (no markdown)`);
  console.log('');

  // Create Playwright request context
  const apiContext = await playwrightRequest.newContext({
    baseURL: 'https://sc.judiciary.gov.ph',
    extraHTTPHeaders: {
      'User-Agent': USER_AGENT,
      'Referer': 'https://sc.judiciary.gov.ph/',
    },
  });

  // Fetch all posts for this year
  console.log(`Fetching post list from WP API (category ${categoryId})...`);
  const posts = await fetchAllPosts(apiContext, categoryId);
  console.log(`\nTotal posts found: ${posts.length}`);

  // Stats
  let downloaded = 0, skipped = 0, failed = 0, transcribed = 0;
  const toProcess = posts.slice(0, limitArg);

  console.log(`\nProcessing ${toProcess.length} posts...\n`);

  for (let i = 0; i < toProcess.length; i++) {
    const post = toProcess[i];
    const contentHtml = post.content?.rendered || '';
    const pdfUrl = extractPdfUrl(contentHtml);

    if (!pdfUrl) {
      console.log(`[${i + 1}/${toProcess.length}] ${post.slug}: SKIP (no PDF URL found)`);
      skipped++;
      continue;
    }

    const pdfFilename = path.basename(pdfUrl);
    const { id: caseId } = parseCaseId(pdfFilename);
    const mdPath = path.join(jurDir, `${caseId}.md`);
    const pdfPath = path.join(pdfDir, pdfFilename);

    // Skip if markdown already exists
    if (fs.existsSync(mdPath)) {
      console.log(`[${i + 1}/${toProcess.length}] ${caseId}: SKIP (already exists)`);
      skipped++;
      continue;
    }

    if (dryRun) {
      console.log(`[${i + 1}/${toProcess.length}] ${caseId}: WOULD DOWNLOAD ${pdfUrl}`);
      continue;
    }

    // Download PDF if not already present
    let pdfDownloaded = false;
    if (!fs.existsSync(pdfPath)) {
      process.stdout.write(`[${i + 1}/${toProcess.length}] ${caseId}: Downloading PDF...`);
      try {
        const pdfResp = await apiContext.get(pdfUrl);
        if (!pdfResp.ok()) {
          throw new Error(`HTTP ${pdfResp.status()}`);
        }
        const pdfBuffer = await pdfResp.body();
        fs.writeFileSync(pdfPath, pdfBuffer);
        pdfDownloaded = true;
        process.stdout.write(` ${Math.round(pdfBuffer.length / 1024)}KB`);
      } catch (err) {
        console.log(` FAILED: ${err.message}`);
        failed++;
        await sleep(RATE_LIMIT_MS);
        continue;
      }
    } else {
      pdfDownloaded = true;
      process.stdout.write(`[${i + 1}/${toProcess.length}] ${caseId}: PDF exists`);
    }

    downloaded++;

    // Transcribe
    if (!noTranscribe && pdfDownloaded) {
      process.stdout.write(' → Assessing...');
      const hasEmbeddedText = assessPdf(pdfPath);
      const pageCount = getPdfPageCount(pdfPath);
      const method = hasEmbeddedText ? 'pdfplumber' : 'OCR';
      process.stdout.write(` ${pageCount}pp/${method} → Extracting...`);

      const rawText = extractPdfText(pdfPath, hasEmbeddedText, pageCount);
      if (!rawText) {
        console.log(' FAILED (extraction)');
        failed++;
        await sleep(RATE_LIMIT_MS);
        continue;
      }

      const postTitle = cleanHtmlTitle(post.title?.rendered || '');
      const postDate = post.date ? new Date(post.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }) : null;
      const meta = parseMetadata(rawText, postTitle, pdfUrl, postDate);
      const body = textToMarkdownBody(rawText);
      const markdown = buildMarkdown(caseId, meta, body, pdfUrl);

      fs.writeFileSync(mdPath, markdown, 'utf8');
      transcribed++;
      console.log(` DONE (${meta.division}, ${meta.ponente})`);
    } else {
      console.log(' DONE (PDF only)');
    }

    await sleep(RATE_LIMIT_MS);
  }

  await apiContext.dispose();

  // Summary
  console.log('\n=== Summary ===');
  console.log(`Year:        ${year}`);
  console.log(`Found:       ${posts.length} posts`);
  console.log(`Downloaded:  ${downloaded}`);
  console.log(`Transcribed: ${transcribed}`);
  console.log(`Skipped:     ${skipped}`);
  console.log(`Failed:      ${failed}`);
  console.log('');
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});
