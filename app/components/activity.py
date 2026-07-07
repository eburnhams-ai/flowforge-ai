import streamlit as st


def activity_feed(items: list[dict]) -> None:
    with st.container(border=True):
        if not items:
            st.write("No recent jobs yet.")
            st.caption("Completed automations will appear here.")
            return

        for item in items:
            st.write(f"✓ {item.get('title', 'Completed job')}")
            detail = item.get("detail")
            if detail:
                st.caption(detail)
