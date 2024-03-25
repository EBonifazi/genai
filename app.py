import streamlit as st
from streamlit_multi_menu import streamlit_multi_menu

st.set_page_config(layout="wide")

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with st.sidebar:
    import smenu
    smenu.menu()