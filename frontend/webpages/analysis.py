import streamlit as st
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import foodgpt

def show_analysis():
    st.title("Recipe Analysis")
    
    if 'selected_recipe' in st.session_state and st.session_state.selected_recipe:
        recipe = st.session_state.selected_recipe
        st.subheader(f"Analysis for {recipe['RecipeName']}")
        ingredients_list = [ingredient['Name'] for ingredient in recipe['Ingredients']]
        prompt = f"Analyze this recipe and provide cooking tips: {recipe['RecipeName']}. Ingredients: {', '.join(ingredients_list)} and always answer in German!"
        response = foodgpt(prompt)
        
        st.write(response)
    else:
        st.write("No recipe selected for analysis. Please go back and select a recipe.")


show_analysis()