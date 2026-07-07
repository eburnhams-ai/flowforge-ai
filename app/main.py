import streamlit as st

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

.stApp {
    background: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E5E7EB;
}

.ff-title {
    font-size: 3.5rem;
    font-weight: 800;
    letter-spacing: -0.06em;
    color: #111827;
    margin-bottom: 0.25rem;
}

.ff-subtitle {
    font-size: 1.15rem;
    color: #6B7280;
    margin-bottom: 2.5rem;
}

.ff-section {
    font-size: 1.35rem;
    font-weight: 800;
    color: #111827;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.ff-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 22px;
    padding: 1.5rem;
    min-height: 155px;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.045);
}

.ff-card-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: #111827;
    margin-bottom: 0.5rem;
}

.ff-card-text {
    color: #6B7280;
    font-size: 0.95rem;
    line-height: 1.5;
}

.ff-badge {
    display: inline-block;
    background: #EFF6FF;
    color: #2563EB;
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 800;
    margin-bottom: 0.75rem;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.markdown("## ⚙️ FlowForge")
st.sidebar.caption("Automate. Organize. Optimize.")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "File Organizer",
        "Duplicate Finder",
        "PDF Tools",
        "Image Tools",
        "Excel Tools",
        "Settings"
    ]
)

if page == "Dashboard":
    st.markdown('<div class="ff-title">FlowForge</div>', unsafe_allow_html=True)
    st.markdown('<div class="ff-subtitle">Premium automation tools for everyday business workflows.</div>', unsafe_allow_html=True)

    st.markdown('<div class="ff-section">Tools</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Ready</div>
            <div class="ff-card-title">File Organizer</div>
            <div class="ff-card-text">Sort files into clean folders and export a polished ZIP package.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Next</div>
            <div class="ff-card-title">PDF Toolkit</div>
            <div class="ff-card-text">Merge, split, compress, and prepare PDFs for business workflows.</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Planned</div>
            <div class="ff-card-title">Spreadsheet Tools</div>
            <div class="ff-card-text">Clean spreadsheets, remove duplicates, and standardize data.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ff-section">Overview</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Tools", "6")
    m2.metric("Files Processed", "0")
    m3.metric("Space Saved", "0 MB")
    m4.metric("Time Saved", "0 hrs")

elif page == "File Organizer":
    st.title("File Organizer")
    st.info("We’ll reconnect the file organizer next.")

elif page == "Duplicate Finder":
    st.title("Duplicate Finder")
    st.info("Coming soon.")

elif page == "PDF Tools":
    st.title("PDF Tools")
    st.info("Coming soon.")

elif page == "Image Tools":
    st.title("Image Tools")
    st.info("Coming soon.")

elif page == "Excel Tools":
    st.title("Excel Tools")
    st.info("Coming soon.")

elif page == "Settings":
    st.title("Settings")
    st.info("Coming soon.")