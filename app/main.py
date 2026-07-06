import streamlit as st

from views.dashboard import show_dashboard
from views.organizer import show_organizer
from views.duplicates import show_duplicates
from views.pdf_tools import show_pdf_tools
from views.image_tools import show_image_tools
from views.excel_tools import show_excel_tools
from views.settings import show_settings

st.set_page_config(
    page_title="FlowForge",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0;
}

.subtitle {
    font-size: 1.25rem;
    color: #6b7280;
    margin-bottom: 2rem;
}

.sidebar-brand {
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 0.25rem;
}

.sidebar-caption {
    color: #6b7280;
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-brand">⚙️ FlowForge</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-caption">Business Automation Suite</div>', unsafe_allow_html=True)

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