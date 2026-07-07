import streamlit as st


def section(title, subtitle=None):
    subtitle_html = f"<div style='color:#6B7280;font-size:15px;margin-top:4px;'>{subtitle}</div>" if subtitle else ""

    st.markdown(
        f"""
        <div style="margin-top:36px;margin-bottom:18px;">
            <div style="
                color:#111827;
                font-size:22px;
                font-weight:800;
                letter-spacing:-.5px;
            ">
                {title}
            </div>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )