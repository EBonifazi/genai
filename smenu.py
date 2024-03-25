import streamlit as st
from streamlit_multi_menu import streamlit_multi_menu

def menu():
    ### Define Menu
    ### Define Menu
    
    page_titles = ["Home",
                   "Sustainability AI Analysis",
                   "Sustainability Agent",
                   "Data Acquisition",
                   ]
    #"Vertex", "Chat", "RAG"
    
    sub_pages = ["home", 
                 "dashboard", 
                 "conversational ai", 
                 "data submission"]
    #,"vertex","chat","rag"
    sub_menus = {"":page_titles}
    # sub_menus = {"Home":["Home","Sustainability"],
    #                "Sustainability":["Sustainability AI Analysis"],
    #                "Agent":["Sustainability Agent"],
    #                "Submission":["Data Submission"]}
    


    # Optinally you can supply google icons
    sub_menu_icons = {
        "": ["home","trending_up", "support_agent","sync_alt"]       
    }

    selected_menu = streamlit_multi_menu(menu_titles=list(sub_menus.keys()),
                                sub_menus=sub_menus,
                                sub_menu_icons = sub_menu_icons,
                                use_container_width=True)
    
    if selected_menu != None:
        #st.write("The selected menu is:",selected_menu)
        from streamlit_extras.switch_page_button import switch_page        
        c = {key: value for key, value in zip(page_titles, sub_pages)}        
        switch_page(c[selected_menu])
