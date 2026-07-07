import streamlit as st


def hero(title: str, subtitle: str):
    st.markdown(
        f"""
        <div style="margin-bottom:40px;">
            <div style="
                font-size:56px;
                font-weight:800;
                letter-spacing:-2px;
                color:#111827;
            ">
                {title}
            </div>

            <div style="
                font-size:20px;
                color:#6B7280;
                margin-top:8px;
            ">
                {subtitle}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
