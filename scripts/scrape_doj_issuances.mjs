#!/usr/bin/env node
/**
 * DOJ Issuances Scraper
 * Scrapes all Department Circulars from https://www.doj.gov.ph/issuances.html
 * Downloads PDFs and creates markdown metadata files.
 *
 * Usage:
 *   node scripts/scrape_doj_issuances.mjs [options]
 *
 * Options:
 *   --output <dir>       Output directory (default: legislation/issuances/doj)
 *   --profile <path>     Chrome profile directory to copy (default: ~/Library/Application Support/Google/Chrome/Default)
 *   --no-download        Skip PDF downloads, only save metadata markdown
 *   --help               Show this help message
 *
 * Requirements:
 *   - npx playwright (chromium-1208 installed)
 *   - Google Chrome installed at /Applications/Google Chrome.app
 *   - User must have previously visited doj.gov.ph to have valid cf_clearance cookie
 */

import { chromium } from '/Users/saidamenmambayao/.nvm/versions/node/v22.17.0/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import os from 'os';

// ── Configuration ─────────────────────────────────────────────────────────────

const DEFAULT_OUTPUT = path.resolve(
  path.dirname(new URL(import.meta.url).pathname),
  '../legislation/issuances/doj'
);

const DEFAULT_CHROME_PROFILE = path.join(
  os.homedir(), 'Library/Application Support/Google/Chrome/Default'
);

const DOJ_ISSUANCES_URL = 'https://www.doj.gov.ph/issuances.html';
const DOJ_BASE_URL = 'https://www.doj.gov.ph';
const RATE_LIMIT_MS = 300; // ms between PDF downloads

// ── Argument parsing ───────────────────────────────────────────────────────────

const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log(`DOJ Issuances Scraper

Usage: node scripts/scrape_doj_issuances.mjs [options]

Options:
  --output <dir>       Output directory (default: legislation/issuances/doj)
  --profile <path>     Chrome profile to copy (default: ~/Library/...Chrome/Default)
  --no-download        Skip PDF downloads
  --help               Show this help message`);
  process.exit(0);
}

const outputDir = args.includes('--output')
  ? path.resolve(args[args.indexOf('--output') + 1])
  : DEFAULT_OUTPUT;

const chromeProfileSrc = args.includes('--profile')
  ? path.resolve(args[args.indexOf('--profile') + 1])
  : DEFAULT_CHROME_PROFILE;

const skipDownload = args.includes('--no-download');

// ── Helpers ────────────────────────────────────────────────────────────────────

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function sanitizeFilename(str) {
  return str
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim()
    .substring(0, 120);
}

function parseDate(dateStr) {
  // "09 March 2026" or "09&nbsp;March&nbsp;2026" → { iso: "2026-03-09", display: "09 March 2026" }
  const cleaned = dateStr.replace(/\u00a0/g, ' ').trim();
  const months = {
    January: '01', February: '02', March: '03', April: '04',
    May: '05', June: '06', July: '07', August: '08',
    September: '09', October: '10', November: '11', December: '12'
  };
  const m = cleaned.match(/(\d{1,2})\s+(\w+)\s+(\d{4})/);
  if (!m) return { iso: null, display: cleaned };
  const day = m[1].padStart(2, '0');
  const month = months[m[2]] || '00';
  return { iso: `${m[3]}-${month}-${day}`, display: cleaned };
}

function docNumberToSlug(docNumber) {
  // "DEPARTMENT CIRCULAR NO. 010" → "DC-010"
  // "JOINT MEMORANDUM CIRCULAR NO. 001" → "JMC-001"
  // "MLACM NO. 001" → "MLACM-001"
  const n = docNumber.toUpperCase();
  if (n.includes('JOINT')) {
    const num = n.match(/NO\.\s*(\S+)/)?.[1] || '';
    return `JMC-${num}`;
  }
  if (n.includes('MLACM')) {
    const num = n.match(/NO\.\s*(\S+)/)?.[1] || '';
    return `MLACM-${num}`;
  }
  if (n.includes('DEPARTMENT CIRCULAR') || n.includes('CIRCULAR')) {
    const num = n.match(/NO\.\s*(\S+)/)?.[1] || '';
    return `DC-${num}`;
  }
  // fallback: first letters of each word + number
  const words = n.replace(/NO\.\s*/, '').split(/\s+/);
  const initials = words.slice(0, 3).map(w => w[0]).join('');
  const num = n.match(/NO\.\s*(\S+)/)?.[1] || '';
  return `${initials}-${num}`;
}

// ── Main ───────────────────────────────────────────────────────────────────────

async function main() {
  // Setup directories
  const pdfsDir = path.join(outputDir, 'pdfs');
  fs.mkdirSync(outputDir, { recursive: true });
  fs.mkdirSync(pdfsDir, { recursive: true });

  console.log('=== DOJ Issuances Scraper ===');
  console.log(`Output: ${outputDir}`);
  console.log(`PDFs: ${pdfsDir}`);
  console.log('');

  // Copy Chrome profile to avoid locking the live profile
  const tmpProfileDir = path.join(os.tmpdir(), 'doj-chrome-profile');
  if (!fs.existsSync(tmpProfileDir)) {
    console.log(`Copying Chrome profile from: ${chromeProfileSrc}`);
    try {
      execSync(`cp -r "${chromeProfileSrc}" "${tmpProfileDir}"`, { stdio: 'pipe' });
      console.log('Chrome profile copied.');
    } catch (e) {
      console.error(`Failed to copy Chrome profile: ${e.message}`);
      console.error('Proceeding without profile copy — Cloudflare may block access.');
    }
  } else {
    console.log('Using existing Chrome profile copy.');
  }

  // Launch browser
  console.log('\nLaunching browser...');
  const browser = await chromium.launchPersistentContext(tmpProfileDir, {
    headless: false,
    channel: 'chrome',
    args: [
      '--disable-blink-features=AutomationControlled',
      '--no-first-run',
      '--no-default-browser-check',
    ],
    viewport: { width: 1280, height: 720 },
    ignoreDefaultArgs: ['--enable-automation'],
  });

  const page = await browser.newPage();
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });

  // Navigate to issuances page
  console.log(`\nNavigating to ${DOJ_ISSUANCES_URL} ...`);
  try {
    await page.goto(DOJ_ISSUANCES_URL, { waitUntil: 'load', timeout: 30000 });
  } catch (e) {
    // Timeout is ok — we'll wait for Cloudflare below
  }

  // Wait for Cloudflare to pass (up to 30s)
  console.log('Waiting for Cloudflare verification...');
  let cloudflareResolved = false;
  for (let i = 0; i < 30; i++) {
    await sleep(1000);
    try {
      const title = await page.title();
      if (!title.includes('moment') && !title.includes('Cloudflare') && title.length > 5) {
        cloudflareResolved = true;
        console.log(`Cloudflare passed after ${i + 1}s. Page title: "${title}"`);
        break;
      }
    } catch (e) { /* navigation still happening */ }
  }

  if (!cloudflareResolved) {
    console.error('\nERROR: Cloudflare challenge was not resolved after 30 seconds.');
    console.error('Please ensure:');
    console.error('1. Google Chrome is installed');
    console.error('2. You have previously visited https://www.doj.gov.ph in Chrome');
    console.error('3. Your cf_clearance cookie is still valid');
    await browser.close();
    process.exit(1);
  }

  // Wait for content to fully render
  await sleep(3000);

  // ── Parse all entries ────────────────────────────────────────────────────────

  console.log('\nParsing issuance entries...');

  const entries = await page.evaluate(() => {
    const blogContent = document.querySelector('.blog-content');
    if (!blogContent) return [];

    const results = [];
    const children = Array.from(blogContent.children);

    let current = {};

    for (const el of children) {
      const tag = el.tagName.toLowerCase();
      const text = el.textContent.replace(/\u00a0/g, ' ').trim();

      if (text.startsWith('---') || text === '') continue; // separator

      if (tag === 'p' && /^\d{1,2}\s+\w+\s+\d{4}$/.test(text)) {
        // Date line
        if (current.date) results.push({ ...current });
        current = { date: text, title: '', subject: '', pdfUrl: '' };
      } else if (tag === 'h2') {
        current.title = text;
      } else if (tag === 'p' && text.startsWith('SUBJECT:')) {
        current.subject = text.replace(/^SUBJECT:\s*/, '').trim();
      } else if (tag === 'p') {
        // Check if it contains a PDF link
        const link = el.querySelector('a[href*=".pdf"], a[href*="PDF"]');
        if (link) {
          current.pdfUrl = link.href;
        }
      }
    }

    // Push last entry
    if (current.date || current.title) results.push({ ...current });

    return results;
  });

  console.log(`Found ${entries.length} entries.`);

  // ── Process entries ──────────────────────────────────────────────────────────

  let successCount = 0;
  let skipCount = 0;
  let failCount = 0;
  const indexRows = [];

  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    const { iso: dateIso, display: dateDisplay } = parseDate(entry.date);
    const year = dateIso ? dateIso.substring(0, 4) : 'unknown';
    const slug = docNumberToSlug(entry.title);
    const mdFilename = dateIso
      ? `${dateIso}-${slug}.md`
      : `${sanitizeFilename(entry.title)}.md`;

    const mdPath = path.join(outputDir, mdFilename);

    // Derive PDF filename from URL
    const pdfUrlPath = entry.pdfUrl ? new URL(entry.pdfUrl).pathname : null;
    const pdfFilename = pdfUrlPath ? path.basename(decodeURIComponent(pdfUrlPath)) : null;
    const pdfPath = pdfFilename ? path.join(pdfsDir, pdfFilename) : null;

    process.stdout.write(`[${i + 1}/${entries.length}] ${slug} (${dateDisplay}): `);

    // Write markdown metadata file
    const mdContent = [
      `# ${entry.title}`,
      '',
      `**Date:** ${dateDisplay}`,
      `**Document:** ${entry.title}`,
      entry.subject ? `**Subject:** ${entry.subject}` : '',
      entry.pdfUrl ? `**PDF:** [Download](${entry.pdfUrl})` : '',
      pdfFilename ? `**Local PDF:** pdfs/${pdfFilename}` : '',
      '',
      '---',
      '',
      entry.subject ? `## Subject\n\n${entry.subject}` : '',
      '',
      '## Transcription',
      '',
      '_Transcription pending. Run the /transcriber skill on the PDF file._',
      '',
    ].filter(line => line !== null).join('\n');

    fs.writeFileSync(mdPath, mdContent, 'utf8');

    // Download PDF
    if (!skipDownload && entry.pdfUrl && pdfPath) {
      if (fs.existsSync(pdfPath) && fs.statSync(pdfPath).size > 1000) {
        process.stdout.write('skipped (PDF exists)\n');
        skipCount++;
      } else {
        try {
          const pdfUrl = entry.pdfUrl.startsWith('/')
            ? DOJ_BASE_URL + entry.pdfUrl
            : entry.pdfUrl;

          const response = await page.request.get(pdfUrl, {
            timeout: 30000,
            headers: { Referer: DOJ_ISSUANCES_URL },
          });

          if (response.ok()) {
            const contentType = response.headers()['content-type'] || '';
            if (contentType.includes('pdf') || contentType.includes('application')) {
              const buffer = await response.body();
              fs.writeFileSync(pdfPath, buffer);
              process.stdout.write(`downloaded (${Math.round(buffer.length / 1024)}KB)\n`);
              successCount++;
            } else {
              process.stdout.write(`BLOCKED (got ${contentType})\n`);
              failCount++;
            }
          } else {
            process.stdout.write(`FAILED (HTTP ${response.status()})\n`);
            failCount++;
          }

          await sleep(RATE_LIMIT_MS);
        } catch (e) {
          process.stdout.write(`ERROR: ${e.message.substring(0, 60)}\n`);
          failCount++;
        }
      }
    } else {
      process.stdout.write('metadata only\n');
    }

    // Index row
    indexRows.push({
      date: dateIso || entry.date,
      title: entry.title,
      subject: entry.subject,
      pdfUrl: entry.pdfUrl,
      mdFile: mdFilename,
      pdfFile: pdfFilename,
    });
  }

  await browser.close();

  // ── Generate INDEX.md ────────────────────────────────────────────────────────

  console.log('\nGenerating INDEX.md...');

  const indexLines = [
    '# DOJ Issuances — Index',
    '',
    `_Source: [${DOJ_ISSUANCES_URL}](${DOJ_ISSUANCES_URL})_`,
    `_Scraped: ${new Date().toISOString().split('T')[0]}_`,
    `_Total: ${indexRows.length} issuances_`,
    '',
    '| Date | Document | Subject | PDF |',
    '|------|----------|---------|-----|',
  ];

  for (const row of indexRows) {
    const dateCell = row.date || '';
    const titleCell = row.mdFile
      ? `[${row.title}](${row.mdFile})`
      : row.title;
    const subjectCell = (row.subject || '').substring(0, 80) + (row.subject?.length > 80 ? '...' : '');
    const pdfCell = row.pdfUrl
      ? `[PDF](${row.pdfUrl})`
      : '';
    indexLines.push(`| ${dateCell} | ${titleCell} | ${subjectCell} | ${pdfCell} |`);
  }

  fs.writeFileSync(path.join(outputDir, 'INDEX.md'), indexLines.join('\n') + '\n', 'utf8');

  // ── Summary ──────────────────────────────────────────────────────────────────

  console.log('\n=== Scrape Complete ===');
  console.log(`Total entries:  ${entries.length}`);
  if (!skipDownload) {
    console.log(`PDFs downloaded: ${successCount}`);
    console.log(`PDFs skipped:   ${skipCount}`);
    console.log(`PDFs failed:    ${failCount}`);
  }
  console.log(`Output:         ${outputDir}`);
  console.log(`INDEX.md:       ${path.join(outputDir, 'INDEX.md')}`);
}

main().catch(err => {
  console.error('\nFATAL:', err.message);
  process.exit(1);
});
