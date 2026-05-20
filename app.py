import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# 1. Page Config
st.set_page_config(page_title="🇸🇦 Vision 2030 Global Insights", layout="wide", initial_sidebar_state="expanded")

# 2. Advanced CSS for "Premium Look"
st.markdown("""
<style>
    .main { background-color: #0b0f19; }
    .stMetric { background: linear-gradient(135deg, #006C35 0%, #004d26 100%); color: white !important; border-radius: 15px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.4); }
    [data-testid="stMetricValue"] { color: #C9A84C !important; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1e2530; border-radius: 5px; color: white; padding: 10px 20px; }
    .status-card { background: #161b25; border-left: 5px solid #C9A84C; padding: 15px; border-radius: 10px; margin-bottom: 15px; color: white; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.image("https://www.vision2030.gov.sa/media/rc0bc1v2/vision2030_logo_en.svg", width=200)
    st.header("📊 Market Intelligence")
    st.info("Focus: Sustainability, AI & Digital Finance")
    st.markdown("---")
    st.write("**Contact Developer:**")
    st.write("👤 Mohammad Zaid")
    st.write("🎓 Jamia Hamdard, New Delhi")

# ── HEADER ──
st.title("🇸🇦 Saudi Vision 2030: The Intelligence Dashboard")
st.markdown("### Strategic Progress Analysis & Market Research | نبض التحول الرقمي")
st.divider()

# ── GLOBAL KPI SECTION ──
k1, k2, k3, k4 = st.columns(4)
k1.metric("Digital Economy", "SAR 175B", "↑ 12% YoY")
k2.metric("SGI: Trees Planted", "50M+", "Target: 10B")
k3.metric("FDI Inflow", "$19.3B", "↑ 25%")
k4.metric("Internet Usage", "99%", "Global Leader")

st.divider()

# ── MARKET RESEARCH TABS ──
tab1, tab2, tab3, tab4 = st.tabs(["📉 Economy & FDI", "🌿 Green Initiative", "🛡️ Digital Security", "🔗 Connect"])

with tab1:
    c1, c2 = st.columns([2, 1])
    with c1:
        # Investment Trend
        fdi_data = pd.DataFrame({
            'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
            'Investment (B USD)': [1.4, 4.2, 4.6, 5.4, 19.3, 8.1, 12.3, 15.1]
        })
        fig_fdi = px.line(fdi_data, x='Year', y='Investment (B USD)', title="Foreign Direct Investment (FDI) Growth", markers=True)
        fig_fdi.update_traces(line_color='#C9A84C', line_width=3)
        st.plotly_chart(fig_fdi, use_container_width=True)
    with c2:
        st.write("### 💎 Top Sectors")
        st.write("1. **Manufacturing** (28%)")
        st.write("2. **Tech & AI** (22%)")
        st.write("3. **Real Estate** (15%)")
        st.write("4. **Renewables** (12%)")

with tab2:
    st.subheader("🌿 Saudi Green Initiative (SGI)")
    g1, g2 = st.columns(2)
    with g1:
        # Carbon Reduction
        fig_green = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 278,
            title = {'text': "Carbon Displacement (M Tons/Year)"},
            gauge = {'axis': {'range': [None, 600]}, 'bar': {'color': "#006C35"}}
        ))
        st.plotly_chart(fig_green, use_container_width=True)
    with g2:
        st.markdown("""
        <div class="status-card">
            <h4>🎯 Sustainability Targets</h4>
            <ul>
                <li>50% Energy from Renewables by 2030</li>
                <li>Zero Carbon Neutrality by 2060</li>
                <li>4% of Global Carbon Reduction contribution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.subheader("🛡️ Digital Transformation & Cybersecurity")
    cyber_data = pd.DataFrame({
        'Level': ['Cyber Readiness', 'E-Government', 'AI Adoption', 'Fintech Growth'],
        'Score %': [95, 88, 72, 85]
    })
    fig_cyber = px.bar(cyber_data, x='Score %', y='Level', orientation='h', color='Score %', color_continuous_scale='Emrld')
    st.plotly_chart(fig_cyber, use_container_width=True)

with tab4:
    st.markdown("### 🤝 Get in Touch / التواصل معي")
    st.write("Looking for a developer who understands the Saudi tech landscape? Let's connect.")
    st.button("Visit my LinkedIn Profile")
    st.button("View my GitHub Portfolio")

# ── FOOTER ──
st.divider()
st.markdown("<center style='color: grey;'>Built with ❤️ and Python for Saudi Vision 2030 | Mohammad Zaid - Jamia Hamdard</center>", unsafe_allow_html=True)