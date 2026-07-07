import streamlit as st


def stat_card(label: str, value: str, detail: str | None = None) -> None:
    st.metric(label, value)
    if detail:
        st.caption(detail)
