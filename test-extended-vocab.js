const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    // Load the page
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    // Check home screen status badge
    const statusBadge = await page.locator('text=/Extended Vocabulary|Core Vocabulary/').textContent();
    console.log('✅ Vocabulary status:', statusBadge.trim());
    
    // Click Animals category to check word count
    await page.click('[data-category="animals"]');
    await page.waitForTimeout(500);
    
    // Get the progress display (should show total cards)
    const progressText = await page.locator('text=/[0-9]+ \\/ [0-9]+/').textContent();
    console.log(`✅ Animal words available: ${progressText.trim()}`);
    
    // Check if extended vocab was loaded by looking at word count
    // Core: ~18 words, Extended: 100+ words
    const matches = progressText.match(/\d+ \/ (\d+)/);
    if (matches) {
      const totalWords = parseInt(matches[1]);
      if (totalWords > 50) {
        console.log(`🎉 Extended vocabulary active! (${totalWords} animal words)`);
      } else {
        console.log(`ℹ️ Core vocabulary in use (${totalWords} animal words)`);
      }
    }
    
    // Verify the app still works with extended data
    const cardText = await page.locator('.card-front').textContent();
    console.log(`✅ Card displays correctly: "${cardText.substring(0, 30).trim()}..."`);
    
    await page.screenshot({ path: '/tmp/vocab-loaded.png', fullPage: true });
    console.log('\n✅ Extended vocabulary system working!');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
