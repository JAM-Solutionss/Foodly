import requests

def get_recipes(ingredients, number=10, ranking=1, ignore_pantry=True):
    ingredients_str = ','.join(ingredients)
    
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    api_key = 'bb68c5d022d646e893196a5080899a08'

    params = {
        'apiKey': api_key,
        'ingredients': ingredients_str,
        'number': number,
        'ranking': ranking,
        'ignorePantry': ignore_pantry
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            recipes = response.json()
            
            for recipe in recipes:
                print(f"Rezept: {recipe.get('title', 'Nicht verfügbar')}")
                print(f"ID: {recipe.get('id', 'Nicht verfügbar')}")
                print(f"Bild: {recipe.get('image', 'Nicht verfügbar')}")
                print("-----------------------")
        else:
            print(f"Fehler bei der Anfrage. Status-Code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")

api_key = 'dein_api_schluessel'

ingredients_list = ['chicken', 'rice', 'broccoli']

get_recipes(ingredients_list)