import streamlit as st


NAV_GROUPS = {
    "HOME": [
        ("Dashboard", "⌂"),
    ],
    "TOOLS": [
        ("File Organizer", "▣"),
        ("Duplicate Finder", "◇"),
        ("PDF Toolkit", "□"),
        ("Image Toolkit", "◧"),
        ("Excel Toolkit", "▦"),
        ("AI Assistant", "✦"),
    ],
    "SYSTEM": [
        ("Settings", "⚙"),
    ],
}


def _nav_item(label, icon):
    active = st.session_state.page == label

    if active:
        st.sidebar.markdown(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                padding:11px 13px;
                border-radius:16px;
                background:linear-gradient(135deg, rgba(99,102,241,0.16), rgba(124,58,237,0.10));
                color:#4F46E5;
                font-weight:800;
                margin-bottom:7px;
                box-shadow:0 10px 28px rgba(99,102,241,0.14);
            ">
                <span style="
                    width:28px;
                    height:28px;
                    border-radius:10px;
                    background:white;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:14px;
                    box-shadow:0 6px 18px rgba(15,23,42,0.08);
                ">{icon}</span>
                <span>{label}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        if st.sidebar.button(f"{icon}  {label}", use_container_width=True):
            st.session_state.page = label
            st.rerun()


def render_sidebar():
    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    st.sidebar.markdown(
        """
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
            <div style="
                width:40px;
                height:40px;
                border-radius:14px;
                background:linear-gradient(135deg,#2563EB,#7C3AED);
                color:white;
                display:flex;
                align-items:center;
                justify-content:center;
                font-weight:900;
                font-size:17px;
                box-shadow:0 16px 34px rgba(99,102,241,0.35);
            ">F</div>
            <div>
                <div style="font-weight:900;font-size:19px;color:#0F172A;letter-spacing:-0.04em;">FlowForge</div>
                <div style="font-size:12px;color:#64748B;">Automate. Organize. Optimize.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.divider()

    for group, items in NAV_GROUPS.items():
        st.sidebar.caption(group)

        for label, icon in items:
            _nav_item(label, icon)

        st.sidebar.write("")

    st.sidebar.markdown(
        """
        <div style="
            margin-top:18px;
            padding:16px;
            border-radius:20px;
            background:linear-gradient(135deg, rgba(238,242,255,0.95), rgba(255,255,255,0.95));
            border:1px solid #E5E7EB;
            box-shadow:0 18px 40px rgba(15,23,42,0.07);
        ">
            <div style="font-weight:850;color:#0F172A;margin-bottom:6px;">Pro Workspace</div>
            <div style="font-size:12px;color:#64748B;line-height:1.45;margin-bottom:12px;">
                Core UI active. Tools will connect after the shell is complete.
            </div>
            <div style="
                height:6px;
                border-radius:999px;
                background:#E5E7EB;
                overflow:hidden;
            ">
                <div style="
                    width:42%;
                    height:100%;
                    border-radius:999px;
                    background:linear-gradient(90deg,#2563EB,#7C3AED);
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.write("")
    st.sidebar.caption("v0.5 • Core UI")
    st.sidebar.caption("Local workspace")

    return st.session_state.page