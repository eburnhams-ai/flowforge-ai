import streamlit as st


def empty_state(title: str, message: str) -> None:
    with st.container(border=True):
        st.subheader(title)
        st.write(message)
