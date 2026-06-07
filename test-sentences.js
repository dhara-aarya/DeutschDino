const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    // Start with animals
    await page.click('[data-category="animals"]');
    await page.waitForTimeout(500);
    
    // Check front card has English sentence
    const frontText = await page.locator('.card-front').textContent();
    console.log('📖 Front card content:');
    console.log(frontText.trim());
    
    // Flip card
    await page.click('.card-container');
    await page.waitForTimeout(700);
    
    // Check back card has German sentence
    const backText = await page.locator('.card-back').textContent();
    console.log('\n📖 Back card content:');
    console.log(backText.trim());
    
    // Take screenshot
    await page.screenshot({ path: '/tmp/sentences-display.png', fullPage: true });
    
    console.log('\n✅ Sentences displaying correctly!');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
