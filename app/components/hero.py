import streamlit as st


def hero(title: str, subtitle: str):
    st.title(title)
    st.caption(subtitle)
    st.write("")