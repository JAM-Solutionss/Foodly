import streamlit as st
import openfoodfacts
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.modules import product, filter_nutriments,  nutriments, nutriments_dataframe, nutrigrade, nutriscore, get_multiple_products
from backend.modules import nutriments_filters
import time

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
            width: 100%;
            
            
        }
        .stTextInput > div > div > input {
            height: 2rem;
            line-height: 2rem;
            padding-top: 0;
            padding-bottom: 0;
            font-size: 1.5rem;
            
        }
        .stSelectbox > div > div > div > div > div > div > input {
            height: 2rem;
            line-height: 2rem;
            padding-top: 0;
            padding-bottom: 0;
            font-size: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    
    c = st.container()
    col1, col2 = st.columns([2,1], vertical_alignment="bottom")
    
    
    with col1:
        products = c.text_input("Enter product name", key="product_input", on_change=perform_search)
    with col2:
        if c.button("Search"):
            perform_search()

    if 'search_performed' in st.session_state and st.session_state.search_performed:
        display_product_selection()

def perform_search():
    products = st.session_state.product_input
    if products:
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        progress_text.text("Searching for products...")
        resp_text = api.product.text_search(products)
        progress_bar.progress(50)
        
        progress_text.text("Processing results...")
        multiple_products = get_multiple_products(resp_text)
        progress_bar.progress(90)
        
        st.session_state.products = multiple_products
        st.session_state.search_performed = True
        st.session_state.clear_inputs = False
        
        progress_bar.progress(100)
        progress_text.text("Search complete!")
        time.sleep(0.5)  # Brief pause to show completion
        
        progress_bar.empty()
        progress_text.empty()

def display_product_selection():
    if 'products' in st.session_state and st.session_state.products:
        product_options = [f"{p['product_name']} (Barcode: {p['code']})" for p in st.session_state.products]
        selected_product = st.selectbox("Select a product", product_options)
        
        if selected_product:
            display_product_details(selected_product)

def display_product_details(selected_product):
    barcode = selected_product.split("(Barcode: ")[1].strip(")")
    resp_code = api.product.get(barcode)
    single_product = product(resp_code)
    single_product_copy_filtered = filter_nutriments(single_product, nutriments_filters)
    
    st.subheader("Current Nutrient Data:")
    col1, col2 = st.columns([1.5, 2])
    with col1:
        grade = nutrigrade(single_product_copy_filtered)
        colored_grade = color_nutrigrade(grade)
        st.markdown(f"### Nutrigrade: {colored_grade}", unsafe_allow_html=True)
    with col2:
        st.subheader("Nutrients in 100g:")
        st.write(nutriments_dataframe(single_product_copy_filtered))

        
          
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
    if 'products' in st.session_state and st.session_state.products:
        product_options = [f"{p['product_name']} (Barcode: {p['code']})" for p in st.session_state.products]
        selected_product = st.selectbox("Select a product", product_options)
        
        if selected_product:
            barcode = selected_product.split("(Barcode: ")[1].strip(")")
            resp_code = api.product.get(barcode)
            single_product = product(resp_code)
            single_product_copy_filtered = filter_nutriments(single_product, nutriments_filters)
            
            st.subheader("Current Nutrient Data:")
            col1, col2 = st.columns([1.5, 2])
            with col1:
                grade = nutrigrade(single_product_copy_filtered)
                colored_grade = color_nutrigrade(grade)
                st.markdown(f"### Nutrigrade: {colored_grade}", unsafe_allow_html=True)
            with col2:
                st.subheader("Nutrients in 100g:")
                st.write(nutriments_dataframe(single_product_copy_filtered))
    else:
        st.write("No products found")





    
    
       

search_product()
    

