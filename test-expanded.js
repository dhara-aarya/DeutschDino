const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    // Count categories
    const btnCount = await page.locator('.category-btn').count();
    console.log(`✅ Categories loaded: ${btnCount}`);
    
    // Get category names
    const categories = await page.locator('.category-btn').allTextContents();
    console.log('\nAvailable categories:');
    categories.slice(0, 10).forEach((cat, i) => {
      console.log(`  ${i + 1}. ${cat.trim().split('\n')[1]}`);
    });
    
    if (btnCount > 10) {
      console.log(`  ... and ${btnCount - 10} more`);
    }
    
    // Take screenshot
    await page.screenshot({ path: '/tmp/categories.png', fullPage: true });
    console.log('\n✅ Expanded category grid saved');
    
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
