import streamlit as st


def show_dashboard():
    st.markdown("""
    <div class="ff-hero">
        <div class="ff-title">FlowForge</div>
        <div class="ff-subtitle">Automate. Organize. Optimize.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ff-section">What would you like to automate?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Ready</div>
            <div class="ff-card-title">File Organizer</div>
            <div class="ff-card-text">Sort uploaded files into clean folders and export a polished ZIP package.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Next</div>
            <div class="ff-card-title">PDF Toolkit</div>
            <div class="ff-card-text">Merge, split, compress, and prepare PDFs for business workflows.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="ff-card">
            <div class="ff-badge">Planned</div>
            <div class="ff-card-title">Spreadsheet Tools</div>
            <div class="ff-card-text">Clean spreadsheets, remove duplicates, merge files, and standardize data.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ff-section">System Overview</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Tools", "6")
    m2.metric("Files Processed", "0")
    m3.metric("Space Saved", "0 MB")
    m4.metric("Time Saved", "0 hrs")