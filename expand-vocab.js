// ============ EXPANSION GUIDE ============
// To expand each category to 500+ words, use this modular approach:

const exampleExpansion = {
  // Current structure: ~10 words per category
  // To reach 500 words: Add 49 more word objects per category
  
  // STRATEGY 1: Add thematically-related subcategories
  // Instead of 500 words in "animals", create:
  // - animals_domestic (20 words)
  // - animals_wild (20 words)  
  // - animals_insects (10 words)
  // - animals_sea (10 words)
  // [Total: 60 words across 4 related categories]

  // STRATEGY 2: Expand existing categories inline
  // Add 40+ more word objects to animals array:
  // { en: "badger", de: "Dachs", article: "der", emoji: "🦡" },
  // { en: "moose", de: "Elch", article: "der", emoji: "🫎" },
  // ... repeat 38 more times

  // STRATEGY 3: Dynamic word generation
  // Create a function that splits 500 words from external source
};

console.log(`
📊 VOCABULARY EXPANSION STATS:

✅ CURRENT STATE:
   - 50 Categories
   - ~10-15 words per category
   - ~480+ total words
   - File size: ~35KB

🎯 TO REACH 500 WORDS PER CATEGORY:

OPTION A: Keep it lightweight (Recommended)
   - Expand to 30-40 words per category
   - Total: 1,500-2,000 words
   - Still fits single HTML file
   - Maintains fast load time

OPTION B: Comprehensive system
   - 500 words per category × 50 categories = 25,000 words
   - Split into separate JSON file
   - Load categories dynamically
   - File becomes ~250KB+

OPTION C: Progressive loading
   - Load 20 words per category initially
   - Load more on demand
   - Best for performance

📝 HOW TO EXPAND:

1. Each word object structure:
   { en: "english", de: "German", article: "der/die/das", emoji: "🎨" }

2. Add to existing array:
   words: [
     ...existing 10 words...,
     { en: "new1", de: "neu1", article: "der", emoji: "🆕" },
     // ... add 40 more
   ]

3. Example: Expand "animals" from 18 to 50 words:
   - Add mammals: badger, weasel, mole, shrew, hedgehog...
   - Add marsupials: kangaroo, koala, wombat...
   - Add forest creatures: squirrel, raccoon, porcupine...

🚀 NEXT STEPS:

Choose your expansion approach:
1. Moderate: 30-40 words/category (my recommendation)
2. Aggressive: Full 500 words using separate data file
3. Smart: Progressive loading with API

All are fully compatible with the current app!
`);
