import streamlit as st

from components.hero import hero
from components.section import section


def render_settings() -> None:
    hero("Settings", "Control how FlowForge looks and behaves.")

    section("Appearance")
    with st.container(border=True):
        st.radio("Theme", ["Light", "Dark"], horizontal=True, disabled=True)
        st.caption("Dark mode is planned for the next UI polish sprint.")

    section("Defaults")
    with st.container(border=True):
        st.text_input("Default export name", value="flowforge_output")
        st.checkbox("Show advanced options", value=False)
