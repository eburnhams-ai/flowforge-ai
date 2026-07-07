import streamlit as st

from components.sidebar import render_sidebar
from components.topbar import render_topbar
from core.router import render_current_page
from core.state import init_state
from core.theme import load_theme


def run() -> None:
    st.set_page_config(
        page_title="FlowForge",
        page_icon="▣",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    init_state()
    load_theme()

    render_sidebar()
    render_topbar()
    render_current_page(st.session_state.page)
