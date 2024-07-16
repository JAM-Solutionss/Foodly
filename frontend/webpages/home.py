import streamlit as st
from backend.modules.llm import foodgpt
from backend.modules.spoonacular import get_recipes
from backend.main import FoodGPT

st.title("FoodGPT")

# Initialize session state
if 'recipes' not in st.session_state:
    st.session_state.recipes = None
if 'selected_recipe' not in st.session_state:
    st.session_state.selected_recipe = None

def get_recipes_from_backend():
    ingredients = FoodGPT().food_items.keys()
    st.session_state.recipes = get_recipes(ingredients)

def display_recipes():
    if st.session_state.recipes:
        # Your existing CSS styles here
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
        st.markdown('<div class="recipe-grid">', unsafe_allow_html=True)
        for index, recipe in enumerate(st.session_state.recipes):
            st.markdown(f"""
            <div class="recipe-tile">
                <div class="recipe-name"><h3>{recipe['name']}</h3></div>
                <img src="{recipe['image_url']}" class="recipe-image">
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"View Details for {recipe['name']}"):
                st.write("Ingredients:")
                for ingredient in recipe['ingredients']:
                    st.write(f"- {ingredient}")
                if st.button(f"Analyze Recipe {index + 1}", key=f"analyze_recipe_{index}"):
                    st.session_state.selected_recipe = recipe
                    st.switch_page("webpages/analysis.py")

        st.markdown('</div>', unsafe_allow_html=True)

# Main app flow
if st.button("Get Recipes"):
    get_recipes_from_backend()

display_recipes()
