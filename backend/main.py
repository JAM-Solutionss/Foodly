from .modules import foodgpt


class FoodGPT:
    def __init__(self):
        # Dummy Data for testing purpose in a dictionary with amount
        self.food_items = {
            'tomato': 1,
            'potatos': 2,
            'bread': 3,
            'cheese': 4,
            'salad': 5,
            'pizza': 6,
            'steak': 7,
            'onions': 8,
            'mozarella': 9,
            'ketchup': 10,
            'chocolate': 11,
            'eggs': 12,
            'salami': 13,
            'banana': 14,
            'beef': 16,
            'groundturkey': 17,
            'butter': 18,
        }

#print(foodgpt(f"Suche die besten Zutaten um ein leckeres Essen zu machen aus folgender Liste: {food_items.keys()}"))