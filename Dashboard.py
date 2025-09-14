import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="PROHI Dashboard LALE7029",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

# INPUT WIDGETS 
selected_region = st.selectbox("Select region", ["Lisbon", "Oporto"])
selected_channel = st.radio("Select channel", ["Hotel, restaurant and cafe", "Retail"])
selected_products = st.multiselect("Choose product categories", ["Fresh", "Milk", "Grocery"])

# DATA ELEMENT
st.markdown("Product data")
df = pd.DataFrame(np.random.randn(10, 3), columns=["Fresh", "Milk", "Grocery"])
st.dataframe(df)

# CHART
st.markdown("Product chart")
st.bar_chart(df[["Fresh", "Milk", "Grocery"]].sum())
