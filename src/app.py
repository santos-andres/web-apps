import streamlit as st
import leafmap.foliumap as leafmap


st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <TBD>
    - GitHub repository: <https://github.com/santos-andres/web-apps.git>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Andrés Santos
    """
)

# Customize page title
st.title("Streamlit for GIS Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). 
    Copied from an open-source project at [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
    """
)
st.header("Widgets")
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'Neptune'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.file_uploader('Upload a photo')

st.header("Maps")


m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)