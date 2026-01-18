import streamlit as st
from ui import side_bar

class MainContent:
    def __init__(self):
        self.set_app_cofig()
        self.sidebar = side_bar.SideBar()
    

    def render_main_content(self):
        self.sidebar.render_sidebar()
        self.sidebar.sidebar_info()

    def set_app_cofig(self, config= {"page_title":"Data Science Application", "page_icon":":bar_chart:", "layout":"wide", "initial_sidebar_state":"expanded"}):
        st.set_page_config(
            page_title=config["page_title"],
            page_icon=config["page_icon"],
            layout=config["layout"],
            initial_sidebar_state=config["initial_sidebar_state"],
        )

    