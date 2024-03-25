from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu

pages = {'Home':'pages/home.py',
         'Sustainability AI Analysis':'pages/dashboard.py',
         'Conversational AI':'pages/conversational_ai.py',
         'Data Submission':'pages/data_submission.py'
         }

# Create a list of the page names
page_list = list(pages.keys())

def nav(current_page=page_list[0]):
    with st.sidebar:
        p = option_menu("", page_list, 
            default_index=page_list.index(current_page), 
            orientation="vertical")

        if current_page != p:
            st.switch_page(pages[p])