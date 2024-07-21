import streamlit as st
import fastf1
import pandas as pd

st.title("Race Data Input")
year = int(st.number_input("Year"))
race = st.text_input("Race")

if "dataframes" not in st.session_state:
    st.session_state["dataframes"] = {}

if st.button("Load"):
    sesh = "R"
    session = fastf1.get_session(year, race, sesh)
    session.load(telemetry=True, laps=True, weather=True)
    data_token = f"{year}_{race}_{sesh}"
    st.session_state["dataframes"][data_token] = session.laps
    # st.session_state["available_data"].append(data_token)
    # st.write(st.session_state['laps'])


