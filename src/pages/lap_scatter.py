import streamlit as st
import duckdb
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Plot data", layout="centered")

available_df = duckdb.sql("SHOW TABLES;").to_df()
options = st.multiselect(
    "Columns",
    available_df
)
available_columns = []

for table in options:
    columns = duckdb.sql(f"DESCRIBE {table}").to_df()['column_name'].to_list()
    columns = [f"{table}.{column_name}" for column_name in columns]
    available_columns.extend(columns)

x_axis = st.multiselect(
    "x_axis",
    available_columns
)

y_axis = st.multiselect(
    "y_axis",
    available_columns
)

if x_axis and y_axis:
    #TODO: improve this plotting logic
    table, x_dimension = x_axis[0].split(".")
    x_df = duckdb.query(f"SELECT {x_dimension} from {table}").to_df()
    x_df = x_df.T.to_numpy().squeeze()
    fig = go.Figure()
    for dim in y_axis:
        y_tab, y_dim = dim.split(".")
        y_df = duckdb.query(f"SELECT {y_dim} from {y_tab}").to_df().T.to_numpy().squeeze()
        fig.add_trace(go.Scatter(x=x_df, y=y_df, name=y_tab))

    fig.update_traces(hoverinfo='text', mode='lines')
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    st.plotly_chart(fig, use_container_width=True)
