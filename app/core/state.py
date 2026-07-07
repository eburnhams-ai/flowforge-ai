import streamlit as st


def init_state() -> None:
    if "page" not in st.session_state:
        st.session_state.page = "dashboard"
    if "recent_activity" not in st.session_state:
        st.session_state.recent_activity = []


def set_page(page_key: str) -> None:
    st.session_state.page = page_key


def add_activity(title: str, detail: str = "") -> None:
    st.session_state.recent_activity.insert(0, {"title": title, "detail": detail})
    st.session_state.recent_activity = st.session_state.recent_activity[:8]
