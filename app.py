import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 1. Page Config
st.set_page_config(
    page_title="🇸🇦 V2030 Pulse",
    page_icon="🇸🇦",
    layout="wide"
)

# 2. Universal Professional Styling (Works for both Light/Dark)
st.markdown("""
<style>
    /* Card Container */
    [data-testid="stMetric"] {
        background: rgba(128, 128, 128, 0.05);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 15px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    /* Hide Streamlit Branding for clean look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive adjustment for Mobile */
    @media (max-width: 640px) {
        .stMetric {
            margin-bottom: 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.title("🇸🇦 Vision 2030 Pulse")
st.subheader("نبض رؤية 2030")
st.markdown(f"**Built by Mohammad Zaid** | Jamia Hamdard | Google Gen AI APAC 2026")
st.divider()

# ── KPI CARDS (Flexible Grid) ──
k1, k2, k3, k4, k5 = st.columns([1,1,1,1,1])
k1.metric("Non-Oil GDP", "50.2%", "Target 50%")
k2.metric("Tourism", "134B SAR", "↑ 38%")
k3.metric("Female Work", "33.6%", "↑ 8.2%")
k4.metric("Digital Pay", "79%", "↑ 22%")
k5.metric("AI Funding", "$1.72B", "↑ 145%")

st.divider()

# ── DATA PREP ──
gdp_df = pd.DataFrame({
    'Year':[2016,2018,2020,2022,2024],
    'Non-Oil GDP %':[57,56,65,54,63]
})

# ── TABS ──
tab1, tab2, tab3 = st.tabs(["📊 Overview", "✈️ Tourism", "🤖 AI & Tech"])

with tab1:
    # Economy Chart with Universal Theme
    fig = px.area(gdp_df, x='Year', y='Non-Oil GDP %',
                  title="Economic Diversification Path",
                  color_discrete_sequence=['#006C35']) # Saudi Green
    fig.update_layout(
        template="plotly_white" if st.get_option("theme.base") == "light" else "plotly_dark",
        margin=dict(l=20, r=20, t=50, b=20),
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Tourism Data
    tourism_df = pd.DataFrame({
        'Category': ['Visitors', 'Target'],
        'Millions': [115, 150]
    })
    fig2 = px.bar(tourism_df, x='Category', y='Millions', 
                  color='Category',
                  color_discrete_map={'Visitors':'#006C35', 'Target':'#C9A84C'})
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.markdown("### 🤖 Key AI Initiatives")
    ai_col1, ai_col2 = st.columns(2)
    with ai_col1:
        st.info("**HUMAIN (PIF):** $100 Billion Fund for AI development.")
    with ai_col2:
        st.success("**Nvidia Deal:** $14.9 Billion AI infrastructure.")

st.divider()
st.caption("Data Source: open.data.gov.sa | Final Year BCA Portfolio Project")