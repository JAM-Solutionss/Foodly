import pandas as pd
import openfoodfacts
from .product_filters import nutriments_filters

def filter_nutriments(product: dict, nutriments_filters: list) -> dict:
    """Filters product nutriments based on the provided "nutriments_filters" list.

    Args:
        product (dict): Single producct dictionary.
        product_filters (list): List of product nutriments, that should be kept.

    Returns:
        dict: A new copy of the filtered product dictionary.
    """
    product_copy = product.copy()
    data_filtered = {}
    
    for filter in nutriments_filters:
        for key, value in product['nutriments'].items():
            if filter == key:
                data_filtered[key] = value
                
        product_copy['nutriments'] = data_filtered
    
    return product_copy

 
def product_data(product: dict, data_key: str) -> dict:
    """Extracts single data of the product like e.g. "nutriments" as dictionary.

    Args:
        product (dict): Single producct dictionary.
        data_key (str): Key of data to extract.

    Returns:
        dict: Dictionary of desired product data specified by "data_key".
    """
    return product[data_key]   


def nutriments(product: dict) -> dict:
    """Return nutriments data as dictionary.

    Args:
        product (dict): Single producct dictionary.

    Returns:
        dict: Dictionary if product nutriments.
    """
    return product_data(product, "nutriments")


def nutriments_dataframe(product: dict) -> pd.DataFrame:
    """Return nutriments data as datafrane.

    Args:
        product (dict): Single producct dictionary.

    Returns:
        pd.DataFrame: Dataframe if product nutriments.
    """
    nutriments_dict = nutriments(product)
    nutriments_df = pd.DataFrame()
    parameters = []
    units= []
    values = []
    
    for key, value in nutriments_dict.items():
        if key.endswith('_unit'):
            units.append(value)
        else:
            parameters.append(key.replace('_100g', '').replace('_', ' ').capitalize())
            values.append(value)
            
    nutriments_df = pd.DataFrame({
        'Nutriment': parameters,
        'Value': values,
        'Unit': units
    })
    
    return nutriments_df

def nutriscore(product: dict) -> int:
    """Returns the nutriscore integer.

    Args:
        product (dict): Single producct dictionary.

    Returns:
        tuple[str,int]: Integer nutriscore.
    """
    nutriscore_score = product_data(product, "nutriscore_score")
    return nutriscore_score

def nutrigrade(product: dict) -> str:
    """Returns the nutrigrade ('a' to 'e') as string.

    Args:
        product (dict): Single producct dictionary.

    Returns:
        tuple[str,int]: String nutrigrage.
    """
    nutriscore_grade = product_data(product, "nutriscore_grade")
    return nutriscore_grade



def product(response, index: int = 0) -> dict:
    """Extract a single product from the response specified by "index".
    If the response contains only one product, the single product will be returned.

    Args:
        response (_type_): Response dictionary of API Call.
        index (int, optional): Index number of product to extract. Counting from 1.

    Returns:
        dict: Dictionary of single product.
    """
    
    if 'count' in response.keys():
        return response['products'][index-1]
    else:
        return response





if __name__ == '__main__':
    # Some example usage
    
    # Getting API response
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    code = "3017620422003"
    resp_text = api.product.text_search('Nutella')
    resp_code = api.product.get(code)
    
    # Printing all keys
    for key in resp_text.keys():
        print(f'resp_text_keys: {key}')

    for key in resp_code.keys():
        print(f'resp_code_keys: {key}')

    
    # Extract a single product
    single_product = product(resp_code)
    single_product_copy = single_product.copy()
    
    # Inspecting all data keys
    single_product_copy_keys = list(single_product_copy.keys())
    print(single_product_copy_keys)

    # Filter product based an filters in product_filters
    single_product_copy_filtered = filter_nutriments(single_product_copy, nutriments_filters)
    
    # Getting nutriments as dictionary and DataFrame
    nutriments_dict = nutriments(single_product_copy_filtered)
    nutriments_Dataframe = nutriments_dataframe(single_product_copy_filtered)
    print(f'{nutriments_dict}\n\n')
    print(f'{nutriments_Dataframe}\n\n')
    
    # Getting nutriscore grade and score
    nutriscore_grade = nutrigrade(single_product_copy_filtered)
    nutriscore_score = nutriscore(single_product_copy_filtered)
    
    print(f'Nutriscore grade: {nutriscore_grade}\nNutriscore score: {nutriscore_score}')




