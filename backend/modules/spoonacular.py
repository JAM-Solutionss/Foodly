import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_recipes(ingredients, number=10, ranking=1, ignore_pantry=True):
    ingredients_str = ','.join(ingredients)
    
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    api_key = os.getenv('SPOONACULAR_API_KEY')

    params = {
        'apiKey': api_key,
        'ingredients': ingredients_str,
        'number': number,  # Number of recipes to retrieve
        'ranking': ranking,  # 1 = popularity, 2 = healthier
        'ignorePantry': ignore_pantry  # True = only our ingredients, False = allow other ingredients
    }
    
    try:
        # Send API request
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            recipes = response.json()

            # Check if recipes.json already exists
            file_path = 'recipes.json'
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(recipes, f, ensure_ascii=False, indent=4)
                print(f'Created new file {file_path}')
            else:
                print(f'{file_path} already exists. Skipping creation.')

        else:
            print(f'Error in request. Status code: {response.status_code}')
            
    except requests.exceptions.RequestException as e:
        print(f'Error in request: {e}')


ingredients_list = ['chicken', 'rice', 'broccoli']

get_recipes(ingredients_list)