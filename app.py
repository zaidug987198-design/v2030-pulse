import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Page Configuration (Ye screen ko sahi set karega)
st.set_page_config(
    page_title="Vision 2030 Pulse",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Styling (White background aur Green headers ke liye)
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stMetric { background-color: #f8f9fa; border-radius: 10px; padding: 15px; border-left: 5px solid #006C35; }
    div[data-testid="stMetricValue"] { color: #006C35; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("🇸🇦 Vision 2030 Pulse | نبض رؤية 2030")
st.write("Real-time Saudi Arabia Progress Tracker | Built by **Mohammad Zaid**")
st.divider()

# 4. Key Metrics (Metrics ko columns mein barabar kiya)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Non-Oil GDP", "50.2%", "↑ 4.1%")
m2.metric("Tourism Revenue", "SAR 134B", "↑ 38%")
m3.metric("Female Employment", "33.6%", "↑ 8.2%")
m4.metric("Digital Payments", "79%", "↑ 22%")

st.subheader("📈 Strategic Growth Analysis")

# 5. Charts (Layout ko clean kiya)
col1, col2 = st.columns(2)

with col1:
    # Economy Chart
    economy_data = pd.DataFrame({
        'Sector': ['Oil', 'Non-Oil', 'Services', 'Tech'],
        'Value': [40, 50, 7, 3]
    })
    fig1 = px.pie(economy_data, values='Value', names='Sector', 
                 title="GDP Composition 2026",
                 color_discrete_sequence=['#006C35', '#228B22', '#32CD32', '#00A36C'])
    fig1.update_layout(width=400, height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Tourism Growth Chart
    tourism_data = pd.DataFrame({
        'Year': ['2021', '2022', '2023', '2024', '2025', '2026'],
        'Visitors (M)': [12, 18, 27, 32, 45, 60]
    })
    fig2 = px.line(tourism_data, x='Year', y='Visitors (M)', 
                  title="Tourism Growth (Millions)",
                  markers=True)
    fig2.update_traces(line_color='#006C35')
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

# 6. Footer
st.divider()
st.caption("Built by **Mohammad Zaid** | Jamia Hamdard | Google Gen AI APAC 2026 | Data Source: open.data.gov.sa")