import duckdb
import streamlit as st

st.set_page_config(page_title="Query Data", layout="centered")

st.title("Query Data")

query = st.text_area("SQL Query")

if query:
    main_df = duckdb.sql(query).to_df()
    options = st.multiselect(
        "Columns",
        main_df.columns
    )
    if not options:
        st.dataframe(main_df)
    if options:
        filters = ",".join(options)
        query = f"SELECT {filters} FROM main_df"
        st.code(query, language='SQL')
        df = duckdb.sql(query).to_df()
        st.dataframe(df)



