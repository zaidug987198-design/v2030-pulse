"""
╔══════════════════════════════════════════════════════════════════════╗
║  Saudi Vision 2030 Strategic Intelligence Hub                       ║
║  مؤشر تقدم رؤية المملكة العربية السعودية 2030                      ║
║  Built by: Mohammad Zaid | Jamia Hamdard | Google Gen AI APAC 2026  ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from io import StringIO

# ══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="رؤية 2030 | V2030 Intelligence Hub",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/mohammad-zaid-289368379/",
        "About": "V2030 Intelligence Hub | Built by Mohammad Zaid"
    }
)

# ══════════════════════════════════════════════════════════════
# VISION 2030 LOGO — Inline SVG
# ══════════════════════════════════════════════════════════════
LOGO_SVG = """
<svg width="180" height="56" viewBox="0 0 180 56" xmlns="http://www.w3.org/2000/svg">
  <rect width="180" height="56" rx="10" fill="#005C2E"/>
  <rect x="4" y="4" width="48" height="48" rx="7" fill="rgba(255,255,255,0.10)"/>
  <line x1="28" y1="42" x2="28" y2="24" stroke="#D4A017" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M28 24 Q21 17 14 19" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M28 24 Q24 15 28 12" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M28 24 Q35 17 42 20" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M28 24 Q30 16 34 15" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M28 24 Q26 16 22 15" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <line x1="15" y1="37" x2="41" y2="46" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
  <line x1="41" y1="37" x2="15" y2="46" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
  <text x="60" y="20" font-family="Arial" font-size="9" font-weight="600"
        fill="rgba(255,255,255,0.75)" letter-spacing="0.8">KINGDOM OF SAUDI ARABIA</text>
  <text x="60" y="36" font-family="Arial" font-size="16" font-weight="900"
        fill="#FFFFFF" letter-spacing="-0.3">VISION 2030</text>
  <text x="60" y="49" font-family="Arial" font-size="9" font-weight="500"
        fill="rgba(255,255,255,0.70)" letter-spacing="0.3">رؤية المملكة العربية السعودية</text>
</svg>
"""

# ══════════════════════════════════════════════════════════════
# ENTERPRISE CSS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Outfit', 'IBM Plex Sans Arabic', sans-serif !important;
    background-color: #F4F7FB !important;
}
.main .block-container { padding: 1.5rem 2rem 2rem !important; max-width: 1440px !important; }
#MainMenu, footer, header, .stDeployButton { display: none !important; }

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 2px solid #E4EAF2 !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.07) !important;
}
[data-testid="stSidebar"] .stRadio label {
    color: #1A2B4A !important; font-weight: 500 !important; font-size: 13.5px !important;
}
[data-testid="stSidebar"] .stTextInput input {
    border: 1.5px solid #E4EAF2 !important; border-radius: 8px !important;
    font-size: 13px !important; color: #0D1F2D !important;
}
[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: #005C2E !important; box-shadow: 0 0 0 3px rgba(0,92,46,0.12) !important;
}

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1.5px solid #E4EAF2 !important;
    border-radius: 14px !important;
    padding: 1.1rem 1.25rem !important;
    box-shadow: 0 2px 14px rgba(0,80,40,0.07) !important;
    transition: transform 0.22s ease, box-shadow 0.22s ease !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 24px rgba(0,80,40,0.13) !important;
}
[data-testid="stMetric"] label {
    color: #5A7080 !important; font-size: 11px !important;
    font-weight: 700 !important; text-transform: uppercase !important;
    letter-spacing: 0.7px !important;
}
[data-testid="stMetricValue"] {
    color: #0D1F2D !important; font-size: 1.9rem !important;
    font-weight: 800 !important; line-height: 1.1 !important;
}
[data-testid="stMetricDelta"] { font-size: 12px !important; font-weight: 600 !important; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background: #FFFFFF !important; border-radius: 14px !important;
    padding: 5px !important; gap: 3px !important;
    border: 1.5px solid #E4EAF2 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    margin-bottom: 1.5rem !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important; border-radius: 10px !important;
    color: #5A7080 !important; font-weight: 600 !important;
    font-size: 13px !important; padding: 9px 16px !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,#004D26,#007A3D) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(0,92,46,0.28) !important;
}

/* DOWNLOAD BUTTON */
.stDownloadButton button {
    background: linear-gradient(135deg,#004D26,#007A3D) !important;
    color: #FFFFFF !important; border: none !important;
    border-radius: 10px !important; font-weight: 700 !important;
    font-size: 12.5px !important; padding: 8px 18px !important;
    transition: all 0.2s !important;
}
.stDownloadButton button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 16px rgba(0,92,46,0.28) !important;
}

/* PREMIUM BUTTON */
.stButton button {
    background: linear-gradient(135deg,#004D26,#007A3D) !important;
    color: #FFFFFF !important; border: none !important;
    border-radius: 10px !important; font-weight: 700 !important;
    font-size: 13px !important;
}

hr { border-color: #E4EAF2 !important; margin: 1.25rem 0 !important; }
[data-testid="stDataFrame"] {
    border-radius: 12px !important; border: 1.5px solid #E4EAF2 !important; overflow: hidden !important;
}
.stSuccess { background: #F0FDF6 !important; border-color: #007A3D !important; color: #004D26 !important; }
.stInfo { background: #EFF6FF !important; }

/* CUSTOM */
.sec-label {
    font-size: 10.5px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 1.4px; color: #5A7080; margin-bottom: 0.75rem;
}
.icard {
    background: #FFFFFF; border: 1.5px solid #E4EAF2;
    border-radius: 14px; padding: 1.25rem; height: 100%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.icard h4 { color: #0D1F2D; font-size: 14.5px; font-weight: 700; margin: 0 0 0.85rem; }
.iitem { display: flex; gap: 10px; margin-bottom: 10px; align-items: flex-start; }
.idot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; margin-top: 5px; }
.itxt { font-size: 13px; color: #334155; line-height: 1.6; margin: 0; }
.pb-wrap { background: #E4EAF2; border-radius: 8px; height: 10px; margin: 6px 0; overflow: hidden; }
.ar { font-family: 'IBM Plex Sans Arabic', sans-serif; }
.premium-banner {
    background: linear-gradient(135deg,#1A1000,#2D1E00);
    border: 1.5px solid #D4A017; border-radius: 12px;
    padding: 1rem 1.25rem; margin: 1rem 0;
}
.ml-badge {
    display: inline-block; background: rgba(0,92,46,0.12);
    color: #005C2E; font-size: 11px; font-weight: 700;
    padding: 3px 10px; border-radius: 12px;
    border: 1px solid rgba(0,92,46,0.25); margin-right: 5px;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# COLOR PALETTE
# ══════════════════════════════════════════════════════════════
C = {
    "g1": "#004D26", "g2": "#007A3D", "g3": "#00A651",
    "g_pale": "#E6F7EE", "g_border": "#BBF7D0",
    "gold": "#D4A017", "gold_d": "#B8860B", "gold_pale": "#FFFBEB",
    "b1": "#1E40AF", "b2": "#2563EB", "b3": "#60A5FA", "b_pale": "#EFF6FF",
    "red": "#DC2626", "red_pale": "#FEF2F2",
    "navy": "#0D1F2D", "slate": "#5A7080",
    "border": "#E4EAF2", "bg": "#F4F7FB", "white": "#FFFFFF",
}

# ══════════════════════════════════════════════════════════════
# ML FORECAST FUNCTION
# ══════════════════════════════════════════════════════════════
def ml_forecast(years, values, forecast_years):
    """Polynomial regression forecast using numpy"""
    x = np.array(years, dtype=float)
    y = np.array(values, dtype=float)
    x_norm = x - x.mean()
    coeffs = np.polyfit(x_norm, y, deg=2)
    poly = np.poly1d(coeffs)
    fx = np.array(forecast_years, dtype=float)
    fx_norm = fx - x.mean()
    return poly(fx_norm).tolist()

# ══════════════════════════════════════════════════════════════
# CHART LAYOUT
# ══════════════════════════════════════════════════════════════
def CL(title, yrange=None):
    L = dict(
        title=dict(text=title, font=dict(size=14.5, color=C["navy"],
                   family="Outfit"), x=0, xanchor="left"),
        plot_bgcolor=C["white"], paper_bgcolor=C["white"],
        font=dict(family="Outfit", color=C["navy"], size=12.5),
        legend=dict(bgcolor=C["bg"], bordercolor=C["border"],
                    borderwidth=1.5, font=dict(size=11.5, color=C["navy"]),
                    orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
        xaxis=dict(gridcolor="#EEF2F7", linecolor=C["border"],
                   tickfont=dict(color=C["slate"], size=12),
                   title_font=dict(color=C["slate"])),
        yaxis=dict(gridcolor="#EEF2F7", linecolor=C["border"],
                   tickfont=dict(color=C["slate"], size=12),
                   title_font=dict(color=C["slate"]),
                   zerolinecolor=C["border"]),
        margin=dict(l=16, r=16, t=60, b=28),
        hoverlabel=dict(bgcolor=C["navy"], font_color=C["white"],
                        font_size=12.5, bordercolor=C["navy"]),
    )
    if yrange:
        L["yaxis"]["range"] = yrange
    return L

# ══════════════════════════════════════════════════════════════
# CSV DOWNLOAD HELPER
# ══════════════════════════════════════════════════════════════
def to_csv(df):
    return df.to_csv(index=False).encode("utf-8")

# ══════════════════════════════════════════════════════════════
# ALL DATA
# ══════════════════════════════════════════════════════════════
HIST_YEARS  = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
FORE_YEARS  = [2025,2026,2027,2028,2029,2030]
ALL_YEARS   = HIST_YEARS + FORE_YEARS

gdp_df = pd.DataFrame({
    "Year":          HIST_YEARS,
    "Oil GDP %":     [43,42,44,41,35,40,46,39,37],
    "Non-Oil GDP %": [57,58,56,59,65,60,54,61,63],
})
tourism_df = pd.DataFrame({
    "Year":         [2019,2020,2021,2022,2023,2024],
    "Visitors (M)":[100, 41,  63,  93,  106, 115],
    "Target 2030": [150]*6,
})
emp_df = pd.DataFrame({
    "Year":          HIST_YEARS,
    "Female Emp %":  [17,18,20,23,25,27,30,32,34],
    "Target (30%)":  [30]*9,
})
ai_df = pd.DataFrame({
    "Initiative":     ["HUMAIN (PIF)","Nvidia Deal","AWS Saudi",
                       "Google Cloud","Microsoft"],
    "Amount (USD B)": [100.0,14.9,5.3,1.0,1.5],
    "Category":       ["Sovereign AI","AI Hardware","Cloud Infra",
                       "Cloud Infra","Cloud Infra"],
})
sectors_df = pd.DataFrame({
    "Sector":              ["Tourism","Technology","Healthcare",
                            "Entertainment","Mining","Logistics"],
    "Investment (SAR B)":  [134,89,67,45,38,29],
    "Growth %":            [38, 24,19, 31,15,22],
    "Jobs Created (000s)": [250,180,120,95, 60,75],
})
digital_df = pd.DataFrame({
    "Year":              HIST_YEARS,
    "Digital Pay %":     [31,38,45,52,60,67,72,77,79],
    "E-Commerce (SAR B)":[12,15,19,25,32,45,58,71,85],
})
giga_df = pd.DataFrame({
    "Project":    ["NEOM","The Line","Qiddiya","Red Sea","ROSHN"],
    "Budget($B)": [500,200,8,28,20],
    "Status":     ["In Progress","Construction","Phase 1","Open","Ongoing"],
    "Focus":      ["Smart City AI","Urban Living","Entertainment",
                   "Eco Tourism","National Housing"],
})

# ML Forecasts
non_oil_fore  = ml_forecast(HIST_YEARS, gdp_df["Non-Oil GDP %"].tolist(), FORE_YEARS)
oil_fore      = ml_forecast(HIST_YEARS, gdp_df["Oil GDP %"].tolist(), FORE_YEARS)
female_fore   = ml_forecast(HIST_YEARS, emp_df["Female Emp %"].tolist(), FORE_YEARS)
digital_fore  = ml_forecast(HIST_YEARS, digital_df["Digital Pay %"].tolist(), FORE_YEARS)
tourism_fore  = ml_forecast(
    tourism_df["Year"].tolist(),
    tourism_df["Visitors (M)"].tolist(),
    FORE_YEARS
)

# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(LOGO_SVG, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<p class="sec-label">Audience View | نوع المستخدم</p>',
                unsafe_allow_html=True)
    view_mode = st.radio(
        "View:",
        ["🏛️ Government & Policy",
         "💼 HR & Talent Acquisition",
         "📊 Investors & Analysts",
         "👥 Public / General"],
        label_visibility="collapsed"
    )
    st.divider()

    # ── LEAD CAPTURE ──
    st.markdown("""
    <div style="background:linear-gradient(135deg,#F0FDF6,#E6F7EE);
                border:1.5px solid #BBF7D0; border-radius:12px;
                padding:1rem; margin-bottom:10px;">
        <p style="font-size:12px; font-weight:800; color:#004D26;
                   margin:0 0 4px; text-transform:uppercase;
                   letter-spacing:0.8px;">
            📩 Subscribe to Saudi Insights
        </p>
        <p style="font-size:11px; color:#5A7080; margin:0 0 8px;
                   font-family:'IBM Plex Sans Arabic',sans-serif;">
            اشترك للحصول على تقارير رؤية 2030
        </p>
    </div>
    """, unsafe_allow_html=True)
    email_input = st.text_input(
        "Your Email Address",
        placeholder="name@company.com",
        label_visibility="collapsed"
    )
    if st.button("✉️  Subscribe — Free Weekly Brief", use_container_width=True):
        if email_input and "@" in email_input:
            st.success(f"✅ Subscribed! We'll send V2030 intelligence to {email_input}")
        else:
            st.warning("⚠️ Please enter a valid email address.")
    st.divider()

    # ── B2B CONSULTING ──
    st.markdown("""
    <div style="background:linear-gradient(135deg,#FFFBEB,#FEF3C7);
                border:1.5px solid #D4A017; border-radius:12px;
                padding:1rem; margin-bottom:10px;">
        <p style="font-size:12px; font-weight:800; color:#92400E;
                   margin:0 0 6px; text-transform:uppercase;
                   letter-spacing:0.7px;">
            💼 Enterprise Consulting
        </p>
        <p style="font-size:12px; color:#334155; line-height:1.6; margin:0 0 8px;">
            Need custom <b>Saudi market intelligence</b>,
            data pipelines, or bilingual AI dashboards for
            your Vision 2030 project?
        </p>
        <p style="font-size:11px; color:#5A7080; margin:0 0 8px;
                   font-family:'IBM Plex Sans Arabic',sans-serif;">
            تحليلات مخصصة للسوق السعودي ورؤية 2030
        </p>
        <p style="font-size:12px; font-weight:700; color:#004D26; margin:0;">
            Contact: <b>Mohammad Zaid</b><br>
            BCA · Jamia Hamdard<br>
            Hafiz-e-Quran · Arabic C1<br>
            Google Gen AI APAC 2026
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <a href="mailto:zaidug987198@gmail.com"
       style="display:block; background:linear-gradient(135deg,#D4A017,#F0C040);
              color:#1A1000; text-decoration:none; border-radius:10px;
              padding:9px 14px; font-size:12px; font-weight:800;
              text-align:center; margin-bottom:6px;">
        📧 &nbsp;Request Custom Report
    </a>
    """, unsafe_allow_html=True)
    st.divider()

    # ── SYSTEM ──
    st.markdown('<p class="sec-label">System Status</p>', unsafe_allow_html=True)
    st.success("✅ Data Pipeline: Live")
    st.info("🤖 ML Forecasting: Active")
    st.caption("📅 Updated: May 2026")
    st.divider()

    # ── DEVELOPER CARD ──
    st.markdown("""
    <div style="background:#F0FDF6; border:1.5px solid #BBF7D0;
                border-radius:12px; padding:.9rem; margin-bottom:10px;">
        <p style="font-size:10px; font-weight:700; color:#004D26;
                   margin:0 0 4px; text-transform:uppercase; letter-spacing:0.8px;">
            Built by
        </p>
        <p style="font-size:14px; font-weight:800; color:#0D1F2D; margin:0;">
            Mohammad Zaid
        </p>
        <p style="font-size:11px; color:#5A7080; margin:4px 0 0; line-height:1.7;">
            🕌 Hafiz-e-Quran<br>
            🗣️ Arabic C1 — DPA Jamia Hamdard<br>
            ☁️ Google Gen AI APAC 2026<br>
            🎓 BCA — Jamia Hamdard University
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <a href="https://github.com/zaidug987198-design/v2030-pulse"
       target="_blank"
       style="display:block; background:#0D1F2D; color:#FFFFFF;
              text-decoration:none; border-radius:9px; padding:8px 14px;
              font-size:12px; font-weight:700; text-align:center;
              margin-bottom:6px;">
        🐙 &nbsp;GitHub — v2030-pulse
    </a>
    <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/"
       target="_blank"
       style="display:block; background:#0A66C2; color:#FFFFFF;
              text-decoration:none; border-radius:9px; padding:8px 14px;
              font-size:12px; font-weight:700; text-align:center;">
        💼 &nbsp;LinkedIn Profile
    </a>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="background:linear-gradient(135deg,#003D1E 0%,#005C2E 40%,#007A3D 75%,#00A651 100%);
            border-radius:20px; padding:1.75rem 2rem; margin-bottom:1.75rem;
            box-shadow:0 10px 40px rgba(0,60,30,0.28);">
  <div style="display:flex; align-items:center;
              justify-content:space-between; flex-wrap:wrap; gap:16px;">
    <div style="display:flex; align-items:center; gap:18px;">
      <div style="flex-shrink:0;">{LOGO_SVG}</div>
      <div>
        <p style="color:rgba(255,255,255,0.60); font-size:10px; font-weight:700;
                   letter-spacing:2.5px; margin:0 0 3px; text-transform:uppercase;">
          KINGDOM OF SAUDI ARABIA · 2026
        </p>
        <h1 style="color:#FFFFFF; margin:0; font-size:1.75rem; font-weight:800;
                    letter-spacing:-0.5px; line-height:1.2;">
          Vision 2030 Intelligence Hub
        </h1>
        <p style="color:rgba(255,255,255,0.82); margin:5px 0 0; font-size:14px;
                   font-family:'IBM Plex Sans Arabic',sans-serif;
                   direction:rtl; text-align:right;">
          لوحة تحليلات استراتيجية لرؤية المملكة العربية السعودية 2030
        </p>
        <p style="color:rgba(255,255,255,0.65); margin:3px 0 0; font-size:12px;">
          National Transformation &amp; Economic Intelligence ·
          <span style="background:rgba(212,160,23,0.3); color:#FFE080;
                        padding:1px 7px; border-radius:8px; font-size:11px;
                        font-weight:700;">
            🤖 ML Forecasting Active
          </span>
        </p>
      </div>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">
      <span style="background:rgba(255,255,255,0.17); color:#FFFFFF; padding:5px 13px;
                    border-radius:20px; font-size:11.5px; font-weight:600;
                    border:1px solid rgba(255,255,255,0.27);">📊 Live Analytics</span>
      <span style="background:rgba(255,255,255,0.17); color:#FFFFFF; padding:5px 13px;
                    border-radius:20px; font-size:11.5px; font-weight:600;
                    border:1px solid rgba(255,255,255,0.27);">🌍 Global Standards</span>
      <span style="background:rgba(212,160,23,0.32); color:#FFE080; padding:5px 13px;
                    border-radius:20px; font-size:11.5px; font-weight:600;
                    border:1px solid rgba(212,160,23,0.42);">⭐ Vision 2030 Aligned</span>
    </div>
  </div>
  <!-- Arabic KPI Strip -->
  <div style="margin-top:1.2rem; padding-top:1rem;
              border-top:1px solid rgba(255,255,255,0.16);
              display:flex; gap:24px; flex-wrap:wrap;">
    {"".join([f'''
    <div style="text-align:center; min-width:80px;">
      <p style="color:#FFE080; font-size:1.25rem; font-weight:800; margin:0;">{val}</p>
      <p style="color:rgba(255,255,255,0.72); font-size:9.5px; margin:2px 0 0;
                 font-family:'IBM Plex Sans Arabic',sans-serif;">{ar}</p>
    </div>''' for val, ar in [
        ("50.2%","الناتج غير النفطي"),
        ("115M","السياح الدوليون"),
        ("33.6%","توظيف المرأة"),
        ("$122B","استثمار الذكاء الاصطناعي"),
        ("79%","المدفوعات الرقمية"),
        ("SAR 134B","إيرادات السياحة"),
    ]])}
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# KPI CARDS
# ══════════════════════════════════════════════════════════════
st.markdown('<p class="sec-label">مؤشرات الأداء الرئيسية — Key Performance Indicators 2024</p>',
            unsafe_allow_html=True)
k1,k2,k3,k4,k5,k6 = st.columns(6)
k1.metric("Non-Oil GDP | غير النفطي",    "50.2%",    "↑ 4.1%  ✅ Target")
k2.metric("Tourism Rev | السياحة",        "SAR 134B", "↑ 38%  YoY")
k3.metric("Female Emp | توظيف المرأة",   "33.6%",    "↑ 8.2%  ✅ Exceeded")
k4.metric("Digital Pay | الدفع الرقمي",  "79.0%",    "↑ 22%  SAMA")
k5.metric("AI Investment | الذكاء",      "$122.7B",  "↑ HUMAIN Deal")
k6.metric("Startups | الشركات الناشئة",  "$1.72B",   "↑ 145%  VC Funding")
st.divider()

# ══════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════
tab1,tab2,tab3,tab4,tab5 = st.tabs([
    "📈  Economy | الاقتصاد",
    "✈️  Tourism | السياحة",
    "🏭  Sectors & Giga-Projects",
    "👩‍💼  Employment | التوظيف",
    "🤖  AI & Tech | الذكاء الاصطناعي",
])

# ══════════════════════════════════════════════════════════════
# TAB 1 — ECONOMY
# ══════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
               border-right:3px solid #005C2E; font-size:12px; color:#5A7080;
               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; text-align:right;">
       التنويع الاقتصادي — نسبة الناتج المحلي النفطي مقابل غير النفطي مع التوقعات حتى 2030
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>'
                '<span class="ml-badge">📊 Polynomial Regression</span>'
                '<span class="ml-badge">Horizon: 2030</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_chart, col_info = st.columns([2.3, 1])
    with col_chart:
        fig1 = go.Figure()
        # Historical
        fig1.add_trace(go.Scatter(
            x=gdp_df["Year"], y=gdp_df["Non-Oil GDP %"],
            name="Non-Oil GDP % (Historical)",
            mode="lines+markers",
            line=dict(color=C["g2"], width=3.5),
            marker=dict(size=9, color=C["g2"], line=dict(color=C["white"], width=2.5)),
            fill="tozeroy", fillcolor="rgba(0,122,61,0.08)",
            hovertemplate="<b>%{x}</b><br>Non-Oil GDP: %{y:.1f}%<extra></extra>",
        ))
        fig1.add_trace(go.Scatter(
            x=gdp_df["Year"], y=gdp_df["Oil GDP %"],
            name="Oil GDP % (Historical)",
            mode="lines+markers",
            line=dict(color=C["gold"], width=3, dash="dot"),
            marker=dict(size=9, color=C["gold"], line=dict(color=C["white"], width=2.5)),
            hovertemplate="<b>%{x}</b><br>Oil GDP: %{y:.1f}%<extra></extra>",
        ))
        # ML Forecasts
        fig1.add_trace(go.Scatter(
            x=FORE_YEARS, y=non_oil_fore,
            name="Non-Oil GDP % (ML Forecast 2030)",
            mode="lines+markers",
            line=dict(color=C["g3"], width=2.5, dash="dash"),
            marker=dict(size=7, symbol="diamond", color=C["g3"]),
            fill="tonexty", fillcolor="rgba(0,166,81,0.04)",
            hovertemplate="<b>%{x} (Forecast)</b><br>Non-Oil GDP: %{y:.1f}%<extra></extra>",
        ))
        fig1.add_trace(go.Scatter(
            x=FORE_YEARS, y=oil_fore,
            name="Oil GDP % (ML Forecast 2030)",
            mode="lines",
            line=dict(color="#F0C040", width=2, dash="dot"),
            hovertemplate="<b>%{x} (Forecast)</b><br>Oil GDP: %{y:.1f}%<extra></extra>",
        ))
        fig1.add_vline(x=2024.5, line_dash="dot", line_color="#94A3B8",
                       annotation_text="  Forecast →", annotation_font_size=11,
                       annotation_font_color="#94A3B8")
        fig1.add_hline(y=50, line_dash="dash", line_color=C["red"], line_width=1.5,
                       annotation_text="  رؤية 2030 Target: 50% ✅",
                       annotation_font_color=C["red"], annotation_font_size=11.5)
        fig1.update_layout(**CL("Oil vs Non-Oil GDP Share (%) + ML Forecast to 2030 | الناتج المحلي", [28,75]))
        st.plotly_chart(fig1, use_container_width=True)

        r1,r2 = st.columns([3,1])
        with r1:
            forecast_val = round(non_oil_fore[-1], 1)
            st.info(f"🤖 **ML Forecast 2030:** Non-Oil GDP projected at **{forecast_val}%** — "
                    f"{'above' if forecast_val >= 50 else 'approaching'} Vision 2030 target.")
        with r2:
            gdp_export = pd.concat([
                gdp_df,
                pd.DataFrame({"Year": FORE_YEARS,
                              "Non-Oil GDP % (Forecast)": [round(v,2) for v in non_oil_fore],
                              "Oil GDP % (Forecast)":     [round(v,2) for v in oil_fore]})
            ], ignore_index=True)
            st.download_button("📥 Download Dataset",
                               data=to_csv(gdp_export),
                               file_name="v2030_gdp_forecast.csv",
                               mime="text/csv",
                               use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="icard">
            <h4>📊 Economic Insights | رؤى اقتصادية</h4>
            <div class="iitem">
                <div class="idot" style="background:#005C2E;"></div>
                <p class="itxt"><b>Target Achieved:</b> Non-Oil GDP hit
                <b style="color:#005C2E;">50.2%</b> in 2024 — ahead of schedule ✅</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#D4A017;"></div>
                <p class="itxt"><b>Nitaqat Program:</b> Saudization quotas driving
                unemployment below <b>7%</b> — historic low.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#2563EB;"></div>
                <p class="itxt"><b>FDI Surge:</b> Foreign Direct Investment
                exceeded <b>SAR 100B</b> in 2024.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#DC2626;"></div>
                <p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English
                AI & Cloud talent is #1 shortage in Saudi tech market.</p>
            </div>
            <div style="background:#F0FDF6; border-radius:10px; padding:10px 12px;
                        margin-top:8px; border:1.5px solid #BBF7D0;">
                <p style="margin:0; font-size:12px; font-weight:700; color:#005C2E;">
                    ✅ Vision 2030 GDP Target: ACHIEVED
                </p>
                <div class="pb-wrap">
                    <div style="background:linear-gradient(90deg,#005C2E,#00A651);
                                 height:10px; width:100%; border-radius:8px;"></div>
                </div>
                <p style="margin:0; font-size:11px; color:#5A7080;">100.4% complete</p>
            </div>
            <div style="margin-top:10px; background:#FFFBEB; border-radius:10px;
                        padding:10px 12px; border:1px solid #FDE68A;">
                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
                    📡 Data Sources
                </p>
                <p style="margin:0; font-size:11px; color:#5A7080;">
                    GASTAT · open.data.gov.sa<br>
                    vision2030.gov.sa · World Bank
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Digital Economy chart
    st.markdown("---")
    st.markdown("##### 💳 Digital Economy Growth | نمو الاقتصاد الرقمي")
    dc1, dc2 = st.columns([2.3,1])
    with dc1:
        fig_d = go.Figure()
        fig_d.add_trace(go.Bar(
            x=digital_df["Year"], y=digital_df["Digital Pay %"],
            name="Digital Payments %",
            marker_color=[C["g1"] if y<=2024 else C["g3"] for y in digital_df["Year"]],
            text=digital_df["Digital Pay %"].astype(str)+"%",
            textposition="outside",
            textfont=dict(color=C["navy"], size=12),
        ))
        # Forecast bars
        fig_d.add_trace(go.Bar(
            x=FORE_YEARS, y=[round(v,1) for v in digital_fore],
            name="Digital Payments % (Forecast)",
            marker_color="rgba(0,166,81,0.4)",
            marker_line=dict(color=C["g3"], width=1.5),
            text=[f"{round(v,1)}%*" for v in digital_fore],
            textposition="outside",
            textfont=dict(color=C["g2"], size=12),
        ))
        fig_d.update_layout(**CL("Digital Payments Adoption (%) + ML Forecast | المدفوعات الرقمية", [0,105]))
        st.plotly_chart(fig_d, use_container_width=True)
        dc_r1, dc_r2 = st.columns([3,1])
        with dc_r1:
            st.info(f"🤖 **ML Forecast:** Digital payments projected at "
                    f"**{round(digital_fore[-1],1)}%** by 2030 — SAMA Vision target: 80%+")
        with dc_r2:
            dig_export = pd.concat([
                digital_df,
                pd.DataFrame({"Year": FORE_YEARS,
                              "Digital Pay % (Forecast)": [round(v,2) for v in digital_fore]})
            ], ignore_index=True)
            st.download_button("📥 Download", to_csv(dig_export),
                               "v2030_digital_forecast.csv", "text/csv",
                               use_container_width=True)
    with dc2:
        st.markdown("""
        <div class="icard">
            <h4>💳 Digital Economy</h4>
            <div class="iitem">
                <div class="idot" style="background:#005C2E;"></div>
                <p class="itxt"><b>79%</b> digital payment adoption 2024 —
                up from just 31% in 2016.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#2563EB;"></div>
                <p class="itxt">E-commerce market reached
                <b>SAR 85B</b> in 2024 — growing 20%+ YoY.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#D4A017;"></div>
                <p class="itxt"><b>STC Pay, stc, Tamara, Foodics</b> —
                Saudi fintech unicorns fueling digital growth.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Premium Banner
    st.markdown("""
    <div class="premium-banner">
        <p style="color:#D4A017; font-size:12px; font-weight:800;
                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
            🔒 Premium Deep-Dive Report Available
        </p>
        <p style="color:rgba(255,255,255,0.85); font-size:13px; margin:0 0 4px;">
            <b>Saudi Economy Intelligence Report 2026</b> — Full GDP breakdown,
            sector analysis, investment forecasts to 2030.
        </p>
        <p style="color:rgba(255,255,255,0.60); font-size:12px; margin:0;">
            📩 Contact: zaidug987198@gmail.com &nbsp;|&nbsp;
            <b style="color:#D4A017;">SAR 500 – 2,000</b> &nbsp;|&nbsp;
            Bilingual Arabic–English format available
        </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 2 — TOURISM
# ══════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
               border-right:3px solid #005C2E; font-size:12px; color:#5A7080;
               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; text-align:right;">
       أداء قطاع السياحة مع توقعات ML حتى 2030 · الهدف: 150 مليون زائر سنوياً
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_chart, col_info = st.columns([2.3, 1])
    with col_chart:
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=tourism_df["Year"], y=tourism_df["Visitors (M)"],
            name="Actual Visitors (M)",
            marker=dict(
                color=[C["g1"],C["red"],C["gold"],C["g2"],C["g3"],C["g1"]],
                line=dict(color=C["white"], width=1.5)
            ),
            text=tourism_df["Visitors (M)"].astype(str)+"M",
            textposition="outside",
            textfont=dict(color=C["navy"], size=12.5, family="Outfit"),
        ))
        fig2.add_trace(go.Bar(
            x=FORE_YEARS, y=[round(v,1) for v in tourism_fore],
            name="Visitors ML Forecast (M)",
            marker=dict(color="rgba(0,166,81,0.35)",
                        line=dict(color=C["g3"], width=1.5)),
            text=[f"{round(v,0):.0f}M*" for v in tourism_fore],
            textposition="outside",
            textfont=dict(color=C["g2"], size=12),
        ))
        fig2.add_hline(y=150, line_dash="dash", line_color=C["red"], line_width=2,
                       annotation_text="  2030 Target: 150M visitors",
                       annotation_font_color=C["red"], annotation_font_size=12)
        fig2.update_layout(**CL("Tourism Visitors (M) + ML Forecast to 2030 | السياحة", [0,190]))
        st.plotly_chart(fig2, use_container_width=True)

        tr1, tr2 = st.columns([3,1])
        with tr1:
            proj_2030 = round(tourism_fore[-1], 0)
            target_met = "✅ On track to meet" if proj_2030 >= 140 else "⚠️ May fall short of"
            st.info(f"🤖 **ML Forecast 2030:** {proj_2030:.0f}M visitors projected. "
                    f"{target_met} the 150M Vision 2030 target.")
        with tr2:
            t_export = pd.concat([
                tourism_df,
                pd.DataFrame({"Year": FORE_YEARS,
                              "Visitors (M) Forecast": [round(v,1) for v in tourism_fore],
                              "Target 2030": [150]*6})
            ], ignore_index=True)
            st.download_button("📥 Download", to_csv(t_export),
                               "v2030_tourism_forecast.csv", "text/csv",
                               use_container_width=True)

    with col_info:
        pct = int((115/150)*100)
        st.markdown(f"""
        <div class="icard">
            <h4>✈️ Tourism | السياحة</h4>
            <div style="text-align:center; margin-bottom:1rem;">
                <p style="font-size:2.8rem; font-weight:800; color:#005C2E;
                           margin:0; line-height:1;">76%</p>
                <p style="font-size:11.5px; color:#5A7080; margin:3px 0 0;">
                    of 2030 target reached<br>
                    <span class="ar" style="font-size:11px;">76% من الهدف 150 مليون</span>
                </p>
            </div>
            <div class="pb-wrap">
                <div style="background:linear-gradient(90deg,#005C2E,#00A651);
                             height:10px; width:{pct}%; border-radius:8px;"></div>
            </div>
            <div style="display:flex; justify-content:space-between;
                        font-size:11px; color:#5A7080; margin-bottom:1rem;">
                <span>0</span><span><b>115M</b></span><span>150M</span>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#005C2E;"></div>
                <p class="itxt"><b>SAR 134B</b> revenue 2024 — up <b style="color:#005C2E;">38%</b> YoY</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#2563EB;"></div>
                <p class="itxt"><b>250,000+</b> new tourism jobs for Saudi nationals</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#D4A017;"></div>
                <p class="itxt">NEOM, Red Sea, Qiddiya driving premium international tourism</p>
            </div>
            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
                        margin-top:8px; border:1px solid #FDE68A;">
                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
                    📡 Source: Saudi Tourism Authority
                </p>
                <p style="margin:0; font-size:11px; color:#5A7080;">sta.gov.sa · vision2030.gov.sa</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="premium-banner">
        <p style="color:#D4A017; font-size:12px; font-weight:800;
                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
            🔒 Premium Tourism Intelligence Report
        </p>
        <p style="color:rgba(255,255,255,0.85); font-size:13px; margin:0 0 4px;">
            Detailed Saudi tourism sector analysis — hotel occupancy,
            source markets, MICE industry, Hajj/Umrah tech opportunities.
        </p>
        <p style="color:rgba(255,255,255,0.60); font-size:12px; margin:0;">
            📩 zaidug987198@gmail.com &nbsp;|&nbsp;
            <b style="color:#D4A017;">SAR 750 – 1,500</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 3 — SECTORS & GIGA-PROJECTS
# ══════════════════════════════════════════════════════════════
with tab3:
    cp, cb = st.columns(2)
    with cp:
        fig3a = px.pie(
            sectors_df, values="Investment (SAR B)", names="Sector",
            title="Investment Distribution | توزيع الاستثمار (SAR B)",
            hole=0.42,
            color_discrete_sequence=[C["g1"],C["g2"],C["g3"],C["gold"],C["b2"],"#8B5CF6"],
        )
        fig3a.update_traces(
            textinfo="percent+label",
            textfont=dict(size=12.5, color=C["navy"], family="Outfit"),
            hovertemplate="<b>%{label}</b><br>SAR %{value}B<br>%{percent}<extra></extra>",
        )
        fig3a.update_layout(**CL(""))
        st.plotly_chart(fig3a, use_container_width=True)
    with cb:
        fig3b = px.bar(
            sectors_df.sort_values("Growth %", ascending=True),
            x="Growth %", y="Sector", orientation="h",
            title="YoY Growth Rate | معدل النمو السنوي (%)",
            color="Growth %",
            color_continuous_scale=["#A7F3D0","#007A3D","#004D26"],
            text="Growth %",
        )
        fig3b.update_traces(
            texttemplate="%{text}%", textposition="outside",
            textfont=dict(color=C["navy"], size=12.5, family="Outfit"),
        )
        fig3b.update_layout(**CL(""), coloraxis_showscale=False)
        st.plotly_chart(fig3b, use_container_width=True)

    sec_r1, sec_r2 = st.columns([3,1])
    with sec_r2:
        st.download_button("📥 Download Sector Data", to_csv(sectors_df),
                           "v2030_sectors.csv", "text/csv", use_container_width=True)

    # Giga-Projects
    st.markdown('<p class="sec-label" style="margin-top:1rem;">المشاريع العملاقة — Giga-Projects Tracker</p>',
                unsafe_allow_html=True)
    gcols = st.columns(5)
    clrs = [C["g1"],C["g2"],C["gold"],C["b2"],C["g3"]]
    for i, (_, row) in enumerate(giga_df.iterrows()):
        with gcols[i]:
            st.markdown(f"""
            <div style="background:#FFFFFF; border:1.5px solid #E4EAF2;
                        border-radius:14px; padding:1rem;
                        border-top:4px solid {clrs[i]};
                        box-shadow:0 2px 10px rgba(0,0,0,0.05); text-align:center;">
                <p style="font-size:14px; font-weight:800; color:{clrs[i]}; margin:0 0 3px;">
                    {row['Project']}</p>
                <p style="font-size:11px; color:#5A7080; margin:0 0 7px;">{row['Focus']}</p>
                <p style="font-size:1.35rem; font-weight:800; color:#0D1F2D; margin:0 0 5px;">
                    ${row['Budget($B)']}B</p>
                <span style="background:{clrs[i]}18; color:{clrs[i]};
                              font-size:10px; font-weight:700;
                              padding:2px 9px; border-radius:12px;">{row['Status']}</span>
            </div>
            """, unsafe_allow_html=True)

    # Sector table
    st.markdown("<br>", unsafe_allow_html=True)
    rows_html = "".join([f"""
    <tr style="background:{'#F4F7FB' if i%2==0 else '#FFFFFF'}; border-bottom:1px solid #E4EAF2;">
        <td style="padding:11px 16px; color:#0D1F2D; font-weight:600;">{r['Sector']}</td>
        <td style="padding:11px 16px; color:#0D1F2D; font-weight:700; text-align:right;">
            SAR {r['Investment (SAR B)']}B</td>
        <td style="padding:11px 16px; text-align:right;">
            <span style="background:#E6F7EE; color:#005C2E; font-weight:700;
                          padding:3px 10px; border-radius:12px; font-size:12px;">
                ↑ {r['Growth %']}%</span></td>
        <td style="padding:11px 16px; color:#5A7080; text-align:right;">{r['Jobs Created (000s)']}K+</td>
    </tr>""" for i,(_, r) in enumerate(sectors_df.iterrows())])

    st.markdown(f"""
    <table style="width:100%; border-collapse:collapse; font-family:Outfit,sans-serif;
                  font-size:13px; background:#FFFFFF; border-radius:12px; overflow:hidden;
                  border:1.5px solid #E4EAF2; box-shadow:0 2px 10px rgba(0,0,0,0.04);">
        <thead>
            <tr style="background:linear-gradient(135deg,#004D26,#007A3D);">
                <th style="padding:12px 16px; color:#FFFFFF; text-align:left; font-weight:700;">
                    Sector | القطاع</th>
                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
                    Investment</th>
                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
                    YoY Growth</th>
                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
                    Jobs Created</th>
            </tr>
        </thead>
        <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 4 — EMPLOYMENT
# ══════════════════════════════════════════════════════════════
with tab4:
    st.markdown("""
    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
               border-right:3px solid #005C2E; font-size:12px; color:#5A7080;
               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; text-align:right;">
       مشاركة المرأة في سوق العمل + توقعات ML حتى 2030 · هدف رؤية 2030: 30% · تم تجاوزه ✅
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_chart, col_info = st.columns([2.3, 1])
    with col_chart:
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=emp_df["Year"], y=emp_df["Female Emp %"],
            name="Female Employment % (Historical)",
            mode="lines+markers",
            line=dict(color=C["g2"], width=3.5),
            marker=dict(size=10, color=C["g2"], line=dict(color=C["white"], width=2.5)),
            fill="tozeroy", fillcolor="rgba(0,122,61,0.08)",
        ))
        fig4.add_trace(go.Scatter(
            x=FORE_YEARS, y=[round(v,1) for v in female_fore],
            name="Female Emp % (ML Forecast)",
            mode="lines+markers",
            line=dict(color=C["g3"], width=2.5, dash="dash"),
            marker=dict(size=8, symbol="diamond", color=C["g3"],
                        line=dict(color=C["white"], width=2)),
            fill="tonexty", fillcolor="rgba(0,166,81,0.04)",
        ))
        fig4.add_hline(y=30, line_dash="dash", line_color=C["red"], line_width=1.5,
                       annotation_text="  رؤية 2030 Target: 30%",
                       annotation_font_color=C["red"], annotation_font_size=11.5)
        fig4.add_vline(x=2024.5, line_dash="dot", line_color="#94A3B8",
                       annotation_text="  Forecast →", annotation_font_size=10,
                       annotation_font_color="#94A3B8")
        fig4.add_annotation(
            x=2024, y=34.5,
            text="<b>33.6% — Target Exceeded! ✅</b>",
            showarrow=True, arrowhead=2,
            arrowcolor=C["g1"], arrowwidth=2,
            font=dict(color=C["g1"], size=12),
            bgcolor=C["g_pale"], bordercolor=C["g2"], borderwidth=1.5,
        )
        fig4.update_layout(**CL("Female Workforce Participation (%) + ML Forecast | توظيف المرأة", [12,48]))
        st.plotly_chart(fig4, use_container_width=True)

        er1, er2 = st.columns([3,1])
        with er1:
            st.info(f"🤖 **ML Forecast 2030:** Female employment projected at "
                    f"**{round(female_fore[-1],1)}%** by 2030 — "
                    f"well above the 30% Vision target.")
        with er2:
            e_export = pd.concat([
                emp_df,
                pd.DataFrame({"Year": FORE_YEARS,
                              "Female Emp % (Forecast)": [round(v,2) for v in female_fore]})
            ], ignore_index=True)
            st.download_button("📥 Download", to_csv(e_export),
                               "v2030_employment_forecast.csv", "text/csv",
                               use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="icard">
            <h4>👩‍💼 Employment | التوظيف</h4>
            <div style="background:#F0FDF6; border-radius:12px; padding:1rem;
                        margin-bottom:10px; border:1.5px solid #BBF7D0; text-align:center;">
                <p style="font-size:2.2rem; font-weight:800; color:#005C2E; margin:0;">33.6%</p>
                <p style="font-size:12px; color:#5A7080; margin:3px 0 0;">
                    Female Workforce 2024<br>
                    <b style="color:#005C2E;">30% Target — Exceeded ✅</b><br>
                    <span class="ar" style="font-size:11px;">تجاوز الهدف المحدد في رؤية 2030</span>
                </p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#005C2E;"></div>
                <p class="itxt">From <b>17%</b> in 2016 to <b>33.6%</b> in 2024
                — nearly <b style="color:#005C2E;">doubled</b> in 8 years.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#D4A017;"></div>
                <p class="itxt"><b>Nitaqat Saudization:</b> Mandatory
                localization quotas across all industries.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#2563EB;"></div>
                <p class="itxt"><b>Unemployment:</b> Below 7% —
                lowest in Saudi history.</p>
            </div>
            <div class="iitem">
                <div class="idot" style="background:#8B5CF6;"></div>
                <p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English
                AI talent is the #1 shortage in Vision 2030 companies.</p>
            </div>
            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
                        margin-top:8px; border:1px solid #FDE68A;">
                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
                    📡 Source: GASTAT</p>
                <p style="margin:0; font-size:11px; color:#5A7080;">stats.gov.sa</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 5 — AI & TECH
# ══════════════════════════════════════════════════════════════
with tab5:
    st.markdown("""
    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
               border-right:3px solid #005C2E; font-size:12px; color:#5A7080;
               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; text-align:right;">
       استثمارات المملكة العربية السعودية في الذكاء الاصطناعي والبنية التحتية التقنية — 2025
    </p>
    """, unsafe_allow_html=True)

    col_chart, col_info = st.columns([2.3, 1])
    with col_chart:
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            x=ai_df["Initiative"],
            y=ai_df["Amount (USD B)"],
            marker=dict(
                color=[C["g1"],C["gold"],C["b2"],C["b3"],"#8B5CF6"],
                line=dict(color=C["white"], width=2)
            ),
            text=["$"+str(v)+"B" for v in ai_df["Amount (USD B)"]],
            textposition="outside",
            textfont=dict(color=C["navy"], size=13, family="Outfit"),
            hovertemplate="<b>%{x}</b><br>$%{y}B<extra></extra>",
        ))
        fig5.update_layout(
            **CL("Saudi AI & Cloud Investment (USD B) | استثمارات الذكاء الاصطناعي 2025", [0,118]),
            showlegend=False,
        )
        st.plotly_chart(fig5, use_container_width=True)

        ai_r1, ai_r2 = st.columns([3,1])
        with ai_r1:
            st.info("🤖 Saudi Arabia's **$122.7B total AI investment** in 2025 makes it the "
                    "world's fastest-growing AI market — anchored by HUMAIN's $100B sovereign fund.")
        with ai_r2:
            st.download_button("📥 Download", to_csv(ai_df),
                               "v2030_ai_investment.csv", "text/csv",
                               use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="icard">
            <h4>🤖 AI & Tech | الذكاء الاصطناعي</h4>
            <div style="background:#F0FDF6; border-radius:10px; padding:10px 12px;
                        margin-bottom:8px; border-left:4px solid #005C2E;">
                <p style="margin:0; font-size:13px; font-weight:700; color:#005C2E;">
                    HUMAIN — $100B</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    PIF-backed sovereign AI company.<br>
                    Partners: Nvidia, AMD, AWS, Google<br>
                    <span class="ar" style="font-size:11px;">شركة الذكاء الاصطناعي السعودية</span>
                </p>
            </div>
            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
                        margin-bottom:8px; border-left:4px solid #D4A017;">
                <p style="margin:0; font-size:13px; font-weight:700; color:#B8860B;">
                    Nvidia Deal — $14.9B</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    Largest-ever GPU deal globally.<br>18,000+ Blackwell AI chips</p>
            </div>
            <div style="background:#EFF6FF; border-radius:10px; padding:10px 12px;
                        margin-bottom:8px; border-left:4px solid #2563EB;">
                <p style="margin:0; font-size:13px; font-weight:700; color:#1E40AF;">
                    AWS + Google + Microsoft</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    $7.8B combined cloud in Saudi Arabia</p>
            </div>
            <div style="background:linear-gradient(135deg,#004D26,#007A3D);
                        border-radius:10px; padding:12px; text-align:center;">
                <p style="color:#FFFFFF; margin:0; font-size:12px; font-weight:700;">
                    🤖 An-Nasir AI</p>
                <p style="color:rgba(255,255,255,0.8); margin:3px 0 0; font-size:11px;">
                    Arabic-English AI Agent<br>
                    Vertex AI + ADK · Vision 2030<br>
                    <span class="ar">وكيل ذكاء اصطناعي ثنائي اللغة</span>
                </p>
                <a href="https://github.com/zaidug987198-design/v2030-pulse"
                   target="_blank"
                   style="display:block; background:rgba(255,255,255,0.18);
                          color:#FFFFFF; text-decoration:none; border-radius:7px;
                          padding:5px 10px; font-size:11px; font-weight:700;
                          margin-top:8px; border:1px solid rgba(255,255,255,0.3);">
                    🐙 View on GitHub
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="premium-banner">
        <p style="color:#D4A017; font-size:12px; font-weight:800;
                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
            🔒 Unlock: Saudi AI Market Intelligence Report 2026
        </p>
        <p style="color:rgba(255,255,255,0.85); font-size:13px; margin:0 0 4px;">
            Complete Saudi AI ecosystem analysis — HUMAIN deep dive,
            Vision 2030 tech talent gaps, bilingual AI deployment strategies,
            investment landscape for Indian tech companies entering Saudi market.
        </p>
        <p style="color:rgba(255,255,255,0.60); font-size:12px; margin:0;">
            📩 zaidug987198@gmail.com &nbsp;|&nbsp;
            <b style="color:#D4A017;">SAR 1,000 – 2,000</b> &nbsp;|&nbsp;
            Arabic + English · Delivered in 5 business days
        </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.divider()
st.markdown(f"""
<div style="background:#FFFFFF; border:1.5px solid #E4EAF2; border-radius:16px;
            padding:1.25rem 1.75rem; display:flex; justify-content:space-between;
            align-items:center; flex-wrap:wrap; gap:14px;
            box-shadow:0 2px 10px rgba(0,0,0,0.04);">
    <div style="display:flex; align-items:center; gap:14px;">
        {LOGO_SVG}
        <div>
            <p style="margin:0; font-size:14px; font-weight:800; color:#0D1F2D;">
                V2030 Intelligence Hub</p>
            <p style="margin:3px 0 0; font-size:12px; color:#5A7080;">
                Data: open.data.gov.sa · vision2030.gov.sa · GASTAT · SDAIA · World Bank
            </p>
            <p style="margin:2px 0 0; font-size:11px; color:#94A3B8;
                       font-family:'IBM Plex Sans Arabic',sans-serif;">
                جميع البيانات من المصادر الحكومية السعودية الرسمية
            </p>
        </div>
    </div>
    <div style="text-align:right;">
        <p style="margin:0; font-size:13px; font-weight:700; color:#005C2E;">
            Engineered by Mohammad Zaid</p>
        <p style="margin:2px 0 4px; font-size:11.5px; color:#5A7080;">
            Hafiz-e-Quran · Arabic C1 · Google Gen AI APAC 2026 · Jamia Hamdard
        </p>
        <div style="display:flex; gap:7px; justify-content:flex-end;">
            <a href="https://github.com/zaidug987198-design/v2030-pulse"
               target="_blank"
               style="background:#0D1F2D; color:#FFFFFF; text-decoration:none;
                       border-radius:7px; padding:5px 12px; font-size:11.5px;
                       font-weight:700;">🐙 GitHub</a>
            <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/"
               target="_blank"
               style="background:#0A66C2; color:#FFFFFF; text-decoration:none;
                       border-radius:7px; padding:5px 12px; font-size:11.5px;
                       font-weight:700;">💼 LinkedIn</a>
            <a href="mailto:zaidug987198@gmail.com"
               style="background:linear-gradient(135deg,#D4A017,#F0C040);
                       color:#1A1000; text-decoration:none; border-radius:7px;
                       padding:5px 12px; font-size:11.5px; font-weight:700;">
                📧 Contact</a>
        </div>
    </div>
</div>
<p style="text-align:center; font-size:11px; color:#94A3B8; margin-top:10px;">
    © 2026 Mohammad Zaid | Python · Streamlit · Plotly · NumPy ML Forecasting |
    All data sourced from official Saudi government portals
</p>
""", unsafe_allow_html=True)