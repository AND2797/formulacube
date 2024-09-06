import streamlit as st
import duckdb
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(page_title="Plot data", layout="centered")

available_df = duckdb.sql("SHOW TABLES;").to_df()
selected_df = st.selectbox("Select datasource", available_df['name'].unique())
df = duckdb.sql(f"SELECT * FROM {selected_df}").to_df()
x_axis = st.multiselect(
    "x_axis",
    df.columns
)

y_axis = st.multiselect(
    "y_axis",
    df.columns
)
if x_axis and y_axis:
    # fig = px.line(df, x=df[x_axis].T.to_numpy()[0], y=df[y_axis].T.to_numpy()[0], title="test")
    fig = px.line(df, x=x_axis[0], y=y_axis, title="test")
    st.plotly_chart(fig, use_container_width=True)
