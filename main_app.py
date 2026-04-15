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
if 'user_info' not in st.session_state:
    st.session_state.user_info = {"name": "Watanabe San", "role": "Senior Engineer"}

# --- CUSTOM STYLING (Modern Snapcon Theme) ---
st.markdown("""
<style>
    /* Global Styles */
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
        transition: transform 0.2s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    .solution-card:hover { transform: translateY(-5px); border-color: #009639; }
    
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

# --- NAVIGATION LOGIC ---
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- SIDEBAR UI ---
with st.sidebar:
    st.markdown("<p class='sidebar-brand'>SNAPCON</p>", unsafe_allow_html=True)
    st.caption("INDUSTRIAL AI & CONTROL")
    st.markdown("---")
    
    if st.session_state.logged_in:
        st.markdown(f"""
            <div class="status-box">
                <p style='margin:0; font-size: 0.8rem; color: #166534;'>Logged in as:</p>
                <p style='margin:0; font-weight: 700; color: #166534;'>{st.session_state.user_info['name']}</p>
                <p style='margin:0; font-size: 0.75rem; color: #15803d;'>{st.session_state.user_info['role']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Navigation Buttons (Cleaned as per request)
    if st.button("🏠 Home", use_container_width=True):
        go_to("main")
        
    if st.button("📊 My Dashboard", use_container_width=True):
        if st.session_state.logged_in:
            go_to("dashboard")
        else:
            go_to("login")
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.session_state.logged_in:
        if st.button("🚪 Sign Out System", type="secondary", use_container_width=True):
            st.session_state.logged_in = False
            go_to("main")

# --- PAGE ROUTING ---

# 1. LOGIN PAGE (AUTHENTICATION)
if st.session_state.page == "login":
    st.markdown("<div style='max-width: 400px; margin: 0 auto; padding-top: 100px;'>", unsafe_allow_html=True)
    st.subheader("System Authentication")
    st.write("Please enter your credentials to access the dashboard.")
    
    emp_id = st.text_input("Employee ID", placeholder="001")
    token = st.text_input("Access Token", type="password", placeholder="••••")
    
    if st.button("AUTHENTICATE", type="primary", use_container_width=True):
        if emp_id == "001" and token == "123":
            st.session_state.logged_in = True
            go_to("dashboard")
        else:
            st.error("Invalid credentials. Try 001 / 123")
    
    if st.button("Back to Home"):
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
    st.info("💡 รันระบบการมอนิเตอร์แบบ Real-time ของสถานะ Node ทั้งหมดในโรงงาน")
    if st.button("Back to Main Screen"):
        go_to("main")

# 3. MAIN PAGE (HOME)
else:
    # Hero Section
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
        st.markdown("""
            <div class="solution-card">
                <h3>📄 Data Sheets</h3>
                <p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>
                    เข้าถึงข้อมูลทางเทคนิคของอุปกรณ์ทั้งหมดและคู่มือการติดตั้งแบบครบวงจร
                </p>
                <p style='color: #009639; font-weight: 600;'>Download Data Sheet ></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Documents", key="sh1"):
            st.toast("กำลังเตรียมไฟล์ Data Sheet สำหรับดาวน์โหลด...")

    with c2:
        st.markdown("""
            <div class="solution-card">
                <h3>⚙️ Drawings</h3>
                <p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>
                    ตรวจสอบสถานะเครื่องจักรและดาวน์โหลดแผนผังโครงสร้างทางวิศวกรรม (DWG/PDF)
                </p>
                <p style='color: #009639; font-weight: 600;'>Download Drawing ></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Get Drawing", key="sh2"):
            st.toast("กำลังดาวน์โหลดไฟล์ Drawing...")

    with c3:
        st.markdown("""
            <div class="solution-card">
                <h3>🛡️ Catalog</h3>
                <p style='color: #64748B; font-size: 0.9rem; margin-bottom: 20px;'>
                    เลือกชมแค็ตตาล็อกสินค้าล่าสุดเพื่อการอัปเกรดประสิทธิภาพเครื่องจักรในระบบของคุณ
                </p>
                <p style='color: #009639; font-weight: 600;'>Product Catalog ></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Catalog", key="sh3"):
            st.toast("กำลังเปิดหน้า Product Catalog...")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("Auth Server: ID-SEA-01 | SNAPCON Enterprise | System Status: Optimal")
