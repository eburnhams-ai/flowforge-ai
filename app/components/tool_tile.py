import streamlit as st


def tool_tile(icon, title, description, status="Ready"):
    badge_color = "#10B981" if status == "Ready" else "#3B82F6"

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:20px;
            padding:22px;
            min-height:190px;
            box-shadow:0 10px 30px rgba(0,0,0,.05);
            transition:.2s;
        ">

            <div style="
                display:inline-block;
                padding:4px 10px;
                border-radius:999px;
                background:{badge_color}20;
                color:{badge_color};
                font-size:12px;
                font-weight:700;
                margin-bottom:16px;
            ">
                {status}
            </div>

            <div style="
                font-size:34px;
                margin-bottom:10px;
            ">
                {icon}
            </div>

            <div style="
                font-size:22px;
                font-weight:700;
                color:#111827;
                margin-bottom:8px;
            ">
                {title}
            </div>

            <div style="
                color:#6B7280;
                line-height:1.6;
            ">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )