import streamlit as st

from ui.pages import home_page

class SideBar:

    def render_sidebar(self):
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Select an option", ["Home"])
        
        if selection == "Home":
            home_page.render_home_page()
    
    def sidebar_info(self):
        st.sidebar.markdown("---")
        st.sidebar.markdown("Data Science Application v1.0")