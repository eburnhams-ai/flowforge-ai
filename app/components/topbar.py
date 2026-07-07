import streamlit as st


def render_topbar():
    st.markdown(
        """
        <style>
        .ff-topbar {
            display: grid;
            grid-template-columns: 1fr 2.4fr 1fr;
            gap: 16px;
            align-items: center;
            margin-bottom: 22px;
        }

        .ff-topbar-card {
            border: 1px solid #E5E7EB;
            background: rgba(255,255,255,0.88);
            border-radius: 22px;
            padding: 14px 18px;
            box-shadow: 0 18px 42px rgba(15,23,42,0.07);
            color: #64748B;
            font-size: 13px;
            font-weight: 700;
        }

        .ff-search-card {
            border: 1px solid #E5E7EB;
            background: rgba(255,255,255,0.92);
            border-radius: 22px;
            padding: 13px 18px;
            box-shadow: 0 18px 42px rgba(15,23,42,0.07);
            color: #64748B;
            font-size: 14px;
            font-weight: 650;
        }

        .ff-topbar-right {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }

        .ff-pill {
            border: 1px solid #E5E7EB;
            background: rgba(255,255,255,0.92);
            border-radius: 999px;
            padding: 10px 13px;
            box-shadow: 0 14px 32px rgba(15,23,42,0.06);
            color: #0F172A;
            font-size: 13px;
            font-weight: 800;
        }
        </style>

        <div class="ff-topbar">
            <div class="ff-topbar-card">FlowForge Core</div>
            <div class="ff-search-card">⌕ Search workflows, tools, or recent jobs...</div>
            <div class="ff-topbar-right">
                <div class="ff-pill">◐</div>
                <div class="ff-pill">EB</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )