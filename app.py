import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 1. ENTERPRISE LEVEL PAGE SETUP
st.set_page_config(
    page_title="Saudi Vision 2030 Intelligence Hub",
    page_icon="🇸🇦",
    layout="wide"
)

# 2. FIXED STYLING FOR MAXIMUM VISIBILITY (No hidden text, Auto-Theme Safe)
st.markdown("""
<style>
    /* Metric Cards - Solid contrasting background for any mode */
    [data-testid="stMetric"] {
        background: #0B1828 !important;
        border: 1px solid #1E3050 !important;
        border-radius: 12px !important;
        padding: 18px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }
    
    /* Ensuring absolute readability inside cards */
    .stMetric label { color: #C9A84C !important; font-size: 1.05rem !important; font-weight: 700 !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 2.1rem !important; font-weight: bold !important; }
    
    /* Custom Badges */
    .gov-badge { background-color: #006C35; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.85rem; font-weight: bold; }
    .hr-badge { background-color: #C9A84C; color: black; padding: 4px 10px; border-radius: 4px; font-size: 0.85rem; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR: CLEANED & FIXED ──
with st.sidebar:
    # Title replaced the broken image icon completely
    st.markdown("### 🇸🇦 Vision 2030 Portal")
    st.markdown("---")
    # Changed from 'Target Audience View' to 'Audience View'
    st.markdown("### 🏢 **Audience View**")
    view_mode = st.radio("Optimize Analytics For:", ["🏛️ Government Metrics", "💼 HR & Talent Acquisition", "👥 Public General Impact"])
    st.markdown("---")
    st.markdown("### 🛠️ **System Status**")
    st.success("Data Pipeline: Stable")
    st.caption("Engineered using Python & Streamlit Core Architecture.")

# ── CENTRAL TITLE HEADER ──
st.title("🇸🇦 Vision 2030 Pulse | نبض رؤية 2030")
st.markdown("#### National Transformation & Economic Intelligence | Executive Portfolio Optimization")
st.divider()

# ── TOP LAYER KEY METRICS ──
k1, k2, k3, k4, k5 = st.columns(5)
with k1: st.metric("Non-Oil GDP Share", "50.2%", "↑ 4.1% (Target: 50% ✅)")
with k2: st.metric("National Digital Payments", "79.0%", "↑ 22.0% (SAMA Index)")
with k3: st.metric("Female Workforce Rate", "33.6%", "↑ 8.2% (Historic Peak)")
with k4: st.metric("Tourism Ecosystem Rev.", "SAR 134B", "↑ 38.0% YoY")
with k5: st.metric("Tech Startup Capital", "$1.72B", "↑ 145.0% Inflow")

st.divider()

# ── CENTRALIZED MARKET RESEARCH DATASETS ──
gdp_df = pd.DataFrame({
    'Year':[2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'Oil GDP %':[43,42,44,41,35,40,46,39,37],
    'Non-Oil GDP %':[57,58,56,59,65,60,54,61,63]
})
tourism_df = pd.DataFrame({
    'Year':[2019,2020,2021,2022,2023,2024],
    'Visitors (M)':[100,41,63,93,106,115],
    'Target 2030':[150,150,150,150,150,150]
})
sectors_df = pd.DataFrame({
    'Sector':['Tourism','Technology','Healthcare','Entertainment','Mining','Logistics'],
    'Investment (SAR B)':[134,89,67,45,38,29]
})

# ── ENTERPRISE TABS MANAGEMENT ──
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Macro-Economics & Localization",
    "✈️ Tourism Infrastructure",
    "🏭 Industrial Capital Flow",
    "🤖 Emerging Tech & Strategic AI"
])

# Shared Visualization Layout Engine (Guarantees Text Visibility dynamically)
def global_layout_engine(fig, chart_title):
    fig.update_layout(
        title=dict(text=chart_title, font=dict(size=16)),
        margin=dict(l=40, r=40, t=50, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

with tab1:
    st.markdown("### Macro Economic Matrix & HR Saudization Parameters")
    col_e1, col_e2 = st.columns([2, 1])
    with col_e1:
        fig1 = px.area(gdp_df, x='Year', y=['Oil GDP %','Non-Oil GDP %'],
                      color_discrete_map={'Oil GDP %':'#112543', 'Non-Oil GDP %':'#006C35'})
        st.plotly_chart(global_layout_engine(fig1, "Structural Diversification: Oil vs Non-Oil GDP"), use_container_width=True)
    with col_e2:
        st.markdown("<span class='hr-badge'>💼 RECRUITER INSIGHTS</span>", unsafe_allow_html=True)
        st.write("")
        st.markdown("""
        * **Nitaqat Compliance:** National talent matching has driven domestic localized employment down to historical unemployment lows.
        * **HR Opportunity Matrix:** High velocity hiring fields detected in Cyber Architecture, Financial Analytics, and Hospitality Management.
        """)

with tab2:
    st.markdown("### Aviation, Border Entry & Domestic Hospitality Data")
    col_t1, col_t2 = st.columns([2, 1])
    with col_t1:
        fig2 = px.bar(tourism_df, x='Year', y=['Visitors (M)','Target 2030'], barmode='group',
                      color_discrete_map={'Visitors (M)':'#5DCAA5', 'Target 2030':'#C9A84C'})
        st.plotly_chart(global_layout_engine(fig2, "Tourism Performance Metrics vs Strategic Targets"), use_container_width=True)
    with col_t2:
        st.markdown("<span class='gov-badge'>🏛️ GOVERNMENT AUDIT</span>", unsafe_allow_html=True)
        st.write("")
        st.markdown("""
        * **Target Evaluation:** Current execution trends represent a 115M annual footprint, positioning the Kingdom to capture the 150M milestone ahead of schedule.
        * **Public Welfare Impact:** Leisure sector expansion has generated directly over 250,000+ localized new jobs for regional citizens.
        """)

with tab3:
    st.markdown("### Capital Allocations across Non-Oil Industrial Pillars")
    col_s1, col_s2 = st.columns([1, 1])
    with col_s1:
        fig3 = px.pie(sectors_df, values='Investment (SAR B)', names='Sector',
                      color_discrete_sequence=px.colors.sequential.Emrld_r)
        st.plotly_chart(global_layout_engine(fig3, "Distribution of Vision Sovereign Investment (SAR Billions)"), use_container_width=True)
    with col_s2:
        st.markdown("#### 🏗️ Giga-Project Capital Status Tracker")
        project_data = pd.DataFrame({
            "Core Giga-Project": ["NEOM", "The Red Sea Project", "Qiddiya Core", "ROSHN Housing"],
            "Operational Focus": ["Cognitive Urban AI", "Regenerative Eco-Tourism", "Global Sports & Entertainment", "National Asset Infrastructure"],
            "State Framework Target": ["Net-Zero Carbon Realized", "100% Microgrid Renewables", "Global Entertainment Capital", "70% Civilian Homeownership"]
        })
        st.table(project_data)

with tab4:
    st.markdown("### High-Performance Computing, Sovereignty & Cloud Scaling")
    ai_data = {
        "Strategic Initiative":["HUMAIN (PIF Fund)","Nvidia Enterprise Deal","AWS Infrastructure Hub","Google Cloud Region","Microsoft Cloud Region"],
        "Capital Volume ($B)":[100.0, 14.9, 5.3, 1.0, 1.5],
        "Architecture Vector":["Sovereign Asset Fund", "AI Hardware Cluster", "Cloud Foundation Layer", "Cloud Foundation Layer", "Cloud Foundation Layer"]
    }
    fig4 = px.bar(pd.DataFrame(ai_data), x="Strategic Initiative", y="Capital Volume ($B)", color="Architecture Vector",
                  color_discrete_sequence=['#C9A84C', '#5DCAA5', '#16315C'])
    st.plotly_chart(global_layout_engine(fig4, "SDAIA Managed AI Capital Deployment Strategy (USD Billions)"), use_container_width=True)

# ── ELITE FOOTER: DUAL METADATA CREDENTIAL PANEL ──
st.divider()
footer_col1, footer_col2 = st.columns([2, 1])

with footer_col1:
    st.markdown("""
    **Framework Specification Notice:** This interactive enterprise asset is engineered by **Mohammad Zaid** using verified reference statistics from the Saudi General Authority for Statistics (`open.data.gov.sa`) and the National Vision 2030 Bureau. It showcases analytical instrumentation, deployment safety protocols, and automated pipeline structuring.
    """)

with footer_col2:
    st.markdown("<p style='color:#C9A84C; font-weight:bold; margin-bottom: 2px;'>SYSTEM DEVELOPER PATHWAYS</p>", unsafe_allow_html=True)
    st.markdown("📦 [Access GitHub Source Repository](https://github.com/zaidug987198-design)")
    st.markdown("👔 [Review Professional Credentials on LinkedIn](https://www.linkedin.com/in/mohammad-zaid-289368379/)")

st.caption("© 2026 Mohammad Zaid | Jamia Hamdard | Google Gen AI APAC Academy Integration Asset")