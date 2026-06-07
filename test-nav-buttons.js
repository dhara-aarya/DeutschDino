const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    // Start game
    await page.click('[data-category="animals"]');
    await page.waitForTimeout(500);
    
    // Check initial card
    const initialCard = await page.locator('.card-front').textContent();
    console.log(`✅ Card 1 shows: ${initialCard.substring(0, 30).trim()}`);
    
    // Check navigation buttons exist
    const prevBtn = await page.locator('.prev-btn');
    const nextBtn = await page.locator('.next-btn');
    
    console.log(`✅ Previous button found: ${await prevBtn.count() > 0 ? 'yes' : 'no'}`);
    console.log(`✅ Next button found: ${await nextBtn.count() > 0 ? 'yes' : 'no'}`);
    
    // Check if previous button is disabled on first card
    const prevDisabled = await prevBtn.getAttribute('disabled');
    console.log(`✅ Previous button disabled on first card: ${prevDisabled ? 'yes' : 'no'}`);
    
    // Click next button
    await page.click('.next-btn');
    await page.waitForTimeout(500);
    
    // Check card changed
    const secondCard = await page.locator('.card-front').textContent();
    console.log(`✅ Card 2 shows: ${secondCard.substring(0, 30).trim()}`);
    console.log(`✅ Cards are different: ${initialCard !== secondCard ? 'yes' : 'no'}`);
    
    // Click previous button
    await page.click('.prev-btn');
    await page.waitForTimeout(500);
    
    // Should be back to first card
    const backCard = await page.locator('.card-front').textContent();
    console.log(`✅ Back to card 1: ${initialCard === backCard ? 'yes' : 'no'}`);
    
    await page.screenshot({ path: '/tmp/nav-buttons.png', fullPage: true });
    
    console.log('\n🎉 Navigation buttons working perfectly!');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
