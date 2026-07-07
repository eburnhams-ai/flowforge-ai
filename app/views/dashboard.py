import streamlit as st


def render_dashboard():
    st.markdown(
        """
        <style>
        .ff-page {
            padding-bottom: 40px;
        }

        .ff-hero {
            position: relative;
            border-radius: 34px;
            padding: 2.8rem 2rem;
            margin-bottom: 1.4rem;
            overflow: hidden;
            background:
                radial-gradient(circle at 10% 15%, rgba(37,99,235,0.18), transparent 30%),
                radial-gradient(circle at 90% 20%, rgba(249,115,22,0.18), transparent 32%),
                linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,255,255,0.86));
            border: 1px solid #E5E7EB;
            box-shadow: 0 32px 90px rgba(15,23,42,0.12);
        }

        .ff-hero h1 {
            text-align: center;
            font-size: 3rem;
            line-height: 1.02;
            letter-spacing: -0.07em;
            margin: 0;
            color: #0F172A;
            font-weight: 950;
        }

        .ff-gradient {
            background: linear-gradient(90deg, #2563EB, #7C3AED, #F97316);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .ff-hero-sub {
            text-align: center;
            margin-top: 0.8rem;
            color: #64748B;
            font-weight: 750;
        }

        .ff-upload {
            max-width: 720px;
            margin: 1.5rem auto 0 auto;
            border: 2px dashed rgba(99,102,241,0.55);
            border-radius: 30px;
            padding: 2.2rem;
            text-align: center;
            background: rgba(255,255,255,0.72);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.95), 0 20px 50px rgba(99,102,241,0.10);
        }

        .ff-upload-icon {
            width: 52px;
            height: 52px;
            border-radius: 18px;
            margin: 0 auto 0.9rem auto;
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 950;
            box-shadow: 0 18px 40px rgba(99,102,241,0.38);
        }

        .ff-safe {
            text-align: center;
            margin-top: 0.9rem;
            color: #64748B;
            font-size: 0.85rem;
        }

        .ff-section-title {
            font-size: 1.35rem;
            font-weight: 900;
            letter-spacing: -0.045em;
            color: #0F172A;
            margin-top: 1.8rem;
        }

        .ff-section-sub {
            color: #64748B;
            font-size: 0.92rem;
            margin-bottom: 1rem;
        }

        .ff-grid-4 {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
        }

        .ff-grid-6 {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 16px;
        }

        .ff-card {
            background: rgba(255,255,255,0.9);
            border: 1px solid #E5E7EB;
            border-radius: 24px;
            padding: 18px;
            box-shadow: 0 18px 44px rgba(15,23,42,0.08);
            min-height: 150px;
        }

        .ff-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 26px 60px rgba(15,23,42,0.12);
        }

        .ff-icon {
            width: 42px;
            height: 42px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 14px;
            font-weight: 900;
        }

        .blue { background:#DBEAFE; color:#2563EB; }
        .green { background:#DCFCE7; color:#16A34A; }
        .red { background:#FEE2E2; color:#DC2626; }
        .orange { background:#FFEDD5; color:#EA580C; }
        .purple { background:#EDE9FE; color:#7C3AED; }

        .ff-card-title {
            font-weight: 900;
            color: #0F172A;
            margin-bottom: 4px;
        }

        .ff-card-text {
            color: #64748B;
            font-size: 0.86rem;
            line-height: 1.45;
        }

        .ff-two-col {
            display: grid;
            grid-template-columns: 1.25fr 1fr;
            gap: 18px;
            margin-top: 1rem;
        }

        .ff-job {
            display:flex;
            align-items:center;
            gap:12px;
            padding:13px;
            border-radius:18px;
            background:#F8FAFC;
            margin-bottom:10px;
        }

        .ff-pill {
            display:inline-block;
            margin-top:12px;
            padding:4px 10px;
            border-radius:999px;
            font-size:12px;
            font-weight:800;
            background:#ECFDF5;
            color:#10B981;
        }
        </style>

        <div class="ff-page">
            <div class="ff-hero">
                <h1>The operating system for<br><span class="ff-gradient">business automation.</span></h1>
                <div class="ff-hero-sub">Drop your files anywhere to get started.</div>

                <div class="ff-upload">
                    <div class="ff-upload-icon">↑</div>
                    <div class="ff-card-title">Drop files here</div>
                    <div class="ff-card-text">or click to browse</div>
                </div>

                <div class="ff-safe">Your files stay private and local.</div>
            </div>

            <div class="ff-two-col">
                <div>
                    <div class="ff-section-title">Quick Actions</div>
                    <div class="ff-section-sub">Start common workflows in one click.</div>

                    <div class="ff-grid-4">
                        <div class="ff-card"><div class="ff-icon blue">F</div><div class="ff-card-title">Organize Files</div><div class="ff-card-text">Sort and structure messy folders.</div></div>
                        <div class="ff-card"><div class="ff-icon green">D</div><div class="ff-card-title">Find Duplicates</div><div class="ff-card-text">Remove duplicate files safely.</div></div>
                        <div class="ff-card"><div class="ff-icon red">P</div><div class="ff-card-title">Merge PDFs</div><div class="ff-card-text">Combine and reorder PDFs.</div></div>
                        <div class="ff-card"><div class="ff-icon orange">I</div><div class="ff-card-title">Convert Images</div><div class="ff-card-text">Resize, compress, and convert.</div></div>
                    </div>
                </div>

                <div>
                    <div class="ff-section-title">Recent Jobs</div>
                    <div class="ff-section-sub">Your latest automation history.</div>

                    <div class="ff-card">
                        <div class="ff-job"><div class="ff-icon blue">F</div><div><div class="ff-card-title">Organized 482 files</div><div class="ff-card-text">Documents / Project Apollo</div></div></div>
                        <div class="ff-job"><div class="ff-icon green">D</div><div><div class="ff-card-title">Removed 112 duplicates</div><div class="ff-card-text">All files</div></div></div>
                        <div class="ff-job"><div class="ff-icon red">P</div><div><div class="ff-card-title">Merged 8 PDFs</div><div class="ff-card-text">Invoices Q1 2024</div></div></div>
                    </div>
                </div>
            </div>

            <div class="ff-section-title">Automation Library</div>
            <div class="ff-section-sub">Powerful workflows to handle repetitive work.</div>

            <div class="ff-grid-6">
                <div class="ff-card"><div class="ff-icon blue">F</div><div class="ff-card-title">File Organizer</div><div class="ff-card-text">Transform chaotic folders into structured systems.</div><span class="ff-pill">Ready</span></div>
                <div class="ff-card"><div class="ff-icon green">D</div><div class="ff-card-title">Duplicate Finder</div><div class="ff-card-text">Find duplicates by content, not filenames.</div><span class="ff-pill">Ready</span></div>
                <div class="ff-card"><div class="ff-icon red">P</div><div class="ff-card-title">PDF Toolkit</div><div class="ff-card-text">Merge, split, compress, and prepare PDFs.</div><span class="ff-pill">Ready</span></div>
                <div class="ff-card"><div class="ff-icon purple">I</div><div class="ff-card-title">Image Toolkit</div><div class="ff-card-text">Convert, resize, and optimize images.</div><span class="ff-pill">Planned</span></div>
                <div class="ff-card"><div class="ff-icon green">X</div><div class="ff-card-title">Excel Toolkit</div><div class="ff-card-text">Clean and analyze spreadsheets.</div><span class="ff-pill">Planned</span></div>
                <div class="ff-card"><div class="ff-icon orange">A</div><div class="ff-card-title">AI Assistant</div><div class="ff-card-text">Classify, summarize, and extract insights.</div><span class="ff-pill">Planned</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )