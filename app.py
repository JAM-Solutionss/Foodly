import streamlit as st

# Pages
home = st.Page(
    "frontend/webpages/home.py",
    title="Home",
    icon=":material/home:"
)

about = st.Page(
    "frontend/webpages/about.py",
    title="About",
    icon=":material/info:"
)


analysis = st.Page(
    "frontend/webpages/analysis.py",
    title="Recipe Analysis",
    icon=":material/database:"
)

find_recipe = st.Page(
    "frontend/webpages/spoonview.py",
    title="Find Recipe",
    icon=":material/search:"
)

# Navigation
pg = st.navigation({"Menu": [home, about]})

pg.run()




# Get LLM Response

