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

# CSS เพื่อซ่อนเมนูเดิมและปรับแต่งปุ่มให้กดได้จริงบน Mobile และ Desktop
st.markdown("""
    <style>
    /* ซ่อนเมนูนำทางมาตรฐานของ Streamlit */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #1e272e !important;
    }

    /* สไตล์ปุ่มกดสีเขียว Navigation */
    div.stButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        margin-bottom: 10px !important;
        cursor: pointer !important;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: #2ecc71 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(46, 204, 113, 0.4);
    }

    .nav-label {
        color: #ffffff;
        font-size: 0.85rem;
        font-weight: bold;
        margin: 20px 0 10px 5px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .status-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        background: #34495e;
        color: #ecf0f1;
    }
    </style>
""", unsafe_allow_html=True)

# ฟังก์ชันสำหรับเปลี่ยนหน้า (แก้ปัญหา Path บน Streamlit Cloud)
def nav_to(page_path):
    try:
        # พยายามรันด้วย Path ปกติ
        st.switch_page(page_path)
    except Exception as e:
        # หากพลาด ให้ลองเช็คว่าไฟล์มีจริงไหมแล้วแสดง Error ที่เข้าใจง่าย
        st.error(f"ไม่สามารถไปที่หน้า {page_path} ได้: {str(e)}")

# ส่วนของ Sidebar
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>SNAPCON</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='nav-label'>🟢 NAVIGATION</div>", unsafe_allow_html=True)
    
    # ปุ่มหลัก
    if st.button("🏠 Main / Home", key="btn_main_nav"):
        nav_to("main_app.py")
    
    if st.button("📊 My Dashboard", key="btn_dash_nav"):
        if st.session_state.logged_in:
            # ตรวจสอบชื่อไฟล์ตามที่คุณตั้งใน GitHub (ถ้าคุณแก้เป็น Folder แล้วใช้ path นี้)
            nav_to("pages/1_Monitor.py")
        else:
            st.warning("🔒 กรุณาเข้าสู่ระบบก่อน")
            
    if st.button("📞 Contact Support", key="btn_contact_nav"):
        nav_to("pages/2_Contact.py")

    st.markdown("---")
    if st.session_state.logged_in:
        st.markdown("<div class='status-badge'>Verified User: Admin</div>", unsafe_allow_html=True)
        if st.button("Logout", key="btn_logout_nav"):
            st.session_state.logged_in = False
            st.rerun()

# --- ส่วนเนื้อหาหน้าหลัก (Main Content) ---
st.markdown("""
    <div style="background:white; padding:15px; border-bottom:3px solid #27ae60; margin-bottom:25px;">
        <h3 style="margin:0; color:#2c3e50;">SNAPCON <span style="font-weight:normal; color:#bdc3c7;">| Green Technology</span></h3>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 0.7])

with col1:
    st.markdown("""
        <div style="background:white; padding:40px; border-radius:15px; box-shadow:0 4px 20px rgba(0,0,0,0.05); border-left:10px solid #27ae60;">
            <h1 style="color:#2c3e50; font-size:2.5rem;">Engineering your success.</h1>
            <p style="color:#7f8c8d; font-size:1.2rem;">
                สัมผัสนวัตกรรมการขับเคลื่อนและระบบควบคุมอัจฉริยะจาก SNAPCON 
                ที่ช่วยเพิ่มประสิทธิภาพการผลิต (OEE) และลดการใช้พลังงานในอุตสาหกรรมยุค 4.0
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    if not st.session_state.logged_in:
        st.markdown("<div style='background:white; padding:30px; border-radius:15px; border:1px solid #eee;'>", unsafe_allow_html=True)
        st.subheader("Customer Sign-In")
        user = st.text_input("Username / E-mail")
        pwd = st.text_input("Password", type="password")
        
        if st.button("SIGN IN", key="btn_login_main"):
            if user == "001" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("ข้อมูลการเข้าสู่ระบบไม่ถูกต้อง")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success("คุณเข้าสู่ระบบแล้ว")
        if st.button("เข้าสู่หน้า Dashboard", key="btn_go_dash"):
            nav_to("pages/1_Monitor.py")

st.markdown("<br><p style='text-align:center; color:#bdc3c7;'>Industrial Automation Solutions | Thailand</p>", unsafe_allow_html=True)
