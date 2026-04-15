import streamlit as st

# ตั้งค่าหน้าจอแบบ Wide และปรับธีมเบื้องต้น
st.set_page_config(
    page_title="Snapcon Enterprise V1.5",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- CSS CUSTOM STYLING ---
st.markdown("""
    <style>
    /* ปรับพื้นหลังและฟอนต์ */
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Sarabun', sans-serif; }
    
    .stApp { background-color: #0d1117; }
    
    /* กล่อง Login */
    .login-container {
        background-color: #161b22;
        padding: 40px;
        border-radius: 24px;
        border: 1px solid #30363d;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        max-width: 450px;
        margin: auto;
        text-align: center;
    }
    
    /* ปรับแต่งปุ่ม */
    .stButton>button {
        border-radius: 12px !important;
        height: 48px !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
    }
    
    /* ปุ่ม Login สีฟ้า */
    div.stButton > button:first-child {
        background-color: #238636 !important;
        color: white !important;
        border: none !important;
    }
    
    /* ปุ่ม Guest สีเทา */
    div.stButton > button:nth-child(2) {
        background-color: #30363d !important;
        color: #adbac7 !important;
        border: 1px solid #444c56 !important;
    }

    /* ซ่อนเมนู Pages ที่ยังไม่ได้ Login ใน Sidebar (ทางเลือก) */
    /* [data-testid="stSidebarNav"] li:nth-child(2) { display: none; } */
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/lightning-bolt.png", width=80)
    st.title("SNAPCON")
    st.markdown("---")
    st.info("📢 ประกาศ: หน้า Contact เปิดให้บุคคลทั่วไปเข้าชมได้แล้ว")
    if st.session_state.logged_in:
        if st.button("🔴 ออกจากระบบ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

# --- MAIN CONTENT ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.logged_in:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # โลโก้แอป
        try:
            st.image("Logo.png", width=150)
        except:
            st.markdown("<h1 style='color:#58a6ff;'>🔌 SNAPCON</h1>", unsafe_allow_html=True)
            
        st.markdown("<h2 style='color:white; margin-bottom:0;'>ยินดีต้อนรับ</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#8b949e;'>กรุณาลงชื่อเข้าใช้เพื่อเข้าสู่ระบบ Monitor</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # ช่องกรอกข้อมูล
        user_input = st.text_input("ชื่อผู้ใช้งาน (Username)", placeholder="กรอกรหัสพนักงาน")
        pass_input = st.text_input("รหัสผ่าน (Password)", type="password", placeholder="••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ปุ่มกด
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("เข้าสู่ระบบ", use_container_width=True):
                if user_input == "001" and pass_input == "123":
                    st.session_state.logged_in = True
                    st.success("กำลังเชื่อมต่อ...")
                    st.rerun()
                else:
                    st.error("ข้อมูลไม่ถูกต้อง")
        
        with btn_col2:
            if st.button("ชมตัวอย่าง (Demo)", use_container_width=True):
                st.session_state.logged_in = True
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ส่วนเสริมด้านล่างกล่อง Login
        st.markdown("<br>", unsafe_allow_html=True)
        st.warning("⚠️ หน้า **Monitor** สงวนสิทธิ์เฉพาะเจ้าหน้าที่เท่านั้น")
        
        if st.button("📞 ติดต่อฝ่ายเทคนิค (ไม่ต้องใช้รหัสผ่าน)"):
            st.switch_page("pages/2_Contact.py")

    else:
        # หน้า Landing หลัง Login สำเร็จ
        st.balloons()
        st.markdown("""
            <div style='text-align:center; padding:50px;'>
                <h1 style='color:#10b981;'>🔓 ปลดล็อคระบบสำเร็จ!</h1>
                <p style='font-size:1.2rem; color:#94a3b8;'>คุณได้รับสิทธิ์ในการเข้าถึงข้อมูล Production ทุก Node แล้ว</p>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("📊 เข้าสู่หน้า Dashboard Monitor", type="primary", use_container_width=True):
                st.switch_page("pages/1_Monitor.py")
        with c2:
            if st.button("📱 ตรวจสอบหน้าการติดต่อ", use_container_width=True):
                st.switch_page("pages/2_Contact.py")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:#444c56; font-size:0.8rem;'>© 2024 Snapcon Automation Solution v1.5 Enterprise Cloud</p>", unsafe_allow_html=True)
