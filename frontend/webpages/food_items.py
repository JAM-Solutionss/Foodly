import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.modules.llm import foodgpt
from backend.main import FoodGPT
import pandas as pd


foodgpt_food_items = FoodGPT().food_items
df = pd.DataFrame(foodgpt_food_items.items(), columns=["Item", "Amount"])

st.title("Food Database")

if st.checkbox("Show Food Items"):
    st.subheader("This is the list of food items from the FoodGPT model:")
    st.write(df)