import streamlit as st


def stat_card(label, value, detail=None):
    detail_html = f"<div style='color:#9CA3AF;font-size:13px;margin-top:6px;'>{detail}</div>" if detail else ""

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:18px;
            padding:22px;
            box-shadow:0 8px 24px rgba(0,0,0,.04);
        ">
            <div style="
                color:#6B7280;
                font-size:14px;
                font-weight:600;
                margin-bottom:8px;
            ">
                {label}
            </div>

            <div style="
                color:#111827;
                font-size:30px;
                font-weight:800;
                letter-spacing:-1px;
            ">
                {value}
            </div>

            {detail_html}
        </div>
        """,
        unsafe_allow_html=True,
    )