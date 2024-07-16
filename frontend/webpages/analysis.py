import streamlit as st
from backend.modules.llm import foodgpt

def show_analysis():
    st.title("Recipe Analysis")
    
    if 'selected_recipe' in st.session_state and st.session_state.selected_recipe:
        recipe = st.session_state.selected_recipe
        st.subheader(f"Analysis for {recipe['name']}")
        
        prompt = f"Analyze this recipe and provide cooking tips: {recipe['name']}. Ingredients: {', '.join(recipe['ingredients'])}"
        response = foodgpt(prompt)
        
        st.write(response)
    else:
        st.write("No recipe selected for analysis. Please go back and select a recipe.")


show_analysis()