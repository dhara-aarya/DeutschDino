const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  try {
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle' });
    await page.waitForSelector('.category-btn');
    
    console.log('✅ HOME SCREEN');
    await page.screenshot({ path: '/tmp/demo-home.png', fullPage: true });
    
    // Click Food category (has sentences)
    await page.click('[data-category="food"]');
    await page.waitForTimeout(500);
    
    console.log('✅ FOOD CARD (Front) - Shows English sentence');
    const frontCard = await page.locator('.card-front').textContent();
    console.log(frontCard.substring(0, 150));
    await page.screenshot({ path: '/tmp/demo-front.png', fullPage: true });
    
    // Flip card
    await page.click('.card-container');
    await page.waitForTimeout(700);
    
    console.log('\n✅ FOOD CARD (Back) - Shows German sentence');
    const backCard = await page.locator('.card-back').textContent();
    console.log(backCard.substring(0, 150));
    await page.screenshot({ path: '/tmp/demo-back.png', fullPage: true });
    
    // Navigate next
    await page.click('.next-btn');
    await page.waitForTimeout(500);
    
    console.log('\n✅ NEXT CARD - Using navigation buttons');
    const nextCard = await page.locator('.card-front').textContent();
    console.log(nextCard.substring(0, 150));
    
    console.log('\n🎉 Complete app with sentences, emojis, and navigation!');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
