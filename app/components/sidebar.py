import streamlit as st
from core.navigation import NAV_ITEMS


def sidebar():
    st.sidebar.markdown("## ⚙️ FlowForge")
    st.sidebar.caption("Automate. Organize. Optimize.")
    st.sidebar.divider()

    groups = {}
    for item in NAV_ITEMS:
        groups.setdefault(item["group"], []).append(item["label"])

    options = []
    for group, labels in groups.items():
        st.sidebar.caption(group.upper())
        options.extend(labels)

    return st.sidebar.radio("Navigation", options, label_visibility="collapsed")