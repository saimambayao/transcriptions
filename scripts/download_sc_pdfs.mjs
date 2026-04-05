#!/usr/bin/env node
/**
 * Download missing SC jurisprudence PDFs (2021-2026).
 *
 * Uses the same WP REST API as scrape_sc_jurisprudence.mjs but ONLY downloads PDFs.
 * Skips transcription entirely. Skips PDFs that already exist on disk.
 *
 * Usage:
 *   node scripts/download_sc_pdfs.mjs --year 2025
 *   node scripts/download_sc_pdfs.mjs                  # all years 2021-2026
 *   node scripts/download_sc_pdfs.mjs --dry-run        # count missing only
 */

import { request } from '/Users/saidamenmambayao/.nvm/versions/node/v22.17.0/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const JUR_DIR = path.resolve(__dirname, '../jurisprudence');

const CATEGORY_IDS = {
  2021: 627, 2022: 637, 2023: 1336,
  2024: 1409, 2025: 1451, 2026: 1486,
};

const API_BASE = 'https://sc.judiciary.gov.ph/wp-json/wp/v2/posts';
const RATE_LIMIT_MS = 300;

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function fetchPostsForCategory(apiCtx, categoryId) {
  const posts = [];
  let page = 1;
  while (true) {
    const url = `${API_BASE}?categories=${categoryId}&per_page=100&page=${page}`;
    const resp = await apiCtx.get(url);
    if (!resp.ok()) break;
    const data = await resp.json();
    if (!data.length) break;
    posts.push(...data);
    const totalPages = parseInt(resp.headers()['x-wp-totalpages'] || '1');
    if (page >= totalPages) break;
    page++;
    await sleep(200);
  }
  return posts;
}

async function fetchSubcategories(apiCtx, parentCatId) {
  const cats = [];
  let page = 1;
  while (true) {
    const url = `https://sc.judiciary.gov.ph/wp-json/wp/v2/categories?parent=${parentCatId}&per_page=100&page=${page}`;
    const resp = await apiCtx.get(url);
    if (!resp.ok()) break;
    const data = await resp.json();
    if (!data.length) break;
    cats.push(...data);
    const totalPages = parseInt(resp.headers()['x-wp-totalpages'] || '1');
    if (page >= totalPages) break;
    page++;
    await sleep(200);
  }
  return cats;
}

async function fetchAllPosts(apiCtx, categoryId) {
  // Fetch posts from parent category
  const posts = await fetchPostsForCategory(apiCtx, categoryId);
  const seenIds = new Set(posts.map(p => p.id));

  // Fetch subcategories and their posts
  const subcats = await fetchSubcategories(apiCtx, categoryId);
  if (subcats.length > 0) {
    console.log(`  Found ${subcats.length} subcategories, fetching their posts...`);
    for (const subcat of subcats) {
      if (subcat.count === 0) continue;
      const subPosts = await fetchPostsForCategory(apiCtx, subcat.id);
      for (const p of subPosts) {
        if (!seenIds.has(p.id)) {
          posts.push(p);
          seenIds.add(p.id);
        }
      }
      await sleep(200);
    }
  }
  return posts;
}

function extractPdfUrl(post) {
  const content = post.content?.rendered || '';
  const match = content.match(/href="([^"]+\.pdf)"/i);
  return match ? match[1] : null;
}

async function main() {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const yearArg = args.includes('--year') ? parseInt(args[args.indexOf('--year') + 1]) : null;
  const years = yearArg ? [yearArg] : [2021, 2022, 2023, 2024, 2025, 2026];

  console.log('=== SC Jurisprudence PDF Downloader ===');
  console.log(`Years: ${years.join(', ')}${dryRun ? ' (DRY RUN)' : ''}\n`);

  const apiCtx = await request.newContext({
    baseURL: 'https://sc.judiciary.gov.ph',
    extraHTTPHeaders: {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
      'Referer': 'https://sc.judiciary.gov.ph/',
    },
  });

  let totalDownloaded = 0, totalSkipped = 0, totalFailed = 0, totalNoPdf = 0;

  for (const year of years) {
    const catId = CATEGORY_IDS[year];
    if (!catId) { console.log(`No category for ${year}, skipping.`); continue; }

    const pdfDir = path.join(JUR_DIR, String(year), 'pdf');
    fs.mkdirSync(pdfDir, { recursive: true });

    console.log(`\n--- ${year} ---`);
    console.log(`Fetching post index (category ${catId})...`);
    const posts = await fetchAllPosts(apiCtx, catId);
    console.log(`Found ${posts.length} posts.`);

    let downloaded = 0, skipped = 0, failed = 0, noPdf = 0;

    for (let i = 0; i < posts.length; i++) {
      const pdfUrl = extractPdfUrl(posts[i]);
      if (!pdfUrl) { noPdf++; continue; }

      const pdfFilename = path.basename(decodeURIComponent(new URL(pdfUrl).pathname));
      const pdfPath = path.join(pdfDir, pdfFilename);

      if (fs.existsSync(pdfPath) && fs.statSync(pdfPath).size > 1000) {
        skipped++;
        continue;
      }

      if (dryRun) {
        console.log(`  [${i+1}/${posts.length}] WOULD download: ${pdfFilename}`);
        downloaded++;
        continue;
      }

      try {
        const resp = await apiCtx.get(pdfUrl, { timeout: 60000 });
        if (resp.ok()) {
          const buf = await resp.body();
          fs.writeFileSync(pdfPath, buf);
          downloaded++;
          if (downloaded % 50 === 0) {
            console.log(`  [${i+1}/${posts.length}] ${downloaded} downloaded so far...`);
          }
        } else {
          console.log(`  [${i+1}/${posts.length}] FAILED ${pdfFilename}: HTTP ${resp.status()}`);
          failed++;
        }
        await sleep(RATE_LIMIT_MS);
      } catch (e) {
        console.log(`  [${i+1}/${posts.length}] ERROR ${pdfFilename}: ${e.message.substring(0, 60)}`);
        failed++;
      }
    }

    console.log(`${year}: downloaded=${downloaded}, skipped=${skipped}, failed=${failed}, noPdf=${noPdf}`);
    totalDownloaded += downloaded;
    totalSkipped += skipped;
    totalFailed += failed;
    totalNoPdf += noPdf;
  }

  await apiCtx.dispose();

  console.log(`\n=== Summary ===`);
  console.log(`Downloaded: ${totalDownloaded}`);
  console.log(`Already existed: ${totalSkipped}`);
  console.log(`Failed: ${totalFailed}`);
  console.log(`No PDF URL: ${totalNoPdf}`);
}

main().catch(err => { console.error('FATAL:', err.message); process.exit(1); });
