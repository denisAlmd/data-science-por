from data_loader import data_loader as dl
import streamlit as st

@st.cache_data
def load_data(file_path):
    data_loader = dl.DataLoader()
    return data_loader.load_data(file_path)

def render_home_page():
    header_home_page()
    content_home_page()
    footer_home_page()

def content_home_page():
    with st.spinner("Loading World Cup Matches Data..."):
        st.subheader("World Cup Matches Data Overview")
        sample_data = load_data("data/WorldCupMatches.csv")

    if not sample_data.empty:
        st.write("Here is a preview of the World Cup Matches data:")
        st.dataframe(sample_data.head())

    st.subheader("Number of Matches per Year")
    matches_per_year = sample_data['Year'].value_counts().sort_index()
    st.bar_chart(matches_per_year, width='stretch', x_label='Year', y_label='Number of Matches')

def header_home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page of the Data Science Application.")
    st.write("Here you can find various data visualizations and analyses. Feel free to explore and suggest improvements!")
    st.write('Below you will find some sample content.')
    st.markdown("---")

def footer_home_page():
    st.markdown("---")
    st.write("© 2024 Data Science Application. All rights reserved.")
