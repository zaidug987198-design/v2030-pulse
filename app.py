import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="🇸🇦 V2030 Pulse",
    page_icon="🇸🇦",
    layout="wide"
)

st.markdown("""<style>
.main{background:#050C18}
.stMetric{background:#0B1828;border:1px solid #1E3050;
          border-radius:10px;padding:.5rem}
</style>""", unsafe_allow_html=True)

# ── HEADER ──
st.title("🇸🇦 Vision 2030 Pulse | نبض رؤية 2030")
st.caption("Real-time Saudi Arabia Progress Tracker | Built by Mohammad Zaid")
st.divider()

# ── KPI CARDS ──
k1,k2,k3,k4,k5 = st.columns(5)
k1.metric("Non-Oil GDP", "50.2%", "↑4.1% (Target:50%✅)")
k2.metric("Tourism Revenue", "SAR 134B", "↑38%")
k3.metric("Female Employment", "33.6%", "↑8.2%")
k4.metric("Digital Payments", "79%", "↑22%")
k5.metric("Startups Funded", "$1.72B", "↑145%")
st.divider()

# ── DATA ──
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
    'Sector':['Tourism','Technology','Healthcare',
              'Entertainment','Mining','Logistics'],
    'Investment (SAR B)':[134,89,67,45,38,29]
})

# ── TABS ──
tab1,tab2,tab3,tab4 = st.tabs([
    "📈 Economy","✈️ Tourism",
    "🏭 Sectors","🤖 AI & Tech"
])

with tab1:
    fig = px.area(gdp_df, x='Year',
                  y=['Oil GDP %','Non-Oil GDP %'],
                  title="Oil vs Non-Oil GDP — Vision 2030 Target: 50% Non-Oil",
                  color_discrete_map={
                      'Oil GDP %':'#C9A84C',
                      'Non-Oil GDP %':'#4A9EFF'
                  })
    fig.update_layout(
        plot_bgcolor='#050C18',
        paper_bgcolor='#050C18',
        font_color='#F0F4FF'
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig2 = px.bar(tourism_df, x='Year',
                  y=['Visitors (M)','Target 2030'],
                  title="Tourism: Visitors vs 2030 Target (150M)",
                  barmode='group',
                  color_discrete_map={
                      'Visitors (M)':'#5DCAA5',
                      'Target 2030':'#C9A84C'
                  })
    fig2.update_layout(plot_bgcolor='#050C18',
                       paper_bgcolor='#050C18',
                       font_color='#F0F4FF')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    fig3 = px.pie(sectors_df, values='Investment (SAR B)',
                  names='Sector',
                  title="Vision 2030 Investment by Sector",
                  color_discrete_sequence=px.colors.sequential.Blues_r)
    fig3.update_layout(paper_bgcolor='#050C18',
                       font_color='#F0F4FF')
    st.plotly_chart(fig3, use_container_width=True)

with tab4:
    st.markdown("### 🤖 Saudi AI Investment 2025")
    ai_data = {
        "Initiative":["HUMAIN (PIF)","Nvidia Deal",
                      "AWS Saudi","Google Cloud","Microsoft"],
        "Amount (USD B)":[100,14.9,5.3,1,1.5],
        "Type":["Government","Hardware",
                "Cloud","Cloud","Cloud"]
    }
    fig4 = px.bar(pd.DataFrame(ai_data),
                  x="Initiative", y="Amount (USD B)",
                  color="Type",
                  title="Saudi Arabia AI Investments 2025 (USD Billions)")
    fig4.update_layout(plot_bgcolor='#050C18',
                       paper_bgcolor='#050C18',
                       font_color='#F0F4FF')
    st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.caption("Built by Mohammad Zaid | Jamia Hamdard | Google Gen AI APAC 2026 | Data: open.data.gov.sa, Vision2030.gov.sa")