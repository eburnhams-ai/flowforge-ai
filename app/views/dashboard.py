import streamlit as st


def show_dashboard():
    st.title("FlowForge AI")
    st.subheader("Automate repetitive business tasks in seconds.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tools Available", "6")
    col2.metric("Files Processed", "0")
    col3.metric("Duplicates Found", "0")
    col4.metric("Time Saved", "0 hrs")

    st.markdown("---")

    st.markdown("### Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("📂 File Organizer\n\nSort files into clean folders.")

    with c2:
        st.info("🔍 Duplicate Finder\n\nFind duplicate files by content.")

    with c3:
        st.info("📄 PDF Tools\n\nMerge, split, and compress PDFs.")