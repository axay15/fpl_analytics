import streamlit as st
from queries import (
    get_top_captains,
    get_differential_picks
)
from ai_retrieval import (
    get_captain_context,
    get_differentials_context
)
from ai_client import ask_llm
from ai_prompts import captain_prompt


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


st.header("🤖 FPL AI Assistant")

question_type = st.selectbox(
    "What do you want help with?",
    ["Captain Recommendation"]
)

if st.button("Ask AI"):
    if question_type == "Captain Recommendation":
        context = get_captain_context()
        prompt = captain_prompt(context)
        answer = ask_llm(prompt)

        st.subheader("AI Recommendation")
        st.write(answer)
