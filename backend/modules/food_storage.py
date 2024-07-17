class FoodStorage:
    def __init__(self):
        self.food_items = {
            }
           
        
    def add_food_item(self, item_name):
        if item_name not in self.food_items.values():
            new_id = max(self.food_items.keys()) + 1 if self.food_items else 1
            self.food_items[new_id] = item_name
            return True
        return False
        


    def get_all_items(self):
        """
        Returns:
            dict: A dictionary of all food items and their amounts.
        """
        return self.food_items


if __name__ == "__main__":
    food_storage = FoodStorage()
    food_storage.add_food_item("Banana")
    food_storage.add_food_item("Tomato")
    print(food_storage.food_items)