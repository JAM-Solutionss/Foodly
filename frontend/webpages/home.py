import streamlit as st
import openfoodfacts
from backend.modules.data_processor import product, filter_nutriments,  nutriments, nutriments_dataframe, nutrigrade, nutriscore
from backend.modules.product_filters import nutriments_filters

#Functions
def get_product_nutriments(product: dict) -> dict:
    """Return nutriments data as dictionary."""
    nutriments_dict = nutriments(product)


st.title("FoodFacts")
# Getting API response
api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0", timeout=100)
#code = "3017620422003"
#resp_text = api.product.text_search('Nutella')
#resp_code = api.product.get(code)
    

def search_product():
    
    if 'clear_inputs' not in st.session_state:
        st.session_state.clear_inputs = False

    if st.session_state.clear_inputs:
        st.session_state.product_input = ''
        st.session_state.clear_inputs = False

     # Custom CSS to align button and input heights
    st.markdown("""
        <style>
        .stButton > button {
            height: 3rem;
            margin-top: 1.5rem;
        }
        .stTextInput > div > div > input {
            height: 3rem;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])
    with col1:
        products = st.text_input("Enter product name", key="product_input", on_change=perform_search)
    with col2:
        if st.button("Search"):
            perform_search()
        # Create a placeholder for search results
    results_placeholder = st.empty()
    with results_placeholder:
                display_data()


def perform_search():
    products = st.session_state.product_input
    if products:
        resp_text = api.product.text_search(products)
        single_product = product(resp_text)
        single_product_copy = single_product.copy()
        single_product_copy_filtered = filter_nutriments(single_product_copy, nutriments_filters)
        st.session_state.single_product = single_product_copy_filtered
        st.success(f"Found {st.session_state.single_product['product_name']}")
        st.session_state.clear_inputs = False
        

        
          
def color_nutrigrade(grade):
    grade = grade.upper()
    if grade in ['A', 'B']:
        return f"<span style='color: green;'>{grade}</span>"
    elif grade in ['C']:
        return f"<span style='color: yellow;'>{grade}</span>"
    elif grade in ['D', 'E']:
        return f"<span style='color: red;'>{grade}</span>"
    else:
        return "Unknown"      
        
def display_data():
    # Display current nutrient data
    
    if st.session_state.single_product:
        st.subheader("Current Nutrient Data:")
        col1, col2 = st.columns([1.5, 2])
        with col1:
            grade = nutrigrade(st.session_state.single_product)
            colored_grade = color_nutrigrade(grade)
            st.markdown(f"### Nutrigrade: {colored_grade}", unsafe_allow_html=True)
        with col2:
            st.subheader("Nutrients in 100g:")
            st.write(nutriments_dataframe(st.session_state.single_product))
    else:
        st.write("No product found")
    
    
       

search_product()
    

