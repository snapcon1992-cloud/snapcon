import streamlit as st
import os

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

# CSS เพื่อซ่อนเมนูเดิมและปรับแต่งปุ่มให้คลิกได้จริง
st.markdown("""
    <style>
    /* 1. ซ่อนเมนูนำทางมาตรฐานของ Streamlit */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* 2. ปรับแต่งพื้นหลัง Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e272e !important;
    }

    /* 3. สไตล์ปุ่มกดสีเขียว (เพิ่ม z-index และ pointer-events เพื่อให้กดได้) */
    div.stButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        display: block !important;
        cursor: pointer !important;
        pointer-events: auto !important;
    }
    
    div.stButton > button:hover {
        background-color: #2ecc71 !important;
        box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3);
    }
    
    /* ส่วนหัวข้อหลอกใน Sidebar */
    .sidebar-custom-header {
        color: #ecf0f1;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 20px 0 15px 5px;
        opacity: 0.5;
        font-weight: bold;
    }
    
    /* ปรับแต่งหน้าหลัก */
    .main-header {
        background-color: white; 
        padding: 20px; 
        border-bottom: 4px solid #27ae60; 
        margin-bottom: 30px;
        border-radius: 0 0 10px 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนของ Sidebar
with st.sidebar:
    # พยายามแสดงโลโก้
    if os.path.exists("Logo.png"):
        st.image("Logo.png", use_container_width=True)
    else:
        st.markdown("<h1 style='color:white; text-align:center;'>SNAPCON</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='sidebar-custom-header'>MENU</div>", unsafe_allow_html=True)
    
    # --- ปุ่มที่ 1: Main ---
    if st.button("🏠 Main", key="btn_main"):
        st.switch_page("main_app.py")
    
    # --- ปุ่มที่ 2: My Dashboard ---
    if st.button("📊 My Dashboard", key="btn_dash"):
        if st.session_state.logged_in:
            try:
                st.switch_page("pages/1_Monitor.py")
            except:
                st.error("ไฟล์ pages/1_Monitor.py หายไป")
        else:
            st.warning("🔒 กรุณา Login ก่อน")
            
    # --- ปุ่มที่ 3: Contact Support ---
    if st.button("📞 Contact Support", key="btn_contact"):
        try:
            st.switch_page("pages/2_Contact.py")
        except:
            st.error("ไฟล์ pages/2_Contact.py หายไป")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # สถานะ Login ใน Sidebar
    if st.session_state.logged_in:
        st.success("Authorized: Admin")
        if st.button("Logout", key="logout_sidebar"):
            st.session_state.logged_in = False
            st.rerun()

# --- ส่วนเนื้อหาหน้าหลัก (Main Content) ---
st.markdown("""
    <div class="main-header">
        <h2 style="margin:0; color:#2c3e50;">SNAPCON <span style="font-weight:300; color:#bdc3c7;">| Green Automation</span></h2>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.markdown("""
        <div style="background:white; padding:35px; border-radius:15px; border-left:8px solid #27ae60; box-shadow:0 10px 25px rgba(0,0,0,0.05);">
            <h1 style="color:#2c3e50; margin-bottom:15px;">Engineering your success.</h1>
            <p style="color:#7f8c8d; font-size:1.1rem; line-height:1.6;">
                ยกระดับอุตสาหกรรมด้วยระบบติดตามผลเรียลไทม์ (Live Monitoring) 
                ช่วยเพิ่มประสิทธิภาพการผลิตและลดการใช้พลังงานอย่างยั่งยืน
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ส่วนปุ่ม Drawing และ Data Sheet
    st.subheader("📂 เอกสารทางเทคนิค (Technical Assets)")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📐 Drawing Files", key="btn_drawing"):
            st.info("กำลังเรียกดูไฟล์เขียนแบบ...")
    with c2:
        if st.button("📑 Data Sheets", key="btn_datasheet"):
            st.info("กำลังดาวน์โหลดรายละเอียดอุปกรณ์...")

with col2:
    if not st.session_state.logged_in:
        st.markdown("<div style='background:white; padding:30px; border-radius:15px; border:1px solid #eee; box-shadow:0 5px 15px rgba(0,0,0,0.05);'>", unsafe_allow_html=True)
        st.subheader("Login Access")
        user_input = st.text_input("Username", placeholder="ระบุชื่อผู้ใช้")
        pass_input = st.text_input("Password", type="password", placeholder="ระบุรหัสผ่าน")
        
        if st.button("SIGN IN", key="login_main"):
            if user_input == "001" and pass_input == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='background:#e8f6ef; padding:30px; border-radius:15px; border:1px solid #27ae60; text-align:center;'>
                <h3 style='color:#27ae60;'>ยินดีต้อนรับกลับมา!</h3>
                <p>ระบบพร้อมใช้งานแล้ว</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("GO TO DASHBOARD", key="go_dash"):
            st.switch_page("pages/1_Monitor.py")

st.markdown("<br><br><p style='text-align:center; color:#bdc3c7; font-size:0.8rem;'>© 2024 SNAPCON AUTOMATION SOLUTION</p>", unsafe_allow_html=True)
