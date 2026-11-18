// Render every contextcon-meta-*.html in this folder to a PNG at its exact size.
// Run from the repo root: node banners/meta-ads/render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = __dirname;
  const files = fs.readdirSync(dir).filter(f => /^contextcon-meta-.*\.html$/.test(f));
  const browser = await chromium.launch();
  for (const f of files) {
    const [w, h] = f.match(/(\d+)x(\d+)\.html$/).slice(1).map(Number);
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    await page.goto('file://' + path.join(dir, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const loaded = await page.evaluate(() => [...document.fonts].filter(x => x.status === 'loaded').map(x => x.family));
    await page.locator('.ad').screenshot({ path: path.join(dir, f.replace(/\.html$/, '.png')) });
    console.log(f, w + 'x' + h, [...new Set(loaded)].join(','));
    await page.close();
  }
  await browser.close();
})();
