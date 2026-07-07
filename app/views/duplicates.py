import streamlit as st

from components.hero import hero
from components.section import section
from core.state import add_activity
from modules.duplicate_finder import build_duplicate_report_csv, find_duplicates, format_size


def render_duplicates() -> None:
    hero("Duplicate Finder", "Find true duplicate files by comparing file contents.")

    section("Upload")
    uploaded_files = st.file_uploader("Upload files to scan", accept_multiple_files=True, key="duplicate_uploads")

    if uploaded_files:
        st.info(f"{len(uploaded_files)} files ready to scan.")

    if st.button("Scan for Duplicates", type="primary"):
        if not uploaded_files:
            st.error("Please upload files first.")
            return

        with st.spinner("Scanning files by content…"):
            duplicate_groups, duplicate_count, recoverable_space = find_duplicates(uploaded_files)

        add_activity("Scanned for duplicates", f"{duplicate_count} duplicate copies found")
        st.success("Scan complete.")

        col1, col2, col3 = st.columns(3)
        col1.metric("Files Scanned", len(uploaded_files))
        col2.metric("Duplicate Copies", duplicate_count)
        col3.metric("Recoverable Space", format_size(recoverable_space))

        if not duplicate_groups:
            st.success("No duplicates found.")
            return

        section("Duplicate Groups")
        for index, files in enumerate(duplicate_groups.values(), start=1):
            with st.expander(f"Duplicate Group {index} • {len(files)} files"):
                st.caption("Keep one copy and review the rest before deleting anything.")
                for file_info in files:
                    st.write(f"{file_info['name']} — {format_size(file_info['size'])}")

        report_csv = build_duplicate_report_csv(duplicate_groups)
        st.download_button(
            "Download Duplicate Report",
            report_csv,
            file_name="duplicate_report.csv",
            mime="text/csv",
        )
