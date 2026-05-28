import env_bootstrap  # noqa: F401 — loads `.env` before Streamlit / Tabs import

import streamlit as st
from ui_theme import inject_global_styles
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

# Configure the app
st.set_page_config(
    page_title = 'Diabetes Prediction System',
    page_icon = '🩺',
    layout = 'wide',
    initial_sidebar_state = 'auto',
)

inject_global_styles()

Tabs = {
    "Home":home,
    "Ask Queries":talk2doc,
    "Diagnosis":diagnosis,
    "Result":result,
    "Knowledge Center":kc
}

st.sidebar.title('Navigation')

page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made By Dhruv Paliwal')

df, X, y = load_data()

if page in ["Diagnosis"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
