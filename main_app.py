import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="SNAPCON | Automation Solution",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Centralized State Management (แหล่งข้อมูลเดียวที่สอดคล้องกัน)
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_db' not in st.session_state:
    st.session_state.user_db = {"001": {"pass": "123", "name": "Watanabe San", "role": "Senior Engineer"}}

# ข้อมูล Monitor ที่เชื่อมโยงกับ Dashboard
if 'plant_metrics' not in st.session_state:
    st.session_state.plant_metrics = {
        "oee": 94.2,
        "output": 4500,
        "alerts": 3,
        "uptime": 99.9
    }

# 3. Custom CSS (SNAPCON Dark Theme & Modern Layout)
st.markdown("""
<style>
    /* Sidebar styling: Dark Green/Black theme */
    section[data-testid="stSidebar"] {
        background-color: #061A14 !important;
        color: white !important;
    }
    .st-emotion-cache-6qob1r { background-color: transparent !important; }
    
    /* User Profile Box in Sidebar */
    .user-profile-card {
        background-color: #F0FFF4;
        padding: 15px;
        border-radius: 10px;
        color: #1A365D;
        border: 1px solid #C6F6D5;
        margin-bottom: 20px;
    }
    
    /* Hero Banner Styling */
    .hero-banner {
        background: white;
        padding: 60px;
        border-radius: 20px;
        border-bottom: 5px solid #009639;
        margin-bottom: 30px;
    }
    
    /* Solution Cards */
    .sol-card {
        background: #F8FAFC;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        height: 100%;
        transition: 0.3s;
    }
    .sol-card:hover { transform: translateY(-5px); border-color: #009639; }

    /* Metric Cards */
    .metric-item {
        background: white;
        padding: 30px;
        border-radius: 40px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 4. Navigation Helper
def switch_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 5. --- SIDEBAR (Clean & Functional as per image_15fc2c.jpg) ---
with st.sidebar:
    st.markdown("<h2 style='color:#00B36E; font-weight:800; margin-bottom:0;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#4FD1C5; font-size:0.8rem; margin-top:-5px;'>AUTOMATION SOLUTION</p>", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        # Profile Section
        st.markdown(f"""
        <div class="user-profile-card">
            <small>Logged in as:</small><br>
            <strong style="font-size:1.1rem;">{st.session_state.user_db['001']['name']}</strong><br>
            <span style="font-size:0.85rem; color:#2F855A;">{st.session_state.user_db['001']['role']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Buttons (ลบปุ่ม Home ซ้ำซ้อนและ Start/Stop ออกตามภาพ image_175923.jpg)
        if st.button("🏠 Home", use_container_width=True): switch_to("main")
        if st.button("📊 My Dashboard", use_container_width=True): switch_to("dashboard")
        
        st.markdown("---")
        # Contact Support เข้าได้เลยไม่ต้อง Login
        if st.button("📞 Contact Support", use_container_width=True):
            st.toast("Redirecting to support center...")
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("🚪 SIGN OUT SYSTEM", use_container_width=True):
            st.session_state.logged_in = False
            switch_to("main")
    else:
        st.info("Please login to access secure features.")

# 6. --- PAGE ROUTING ---

# PAGE: AUTHENTICATION (Login / Register Card)
if st.session_state.page == "auth":
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div style='text-align:center;'><h1 style='color:#00B36E; margin-bottom:0;'>S</h1><h2 style='margin-top:0;'>SNAPCON</h2><p style='color:#718096;'>ENTERPRISE CONTROL UNIT</p></div>", unsafe_allow_html=True)
            st.markdown("---")
            uid = st.text_input("Employee ID", placeholder="001")
            upass = st.text_input("Access Token", type="password", placeholder="••••")
            
            if st.button("AUTHENTICATE", type="primary", use_container_width=True):
                if uid == "001" and upass == "123":
                    st.session_state.logged_in = True
                    switch_to("dashboard")
                else: st.error("Invalid Credentials")
            
            if st.button("Register New User", use_container_width=True):
                st.info("Registration portal is under maintenance.")
            st.button("Back to Home", on_click=lambda: switch_to("main"), use_container_width=True)

# PAGE: MAIN (Home with Google Drive Links)
elif st.session_state.page == "main":
    # Header area with Login inputs (image_184225.jpg)
    if not st.session_state.logged_in:
        h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([4, 1, 1, 1, 1])
        with h_col2: st.caption("Login ID:")
        with h_col3: login_id = st.text_input("", label_visibility="collapsed", key="top_id")
        with h_col4: st.caption("Pass:")
        with h_col5: login_pw = st.text_input("", type="password", label_visibility="collapsed", key="top_pw")
    
    # Hero Banner (image_15eca7.jpg)
    st.markdown("""
    <div class="hero-banner">
        <h1 style='font-size: 3.5rem; font-weight: 800; line-height: 1.1;'>Cool running.<br><span style='color:#009639;'>Long life.</span></h1>
        <p style='color:#4A5568; font-size: 1.2rem; margin-top:20px;'>
            Industrial Automation Solutions for a Greener Future.<br>
            Optimizing energy efficiency and system longevity.
        </p>
        <button style='background:#00B36E; color:white; border:none; padding:12px 30px; border-radius:8px; font-weight:bold; cursor:pointer;'>Find out more</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Solutions Section with Actual Drive Links (image_17ccae.png)
    st.subheader("Our Solutions")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='sol-card'><h3>📄 Data & Documents</h3><p>เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัลครบวงจร</p></div>", unsafe_allow_html=True)
        st.link_button("Download Data Sheet", "https://drive.google.com/...", use_container_width=True)
        
    with c2:
        st.markdown("<div class='sol-card'><h3>⚙️ Product Status</h3><p>ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และแจ้งเตือนการซ่อมบำรุงแบบ Real-time</p></div>", unsafe_allow_html=True)
        if st.button("Go to Monitor", use_container_width=True): switch_to("monitor")
        
    with c3:
        st.markdown("<div class='sol-card'><h3>🛡️ Quality Control</h3><p>วิเคราะห์รายงานคุณภาพและการใช้พลังงาน เพื่อลดคาร์บอนฟุตพริ้นท์ตามมาตรฐานสากล</p></div>", unsafe_allow_html=True)
        st.link_button("Product Catalog", "https://drive.google.com/...", use_container_width=True)

# PAGE: DASHBOARD & MONITOR (Shared Metrics)
elif st.session_state.page in ["dashboard", "monitor"]:
    st.title("Plant Intelligence")
    st.caption("CONTROL CENTER / REAL-TIME DATA SYNC")
    
    # Metrics (Shared Source)
    m = st.session_state.plant_metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f"<div class='metric-item'><small>OEE PERFORMANCE</small><h2>{m['oee']}%</h2><span style='color:green;'>+1.2%</span></div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='metric-item'><small>SHIFT OUTPUT</small><h2>{m['output']:,}</h2><span style='color:green;'>+420</span></div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='metric-item'><small>ACTIVE ALERTS</small><h2>{m['alerts']:02d}</h2><span style='color:red;'>-1</span></div>", unsafe_allow_html=True)
    with col4: st.markdown(f"<div class='metric-item'><small>UPTIME RATIO</small><h2>{m['uptime']}%</h2><span style='color:blue;'>MAX</span></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    if st.session_state.page == "dashboard":
        st.subheader("Efficiency Trends")
        st.area_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Line A', 'Line B']))
    else:
        st.subheader("Edge Node Monitor")
        st.info("Connected to 4 Active Nodes in Production Area A.")

    if st.button("← Back to Home"): switch_to("main")

# Footer
st.markdown("<br><hr><center><small style='color:#94A3B8;'>Auth Server: ID-SEA-01 | SNAPCON Automation Solution | 2026</small></center>", unsafe_allow_html=True)
