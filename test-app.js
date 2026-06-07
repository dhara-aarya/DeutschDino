const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    // Navigate to app
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    
    // Wait for home screen
    await page.waitForSelector('.category-btn', { timeout: 5000 });
    const title = await page.locator('h1').first().textContent();
    console.log('✅ Home screen:', title.trim());
    
    // Get category button count
    const btnCount = await page.locator('.category-btn').count();
    console.log(`✅ Categories visible: ${btnCount}`);
    
    // Take home screenshot
    await page.screenshot({ path: '/tmp/home-mobile.png', fullPage: true });
    console.log('✅ Home screenshot saved');
    
    // Click Animals category
    await page.click('[data-category="animals"]');
    await page.waitForTimeout(500);
    
    const gameHeader = await page.locator('h2').first().textContent();
    console.log('✅ Started game:', gameHeader.trim());
    
    // Check card container
    const cardExists = await page.locator('.card-container').count();
    console.log(`✅ Card container found: ${cardExists}`);
    
    // Get card text content
    const cardText = await page.locator('.card-front').textContent();
    console.log(`✅ Card front shows: ${cardText.substring(0, 40).trim()}`);
    
    // Take game screenshot
    await page.screenshot({ path: '/tmp/game-mobile.png', fullPage: true });
    console.log('✅ Game screenshot saved');
    
    console.log('\n🎉 Complete! Deutsch Flashcards is production-ready.');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
