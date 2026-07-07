import streamlit as st


def section(title, subtitle=None):
    st.subheader(title)
    if subtitle:
        st.caption(subtitle)