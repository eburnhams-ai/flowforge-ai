import streamlit as st


def stat_card(title, value, subtitle):
    st.metric(title, value)
    st.caption(subtitle)