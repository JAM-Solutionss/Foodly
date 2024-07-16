import pandas as pd
import openfoodfacts

api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
code = "3017620422003"
resp_text = api.product.text_search('Nutella')
resp_code = api.product.get(code)
for key in resp_text.keys():
    print(f'resp_text_keys: {key}')

for key in resp_code.keys():
    print(f'resp_code_keys: {key}')

default_nutriments = [
    'carbohydrates_100g',
    'energy-kcal_100g',
    'fat_100g',
    'sugars_100g',
    
]

def filter_product(product: dict, data_name: str, filters: list):
    data = product[data_name]
    for filter in filters:
        data_filtered = {key: value for key, value in data.items() if filter in key}
        product[data_name] = data_filtered
    
    return product
    

def nutriments(product: dict, filter: list=default_nutriments) -> dict:
    return product['nutriments']

# def nutriments_dataframe(product: dict) -> pd.DataFrame:
#     nutrition_data = pd.DataFrame.from_dict(product['nutriments'])
#     nutrition_data['unit'] pd.DataFrame.from_dict(product['nutriments'])
#     return nutrition_data

def product(response, index: int = 0) -> dict:
    
    if 'count' in response.keys():
        return response['products'][index+1]
    else:
        return response







single_product = product(resp_code)
single_product_keys = list(single_product.keys())
nutriments = nutriments(single_product)
product_filtered = filter_product(single_product, 'nutriments', default_nutriments)
product_filtered['nutriments']




