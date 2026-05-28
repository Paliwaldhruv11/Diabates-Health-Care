"""Global Streamlit look-and-feel (CSS only; does not change app logic)."""
from __future__ import annotations

import streamlit as st


def inject_global_styles() -> None:
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --dh-teal: #0d9488;
                --dh-teal-dark: #115e59;
                --dh-teal-deep: #134e4a;
                --dh-mint: #ccfbf1;
                --dh-accent: #7c3aed;
                --dh-surface: #ffffff;
                --dh-text: #134e4a;
                --dh-muted: #5b7c78;
            }
            html, body, [class*="css"]  {
                font-family: "DM Sans", system-ui, sans-serif !important;
            }
            .stApp {
                background: radial-gradient(1200px 600px at 10% -10%, #ccfbf1 0%, transparent 55%),
                            radial-gradient(900px 500px at 100% 0%, #e9d5ff 0%, transparent 50%),
                            linear-gradient(180deg, #f0fdf9 0%, #ecfeff 45%, #f8fafc 100%) !important;
            }
            [data-testid="stHeader"] {
                background: transparent;
            }
            [data-testid="stToolbar"] {
                background: rgba(255,255,255,0.6);
                border-radius: 0 0 0 12px;
            }
            [data-testid="stSidebar"] {
                background: linear-gradient(175deg, #134e4a 0%, #115e59 55%, #0f766e 100%) !important;
                border-right: 1px solid rgba(255,255,255,0.12);
            }
            [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
            [data-testid="stSidebar"] label,
            [data-testid="stSidebar"] span {
                color: #ecfdf5 !important;
            }
            [data-testid="stSidebar"] .stRadio label {
                font-weight: 500;
            }
            [data-testid="stSidebar"] h1 {
                font-family: "Outfit", "DM Sans", sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.02em;
                color: #f0fdfa !important;
                border-bottom: 1px solid rgba(255,255,255,0.15);
                padding-bottom: 0.5rem;
            }
            [data-testid="stSidebar"] [data-baseweb="notification"] {
                background: rgba(15, 118, 110, 0.55) !important;
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 12px;
                color: #ecfdf5 !important;
            }
            .block-container {
                padding-top: 1.75rem;
                padding-bottom: 3rem;
                max-width: 1180px;
            }
            h1, h2, h3 {
                font-family: "Outfit", "DM Sans", sans-serif !important;
                color: var(--dh-teal-deep) !important;
                letter-spacing: -0.02em;
            }
            h1 { font-weight: 700 !important; }
            .stTabs [data-baseweb="tab-list"] {
                gap: 8px;
                background: rgba(255,255,255,0.75);
                padding: 8px;
                border-radius: 14px;
                border: 1px solid rgba(13, 148, 136, 0.15);
            }
            .stTabs [data-baseweb="tab"] {
                border-radius: 10px !important;
                padding: 10px 16px !important;
            }
            .stTabs [aria-selected="true"] {
                background: linear-gradient(135deg, #0d9488, #14b8a6) !important;
                color: white !important;
            }
            .stTabs [data-baseweb="tab-list"] button p {
                font-size: 1.05rem !important;
                font-weight: 600 !important;
            }
            .stButton > button {
                border-radius: 12px !important;
                border: none !important;
                background: linear-gradient(90deg, #0d9488, #2dd4bf) !important;
                color: white !important;
                font-weight: 600 !important;
                box-shadow: 0 4px 14px rgba(13, 148, 136, 0.35);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }
            .stButton > button:hover {
                box-shadow: 0 6px 20px rgba(13, 148, 136, 0.45);
                transform: translateY(-1px);
            }
            .stDownloadButton > button {
                border-radius: 12px !important;
                border: 1px solid rgba(13, 148, 136, 0.35) !important;
                background: #ffffff !important;
                color: #0f766e !important;
                font-weight: 600 !important;
            }
            div[data-testid="stExpander"] {
                border: 1px solid rgba(13, 148, 136, 0.2);
                border-radius: 14px;
                background: rgba(255,255,255,0.85);
                overflow: hidden;
            }
            [data-testid="stMetric"] {
                background: rgba(255,255,255,0.9);
                border: 1px solid rgba(13, 148, 136, 0.15);
                border-radius: 14px;
                padding: 12px 14px;
            }
            .stTextInput > div > div > input,
            .stNumberInput input,
            .stSelectbox > div > div {
                border-radius: 10px !important;
            }
            .stSuccess, .stInfo, .stWarning, .stError {
                border-radius: 12px !important;
            }
            hr {
                border: none;
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(13,148,136,0.35), transparent);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
