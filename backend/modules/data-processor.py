import pandas as pd
import openfoodfacts


def nutritions_table() -> pd.DataFrame:
    pass

api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
code = "3017620422003"
resp = api.product.get(code, fields=["code", "product_name"])