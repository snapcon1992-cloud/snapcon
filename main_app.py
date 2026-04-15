import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION ---
st.set_page_config(
    page_title="SNAPCON | Shared Intelligence Unit",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CENTRALIZED DATA ENGINE (SHARED SOURCE) ---
# ฟังก์ชันนี้จำลองการดึงข้อมูลจาก Edge Gateway เพื่อให้ทุกหน้าเห็นข้อมูลตรงกัน
if 'plant_data' not in st.session_state:
    st.session_state.plant_data = {
        "oee": 94.2,
        "shift_output": 4580,
        "active_alerts": 2,
        "uptime": 99.8,
        "nodes": [
            {"id": "NODE-A1", "status": "Online", "temp": 42.5, "load": 78},
            {"id": "NODE-A2", "status": "Online", "temp": 38.2, "load": 62},
            {"id": "NODE-B1", "status": "Offline", "temp": 0.0, "load": 0},
            {"id": "NODE-C3", "status": "Warning", "temp": 56.8, "load": 91},
        ]
    }

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "login"
if 'user_db' not in st.session_state:
    st.session_state.user_db = {"001": {"token": "123", "name": "Watanabe San", "role": "Senior Engineer"}}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #FFFFFF; }
    
    .hero-box {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
        padding: 60px;
        border-radius: 0 0 40px 40px;
        border-bottom: 5px solid #009639;
        margin-bottom: 30px;
    }
    .hero-title { font-size: 3.2rem; font-weight: 800; color: #1A202C; margin:0; }
    .hero-highlight { color: #009639; }
    
    .solution-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        height: 100%;
    }
    
    section[data-testid="stSidebar"] { background-color: #F8FAFC !important; }
    .status-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-online { background: #DCFCE7; color: #166534; }
    .badge-offline { background: #FEE2E2; color: #991B1B; }
    .badge-warning { background: #FEF3C7; color: #92400E; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def toggle_auth(mode):
    st.session_state.auth_mode = mode
    st.rerun()

# --- REUSABLE COMPONENTS ---
def render_kpi_metrics():
    """แสดงค่า KPI หลักที่ใช้ร่วมกันทุกหน้า"""
    data = st.session_state.plant_data
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("OEE Performance", f"{data['oee']}%", "Stable")
    c2.metric("Shift Output", f"{data['shift_output']:,}", "+120")
    c3.metric("Critical Alerts", f"0{data['active_alerts']}", "-1", delta_color="inverse")
    c4.metric("System Uptime", f"{data['uptime']}%", "Optimal")

# --- SIDEBAR UI ---
with st.sidebar:
    st.markdown("<h2 style='color:#009639; margin-bottom:0;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.caption("INTELLIGENT CONTROL UNIT")
    st.markdown("---")
    
    if st.session_state.logged_in:
        u = st.session_state.current_user
        st.success(f"**{u['name']}**\n\n{u['role']}")
        if st.button("📊 My Dashboard", use_container_width=True): go_to("dashboard")
        if st.button("🔌 Monitor Center", use_container_width=True): go_to("monitor")
    else:
        if st.button("🔑 Login to System", use_container_width=True, type="primary"): 
            st.session_state.auth_mode = "login"
            go_to("auth")

    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): go_to("main")
    
    if st.session_state.logged_in:
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            go_to("main")

# --- PAGES ---

# 1. AUTH PAGE
if st.session_state.page == "auth":
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.session_state.auth_mode == "login":
            st.title("Sign In")
            uid = st.text_input("Employee ID")
            utoken = st.text_input("Token", type="password")
            if st.button("Login", type="primary", use_container_width=True):
                if uid in st.session_state.user_db and st.session_state.user_db[uid]['token'] == utoken:
                    st.session_state.logged_in = True
                    st.session_state.current_user = st.session_state.user_db[uid]
                    go_to("dashboard")
                else: st.error("Access Denied")
            st.button("New User? Register here", on_click=lambda: toggle_auth("register"))
        else:
            st.title("Register")
            rid = st.text_input("New Employee ID")
            rname = st.text_input("Full Name")
            rrole = st.selectbox("Role", ["Engineer", "Operator", "Manager"])
            rtoken = st.text_input("Create Token", type="password")
            if st.button("Create Account", type="primary", use_container_width=True):
                st.session_state.user_db[rid] = {"token": rtoken, "name": rname, "role": rrole}
                st.success("Registered!")
                toggle_auth("login")
            st.button("Back to Login", on_click=lambda: toggle_auth("login"))

# 2. DASHBOARD PAGE (Internal Overview)
elif st.session_state.page == "dashboard":
    st.title(f"Welcome, {st.session_state.current_user['name']}")
    st.subheader("Enterprise Performance Overview")
    
    # ใช้ Metrics ตัวเดียวกัน
    render_kpi_metrics()
    
    st.markdown("### Production Trend")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Line A', 'Line B', 'Line C'])
    st.line_chart(chart_data)

# 3. MONITOR PAGE (Detailed Node View)
elif st.session_state.page == "monitor":
    st.title("Live Node Monitor")
    st.info("Direct synchronization with Edge Computing Gateway")
    
    # ใช้ Metrics ตัวเดียวกันเพื่อให้เห็นภาพรวมก่อนลงรายละเอียด
    render_kpi_metrics()
    
    st.markdown("---")
    nodes = st.session_state.plant_data['nodes']
    
    for node in nodes:
        with st.expander(f"🖥️ {node['id']} - Status: {node['status']}"):
            c1, c2, c3 = st.columns(3)
            c1.write(f"**Temperature:** {node['temp']}°C")
            c2.write(f"**Load Factor:** {node['load']}%")
            state_color = "green" if node['status'] == "Online" else "red" if node['status'] == "Offline" else "orange"
            c3.markdown(f"**Signal:** <span style='color:{state_color}'>● Active</span>", unsafe_allow_html=True)

# 4. MAIN PAGE
else:
    st.markdown(f"""
        <div class="hero-box">
            <h1 class="hero-title">Cloud Monitoring.<br><span class="hero-highlight">Connected Intelligence.</span></h1>
            <p style='color: #64748B; font-size: 1.1rem; margin-top: 20px;'>
                Shared data ecosystem for real-time industrial control.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # แสดง Preview ข้อมูลจริงที่หน้า Home แม้ยังไม่ได้ Login (Public KPI)
    st.subheader("Global Plant Status (Live)")
    render_kpi_metrics()
    
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="solution-card"><h4>Engineering Docs</h4><p>Access technical drawings and node specifications.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="solution-card"><h4>Maintenance Portal</h4><p>Schedule and track hardware health checks.</p></div>""", unsafe_allow_html=True)
