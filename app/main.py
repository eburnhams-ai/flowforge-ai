import streamlit as st
from pages.dashboard import show_dashboard
from pages.organizer import show_organizer
from pages.duplicates import show_duplicates
from pages.pdf_tools import show_pdf_tools
from pages.image_tools import show_image_tools
from pages.excel_tools import show_excel_tools
from pages.settings import show_settings

st.set_page_config(
    page_title="FlowForge AI",
    page_icon="⚙️",
    layout="wide"
)

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
    ]
)

if page == "🏠 Dashboard":
    show_dashboard()
elif page == "📂 File Organizer":
    show_organizer()
elif page == "🔍 Duplicate Finder":
    show_duplicates()
elif page == "📄 PDF Tools":
    show_pdf_tools()
elif page == "🖼 Image Tools":
    show_image_tools()
elif page == "📊 Excel Tools":
    show_excel_tools()
elif page == "⚙️ Settings":
    show_settings()