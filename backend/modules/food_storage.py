class FoodStorage:
    def __init__(self):
        self.food_items = {
            "Tomato": 1,
        }
    

    def add_food_item(self, name, amount):
        """
        Adds a new food item to the `food_items` dictionary or updates the amount if it already exists.
        
        Args:
            name (str): The name of the food item.
            amount (int): The amount of the food item.
        
        Returns:
            int: The updated amount of the food item.
        """
        if name in self.food_items:
            self.food_items[name] += amount
        else:
            self.food_items[name] = amount
        
        print(self.food_items)
        return self.food_items[name]

    def get_all_items(self):
        """
        Returns:
            dict: A dictionary of all food items and their amounts.
        """
        return self.food_items


if __name__ == "__main__":
    food_storage = FoodStorage()
    food_storage.add_food_item("Banana", 1)
    food_storage.add_food_item("Tomato", 1)
    print(food_storage.food_items)