import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURATION ---
st.set_page_config(
    page_title="SNAPCON | Industrial AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CENTRALIZED DATA (SINGLE SOURCE OF TRUTH) ---
if 'plant_data' not in st.session_state:
    st.session_state.plant_data = {
        "oee": 94.2,
        "shift_output": 4500,
        "active_alerts": 3,
        "uptime": 99.9,
        "nodes": [
            {"id": "NODE-01", "status": "Operational", "temp": 42.5, "load": 78},
            {"id": "NODE-02", "status": "Operational", "temp": 38.2, "load": 62},
            {"id": "NODE-03", "status": "Warning", "temp": 56.8, "load": 91},
        ]
    }

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- CUSTOM CSS (MATCHING THE UPLOADED IMAGES) ---
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #061A14 !important;
        color: white !important;
    }
    .sidebar-user-box {
        background-color: #F0FFF4;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #C6F6D5;
        color: #1A365D;
    }
    
    /* Button Styles */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    /* Hero Section */
    .hero-container {
        background: white;
        padding: 40px;
        border-radius: 20px;
        border-bottom: 4px solid #009639;
        margin-bottom: 30px;
    }
    .hero-title { font-size: 3.5rem; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
    .hero-subtitle { color: #4A5568; font-size: 1.2rem; margin-bottom: 25px; }
    
    /* Solution Cards */
    .solution-card {
        background: #F8FAFC;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #EDF2F7;
        height: 100%;
        transition: transform 0.2s;
    }
    .solution-card:hover { transform: translateY(-5px); }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 40px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- SIDEBAR UI (AS PER IMAGE_0B7463.PNG) ---
with st.sidebar:
    st.markdown("<h2 style='color:#00B36E; font-weight:800;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#4FD1C5; font-size:0.8rem; margin-top:-15px;'>INDUSTRIAL AI</p>", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown(f"""
        <div class="sidebar-user-box">
            <small style='color:#718096;'>Logged in as:</small><br>
            <strong style='font-size:1.1rem;'>Watanabe San</strong><br>
            <span style='font-size:0.9rem;'>Senior Engineer</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 HOME", use_container_width=True): nav_to("main")
        if st.button("📊 MY DASHBOARD", use_container_width=True): nav_to("dashboard")
        if st.button("🔌 MONITOR CENTER", use_container_width=True): nav_to("monitor")
        
        st.markdown("---")
        st.caption("Resources")
        if st.button("📞 Contact Support", use_container_width=True): st.toast("Connecting to support...")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            nav_to("main")
    else:
        if st.button("🔑 Login to Access Dashboard", use_container_width=True, type="primary"):
            nav_to("auth")

# --- SHARED METRIC COMPONENT ---
def display_kpis():
    data = st.session_state.plant_data
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='metric-card'><small>OEE PERFORMANCE</small><h2>{data['oee']}%</h2><span style='color:green;'>+1.2%</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><small>SHIFT OUTPUT</small><h2>{data['shift_output']:,}</h2><span style='color:green;'>+420</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><small>ACTIVE ALERTS</small><h2>{data['active_alerts']:02d}</h2><span style='color:red;'>-1</span></div>", unsafe_allow_html=True)
    with c4:
        st.markdown(f"<div class='metric-card'><small>UPTIME RATIO</small><h2>{data['uptime']}%</h2><span style='color:blue;'>MAX</span></div>", unsafe_allow_html=True)

# --- PAGES ---

# 1. AUTHENTICATION (AS PER IMAGE_15FC0F.PNG)
if st.session_state.page == "auth":
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text-align:center;'><h1 style='color:#00B36E;'>S</h1><h2>SNAPCON</h2><p>ENTERPRISE CONTROL UNIT</p></div>", unsafe_allow_html=True)
            st.markdown("---")
            emp_id = st.text_input("Employee ID", placeholder="Enter ID...")
            token = st.text_input("Access Token", type="password", placeholder="••••••••")
            if st.button("AUTHENTICATE", type="primary", use_container_width=True):
                st.session_state.logged_in = True
                nav_to("dashboard")
            st.button("Back to Home", on_click=lambda: nav_to("main"), use_container_width=True)

# 2. HOME PAGE (AS PER IMAGE_175923.JPG & IMAGE_15FC2C.JPG)
elif st.session_state.page == "main":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Cool running.<br><span style='color:#009639;'>Long life.</span></h1>
            <p class="hero-subtitle">Industrial Automation Solutions for a Greener Future.<br>Optimizing energy efficiency and system longevity.</p>
            <button style='background:#00B36E; color:white; border:none; padding:10px 25px; border-radius:5px; font-weight:bold;'>Find out more</button>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Our Solutions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='solution-card'><h3>📄 Data & Documents</h3><p>เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัลครบวงจร</p></div>", unsafe_allow_html=True)
        st.link_button("Open Data Sheet", "https://drive.google.com/your-datasheet-link", use_container_width=True)
        
    with col2:
        st.markdown("<div class='solution-card'><h3>⚙️ Product Status</h3><p>ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และแจ้งเตือนการซ่อมบำรุงแบบ Real-time</p></div>", unsafe_allow_html=True)
        if st.button("Go to Monitor", use_container_width=True): nav_to("monitor")
        
    with col3:
        st.markdown("<div class='solution-card'><h3>🛡️ Quality Control</h3><p>วิเคราะห์รายงานคุณภาพและการใช้พลังงาน เพื่อลดคาร์บอนฟุตพริ้นท์ตามมาตรฐานสากล</p></div>", unsafe_allow_html=True)
        st.link_button("Product Catalog", "https://drive.google.com/your-catalog-link", use_container_width=True)

# 3. DASHBOARD PAGE
elif st.session_state.page == "dashboard":
    st.title("Plant Telemetry")
    st.caption("Control Center / General View")
    display_kpis()
    
    st.markdown("### Efficiency Trend")
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Output', 'Target']))

# 4. MONITOR PAGE
elif st.session_state.page == "monitor":
    st.title("Node Status Monitor")
    display_kpis()
    
    st.markdown("---")
    for node in st.session_state.plant_data['nodes']:
        with st.expander(f"📍 {node['id']} - {node['status']}"):
            c1, c2, c3 = st.columns(3)
            c1.metric("Temperature", f"{node['temp']} °C")
            c2.metric("System Load", f"{node['load']}%")
            c3.markdown(f"**Health Score:** {'Good' if node['load'] < 80 else 'Attention Required'}")
