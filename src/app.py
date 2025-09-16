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

st.header("Maps")


m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)