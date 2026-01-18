import streamlit as st

from ui.pages import page_teste
class SideBar:

    def render_sidebar(self):
        st.sidebar.title("Escolha o que deseja visualizar")
        selection = st.sidebar.radio("Select an option", ["Home"])
        
        if selection == "Home":
            page_teste.render_page_content()