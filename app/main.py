import streamlit as st
from modules.file_organizer import organize_uploaded_files
from modules.duplicate_finder import find_duplicates, format_size
st.set_page_config(
    page_title="FlowForge AI",
    page_icon="⚙️",
    layout="wide"
)

# -------------------------
# CUSTOM STYLE
# -------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.big-card {
    padding: 1.25rem;
    border-radius: 16px;
    background: #f7f7f9;
    border: 1px solid #e5e5e5;
    margin-bottom: 1rem;
}

.tool-card {
    padding: 1rem;
    border-radius: 14px;
    background: #ffffff;
    border: 1px solid #e6e6e6;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("⚙️ FlowForge AI")
st.sidebar.caption("Business Automation Suite")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📂 File Organizer",
        "🔍 Duplicate Finder",
        "📄 PDF Tools",
        "🖼 Image Tools",
        "📊 Excel Tools",
        "⚙️ Settings",
        "ℹ️ About"
    ]
)

# -------------------------
# DASHBOARD
# -------------------------
if page == "🏠 Dashboard":
    st.title("FlowForge AI")
    st.subheader("Automate repetitive business tasks in seconds.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tools Available", "2", "+3 planned")
    col2.metric("Files Processed", "0")
    col3.metric("Duplicates Found", "0")
    col4.metric("Time Saved", "0 hrs")

    st.markdown("---")

    st.markdown("### Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="tool-card">
        <h4>📂 File Organizer</h4>
        <p>Upload files and automatically sort them into clean folders.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="tool-card">
        <h4>🔍 Duplicate Finder</h4>
        <p>Find duplicate files by content, not just filename.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="tool-card">
        <h4>📄 PDF Tools</h4>
        <p>Coming soon: merge, split, compress, and organize PDFs.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Use the sidebar to open a tool.")

# -------------------------
# FILE ORGANIZER
# -------------------------
elif page == "📂 File Organizer":
    st.title("📂 File Organizer")
    st.write("Upload files and get a structured, business-ready ZIP package.")

    uploaded_files = st.file_uploader(
        "Upload files",
        accept_multiple_files=True
    )

    custom_input = st.text_area(
        "Custom rules (FolderName: .ext,.ext)",
        placeholder="Images: .png,.jpg\nDocs: .pdf,.docx"
    )

    custom_rules = {}

    if custom_input:
        try:
            for line in custom_input.split("\n"):
                if ":" in line:
                    folder, exts = line.split(":")
                    custom_rules[folder.strip()] = [
                        e.strip().lower() for e in exts.split(",")
                    ]
        except Exception:
            st.error("Invalid rule format. Use: FolderName: .ext,.ext")

    if st.button("🚀 Run File Organizer"):
        if uploaded_files:
            with st.spinner("FlowForge AI is organizing your files..."):
                zip_path, files, summary, duplicates = organize_uploaded_files(
                    uploaded_files,
                    custom_rules if custom_rules else None
                )

            st.success("Organization complete.")

            col1, col2 = st.columns(2)
            col1.metric("Files Processed", len(files))
            col2.metric("Duplicate Names Found", len(duplicates))

            st.markdown("### Breakdown")
            st.json(summary)

            if duplicates:
                st.warning("Duplicate filenames detected:")
                st.write(duplicates)

            with open(zip_path, "rb") as f:
                st.download_button(
                    "⬇️ Download Organized Files",
                    f,
                    file_name="flowforge_output.zip"
                )
        else:
            st.error("Please upload files first.")

# -------------------------
# DUPLICATE FINDER PLACEHOLDER
# -------------------------
elif page == "🔍 Duplicate Finder":
    st.title("🔍 Duplicate Finder Pro")
    st.write("Upload files and find true duplicates by file content, not just filename.")

    uploaded_files = st.file_uploader(
        "Upload files to scan",
        accept_multiple_files=True,
        key="duplicate_scanner"
    )

    if uploaded_files:
        st.info(f"{len(uploaded_files)} files ready to scan.")

    if st.button("🔍 Scan for Duplicates"):
        if uploaded_files:
            with st.spinner("Scanning files for duplicates..."):
duplicate_groups, duplicate_count, recoverable_space = find_duplicates(uploaded_files)

            st.success("Scan complete.")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Files Scanned", summary["files_scanned"])
            col2.metric("Unique Files", summary["unique_files"])
            col3.metric("Duplicate Copies", summary["duplicate_copies"])
            col4.metric("Recoverable Space", f'{summary["recoverable_mb"]} MB')

            st.markdown("### Duplicate Results")

            if duplicates:
                st.warning("Duplicate files found.")
                st.dataframe(duplicates, use_container_width=True)

                with open(report_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Duplicate Report",
                        f,
                        file_name="duplicate_report.csv"
                    )
            else:
                st.success("No duplicate files found.")
        else:
            st.error("Please upload files first.")cd business-automation-hub













# -------------------------
# FUTURE TOOLS
# -------------------------
elif page == "📄 PDF Tools":
    st.title("📄 PDF Tools")
    st.info("Coming soon: merge, split, compress, rotate, and extract PDFs.")

elif page == "🖼 Image Tools":
    st.title("🖼 Image Tools")
    st.info("Coming soon: resize, compress, convert, and watermark images.")

elif page == "📊 Excel Tools":
    st.title("📊 Excel Tools")
    st.info("Coming soon: clean, merge, deduplicate, and format spreadsheets.")

elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.write("Settings will go here later.")

elif page == "ℹ️ About":
    st.title("About FlowForge AI")
    st.markdown("""
FlowForge AI is a business automation system designed to:

- Eliminate repetitive file management tasks
- Save hours of manual work
- Provide structured, automated workflows
- Help businesses operate more efficiently

Built with Python + Streamlit.
""")