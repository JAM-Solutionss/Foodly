import openfoodfacts
import json

api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
# Set the global timeout for all API requests
openfoodfacts.api.http_session.timeout = 30

def search_product(item):
    product = api.product.text_search(item)
    return product

def get_product_nutriscore(search_result):
    # Load the JSON data from the file
    with open('nutella_product.json', 'r') as file:
        data = json.load(file)

    # Extract Nutri-Score information
    products = search_result['products']

    # Print Nutri-Score for each product
    for product in products:
        nutri_score = product.get('nutriscore_data', {}).get('grade', 'No Nutri-Score')
        product_name = product.get('product_name', 'Unnamed product')
        print(f"Product: {product_name}, Nutri-Score: {nutri_score}")

if __name__ == "__main__":
    product = search_product("pizza")
    get_product_nutriscore(product)