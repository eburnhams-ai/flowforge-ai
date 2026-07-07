import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="FlowForge",
    page_icon="F",
    layout="wide",
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stSidebarNav"] { display: none; }
    .block-container { padding: 0 !important; max-width: none !important; }
    .stApp { background: #F8FAFC; }
    header { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", sans-serif;
            background:
                radial-gradient(circle at 7% 4%, rgba(37,99,235,.16), transparent 28%),
                radial-gradient(circle at 93% 6%, rgba(249,115,22,.16), transparent 30%),
                #F8FAFC;
            color: #0F172A;
        }

        .app {
            display: grid;
            grid-template-columns: 250px 1fr;
            min-height: 100vh;
        }

        .sidebar {
            background: rgba(255,255,255,.96);
            border-right: 1px solid #E5E7EB;
            padding: 24px 18px;
            box-shadow: 28px 0 70px rgba(15,23,42,.08);
            display: flex;
            flex-direction: column;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 13px;
            margin-bottom: 34px;
        }

        .logo {
            width: 44px;
            height: 44px;
            border-radius: 16px;
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            color: white;
            display: grid;
            place-items: center;
            font-weight: 950;
            font-size: 24px;
            box-shadow: 0 20px 44px rgba(99,102,241,.38);
        }

        .brand-title {
            font-size: 21px;
            font-weight: 950;
            letter-spacing: -.05em;
        }

        .brand-sub {
            font-size: 12px;
            color: #64748B;
            font-weight: 650;
        }

        .nav-section { margin-bottom: 24px; }

        .nav-label {
            color: #94A3B8;
            font-size: 11px;
            font-weight: 900;
            letter-spacing: .11em;
            text-transform: uppercase;
            margin: 0 0 10px 8px;
        }

        .nav-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 11px 12px;
            border-radius: 16px;
            color: #475569;
            font-weight: 780;
            margin-bottom: 7px;
        }

        .nav-item.active {
            background: linear-gradient(135deg, rgba(37,99,235,.13), rgba(124,58,237,.10));
            color: #2563EB;
            box-shadow: 0 18px 40px rgba(37,99,235,.14);
        }

        .nav-icon {
            width: 28px;
            height: 28px;
            border-radius: 11px;
            display: grid;
            place-items: center;
            font-weight: 950;
            font-size: 13px;
            background: #F1F5F9;
        }

        .active .nav-icon {
            background: white;
            box-shadow: 0 10px 24px rgba(15,23,42,.08);
        }

        .workspace-card {
            margin-top: auto;
            border: 1px solid #E5E7EB;
            border-radius: 24px;
            padding: 18px;
            background:
                radial-gradient(circle at top right, rgba(124,58,237,.12), transparent 40%),
                rgba(255,255,255,.94);
            box-shadow: 0 24px 54px rgba(15,23,42,.10);
        }

        .workspace-title {
            font-weight: 950;
            margin-bottom: 7px;
            letter-spacing: -.03em;
        }

        .workspace-text {
            color: #64748B;
            font-size: 13px;
            line-height: 1.45;
        }

        .progress-track {
            height: 8px;
            background: #E5E7EB;
            border-radius: 999px;
            overflow: hidden;
            margin: 14px 0;
        }

        .progress-fill {
            width: 42%;
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #2563EB, #7C3AED);
        }

        .upgrade {
            background: linear-gradient(135deg, #EEF2FF, #F5F3FF);
            color: #4F46E5;
            border-radius: 15px;
            padding: 12px;
            text-align: center;
            font-weight: 900;
            font-size: 13px;
        }

        .version {
            margin-top: 16px;
            color: #94A3B8;
            font-size: 12px;
            font-weight: 700;
        }

        .main {
            padding: 24px 34px 42px;
        }

        .topbar {
            display: grid;
            grid-template-columns: 230px 1fr 150px;
            gap: 18px;
            align-items: center;
            margin-bottom: 22px;
        }

        .top-left,
        .search,
        .circle {
            background: rgba(255,255,255,.88);
            border: 1px solid #E5E7EB;
            box-shadow: 0 18px 42px rgba(15,23,42,.07);
        }

        .top-left {
            border-radius: 20px;
            padding: 13px 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 900;
        }

        .mini-logo {
            width: 26px;
            height: 26px;
            border-radius: 9px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            color: white;
            font-weight: 950;
        }

        .search {
            border-radius: 20px;
            padding: 15px 18px;
            color: #94A3B8;
            font-weight: 700;
        }

        .top-actions {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }

        .circle {
            width: 44px;
            height: 44px;
            border-radius: 16px;
            display: grid;
            place-items: center;
            font-weight: 950;
        }

        .avatar {
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            color: white;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border-radius: 36px;
            padding: 56px 40px 32px;
            margin-bottom: 28px;
            background:
                radial-gradient(circle at 13% 22%, rgba(37,99,235,.24), transparent 28%),
                radial-gradient(circle at 88% 18%, rgba(249,115,22,.24), transparent 30%),
                linear-gradient(135deg, rgba(255,255,255,.99), rgba(255,255,255,.84));
            border: 1px solid #E5E7EB;
            box-shadow: 0 36px 100px rgba(15,23,42,.14);
        }

        .floating {
            position: absolute;
            width: 76px;
            height: 76px;
            border-radius: 26px;
            background: rgba(255,255,255,.76);
            backdrop-filter: blur(14px);
            display: grid;
            place-items: center;
            font-weight: 950;
            box-shadow: 0 24px 54px rgba(15,23,42,.14);
            transform: rotate(-4deg);
        }

        .folder { left: 82px; top: 70px; color:#2563EB; font-size:35px; }
        .pdf { left: 62px; bottom: 70px; color:#EF4444; }
        .sheet { right: 112px; top: 68px; color:#16A34A; transform: rotate(5deg); }
        .image { right: 70px; bottom: 72px; color:#F97316; transform: rotate(4deg); }

        .hero h1 {
            text-align: center;
            margin: 0;
            font-size: 52px;
            line-height: 1.02;
            letter-spacing: -.075em;
            font-weight: 950;
        }

        .gradient-text {
            background: linear-gradient(90deg, #2563EB, #7C3AED, #F97316);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-sub {
            text-align: center;
            margin-top: 14px;
            color: #64748B;
            font-weight: 780;
            font-size: 16px;
        }

        .dropzone {
            width: 720px;
            max-width: 72%;
            margin: 24px auto 0;
            border: 2px dashed rgba(99,102,241,.58);
            border-radius: 32px;
            padding: 36px;
            text-align: center;
            background: rgba(255,255,255,.76);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.95), 0 26px 60px rgba(99,102,241,.14);
        }

        .upload-icon {
            width: 58px;
            height: 58px;
            border-radius: 20px;
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            color: white;
            display: grid;
            place-items: center;
            font-size: 28px;
            font-weight: 950;
            margin: 0 auto 14px;
            box-shadow: 0 20px 44px rgba(99,102,241,.40);
        }

        .safe {
            text-align: center;
            color: #64748B;
            font-size: 13px;
            margin-top: 14px;
            font-weight: 700;
        }

        .content-grid {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 24px;
            margin-bottom: 28px;
        }

        .section-title {
            font-size: 24px;
            font-weight: 950;
            letter-spacing: -.05em;
            margin-bottom: 4px;
        }

        .section-sub {
            color: #64748B;
            font-size: 14px;
            margin-bottom: 15px;
            font-weight: 650;
        }

        .quick-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
        }

        .card {
            background: rgba(255,255,255,.92);
            border: 1px solid #E5E7EB;
            border-radius: 26px;
            padding: 18px;
            box-shadow: 0 22px 54px rgba(15,23,42,.09);
            transition: all .22s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 34px 72px rgba(15,23,42,.14);
        }

        .card-icon {
            width: 50px;
            height: 50px;
            border-radius: 19px;
            display: grid;
            place-items: center;
            font-weight: 950;
            font-size: 22px;
            margin-bottom: 14px;
        }

        .blue { background:#DBEAFE; color:#2563EB; }
        .green { background:#DCFCE7; color:#16A34A; }
        .red { background:#FEE2E2; color:#EF4444; }
        .orange { background:#FFEDD5; color:#F97316; }
        .purple { background:#EDE9FE; color:#7C3AED; }

        .card-title {
            font-weight: 950;
            letter-spacing: -.025em;
            margin-bottom: 6px;
        }

        .card-text {
            color: #475569;
            font-size: 14px;
            line-height: 1.45;
            font-weight: 550;
        }

        .arrow {
            text-align: right;
            color: #2563EB;
            font-weight: 950;
            margin-top: 14px;
        }

        .jobs { padding: 16px; }

        .job {
            display: grid;
            grid-template-columns: 52px 1fr 86px 24px;
            align-items: center;
            gap: 12px;
            padding: 12px;
            border-radius: 20px;
            background: #F8FAFC;
            margin-bottom: 10px;
        }

        .check {
            color: #10B981;
            font-weight: 950;
        }

        .library-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 15px;
        }

        .library-grid .card {
            min-height: 230px;
            display: flex;
            flex-direction: column;
        }

        .pill {
            margin-top: auto;
            padding: 8px;
            border-radius: 14px;
            background: #ECFDF5;
            color: #10B981;
            text-align: center;
            font-weight: 950;
            font-size: 13px;
        }

        .pill.planned {
            background: #EEF2FF;
            color: #4F46E5;
        }
    </style>
    </head>

    <body>
        <div class="app">
            <aside class="sidebar">
                <div class="brand">
                    <div class="logo">F</div>
                    <div>
                        <div class="brand-title">FlowForge</div>
                        <div class="brand-sub">Automation workspace</div>
                    </div>
                </div>

                <div class="nav-section">
                    <div class="nav-item active"><span class="nav-icon">⌂</span>Dashboard</div>
                </div>

                <div class="nav-section">
                    <div class="nav-label">Automation</div>
                    <div class="nav-item"><span class="nav-icon">□</span>File Organizer</div>
                    <div class="nav-item"><span class="nav-icon">◇</span>Duplicate Finder</div>
                    <div class="nav-item"><span class="nav-icon">▱</span>PDF Toolkit</div>
                    <div class="nav-item"><span class="nav-icon">▧</span>Image Toolkit</div>
                    <div class="nav-item"><span class="nav-icon">▦</span>Excel Toolkit</div>
                </div>

                <div class="nav-section">
                    <div class="nav-label">AI</div>
                    <div class="nav-item"><span class="nav-icon">✦</span>AI Assistant</div>
                </div>

                <div class="nav-section">
                    <div class="nav-label">Workspace</div>
                    <div class="nav-item"><span class="nav-icon">◷</span>Recent Jobs</div>
                    <div class="nav-item"><span class="nav-icon">⚙</span>Settings</div>
                </div>

                <div class="workspace-card">
                    <div class="workspace-title">Pro Workspace</div>
                    <div class="workspace-text">4.2 GB / 50 GB used</div>
                    <div class="progress-track"><div class="progress-fill"></div></div>
                    <div class="upgrade">Upgrade Plan</div>
                </div>

                <div class="version">v0.5.0 • Local Workspace</div>
            </aside>

            <main class="main">
                <div class="topbar">
                    <div class="top-left"><div class="mini-logo">F</div>FlowForge Core</div>
                    <div class="search">⌕ Search workflows, files, jobs...</div>
                    <div class="top-actions">
                        <div class="circle">◐</div>
                        <div class="circle avatar">EB</div>
                    </div>
                </div>

                <section class="hero">
                    <div class="floating folder">📁</div>
                    <div class="floating pdf">PDF</div>
                    <div class="floating sheet">▦</div>
                    <div class="floating image">▧</div>

                    <h1>The operating system for<br><span class="gradient-text">business automation.</span></h1>
                    <div class="hero-sub">Drop your files anywhere to get started.</div>

                    <div class="dropzone">
                        <div class="upload-icon">↑</div>
                        <div class="card-title">Drop files here</div>
                        <div class="card-text">or click to browse</div>
                    </div>

                    <div class="safe">Your files stay private and local.</div>
                </section>

                <div class="content-grid">
                    <section>
                        <div class="section-title">Quick Actions</div>
                        <div class="section-sub">Start common workflows in one click.</div>

                        <div class="quick-grid">
                            <div class="card"><div class="card-icon blue">📁</div><div class="card-title">Organize Files</div><div class="card-text">Sort and structure messy folders.</div><div class="arrow">→</div></div>
                            <div class="card"><div class="card-icon green">◇</div><div class="card-title">Find Duplicates</div><div class="card-text">Remove duplicate files safely.</div><div class="arrow">→</div></div>
                            <div class="card"><div class="card-icon red">PDF</div><div class="card-title">Merge PDFs</div><div class="card-text">Combine and reorder PDFs.</div><div class="arrow">→</div></div>
                            <div class="card"><div class="card-icon orange">▧</div><div class="card-title">Convert Images</div><div class="card-text">Resize, compress, and convert.</div><div class="arrow">→</div></div>
                        </div>
                    </section>

                    <section>
                        <div class="section-title">Recent Jobs</div>
                        <div class="section-sub">Your latest automation history.</div>

                        <div class="card jobs">
                            <div class="job"><div class="card-icon blue">📁</div><div><div class="card-title">Organized 482 files</div><div class="card-text">Documents / Project Apollo</div></div><div class="card-text">Yesterday</div><div class="check">✓</div></div>
                            <div class="job"><div class="card-icon green">◇</div><div><div class="card-title">Removed 112 duplicates</div><div class="card-text">All files</div></div><div class="card-text">2 days ago</div><div class="check">✓</div></div>
                            <div class="job"><div class="card-icon red">PDF</div><div><div class="card-title">Merged 8 PDFs</div><div class="card-text">Invoices Q1 2024</div></div><div class="card-text">3 days ago</div><div class="check">✓</div></div>
                        </div>
                    </section>
                </div>

                <section>
                    <div class="section-title">Automation Library</div>
                    <div class="section-sub">Powerful workflows to handle repetitive work.</div>

                    <div class="library-grid">
                        <div class="card"><div class="card-icon blue">📁</div><div class="card-title">File Organizer</div><div class="card-text">Transform chaotic folders into structured systems.</div><div class="pill">Ready</div></div>
                        <div class="card"><div class="card-icon green">◇</div><div class="card-title">Duplicate Finder</div><div class="card-text">Find duplicates by content, not filenames.</div><div class="pill">Ready</div></div>
                        <div class="card"><div class="card-icon red">PDF</div><div class="card-title">PDF Toolkit</div><div class="card-text">Merge, split, compress, and prepare PDFs.</div><div class="pill">Ready</div></div>
                        <div class="card"><div class="card-icon purple">▧</div><div class="card-title">Image Toolkit</div><div class="card-text">Convert, resize, and optimize images.</div><div class="pill planned">Planned</div></div>
                        <div class="card"><div class="card-icon green">▦</div><div class="card-title">Excel Toolkit</div><div class="card-text">Clean and analyze spreadsheets.</div><div class="pill planned">Planned</div></div>
                        <div class="card"><div class="card-icon orange">✦</div><div class="card-title">AI Assistant</div><div class="card-text">Classify, summarize, and extract insights.</div><div class="pill planned">Planned</div></div>
                    </div>
                </section>
            </main>
        </div>
    </body>
    </html>
    """,
    height=1200,
    scrolling=True,
)