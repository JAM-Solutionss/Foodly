import streamlit as st
from backend.modules.llm import foodgpt
from backend.modules.spoonacular import get_recipes
from backend.main import FoodGPT
from backend.modules.food_storage import FoodStorage

st.title("FoodGPT")
if 'food_storage' not in st.session_state:
        st.session_state.food_storage = FoodStorage()

st.subheader("A recipe generator powered by Groq")
# Add Ingredients
def add_ingredient():
    

    if 'clear_inputs' not in st.session_state:
        st.session_state.clear_inputs = False

    if st.session_state.clear_inputs:
        st.session_state.ingredient_input = ''
        st.session_state.amount_input = 0
        st.session_state.clear_inputs = False

    col1, col2 = st.columns([2, 1])
    with col1:
        ingredient = st.text_input("Enter ingredient name", key="ingredient_input")
    with col2:
        amount = st.number_input("Enter amount", min_value=0, step=1, key="amount_input")
    
    if st.button("Add Ingredient"):
        if ingredient and amount > 0:
            st.session_state.food_storage.add_food_item(ingredient, amount)
            st.success(f"Added {amount} of {ingredient}")
            st.session_state.clear_inputs = True
            st.experimental_rerun()
        else:
            st.error("Please enter a valid ingredient and amount")

    # Display current storage
    st.write("Current Storage:")
    for item, quantity in st.session_state.food_storage.get_all_items().items():
        st.write(f"{item}: {quantity}")
add_ingredient()



# Initialize session state
if 'recipes' not in st.session_state:
    st.session_state.recipes = None
if 'selected_recipe' not in st.session_state:
    st.session_state.selected_recipe = None

def get_recipes_from_backend():
    ingredients = []
    for item, quantity in st.session_state.food_storage.get_all_items().items():
        ingredients.append(item)
    print(ingredients)
    
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
                <div class="recipe-name"><h3>{recipe['rname']}</h3></div>
                <img src="{recipe['image_url']}" class="recipe-image">
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"View Details for {recipe['rname']}"):
                st.write("Ingredients:")
                for ingredient in recipe['ingredients']:
                    #ingredient_text = f"{ingredient['Name']}: {ingredient['Amount']} {ingredient['Unit']} ({ingredient['Original']})"
                    st.write(f"- {ingredient}")
                if st.button(f"Analyze Recipe {index + 1}", key=f"analyze_recipe_{index}"):
                    st.session_state.selected_recipe = recipe
                    st.switch_page("webpages/analysis.py")

        st.markdown('</div>', unsafe_allow_html=True)

# Main app flow
if st.button("Get Recipes"):
    get_recipes_from_backend()

display_recipes()
