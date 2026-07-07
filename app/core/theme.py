import streamlit as st


def load_theme():
    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(99,102,241,0.10), transparent 28%),
                radial-gradient(circle at top right, rgba(249,115,22,0.10), transparent 28%),
                #F8FAFC;
        }

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 4rem;
            max-width: 1220px;
        }

        section[data-testid="stSidebar"] {
            background: rgba(255,255,255,0.92);
            border-right: 1px solid #E5E7EB;
            box-shadow: 18px 0 45px rgba(15,23,42,0.06);
        }

        section[data-testid="stSidebar"] button {
            background: transparent !important;
            border: 0 !important;
            box-shadow: none !important;
            text-align: left !important;
            justify-content: flex-start !important;
            color: #374151 !important;
            font-weight: 650 !important;
            border-radius: 14px !important;
            min-height: 38px !important;
        }

        section[data-testid="stSidebar"] button:hover {
            background: #EEF2FF !important;
            color: #4F46E5 !important;
        }

        h1 {
            letter-spacing: -0.065em;
            color: #0F172A;
            font-size: 3rem !important;
            line-height: 1.05 !important;
        }

        h2, h3 {
            letter-spacing: -0.04em;
            color: #0F172A;
        }

        div[data-testid="stButton"] > button {
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            background: #FFFFFF;
            color: #0F172A;
            font-weight: 750;
            min-height: 44px;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
            transition: all 0.18s ease;
        }

        div[data-testid="stButton"] > button:hover {
            transform: translateY(-1px);
            border-color: #6366F1;
            color: #4F46E5;
            box-shadow: 0 18px 40px rgba(79, 70, 229, 0.16);
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 24px;
            border-color: #E5E7EB;
            background: rgba(255,255,255,0.86);
            box-shadow: 0 20px 50px rgba(15, 23, 42, 0.08);
        }

        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 22px;
            padding: 1.2rem;
            box-shadow: 0 16px 34px rgba(15, 23, 42, 0.07);
        }

        input {
            border-radius: 16px !important;
        }

        hr {
            margin-top: 1.7rem;
            margin-bottom: 1.7rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )