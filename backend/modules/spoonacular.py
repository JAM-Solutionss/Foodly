import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_recipes(ingredients, ingredient_number=1, max_calories=800, min_protein=0, max_ready_time=1000, servings=2, number=10, ranking=1, ignore_pantry=True):
    ingredients_str = ','.join(ingredients)
    
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    api_key = os.getenv('SPOONACULAR_API_KEY')

    params = {
        'apiKey': api_key,
        'ingredients': ingredients_str,
        'ingredientsNumber': ingredient_number,
        'servings': servings,
        'maxCalories': max_calories,
        'minProtein': min_protein,
        'maxReadTime': max_ready_time,
        'number': number,  # Number of recipes to retrieve
        'ranking': ranking,  # 1 = popularity, 2 = healthier
        'ignorePantry': ignore_pantry  # True = only our ingredients, False = allow other ingredients
    }
    
    try:
        # Send API request
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            recipes = response.json()

            processed_recipes = []

            for recipe in recipes:
                recipe_name = recipe.get('title', 'No title available')
                image_url = recipe.get('image', 'No image available')
                
                missed_ingredients = recipe.get('missedIngredients', [])
                
                sorted_missed_ingredients = sorted(missed_ingredients, key=lambda x: int(x['original'].split()[0]) if x['original'].split()[0].isdigit() else float('inf'))

                recipe_dict = {
                    'RecipeName': recipe_name,
                    'ImageURL': image_url,
                    'Ingredients': []
                }

                for ingredient in sorted_missed_ingredients:
                    ingredient_name = ingredient.get('name', 'Unknown')
                    ingredient_amount = ingredient.get('amount', 'Unknown')
                    ingredient_unit = ingredient.get('unit', '')
                    ingredient_original = ingredient.get('original', 'Unknown')

                    ingredient_dict = {
                        'Name': ingredient_name,
                        'Amount': ingredient_amount,
                        'Unit': ingredient_unit,
                        'Original': ingredient_original
                    }

                    recipe_dict['Ingredients'].append(ingredient_dict)

                processed_recipes.append(recipe_dict)

            for recipe in recipes:
                print(f"Recipe Name: {recipe['RecipeName']}")
                print(f"Image URL: {recipe['ImageURL']}")
                print("Ingredients:")
                for ingredient in recipe['Ingredients']:
                    print(f"  - {ingredient['Name']}: {ingredient['Amount']} {ingredient['Unit']}")
                print("-----------------------")

            print(recipe_dict)

        else:
            print(f'Error in request. Status code: {response.status_code}')
            
    except requests.exceptions.RequestException as e:
        print(f'Error in request: {e}')


ingredients_list = ['chicken', 'rice', 'broccoli']

list = get_recipes(ingredients_list)
print(list)