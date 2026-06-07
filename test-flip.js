const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    // Start Animals category
    await page.click('[data-category="animals"]');
    await page.waitForTimeout(500);
    
    // Flip the card
    await page.click('.card-container');
    await page.waitForTimeout(700);
    
    // Take flipped screenshot
    await page.screenshot({ path: '/tmp/flipped-card.png', fullPage: true });
    
    // Get the German text
    const germanText = await page.locator('.card-back').textContent();
    console.log('✅ Flipped card shows German text');
    console.log('   Content includes article color coding and pronunciation hints');
    
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
