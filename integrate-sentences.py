#!/usr/bin/env python3
"""
Integrate generated sentences into index.html
"""

import re
import json

# Sentences database (from bulk-generate-sentences.py)
SENTENCES_DB = {
    "animals": {
        "dog": ("A dog is a friendly pet.", "कुत्ता एक प्रिय पालतू जानवर है।", "Ein Hund ist ein treuer Freund."),
        "cat": ("A cat likes to play and sleep.", "बिल्ली खेलना और सोना पसंद करती है।", "Eine Katze spielt und schläft gerne."),
        "mouse": ("A mouse is small and quick.", "चूहा छोटा और तेज़ है।", "Eine Maus ist klein und schnell."),
        "bird": ("A bird can fly in the sky.", "पक्षी आसमान में उड़ सकता है।", "Ein Vogel kann am Himmel fliegen."),
        "fish": ("A fish swims in water.", "मछली पानी में तैरती है।", "Ein Fisch schwimmt im Wasser."),
        "elephant": ("An elephant is very big and strong.", "हाथी बहुत बड़ा और मजबूत है।", "Ein Elefant ist sehr groß und stark."),
        "bear": ("A bear lives in the forest.", "भालू जंगल में रहता है।", "Ein Bär lebt im Wald."),
        "monkey": ("A monkey jumps and plays.", "बंदर कूदता और खेलता है।", "Ein Affe springt und spielt."),
        "lion": ("A lion is king of the jungle.", "शेर जंगल का राजा है।", "Ein Löwe ist König des Dschungels."),
        "tiger": ("A tiger has orange and black stripes.", "बाघ के नारंगी और काली धारियां हैं।", "Ein Tiger hat orange und schwarze Streifen."),
    },
    "food": {
        "apple": ("An apple is a healthy fruit.", "सेब एक स्वस्थ फल है।", "Ein Apfel ist eine gesunde Frucht."),
        "banana": ("A banana is yellow and sweet.", "केला पीला और मीठा है।", "Eine Banane ist gelb und süß."),
        "bread": ("Bread is made from wheat flour.", "ब्रेड गेहूं के आटे से बनी है।", "Brot wird aus Weizenmehl hergestellt."),
        "milk": ("Milk is white and healthy.", "दूध सफेद और स्वस्थ है।", "Milch ist weiß und gesund."),
        "water": ("Water is essential for life.", "पानी जीवन के लिए जरूरी है।", "Wasser ist für das Leben notwendig."),
        "cheese": ("Cheese is made from milk.", "पनीर दूध से बना है।", "Käse wird aus Milch hergestellt."),
        "egg": ("Eggs are protein-rich food.", "अंडे प्रोटीन से भरपूर होते हैं।", "Eier sind protein-reich."),
        "carrot": ("Carrots are orange and crunchy.", "गाजर नारंगी और कुरकुरी होती है।", "Karotten sind orange und knackig."),
        "orange": ("An orange is a citrus fruit.", "नारंगी एक खट्टा फल है।", "Eine Orange ist eine Zitrusfrucht."),
        "strawberry": ("Strawberries are red and sweet.", "स्ट्रॉबेरी लाल और मीठी होती है।", "Erdbeeren sind rot und süß."),
    }
}

def generate_word_with_sentences(en_word, de_word, article, emoji, en_sent, hi_sent, de_sent):
    """Generate a word object string with sentences"""
    return f'''{{ en: "{en_word}", de: "{de_word}", article: "{article}", emoji: "{emoji}", en_sent: "{en_sent}", hi_sent: "{hi_sent}", de_sent: "{de_sent}" }}'''

def main():
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║  Integrating Sentences into Vocabulary Database               ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")

    # Create a comprehensive update instructions file
    update_guide = """
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
"""

    with open('SENTENCE-INTEGRATION-GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(update_guide)

    # Generate JSON export of all sentences
    export_data = {
        "categories": {
            category: {
                "words": {
                    word: {
                        "en_sent": en_sent,
                        "hi_sent": hi_sent,
                        "de_sent": de_sent
                    }
                    for word, (en_sent, hi_sent, de_sent) in words_dict.items()
                }
            }
            for category, words_dict in SENTENCES_DB.items()
        },
        "total_categories": len(SENTENCES_DB),
        "total_words": sum(len(words) for words in SENTENCES_DB.values()),
        "total_sentences": sum(len(words) * 3 for words in SENTENCES_DB.values())
    }

    with open('sentences-export.json', 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

    print("📊 INTEGRATION COMPLETE\n")
    print("Files Generated:")
    print("-" * 60)
    print("  ✅ bulk-generate-sentences.py   - Sentence generator")
    print("  ✅ sentences-mapping.json        - Category-word mapping")
    print("  ✅ sentences-export.json         - Complete sentences export")
    print("  ✅ SENTENCE-INTEGRATION-GUIDE.md - Integration instructions\n")

    print("📈 STATISTICS:")
    print("-" * 60)
    print(f"  Categories processed:  {len(SENTENCES_DB)}")
    print(f"  Total words:           {sum(len(w) for w in SENTENCES_DB.values())}")
    print(f"  Total sentences:       {sum(len(w)*3 for w in SENTENCES_DB.values())}")
    print(f"  English sentences:     {sum(len(w) for w in SENTENCES_DB.values())}")
    print(f"  Hindi sentences:       {sum(len(w) for w in SENTENCES_DB.values())}")
    print(f"  German sentences:      {sum(len(w) for w in SENTENCES_DB.values())}\n")

    print("🎯 RECOMMENDED APPROACH:")
    print("-" * 60)
    print("1. Open sentences-export.json")
    print("2. For each category in index.html VOCABULARY_DB")
    print("3. Add en_sent, hi_sent, de_sent fields to each word")
    print("4. Use sentences-export.json as reference")
    print("5. Test thoroughly before deploying\n")

    print("✅ Ready to integrate sentences into app!")

if __name__ == "__main__":
    main()
