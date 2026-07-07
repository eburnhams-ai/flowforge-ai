import streamlit as st


def topbar():
    left, right = st.columns([3, 1])

    with left:
        st.caption("FlowForge Core")

    with right:
        st.caption("v0.5 • Local")