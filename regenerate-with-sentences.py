#!/usr/bin/env python3
"""
Add sentences to all vocabulary categories
"""

# Comprehensive vocabulary with sentences
COMPLETE_VOCAB = {
    "colors": [
        ("red", "rot", "die", "🔴", "Red is a bright color.", "लाल एक चमकीला रंग है।", "Rot ist eine helle Farbe."),
        ("blue", "blau", "die", "🔵", "Blue is the color of the sky.", "नीला आसमान का रंग है।", "Blau ist die Farbe des Himmels."),
        ("yellow", "gelb", "die", "🟡", "Yellow is a warm color.", "पीला एक गर्म रंग है।", "Gelb ist eine warme Farbe."),
        ("green", "grün", "die", "🟢", "Green is the color of grass.", "हरा घास का रंग है।", "Grün ist die Farbe von Gras."),
    ],
    "clothes": [
        ("pants", "Hose", "die", "👖", "I wear pants every day.", "मैं हर दिन पैंट पहनता हूँ।", "Ich trage jeden Tag Hosen."),
        ("shirt", "T-Shirt", "das", "👕", "A shirt covers the body.", "शर्ट शरीर को ढकती है।", "Ein T-Shirt bedeckt den Körper."),
        ("shoe", "Schuh", "der", "👟", "Shoes protect the feet.", "जूते पैरों की सुरक्षा करते हैं।", "Schuhe schützen die Füße."),
        ("hat", "Hut", "der", "🧢", "A hat covers the head.", "टोपी सिर को ढकती है।", "Ein Hut bedeckt den Kopf."),
    ],
    "home": [
        ("bed", "Bett", "das", "🛏️", "I sleep on a bed.", "मैं बिस्तर पर सोता हूँ।", "Ich schlafe auf einem Bett."),
        ("chair", "Stuhl", "der", "🪑", "A chair is for sitting.", "कुर्सी बैठने के लिए है।", "Ein Stuhl ist zum Sitzen."),
        ("table", "Tisch", "der", "🪑", "A table is for eating.", "टेबल खाने के लिए है।", "Ein Tisch ist zum Essen."),
        ("door", "Tür", "die", "🚪", "A door opens the house.", "दरवाज़ा घर को खोलता है।", "Eine Tür öffnet das Haus."),
    ]
}

print("✅ Vocabulary data prepared with sentences")
print("\nCategories ready:")
for cat, words in COMPLETE_VOCAB.items():
    print(f"  {cat}: {len(words)} words with English, Hindi, and German sentences")

