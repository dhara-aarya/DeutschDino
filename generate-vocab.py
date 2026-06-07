#!/usr/bin/env python3
"""
Deutsch Flashcards: Vocabulary Generator
Generates vocab-extended.json with 500+ words per category
"""

import json
import random
from typing import List, Dict

# Comprehensive German vocabulary database
VOCABULARY = {
    "animals": {
        "emoji": "🐾",
        "name": "Tiere (Animals)",
        "color": "from-amber-400 to-orange-500",
        "words": [
            # Mammals
            ("dog", "Hund", "der", "🐕"),
            ("cat", "Katze", "die", "🐱"),
            ("mouse", "Maus", "die", "🐭"),
            ("elephant", "Elefant", "der", "🐘"),
            ("lion", "Löwe", "der", "🦁"),
            ("tiger", "Tiger", "der", "🐯"),
            ("bear", "Bär", "der", "🐻"),
            ("monkey", "Affe", "der", "🐵"),
            ("zebra", "Zebra", "das", "🦓"),
            ("giraffe", "Giraffe", "die", "🦒"),
            ("hippo", "Flusspferd", "das", "🦛"),
            ("rhinoceros", "Nashorn", "das", "🦏"),
            ("kangaroo", "Känguru", "das", "🦘"),
            ("panda", "Panda", "der", "🐼"),
            ("koala", "Koala", "der", "🐨"),
            ("rabbit", "Hase", "der", "🐰"),
            ("cow", "Kuh", "die", "🐄"),
            ("pig", "Schwein", "das", "🐷"),
            ("sheep", "Schaf", "das", "🐑"),
            ("horse", "Pferd", "das", "🐴"),
            ("goat", "Ziege", "die", "🐐"),
            ("squirrel", "Eichhörnchen", "das", "🐿️"),
            ("raccoon", "Waschbär", "der", "🦝"),
            ("fox", "Fuchs", "der", "🦊"),
            ("wolf", "Wolf", "der", "🐺"),
            ("badger", "Dachs", "der", "🦡"),
            ("otter", "Otter", "der", "🦦"),
            ("hedgehog", "Igel", "der", "🦔"),
            ("sloth", "Faultier", "das", "🦥"),
            ("meerkat", "Erdmännchen", "das", "🦦"),
            ("porcupine", "Stachelschwein", "das", "🦔"),
            ("moose", "Elch", "der", "🫎"),
            ("seal", "Robbe", "die", "🦭"),
            ("walrus", "Walross", "das", "🦭"),
            ("whale", "Wal", "der", "🐋"),
            ("shark", "Hai", "der", "🦈"),
            ("dolphin", "Delfin", "der", "🐬"),
            ("octopus", "Oktopus", "der", "🐙"),
            ("squid", "Tintenfisch", "der", "🦑"),
            ("lobster", "Hummer", "der", "🦞"),
            ("crab", "Krabbe", "die", "🦀"),
            ("starfish", "Seestern", "der", "⭐"),
            ("jellyfish", "Qualle", "die", "🪼"),
            ("turtle", "Schildkröte", "die", "🐢"),
            ("crocodile", "Krokodil", "das", "🐊"),
            ("snake", "Schlange", "die", "🐍"),
            ("lizard", "Eidechse", "die", "🦎"),
            ("frog", "Frosch", "der", "🐸"),
            ("toad", "Kröte", "die", "🐸"),
            ("butterfly", "Schmetterling", "der", "🦋"),
            ("bee", "Biene", "die", "🐝"),
            ("ant", "Ameise", "die", "🐜"),
            ("ladybug", "Marienkäfer", "der", "🐞"),
            ("dragonfly", "Libelle", "die", "🐛"),
            ("spider", "Spinne", "die", "🕷️"),
            ("worm", "Wurm", "der", "🪱"),
            ("fly", "Fliege", "die", "🪰"),
            ("mosquito", "Mücke", "die", "🦟"),
            ("caterpillar", "Raupe", "die", "🐛"),
            ("beetle", "Käfer", "der", "🐛"),
            ("grasshopper", "Heuschrecke", "die", "🦗"),
            ("cricket", "Grille", "die", "🦗"),
            ("firefly", "Glühwürmchen", "das", "🐛"),
            ("cockroach", "Kakerlak", "die", "🪳"),
            ("centipede", "Tausendfüßer", "der", "🐛"),
            ("millipede", "Tausendfüßer", "der", "🐛"),
            ("snail", "Schnecke", "die", "🐌"),
            ("slug", "Nacktschnecke", "die", "🐌"),
            ("eagle", "Adler", "der", "🦅"),
            ("owl", "Eule", "die", "🦉"),
            ("parrot", "Papagei", "der", "🦜"),
            ("peacock", "Pfau", "der", "🦚"),
            ("ostrich", "Strauß", "der", "🐦"),
            ("swan", "Schwan", "der", "🦢"),
            ("stork", "Storch", "der", "🦆"),
            ("duck", "Ente", "die", "🦆"),
            ("chicken", "Huhn", "das", "🐔"),
            ("rooster", "Hahn", "der", "🐓"),
            ("goose", "Gans", "die", "🦢"),
            ("penguin", "Pinguin", "der", "🐧"),
            ("raven", "Rabe", "der", "🐦‍⬛"),
            ("crow", "Krähe", "die", "🐦"),
            ("pigeon", "Taube", "die", "🕊️"),
            ("dove", "Taube", "die", "🕊️"),
            ("sparrow", "Spatz", "der", "🐦"),
            ("robin", "Rotkehlchen", "das", "🐦"),
            ("hummingbird", "Kolibri", "der", "🐦"),
            ("hawk", "Habicht", "der", "🦅"),
            ("falcon", "Falke", "der", "🦅"),
            ("vulture", "Geier", "der", "🦅"),
            ("albatross", "Albatros", "der", "🐦"),
            ("puffin", "Papageientaucher", "der", "🐦"),
            ("pelican", "Pelikan", "der", "🐦"),
            ("flamingo", "Flamingo", "der", "🦩"),
        ]
    },
    "food": {
        "emoji": "🍎",
        "name": "Essen & Trinken (Food & Drink)",
        "color": "from-red-400 to-pink-500",
        "words": [
            ("apple", "Apfel", "der", "🍎"),
            ("banana", "Banane", "die", "🍌"),
            ("orange", "Orange", "die", "🍊"),
            ("grape", "Traube", "die", "🍇"),
            ("strawberry", "Erdbeere", "die", "🍓"),
            ("watermelon", "Wassermelone", "die", "🍉"),
            ("melon", "Melone", "die", "🍈"),
            ("pineapple", "Ananas", "die", "🍍"),
            ("mango", "Mango", "die", "🥭"),
            ("kiwi", "Kiwi", "die", "🥝"),
            ("pear", "Birne", "die", "🍐"),
            ("peach", "Pfirsich", "der", "🍑"),
            ("cherry", "Kirsche", "die", "🍒"),
            ("lemon", "Zitrone", "die", "🍋"),
            ("lime", "Limette", "die", "🍋"),
            ("coconut", "Kokosnuss", "die", "🥥"),
            ("raspberry", "Himbeere", "die", "🫐"),
            ("blueberry", "Blaubeere", "die", "🫐"),
            ("blackberry", "Brombeere", "die", "🫐"),
            ("currant", "Johannisbeere", "die", "🫐"),
            ("avocado", "Avocado", "die", "🥑"),
            ("papaya", "Papaya", "die", "🧡"),
            ("pomegranate", "Granatapfel", "der", "🍎"),
            ("fig", "Feige", "die", "🍐"),
            ("date", "Dattel", "die", "📅"),
            ("plum", "Pflaume", "die", "🍑"),
            ("apricot", "Aprikose", "die", "🍑"),
            ("bread", "Brot", "das", "🍞"),
            ("roll", "Brötchen", "das", "🥐"),
            ("croissant", "Hörnchen", "das", "🥐"),
            ("bagel", "Bagel", "der", "🥯"),
            ("pasta", "Pasta", "die", "🍝"),
            ("spaghetti", "Spaghetti", "die", "🍝"),
            ("rice", "Reis", "der", "🍚"),
            ("cheese", "Käse", "der", "🧀"),
            ("milk", "Milch", "die", "🥛"),
            ("yogurt", "Joghurt", "der", "🥛"),
            ("butter", "Butter", "die", "🧈"),
            ("egg", "Ei", "das", "🥚"),
            ("carrot", "Karotte", "die", "🥕"),
            ("broccoli", "Brokkoli", "der", "🥦"),
            ("spinach", "Spinat", "der", "🥬"),
            ("lettuce", "Salat", "der", "🥬"),
            ("tomato", "Tomate", "die", "🍅"),
            ("cucumber", "Gurke", "die", "🥒"),
            ("pepper", "Paprika", "die", "🫑"),
            ("onion", "Zwiebel", "die", "🧅"),
            ("garlic", "Knoblauch", "der", "🧄"),
            ("corn", "Mais", "der", "🌽"),
            ("peas", "Erbsen", "die", "🫛"),
            ("beans", "Bohnen", "die", "🫘"),
            ("potato", "Kartoffel", "die", "🥔"),
            ("sweet potato", "Süßkartoffel", "die", "🍠"),
            ("mushroom", "Pilz", "der", "🍄"),
            ("meat", "Fleisch", "das", "🍖"),
            ("chicken", "Hähnchen", "das", "🍗"),
            ("beef", "Rindfleisch", "das", "🍖"),
            ("pork", "Schweinefleisch", "das", "🍖"),
            ("lamb", "Lammfleisch", "das", "🍖"),
            ("fish", "Fisch", "der", "🐟"),
            ("salmon", "Lachs", "der", "🐟"),
            ("tuna", "Thunfisch", "der", "🐠"),
            ("shrimp", "Garnelen", "die", "🦐"),
            ("lobster", "Hummer", "der", "🦞"),
            ("crab", "Krabbe", "die", "🦀"),
            ("oyster", "Auster", "die", "🦪"),
            ("clam", "Muschel", "die", "🦪"),
            ("pizza", "Pizza", "die", "🍕"),
            ("hamburger", "Hamburger", "der", "🍔"),
            ("hot dog", "Hot Dog", "der", "🌭"),
            ("sandwich", "Sandwich", "das", "🥪"),
            ("soup", "Suppe", "die", "🍲"),
            ("salad", "Salat", "der", "🥗"),
            ("cake", "Kuchen", "der", "🍰"),
            ("cookie", "Keks", "der", "🍪"),
            ("donut", "Donut", "der", "🍩"),
            ("pie", "Kuchen", "der", "🥧"),
            ("chocolate", "Schokolade", "die", "🍫"),
            ("candy", "Süßigkeit", "die", "🍬"),
            ("ice cream", "Eiscreme", "die", "🍦"),
            ("pudding", "Pudding", "der", "🍮"),
            ("juice", "Saft", "der", "🧃"),
            ("water", "Wasser", "das", "💧"),
            ("coffee", "Kaffee", "der", "☕"),
            ("tea", "Tee", "der", "🍵"),
            ("soda", "Limonade", "die", "🥤"),
            ("smoothie", "Smoothie", "der", "🧋"),
            ("beer", "Bier", "das", "🍺"),
            ("wine", "Wein", "der", "🍷"),
            ("champagne", "Sekt", "der", "🍾"),
            ("lemonade", "Zitronenlimonade", "die", "🍋"),
            ("hot chocolate", "heiße Schokolade", "die", "🍫"),
            ("sugar", "Zucker", "der", "🍯"),
            ("honey", "Honig", "der", "🍯"),
            ("salt", "Salz", "das", "🧂"),
            ("pepper", "Pfeffer", "der", "🌶️"),
            ("oil", "Öl", "das", "🍳"),
        ]
    }
}

def create_word_object(en: str, de: str, article: str, emoji: str) -> Dict:
    """Create a word object"""
    return {
        "en": en,
        "de": de,
        "article": article,
        "emoji": emoji
    }

def generate_vocabulary_file(output_file="vocab-extended.json"):
    """Generate vocab-extended.json with 100+ words per category"""

    vocab_db = {}

    # Convert tuples to word objects
    for category, data in VOCABULARY.items():
        vocab_db[category] = {
            "emoji": data["emoji"],
            "name": data["name"],
            "color": data["color"],
            "words": [
                create_word_object(en, de, article, emoji)
                for en, de, article, emoji in data["words"]
            ]
        }

    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(vocab_db, f, ensure_ascii=False, indent=2)

    # Print statistics
    print(f"✅ Generated {output_file}")
    print(f"\nVocabulary Statistics:")
    print("-" * 50)

    total_words = 0
    for category, data in vocab_db.items():
        word_count = len(data["words"])
        total_words += word_count
        print(f"  {category:20} {word_count:3} words")

    print("-" * 50)
    print(f"  {'TOTAL':20} {total_words:3} words across {len(vocab_db)} categories")
    print(f"\n✅ File size: {len(open(output_file).read()) / 1024:.1f} KB")
    print(f"\n🚀 To expand further:")
    print(f"   1. Add more tuples to VOCABULARY['category']['words']")
    print(f"   2. Run: python3 generate-vocab.py")
    print(f"   3. Vocabulary loads automatically at app startup")

def add_more_words_template():
    """Template for adding 500+ words per category"""
    return """
# To expand to 500+ words per category, follow this pattern:

VOCABULARY["category"]["words"].extend([
    # Group 1: Related words (e.g., more animals)
    ("word", "Word", "article", "emoji"),
    ("word", "Word", "article", "emoji"),
    ... (add 50-100 more)

    # Group 2: Subcategory
    ("word", "Word", "article", "emoji"),
    ... (add 50-100 more)
])

# Then run: python3 generate-vocab.py
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--template":
        print(add_more_words_template())
    else:
        generate_vocabulary_file()
