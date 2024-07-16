from calendar import day_abbr
import pandas as pd
import openfoodfacts
import product_filters

def filter_product(product: dict, product_filters: list) -> dict:
    """Filters product based on the provided "product_filters" dict.

    Args:
        product (dict): Single producct dictionary.
        product_filters (list): Dictionary of product data, that should be kept.

    Returns:
        dict: A new copy of the filtered product dictionary.
    """
    product_copy = product.copy()
    data_filtered = {}
    
    for data, filters in product_filters.items():
    
        for filter in filters:
            for key, value in product[data].items():
                if filter == key:
                    data_filtered[key] = value
                
        product_copy[data] = data_filtered
    
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

def product_data_dataframe(product: dict, data_key: str) -> pd.DataFrame:
    """Extracts single data of the product like e.g. "nutriments" as pandas DataFrame .

    Args:
        product (dict): Single producct dictionary.
        data_key (str): Key of data to extract.

    Returns:
        pd.DataFrame: DataFrame of desired product data specified by "data_key".
    """
    dataframe = pd.DataFrame()
    for key, value in product[data_key].items():
        print(key, value)
        dataframe[key] = [value]
    return dataframe

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
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    code = "3017620422003"
    resp_text = api.product.text_search('Nutella')
    resp_code = api.product.get(code)
    
    for key in resp_text.keys():
        print(f'resp_text_keys: {key}')

    for key in resp_code.keys():
        print(f'resp_code_keys: {key}')

    
    
    single_product = product(resp_code)
    single_product_copy = single_product.copy()
    single_product_copy_keys = list(single_product_copy.keys())
    print(single_product_copy_keys)

    single_product_copy_filtered = filter_product(single_product_copy, default_filters)
    nutriments = product_data(single_product_copy_filtered, 'nutriments')
    nutriments_Dataframe = product_data_dataframe(single_product_copy_filtered, 'nutriments')





