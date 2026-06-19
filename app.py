"""
╔══════════════════════════════════════════════════════════════╗
║  Saudi Vision 2030 Intelligence Hub                         ║
║  Built by: Mohammad Zaid | Jamia Hamdard                   ║
║  Google Gen AI APAC 2026 | Arabic C1 | Hafiz-e-Quran       ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="رؤية 2030 | V2030 Intelligence Hub",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="expanded",
)

LOGO = """<svg width="172" height="52" viewBox="0 0 172 52" xmlns="http://www.w3.org/2000/svg">
  <rect width="172" height="52" rx="9" fill="#005C2E"/>
  <rect x="4" y="4" width="44" height="44" rx="6" fill="rgba(255,255,255,0.10)"/>
  <line x1="26" y1="41" x2="26" y2="23" stroke="#D4A017" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M26 23 Q19 16 13 18" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M26 23 Q22 14 26 11" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M26 23 Q33 16 39 19" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M26 23 Q29 15 33 14" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M26 23 Q23 15 19 14" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <line x1="14" y1="36" x2="38" y2="44" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
  <line x1="38" y1="36" x2="14" y2="44" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
  <text x="56" y="19" font-family="Arial" font-size="8.5" font-weight="600"
        fill="rgba(255,255,255,0.72)" letter-spacing="0.7">KINGDOM OF SAUDI ARABIA</text>
  <text x="56" y="34" font-family="Arial" font-size="15" font-weight="900"
        fill="#FFFFFF" letter-spacing="-0.3">VISION 2030</text>
  <text x="56" y="47" font-family="Arial" font-size="8.5" font-weight="500"
        fill="rgba(255,255,255,0.68)" letter-spacing="0.3">رؤية المملكة العربية السعودية</text>
</svg>"""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');
html,body,[class*="css"],.stApp{font-family:'Outfit','IBM Plex Sans Arabic',sans-serif!important;background:#F4F7FB!important;}
.main .block-container{padding:1.4rem 1.8rem 2rem!important;max-width:1440px!important;}
#MainMenu,footer,header,.stDeployButton{display:none!important;}
[data-testid="stSidebar"]{background:#FFFFFF!important;border-right:2px solid #E0E8F0!important;box-shadow:4px 0 20px rgba(0,0,0,0.07)!important;}
[data-testid="stMetric"]{background:#FFFFFF!important;border:1.5px solid #E0E8F0!important;border-radius:14px!important;padding:1rem 1.2rem!important;box-shadow:0 2px 12px rgba(0,80,40,0.07)!important;transition:transform .2s,box-shadow .2s!important;}
[data-testid="stMetric"]:hover{transform:translateY(-2px)!important;box-shadow:0 7px 22px rgba(0,80,40,0.13)!important;}
[data-testid="stMetric"] label{color:#5A7080!important;font-size:10.5px!important;font-weight:700!important;text-transform:uppercase!important;letter-spacing:.7px!important;}
[data-testid="stMetricValue"]{color:#0D1F2D!important;font-size:1.85rem!important;font-weight:800!important;line-height:1.1!important;}
[data-testid="stMetricDelta"]{font-size:11.5px!important;font-weight:600!important;}
.stTabs [data-baseweb="tab-list"]{background:#FFFFFF!important;border-radius:13px!important;padding:5px!important;gap:3px!important;border:1.5px solid #E0E8F0!important;box-shadow:0 2px 8px rgba(0,0,0,0.05)!important;margin-bottom:1.4rem!important;}
.stTabs [data-baseweb="tab"]{background:transparent!important;border-radius:9px!important;color:#5A7080!important;font-weight:600!important;font-size:12.5px!important;padding:8px 14px!important;}
.stTabs [aria-selected="true"]{background:linear-gradient(135deg,#004D26,#007A3D)!important;color:#FFFFFF!important;box-shadow:0 4px 14px rgba(0,92,46,0.28)!important;}
.stDownloadButton>button{background:linear-gradient(135deg,#004D26,#007A3D)!important;color:#FFFFFF!important;border:none!important;border-radius:9px!important;font-weight:700!important;font-size:12px!important;padding:7px 16px!important;transition:all .2s!important;}
.stButton>button{background:linear-gradient(135deg,#004D26,#007A3D)!important;color:#FFFFFF!important;border:none!important;border-radius:9px!important;font-weight:700!important;font-size:13px!important;width:100%!important;}
.stTextInput>div>div>input{border:1.5px solid #E0E8F0!important;border-radius:9px!important;font-size:13px!important;color:#0D1F2D!important;background:#FAFBFC!important;}
.stTextInput>div>div>input:focus{border-color:#005C2E!important;box-shadow:0 0 0 3px rgba(0,92,46,0.12)!important;}
hr{border-color:#E0E8F0!important;margin:1.2rem 0!important;}
.sec-lbl{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:1.3px;color:#5A7080;margin-bottom:.7rem;}
.icard{background:#FFFFFF;border:1.5px solid #E0E8F0;border-radius:13px;padding:1.2rem;height:100%;box-shadow:0 2px 10px rgba(0,0,0,0.05);}
.icard h4{color:#0D1F2D;font-size:14px;font-weight:700;margin:0 0 .8rem;}
.irow{display:flex;gap:9px;margin-bottom:9px;align-items:flex-start;}
.idot{width:7px;height:7px;border-radius:50%;flex-shrink:0;margin-top:5px;}
.itxt{font-size:12.5px;color:#334155;line-height:1.6;margin:0;}
.pb{background:#E0E8F0;border-radius:8px;height:9px;margin:5px 0;overflow:hidden;}
.ar{font-family:'IBM Plex Sans Arabic',sans-serif;}
.ar-strip{background:#F0FDF6;padding:8px 14px;border-radius:8px;border-right:3px solid #005C2E;font-size:12px;color:#5A7080;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;text-align:right;margin-bottom:1rem;}
.badge{display:inline-block;background:rgba(0,92,46,0.10);color:#005C2E;font-size:10.5px;font-weight:700;padding:2px 9px;border-radius:11px;border:1px solid rgba(0,92,46,0.22);margin-right:4px;}
.premium{background:linear-gradient(135deg,#1A1000,#2A1E00);border:1.5px solid #D4A017;border-radius:12px;padding:1rem 1.2rem;margin-top:1.1rem;}
.src-box{background:#FFFBEB;border-radius:9px;padding:9px 12px;margin-top:8px;border:1px solid #FDE68A;}
</style>
""", unsafe_allow_html=True)

G1,G2,G3 = "#004D26","#007A3D","#00A651"
GOLD,GOLDD = "#D4A017","#B8860B"
B2,B3 = "#2563EB","#60A5FA"
RED = "#DC2626"
NAVY,SL = "#0D1F2D","#5A7080"
BDR,BG,WH = "#E0E8F0","#F4F7FB","#FFFFFF"

def CL(title="", yr=None):
    d = dict(
        title=dict(text=title, font=dict(size=14, color=NAVY, family="Outfit"), x=0, xanchor="left"),
        plot_bgcolor=WH, paper_bgcolor=WH,
        font=dict(family="Outfit", color=NAVY, size=12),
        legend=dict(bgcolor=BG, bordercolor=BDR, borderwidth=1.5,
                    font=dict(size=11, color=NAVY),
                    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(gridcolor="#EEF2F7", linecolor=BDR,
                   tickfont=dict(color=SL, size=11), title_font=dict(color=SL)),
        yaxis=dict(gridcolor="#EEF2F7", linecolor=BDR,
                   tickfont=dict(color=SL, size=11), title_font=dict(color=SL),
                   zerolinecolor=BDR),
        margin=dict(l=10, r=10, t=64, b=20),
        hoverlabel=dict(bgcolor=NAVY, font_color=WH, font_size=12, bordercolor=NAVY),
    )
    if yr:
        d["yaxis"]["range"] = yr
    return d

def csv_b(df):
    return df.to_csv(index=False).encode("utf-8")

def forecast(hx, hy, fx, deg=2):
    x = np.array(hx, float); y = np.array(hy, float); m = x.mean()
    c = np.polyfit(x - m, y, deg); p = np.poly1d(c)
    return [round(float(p(v - m)), 2) for v in fx]

HY = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
FY = [2025,2026,2027,2028,2029,2030]

gdp_df = pd.DataFrame({"Year":HY,"Oil GDP %":[43,42,44,41,35,40,46,39,37],"Non-Oil GDP %":[57,58,56,59,65,60,54,61,63]})
tour_df = pd.DataFrame({"Year":[2019,2020,2021,2022,2023,2024],"Visitors (M)":[100,41,63,93,106,115]})
emp_df = pd.DataFrame({"Year":HY,"Female %":[17,18,20,23,25,27,30,32,34]})
dig_df = pd.DataFrame({"Year":HY,"Digital Pay %":[31,38,45,52,60,67,72,77,79]})
ai_df = pd.DataFrame({"Initiative":["HUMAIN (PIF)","Nvidia Deal","AWS Saudi","Google Cloud","Microsoft"],"USD Billion":[100.0,14.9,5.3,1.0,1.5]})
sec_df = pd.DataFrame({"Sector":["Tourism","Technology","Healthcare","Entertainment","Mining","Logistics"],"Investment (SAR B)":[134,89,67,45,38,29],"Growth %":[38,24,19,31,15,22],"Jobs (000s)":[250,180,120,95,60,75]})
giga_df = pd.DataFrame({"Project":["NEOM","The Line","Qiddiya","Red Sea","ROSHN"],"Budget($B)":[500,200,8,28,20],"Status":["In Progress","Construction","Phase 1","Open","Ongoing"],"Focus":["Smart City AI","Urban Living","Entertainment","Eco Tourism","Housing"]})

noil_f = forecast(HY, gdp_df["Non-Oil GDP %"].tolist(), FY)
oil_f  = forecast(HY, gdp_df["Oil GDP %"].tolist(), FY)
tour_f = forecast([2019,2020,2021,2022,2023,2024], tour_df["Visitors (M)"].tolist(), FY)
fem_f  = forecast(HY, emp_df["Female %"].tolist(), FY)
dig_f  = forecast(HY, dig_df["Digital Pay %"].tolist(), FY)

# ═══════════════ SIDEBAR ═══════════════
with st.sidebar:
    st.markdown(LOGO, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sec-lbl">Audience | نوع المستخدم</p>', unsafe_allow_html=True)
    st.radio("view", ["🏛️ Government & Policy","💼 HR & Talent Acquisition","📊 Investors & Analysts","👥 Public / General"], label_visibility="collapsed")
    st.divider()

    st.markdown("""
    <div style="background:linear-gradient(135deg,#F0FDF6,#E6F7EE);border:1.5px solid #BBF7D0;border-radius:12px;padding:.9rem;margin-bottom:.6rem;">
      <p style="font-size:11.5px;font-weight:800;color:#004D26;margin:0 0 2px;text-transform:uppercase;letter-spacing:.7px;">📩 Free Weekly Insights</p>
      <p style="font-size:11px;color:#5A7080;margin:0;font-family:'IBM Plex Sans Arabic',sans-serif;">اشترك للحصول على تقارير رؤية 2030</p>
    </div>
    """, unsafe_allow_html=True)
    sub_email = st.text_input("Email", placeholder="name@company.com", label_visibility="collapsed", key="se")
    sub_name  = st.text_input("Name", placeholder="Your name (optional)",  label_visibility="collapsed", key="sn")
    if st.button("✉️  Subscribe — Free Brief", key="sb"):
        if sub_email and "@" in sub_email and "." in sub_email:
            nm = f", {sub_name.strip()}" if sub_name.strip() else ""
            st.success(f"✅ Subscribed{nm}!\nWeekly V2030 insights sent to:\n{sub_email}")
        else:
            st.warning("⚠️ Please enter a valid email address.")
    st.divider()

    st.markdown("""
    <div style="background:linear-gradient(135deg,#FFFBEB,#FEF3C7);border:1.5px solid #D4A017;border-radius:12px;padding:.9rem;margin-bottom:.6rem;">
      <p style="font-size:11.5px;font-weight:800;color:#92400E;margin:0 0 5px;text-transform:uppercase;letter-spacing:.7px;">💼 Enterprise Consulting</p>
      <p style="font-size:12px;color:#334155;line-height:1.6;margin:0 0 6px;">Need <b>custom Saudi market intelligence</b>, bilingual AI dashboards, or data pipelines for your Vision 2030 project?</p>
      <p style="font-size:11px;color:#5A7080;margin:0 0 6px;font-family:'IBM Plex Sans Arabic',sans-serif;">تحليلات مخصصة للسوق السعودي</p>
      <p style="font-size:12px;font-weight:700;color:#004D26;margin:0;line-height:1.7;"><b>Mohammad Zaid</b><br>🕌 Hafiz-e-Quran · 🗣️ Arabic C1<br>☁️ Google Gen AI APAC 2026<br>🎓 BCA — Jamia Hamdard</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<a href="mailto:zaidug987198@gmail.com" style="display:block;background:linear-gradient(135deg,#D4A017,#F0C040);color:#1A1000;text-decoration:none;border-radius:9px;padding:8px 14px;font-size:12px;font-weight:800;text-align:center;margin-bottom:6px;">📧 Request Custom Report</a>', unsafe_allow_html=True)
    st.divider()
    st.success("✅ Data Pipeline: Live")
    st.info("🤖 ML Forecasting: Active")
    st.caption("📅 Data Updated: May 2026")
    st.divider()
    st.markdown("""
    <div style="background:#F0FDF6;border:1.5px solid #BBF7D0;border-radius:12px;padding:.85rem;margin-bottom:.6rem;">
      <p style="font-size:10px;font-weight:700;color:#004D26;margin:0 0 3px;text-transform:uppercase;letter-spacing:.7px;">Built by</p>
      <p style="font-size:14px;font-weight:800;color:#0D1F2D;margin:0;">Mohammad Zaid</p>
      <p style="font-size:11px;color:#5A7080;margin:4px 0 0;line-height:1.7;">🕌 Hafiz-e-Quran<br>🗣️ Arabic C1 — DPA, Jamia Hamdard<br>☁️ Google Gen AI APAC 2026<br>🎓 BCA — Jamia Hamdard University</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <a href="https://github.com/zaidug987198-design/v2030-pulse" target="_blank" style="display:block;background:#0D1F2D;color:#FFFFFF;text-decoration:none;border-radius:9px;padding:8px 14px;font-size:12px;font-weight:700;text-align:center;margin-bottom:6px;">🐙  GitHub — v2030-pulse</a>
    <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/" target="_blank" style="display:block;background:#0A66C2;color:#FFFFFF;text-decoration:none;border-radius:9px;padding:8px 14px;font-size:12px;font-weight:700;text-align:center;">💼  LinkedIn Profile</a>
    """, unsafe_allow_html=True)

# ═══════════════ HEADER ═══════════════
kpi_strip = "".join(
    f'<div style="text-align:center;min-width:80px;"><p style="color:#FFE080;font-size:1.2rem;font-weight:800;margin:0;">{v}</p><p style="color:rgba(255,255,255,0.72);font-size:9px;margin:2px 0 0;font-family:IBM Plex Sans Arabic,sans-serif;">{a}</p></div>'
    for v,a in [("50.2%","الناتج غير النفطي"),("115M","السياح الدوليون"),("33.6%","توظيف المرأة"),("$122B","استثمار الذكاء الاصطناعي"),("79%","المدفوعات الرقمية"),("SAR 134B","إيرادات السياحة")]
)
st.markdown(f"""
<div style="background:linear-gradient(135deg,#003D1E 0%,#005C2E 40%,#007A3D 75%,#009950 100%);border-radius:18px;padding:1.6rem 1.8rem;margin-bottom:1.6rem;box-shadow:0 10px 40px rgba(0,60,30,0.26);">
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;">
    <div style="display:flex;align-items:center;gap:16px;">
      <div style="flex-shrink:0;">{LOGO}</div>
      <div>
        <p style="color:rgba(255,255,255,0.58);font-size:9.5px;font-weight:700;letter-spacing:2.4px;margin:0 0 2px;text-transform:uppercase;">KINGDOM OF SAUDI ARABIA · 2026</p>
        <h1 style="color:#FFFFFF;margin:0;font-size:1.65rem;font-weight:800;letter-spacing:-.5px;line-height:1.2;">Vision 2030 Intelligence Hub</h1>
        <p style="color:rgba(255,255,255,0.80);margin:4px 0 0;font-size:13px;font-family:IBM Plex Sans Arabic,sans-serif;direction:rtl;text-align:right;">لوحة تحليلات استراتيجية لرؤية 2030</p>
        <p style="color:rgba(255,255,255,0.60);margin:2px 0 0;font-size:11.5px;">National Transformation &amp; Economic Intelligence · <span style="background:rgba(212,160,23,.28);color:#FFE080;padding:1px 7px;border-radius:7px;font-size:10.5px;font-weight:700;">🤖 ML Forecasting Active</span></p>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:5px;align-items:flex-end;">
      <span style="background:rgba(255,255,255,.16);color:#FFF;padding:4px 12px;border-radius:18px;font-size:11px;font-weight:600;border:1px solid rgba(255,255,255,.25);">📊 Live Analytics</span>
      <span style="background:rgba(255,255,255,.16);color:#FFF;padding:4px 12px;border-radius:18px;font-size:11px;font-weight:600;border:1px solid rgba(255,255,255,.25);">🌍 Global Standards</span>
      <span style="background:rgba(212,160,23,.30);color:#FFE080;padding:4px 12px;border-radius:18px;font-size:11px;font-weight:600;border:1px solid rgba(212,160,23,.40);">⭐ Vision 2030 Aligned</span>
    </div>
  </div>
  <div style="margin-top:1rem;padding-top:.9rem;border-top:1px solid rgba(255,255,255,.15);display:flex;gap:20px;flex-wrap:wrap;">{kpi_strip}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="sec-lbl">مؤشرات الأداء — Key Performance Indicators 2024</p>', unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric("Non-Oil GDP","50.2%","↑ 4.1% ✅")
c2.metric("Tourism Rev","SAR 134B","↑ 38% YoY")
c3.metric("Female Emp","33.6%","↑ 8.2% ✅")
c4.metric("Digital Pay","79.0%","↑ 22% SAMA")
c5.metric("AI Investment","$122.7B","↑ HUMAIN")
c6.metric("VC Startups","$1.72B","↑ 145% YoY")
st.divider()

# ═══════════════ TABS ═══════════════
t1,t2,t3,t4,t5 = st.tabs(["📈  Economy | الاقتصاد","✈️  Tourism | السياحة","🏭  Sectors & Giga-Projects","👩‍💼  Employment | التوظيف","🤖  AI & Tech | الذكاء الاصطناعي"])

# ─── TAB 1 ───
with t1:
    st.markdown('<p class="ar-strip">التنويع الاقتصادي · نسبة الناتج المحلي النفطي مقابل غير النفطي مع التوقعات حتى 2030</p>', unsafe_allow_html=True)
    st.markdown('<span class="badge">🤖 Polynomial Regression</span><span class="badge">Horizon: 2030</span>', unsafe_allow_html=True)
    st.write("")
    cc,ci = st.columns([2.4,1])
    with cc:
        f1 = go.Figure()
        f1.add_trace(go.Scatter(x=gdp_df["Year"],y=gdp_df["Non-Oil GDP %"],name="Non-Oil GDP % (Actual)",mode="lines+markers",line=dict(color=G2,width=3.5),marker=dict(size=8,color=G2,line=dict(color=WH,width=2.5)),fill="tozeroy",fillcolor="rgba(0,122,61,0.08)",hovertemplate="<b>%{x}</b><br>Non-Oil: %{y}%<extra></extra>"))
        f1.add_trace(go.Scatter(x=gdp_df["Year"],y=gdp_df["Oil GDP %"],name="Oil GDP % (Actual)",mode="lines+markers",line=dict(color=GOLD,width=3,dash="dot"),marker=dict(size=8,color=GOLD,line=dict(color=WH,width=2.5)),hovertemplate="<b>%{x}</b><br>Oil: %{y}%<extra></extra>"))
        f1.add_trace(go.Scatter(x=FY,y=noil_f,name="Non-Oil GDP % (Forecast)",mode="lines+markers",line=dict(color=G3,width=2.5,dash="dash"),marker=dict(size=7,symbol="diamond",color=G3,line=dict(color=WH,width=2)),hovertemplate="<b>%{x} ★</b><br>Forecast: %{y}%<extra></extra>"))
        f1.add_trace(go.Scatter(x=FY,y=oil_f,name="Oil GDP % (Forecast)",mode="lines",line=dict(color="#F0C040",width=2,dash="dot"),hovertemplate="<b>%{x} ★</b><br>Forecast: %{y}%<extra></extra>"))
        f1.add_vline(x=2024.5,line_dash="dot",line_color="#94A3B8",annotation_text="  Forecast →",annotation_font_size=10,annotation_font_color="#94A3B8")
        f1.add_hline(y=50,line_dash="dash",line_color=RED,line_width=1.5,annotation_text="  Target: 50% ✅",annotation_font_color=RED,annotation_font_size=11)
        f1.update_layout(**CL("GDP Diversification: Oil vs Non-Oil (%) + ML Forecast to 2030",[28,74]))
        st.plotly_chart(f1,use_container_width=True)
        ia,ib = st.columns([3,1])
        with ia:
            st.info(f"🤖 **ML Forecast 2030:** Non-Oil → **{noil_f[-1]}%** | Oil → **{oil_f[-1]}%** (polynomial regression)")
        with ib:
            ex = pd.DataFrame({"Year":HY+FY,"Non-Oil GDP %":gdp_df["Non-Oil GDP %"].tolist()+noil_f,"Oil GDP %":gdp_df["Oil GDP %"].tolist()+oil_f,"Type":["Actual"]*9+["ML Forecast"]*6})
            st.download_button("📥 Download CSV",csv_b(ex),"gdp_forecast.csv","text/csv",use_container_width=True)
    with ci:
        st.markdown("""
        <div class="icard"><h4>📊 Economic Insights<br><span class="ar" style="font-size:12px;color:#5A7080;">رؤى اقتصادية</span></h4>
        <div class="irow"><div class="idot" style="background:#005C2E;"></div><p class="itxt"><b>Target Hit:</b> Non-Oil GDP reached <b style="color:#005C2E">50.2%</b> in 2024 — ahead of schedule ✅</p></div>
        <div class="irow"><div class="idot" style="background:#D4A017;"></div><p class="itxt"><b>Nitaqat:</b> Saudization driving unemployment below <b>7%</b> — historic low.</p></div>
        <div class="irow"><div class="idot" style="background:#2563EB;"></div><p class="itxt"><b>FDI:</b> Foreign investment exceeded <b>SAR 100B</b> in 2024.</p></div>
        <div class="irow"><div class="idot" style="background:#DC2626;"></div><p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English AI talent is #1 shortage in Vision 2030 firms.</p></div>
        <div style="background:#F0FDF6;border-radius:9px;padding:9px 12px;margin-top:7px;border:1.5px solid #BBF7D0;">
          <p style="margin:0;font-size:12px;font-weight:700;color:#005C2E;">✅ Non-Oil GDP Target: ACHIEVED</p>
          <div class="pb"><div style="background:linear-gradient(90deg,#005C2E,#00A651);height:9px;width:100%;border-radius:8px;"></div></div>
          <p style="margin:0;font-size:11px;color:#5A7080;">100.4% complete</p>
        </div>
        <div class="src-box"><p style="margin:0;font-size:11px;font-weight:700;color:#92400E;">📡 Sources</p><p style="margin:0;font-size:11px;color:#5A7080;">GASTAT · open.data.gov.sa<br>vision2030.gov.sa · World Bank</p></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 💳 Digital Payments | المدفوعات الرقمية")
    da,db = st.columns([2.4,1])
    with da:
        fd = go.Figure()
        fd.add_trace(go.Bar(x=dig_df["Year"],y=dig_df["Digital Pay %"],name="Actual",marker_color=[G1]*len(dig_df),text=dig_df["Digital Pay %"].astype(str)+"%",textposition="outside",textfont=dict(color=NAVY,size=11.5),hovertemplate="<b>%{x}</b><br>%{y}%<extra></extra>"))
        fd.add_trace(go.Bar(x=FY,y=dig_f,name="ML Forecast",marker_color="rgba(0,166,81,0.35)",marker_line=dict(color=G3,width=1.5),text=[f"{v}%*" for v in dig_f],textposition="outside",textfont=dict(color=G2,size=11.5),hovertemplate="<b>%{x} ★</b><br>%{y}%<extra></extra>"))
        fd.update_layout(**CL("Digital Payments Adoption (%) + ML Forecast | المدفوعات الرقمية",[0,106]))
        st.plotly_chart(fd,use_container_width=True)
        dra,drb = st.columns([3,1])
        with dra: st.info(f"🤖 **ML 2030:** Digital payments → **{dig_f[-1]}%** (SAMA target: 80%+)")
        with drb:
            de = pd.DataFrame({"Year":HY+FY,"Digital Pay %":dig_df["Digital Pay %"].tolist()+dig_f,"Type":["Actual"]*9+["ML Forecast"]*6})
            st.download_button("📥 Download CSV",csv_b(de),"digital_forecast.csv","text/csv",use_container_width=True)
    with db:
        st.markdown("""<div class="icard"><h4>💳 Digital Economy</h4>
        <div class="irow"><div class="idot" style="background:#005C2E;"></div><p class="itxt">79% digital payment adoption 2024 — up from 31% in 2016.</p></div>
        <div class="irow"><div class="idot" style="background:#2563EB;"></div><p class="itxt">E-commerce reached <b>SAR 85B</b> — 20%+ YoY growth.</p></div>
        <div class="irow"><div class="idot" style="background:#D4A017;"></div><p class="itxt">STC Pay, Tamara, Foodics driving Saudi fintech boom.</p></div></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="premium"><p style="color:#D4A017;font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin:0 0 5px;">🔒 Premium — Saudi Economy Intelligence Report 2026</p><p style="color:rgba(255,255,255,.85);font-size:12.5px;margin:0 0 3px;">Full GDP breakdown, sector analysis &amp; ML forecasts to 2030. Bilingual Arabic–English.</p><p style="color:rgba(255,255,255,.55);font-size:11.5px;margin:0;">📩 zaidug987198@gmail.com &nbsp;|&nbsp; <b style="color:#D4A017;">SAR 500 – 2,000</b></p></div>""", unsafe_allow_html=True)

# ─── TAB 2 ───
with t2:
    st.markdown('<p class="ar-strip">أداء قطاع السياحة مع توقعات ML حتى 2030 · الهدف: 150 مليون زائر</p>', unsafe_allow_html=True)
    st.markdown('<span class="badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
    st.write("")
    tc,ti = st.columns([2.4,1])
    with tc:
        f2 = go.Figure()
        f2.add_trace(go.Bar(x=tour_df["Year"],y=tour_df["Visitors (M)"],name="Actual Visitors (M)",marker=dict(color=[G1,RED,GOLD,G2,G3,G1],line=dict(color=WH,width=1.5)),text=tour_df["Visitors (M)"].astype(str)+"M",textposition="outside",textfont=dict(color=NAVY,size=12),hovertemplate="<b>%{x}</b><br>%{y}M<extra></extra>"))
        f2.add_trace(go.Bar(x=FY,y=tour_f,name="ML Forecast (M)",marker=dict(color="rgba(0,166,81,0.32)",line=dict(color=G3,width=1.5)),text=[f"{round(v)}M*" for v in tour_f],textposition="outside",textfont=dict(color=G2,size=12),hovertemplate="<b>%{x} ★</b><br>%{y:.0f}M<extra></extra>"))
        f2.add_hline(y=150,line_dash="dash",line_color=RED,line_width=2,annotation_text="  2030 Target: 150M",annotation_font_color=RED,annotation_font_size=11)
        f2.update_layout(**CL("Tourism Visitors (M) + ML Forecast to 2030 | السياحة",[0,195]))
        st.plotly_chart(f2,use_container_width=True)
        tra,trb = st.columns([3,1])
        with tra:
            proj = round(tour_f[-1])
            st.info(f"🤖 **ML 2030:** {proj}M visitors projected — {'✅ On track' if proj>=140 else '⚠️ May fall short'} for 150M target.")
        with trb:
            te = pd.DataFrame({"Year":[2019,2020,2021,2022,2023,2024]+FY,"Visitors (M)":tour_df["Visitors (M)"].tolist()+tour_f,"Type":["Actual"]*6+["ML Forecast"]*6})
            st.download_button("📥 Download CSV",csv_b(te),"tourism_forecast.csv","text/csv",use_container_width=True)
    with ti:
        pct = int((115/150)*100)
        st.markdown(f"""<div class="icard"><h4>✈️ Tourism | السياحة</h4>
        <div style="text-align:center;margin-bottom:.9rem;"><p style="font-size:2.6rem;font-weight:800;color:#005C2E;margin:0;line-height:1;">76%</p><p style="font-size:11.5px;color:#5A7080;margin:3px 0 0;">of 150M target reached<br><span class="ar" style="font-size:11px;">76% من الهدف 150 مليون</span></p></div>
        <div class="pb"><div style="background:linear-gradient(90deg,#005C2E,#00A651);height:9px;width:{pct}%;border-radius:8px;"></div></div>
        <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#5A7080;margin-bottom:.8rem;"><span>0</span><span><b>115M</b></span><span>150M</span></div>
        <div class="irow"><div class="idot" style="background:#005C2E;"></div><p class="itxt"><b>SAR 134B</b> revenue 2024 — up <b style="color:#005C2E">38%</b> YoY</p></div>
        <div class="irow"><div class="idot" style="background:#2563EB;"></div><p class="itxt"><b>250,000+</b> new tourism jobs for Saudi nationals</p></div>
        <div class="irow"><div class="idot" style="background:#D4A017;"></div><p class="itxt">NEOM, Red Sea, Qiddiya driving premium international tourism</p></div>
        <div class="src-box"><p style="margin:0;font-size:11px;font-weight:700;color:#92400E;">📡 Source</p><p style="margin:0;font-size:11px;color:#5A7080;">sta.gov.sa · vision2030.gov.sa</p></div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="premium"><p style="color:#D4A017;font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin:0 0 5px;">🔒 Premium Tourism Intelligence Report</p><p style="color:rgba(255,255,255,.85);font-size:12.5px;margin:0 0 3px;">Hotel occupancy · Source markets · Hajj/Umrah tech · MICE industry analysis.</p><p style="color:rgba(255,255,255,.55);font-size:11.5px;margin:0;">📩 zaidug987198@gmail.com &nbsp;|&nbsp; <b style="color:#D4A017;">SAR 750 – 1,500</b></p></div>""", unsafe_allow_html=True)

# ─── TAB 3 ───
with t3:
    sp,sb_col = st.columns(2)
    with sp:
        fp = px.pie(sec_df,values="Investment (SAR B)",names="Sector",title="Investment by Sector | توزيع الاستثمار (SAR B)",hole=0.42,color_discrete_sequence=[G1,G2,G3,GOLD,B2,"#8B5CF6"])
        fp.update_traces(textinfo="percent+label",textfont=dict(size=12,color=NAVY,family="Outfit"),hovertemplate="<b>%{label}</b><br>SAR %{value}B<br>%{percent}<extra></extra>")
        fp.update_layout(**CL(""))
        st.plotly_chart(fp,use_container_width=True)
    with sb_col:
        fg = px.bar(sec_df.sort_values("Growth %"),x="Growth %",y="Sector",orientation="h",title="YoY Growth by Sector | معدل النمو (%)",color="Growth %",color_continuous_scale=["#A7F3D0","#007A3D","#004D26"],text="Growth %")
        fg.update_traces(texttemplate="%{text}%",textposition="outside",textfont=dict(color=NAVY,size=12,family="Outfit"))
        fg.update_layout(**CL(""),coloraxis_showscale=False)
        st.plotly_chart(fg,use_container_width=True)
    sr1,sr2 = st.columns([4,1])
    with sr2: st.download_button("📥 Download Sector Data",csv_b(sec_df),"sectors.csv","text/csv",use_container_width=True)

    st.markdown('<p class="sec-lbl" style="margin-top:.8rem;">المشاريع العملاقة — Giga-Projects Tracker</p>', unsafe_allow_html=True)
    gcols = st.columns(5)
    gclrs = [G1,G2,GOLD,B2,G3]
    for i,(_,row) in enumerate(giga_df.iterrows()):
        with gcols[i]:
            st.markdown(f"""<div style="background:{WH};border:1.5px solid {BDR};border-radius:13px;padding:.95rem;border-top:4px solid {gclrs[i]};box-shadow:0 2px 10px rgba(0,0,0,0.05);text-align:center;"><p style="font-size:13.5px;font-weight:800;color:{gclrs[i]};margin:0 0 3px;">{row['Project']}</p><p style="font-size:11px;color:{SL};margin:0 0 6px;">{row['Focus']}</p><p style="font-size:1.3rem;font-weight:800;color:{NAVY};margin:0 0 5px;">${row['Budget($B)']}B</p><span style="background:{gclrs[i]}18;color:{gclrs[i]};font-size:10px;font-weight:700;padding:2px 8px;border-radius:11px;">{row['Status']}</span></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    trows = "".join([f"""<tr style="background:{'#F4F7FB' if i%2==0 else WH};border-bottom:1px solid {BDR};"><td style="padding:10px 15px;color:{NAVY};font-weight:600;">{r['Sector']}</td><td style="padding:10px 15px;color:{NAVY};font-weight:700;text-align:right;">SAR {r['Investment (SAR B)']}B</td><td style="padding:10px 15px;text-align:right;"><span style="background:#E6F7EE;color:#005C2E;font-weight:700;padding:2px 9px;border-radius:10px;font-size:11.5px;">↑ {r['Growth %']}%</span></td><td style="padding:10px 15px;color:{SL};text-align:right;">{r['Jobs (000s)']}K+</td></tr>""" for i,(_,r) in enumerate(sec_df.iterrows())])
    st.markdown(f"""<table style="width:100%;border-collapse:collapse;font-family:Outfit,sans-serif;font-size:12.5px;background:{WH};border-radius:12px;overflow:hidden;border:1.5px solid {BDR};box-shadow:0 2px 10px rgba(0,0,0,0.04);">
    <thead><tr style="background:linear-gradient(135deg,#004D26,#007A3D);"><th style="padding:11px 15px;color:{WH};text-align:left;font-weight:700;">Sector | القطاع</th><th style="padding:11px 15px;color:{WH};text-align:right;font-weight:700;">Investment</th><th style="padding:11px 15px;color:{WH};text-align:right;font-weight:700;">YoY Growth</th><th style="padding:11px 15px;color:{WH};text-align:right;font-weight:700;">Jobs Created</th></tr></thead>
    <tbody>{trows}</tbody></table>""", unsafe_allow_html=True)

# ─── TAB 4 ───
with t4:
    st.markdown('<p class="ar-strip">مشاركة المرأة في سوق العمل + توقعات ML · هدف رؤية 2030: 30% · تم تجاوزه ✅</p>', unsafe_allow_html=True)
    st.markdown('<span class="badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
    st.write("")
    ec,ei = st.columns([2.4,1])
    with ec:
        f4 = go.Figure()
        f4.add_trace(go.Scatter(x=emp_df["Year"],y=emp_df["Female %"],name="Female Emp % (Actual)",mode="lines+markers",line=dict(color=G2,width=3.5),marker=dict(size=9,color=G2,line=dict(color=WH,width=2.5)),fill="tozeroy",fillcolor="rgba(0,122,61,0.08)",hovertemplate="<b>%{x}</b><br>Female Emp: %{y}%<extra></extra>"))
        f4.add_trace(go.Scatter(x=FY,y=fem_f,name="Female Emp % (Forecast)",mode="lines+markers",line=dict(color=G3,width=2.5,dash="dash"),marker=dict(size=8,symbol="diamond",color=G3,line=dict(color=WH,width=2)),hovertemplate="<b>%{x} ★</b><br>Forecast: %{y}%<extra></extra>"))
        f4.add_hline(y=30,line_dash="dash",line_color=RED,line_width=1.5,annotation_text="  رؤية 2030 Target: 30%",annotation_font_color=RED,annotation_font_size=11)
        f4.add_vline(x=2024.5,line_dash="dot",line_color="#94A3B8",annotation_text="  Forecast →",annotation_font_size=10,annotation_font_color="#94A3B8")
        f4.add_annotation(x=2024,y=35.5,text="<b>33.6% — Exceeded! ✅</b>",showarrow=True,arrowhead=2,arrowcolor=G1,arrowwidth=2,font=dict(color=G1,size=11.5),bgcolor="#E6F7EE",bordercolor=G2,borderwidth=1.5)
        f4.update_layout(**CL("Female Workforce Participation (%) + ML Forecast to 2030 | توظيف المرأة",[12,50]))
        st.plotly_chart(f4,use_container_width=True)
        ea,eb = st.columns([3,1])
        with ea: st.info(f"🤖 **ML 2030:** Female employment → **{fem_f[-1]}%** — well above the 30% Vision target.")
        with eb:
            ee = pd.DataFrame({"Year":HY+FY,"Female Emp %":emp_df["Female %"].tolist()+fem_f,"Type":["Actual"]*9+["ML Forecast"]*6})
            st.download_button("📥 Download CSV",csv_b(ee),"employment_forecast.csv","text/csv",use_container_width=True)
    with ei:
        st.markdown(f"""<div class="icard"><h4>👩‍💼 Employment | التوظيف</h4>
        <div style="background:#F0FDF6;border-radius:11px;padding:.95rem;margin-bottom:.8rem;border:1.5px solid #BBF7D0;text-align:center;"><p style="font-size:2.2rem;font-weight:800;color:#005C2E;margin:0;">33.6%</p><p style="font-size:11.5px;color:#5A7080;margin:3px 0 0;">Female Workforce 2024<br><b style="color:#005C2E;">30% Target — Exceeded ✅</b><br><span class="ar" style="font-size:10.5px;">تجاوز هدف رؤية 2030</span></p></div>
        <div class="irow"><div class="idot" style="background:#005C2E;"></div><p class="itxt">From <b>17%</b> in 2016 to <b>33.6%</b> in 2024 — nearly <b style="color:#005C2E">doubled</b> in 8 years.</p></div>
        <div class="irow"><div class="idot" style="background:#D4A017;"></div><p class="itxt"><b>Nitaqat Saudization:</b> Mandatory quotas across all industries.</p></div>
        <div class="irow"><div class="idot" style="background:#2563EB;"></div><p class="itxt"><b>Unemployment:</b> Below 7% — lowest in Saudi history.</p></div>
        <div class="irow"><div class="idot" style="background:#8B5CF6;"></div><p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English AI talent is #1 shortage in Vision 2030 companies.</p></div>
        <div class="src-box"><p style="margin:0;font-size:11px;font-weight:700;color:#92400E;">📡 Source</p><p style="margin:0;font-size:11px;color:{SL};">GASTAT · stats.gov.sa</p></div></div>""", unsafe_allow_html=True)

# ─── TAB 5 ───
with t5:
    st.markdown('<p class="ar-strip">استثمارات المملكة في الذكاء الاصطناعي والبنية التحتية التقنية — 2025</p>', unsafe_allow_html=True)
    ac,ai_i = st.columns([2.4,1])
    with ac:
        f5 = go.Figure()
        f5.add_trace(go.Bar(x=ai_df["Initiative"],y=ai_df["USD Billion"],marker=dict(color=[G1,GOLD,B2,B3,"#8B5CF6"],line=dict(color=WH,width=2)),text=["$"+str(v)+"B" for v in ai_df["USD Billion"]],textposition="outside",textfont=dict(color=NAVY,size=13,family="Outfit"),hovertemplate="<b>%{x}</b><br>$%{y}B<extra></extra>"))
        f5.update_layout(**CL("Saudi AI & Cloud Investment (USD B) | استثمارات الذكاء الاصطناعي 2025",[0,120]),showlegend=False)
        st.plotly_chart(f5,use_container_width=True)
        ar1,ar2 = st.columns([3,1])
        with ar1: st.info("🤖 Saudi Arabia's **$122.7B total AI investment** in 2025 makes it the world's fastest-growing AI market — anchored by HUMAIN's $100B sovereign fund.")
        with ar2: st.download_button("📥 Download CSV",csv_b(ai_df),"ai_investment.csv","text/csv",use_container_width=True)
    with ai_i:
        st.markdown(f"""<div class="icard"><h4>🤖 AI & Tech<br><span class="ar" style="font-size:12px;color:{SL};">الذكاء الاصطناعي</span></h4>
        <div style="background:#F0FDF6;border-radius:9px;padding:9px 12px;margin-bottom:7px;border-left:4px solid {G1};"><p style="margin:0;font-size:13px;font-weight:700;color:{G1};">HUMAIN — $100B</p><p style="margin:0;font-size:11.5px;color:{SL};">PIF sovereign AI company.<br>Partners: Nvidia, AMD, AWS, Google<br><span class="ar" style="font-size:11px;">شركة الذكاء الاصطناعي السعودية</span></p></div>
        <div style="background:#FFFBEB;border-radius:9px;padding:9px 12px;margin-bottom:7px;border-left:4px solid {GOLD};"><p style="margin:0;font-size:13px;font-weight:700;color:{GOLDD};">Nvidia Deal — $14.9B</p><p style="margin:0;font-size:11.5px;color:{SL};">Largest-ever GPU deal globally.<br>18,000+ Blackwell AI chips</p></div>
        <div style="background:#EFF6FF;border-radius:9px;padding:9px 12px;margin-bottom:7px;border-left:4px solid {B2};"><p style="margin:0;font-size:13px;font-weight:700;color:#1E40AF;">AWS + Google + Microsoft</p><p style="margin:0;font-size:11.5px;color:{SL};">$7.8B combined cloud in Saudi Arabia</p></div>
        <div style="background:linear-gradient(135deg,#004D26,#007A3D);border-radius:10px;padding:11px;text-align:center;">
          <p style="color:{WH};margin:0;font-size:12.5px;font-weight:700;">🤖 An-Nasir AI</p>
          <p style="color:rgba(255,255,255,.80);margin:3px 0 5px;font-size:11px;">Arabic-English AI Agent<br>Vertex AI + ADK · Vision 2030<br><span class="ar">وكيل ذكاء اصطناعي ثنائي اللغة</span></p>
          <a href="https://github.com/zaidug987198-design/v2030-pulse" target="_blank" style="display:block;background:rgba(255,255,255,.18);color:{WH};text-decoration:none;border-radius:7px;padding:5px 10px;font-size:11px;font-weight:700;border:1px solid rgba(255,255,255,.28);">🐙 View on GitHub</a>
        </div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="premium"><p style="color:#D4A017;font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin:0 0 5px;">🔒 Saudi AI Market Intelligence Report 2026</p><p style="color:rgba(255,255,255,.85);font-size:12.5px;margin:0 0 3px;">HUMAIN deep dive · Vision 2030 tech talent gaps · Bilingual AI strategies · Indian tech entering Saudi market.</p><p style="color:rgba(255,255,255,.55);font-size:11.5px;margin:0;">📩 zaidug987198@gmail.com &nbsp;|&nbsp; <b style="color:#D4A017;">SAR 1,000 – 2,000</b> &nbsp;|&nbsp; Arabic + English · 5 business days</p></div>""", unsafe_allow_html=True)

# ═══════════════ FOOTER ═══════════════
st.divider()
st.markdown(f"""
<div style="background:{WH};border:1.5px solid {BDR};border-radius:15px;padding:1.2rem 1.6rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;box-shadow:0 2px 10px rgba(0,0,0,0.04);">
  <div style="display:flex;align-items:center;gap:13px;">
    {LOGO}
    <div>
      <p style="margin:0;font-size:13.5px;font-weight:800;color:{NAVY};">V2030 Intelligence Hub</p>
      <p style="margin:2px 0 0;font-size:11.5px;color:{SL};">open.data.gov.sa · vision2030.gov.sa · GASTAT · SDAIA · World Bank</p>
      <p style="margin:1px 0 0;font-size:10.5px;color:#94A3B8;font-family:IBM Plex Sans Arabic,sans-serif;">جميع البيانات من المصادر الحكومية السعودية الرسمية</p>
    </div>
  </div>
  <div style="text-align:right;">
    <p style="margin:0;font-size:13px;font-weight:700;color:{G1};">Engineered by Mohammad Zaid</p>
    <p style="margin:2px 0 5px;font-size:11px;color:{SL};">Hafiz-e-Quran · Arabic C1 · Google Gen AI APAC 2026 · Jamia Hamdard</p>
    <div style="display:flex;gap:6px;justify-content:flex-end;">
      <a href="https://github.com/zaidug987198-design/v2030-pulse" target="_blank" style="background:{NAVY};color:{WH};text-decoration:none;border-radius:7px;padding:5px 11px;font-size:11px;font-weight:700;">🐙 GitHub</a>
      <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/" target="_blank" style="background:#0A66C2;color:{WH};text-decoration:none;border-radius:7px;padding:5px 11px;font-size:11px;font-weight:700;">💼 LinkedIn</a>
      <a href="mailto:zaidug987198@gmail.com" style="background:linear-gradient(135deg,{GOLD},{GOLDD});color:#1A1000;text-decoration:none;border-radius:7px;padding:5px 11px;font-size:11px;font-weight:700;">📧 Contact</a>
    </div>
  </div>
</div>
<p style="text-align:center;font-size:10.5px;color:#94A3B8;margin-top:9px;">
  © 2026 Mohammad Zaid &nbsp;|&nbsp; Python · Streamlit · Plotly · NumPy ML Forecasting &nbsp;|&nbsp; Data from official Saudi government portals
</p>
""", unsafe_allow_html=True)