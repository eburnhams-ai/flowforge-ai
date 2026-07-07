import streamlit as st


def tool_tile(icon, title, description, status):
    status_labels = {
        "Ready": "Available now",
        "Next": "Coming next",
        "Planned": "On the roadmap",
        "Coming Soon": "Coming soon",
    }

    detail = status_labels.get(status, status)

    with st.container(border=True):
        st.caption(status.upper())
        st.markdown(f"## {title}")
        st.write(description)
        st.caption(detail)