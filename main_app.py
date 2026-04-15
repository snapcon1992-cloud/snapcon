import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="SNAPCON | Enterprise Control Unit",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "login" # 'login' or 'register'
if 'user_db' not in st.session_state:
    # เริ่มต้นด้วย User ตัวอย่าง (Employee ID: 001, Token: 123)
    st.session_state.user_db = {"001": {"token": "123", "name": "Watanabe San", "role": "Senior Engineer"}}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .stApp { background-color: #FFFFFF; }
    
    /* Hero Section */
    .hero-box {
        background-color: #F8FAFC;
        padding: 80px 60px;
        border-radius: 0 0 40px 40px;
        border-bottom: 5px solid #009639;
        margin-bottom: 40px;
    }
    .hero-title { font-size: 3.8rem; font-weight: 800; line-height: 1.1; color: #1A202C; }
    .hero-highlight { color: #009639; }
    
    /* Solution Cards */
    .solution-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        height: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #F8FAFC !important; border-right: 1px solid #E2E8F0; }
    .sidebar-brand { color: #009639; font-weight: 800; font-size: 1.5rem; margin-bottom: 0; }
    
    /* Status Box */
    .status-box {
        background-color: #F0FDF4;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #BBF7D0;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def toggle_auth(mode):
    st.session_state.auth_mode = mode
    st.rerun()

# --- SIDEBAR UI ---
with st.sidebar:
    st.markdown("<p class='sidebar-brand'>SNAPCON</p>", unsafe_allow_html=True)
    st.caption("INDUSTRIAL AI & CONTROL")
    st.markdown("---")
    
    if st.session_state.logged_in and st.session_state.current_user:
        u = st.session_state.current_user
        st.markdown(f"""
            <div class="status-box">
                <p style='margin:0; font-size: 0.8rem; color: #166534;'>Logged in as:</p>
                <p style='margin:0; font-weight: 700; color: #166534;'>{u['name']}</p>
                <p style='margin:0; font-size: 0.75rem; color: #15803d;'>{u['role']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    if st.button("🏠 Home", use_container_width=True):
        go_to("main")
        
    if st.button("📊 My Dashboard", use_container_width=True):
        if st.session_state.logged_in:
            go_to("dashboard")
        else:
            st.session_state.auth_mode = "login"
            go_to("auth")
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.session_state.logged_in:
        if st.button("🚪 Sign Out System", type="secondary", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            go_to("main")

# --- PAGE ROUTING ---

# 1. AUTHENTICATION PAGE (LOGIN & REGISTER)
if st.session_state.page == "auth":
    st.markdown("<div style='max-width: 450px; margin: 0 auto; padding-top: 50px;'>", unsafe_allow_html=True)
    
    if st.session_state.auth_mode == "login":
        st.title("Sign In")
        st.write("Access the SNAPCON Enterprise Dashboard")
        
        login_id = st.text_input("Employee ID", placeholder="e.g. 001")
        login_token = st.text_input("Access Token", type="password")
        
        if st.button("SIGN IN", type="primary", use_container_width=True):
            if login_id in st.session_state.user_db and st.session_state.user_db[login_id]['token'] == login_token:
                st.session_state.logged_in = True
                st.session_state.current_user = st.session_state.user_db[login_id]
                go_to("dashboard")
            else:
                st.error("Invalid credentials. Please check your ID and Token.")
        
        st.markdown("---")
        st.write("New to SNAPCON?")
        if st.button("Create New Account", use_container_width=True):
            toggle_auth("register")

    else: # REGISTER MODE
        st.title("Register")
        st.write("Create your enterprise access account")
        
        reg_id = st.text_input("Employee ID (Unique)", placeholder="e.g. 002")
        reg_name = st.text_input("Full Name", placeholder="e.g. John Doe")
        reg_role = st.selectbox("Role", ["Senior Engineer", "Maintenance", "Operator", "Manager"])
        reg_token = st.text_input("Set Access Token", type="password")
        
        if st.button("REGISTER NOW", type="primary", use_container_width=True):
            if not reg_id or not reg_name or not reg_token:
                st.warning("Please fill in all fields.")
            elif reg_id in st.session_state.user_db:
                st.error("This Employee ID is already registered.")
            else:
                # Save to memory (Session)
                st.session_state.user_db[reg_id] = {
                    "token": reg_token,
                    "name": reg_name,
                    "role": reg_role
                }
                st.success("Account created successfully!")
                st.session_state.auth_mode = "login"
                st.rerun()
        
        if st.button("Already have an account? Sign In", use_container_width=True):
            toggle_auth("login")
            
    if st.button("← Back to Home"):
        go_to("main")
    st.markdown("</div>", unsafe_allow_html=True)

# 2. DASHBOARD PAGE
elif st.session_state.page == "dashboard":
    st.title("Plant Telemetry")
    st.caption("CONTROL CENTER / GENERAL VIEW")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("OEE PERFORMANCE", "94.2%", "+1.2%")
    m2.metric("SHIFT OUTPUT", "4,500", "+420")
    m3.metric("ACTIVE ALERTS", "03", "-1", delta_color="inverse")
    m4.metric("UPTIME RATIO", "99.9%", "MAX")
    
    st.markdown("---")
    st.subheader("Active Nodes Monitor")
    st.info("💡 ระบบกำลังรวบรวมข้อมูล Real-time จาก Edge Computing Gateway ทั้งหมดในพื้นที่ A1")
    
    if st.button("Back to Main Screen"):
        go_to("main")

# 3. MAIN PAGE (HOME)
else:
    st.markdown("""
        <div class="hero-box">
            <h1 class="hero-title">Cool running.<br><span class="hero-highlight">Long life.</span></h1>
            <p style='color: #64748B; font-size: 1.1rem; margin-top: 25px; max-width: 600px;'>
                Industrial Automation Solutions for a Greener Future.<br>
                Optimizing energy efficiency and system longevity.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Our Solutions")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""<div class="solution-card"><h3>📄 Data Sheets</h3><p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>เข้าถึงข้อมูลทางเทคนิคของอุปกรณ์ทั้งหมดและคู่มือการติดตั้งแบบครบวงจร</p><p style='color: #009639; font-weight: 600;'>Download Data Sheet ></p></div>""", unsafe_allow_html=True)
        if st.button("Open Documents", key="sh1"): st.toast("เตรียมไฟล์ Data Sheet...")

    with c2:
        st.markdown("""<div class="solution-card"><h3>⚙️ Drawings</h3><p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>ตรวจสอบสถานะเครื่องจักรและดาวน์โหลดแผนผังโครงสร้างทางวิศวกรรม (DWG/PDF)</p><p style='color: #009639; font-weight: 600;'>Download Drawing ></p></div>""", unsafe_allow_html=True)
        if st.button("Get Drawing", key="sh2"): st.toast("ดาวน์โหลดไฟล์ Drawing...")

    with c3:
        st.markdown("""<div class="solution-card"><h3>🛡️ Catalog</h3><p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>เลือกชมแค็ตตาล็อกสินค้าล่าสุดเพื่อการอัปเกรดประสิทธิภาพเครื่องจักรในระบบของคุณ</p><p style='color: #009639; font-weight: 600;'>Product Catalog ></p></div>""", unsafe_allow_html=True)
        if st.button("View Catalog", key="sh3"): st.toast("เปิด Product Catalog...")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("Auth Server: ID-SEA-01 | SNAPCON Enterprise | System Status: Optimal")
