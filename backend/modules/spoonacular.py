import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_recipes(ingredients, ingredient_number=1, max_calories=800, min_protein=0, max_ready_time=1000, servings=2, number=10, ranking=1, ignore_pantry=True):
    ingredients_str = ','.join(ingredients) # combines all ingredients into one string
  
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    api_key = os.getenv('SPOONACULAR_API_KEY')

    params = {
        'apiKey': api_key,
        'ingredients': ingredients_str, # all ingredients
        'ingredientsNumber': ingredient_number, # number of ingredients
        'servings': servings, # number of servings
        'maxCalories': max_calories, # max amount of calories
        'minProtein': min_protein, # min amount of protein
        'maxReadyTime': max_ready_time, # max time to cook
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
                calories = recipe.get('calories', 'N/A') # extract calories
                protein = recipe.get('protein', 'N/A') # extract protein
                fat = recipe.get('fat', 'N/A') # extract fat
                
                missed_ingredients = recipe.get('missedIngredients', [])
                
                sorted_missed_ingredients = sorted(missed_ingredients, key=lambda x: int(x['original'].split()[0]) if x['original'].split()[0].isdigit() else float('inf'))

                recipe_dict = {
                    'RecipeName': recipe_name,
                    'ImageURL': image_url,
                    'Calories': calories,
                    'Protein': protein,
                    'Fat': fat,
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

            for recipe in processed_recipes:
                print(f"Recipe Name: {recipe['RecipeName']}")
                print(f"Image URL: {recipe['ImageURL']}")
                print(f"Calories: {recipe['Calories']}")
                print(f"Protein: {recipe['Protein']}")
                print(f"Fat: {recipe['Fat']}")
                print("Ingredients:")
                for ingredient in recipe['Ingredients']:
                    print(f"  - {ingredient['Name']}: {ingredient['Amount']} {ingredient['Unit']}")
                print("-----------------------")

            return processed_recipes

            # Output for streamlit
            streamlit_output = []
            for recipe in processed_recipes:
                recipe_data = {
                    "rname": recipe['RecipeName'],
                    "image_url": recipe['ImageURL'],
                    "ingredients": [
                        f"{ingredient['Name']}: {ingredient['Amount']} {ingredient['Unit']} ({ingredient['Original']})"
                        for ingredient in recipe['Ingredients']
                    ]
                }
                streamlit_output.append(recipe_data)
            print(streamlit_output)
            return streamlit_output
            
        else:
            print(f'Error in request. Status code: {response.status_code}')
            return None
            
    except requests.exceptions.RequestException as e:
        print(f'Error in request: {e}')
        return None


ingredients_list = ['chicken', 'rice', 'broccoli']
if __name__ == '__main__':
    recipes_list = get_recipes(ingredients_list)
    if recipes_list:
        print(recipes_list)
    else:
        print("No recipes found or an error occurred.")
