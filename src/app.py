import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello, Streamlit!")
st.header("Getting Started")
st.markdown("This is a simple Streamlit application.")
st.write("Welcome to your first Streamlit app.")

#data 
# Generate 20 random [x, y] pairs
data = [[np.random.random(), np.random.random()] for _ in range(20)]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['x', 'y'])

print(df)
# with matplotlib
fig, ax = plt.subplots()
ax.hist(data, bins=15)
st.pyplot(fig)

# with streamlit
st.bar_chart(df)