#!/usr/bin/env python3
"""
Categorize top 3000 German words by semantic category.
Only uses rows 1-1029 (valid words; rows 1030+ are garbage).
"""

import csv
import json
from pathlib import Path

CATEGORIES = {
    "grammar": {
        "name": "Grammar & Function Words",
        "emoji": "📝",
        "color": "from-gray-500 to-slate-700",
        "keywords": ["the", "a", "an", "and", "or", "but", "if", "when", "not", "yes", "no", "so", "thus",
                     "in", "on", "at", "to", "for", "with", "by", "of", "from", "out", "up", "over", "under",
                     "after", "before", "through", "around", "above", "how", "where", "why", "what", "there", "here"]
    },
    "pronouns": {
        "name": "Pronouns",
        "emoji": "👤",
        "color": "from-blue-500 to-indigo-600",
        "keywords": ["i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
                     "my", "your", "his", "our", "their", "one", "each", "every", "all", "both", "self", "oneself"]
    },
    "verbs": {
        "name": "Core Verbs",
        "emoji": "⚡",
        "color": "from-yellow-500 to-orange-600",
        "keywords": ["be", "have", "do", "say", "make", "go", "come", "know", "think", "see", "get", "give",
                     "take", "let", "stand", "want", "become", "look", "find", "use", "tell", "call", "keep",
                     "hold", "live", "speak", "write", "read", "work", "play", "help", "need", "try", "ask", "feel", "seem", "mean"]
    },
    "time": {
        "name": "Time & Calendar",
        "emoji": "⏰",
        "color": "from-purple-500 to-violet-600",
        "keywords": ["time", "day", "year", "week", "month", "hour", "minute", "morning", "evening", "night",
                     "today", "tomorrow", "yesterday", "now", "then", "always", "still", "already", "soon", "moment", "clock"]
    },
    "numbers": {
        "name": "Numbers & Quantities",
        "emoji": "🔢",
        "color": "from-teal-500 to-cyan-600",
        "keywords": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                     "hundred", "thousand", "million", "billion", "half", "quarter", "third", "first",
                     "second", "last", "once", "twice", "zero", "number", "percent"]
    },
    "people": {
        "name": "People & Family",
        "emoji": "👨‍👩‍👧",
        "color": "from-pink-500 to-rose-600",
        "keywords": ["man", "woman", "child", "boy", "girl", "mother", "father", "parents", "brother", "sister",
                     "friend", "human", "people", "person", "family", "baby", "son", "daughter", "husband", "wife", "neighbor"]
    },
    "body": {
        "name": "Body & Health",
        "emoji": "💪",
        "color": "from-red-400 to-pink-500",
        "keywords": ["head", "hand", "eye", "hair", "heart", "face", "arm", "leg", "mouth", "ear", "nose",
                     "body", "finger", "foot", "back", "skin"]
    },
    "home": {
        "name": "Home & Buildings",
        "emoji": "🏠",
        "color": "from-amber-500 to-orange-500",
        "keywords": ["house", "room", "door", "window", "bed", "floor", "table", "chair", "kitchen", "school",
                     "city", "street", "building", "place", "wall", "garden"]
    },
    "nature": {
        "name": "Nature & World",
        "emoji": "🌍",
        "color": "from-green-500 to-emerald-600",
        "keywords": ["water", "tree", "land", "air", "light", "world", "earth", "life", "nature", "sun", "moon",
                     "star", "sky", "sea", "forest", "mountain", "river"]
    },
    "feelings": {
        "name": "Feelings & Mind",
        "emoji": "💭",
        "color": "from-indigo-400 to-purple-500",
        "keywords": ["think", "feel", "love", "hope", "fear", "joy", "sense", "reason", "truth", "belief",
                     "thought", "idea", "dream", "memory"]
    },
    "work": {
        "name": "Work & Economy",
        "emoji": "💼",
        "color": "from-stone-500 to-gray-700",
        "keywords": ["work", "money", "job", "question", "problem", "answer", "word", "right", "case", "part",
                     "end", "thing", "example", "kind", "way", "reason", "sense", "page", "state", "matter", "power"]
    },
    "travel": {
        "name": "Travel & Movement",
        "emoji": "🚗",
        "color": "from-blue-400 to-sky-500",
        "keywords": ["car", "road", "street", "way", "go", "come", "run", "walk", "move", "drive", "fly", "ship", "train"]
    },
    "colors": {
        "name": "Colors & Descriptions",
        "emoji": "🎨",
        "color": "from-rose-400 to-pink-600",
        "keywords": ["big", "small", "good", "bad", "new", "old", "long", "short", "great", "simple", "own",
                     "same", "right", "high", "different", "beautiful", "dark", "bright"]
    },
    "other": {
        "name": "Everything Else",
        "emoji": "🌟",
        "color": "from-purple-400 to-blue-400",
        "keywords": []
    }
}

def categorize_word(english_translation):
    """Return category key for a word."""
    en_lower = english_translation.lower()

    for cat_key, cat_data in CATEGORIES.items():
        if cat_key == "other":
            continue
        for keyword in cat_data["keywords"]:
            if en_lower == keyword or en_lower.startswith(keyword + " "):
                return cat_key

    return "other"

def main():
    csv_path = Path.home() / "Downloads" / "top_3000_german_words.csv"
    output_path = Path("words-3000.json")

    # Read CSV, keeping only first 1029 rows (valid words)
    words = []
    with open(csv_path) as f:
        for i, row in enumerate(csv.DictReader(f)):
            if i >= 1029:
                break
            words.append({
                "de": row["German_Word"],
                "en": row["English_Translation"],
                "img": row["Image_URL"]
            })

    # Build category structure
    db = {key: {"name": cat["name"], "emoji": cat["emoji"], "color": cat["color"], "words": []}
          for key, cat in CATEGORIES.items()}

    # Categorize each word
    for word in words:
        cat_key = categorize_word(word["en"])
        db[cat_key]["words"].append(word)

    # Write JSON
    with open(output_path, "w") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    # Print summary
    total = sum(len(cat["words"]) for cat in db.values())
    print(f"✅ Generated {output_path} with {total} words in {len(CATEGORIES)} categories:")
    for key, cat in db.items():
        print(f"  {cat['emoji']} {cat['name']}: {len(cat['words'])} words")

if __name__ == "__main__":
    main()
