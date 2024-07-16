import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.modules.llm import foodgpt
from backend.modules.spoonacular import get_recipes
from backend.main import FoodGPT
import pandas as pd

st.title("FoodGPT")

def generate_meal():
    # Get the items from the food items list in FoodGPT 
    foodgpt_food_items = FoodGPT().food_items
    prompt = f"Suche die besten Zutaten um ein leckeres Essen zu machen aus folgender Liste: {foodgpt_food_items.keys()}"
    with st.chat_message("AI Assistant"):
        st.write(foodgpt(prompt))

st.button("Generate Food", on_click=lambda: generate_meal())

def get_recipes_from_backend():
    ingredients = FoodGPT().food_items.keys()
    get_recipes(ingredients)

st.button("Get Recipes", on_click=lambda: get_recipes_from_backend())