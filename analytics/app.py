import streamlit as st
from queries import (
    get_top_captains,
    get_differential_picks
)

st.set_page_config(
    page_title="FPL Smart Assistant",
    layout="wide"
)

st.title("⚽ FPL Smart Assistant — Analytics")

st.markdown(
    """
    This dashboard is powered by an automated data pipeline:
    - FPL API ingestion
    - dbt transformations (bronze → silver → gold)
    - DuckDB analytics warehouse
    """
)

st.header("🔥 Top Captain Picks")
captains = get_top_captains()
st.dataframe(captains, use_container_width=True)

st.header("🎯 Differential Picks (<10% ownership)")
differentials = get_differential_picks()
st.dataframe(differentials, use_container_width=True)
