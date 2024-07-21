import streamlit as st
import pandas as pd


st.set_page_config(page_title="Render Data", layout="centered")

st.title("Render Data")
# data_options = (opt for opt in st.session_state["available_data"]) if "available_data" in st.session_state else ("")
# option = st.selectbox("Enter session data to view",
#                       data_options)
if 'dataframes' in st.session_state:
    df_name = st.selectbox("Select dataframe to view", st.session_state['dataframes'].keys())
    if df_name:
        st.dataframe(st.session_state['dataframes'][df_name])
