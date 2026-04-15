import streamlit as st

# การตั้งค่าหน้าจอ
st.set_page_config(
    page_title="SNAPCON | Automation Solutions",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ตรวจสอบสถานะ Login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# CSS เพื่อซ่อนเมนูเดิมและปรับแต่งปุ่ม
st.markdown("""
    <style>
    /* 1. ซ่อนเมนูนำทางมาตรฐานของ Streamlit ทั้งหมด */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* 2. ปรับแต่งพื้นหลัง Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e272e !important;
    }

    /* 3. สไตล์ปุ่มกดสีเขียว */
    div.stButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        width: 100% !important;
        margin-bottom: 5px !important;
        transition: all 0.2s ease;
    }
    
    div.stButton > button:hover {
        background-color: #2ecc71 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* ปรับแต่งส่วนหัวข้อใน Sidebar */
    .sidebar-custom-header {
        color: #ecf0f1;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 15px;
        opacity: 0.6;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนของ Sidebar
with st.sidebar:
    # แสดงโลโก้ (ถ้ามีไฟล์ Logo.png ในเครื่อง)
    try:
        st.image("Logo.png", width=150)
    except:
        st.title("SNAPCON")
    
    st.markdown("<div class='sidebar-custom-header'>Service Menu</div>", unsafe_allow_html=True)
    
    # --- ปุ่มที่ 1: Main ---
    if st.button("🏠 Main"):
        # สำหรับหน้าแรกสุด ใช้การ rerun เพื่อกลับมาหน้าเดิม
        st.rerun()
    
    # --- ปุ่มที่ 2: My Dashboard ---
    if st.button("📊 My Dashboard"):
        if st.session_state.logged_in:
            # ต้องระบุพาธให้ตรงกับโครงสร้างใน GitHub/Streamlit Cloud
            try:
                st.switch_page("pages/1_Monitor.py")
            except Exception as e:
                st.error("ไม่พบไฟล์ Dashboard กรุณาตรวจสอบโฟลเดอร์ pages")
        else:
            st.warning("🔒 กรุณาเข้าสู่ระบบก่อน")
            
    # --- ปุ่มที่ 3: Contact Support ---
    if st.button("📞 Contact Support"):
        try:
            st.switch_page("pages/2_Contact.py")
        except Exception as e:
            st.error("ไม่พบไฟล์ Contact")

    st.markdown("---")
    
    # แสดงสถานะผู้ใช้งาน
    if st.session_state.logged_in:
        st.success("Authorized: Admin")
        if st.button("Logout", key="logout_btn"):
            st.session_state.logged_in = False
            st.rerun()

# --- ส่วนเนื้อหาหน้าหลัก (Main Content) ---
st.markdown("""
    <div style="background-color:white; padding:20px; border-bottom:3px solid #27ae60; margin-bottom:30px;">
        <h2 style="margin:0; color:#2c3e50;">SNAPCON <span style="font-weight:300; color:#bdc3c7;">| Solutions for Automation</span></h2>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.title("Engineering your success.")
    st.write("สัมผัสเทคโนโลยีการควบคุมและตรวจสอบประสิทธิภาพการผลิตแบบ Real-time เพื่อก้าวสู่ยุคอุตสาหกรรม 4.0 อย่างยั่งยืน")
    st.info("💡 เลือกเมนู My Dashboard ด้านซ้ายเพื่อดูข้อมูลระบบ")

with col2:
    if not st.session_state.logged_in:
        st.subheader("Login Access")
        user_input = st.text_input("Username / E-mail")
        pass_input = st.text_input("Password", type="password")
        
        if st.button("SIGN IN", use_container_width=True):
            if user_input == "001" and pass_input == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    else:
        st.success("คุณได้เข้าสู่ระบบแล้ว")
        st.write("พร้อมสำหรับการตรวจสอบระบบ (Monitoring)")
