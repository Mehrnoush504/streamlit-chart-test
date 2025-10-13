import streamlit as st
import pandas as pd

# Cached function to load CSV from URL
@st.cache_data
def load_csv(url):
    return pd.read_csv(url)

# Load the data
# df = load_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
df = load_csv("C:/Users/Mehrnoush/Desktop/starcoach/Classes/class s00/airtravel.csv")
st.success("CSV loaded successfully!")

# Use Streamlit's line_chart with x='Month' to preserve order
st.line_chart(data=df, x=df.columns[0], y=df.columns[1:4], height=300)