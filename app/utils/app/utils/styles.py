import streamlit as st


def load_styles():
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

    h1, h2, h3 {
        color: #111827;
        letter-spacing: -0.04em;
    }

    p, div {
        color: #374151;
    }

    .ff-hero {
        padding: 2rem 0 1rem 0;
    }

    .ff-title {
        font-size: 3.25rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0.25rem;
        letter-spacing: -0.06em;
    }

    .ff-subtitle {
        font-size: 1.15rem;
        color: #6B7280;
        margin-bottom: 2rem;
    }

    .ff-card {
        background: white;
        border-radius: 22px;
        padding: 1.5rem;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
        transition: all 0.2s ease;
        min-height: 155px;
    }

    .ff-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);
    }

    .ff-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .ff-card-text {
        font-size: 0.95rem;
        color: #6B7280;
        line-height: 1.5;
    }

    .ff-badge {
        display: inline-block;
        background: #EFF6FF;
        color: #2563EB;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    .ff-section {
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        font-size: 1.35rem;
        font-weight: 800;
        color: #111827;
    }

    .ff-muted {
        color: #6B7280;
    }

    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 1.25rem;
        border-radius: 18px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.035);
    }
    </style>
    """, unsafe_allow_html=True)