const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/hadith/bukhari";
if (!fs.existsSync(BASE_DIR)) {
    fs.mkdirSync(BASE_DIR, { recursive: true });
}

async function scrapeBook(bookId) {
    const browser = await chromium.launch({ headless: true });
    // Use a real User-Agent to avoid bot detection
    const context = await browser.newContext({
        userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    });
    const page = await context.newPage();

    const url = `https://sunnah.com/bukhari/${bookId}`;
    console.log(`[Book ${bookId}] Navigating to ${url}...`);

    try {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
        // Use the actual container class found in curl
        await page.waitForSelector('.actualHadithContainer', { timeout: 30000 });

        // Get book title and range
        const bookTitle = await page.textContent('.book_page_en_name');
        const bookTitleArabic = await page.textContent('.book_page_ar_name');
        
        const hadiths = await page.$$eval('.actualHadithContainer', (elements) => {
            return elements.map(el => {
                // Number extraction
                const refNode = el.querySelector('.hadith_reference');
                const idNode = refNode ? refNode.querySelector('span:last-child') : null;
                const id = idNode ? idNode.textContent.trim().match(/\d+/)?.[0] : 'unknown';

                const english = el.querySelector('.english_hadith_full')?.innerText || '';
                const arabic = el.querySelector('.arabic_hadith_full')?.innerText || el.querySelector('.arabic_text_details')?.innerText || '';
                
                return { id, english, arabic };
            });
        });

        if (hadiths.length === 0) {
            console.log(`[Book ${bookId}] No hadiths found on page.`);
            await browser.close();
            return;
        }

        const startId = hadiths[0].id;
        const endId = hadiths[hadiths.length - 1].id;
        const cleanTitle = bookTitle.trim()
            .replace(/[^a-zA-Z0-9 ]/g, '') // Remove special chars
            .replace(/\s+/g, '-') // Replace spaces with dashes
            .replace(/-+/g, '-'); // Remove duplicate dashes
        
        const filename = `${String(bookId).padStart(2, '0')}-${cleanTitle}-${startId}-${endId}.md`;
        const filepath = path.join(BASE_DIR, filename);

        let content = `# Book ${bookId}: ${bookTitle.trim()} (${bookTitleArabic.trim()})\n\n`;
        content += `- **Collection:** Sahih al-Bukhari\n`;
        content += `- **Translation:** Dr. M. Muhsin Khan\n`;
        content += `- **Source:** Sunnah.com\n\n`;
        content += `---\n\n`;

        for (const h of hadiths) {
            content += `### Hadith ${h.id}\n\n`;
            content += `> ${h.arabic.trim()}\n\n`;
            content += `${h.english.trim()}\n\n`;
            content += `---\n\n`;
        }

        fs.writeFileSync(filepath, content, 'utf-8');
        console.log(`[Book ${bookId}] Saved to ${filename} (${hadiths.length} hadiths)`);

    } catch (err) {
        console.error(`[Book ${bookId}] Error: ${err.message}`);
    } finally {
        await browser.close();
    }
}

async function main() {
    const args = process.argv.slice(2);
    const startBook = 1;
    const endBook = args.includes('--all') ? 97 : 3;

    console.log(`Starting scrape from Book ${startBook} to ${endBook}...`);
    for (let i = startBook; i <= endBook; i++) {
        await scrapeBook(i);
        // Random delay to be extra polite and avoid rate limits
        const delay = 1000 + Math.random() * 2000;
        await new Promise(r => setTimeout(r, delay));
    }
    console.log("Scrape finished.");
}

main();
