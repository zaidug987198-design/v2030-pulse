जी बिल्कुल! यहां आपका पूरा fixed code है:
Action: file_editor view /app/app.py
Observation: [Showing lines 1-1525 of 1525 total] /app/app.py:
1|"""
2|╔══════════════════════════════════════════════════════════════════════╗
3|║  Saudi Vision 2030 Strategic Intelligence Hub                       ║
4|║  مؤشر تقدم رؤية المملكة العربية السعودية 2030                      ║
5|║  Built by: Mohammad Zaid | Jamia Hamdard | Google Gen AI APAC 2026  ║
6|╚══════════════════════════════════════════════════════════════════════╝
7|"""
8|
9|import streamlit as st
10|import plotly.express as px
11|import plotly.graph_objects as go
12|import pandas as pd
13|import numpy as np
14|from io import StringIO
15|
16|# ══════════════════════════════════════════════════════════════
17|# PAGE CONFIG
18|# ══════════════════════════════════════════════════════════════
19|st.set_page_config(
20|    page_title="رؤية 2030 | V2030 Intelligence Hub",
21|    page_icon="🇸🇦",
22|    layout="wide",
23|    initial_sidebar_state="expanded",
24|    menu_items={
25|        "Get Help": "https://www.linkedin.com/in/mohammad-zaid-289368379/",
26|        "About": "V2030 Intelligence Hub | Built by Mohammad Zaid"
27|    }
28|)
29|
30|# ══════════════════════════════════════════════════════════════
31|# VISION 2030 LOGO — Inline SVG
32|# ══════════════════════════════════════════════════════════════
33|LOGO_SVG = """
34|<svg width="180" height="56" viewBox="0 0 180 56" xmlns="http://www.w3.org/2000/svg">
35|  <rect width="180" height="56" rx="10" fill="#005C2E"/>
36|  <rect x="4" y="4" width="48" height="48" rx="7" fill="rgba(255,255,255,0.10)"/>
37|  <line x1="28" y1="42" x2="28" y2="24" stroke="#D4A017" stroke-width="2.5" stroke-linecap="round"/>
38|  <path d="M28 24 Q21 17 14 19" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
39|  <path d="M28 24 Q24 15 28 12" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
40|  <path d="M28 24 Q35 17 42 20" stroke="#D4A017" stroke-width="2" fill="none" stroke-linecap="round"/>
41|  <path d="M28 24 Q30 16 34 15" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
42|  <path d="M28 24 Q26 16 22 15" stroke="#D4A017" stroke-width="1.5" fill="none" stroke-linecap="round"/>
43|  <line x1="15" y1="37" x2="41" y2="46" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
44|  <line x1="41" y1="37" x2="15" y2="46" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
45|  <text x="60" y="20" font-family="Arial" font-size="9" font-weight="600"
46|        fill="rgba(255,255,255,0.75)" letter-spacing="0.8">KINGDOM OF SAUDI ARABIA</text>
47|  <text x="60" y="36" font-family="Arial" font-size="16" font-weight="900"
48|        fill="#FFFFFF" letter-spacing="-0.3">VISION 2030</text>
49|  <text x="60" y="49" font-family="Arial" font-size="9" font-weight="500"
50|        fill="rgba(255,255,255,0.70)" letter-spacing="0.3">رؤية المملكة العربية السعودية</text>
51|</svg>
52|"""
53|
54|# ══════════════════════════════════════════════════════════════
55|# ENTERPRISE CSS - FIXED FOR TEXT OVERLAP
56|# ══════════════════════════════════════════════════════════════
57|st.markdown("""
58|<style>
59|@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');
60|
61|html, body, [class*="css"], .stApp {
62|    font-family: 'Outfit', 'IBM Plex Sans Arabic', sans-serif !important;
63|    background-color: #F4F7FB !important;
64|}
65|.main .block-container { 
66|    padding: 1.5rem 2rem 2rem !important; 
67|    max-width: 1440px !important; 
68|}
69|#MainMenu, footer, header, .stDeployButton { display: none !important; }
70|
71|/* SIDEBAR - FIXED OVERFLOW */
72|[data-testid="stSidebar"] {
73|    background: #FFFFFF !important;
74|    border-right: 2px solid #E4EAF2 !important;
75|    box-shadow: 4px 0 24px rgba(0,0,0,0.07) !important;
76|    overflow-y: auto !important;
77|}
78|[data-testid="stSidebar"] .stRadio label {
79|    color: #1A2B4A !important; 
80|    font-weight: 500 !important; 
81|    font-size: 13.5px !important;
82|    word-wrap: break-word !important;
83|    overflow-wrap: break-word !important;
84|}
85|[data-testid="stSidebar"] .stTextInput input {
86|    border: 1.5px solid #E4EAF2 !important; 
87|    border-radius: 8px !important;
88|    font-size: 13px !important; 
89|    color: #0D1F2D !important;
90|}
91|[data-testid="stSidebar"] .stTextInput input:focus {
92|    border-color: #005C2E !important; 
93|    box-shadow: 0 0 0 3px rgba(0,92,46,0.12) !important;
94|}
95|
96|/* METRIC CARDS - FIXED TEXT OVERFLOW */
97|[data-testid="stMetric"] {
98|    background: #FFFFFF !important;
99|    border: 1.5px solid #E4EAF2 !important;
100|    border-radius: 14px !important;
101|    padding: 1.1rem 1.25rem !important;
102|    box-shadow: 0 2px 14px rgba(0,80,40,0.07) !important;
103|    transition: transform 0.22s ease, box-shadow 0.22s ease !important;
104|    min-height: 120px !important;
105|    overflow: hidden !important;
106|}
107|[data-testid="stMetric"]:hover {
108|    transform: translateY(-3px) !important;
109|    box-shadow: 0 8px 24px rgba(0,80,40,0.13) !important;
110|}
111|[data-testid="stMetric"] label {
112|    color: #5A7080 !important; 
113|    font-size: 10.5px !important;
114|    font-weight: 700 !important; 
115|    text-transform: uppercase !important;
116|    letter-spacing: 0.7px !important;
117|    word-wrap: break-word !important;
118|    overflow-wrap: break-word !important;
119|    line-height: 1.3 !important;
120|    display: block !important;
121|    margin-bottom: 8px !important;
122|}
123|[data-testid="stMetricValue"] {
124|    color: #0D1F2D !important; 
125|    font-size: 1.7rem !important;
126|    font-weight: 800 !important; 
127|    line-height: 1.2 !important;
128|    word-wrap: break-word !important;
129|    overflow-wrap: break-word !important;
130|}
131|[data-testid="stMetricDelta"] { 
132|    font-size: 11.5px !important; 
133|    font-weight: 600 !important;
134|    white-space: nowrap !important;
135|    overflow: hidden !important;
136|    text-overflow: ellipsis !important;
137|}
138|
139|/* TABS */
140|.stTabs [data-baseweb="tab-list"] {
141|    background: #FFFFFF !important; 
142|    border-radius: 14px !important;
143|    padding: 5px !important; 
144|    gap: 3px !important;
145|    border: 1.5px solid #E4EAF2 !important;
146|    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
147|    margin-bottom: 1.5rem !important;
148|    overflow-x: auto !important;
149|    flex-wrap: wrap !important;
150|}
151|.stTabs [data-baseweb="tab"] {
152|    background: transparent !important; 
153|    border-radius: 10px !important;
154|    color: #5A7080 !important; 
155|    font-weight: 600 !important;
156|    font-size: 12.5px !important; 
157|    padding: 9px 14px !important;
158|    white-space: nowrap !important;
159|}
160|.stTabs [aria-selected="true"] {
161|    background: linear-gradient(135deg,#004D26,#007A3D) !important;
162|    color: #FFFFFF !important;
163|    box-shadow: 0 4px 14px rgba(0,92,46,0.28) !important;
164|}
165|
166|/* DOWNLOAD BUTTON */
167|.stDownloadButton button {
168|    background: linear-gradient(135deg,#004D26,#007A3D) !important;
169|    color: #FFFFFF !important; 
170|    border: none !important;
171|    border-radius: 10px !important; 
172|    font-weight: 700 !important;
173|    font-size: 12px !important; 
174|    padding: 8px 18px !important;
175|    transition: all 0.2s !important;
176|}
177|.stDownloadButton button:hover {
178|    transform: translateY(-1px) !important;
179|    box-shadow: 0 6px 16px rgba(0,92,46,0.28) !important;
180|}
181|
182|/* PREMIUM BUTTON */
183|.stButton button {
184|    background: linear-gradient(135deg,#004D26,#007A3D) !important;
185|    color: #FFFFFF !important; 
186|    border: none !important;
187|    border-radius: 10px !important; 
188|    font-weight: 700 !important;
189|    font-size: 13px !important;
190|}
191|
192|hr { 
193|    border-color: #E4EAF2 !important; 
194|    margin: 1.25rem 0 !important; 
195|}
196|
197|[data-testid="stDataFrame"] {
198|    border-radius: 12px !important; 
199|    border: 1.5px solid #E4EAF2 !important; 
200|    overflow: hidden !important;
201|}
202|
203|.stSuccess { 
204|    background: #F0FDF6 !important; 
205|    border-color: #007A3D !important; 
206|    color: #004D26 !important; 
207|}
208|
209|.stInfo { 
210|    background: #EFF6FF !important; 
211|}
212|
213|/* CUSTOM CLASSES - FIXED OVERLAPS */
214|.sec-label {
215|    font-size: 10.5px; 
216|    font-weight: 700; 
217|    text-transform: uppercase;
218|    letter-spacing: 1.4px; 
219|    color: #5A7080; 
220|    margin-bottom: 0.75rem;
221|    word-wrap: break-word;
222|    overflow-wrap: break-word;
223|}
224|
225|.icard {
226|    background: #FFFFFF; 
227|    border: 1.5px solid #E4EAF2;
228|    border-radius: 14px; 
229|    padding: 1.25rem; 
230|    height: 100%;
231|    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
232|    overflow: hidden;
233|}
234|
235|.icard h4 { 
236|    color: #0D1F2D; 
237|    font-size: 14.5px; 
238|    font-weight: 700; 
239|    margin: 0 0 0.85rem;
240|    word-wrap: break-word;
241|    overflow-wrap: break-word;
242|}
243|
244|.iitem { 
245|    display: flex; 
246|    gap: 10px; 
247|    margin-bottom: 10px; 
248|    align-items: flex-start; 
249|}
250|
251|.idot { 
252|    width: 8px; 
253|    height: 8px; 
254|    border-radius: 50%; 
255|    flex-shrink: 0; 
256|    margin-top: 5px; 
257|}
258|
259|.itxt { 
260|    font-size: 12.5px; 
261|    color: #334155; 
262|    line-height: 1.6; 
263|    margin: 0;
264|    word-wrap: break-word;
265|    overflow-wrap: break-word;
266|    flex: 1;
267|}
268|
269|.pb-wrap { 
270|    background: #E4EAF2; 
271|    border-radius: 8px; 
272|    height: 10px; 
273|    margin: 6px 0; 
274|    overflow: hidden; 
275|}
276|
277|.ar { 
278|    font-family: 'IBM Plex Sans Arabic', sans-serif;
279|    word-wrap: break-word;
280|    overflow-wrap: break-word;
281|}
282|
283|.premium-banner {
284|    background: linear-gradient(135deg,#1A1000,#2D1E00);
285|    border: 1.5px solid #D4A017; 
286|    border-radius: 12px;
287|    padding: 1rem 1.25rem; 
288|    margin: 1rem 0;
289|    overflow: hidden;
290|}
291|
292|.premium-banner p {
293|    word-wrap: break-word !important;
294|    overflow-wrap: break-word !important;
295|}
296|
297|.ml-badge {
298|    display: inline-block; 
299|    background: rgba(0,92,46,0.12);
300|    color: #005C2E; 
301|    font-size: 10.5px; 
302|    font-weight: 700;
303|    padding: 4px 10px; 
304|    border-radius: 12px;
305|    border: 1px solid rgba(0,92,46,0.25); 
306|    margin-right: 5px;
307|    margin-bottom: 5px;
308|    white-space: nowrap;
309|}
310|
311|/* RESPONSIVE FIXES */
312|@media (max-width: 768px) {
313|    .main .block-container { 
314|        padding: 1rem !important; 
315|    }
316|    
317|    [data-testid="stMetric"] {
318|        min-height: auto !important;
319|        padding: 0.9rem 1rem !important;
320|    }
321|    
322|    [data-testid="stMetricValue"] {
323|        font-size: 1.4rem !important;
324|    }
325|    
326|    [data-testid="stMetric"] label {
327|        font-size: 9.5px !important;
328|    }
329|    
330|    .stTabs [data-baseweb="tab"] {
331|        font-size: 11.5px !important;
332|        padding: 8px 12px !important;
333|    }
334|    
335|    .ml-badge {
336|        font-size: 9.5px !important;
337|        padding: 3px 8px !important;
338|    }
339|}
340|
341|/* ADDITIONAL FIXES FOR TEXT WRAPPING */
342|* {
343|    word-wrap: break-word;
344|    overflow-wrap: break-word;
345|}
346|
347|/* Fix for long URLs and emails */
348|a {
349|    word-break: break-all;
350|    overflow-wrap: anywhere;
351|}
352|</style>
353|""", unsafe_allow_html=True)
354|
355|# ══════════════════════════════════════════════════════════════
356|# COLOR PALETTE
357|# ══════════════════════════════════════════════════════════════
358|C = {
359|    "g1": "#004D26", "g2": "#007A3D", "g3": "#00A651",
360|    "g_pale": "#E6F7EE", "g_border": "#BBF7D0",
361|    "gold": "#D4A017", "gold_d": "#B8860B", "gold_pale": "#FFFBEB",
362|    "b1": "#1E40AF", "b2": "#2563EB", "b3": "#60A5FA", "b_pale": "#EFF6FF",
363|    "red": "#DC2626", "red_pale": "#FEF2F2",
364|    "navy": "#0D1F2D", "slate": "#5A7080",
365|    "border": "#E4EAF2", "bg": "#F4F7FB", "white": "#FFFFFF",
366|}
367|
368|# ══════════════════════════════════════════════════════════════
369|# ML FORECAST FUNCTION
370|# ══════════════════════════════════════════════════════════════
371|def ml_forecast(years, values, forecast_years):
372|    """Polynomial regression forecast using numpy with error handling"""
373|    try:
374|        x = np.array(years, dtype=float)
375|        y = np.array(values, dtype=float)
376|        
377|        # Validate input
378|        if len(x) != len(y) or len(x) < 3:
379|            raise ValueError("Insufficient data points for forecasting")
380|        
381|        x_norm = x - x.mean()
382|        coeffs = np.polyfit(x_norm, y, deg=2)
383|        poly = np.poly1d(coeffs)
384|        fx = np.array(forecast_years, dtype=float)
385|        fx_norm = fx - x.mean()
386|        return poly(fx_norm).tolist()
387|    except Exception as e:
388|        st.error(f"Forecasting error: {str(e)}")
389|        return [0] * len(forecast_years)
390|
391|# ══════════════════════════════════════════════════════════════
392|# CHART LAYOUT
393|# ══════════════════════════════════════════════════════════════
394|def CL(title, yrange=None):
395|    """Chart layout configuration"""
396|    L = dict(
397|        title=dict(
398|            text=title, 
399|            font=dict(size=14.5, color=C["navy"], family="Outfit"), 
400|            x=0, 
401|            xanchor="left"
402|        ),
403|        plot_bgcolor=C["white"], 
404|        paper_bgcolor=C["white"],
405|        font=dict(family="Outfit", color=C["navy"], size=12.5),
406|        legend=dict(
407|            bgcolor=C["bg"], 
408|            bordercolor=C["border"],
409|            borderwidth=1.5, 
410|            font=dict(size=11.5, color=C["navy"]),
411|            orientation="h", 
412|            yanchor="bottom", 
413|            y=1.02,
414|            xanchor="right", 
415|            x=1
416|        ),
417|        xaxis=dict(
418|            gridcolor="#EEF2F7", 
419|            linecolor=C["border"],
420|            tickfont=dict(color=C["slate"], size=12),
421|            title_font=dict(color=C["slate"])
422|        ),
423|        yaxis=dict(
424|            gridcolor="#EEF2F7", 
425|            linecolor=C["border"],
426|            tickfont=dict(color=C["slate"], size=12),
427|            title_font=dict(color=C["slate"]),
428|            zerolinecolor=C["border"]
429|        ),
430|        margin=dict(l=16, r=16, t=60, b=28),
431|        hoverlabel=dict(
432|            bgcolor=C["navy"], 
433|            font_color=C["white"],
434|            font_size=12.5, 
435|            bordercolor=C["navy"]
436|        ),
437|    )
438|    if yrange:
439|        L["yaxis"]["range"] = yrange
440|    return L
441|
442|# ══════════════════════════════════════════════════════════════
443|# CSV DOWNLOAD HELPER
444|# ══════════════════════════════════════════════════════════════
445|def to_csv(df):
446|    """Convert DataFrame to CSV"""
447|    return df.to_csv(index=False).encode("utf-8")
448|
449|# ══════════════════════════════════════════════════════════════
450|# ALL DATA
451|# ══════════════════════════════════════════════════════════════
452|HIST_YEARS  = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
453|FORE_YEARS  = [2025,2026,2027,2028,2029,2030]
454|ALL_YEARS   = HIST_YEARS + FORE_YEARS
455|
456|gdp_df = pd.DataFrame({
457|    "Year":          HIST_YEARS,
458|    "Oil GDP %":     [43,42,44,41,35,40,46,39,37],
459|    "Non-Oil GDP %": [57,58,56,59,65,60,54,61,63],
460|})
461|
462|tourism_df = pd.DataFrame({
463|    "Year":         [2019,2020,2021,2022,2023,2024],
464|    "Visitors (M)":[100, 41,  63,  93,  106, 115],
465|    "Target 2030": [150]*6,
466|})
467|
468|emp_df = pd.DataFrame({
469|    "Year":          HIST_YEARS,
470|    "Female Emp %":  [17,18,20,23,25,27,30,32,34],
471|    "Target (30%)":  [30]*9,
472|})
473|
474|ai_df = pd.DataFrame({
475|    "Initiative":     ["HUMAIN (PIF)","Nvidia Deal","AWS Saudi",
476|                       "Google Cloud","Microsoft"],
477|    "Amount (USD B)": [100.0,14.9,5.3,1.0,1.5],
478|    "Category":       ["Sovereign AI","AI Hardware","Cloud Infra",
479|                       "Cloud Infra","Cloud Infra"],
480|})
481|
482|sectors_df = pd.DataFrame({
483|    "Sector":              ["Tourism","Technology","Healthcare",
484|                            "Entertainment","Mining","Logistics"],
485|    "Investment (SAR B)":  [134,89,67,45,38,29],
486|    "Growth %":            [38, 24,19, 31,15,22],
487|    "Jobs Created (000s)": [250,180,120,95, 60,75],
488|})
489|
490|digital_df = pd.DataFrame({
491|    "Year":              HIST_YEARS,
492|    "Digital Pay %":     [31,38,45,52,60,67,72,77,79],
493|    "E-Commerce (SAR B)":[12,15,19,25,32,45,58,71,85],
494|})
495|
496|giga_df = pd.DataFrame({
497|    "Project":    ["NEOM","The Line","Qiddiya","Red Sea","ROSHN"],
498|    "Budget($B)": [500,200,8,28,20],
499|    "Status":     ["In Progress","Construction","Phase 1","Open","Ongoing"],
500|    "Focus":      ["Smart City AI","Urban Living","Entertainment",
501|                   "Eco Tourism","National Housing"],
502|})
503|
504|# ML Forecasts
505|non_oil_fore  = ml_forecast(HIST_YEARS, gdp_df["Non-Oil GDP %"].tolist(), FORE_YEARS)
506|oil_fore      = ml_forecast(HIST_YEARS, gdp_df["Oil GDP %"].tolist(), FORE_YEARS)
507|female_fore   = ml_forecast(HIST_YEARS, emp_df["Female Emp %"].tolist(), FORE_YEARS)
508|digital_fore  = ml_forecast(HIST_YEARS, digital_df["Digital Pay %"].tolist(), FORE_YEARS)
509|tourism_fore  = ml_forecast(
510|    tourism_df["Year"].tolist(),
511|    tourism_df["Visitors (M)"].tolist(),
512|    FORE_YEARS
513|)
514|
515|# ══════════════════════════════════════════════════════════════
516|# SIDEBAR
517|# ══════════════════════════════════════════════════════════════
518|with st.sidebar:
519|    st.markdown(LOGO_SVG, unsafe_allow_html=True)
520|    st.markdown("<br>", unsafe_allow_html=True)
521|
522|    st.markdown('<p class="sec-label">Audience View | نوع المستخدم</p>',
523|                unsafe_allow_html=True)
524|    view_mode = st.radio(
525|        "View:",
526|        ["🏛️ Government & Policy",
527|         "💼 HR & Talent Acquisition",
528|         "📊 Investors & Analysts",
529|         "👥 Public / General"],
530|        label_visibility="collapsed"
531|    )
532|    st.divider()
533|
534|    # ── LEAD CAPTURE ──
535|    st.markdown("""
536|    <div style="background:linear-gradient(135deg,#F0FDF6,#E6F7EE);
537|                border:1.5px solid #BBF7D0; border-radius:12px;
538|                padding:1rem; margin-bottom:10px;">
539|        <p style="font-size:12px; font-weight:800; color:#004D26;
540|                   margin:0 0 4px; text-transform:uppercase;
541|                   letter-spacing:0.8px;">
542|            📩 Subscribe to Saudi Insights
543|        </p>
544|        <p style="font-size:11px; color:#5A7080; margin:0 0 8px;
545|                   font-family:'IBM Plex Sans Arabic',sans-serif;
546|                   word-wrap:break-word;">
547|            اشترك للحصول على تقارير رؤية 2030
548|        </p>
549|    </div>
550|    """, unsafe_allow_html=True)
551|    
552|    email_input = st.text_input(
553|        "Your Email Address",
554|        placeholder="name@company.com",
555|        label_visibility="collapsed"
556|    )
557|    
558|    if st.button("✉️  Subscribe — Free Weekly Brief", use_container_width=True):
559|        if email_input and "@" in email_input:
560|            st.success(f"✅ Subscribed! We'll send V2030 intelligence to {email_input}")
561|        else:
562|            st.warning("⚠️ Please enter a valid email address.")
563|    
564|    st.divider()
565|
566|    # ── B2B CONSULTING ──
567|    st.markdown("""
568|    <div style="background:linear-gradient(135deg,#FFFBEB,#FEF3C7);
569|                border:1.5px solid #D4A017; border-radius:12px;
570|                padding:1rem; margin-bottom:10px;">
571|        <p style="font-size:12px; font-weight:800; color:#92400E;
572|                   margin:0 0 6px; text-transform:uppercase;
573|                   letter-spacing:0.7px;">
574|            💼 Enterprise Consulting
575|        </p>
576|        <p style="font-size:11.5px; color:#334155; line-height:1.6; 
577|                   margin:0 0 8px; word-wrap:break-word;">
578|            Need custom <b>Saudi market intelligence</b>,
579|            data pipelines, or bilingual AI dashboards for
580|            your Vision 2030 project?
581|        </p>
582|        <p style="font-size:10.5px; color:#5A7080; margin:0 0 8px;
583|                   font-family:'IBM Plex Sans Arabic',sans-serif;
584|                   word-wrap:break-word;">
585|            تحليلات مخصصة للسوق السعودي ورؤية 2030
586|        </p>
587|        <p style="font-size:11.5px; font-weight:700; color:#004D26; 
588|                   margin:0; line-height:1.5; word-wrap:break-word;">
589|            Contact: <b>Mohammad Zaid</b><br>
590|            BCA · Jamia Hamdard<br>
591|            Hafiz-e-Quran · Arabic C1<br>
592|            Google Gen AI APAC 2026
593|        </p>
594|    </div>
595|    """, unsafe_allow_html=True)
596|    
597|    st.markdown("""
598|    <a href="mailto:zaidug987198@gmail.com"
599|       style="display:block; background:linear-gradient(135deg,#D4A017,#F0C040);
600|              color:#1A1000; text-decoration:none; border-radius:10px;
601|              padding:9px 14px; font-size:11.5px; font-weight:800;
602|              text-align:center; margin-bottom:6px; word-wrap:break-word;">
603|        📧 &nbsp;Request Custom Report
604|    </a>
605|    """, unsafe_allow_html=True)
606|    
607|    st.divider()
608|
609|    # ── SYSTEM ──
610|    st.markdown('<p class="sec-label">System Status</p>', unsafe_allow_html=True)
611|    st.success("✅ Data Pipeline: Live")
612|    st.info("🤖 ML Forecasting: Active")
613|    st.caption("📅 Updated: May 2026")
614|    st.divider()
615|
616|    # ── DEVELOPER CARD ──
617|    st.markdown("""
618|    <div style="background:#F0FDF6; border:1.5px solid #BBF7D0;
619|                border-radius:12px; padding:.9rem; margin-bottom:10px;">
620|        <p style="font-size:10px; font-weight:700; color:#004D26;
621|                   margin:0 0 4px; text-transform:uppercase; letter-spacing:0.8px;">
622|            Built by
623|        </p>
624|        <p style="font-size:14px; font-weight:800; color:#0D1F2D; margin:0;">
625|            Mohammad Zaid
626|        </p>
627|        <p style="font-size:10.5px; color:#5A7080; margin:4px 0 0; 
628|                   line-height:1.7; word-wrap:break-word;">
629|            🕌 Hafiz-e-Quran<br>
630|            🗣️ Arabic C1 — DPA Jamia Hamdard<br>
631|            ☁️ Google Gen AI APAC 2026<br>
632|            🎓 BCA — Jamia Hamdard University
633|        </p>
634|    </div>
635|    """, unsafe_allow_html=True)
636|    
637|    st.markdown("""
638|    <a href="https://github.com/zaidug987198-design/v2030-pulse"
639|       target="_blank"
640|       style="display:block; background:#0D1F2D; color:#FFFFFF;
641|              text-decoration:none; border-radius:9px; padding:8px 14px;
642|              font-size:11.5px; font-weight:700; text-align:center;
643|              margin-bottom:6px;">
644|        🐙 &nbsp;GitHub — v2030-pulse
645|    </a>
646|    <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/"
647|       target="_blank"
648|       style="display:block; background:#0A66C2; color:#FFFFFF;
649|              text-decoration:none; border-radius:9px; padding:8px 14px;
650|              font-size:11.5px; font-weight:700; text-align:center;">
651|        💼 &nbsp;LinkedIn Profile
652|    </a>
653|    """, unsafe_allow_html=True)
654|
655|# ══════════════════════════════════════════════════════════════
656|# HEADER - FIXED TEXT OVERLAP
657|# ══════════════════════════════════════════════════════════════
658|st.markdown(f"""
659|<div style="background:linear-gradient(135deg,#003D1E 0%,#005C2E 40%,#007A3D 75%,#00A651 100%);
660|            border-radius:20px; padding:1.75rem 2rem; margin-bottom:1.75rem;
661|            box-shadow:0 10px 40px rgba(0,60,30,0.28);">
662|  <div style="display:flex; align-items:center;
663|              justify-content:space-between; flex-wrap:wrap; gap:20px;">
664|    <div style="display:flex; align-items:center; gap:18px; flex:1; min-width:300px;">
665|      <div style="flex-shrink:0;">{LOGO_SVG}</div>
666|      <div style="flex:1; overflow:hidden;">
667|        <p style="color:rgba(255,255,255,0.60); font-size:10px; font-weight:700;
668|                   letter-spacing:2.5px; margin:0 0 3px; text-transform:uppercase;
669|                   word-wrap:break-word;">
670|          KINGDOM OF SAUDI ARABIA · 2026
671|        </p>
672|        <h1 style="color:#FFFFFF; margin:0; font-size:1.75rem; font-weight:800;
673|                    letter-spacing:-0.5px; line-height:1.3; word-wrap:break-word;">
674|          Vision 2030 Intelligence Hub
675|        </h1>
676|        <p style="color:rgba(255,255,255,0.82); margin:5px 0 0; font-size:13.5px;
677|                   font-family:'IBM Plex Sans Arabic',sans-serif;
678|                   direction:rtl; text-align:right; word-wrap:break-word;">
679|          لوحة تحليلات استراتيجية لرؤية المملكة العربية السعودية 2030
680|        </p>
681|        <p style="color:rgba(255,255,255,0.65); margin:5px 0 0; font-size:11.5px;
682|                   word-wrap:break-word; line-height:1.5;">
683|          National Transformation &amp; Economic Intelligence ·
684|          <span style="background:rgba(212,160,23,0.3); color:#FFE080;
685|                        padding:2px 8px; border-radius:8px; font-size:10.5px;
686|                        font-weight:700; white-space:nowrap;">
687|            🤖 ML Forecasting Active
688|          </span>
689|        </p>
690|      </div>
691|    </div>
692|    <div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">
693|      <span style="background:rgba(255,255,255,0.17); color:#FFFFFF; padding:5px 13px;
694|                    border-radius:20px; font-size:11px; font-weight:600;
695|                    border:1px solid rgba(255,255,255,0.27); white-space:nowrap;">
696|        📊 Live Analytics
697|      </span>
698|      <span style="background:rgba(255,255,255,0.17); color:#FFFFFF; padding:5px 13px;
699|                    border-radius:20px; font-size:11px; font-weight:600;
700|                    border:1px solid rgba(255,255,255,0.27); white-space:nowrap;">
701|        🌍 Global Standards
702|      </span>
703|      <span style="background:rgba(212,160,23,0.32); color:#FFE080; padding:5px 13px;
704|                    border-radius:20px; font-size:11px; font-weight:600;
705|                    border:1px solid rgba(212,160,23,0.42); white-space:nowrap;">
706|        ⭐ Vision 2030 Aligned
707|      </span>
708|    </div>
709|  </div>
710|  
711|  <!-- Arabic KPI Strip - FIXED OVERFLOW -->
712|  <div style="margin-top:1.2rem; padding-top:1rem;
713|              border-top:1px solid rgba(255,255,255,0.16);
714|              display:flex; gap:20px; flex-wrap:wrap; justify-content:center;">
715|    {"".join([f'''
716|    <div style="text-align:center; min-width:80px; max-width:120px; flex:1;">
717|      <p style="color:#FFE080; font-size:1.15rem; font-weight:800; margin:0; 
718|                 word-wrap:break-word; line-height:1.2;">{val}</p>
719|      <p style="color:rgba(255,255,255,0.72); font-size:9px; margin:4px 0 0;
720|                 font-family:'IBM Plex Sans Arabic',sans-serif; 
721|                 word-wrap:break-word; line-height:1.3;">{ar}</p>
722|    </div>''' for val, ar in [
723|        ("50.2%","الناتج غير النفطي"),
724|        ("115M","السياح الدوليون"),
725|        ("33.6%","توظيف المرأة"),
726|        ("$122B","استثمار الذكاء الاصطناعي"),
727|        ("79%","المدفوعات الرقمية"),
728|        ("SAR 134B","إيرادات السياحة"),
729|    ]])}
730|  </div>
731|</div>
732|""", unsafe_allow_html=True)
733|
734|# ══════════════════════════════════════════════════════════════
735|# KPI CARDS - FIXED OVERFLOW
736|# ══════════════════════════════════════════════════════════════
737|st.markdown('<p class="sec-label">مؤشرات الأداء الرئيسية — Key Performance Indicators 2024</p>',
738|            unsafe_allow_html=True)
739|
740|k1,k2,k3,k4,k5,k6 = st.columns(6)
741|k1.metric("Non-Oil GDP غير النفطي",    "50.2%",    "↑ 4.1%  ✅")
742|k2.metric("Tourism Rev السياحة",        "SAR 134B", "↑ 38%")
743|k3.metric("Female Emp توظيف المرأة",   "33.6%",    "↑ 8.2%  ✅")
744|k4.metric("Digital Pay الدفع الرقمي",  "79.0%",    "↑ 22%")
745|k5.metric("AI Investment الذكاء",      "$122.7B",  "↑ HUMAIN")
746|k6.metric("Startups الشركات الناشئة",  "$1.72B",   "↑ 145%")
747|
748|st.divider()
749|
750|# ══════════════════════════════════════════════════════════════
751|# TABS
752|# ══════════════════════════════════════════════════════════════
753|tab1,tab2,tab3,tab4,tab5 = st.tabs([
754|    "📈  Economy | الاقتصاد",
755|    "✈️  Tourism | السياحة",
756|    "🏭  Sectors & Giga",
757|    "👩‍💼  Employment | التوظيف",
758|    "🤖  AI & Tech | الذكاء",
759|])
760|
761|# ══════════════════════════════════════════════════════════════
762|# TAB 1 — ECONOMY
763|# ══════════════════════════════════════════════════════════════
764|with tab1:
765|    st.markdown("""
766|    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
767|               border-right:3px solid #005C2E; font-size:11.5px; color:#5A7080;
768|               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; 
769|               text-align:right; word-wrap:break-word; line-height:1.5;">
770|       التنويع الاقتصادي — نسبة الناتج المحلي النفطي مقابل غير النفطي مع التوقعات حتى 2030
771|    </p>
772|    """, unsafe_allow_html=True)
773|    
774|    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>'
775|                '<span class="ml-badge">📊 Polynomial Regression</span>'
776|                '<span class="ml-badge">Horizon: 2030</span>', unsafe_allow_html=True)
777|    st.markdown("<br>", unsafe_allow_html=True)
778|
779|    col_chart, col_info = st.columns([2.3, 1])
780|    
781|    with col_chart:
782|        fig1 = go.Figure()
783|        
784|        # Historical
785|        fig1.add_trace(go.Scatter(
786|            x=gdp_df["Year"], y=gdp_df["Non-Oil GDP %"],
787|            name="Non-Oil GDP % (Historical)",
788|            mode="lines+markers",
789|            line=dict(color=C["g2"], width=3.5),
790|            marker=dict(size=9, color=C["g2"], line=dict(color=C["white"], width=2.5)),
791|            fill="tozeroy", fillcolor="rgba(0,122,61,0.08)",
792|            hovertemplate="<b>%{x}</b><br>Non-Oil GDP: %{y:.1f}%<extra></extra>",
793|        ))
794|        
795|        fig1.add_trace(go.Scatter(
796|            x=gdp_df["Year"], y=gdp_df["Oil GDP %"],
797|            name="Oil GDP % (Historical)",
798|            mode="lines+markers",
799|            line=dict(color=C["gold"], width=3, dash="dot"),
800|            marker=dict(size=9, color=C["gold"], line=dict(color=C["white"], width=2.5)),
801|            hovertemplate="<b>%{x}</b><br>Oil GDP: %{y:.1f}%<extra></extra>",
802|        ))
803|        
804|        # ML Forecasts
805|        fig1.add_trace(go.Scatter(
806|            x=FORE_YEARS, y=non_oil_fore,
807|            name="Non-Oil GDP % (ML Forecast 2030)",
808|            mode="lines+markers",
809|            line=dict(color=C["g3"], width=2.5, dash="dash"),
810|            marker=dict(size=7, symbol="diamond", color=C["g3"]),
811|            fill="tonexty", fillcolor="rgba(0,166,81,0.04)",
812|            hovertemplate="<b>%{x} (Forecast)</b><br>Non-Oil GDP: %{y:.1f}%<extra></extra>",
813|        ))
814|        
815|        fig1.add_trace(go.Scatter(
816|            x=FORE_YEARS, y=oil_fore,
817|            name="Oil GDP % (ML Forecast 2030)",
818|            mode="lines",
819|            line=dict(color="#F0C040", width=2, dash="dot"),
820|            hovertemplate="<b>%{x} (Forecast)</b><br>Oil GDP: %{y:.1f}%<extra></extra>",
821|        ))
822|        
823|        fig1.add_vline(x=2024.5, line_dash="dot", line_color="#94A3B8",
824|                       annotation_text="  Forecast →", annotation_font_size=11,
825|                       annotation_font_color="#94A3B8")
826|        
827|        fig1.add_hline(y=50, line_dash="dash", line_color=C["red"], line_width=1.5,
828|                       annotation_text="  رؤية 2030 Target: 50% ✅",
829|                       annotation_font_color=C["red"], annotation_font_size=11.5)
830|        
831|        fig1.update_layout(**CL("Oil vs Non-Oil GDP Share (%) + ML Forecast to 2030 | الناتج المحلي", [28,75]))
832|        st.plotly_chart(fig1, use_container_width=True)
833|
834|        r1,r2 = st.columns([3,1])
835|        with r1:
836|            forecast_val = round(non_oil_fore[-1], 1)
837|            st.info(f"🤖 **ML Forecast 2030:** Non-Oil GDP projected at **{forecast_val}%** — "
838|                    f"{'above' if forecast_val >= 50 else 'approaching'} Vision 2030 target.")
839|        with r2:
840|            gdp_export = pd.concat([
841|                gdp_df,
842|                pd.DataFrame({"Year": FORE_YEARS,
843|                              "Non-Oil GDP % (Forecast)": [round(v,2) for v in non_oil_fore],
844|                              "Oil GDP % (Forecast)":     [round(v,2) for v in oil_fore]})
845|            ], ignore_index=True)
846|            st.download_button("📥 Download Dataset",
847|                               data=to_csv(gdp_export),
848|                               file_name="v2030_gdp_forecast.csv",
849|                               mime="text/csv",
850|                               use_container_width=True)
851|
852|    with col_info:
853|        st.markdown("""
854|        <div class="icard">
855|            <h4>📊 Economic Insights | رؤى اقتصادية</h4>
856|            <div class="iitem">
857|                <div class="idot" style="background:#005C2E;"></div>
858|                <p class="itxt"><b>Target Achieved:</b> Non-Oil GDP hit
859|                <b style="color:#005C2E;">50.2%</b> in 2024 — ahead of schedule ✅</p>
860|            </div>
861|            <div class="iitem">
862|                <div class="idot" style="background:#D4A017;"></div>
863|                <p class="itxt"><b>Nitaqat Program:</b> Saudization quotas driving
864|                unemployment below <b>7%</b> — historic low.</p>
865|            </div>
866|            <div class="iitem">
867|                <div class="idot" style="background:#2563EB;"></div>
868|                <p class="itxt"><b>FDI Surge:</b> Foreign Direct Investment
869|                exceeded <b>SAR 100B</b> in 2024.</p>
870|            </div>
871|            <div class="iitem">
872|                <div class="idot" style="background:#DC2626;"></div>
873|                <p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English
874|                AI & Cloud talent is #1 shortage in Saudi tech market.</p>
875|            </div>
876|            <div style="background:#F0FDF6; border-radius:10px; padding:10px 12px;
877|                        margin-top:8px; border:1.5px solid #BBF7D0;">
878|                <p style="margin:0; font-size:12px; font-weight:700; color:#005C2E;">
879|                    ✅ Vision 2030 GDP Target: ACHIEVED
880|                </p>
881|                <div class="pb-wrap">
882|                    <div style="background:linear-gradient(90deg,#005C2E,#00A651);
883|                                 height:10px; width:100%; border-radius:8px;"></div>
884|                </div>
885|                <p style="margin:0; font-size:11px; color:#5A7080;">100.4% complete</p>
886|            </div>
887|            <div style="margin-top:10px; background:#FFFBEB; border-radius:10px;
888|                        padding:10px 12px; border:1px solid #FDE68A;">
889|                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
890|                    📡 Data Sources
891|                </p>
892|                <p style="margin:0; font-size:10.5px; color:#5A7080; word-wrap:break-word;">
893|                    GASTAT · open.data.gov.sa<br>
894|                    vision2030.gov.sa · World Bank
895|                </p>
896|            </div>
897|        </div>
898|        """, unsafe_allow_html=True)
899|
900|    # Digital Economy chart
901|    st.markdown("---")
902|    st.markdown("##### 💳 Digital Economy Growth | نمو الاقتصاد الرقمي")
903|    
904|    dc1, dc2 = st.columns([2.3,1])
905|    
906|    with dc1:
907|        fig_d = go.Figure()
908|        fig_d.add_trace(go.Bar(
909|            x=digital_df["Year"], y=digital_df["Digital Pay %"],
910|            name="Digital Payments %",
911|            marker_color=[C["g1"] if y<=2024 else C["g3"] for y in digital_df["Year"]],
912|            text=digital_df["Digital Pay %"].astype(str)+"%",
913|            textposition="outside",
914|            textfont=dict(color=C["navy"], size=12),
915|        ))
916|        
917|        # Forecast bars
918|        fig_d.add_trace(go.Bar(
919|            x=FORE_YEARS, y=[round(v,1) for v in digital_fore],
920|            name="Digital Payments % (Forecast)",
921|            marker_color="rgba(0,166,81,0.4)",
922|            marker_line=dict(color=C["g3"], width=1.5),
923|            text=[f"{round(v,1)}%*" for v in digital_fore],
924|            textposition="outside",
925|            textfont=dict(color=C["g2"], size=12),
926|        ))
927|        
928|        fig_d.update_layout(**CL("Digital Payments Adoption (%) + ML Forecast | المدفوعات الرقمية", [0,105]))
929|        st.plotly_chart(fig_d, use_container_width=True)
930|        
931|        dc_r1, dc_r2 = st.columns([3,1])
932|        with dc_r1:
933|            st.info(f"🤖 **ML Forecast:** Digital payments projected at "
934|                    f"**{round(digital_fore[-1],1)}%** by 2030 — SAMA Vision target: 80%+")
935|        with dc_r2:
936|            dig_export = pd.concat([
937|                digital_df,
938|                pd.DataFrame({"Year": FORE_YEARS,
939|                              "Digital Pay % (Forecast)": [round(v,2) for v in digital_fore]})
940|            ], ignore_index=True)
941|            st.download_button("📥 Download", to_csv(dig_export),
942|                               "v2030_digital_forecast.csv", "text/csv",
943|                               use_container_width=True)
944|    
945|    with dc2:
946|        st.markdown("""
947|        <div class="icard">
948|            <h4>💳 Digital Economy</h4>
949|            <div class="iitem">
950|                <div class="idot" style="background:#005C2E;"></div>
951|                <p class="itxt"><b>79%</b> digital payment adoption 2024 —
952|                up from just 31% in 2016.</p>
953|            </div>
954|            <div class="iitem">
955|                <div class="idot" style="background:#2563EB;"></div>
956|                <p class="itxt">E-commerce market reached
957|                <b>SAR 85B</b> in 2024 — growing 20%+ YoY.</p>
958|            </div>
959|            <div class="iitem">
960|                <div class="idot" style="background:#D4A017;"></div>
961|                <p class="itxt"><b>STC Pay, stc, Tamara, Foodics</b> —
962|                Saudi fintech unicorns fueling digital growth.</p>
963|            </div>
964|        </div>
965|        """, unsafe_allow_html=True)
966|
967|    # Premium Banner
968|    st.markdown("""
969|    <div class="premium-banner">
970|        <p style="color:#D4A017; font-size:12px; font-weight:800;
971|                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
972|            🔒 Premium Deep-Dive Report Available
973|        </p>
974|        <p style="color:rgba(255,255,255,0.85); font-size:12.5px; margin:0 0 4px;
975|                   word-wrap:break-word; line-height:1.5;">
976|            <b>Saudi Economy Intelligence Report 2026</b> — Full GDP breakdown,
977|            sector analysis, investment forecasts to 2030.
978|        </p>
979|        <p style="color:rgba(255,255,255,0.60); font-size:11.5px; margin:0;
980|                   word-wrap:break-word; line-height:1.5;">
981|            📩 Contact: zaidug987198@gmail.com &nbsp;|&nbsp;
982|            <b style="color:#D4A017;">SAR 500 – 2,000</b> &nbsp;|&nbsp;
983|            Bilingual Arabic–English format available
984|        </p>
985|    </div>
986|    """, unsafe_allow_html=True)
987|
988|# ══════════════════════════════════════════════════════════════
989|# TAB 2 — TOURISM
990|# ══════════════════════════════════════════════════════════════
991|with tab2:
992|    st.markdown("""
993|    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
994|               border-right:3px solid #005C2E; font-size:11.5px; color:#5A7080;
995|               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; 
996|               text-align:right; word-wrap:break-word; line-height:1.5;">
997|       أداء قطاع السياحة مع توقعات ML حتى 2030 · الهدف: 150 مليون زائر سنوياً
998|    </p>
999|    """, unsafe_allow_html=True)
1000|    
1001|    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
1002|    st.markdown("<br>", unsafe_allow_html=True)
1003|
1004|    col_chart, col_info = st.columns([2.3, 1])
1005|    
1006|    with col_chart:
1007|        fig2 = go.Figure()
1008|        fig2.add_trace(go.Bar(
1009|            x=tourism_df["Year"], y=tourism_df["Visitors (M)"],
1010|            name="Actual Visitors (M)",
1011|            marker=dict(
1012|                color=[C["g1"],C["red"],C["gold"],C["g2"],C["g3"],C["g1"]],
1013|                line=dict(color=C["white"], width=1.5)
1014|            ),
1015|            text=tourism_df["Visitors (M)"].astype(str)+"M",
1016|            textposition="outside",
1017|            textfont=dict(color=C["navy"], size=12.5, family="Outfit"),
1018|        ))
1019|        
1020|        fig2.add_trace(go.Bar(
1021|            x=FORE_YEARS, y=[round(v,1) for v in tourism_fore],
1022|            name="Visitors ML Forecast (M)",
1023|            marker=dict(color="rgba(0,166,81,0.35)",
1024|                        line=dict(color=C["g3"], width=1.5)),
1025|            text=[f"{round(v,0):.0f}M*" for v in tourism_fore],
1026|            textposition="outside",
1027|            textfont=dict(color=C["g2"], size=12),
1028|        ))
1029|        
1030|        fig2.add_hline(y=150, line_dash="dash", line_color=C["red"], line_width=2,
1031|                       annotation_text="  2030 Target: 150M visitors",
1032|                       annotation_font_color=C["red"], annotation_font_size=12)
1033|        
1034|        fig2.update_layout(**CL("Tourism Visitors (M) + ML Forecast to 2030 | السياحة", [0,190]))
1035|        st.plotly_chart(fig2, use_container_width=True)
1036|
1037|        tr1, tr2 = st.columns([3,1])
1038|        with tr1:
1039|            proj_2030 = round(tourism_fore[-1], 0)
1040|            target_met = "✅ On track to meet" if proj_2030 >= 140 else "⚠️ May fall short of"
1041|            st.info(f"🤖 **ML Forecast 2030:** {proj_2030:.0f}M visitors projected. "
1042|                    f"{target_met} the 150M Vision 2030 target.")
1043|        with tr2:
1044|            t_export = pd.concat([
1045|                tourism_df,
1046|                pd.DataFrame({"Year": FORE_YEARS,
1047|                              "Visitors (M) Forecast": [round(v,1) for v in tourism_fore],
1048|                              "Target 2030": [150]*6})
1049|            ], ignore_index=True)
1050|            st.download_button("📥 Download", to_csv(t_export),
1051|                               "v2030_tourism_forecast.csv", "text/csv",
1052|                               use_container_width=True)
1053|
1054|    with col_info:
1055|        pct = int((115/150)*100)
1056|        st.markdown(f"""
1057|        <div class="icard">
1058|            <h4>✈️ Tourism | السياحة</h4>
1059|            <div style="text-align:center; margin-bottom:1rem;">
1060|                <p style="font-size:2.8rem; font-weight:800; color:#005C2E;
1061|                           margin:0; line-height:1;">76%</p>
1062|                <p style="font-size:11px; color:#5A7080; margin:3px 0 0; 
1063|                           word-wrap:break-word; line-height:1.4;">
1064|                    of 2030 target reached<br>
1065|                    <span class="ar" style="font-size:10.5px;">76% من الهدف 150 مليون</span>
1066|                </p>
1067|            </div>
1068|            <div class="pb-wrap">
1069|                <div style="background:linear-gradient(90deg,#005C2E,#00A651);
1070|                             height:10px; width:{pct}%; border-radius:8px;"></div>
1071|            </div>
1072|            <div style="display:flex; justify-content:space-between;
1073|                        font-size:11px; color:#5A7080; margin-bottom:1rem;">
1074|                <span>0</span><span><b>115M</b></span><span>150M</span>
1075|            </div>
1076|            <div class="iitem">
1077|                <div class="idot" style="background:#005C2E;"></div>
1078|                <p class="itxt"><b>SAR 134B</b> revenue 2024 — up <b style="color:#005C2E;">38%</b> YoY</p>
1079|            </div>
1080|            <div class="iitem">
1081|                <div class="idot" style="background:#2563EB;"></div>
1082|                <p class="itxt"><b>250,000+</b> new tourism jobs for Saudi nationals</p>
1083|            </div>
1084|            <div class="iitem">
1085|                <div class="idot" style="background:#D4A017;"></div>
1086|                <p class="itxt">NEOM, Red Sea, Qiddiya driving premium international tourism</p>
1087|            </div>
1088|            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
1089|                        margin-top:8px; border:1px solid #FDE68A;">
1090|                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
1091|                    📡 Source: Saudi Tourism Authority
1092|                </p>
1093|                <p style="margin:0; font-size:10.5px; color:#5A7080; word-wrap:break-word;">
1094|                    sta.gov.sa · vision2030.gov.sa
1095|                </p>
1096|            </div>
1097|        </div>
1098|        """, unsafe_allow_html=True)
1099|
1100|    st.markdown("""
1101|    <div class="premium-banner">
1102|        <p style="color:#D4A017; font-size:12px; font-weight:800;
1103|                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
1104|            🔒 Premium Tourism Intelligence Report
1105|        </p>
1106|        <p style="color:rgba(255,255,255,0.85); font-size:12.5px; margin:0 0 4px;
1107|                   word-wrap:break-word; line-height:1.5;">
1108|            Detailed Saudi tourism sector analysis — hotel occupancy,
1109|            source markets, MICE industry, Hajj/Umrah tech opportunities.
1110|        </p>
1111|        <p style="color:rgba(255,255,255,0.60); font-size:11.5px; margin:0;
1112|                   word-wrap:break-word;">
1113|            📩 zaidug987198@gmail.com &nbsp;|&nbsp;
1114|            <b style="color:#D4A017;">SAR 750 – 1,500</b>
1115|        </p>
1116|    </div>
1117|    """, unsafe_allow_html=True)
1118|
1119|# ══════════════════════════════════════════════════════════════
1120|# TAB 3 — SECTORS & GIGA-PROJECTS
1121|# ══════════════════════════════════════════════════════════════
1122|with tab3:
1123|    cp, cb = st.columns(2)
1124|    
1125|    with cp:
1126|        fig3a = px.pie(
1127|            sectors_df, values="Investment (SAR B)", names="Sector",
1128|            title="Investment Distribution | توزيع الاستثمار (SAR B)",
1129|            hole=0.42,
1130|            color_discrete_sequence=[C["g1"],C["g2"],C["g3"],C["gold"],C["b2"],"#8B5CF6"],
1131|        )
1132|        fig3a.update_traces(
1133|            textinfo="percent+label",
1134|            textfont=dict(size=12.5, color=C["navy"], family="Outfit"),
1135|            hovertemplate="<b>%{label}</b><br>SAR %{value}B<br>%{percent}<extra></extra>",
1136|        )
1137|        fig3a.update_layout(**CL(""))
1138|        st.plotly_chart(fig3a, use_container_width=True)
1139|    
1140|    with cb:
1141|        fig3b = px.bar(
1142|            sectors_df.sort_values("Growth %", ascending=True),
1143|            x="Growth %", y="Sector", orientation="h",
1144|            title="YoY Growth Rate | معدل النمو السنوي (%)",
1145|            color="Growth %",
1146|            color_continuous_scale=["#A7F3D0","#007A3D","#004D26"],
1147|            text="Growth %",
1148|        )
1149|        fig3b.update_traces(
1150|            texttemplate="%{text}%", textposition="outside",
1151|            textfont=dict(color=C["navy"], size=12.5, family="Outfit"),
1152|        )
1153|        fig3b.update_layout(**CL(""), coloraxis_showscale=False)
1154|        st.plotly_chart(fig3b, use_container_width=True)
1155|
1156|    sec_r1, sec_r2 = st.columns([3,1])
1157|    with sec_r2:
1158|        st.download_button("📥 Download Sector Data", to_csv(sectors_df),
1159|                           "v2030_sectors.csv", "text/csv", use_container_width=True)
1160|
1161|    # Giga-Projects
1162|    st.markdown('<p class="sec-label" style="margin-top:1rem;">المشاريع العملاقة — Giga-Projects Tracker</p>',
1163|                unsafe_allow_html=True)
1164|    
1165|    gcols = st.columns(5)
1166|    clrs = [C["g1"],C["g2"],C["gold"],C["b2"],C["g3"]]
1167|    
1168|    for i, (_, row) in enumerate(giga_df.iterrows()):
1169|        with gcols[i]:
1170|            st.markdown(f"""
1171|            <div style="background:#FFFFFF; border:1.5px solid #E4EAF2;
1172|                        border-radius:14px; padding:1rem;
1173|                        border-top:4px solid {clrs[i]};
1174|                        box-shadow:0 2px 10px rgba(0,0,0,0.05); text-align:center;">
1175|                <p style="font-size:14px; font-weight:800; color:{clrs[i]}; 
1176|                           margin:0 0 3px; word-wrap:break-word;">
1177|                    {row['Project']}</p>
1178|                <p style="font-size:10.5px; color:#5A7080; margin:0 0 7px; 
1179|                           word-wrap:break-word; line-height:1.4;">
1180|                    {row['Focus']}</p>
1181|                <p style="font-size:1.35rem; font-weight:800; color:#0D1F2D; margin:0 0 5px;">
1182|                    ${row['Budget($B)']}B</p>
1183|                <span style="background:{clrs[i]}18; color:{clrs[i]};
1184|                              font-size:10px; font-weight:700;
1185|                              padding:2px 9px; border-radius:12px; white-space:nowrap;">
1186|                    {row['Status']}</span>
1187|            </div>
1188|            """, unsafe_allow_html=True)
1189|
1190|    # Sector table
1191|    st.markdown("<br>", unsafe_allow_html=True)
1192|    
1193|    rows_html = "".join([f"""
1194|    <tr style="background:{'#F4F7FB' if i%2==0 else '#FFFFFF'}; border-bottom:1px solid #E4EAF2;">
1195|        <td style="padding:11px 16px; color:#0D1F2D; font-weight:600;">{r['Sector']}</td>
1196|        <td style="padding:11px 16px; color:#0D1F2D; font-weight:700; text-align:right;">
1197|            SAR {r['Investment (SAR B)']}B</td>
1198|        <td style="padding:11px 16px; text-align:right;">
1199|            <span style="background:#E6F7EE; color:#005C2E; font-weight:700;
1200|                          padding:3px 10px; border-radius:12px; font-size:12px;">
1201|                ↑ {r['Growth %']}%</span></td>
1202|        <td style="padding:11px 16px; color:#5A7080; text-align:right;">{r['Jobs Created (000s)']}K+</td>
1203|    </tr>""" for i,(_, r) in enumerate(sectors_df.iterrows())])
1204|
1205|    st.markdown(f"""
1206|    <div style="overflow-x:auto;">
1207|    <table style="width:100%; border-collapse:collapse; font-family:Outfit,sans-serif;
1208|                  font-size:13px; background:#FFFFFF; border-radius:12px; overflow:hidden;
1209|                  border:1.5px solid #E4EAF2; box-shadow:0 2px 10px rgba(0,0,0,0.04);">
1210|        <thead>
1211|            <tr style="background:linear-gradient(135deg,#004D26,#007A3D);">
1212|                <th style="padding:12px 16px; color:#FFFFFF; text-align:left; font-weight:700;">
1213|                    Sector | القطاع</th>
1214|                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
1215|                    Investment</th>
1216|                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
1217|                    YoY Growth</th>
1218|                <th style="padding:12px 16px; color:#FFFFFF; text-align:right; font-weight:700;">
1219|                    Jobs Created</th>
1220|            </tr>
1221|        </thead>
1222|        <tbody>{rows_html}</tbody>
1223|    </table>
1224|    </div>
1225|    """, unsafe_allow_html=True)
1226|
1227|# ══════════════════════════════════════════════════════════════
1228|# TAB 4 — EMPLOYMENT
1229|# ══════════════════════════════════════════════════════════════
1230|with tab4:
1231|    st.markdown("""
1232|    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
1233|               border-right:3px solid #005C2E; font-size:11.5px; color:#5A7080;
1234|               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; 
1235|               text-align:right; word-wrap:break-word; line-height:1.5;">
1236|       مشاركة المرأة في سوق العمل + توقعات ML حتى 2030 · هدف رؤية 2030: 30% · تم تجاوزه ✅
1237|    </p>
1238|    """, unsafe_allow_html=True)
1239|    
1240|    st.markdown('<span class="ml-badge">🤖 ML Forecast Active</span>', unsafe_allow_html=True)
1241|    st.markdown("<br>", unsafe_allow_html=True)
1242|
1243|    col_chart, col_info = st.columns([2.3, 1])
1244|    
1245|    with col_chart:
1246|        fig4 = go.Figure()
1247|        fig4.add_trace(go.Scatter(
1248|            x=emp_df["Year"], y=emp_df["Female Emp %"],
1249|            name="Female Employment % (Historical)",
1250|            mode="lines+markers",
1251|            line=dict(color=C["g2"], width=3.5),
1252|            marker=dict(size=10, color=C["g2"], line=dict(color=C["white"], width=2.5)),
1253|            fill="tozeroy", fillcolor="rgba(0,122,61,0.08)",
1254|        ))
1255|        
1256|        fig4.add_trace(go.Scatter(
1257|            x=FORE_YEARS, y=[round(v,1) for v in female_fore],
1258|            name="Female Emp % (ML Forecast)",
1259|            mode="lines+markers",
1260|            line=dict(color=C["g3"], width=2.5, dash="dash"),
1261|            marker=dict(size=8, symbol="diamond", color=C["g3"],
1262|                        line=dict(color=C["white"], width=2)),
1263|            fill="tonexty", fillcolor="rgba(0,166,81,0.04)",
1264|        ))
1265|        
1266|        fig4.add_hline(y=30, line_dash="dash", line_color=C["red"], line_width=1.5,
1267|                       annotation_text="  رؤية 2030 Target: 30%",
1268|                       annotation_font_color=C["red"], annotation_font_size=11.5)
1269|        
1270|        fig4.add_vline(x=2024.5, line_dash="dot", line_color="#94A3B8",
1271|                       annotation_text="  Forecast →", annotation_font_size=10,
1272|                       annotation_font_color="#94A3B8")
1273|        
1274|        fig4.add_annotation(
1275|            x=2024, y=34.5,
1276|            text="<b>33.6% — Target Exceeded! ✅</b>",
1277|            showarrow=True, arrowhead=2,
1278|            arrowcolor=C["g1"], arrowwidth=2,
1279|            font=dict(color=C["g1"], size=12),
1280|            bgcolor=C["g_pale"], bordercolor=C["g2"], borderwidth=1.5,
1281|        )
1282|        
1283|        fig4.update_layout(**CL("Female Workforce Participation (%) + ML Forecast | توظيف المرأة", [12,48]))
1284|        st.plotly_chart(fig4, use_container_width=True)
1285|
1286|        er1, er2 = st.columns([3,1])
1287|        with er1:
1288|            st.info(f"🤖 **ML Forecast 2030:** Female employment projected at "
1289|                    f"**{round(female_fore[-1],1)}%** by 2030 — "
1290|                    f"well above the 30% Vision target.")
1291|        with er2:
1292|            e_export = pd.concat([
1293|                emp_df,
1294|                pd.DataFrame({"Year": FORE_YEARS,
1295|                              "Female Emp % (Forecast)": [round(v,2) for v in female_fore]})
1296|            ], ignore_index=True)
1297|            st.download_button("📥 Download", to_csv(e_export),
1298|                               "v2030_employment_forecast.csv", "text/csv",
1299|                               use_container_width=True)
1300|
1301|    with col_info:
1302|        st.markdown("""
1303|        <div class="icard">
1304|            <h4>👩‍💼 Employment | التوظيف</h4>
1305|            <div style="background:#F0FDF6; border-radius:12px; padding:1rem;
1306|                        margin-bottom:10px; border:1.5px solid #BBF7D0; text-align:center;">
1307|                <p style="font-size:2.2rem; font-weight:800; color:#005C2E; margin:0;">33.6%</p>
1308|                <p style="font-size:11.5px; color:#5A7080; margin:3px 0 0; 
1309|                           word-wrap:break-word; line-height:1.4;">
1310|                    Female Workforce 2024<br>
1311|                    <b style="color:#005C2E;">30% Target — Exceeded ✅</b><br>
1312|                    <span class="ar" style="font-size:10.5px;">تجاوز الهدف المحدد في رؤية 2030</span>
1313|                </p>
1314|            </div>
1315|            <div class="iitem">
1316|                <div class="idot" style="background:#005C2E;"></div>
1317|                <p class="itxt">From <b>17%</b> in 2016 to <b>33.6%</b> in 2024
1318|                — nearly <b style="color:#005C2E;">doubled</b> in 8 years.</p>
1319|            </div>
1320|            <div class="iitem">
1321|                <div class="idot" style="background:#D4A017;"></div>
1322|                <p class="itxt"><b>Nitaqat Saudization:</b> Mandatory
1323|                localization quotas across all industries.</p>
1324|            </div>
1325|            <div class="iitem">
1326|                <div class="idot" style="background:#2563EB;"></div>
1327|                <p class="itxt"><b>Unemployment:</b> Below 7% —
1328|                lowest in Saudi history.</p>
1329|            </div>
1330|            <div class="iitem">
1331|                <div class="idot" style="background:#8B5CF6;"></div>
1332|                <p class="itxt"><b>HR Demand:</b> Bilingual Arabic-English
1333|                AI talent is the #1 shortage in Vision 2030 companies.</p>
1334|            </div>
1335|            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
1336|                        margin-top:8px; border:1px solid #FDE68A;">
1337|                <p style="margin:0; font-size:11px; font-weight:700; color:#92400E;">
1338|                    📡 Source: GASTAT</p>
1339|                <p style="margin:0; font-size:10.5px; color:#5A7080; word-wrap:break-word;">
1340|                    stats.gov.sa</p>
1341|            </div>
1342|        </div>
1343|        """, unsafe_allow_html=True)
1344|
1345|# ══════════════════════════════════════════════════════════════
1346|# TAB 5 — AI & TECH
1347|# ══════════════════════════════════════════════════════════════
1348|with tab5:
1349|    st.markdown("""
1350|    <p style="background:#F0FDF6; padding:8px 14px; border-radius:8px;
1351|               border-right:3px solid #005C2E; font-size:11.5px; color:#5A7080;
1352|               font-family:'IBM Plex Sans Arabic',sans-serif; direction:rtl; 
1353|               text-align:right; word-wrap:break-word; line-height:1.5;">
1354|       استثمارات المملكة العربية السعودية في الذكاء الاصطناعي والبنية التحتية التقنية — 2025
1355|    </p>
1356|    """, unsafe_allow_html=True)
1357|
1358|    col_chart, col_info = st.columns([2.3, 1])
1359|    
1360|    with col_chart:
1361|        fig5 = go.Figure()
1362|        fig5.add_trace(go.Bar(
1363|            x=ai_df["Initiative"],
1364|            y=ai_df["Amount (USD B)"],
1365|            marker=dict(
1366|                color=[C["g1"],C["gold"],C["b2"],C["b3"],"#8B5CF6"],
1367|                line=dict(color=C["white"], width=2)
1368|            ),
1369|            text=["$"+str(v)+"B" for v in ai_df["Amount (USD B)"]],
1370|            textposition="outside",
1371|            textfont=dict(color=C["navy"], size=13, family="Outfit"),
1372|            hovertemplate="<b>%{x}</b><br>$%{y}B<extra></extra>",
1373|        ))
1374|        fig5.update_layout(
1375|            **CL("Saudi AI & Cloud Investment (USD B) | استثمارات الذكاء الاصطناعي 2025", [0,118]),
1376|            showlegend=False,
1377|        )
1378|        st.plotly_chart(fig5, use_container_width=True)
1379|
1380|        ai_r1, ai_r2 = st.columns([3,1])
1381|        with ai_r1:
1382|            st.info("🤖 Saudi Arabia's **$122.7B total AI investment** in 2025 makes it the "
1383|                    "world's fastest-growing AI market — anchored by HUMAIN's $100B sovereign fund.")
1384|        with ai_r2:
1385|            st.download_button("📥 Download", to_csv(ai_df),
1386|                               "v2030_ai_investment.csv", "text/csv",
1387|                               use_container_width=True)
1388|
1389|    with col_info:
1390|        st.markdown("""
1391|        <div class="icard">
1392|            <h4>🤖 AI & Tech | الذكاء الاصطناعي</h4>
1393|            <div style="background:#F0FDF6; border-radius:10px; padding:10px 12px;
1394|                        margin-bottom:8px; border-left:4px solid #005C2E;">
1395|                <p style="margin:0; font-size:12.5px; font-weight:700; color:#005C2E;
1396|                           word-wrap:break-word;">
1397|                    HUMAIN — $100B</p>
1398|                <p style="margin:0; font-size:11.5px; color:#5A7080; word-wrap:break-word;
1399|                           line-height:1.5;">
1400|                    PIF-backed sovereign AI company.<br>
1401|                    Partners: Nvidia, AMD, AWS, Google<br>
1402|                    <span class="ar" style="font-size:10.5px;">شركة الذكاء الاصطناعي السعودية</span>
1403|                </p>
1404|            </div>
1405|            <div style="background:#FFFBEB; border-radius:10px; padding:10px 12px;
1406|                        margin-bottom:8px; border-left:4px solid #D4A017;">
1407|                <p style="margin:0; font-size:12.5px; font-weight:700; color:#B8860B;
1408|                           word-wrap:break-word;">
1409|                    Nvidia Deal — $14.9B</p>
1410|                <p style="margin:0; font-size:11.5px; color:#5A7080; word-wrap:break-word;
1411|                           line-height:1.5;">
1412|                    Largest-ever GPU deal globally.<br>18,000+ Blackwell AI chips</p>
1413|            </div>
1414|            <div style="background:#EFF6FF; border-radius:10px; padding:10px 12px;
1415|                        margin-bottom:8px; border-left:4px solid #2563EB;">
1416|                <p style="margin:0; font-size:12.5px; font-weight:700; color:#1E40AF;
1417|                           word-wrap:break-word;">
1418|                    AWS + Google + Microsoft</p>
1419|                <p style="margin:0; font-size:11.5px; color:#5A7080; word-wrap:break-word;">
1420|                    $7.8B combined cloud in Saudi Arabia</p>
1421|            </div>
1422|            <div style="background:linear-gradient(135deg,#004D26,#007A3D);
1423|                        border-radius:10px; padding:12px; text-align:center;">
1424|                <p style="color:#FFFFFF; margin:0; font-size:12px; font-weight:700;">
1425|                    🤖 An-Nasir AI</p>
1426|                <p style="color:rgba(255,255,255,0.8); margin:3px 0 0; font-size:10.5px;
1427|                           word-wrap:break-word; line-height:1.5;">
1428|                    Arabic-English AI Agent<br>
1429|                    Vertex AI + ADK · Vision 2030<br>
1430|                    <span class="ar">وكيل ذكاء اصطناعي ثنائي اللغة</span>
1431|                </p>
1432|                <a href="https://github.com/zaidug987198-design/v2030-pulse"
1433|                   target="_blank"
1434|                   style="display:block; background:rgba(255,255,255,0.18);
1435|                          color:#FFFFFF; text-decoration:none; border-radius:7px;
1436|                          padding:5px 10px; font-size:11px; font-weight:700;
1437|                          margin-top:8px; border:1px solid rgba(255,255,255,0.3);">
1438|                    🐙 View on GitHub
1439|                </a>
1440|            </div>
1441|        </div>
1442|        """, unsafe_allow_html=True)
1443|
1444|    st.markdown("""
1445|    <div class="premium-banner">
1446|        <p style="color:#D4A017; font-size:12px; font-weight:800;
1447|                   text-transform:uppercase; letter-spacing:1px; margin:0 0 6px;">
1448|            🔒 Unlock: Saudi AI Market Intelligence Report 2026
1449|        </p>
1450|        <p style="color:rgba(255,255,255,0.85); font-size:12.5px; margin:0 0 4px;
1451|                   word-wrap:break-word; line-height:1.5;">
1452|            Complete Saudi AI ecosystem analysis — HUMAIN deep dive,
1453|            Vision 2030 tech talent gaps, bilingual AI deployment strategies,
1454|            investment landscape for Indian tech companies entering Saudi market.
1455|        </p>
1456|        <p style="color:rgba(255,255,255,0.60); font-size:11.5px; margin:0;
1457|                   word-wrap:break-word; line-height:1.5;">
1458|            📩 zaidug987198@gmail.com &nbsp;|&nbsp;
1459|            <b style="color:#D4A017;">SAR 1,000 – 2,000</b> &nbsp;|&nbsp;
1460|            Arabic + English · Delivered in 5 business days
1461|        </p>
1462|    </div>
1463|    """, unsafe_allow_html=True)
1464|
1465|# ══════════════════════════════════════════════════════════════
1466|# FOOTER - FIXED TEXT OVERFLOW
1467|# ══════════════════════════════════════════════════════════════
1468|st.divider()
1469|
1470|st.markdown(f"""
1471|<div style="background:#FFFFFF; border:1.5px solid #E4EAF2; border-radius:16px;
1472|            padding:1.25rem 1.75rem; display:flex; justify-content:space-between;
1473|            align-items:center; flex-wrap:wrap; gap:20px;
1474|            box-shadow:0 2px 10px rgba(0,0,0,0.04);">
1475|    <div style="display:flex; align-items:center; gap:14px; flex:1; min-width:300px;">
1476|        <div style="flex-shrink:0;">{LOGO_SVG}</div>
1477|        <div style="flex:1; overflow:hidden;">
1478|            <p style="margin:0; font-size:14px; font-weight:800; color:#0D1F2D;
1479|                       word-wrap:break-word;">
1480|                V2030 Intelligence Hub</p>
1481|            <p style="margin:3px 0 0; font-size:11.5px; color:#5A7080;
1482|                       word-wrap:break-word; line-height:1.5;">
1483|                Data: open.data.gov.sa · vision2030.gov.sa · GASTAT · SDAIA · World Bank
1484|            </p>
1485|            <p style="margin:2px 0 0; font-size:10.5px; color:#94A3B8;
1486|                       font-family:'IBM Plex Sans Arabic',sans-serif;
1487|                       word-wrap:break-word; line-height:1.4;">
1488|                جميع البيانات من المصادر الحكومية السعودية الرسمية
1489|            </p>
1490|        </div>
1491|    </div>
1492|    <div style="text-align:right; flex:1; min-width:280px;">
1493|        <p style="margin:0; font-size:13px; font-weight:700; color:#005C2E;
1494|                   word-wrap:break-word;">
1495|            Engineered by Mohammad Zaid</p>
1496|        <p style="margin:2px 0 4px; font-size:11px; color:#5A7080;
1497|                   word-wrap:break-word; line-height:1.5;">
1498|            Hafiz-e-Quran · Arabic C1 · Google Gen AI APAC 2026 · Jamia Hamdard
1499|        </p>
1500|        <div style="display:flex; gap:7px; justify-content:flex-end; flex-wrap:wrap;">
1501|            <a href="https://github.com/zaidug987198-design/v2030-pulse"
1502|               target="_blank"
1503|               style="background:#0D1F2D; color:#FFFFFF; text-decoration:none;
1504|                       border-radius:7px; padding:5px 12px; font-size:11px;
1505|                       font-weight:700; white-space:nowrap;">🐙 GitHub</a>
1506|            <a href="https://www.linkedin.com/in/mohammad-zaid-289368379/"
1507|               target="_blank"
1508|               style="background:#0A66C2; color:#FFFFFF; text-decoration:none;
1509|                       border-radius:7px; padding:5px 12px; font-size:11px;
1510|                       font-weight:700; white-space:nowrap;">💼 LinkedIn</a>
1511|            <a href="mailto:zaidug987198@gmail.com"
1512|               style="background:linear-gradient(135deg,#D4A017,#F0C040);
1513|                       color:#1A1000; text-decoration:none; border-radius:7px;
1514|                       padding:5px 12px; font-size:11px; font-weight:700;
1515|                       white-space:nowrap;">📧 Contact</a>
1516|        </div>
1517|    </div>
1518|</div>
1519|<p style="text-align:center; font-size:10.5px; color:#94A3B8; margin-top:10px;
1520|           word-wrap:break-word; line-height:1.5;">
1521|    © 2026 Mohammad Zaid | Python · Streamlit · Plotly · NumPy ML Forecasting |
1522|    All data sourced from official Saudi government portals
1523|</p>
1524|""", unsafe_allow_html=True)
1525|
[End of file]