from modules.llm import foodgpt

# Dummy Data for testing purpose in a dictionary with amount
food_items = {
    'Tomaten': 1,
    'Kartoffeln': 2,
    'Brot': 3,
    'Käse': 4,
    'Salat': 5,
    'Pizza': 6,
    'Schnitzel': 7,
    'Kuchen': 8,
    'Mozarella': 9,
    'Ketchup': 10,
    'Schokolade': 11,
    'Eier': 12,
    'Salami': 13,
    'Paprika': 14,
    'Zwiebel': 15,
    'Mais': 16,
    'Pilz': 17,
    'Butter': 18,
}

print(foodgpt(f"Suche die besten Zutaten um ein leckeres Essen zu machen aus folgender Liste: {food_items.keys()}"))