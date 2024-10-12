import streamlit as st
import fastf1
import pandas as pd
import duckdb

st.title("Load Session")
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
    laps_data = session.laps
    tdelta_cols = list(laps_data.select_dtypes(include='timedelta64[ns]').columns)
    for col in tdelta_cols:
        #TODO: LapTime is fucked up. Cannot add starting time to LapTime.
        laps_data[col] = start_time + laps_data[col]

    duckdb.sql(f"CREATE TABLE {data_token}_laps AS SELECT * FROM laps_data")

