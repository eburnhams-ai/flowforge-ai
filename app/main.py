import streamlit as st

from components.sidebar import sidebar
from components.topbar import topbar
from components.hero import hero
from components.tool_tile import tool_tile
from components.stat_card import stat_card
from components.section import section

st.set_page_config(
    page_title="FlowForge",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none; }
.stApp { background: #F8FAFC; }
.block-container { padding-top: 2rem; max-width: 1180px; }
section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E5E7EB;
}
</style>
""", unsafe_allow_html=True)

page = sidebar()
topbar()

if page == "Dashboard":
    hero("FlowForge", "Premium automation tools for everyday business workflows.")

    section("Core Tools", "Start with the tools that save the most time.")

    c1, c2, c3 = st.columns(3)
    with c1:
        tool_tile("📂", "File Organizer", "Sort files into clean folders and export a ZIP package.", "Ready")
    with c2:
        tool_tile("📄", "PDF Toolkit", "Merge, split, compress, and prepare PDFs.", "Next")
    with c3:
        tool_tile("📊", "Excel Toolkit", "Clean spreadsheets and standardize data.", "Planned")

    section("System Overview")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        stat_card("Tools", "8", "Core modules")
    with m2:
        stat_card("Files Processed", "0", "Across all jobs")
    with m3:
        stat_card("Space Saved", "0 MB", "Duplicates + compression")
    with m4:
        stat_card("Time Saved", "0 hrs", "Estimated")
else:
    hero(page, "This tool will plug into the FlowForge platform.")
    st.info("Coming soon.")