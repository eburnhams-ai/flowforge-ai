import streamlit as st

from components.hero import hero
from components.section import section
from core.state import add_activity
from modules.file_organizer import organize_uploaded_files


def _parse_custom_rules(custom_input: str):
    rules = {}
    for line in custom_input.splitlines():
        line = line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError("Rules must use: FolderName: .ext,.ext")
        folder, exts = line.split(":", 1)
        rules[folder.strip()] = [ext.strip().lower() for ext in exts.split(",") if ext.strip()]
    return rules


def render_file_organizer() -> None:
    hero("File Organizer", "Sort uploaded files into clean folders and export a ZIP package.")

    section("Upload")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True, key="file_organizer_uploads")

    section("Rules")
    custom_input = st.text_area(
        "Custom rules",
        placeholder="Images: .png,.jpg,.jpeg\nDocs: .pdf,.docx\nSpreadsheets: .xlsx,.csv",
    )

    custom_rules = None
    if custom_input.strip():
        try:
            custom_rules = _parse_custom_rules(custom_input)
            st.success("Custom rules loaded.")
        except ValueError as exc:
            st.error(str(exc))
            custom_rules = None

    if st.button("Organize Files", type="primary"):
        if not uploaded_files:
            st.error("Please upload files first.")
            return

        with st.spinner("Organizing files…"):
            zip_path, files, summary, duplicates = organize_uploaded_files(uploaded_files, custom_rules)

        add_activity("Organized files", f"{len(files)} files processed")
        st.success("Files organized successfully.")

        col1, col2 = st.columns(2)
        col1.metric("Files Processed", len(files))
        col2.metric("Duplicate Names", len(duplicates))

        section("Breakdown")
        st.json(summary)

        if duplicates:
            st.warning("Duplicate filenames detected.")
            st.write(duplicates)

        with open(zip_path, "rb") as file:
            st.download_button(
                "Download Organized Files",
                file,
                file_name="flowforge_output.zip",
                mime="application/zip",
            )
