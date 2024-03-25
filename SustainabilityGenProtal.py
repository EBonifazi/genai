from pathlib import Path
import streamlit as st


    

st.title("Baeringer Schlingelheim: Scope 3 Emissions Insight Platform")

st.map()  # Interactive map placeholder



from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("home.py", 'Home <img src=\"navigation_14019644.png\"/>', "<img src=\"navigation_14019644.png\"/>"),
        # Can use :<icon-name>: or the actual icon
        Page("dashboard.py", "Sustainability AI Analysis", ),
        Page("conversational_ai.py", "Sustainability Agent", ),
        Page("data_submission.py", "Data Submission", ),

    ]
)

add_page_title()  # Optional method to add title and icon to current page


with st.expander("Show documentation"):
    st.help(show_pages)

    st.help(Page)

    st.help(add_page_title) 