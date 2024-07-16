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

default_filters = {
    'nutriments': [
        'carbohydrates_100g',
        'carbohydrates_unit'
        'energy-kcal_100g',
        'energy-kcal_unit',
        'fat_100g',
        'fat_unit',
        'sugars_100g',
        'sugars_unit'        
    ]
}



def filter_product(product: dict, product_filters: list) -> dict:
    
    product_copy = product.copy()
    data_filtered = {}
    
    for data, filters in product_filters.items():
    
        for filter in filters:
            for key, value in product[data].items():
                if filter == key:
                    data_filtered[key] = value
                
        product_copy[data] = data_filtered
    
    return product_copy
    

def nutriments(product: dict) -> dict:
    return product['nutriments']

def nutriments_dataframe(product: dict) -> pd.DataFrame:
    nutrition_data = pd.DataFrame.from_dict(product['nutriments'])
    return nutrition_data

def product(response, index: int = 0) -> dict:
    
    if 'count' in response.keys():
        return response['products'][index+1]
    else:
        return response






single_product = product(resp_code)
single_product_keys = list(single_product.keys())
single_product_copy = single_product.copy()
print(list(single_product_copy['nutriments'].keys()))

single_product_copy_filtered = filter_product(single_product_copy, default_filters)
nutriments_data = nutriments(single_product_copy)

product_filtered = filter_product(single_product_copy, default_filters)
product_filtered['nutriments']





