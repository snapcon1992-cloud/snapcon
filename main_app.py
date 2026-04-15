import streamlit as st

# ตั้งค่าหน้าจอ
st.set_page_config(
    page_title="Snapcon Login",
    page_icon="🔌",
    layout="centered"
)

# --- ตรวจสอบสถานะ Login ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- CSS เพื่อความสวยงาม ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 50px; font-weight: bold; }
    .login-box {
        background-color: #161b22;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #30363d;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- หน้า Login ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    # แสดงโลโก้ (ถ้ามีไฟล์ Logo.png ใน GitHub)
    try:
        st.image("Logo.png", width=120)
    except:
        st.title("🔌 SNAPCON")
    
    st.subheader("Enterprise V1.5 Login")
    
    username = st.text_input("Username", placeholder="ระบุชื่อผู้ใช้งาน")
    password = st.text_input("Password", type="password", placeholder="ระบุรหัสผ่าน")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("เข้าสู่ระบบ (Login)"):
            if username == "001" and password == "123":
                st.session_state.logged_in = True
                st.success("Login สำเร็จ! กำลังไปที่หน้า Monitor...")
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    
    with col2:
        if st.button("Guest Access (Demo)"):
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
    st.info("💡 รหัสทดสอบ: User: 001 | Pass: 123")

else:
    # --- เมื่อ Login แล้วจะแสดงหน้านี้ ---
    st.balloons()
    st.success("✅ เชื่อมต่อระบบ Snapcon สำเร็จ!")
    
    st.markdown("### ยินดีต้อนรับสู่ระบบควบคุมอัจฉริยะ")
    st.write("ขณะนี้คุณสามารถเข้าถึงข้อมูล Real-time จาก Nodes ทั้งหมดได้แล้ว")
    
    if st.button("📊 ไปที่หน้า Dashboard (Monitor)"):
        st.switch_page("pages/1_Monitor.py")
        
    if st.button("ออกจากระบบ (Logout)"):
        st.session_state.logged_in = False
        st.rerun()
