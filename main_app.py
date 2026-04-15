import streamlit as st

# 1. การตั้งค่าหน้าจอ
st.set_page_config(
    page_title="SNAPCON | Green Automation",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ตรวจสอบสถานะการเข้าสู่ระบบ
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 3. CSS Custom Design (รวมการซ่อนเมนูเดิมและปรับแต่งปุ่ม)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Sarabun:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Roboto', 'Sarabun', sans-serif;
    }
    
    /* ซ่อนเมนูเดิมของ Streamlit ที่อยู่ด้านบน Sidebar */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    .stApp { background-color: #f0f4f0; }
    
    /* Corporate Header */
    .corp-header {
        background-color: #ffffff;
        border-bottom: 4px solid #27ae60;
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* ปุ่มเมนูสีเขียว */
    .stButton>button {
        background-color: #27ae60 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 0.7rem !important;
        font-size: 1.1rem !important;
        margin-bottom: 10px !important;
        width: 100%;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #219150 !important;
        transform: scale(1.02);
    }

    [data-testid="stSidebar"] {
        background-color: #1e272e !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. TOP NAVIGATION BAR
st.markdown("""
    <div class="corp-header">
        <div style="display:flex; align-items:center; gap:15px;">
            <span style="font-size:1.8rem; font-weight:900; color:#27ae60; letter-spacing:-1px;">SNAPCON</span>
            <span style="border-left:1px solid #ddd; padding-left:15px; color:#666; font-size:0.9rem;">Green Technology & Automation</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. SIDEBAR (ปรับปรุงใหม่ตามสั่ง)
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ปุ่ม Main
    if st.button("🏠 Main", use_container_width=True):
        st.switch_page("main_app.py")
    
    # ปุ่ม My Dashboard (เช็คสิทธิ์ก่อนเข้า)
    if st.button("📊 My Dashboard", use_container_width=True):
        if st.session_state.logged_in:
            st.switch_page("pages/1_Monitor.py")
        else:
            st.warning("🔒 กรุณา Login ก่อนเข้าใช้งาน Dashboard")
            
    # ปุ่ม Contact Support
    if st.button("📞 Contact Support", use_container_width=True):
        st.switch_page("pages/2_Contact.py")
    
    st.markdown("---")
    if st.session_state.logged_in:
        st.success("Authorized: Admin")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.info("Technical Portal")

# 6. MAIN CONTENT
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.markdown("""
        <div style="background:white; padding:40px; border-radius:8px; border-left:10px solid #27ae60; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
            <h1 style="font-size:2.5rem; font-weight:900; color:#2c3e50;">Eco-Friendly Engineering.</h1>
            <p style="font-size:1.1rem; color:#7f8c8d;">ระบบควบคุมอัจฉริยะที่ออกแบบมาเพื่อความยั่งยืน</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📂 Technical Resources")
    d1, d2 = st.columns(2)
    with d1:
        if st.button("📐 View Drawing Files"):
            st.write("Opening Drawings...")
    with d2:
        if st.button("📑 Download Data Sheets"):
            st.write("Downloading Specs...")

with col2:
    if not st.session_state.logged_in:
        st.markdown("<div style='background:white; padding:30px; border-radius:8px; border:1px solid #ddd;'>", unsafe_allow_html=True)
        st.subheader("Portal Login")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("LOGIN"):
            if user == "001" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("ข้อมูลไม่ถูกต้อง")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background:#e8f6ef; padding:30px; border-radius:8px; border:1px solid #27ae60;'>", unsafe_allow_html=True)
        st.subheader("Welcome back!")
        st.write("คุณสามารถเข้าใช้งาน My Dashboard ได้ทันทีจากเมนูด้านซ้าย")
        if st.button("Go to My Dashboard"):
            st.switch_page("pages/1_Monitor.py")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#7f8c8d; font-size:0.8rem;'>© 2024 SNAPCON GREEN SOLUTION</p>", unsafe_allow_html=True)
