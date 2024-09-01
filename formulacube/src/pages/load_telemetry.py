import streamlit as st
import duckdb

st.set_page_config(page_title="Load Telemetry", layout="centered")

if 'dataframes' in st.session_state:
    df_name = st.selectbox("Select session for telemetry", st.session_state['dataframes'].keys())
    if df_name:
        df = st.session_state['dataframes'][df_name]
        driver = st.selectbox("Select driver for telemetry", df.laps['Driver'].unique())
        driver_laps = df.laps.pick_driver(driver)
        laps = st.text_input("Input")
        if st.button('Load'):
            telemetry_key = f"{df_name}_{driver}_{laps}"
            laps_df = driver_laps.pick_laps(int(laps))
            telemetry = laps_df.get_telemetry()
            tdelta_cols = list(telemetry.select_dtypes(include='timedelta64[ns]').columns)
            start_time = df.event['Session5Date']
            for col in tdelta_cols:
                telemetry[col] = start_time + telemetry[col]
            sql_str = f"CREATE TABLE {telemetry_key} AS SELECT * FROM telemetry"
            print(f"created {telemetry_key}")
            duckdb.sql(sql_str)








