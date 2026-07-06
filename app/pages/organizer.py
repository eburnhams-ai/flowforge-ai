import streamlit as st
from modules.file_organizer import organize_uploaded_files


def show_organizer():
    st.title("📂 File Organizer")
    st.write("Upload files and FlowForge will organize them into a clean ZIP package.")

    uploaded_files = st.file_uploader(
        "Upload files",
        accept_multiple_files=True,
        key="organizer_uploads"
    )

    custom_input = st.text_area(
        "Custom rules",
        placeholder="Images: .png,.jpg\nDocs: .pdf,.docx\nSpreadsheets: .xlsx,.csv"
    )

    custom_rules = {}

    if custom_input:
        try:
            for line in custom_input.split("\n"):
                if ":" in line:
                    folder, exts = line.split(":", 1)
                    custom_rules[folder.strip()] = [
                        ext.strip().lower()
                        for ext in exts.split(",")
                        if ext.strip()
                    ]
        except Exception:
            st.error("Invalid rule format. Use: FolderName: .ext,.ext")

    if st.button("🚀 Organize Files"):
        if not uploaded_files:
            st.error("Please upload files first.")
            return

        with st.spinner("Organizing your files..."):
            zip_path, files, summary, duplicates = organize_uploaded_files(
                uploaded_files,
                custom_rules if custom_rules else None
            )

        st.success("Files organized successfully.")

        col1, col2 = st.columns(2)
        col1.metric("Files Processed", len(files))
        col2.metric("Duplicate Names", len(duplicates))

        st.markdown("### Breakdown")
        st.json(summary)

        if duplicates:
            st.warning("Duplicate filenames detected:")
            st.write(duplicates)

        with open(zip_path, "rb") as f:
            st.download_button(
                "⬇️ Download Organized Files",
                f,
                file_name="flowforge_organized_files.zip",
                mime="application/zip"
            )