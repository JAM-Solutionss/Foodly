import openfoodfacts

# User-Agent is mandatory
api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")

product = api.product.text_search("nutella")
print(product)
#code = "3017620422003"
#api.product.get(code, fields=["code", "product_name"])