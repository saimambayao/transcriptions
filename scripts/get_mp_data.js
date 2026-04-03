const { chromium } = require('playwright');

async function getMPData(url) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  try {
    await page.goto(url, { waitUntil: 'load', timeout: 60000 });
    
    // Wait for main content to ensure we are past any initial redirects or Cloudflare
    try {
        await page.waitForSelector('#main-content', { timeout: 10000 });
    } catch (e) {
        // Fallback for some pages that might not have #main-content
        await page.waitForTimeout(5000);
    }
    
    // Wait a bit more for Divi tabs to initialize
    await page.waitForTimeout(2000);
    
    // Extract the full HTML
    const content = await page.content();
    console.log(content);
  } catch (error) {
    console.error(`Error fetching ${url}: ${error.message}`);
    process.exit(1);
  } finally {
    await browser.close();
  }
}

const url = process.argv[2];
if (!url) {
  console.error('Usage: node get_mp_data.js <url>');
  process.exit(1);
}

getMPData(url).catch(err => {
    console.error(err);
    process.exit(1);
});
