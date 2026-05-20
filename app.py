import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="V2030 Intelligence Hub | Saudi Arabia",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════════════════════
# PROFESSIONAL CSS — White + Saudi Green + Gold
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

/* ── GLOBAL ── */
html, body, [class*="css"], .stApp {
    font-family: 'Outfit', 'IBM Plex Sans Arabic', sans-serif !important;
    background-color: #F7F9FC !important;
}

.main .block-container {
    padding: 1.5rem 2rem 2rem !important;
    max-width: 1400px !important;
}

/* ── HIDE CLUTTER ── */
#MainMenu, footer, header, .stDeployButton { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 2px solid #E8EDF5 !important;
    box-shadow: 4px 0 20px rgba(0,0,0,0.06) !important;
}
[data-testid="stSidebar"] .stRadio label {
    color: #1A2B4A !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}

/* ── METRIC CARDS ── */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1.5px solid #E8EDF5 !important;
    border-radius: 14px !important;
    padding: 1.1rem 1.25rem !important;
    box-shadow: 0 2px 12px rgba(0,80,40,0.07) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,80,40,0.12) !important;
}
[data-testid="stMetric"] label {
    color: #5A7080 !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
}
[data-testid="stMetricValue"] {
    color: #0D1F2D !important;
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    line-height: 1.1 !important;
}
[data-testid="stMetricDelta"] {
    font-size: 12px !important;
    font-weight: 600 !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: #FFFFFF !important;
    border-radius: 14px !important;
    padding: 5px !important;
    gap: 3px !important;
    border: 1.5px solid #E8EDF5 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    margin-bottom: 1.5rem !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 10px !important;
    color: #5A7080 !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    padding: 9px 18px !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #005C2E, #007A3D) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(0,92,46,0.3) !important;
}

/* ── DIVIDER ── */
hr { border-color: #E8EDF5 !important; margin: 1.25rem 0 !important; }

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    border: 1.5px solid #E8EDF5 !important;
    overflow: hidden !important;
}

/* ── SUCCESS/INFO ── */
.stSuccess {
    background: #F0FDF6 !important;
    border-color: #007A3D !important;
    color: #004D26 !important;
}

/* ── CUSTOM CLASSES ── */
.section-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #5A7080;
    margin-bottom: 0.75rem;
}
.insight-card {
    background: #FFFFFF;
    border: 1.5px solid #E8EDF5;
    border-radius: 14px;
    padding: 1.25rem;
    height: 100%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.insight-card h4 {
    color: #0D1F2D;
    font-size: 15px;
    font-weight: 700;
    margin: 0 0 0.85rem;
}
.insight-item {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
    align-items: flex-start;
}
.insight-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
    margin-top: 5px;
}
.insight-text {
    font-size: 13px;
    color: #334155;
    line-height: 1.6;
}
.progress-bar-wrap {
    background: #E8EDF5;
    border-radius: 8px;
    height: 10px;
    margin: 6px 0;
    overflow: hidden;
}
.kpi-tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    margin-right: 5px;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# COLOR PALETTE
# ══════════════════════════════════════════════════════════════
C = {
    "green_dark":  "#005C2E",
    "green_mid":   "#007A3D",
    "green_light": "#00A651",
    "green_pale":  "#E6F7EE",
    "gold_dark":   "#B8860B",
    "gold_mid":    "#D4A017",
    "gold_light":  "#F0C040",
    "gold_pale":   "#FFFBEB",
    "blue_dark":   "#1E40AF",
    "blue_mid":    "#2563EB",
    "blue_light":  "#60A5FA",
    "blue_pale":   "#EFF6FF",
    "red":         "#DC2626",
    "red_pale":    "#FEF2F2",
    "navy":        "#0D1F2D",
    "slate":       "#5A7080",
    "border":      "#E8EDF5",
    "bg":          "#F7F9FC",
    "white":       "#FFFFFF",
}

# ══════════════════════════════════════════════════════════════
# CHART LAYOUT — consistent across all charts
# ══════════════════════════════════════════════════════════════
def chart_layout(title, yrange=None):
    layout = dict(
        title=dict(
            text=title,
            font=dict(size=15, color=C["navy"],
                      family="Outfit, sans-serif"),
            x=0,
            xanchor="left",
        ),
        plot_bgcolor=C["white"],
        paper_bgcolor=C["white"],
        font=dict(family="Outfit, sans-serif",
                  color=C["navy"], size=13),
        legend=dict(
            bgcolor=C["bg"],
            bordercolor=C["border"],
            borderwidth=1.5,
            font=dict(size=12, color=C["navy"]),
            orientation="h",
            yanchor="bottom", y=1.02,
            xanchor="right", x=1,
        ),
        xaxis=dict(
            gridcolor="#F1F5F9",
            linecolor=C["border"],
            tickfont=dict(color=C["slate"], size=12),
            title_font=dict(color=C["slate"], size=13),
        ),
        yaxis=dict(
            gridcolor="#F1F5F9",
            linecolor=C["border"],
            tickfont=dict(color=C["slate"], size=12),
            title_font=dict(color=C["slate"], size=13),
            zerolinecolor=C["border"],
        ),
        margin=dict(l=20, r=20, t=65, b=30),
        hoverlabel=dict(
            bgcolor=C["navy"],
            font_color=C["white"],
            font_size=13,
            bordercolor=C["navy"],
        ),
    )
    if yrange:
        layout["yaxis"]["range"] = yrange
    return layout

# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#005C2E,#007A3D);
                border-radius:14px; padding:1.25rem; margin-bottom:1rem;
                text-align:center;">
        <div style="font-size:2rem; margin-bottom:6px;">🇸🇦</div>
        <p style="color:#FFFFFF; font-size:15px; font-weight:800;
                   margin:0; letter-spacing:-0.3px;">V2030 Pulse</p>
        <p style="color:rgba(255,255,255,0.75); font-size:11px;
                   margin:3px 0 0; letter-spacing:0.5px;">
            نبض رؤية 2030
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-label">Audience View</p>',
                unsafe_allow_html=True)
    view_mode = st.radio(
        "Optimize Analytics For:",
        ["🏛️ Government Metrics",
         "💼 HR & Talent Acquisition",
         "👥 Public General Impact"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown('<p class="section-label">System Status</p>',
                unsafe_allow_html=True)
    st.success("✅  Data Pipeline: Stable")
    st.info("📅  Last Updated: May 2026")

    st.divider()

    st.markdown("""
    <div style="background:#F0FDF6; border:1.5px solid #BBF7D0;
                border-radius:12px; padding:1rem;">
        <p style="font-size:12px; font-weight:700; color:#005C2E;
                   margin:0 0 6px;">Built by</p>
        <p style="font-size:13px; font-weight:800; color:#0D1F2D;
                   margin:0;">Mohammad Zaid</p>
        <p style="font-size:11px; color:#5A7080; margin:3px 0 0;">
            Hafiz-e-Quran · Arabic C1<br>
            Google Gen AI APAC 2026<br>
            Jamia Hamdard University
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:12px;">
        <a href="https://github.com/zaidug987198" target="_blank"
           style="display:block; background:#0D1F2D; color:#FFFFFF;
                  text-decoration:none; border-radius:8px; padding:8px 12px;
                  font-size:12px; font-weight:600; text-align:center;
                  margin-bottom:6px;">
            🐙 GitHub Repository
        </a>
        <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/"
           target="_blank"
           style="display:block; background:#0A66C2; color:#FFFFFF;
                  text-decoration:none; border-radius:8px; padding:8px 12px;
                  font-size:12px; font-weight:600; text-align:center;">
            💼 LinkedIn Profile
        </a>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#005C2E 0%,#007A3D 55%,#00A651 100%);
            border-radius:18px; padding:1.75rem 2rem;
            margin-bottom:1.75rem;
            box-shadow:0 8px 32px rgba(0,92,46,0.22);">
    <div style="display:flex; align-items:center;
                justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div>
            <p style="color:rgba(255,255,255,0.7); font-size:11px;
                       font-weight:700; letter-spacing:2px; margin:0 0 4px;
                       text-transform:uppercase;">
                Saudi Arabia · رؤية 2030
            </p>
            <h1 style="color:#FFFFFF; margin:0; font-size:1.8rem;
                        font-weight:800; letter-spacing:-0.5px;
                        line-height:1.2;">
                Vision 2030 Intelligence Hub
            </h1>
            <p style="color:rgba(255,255,255,0.8); margin:6px 0 0;
                       font-size:13.5px; font-weight:400;">
                National Transformation &amp; Economic Intelligence Dashboard
                &nbsp;|&nbsp; نبض رؤية 2030
            </p>
        </div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <span style="background:rgba(255,255,255,0.18);
                          color:#FFFFFF; padding:5px 14px;
                          border-radius:20px; font-size:12px;
                          font-weight:600; border:1px solid
                          rgba(255,255,255,0.25);">
                📊 Live Analytics
            </span>
            <span style="background:rgba(255,255,255,0.18);
                          color:#FFFFFF; padding:5px 14px;
                          border-radius:20px; font-size:12px;
                          font-weight:600; border:1px solid
                          rgba(255,255,255,0.25);">
                🌍 Global Standards
            </span>
            <span style="background:rgba(240,192,64,0.3);
                          color:#FFDD80; padding:5px 14px;
                          border-radius:20px; font-size:12px;
                          font-weight:600; border:1px solid
                          rgba(240,192,64,0.4);">
                ⭐ Vision 2030 Aligned
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# KPI CARDS
# ══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Key Performance Indicators — 2024 Update</p>',
            unsafe_allow_html=True)

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Non-Oil GDP Share",    "50.2%",    "↑ 4.1%  Target ✅")
k2.metric("Digital Payments",     "79.0%",    "↑ 22.0%  SAMA Index")
k3.metric("Female Workforce",     "33.6%",    "↑ 8.2%  Historic Peak")
k4.metric("Tourism Revenue",      "SAR 134B", "↑ 38.0%  YoY")
k5.metric("AI Investment",        "$122.7B",  "↑ HUMAIN + Tech Deals")

st.divider()

# ══════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════
gdp_df = pd.DataFrame({
    "Year":          [2016,2017,2018,2019,2020,2021,2022,2023,2024],
    "Oil GDP %":     [43,  42,  44,  41,  35,  40,  46,  39,  37 ],
    "Non-Oil GDP %": [57,  58,  56,  59,  65,  60,  54,  61,  63 ],
})
tourism_df = pd.DataFrame({
    "Year":          [2019,2020,2021,2022,2023,2024],
    "Visitors (M)":  [100, 41,  63,  93,  106, 115 ],
    "Target 2030":   [150, 150, 150, 150, 150, 150 ],
})
sectors_df = pd.DataFrame({
    "Sector":                ["Tourism","Technology","Healthcare",
                              "Entertainment","Mining","Logistics"],
    "Investment (SAR B)":    [134, 89, 67, 45, 38, 29],
    "Growth %":              [38,  24, 19, 31, 15, 22],
    "Jobs Created (000s)":   [250, 180, 120, 95, 60, 75],
})
emp_df = pd.DataFrame({
    "Year":              [2016,2017,2018,2019,2020,2021,2022,2023,2024],
    "Female Emp %":      [17,  18,  20,  23,  25,  27,  30,  32,  34 ],
    "Target (30%)":      [30,  30,  30,  30,  30,  30,  30,  30,  30 ],
})
ai_df = pd.DataFrame({
    "Initiative":        ["HUMAIN (PIF)","Nvidia Deal","AWS Saudi",
                          "Google Cloud","Microsoft"],
    "Amount (USD B)":    [100.0, 14.9, 5.3, 1.0, 1.5],
    "Category":          ["Sovereign AI","AI Hardware","Cloud Infra",
                          "Cloud Infra","Cloud Infra"],
})
giga_df = pd.DataFrame({
    "Project":    ["NEOM","The Line","Qiddiya","Red Sea Project","ROSHN"],
    "Budget ($B)":[500,   200,       8,        28,                20   ],
    "Status":     ["In Progress","Construction","Phase 1",
                   "Open","Ongoing"],
    "Focus":      ["Smart City AI","Urban Living","Entertainment",
                   "Eco Tourism","Housing"],
})

# ══════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈  Economy",
    "✈️  Tourism",
    "🏭  Sectors & Projects",
    "👩‍💼  Employment",
    "🤖  AI & Technology",
])

# ─────────────────────── TAB 1 — ECONOMY ───────────────────────
with tab1:
    col_chart, col_info = st.columns([2.2, 1])

    with col_chart:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=gdp_df["Year"], y=gdp_df["Non-Oil GDP %"],
            name="Non-Oil GDP %",
            mode="lines+markers",
            line=dict(color=C["green_mid"], width=3.5),
            marker=dict(size=9, color=C["green_mid"],
                        line=dict(color=C["white"], width=2.5)),
            fill="tozeroy",
            fillcolor="rgba(0,122,61,0.09)",
            hovertemplate="<b>%{x}</b><br>Non-Oil GDP: %{y}%<extra></extra>",
        ))
        fig1.add_trace(go.Scatter(
            x=gdp_df["Year"], y=gdp_df["Oil GDP %"],
            name="Oil GDP %",
            mode="lines+markers",
            line=dict(color=C["gold_mid"], width=3,
                      dash="dot"),
            marker=dict(size=9, color=C["gold_mid"],
                        line=dict(color=C["white"], width=2.5)),
            hovertemplate="<b>%{x}</b><br>Oil GDP: %{y}%<extra></extra>",
        ))
        fig1.add_hline(
            y=50,
            line_dash="dash",
            line_color=C["red"],
            line_width=1.5,
            annotation_text="  Vision 2030 Target: 50% Non-Oil",
            annotation_font_color=C["red"],
            annotation_font_size=12,
        )
        fig1.update_layout(
            **chart_layout("Structural Diversification — Oil vs Non-Oil GDP (%)",
                           [30, 72])
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="insight-card">
            <h4>📊 Economic Insights</h4>
            <div class="insight-item">
                <div class="insight-dot" style="background:#005C2E;"></div>
                <p class="insight-text">
                    <b>Target Achieved:</b> Non-Oil GDP hit
                    <b style="color:#005C2E;">50.2%</b> in 2024 —
                    Vision 2030 milestone reached ahead of schedule.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#D4A017;"></div>
                <p class="insight-text">
                    <b>Nitaqat Program:</b> Localization compliance
                    driving domestic employment to historic lows in
                    unemployment — below 7%.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#2563EB;"></div>
                <p class="insight-text">
                    <b>FDI Surge:</b> Foreign Direct Investment
                    exceeded SAR 100B in 2024 across tech,
                    tourism, and energy sectors.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#DC2626;"></div>
                <p class="insight-text">
                    <b>HR Opportunity:</b> High-velocity hiring in
                    Cyber Security, Financial Analytics,
                    Cloud Engineering, and AI Development.
                </p>
            </div>
            <div style="background:#F0FDF6; border-radius:10px;
                        padding:10px 12px; margin-top:8px;
                        border:1px solid #BBF7D0;">
                <p style="margin:0; font-size:12px; font-weight:700;
                           color:#005C2E;">
                    ✅ Vision 2030 GDP Target: ACHIEVED
                </p>
                <div class="progress-bar-wrap">
                    <div style="background:linear-gradient(90deg,#005C2E,#00A651);
                                 height:10px; width:100%;
                                 border-radius:8px;"></div>
                </div>
                <p style="margin:0; font-size:11px; color:#5A7080;">
                    100.4% of target completed
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────── TAB 2 — TOURISM ───────────────────────
with tab2:
    col_chart, col_info = st.columns([2.2, 1])

    with col_chart:
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=tourism_df["Year"],
            y=tourism_df["Visitors (M)"],
            name="Actual Visitors (M)",
            marker=dict(
                color=[C["green_dark"], C["red"],
                        C["gold_mid"], C["green_mid"],
                        C["green_light"], C["green_dark"]],
                line=dict(color=C["white"], width=1.5)
            ),
            text=tourism_df["Visitors (M)"].astype(str) + "M",
            textposition="outside",
            textfont=dict(color=C["navy"], size=12.5,
                          family="Outfit"),
            hovertemplate="<b>%{x}</b><br>Visitors: %{y}M<extra></extra>",
        ))
        fig2.add_trace(go.Scatter(
            x=tourism_df["Year"],
            y=tourism_df["Target 2030"],
            name="Target 2030 (150M)",
            mode="lines",
            line=dict(color=C["red"], width=2.5, dash="dash"),
            hovertemplate="Target: %{y}M<extra></extra>",
        ))
        fig2.update_layout(
            **chart_layout("Tourism Performance vs Strategic 2030 Target",
                           [0, 180])
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col_info:
        pct = int((115/150)*100)
        st.markdown(f"""
        <div class="insight-card">
            <h4>✈️ Tourism Progress</h4>
            <div style="text-align:center; margin-bottom:1rem;">
                <p style="font-size:2.8rem; font-weight:800;
                           color:#005C2E; margin:0; line-height:1;">
                    76%
                </p>
                <p style="font-size:12px; color:#5A7080; margin:3px 0 0;">
                    of 150M target reached
                </p>
            </div>
            <div class="progress-bar-wrap">
                <div style="background:linear-gradient(90deg,#005C2E,#00A651);
                             height:10px; width:{pct}%;
                             border-radius:8px;"></div>
            </div>
            <div style="display:flex; justify-content:space-between;
                        font-size:11px; color:#5A7080; margin-bottom:1rem;">
                <span>0</span><span>2024: 115M</span><span>150M</span>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#005C2E;"></div>
                <p class="insight-text">
                    <b>SAR 134B</b> revenue in 2024,
                    up <b style="color:#005C2E;">38%</b> YoY.
                    On track for 150M visitors by 2030.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#2563EB;"></div>
                <p class="insight-text">
                    <b>250,000+</b> new tourism jobs
                    created, directly benefiting
                    Saudi nationals.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#D4A017;"></div>
                <p class="insight-text">
                    New mega-projects: Red Sea,
                    NEOM, Qiddiya driving premium
                    international visitor segments.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────── TAB 3 — SECTORS & PROJECTS ─────────────────
with tab3:
    col_pie, col_bar = st.columns(2)

    with col_pie:
        fig3a = px.pie(
            sectors_df,
            values="Investment (SAR B)",
            names="Sector",
            title="Investment Distribution by Sector (SAR B)",
            hole=0.42,
            color_discrete_sequence=[
                C["green_dark"], C["green_mid"],
                C["green_light"], C["gold_mid"],
                C["blue_mid"], "#8B5CF6"
            ],
        )
        fig3a.update_traces(
            textinfo="percent+label",
            textfont=dict(size=12.5, color=C["navy"],
                          family="Outfit"),
            hovertemplate="<b>%{label}</b><br>SAR %{value}B<br>%{percent}<extra></extra>",
        )
        fig3a.update_layout(**chart_layout(""))
        st.plotly_chart(fig3a, use_container_width=True)

    with col_bar:
        fig3b = px.bar(
            sectors_df.sort_values("Growth %", ascending=True),
            x="Growth %",
            y="Sector",
            orientation="h",
            title="YoY Growth Rate by Sector (%)",
            color="Growth %",
            color_continuous_scale=["#A7F3D0", "#007A3D", "#005C2E"],
            text="Growth %",
        )
        fig3b.update_traces(
            texttemplate="%{text}%",
            textposition="outside",
            textfont=dict(color=C["navy"], size=12.5,
                          family="Outfit"),
        )
        fig3b.update_layout(
            **chart_layout(""),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig3b, use_container_width=True)

    st.markdown('<p class="section-label" style="margin-top:1rem;">Giga-Projects Status Tracker</p>',
                unsafe_allow_html=True)

    cols = st.columns(len(giga_df))
    colors_proj = [C["green_dark"], C["green_mid"],
                   C["gold_mid"], C["blue_mid"], C["green_light"]]
    for i, row in giga_df.iterrows():
        with cols[i]:
            st.markdown(f"""
            <div style="background:#FFFFFF; border:1.5px solid #E8EDF5;
                        border-radius:14px; padding:1rem;
                        border-top:4px solid {colors_proj[i]};
                        box-shadow:0 2px 10px rgba(0,0,0,0.05);
                        text-align:center; height:100%;">
                <p style="font-size:14px; font-weight:800;
                           color:{colors_proj[i]}; margin:0 0 4px;">
                    {row['Project']}
                </p>
                <p style="font-size:11px; color:#5A7080;
                           margin:0 0 8px; font-weight:500;">
                    {row['Focus']}
                </p>
                <p style="font-size:1.3rem; font-weight:800;
                           color:#0D1F2D; margin:0 0 4px;">
                    ${row['Budget ($B)']}B
                </p>
                <span style="background:{colors_proj[i]}22;
                              color:{colors_proj[i]};
                              font-size:10px; font-weight:700;
                              padding:2px 8px; border-radius:12px;">
                    {row['Status']}
                </span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:1rem;">
    <table style="width:100%; border-collapse:collapse;
                  font-family:Outfit,sans-serif; font-size:13px;
                  background:#FFFFFF; border-radius:12px;
                  overflow:hidden; border:1.5px solid #E8EDF5;">
        <thead>
            <tr style="background:linear-gradient(135deg,#005C2E,#007A3D);">
                <th style="padding:12px 16px; color:#FFFFFF;
                            text-align:left; font-weight:700;">Sector</th>
                <th style="padding:12px 16px; color:#FFFFFF;
                            text-align:right; font-weight:700;">
                    Investment (SAR B)</th>
                <th style="padding:12px 16px; color:#FFFFFF;
                            text-align:right; font-weight:700;">
                    Growth %</th>
                <th style="padding:12px 16px; color:#FFFFFF;
                            text-align:right; font-weight:700;">
                    Jobs Created (000s)</th>
            </tr>
        </thead>
        <tbody>
    """ + "".join([f"""
            <tr style="border-bottom:1px solid #E8EDF5;
                        {'background:#F7F9FC' if i%2==0 else 'background:#FFFFFF'}">
                <td style="padding:11px 16px; color:#0D1F2D;
                            font-weight:600;">{row['Sector']}</td>
                <td style="padding:11px 16px; color:#0D1F2D;
                            text-align:right; font-weight:700;">
                    SAR {row['Investment (SAR B)']}B</td>
                <td style="padding:11px 16px; text-align:right;">
                    <span style="background:#E6F7EE; color:#005C2E;
                                  font-weight:700; padding:3px 10px;
                                  border-radius:12px; font-size:12px;">
                        ↑ {row['Growth %']}%
                    </span>
                </td>
                <td style="padding:11px 16px; color:#5A7080;
                            text-align:right; font-weight:500;">
                    {row['Jobs Created (000s)']}K+</td>
            </tr>
    """ for i, (_, row) in enumerate(sectors_df.iterrows())]) + """
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────── TAB 4 — EMPLOYMENT ───────────────────────
with tab4:
    col_chart, col_info = st.columns([2.2, 1])

    with col_chart:
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=emp_df["Year"], y=emp_df["Female Emp %"],
            name="Female Employment %",
            mode="lines+markers",
            line=dict(color=C["green_mid"], width=3.5),
            marker=dict(size=10, color=C["green_mid"],
                        line=dict(color=C["white"], width=2.5)),
            fill="tozeroy",
            fillcolor="rgba(0,122,61,0.08)",
            hovertemplate="<b>%{x}</b><br>Female Emp: %{y}%<extra></extra>",
        ))
        fig4.add_trace(go.Scatter(
            x=emp_df["Year"], y=emp_df["Target (30%)"],
            name="Vision 2030 Target (30%)",
            mode="lines",
            line=dict(color=C["red"], width=2,
                      dash="dash"),
            hovertemplate="Target: %{y}%<extra></extra>",
        ))
        fig4.add_annotation(
            x=2024, y=34,
            text="<b>33.6% — Target Exceeded! ✅</b>",
            showarrow=True, arrowhead=2,
            arrowcolor=C["green_dark"],
            arrowwidth=2,
            font=dict(color=C["green_dark"], size=12),
            bgcolor=C["green_pale"],
            bordercolor=C["green_mid"],
            borderwidth=1.5,
        )
        fig4.update_layout(
            **chart_layout("Female Workforce Participation (%) — Vision 2030 Progress",
                           [12, 42])
        )
        st.plotly_chart(fig4, use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="insight-card">
            <h4>👩‍💼 Employment Highlights</h4>
            <div style="background:#F0FDF6; border-radius:12px;
                        padding:1rem; margin-bottom:10px;
                        border:1.5px solid #BBF7D0; text-align:center;">
                <p style="font-size:2.2rem; font-weight:800;
                           color:#005C2E; margin:0;">33.6%</p>
                <p style="font-size:12px; color:#5A7080; margin:3px 0 0;">
                    Female Workforce 2024<br>
                    <b style="color:#005C2E;">Target 30% — Exceeded ✅</b>
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#005C2E;"></div>
                <p class="insight-text">
                    From <b>17%</b> in 2016 to <b>33.6%</b> in 2024 —
                    nearly <b style="color:#005C2E;">doubled</b> in 8 years.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#D4A017;"></div>
                <p class="insight-text">
                    <b>Nitaqat Saudization:</b> Mandatory localization
                    quotas across all industries driving Saudi national
                    employment.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#2563EB;"></div>
                <p class="insight-text">
                    <b>Unemployment:</b> National rate dropped below
                    7% — lowest in Kingdom's history.
                </p>
            </div>
            <div class="insight-item">
                <div class="insight-dot" style="background:#8B5CF6;"></div>
                <p class="insight-text">
                    <b>HR Opportunity:</b> Bilingual Arabic-English
                    tech talent is the #1 demand across Vision 2030
                    companies.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────── TAB 5 — AI & TECH ───────────────────────
with tab5:
    col_chart, col_info = st.columns([2.2, 1])

    with col_chart:
        fig5 = go.Figure()
        bar_colors = [C["green_dark"], C["gold_mid"],
                      C["blue_mid"], C["blue_light"], "#8B5CF6"]
        fig5.add_trace(go.Bar(
            x=ai_df["Initiative"],
            y=ai_df["Amount (USD B)"],
            name="Investment",
            marker=dict(
                color=bar_colors,
                line=dict(color=C["white"], width=2)
            ),
            text=["$" + str(v) + "B" for v in ai_df["Amount (USD B)"]],
            textposition="outside",
            textfont=dict(color=C["navy"], size=13,
                          family="Outfit"),
            hovertemplate="<b>%{x}</b><br>$%{y}B<extra></extra>",
        ))
        fig5.update_layout(
            **chart_layout("Saudi Arabia AI & Cloud Investment (USD Billions) — 2025",
                           [0, 118]),
            showlegend=False,
        )
        st.plotly_chart(fig5, use_container_width=True)

    with col_info:
        st.markdown("""
        <div class="insight-card">
            <h4>🤖 AI & Tech Highlights</h4>
            <div style="background:#F0FDF6; border-radius:10px;
                        padding:10px 12px; margin-bottom:8px;
                        border-left:4px solid #005C2E;">
                <p style="margin:0; font-size:13px; font-weight:700;
                           color:#005C2E;">HUMAIN — $100B</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    PIF-backed sovereign AI company.<br>
                    Partners: Nvidia, AMD, AWS, Google
                </p>
            </div>
            <div style="background:#FFFBEB; border-radius:10px;
                        padding:10px 12px; margin-bottom:8px;
                        border-left:4px solid #D4A017;">
                <p style="margin:0; font-size:13px; font-weight:700;
                           color:#B8860B;">Nvidia Deal — $14.9B</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    Largest-ever GPU deal globally.<br>
                    18,000+ Blackwell AI chips
                </p>
            </div>
            <div style="background:#EFF6FF; border-radius:10px;
                        padding:10px 12px; margin-bottom:8px;
                        border-left:4px solid #2563EB;">
                <p style="margin:0; font-size:13px; font-weight:700;
                           color:#1E40AF;">AWS + Google + Microsoft</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    $7.8B combined cloud infrastructure<br>
                    in Saudi Arabia
                </p>
            </div>
            <div style="background:#F5F3FF; border-radius:10px;
                        padding:10px 12px; margin-bottom:8px;
                        border-left:4px solid #8B5CF6;">
                <p style="margin:0; font-size:13px; font-weight:700;
                           color:#6D28D9;">Startups: $1.72B</p>
                <p style="margin:0; font-size:12px; color:#5A7080;">
                    145% YoY growth in VC funding.<br>
                    AI + Fintech leading sectors
                </p>
            </div>
            <div style="background:linear-gradient(135deg,#005C2E,#007A3D);
                        border-radius:10px; padding:10px 12px;
                        margin-top:4px; text-align:center;">
                <p style="color:#FFFFFF; margin:0; font-size:12px;
                           font-weight:600;">
                    🤖 An-Nasir AI — Built for this market
                </p>
                <p style="color:rgba(255,255,255,0.75); margin:3px 0 0;
                           font-size:11px;">
                    Arabic-English AI Agent · Vertex AI + ADK
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.divider()
st.markdown("""
<div style="background:#FFFFFF; border:1.5px solid #E8EDF5;
            border-radius:16px; padding:1.25rem 1.75rem;
            display:flex; justify-content:space-between;
            align-items:center; flex-wrap:wrap; gap:14px;
            box-shadow:0 2px 10px rgba(0,0,0,0.04);">
    <div>
        <p style="margin:0; font-size:14px; font-weight:800;
                   color:#0D1F2D;">
            🇸🇦 V2030 Intelligence Hub
        </p>
        <p style="margin:3px 0 0; font-size:12px; color:#5A7080;">
            Data sources: open.data.gov.sa · vision2030.gov.sa ·
            GASTAT · SDAIA · World Bank
        </p>
    </div>
    <div style="text-align:right;">
        <p style="margin:0; font-size:13px; font-weight:700;
                   color:#005C2E;">
            Engineered by Mohammad Zaid
        </p>
        <p style="margin:3px 0 0; font-size:12px; color:#5A7080;">
            Hafiz-e-Quran · Arabic C1 · Google Gen AI APAC 2026 ·
            Jamia Hamdard
        </p>
    </div>
</div>
<p style="text-align:center; font-size:11px; color:#94A3B8;
           margin-top:12px;">
    © 2026 Mohammad Zaid | Built with Python · Streamlit · Plotly |
    All data sourced from official Saudi government portals
</p>
""", unsafe_allow_html=True)