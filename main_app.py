import streamlit as st

# 1. การตั้งค่าหน้าจอเบื้องต้น
st.set_page_config(
    page_title="SNAPCON ",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ตรวจสอบสถานะการเข้าสู่ระบบ
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 3. CSS Custom Design (Premium Look)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@200;400;700&display=swap');
    
    * { font-family: 'Sarabun', sans-serif; }
    
    /* Background & Main Layout */
    .stApp {
        background: radial-gradient(circle at top right, #1a1f2e, #0d1117);
    }
    
    /* Glassmorphism Card */
    .main-card {
        background: rgba(22, 27, 34, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        max-width: 500px;
        margin: auto;
    }
    
    /* Input Styling */
    div[data-baseweb="input"] {
        background-color: rgba(13, 17, 23, 0.6) !important;
        border-radius: 12px !important;
        border: 1px solid #30363d !important;
    }
    
    /* Button Premium Styling */
    .stButton>button {
        border-radius: 14px !important;
        height: 52px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
    }
    
    /* Login Button (Highlight) */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(35, 134, 54, 0.3) !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #30363d !important;
    }
    
    .status-text {
        font-size: 0.85rem;
        color: #8b949e;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    # แสดงโลโก้ใน Sidebar
    try:
        st.image("Logo.png", width=120)
    except:
        st.markdown("<h2 style='color:#58a6ff;'>🔌 SNAPCON</h2>", unsafe_allow_html=True)
    
    st.markdown("### เมนูระบบ")
    
    # เมนูที่แสดงผลตลอดเวลา (Public)
    if st.button("🏠 หน้าแรก / Login", use_container_width=True):
        st.switch_page("main_app.py")
        
    if st.button("📞 ติดต่อฝ่ายเทคนิค (Contact)", use_container_width=True):
        st.switch_page("pages/2_Contact.py")

    st.markdown("---")
    
    # เมนูที่ต้อง Login เท่านั้น
    if st.session_state.logged_in:
        st.success("Log in แล้ว (Admin)")
        if st.button("📊 Monitor Dashboard", type="primary", use_container_width=True):
            st.switch_page("pages/1_Monitor.py")
        if st.button("🔓 ออกจากระบบ", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.warning("🔒 Monitor (ต้องใช้รหัส)")

# 5. MAIN CONTENT
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.logged_in:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        
        # Header Section
        try:
            st.image("Logo.png", width=180)
        except:
            st.markdown("<h1 style='color:white; text-align:center;'>SNAPCON</h1>", unsafe_allow_html=True)
            
        st.markdown("<h2 style='color:white; text-align:center; margin-top:0;'>Enterprise v1.5</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#8b949e; text-align:center;'>ระบบจัดการพลังงานและการผลิตอัจฉริยะ</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Form
        username = st.text_input("Username", placeholder="ระบุชื่อผู้ใช้งาน")
        password = st.text_input("Password", type="password", placeholder="ระบุรหัสผ่าน")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("เข้าสู่ระบบ (Admin Login)", use_container_width=True):
            if username == "001" and password == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        
        st.markdown("<p style='text-align:center; color:#58a6ff; font-size:0.8rem; margin-top:15px; cursor:pointer;'>ลืมรหัสผ่านใช่หรือไม่?</p>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Public Shortcut Below Card
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8b949e;'>หากคุณเป็นบุคคลทั่วไปหรือต้องการขอข้อมูลเพิ่มเติม</p>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            if st.button("📱 ติดต่อสอบถามได้ที่นี่"):
                st.switch_page("pages/2_Contact.py")

    else:
        # แสดงเมื่อ Login แล้ว
        st.balloons()
        st.markdown(f"""
            <div style='text-align:center; background:rgba(35, 134, 54, 0.1); padding:40px; border-radius:24px; border:1px solid #238636;'>
                <h1 style='color:#2ea043;'>ยินดีต้อนรับกลับมา!</h1>
                <p style='color:white; font-size:1.1rem;'>ระบบ SNAPCON พร้อมใช้งานแล้วสำหรับคุณ</p>
                <br>
                <p style='color:#8b949e;'>เลือกเมนูที่ต้องการดำเนินการต่อ</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("📊 เข้าดู Monitor Dashboard", use_container_width=True):
                st.switch_page("pages/1_Monitor.py")
        with col_btn2:
            if st.button("📞 เข้าหน้า Contact", use_container_width=True):
                st.switch_page("pages/2_Contact.py")

# 6. FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#30363d; font-size:0.8rem;'>© 2024 Snapcon Industrial Solution. All Rights Reserved.</p>", unsafe_allow_html=True)
