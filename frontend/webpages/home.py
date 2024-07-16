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
    recipes = get_recipes(ingredients)
    num_columns = 2
    #for recipe in recipes:
    #    st.header(recipe['name'])
    #    st.image(recipe['image_url'])
    #    st.subheader("Ingredients:")
    #    for ingredient in recipe['ingredients']:
    #        st.write(ingredient)
    #    st.markdown("---")
    #for i in range(0, len(recipes), num_columns):
    #    cols = st.columns(num_columns)
    #    for j in range(num_columns):
    #        if i + j < len(recipes):
    #            recipe = recipes[i + j]
    #            with cols[j]:
    #                st.subheader(recipe['name'])
    #                st.image(recipe['image_url'], use_column_width=True)
    #                with st.expander("View Details"):
    #                    st.write("Ingredients:")
    #                    for ingredient in recipe['ingredients']:
    #                        st.write(f"- {ingredient}")
    #                st.write("---")


   # CSS to create a grid layout with equal height tiles
    st.markdown("""
        <style>
        .recipe-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
        }
        .recipe-tile {
            display: flex;
            flex-direction: column;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
        }
        .recipe-name {
            padding: 0.5rem;
            background-color: #ffd8fb;
        }
        .recipe-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        h3 {
            color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

    # Create the grid container
    st.markdown('<div class="recipe-grid">', unsafe_allow_html=True)

    # Add recipes to the grid
    for recipe in recipes:
        st.markdown(f"""
        <div class="recipe-tile">
            <div class="recipe-name"><h3>{recipe['name']}</h3></div>
            <img src="{recipe['image_url']}" class="recipe-image">
        </div>
        """, unsafe_allow_html=True)
        
        # Use Streamlit components for interactive elements
        with st.expander("View Details"):
            st.write("Ingredients:")
            for ingredient in recipe['ingredients']:
                st.write(f"- {ingredient}")

    # Close the grid container
    st.markdown('</div>', unsafe_allow_html=True)

st.button("Get Recipes", on_click=lambda: get_recipes_from_backend())