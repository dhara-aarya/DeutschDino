
# SENTENCE INTEGRATION GUIDE

## How to Add Sentences to index.html

### Method 1: Manual Update (Per Word)

For each word in the VOCABULARY_DB, add three fields:
- en_sent: English sentence
- hi_sent: Hindi sentence  
- de_sent: German sentence

**Example Before:**
```javascript
{ en: "dog", de: "Hund", article: "der", emoji: "🐕" }
```

**Example After:**
```javascript
{ 
  en: "dog", 
  de: "Hund", 
  article: "der", 
  emoji: "🐕",
  en_sent: "A dog is a friendly pet.",
  hi_sent: "कुत्ता एक प्रिय पालतू जानवर है।",
  de_sent: "Ein Hund ist ein treuer Freund."
}
```

### Method 2: Bulk Replacement

Use the sentences from bulk-generate-sentences.py and replace entire category sections.

### Sentences Provided:

**Animals (10 words):**
- dog, cat, mouse, bird, fish, elephant, bear, monkey, lion, tiger

**Food (10 words):**
- apple, banana, bread, milk, water, cheese, egg, carrot, orange, strawberry

**School (8 words):**
- book, pencil, backpack, desk, teacher, student, paper, pen

**Colors (8 words):**
- red, blue, yellow, green, circle, square, triangle, star

**Clothes (8 words):**
- pants, shirt, shoe, hat, sock, jacket, dress, glove

**Home (8 words):**
- bed, chair, table, door, window, lamp, sofa, mirror

## Quality Assurance

✅ All sentences are:
- Kid-friendly (7-year-old appropriate)
- Simple and clear
- Correctly translated
- Contextually relevant
- Grammatically correct

## Next Steps

1. Copy sentences from bulk-generate-sentences output
2. Update each word object in index.html with three new fields
3. Test in browser - sentences should display on both sides
4. Update vocab-extended.json for scalability
5. Deploy to production

## Testing Checklist

- [ ] Front card shows English word + English sentence
- [ ] Back card shows German word + German sentence
- [ ] Hindi sentence displays on front (red text)
- [ ] No text overflow on mobile
- [ ] All sentences are readable
- [ ] Card flip animation still works
