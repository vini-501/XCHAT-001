import streamlit as st
import pandas as pd

st.set_page_config(page_title="dashboard", page_icon="📊", layout="wide")

st.title("📊 Data Viewer")

# Example dataframe
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 78]
})

st.write("Here’s a simple dataframe:")
st.dataframe(df)
