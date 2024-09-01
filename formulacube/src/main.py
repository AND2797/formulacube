import streamlit as st
import fastf1
import pandas as pd
import duckdb

st.title("Race Data Input")
year = int(st.number_input("Year"))
race = st.text_input("Race")
race_session = st.text_input("Session")


if "dataframes" not in st.session_state:
    st.session_state["dataframes"] = {}


if st.button("Load"):
    session = fastf1.get_session(year, race, race_session)
    session.load(telemetry=True, laps=True, weather=True)
    data_token = f"{race}_{year}_{race_session}_Session"
    start_time = session.event['Session5Date']
    st.session_state['dataframes'][data_token] = session

