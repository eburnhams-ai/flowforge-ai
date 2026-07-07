import streamlit as st


def tool_tile(icon, title, description, status):
    with st.container(border=True):
        st.caption(status)
        st.subheader(f"{icon} {title}")
        st.write(description)