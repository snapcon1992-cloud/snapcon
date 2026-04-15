import streamlit as st
import pandas as pd
import numpy as np

# 1. การตั้งค่าหน้ากระดาษ
st.set_page_config(
    page_title="SNAPCON | Smart Automation",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. การจัดการสถานะ (Session State)
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Watanabe San"

# 3. Custom CSS เพื่อความเป๊ะ 100% (SNAPCON Theme)
st.markdown("""
<style>
    /* พื้นหลัง Sidebar สีเขียวเข้มตามรูป */
    [data-testid="stSidebar"] {
        background-color: #062822 !important;
        color: white !important;
    }
    
    /* หัวข้อ SNAPCON ใน Sidebar */
    .sidebar-brand {
        color: #00B36E;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sidebar-subbrand {
        color: #4FD1C5;
        font-size: 10px;
        margin-top: -10px;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    
    /* การ์ดโปรไฟล์ผู้ใช้ */
    .user-card {
        background-color: #E6FFFA;
        padding: 15px;
        border-radius: 12px;
        color: #1A365D;
        margin-bottom: 25px;
        border-left: 5px solid #00B36E;
    }
    
    /* Hero Banner สีขาว สะอาดตา */
    .hero-container {
        background-color: white;
        padding: 50px;
        border-radius: 20px;
        border-bottom: 6px solid #009639;
        margin-bottom: 40px;
    }
    .hero-title {
        font-size: 3.8rem;
        font-weight: 900;
        line-height: 1.1;
        color: #1A202C;
    }
    .hero-highlight {
        color: #009639;
    }
    
    /* การ์ด Solutions */
    .solution-card {
        background-color: #F7FAFC;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        min-height: 200px;
        margin-bottom: 10px;
    }
    
    /* ปุ่มสไตล์ SNAPCON */
    .stButton>button {
        border-radius: 8px;
        text-transform: uppercase;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ฟังก์ชันเปลี่ยนหน้า
def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 4. SIDEBAR
with st.sidebar:
    st.markdown('<p class="sidebar-brand">SNAPCON</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-subbrand">AUTOMATION SOLUTION</p>', unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown(f"""
        <div class="user-card">
            <small style="color: #4A5568;">Current Operator:</small><br>
            <strong>{st.session_state.user_name}</strong><br>
            <span style="font-size: 0.8rem; color: #2D3748;">Senior Engineer</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 MAIN HOME", use_container_width=True): nav_to("main")
        if st.button("📊 PRODUCTION DASHBOARD", use_container_width=True): nav_to("dashboard")
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        if st.button("📞 CONTACT SUPPORT", use_container_width=True):
            st.toast("กำลังเชื่อมต่อฝ่ายเทคนิค...")
            
        if st.button("🚪 LOGOUT", use_container_width=True):
            st.session_state.logged_in = False
            nav_to("main")
    else:
        st.warning("Please login to access all engineering files.")

# 5. CONTENT AREA
if st.session_state.page == "main":
    # Login Section
    if not st.session_state.logged_in:
        c1, c2, c3, c4 = st.columns([5, 2, 2, 1])
        with c2: 
            user_in = st.text_input("ID", placeholder="001", label_visibility="collapsed")
        with c3:
            pass_in = st.text_input("Password", type="password", placeholder="****", label_visibility="collapsed")
        with c4:
            if st.button("LOGIN"):
                if user_in == "001" and pass_in == "123":
                    st.session_state.logged_in = True
                    st.rerun()

    # Hero Banner
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Plug & Play.<br><span class="hero-highlight">Control Made Easy.</span></h1>
        <p style="font-size: 1.5rem; color: #2D3748; margin-top: 15px; font-weight: 700; letter-spacing: 0.5px;">
            “Just Connect. Just Control.”
        </p>
        <p style="font-size: 1.1rem; color: #718096; margin-top: 5px;">
            Easy Setup. Instant Control.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Solutions Section
    st.subheader("SNAPCON Digital Solutions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="solution-card">
            <h3>📂 Documentation</h3>
            <p>รวมคู่มือการใช้งาน (Manual) และเอกสารรับรองมาตรฐานผลิตภัณฑ์ทั้งหมด</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("OPEN MANUALS", "https://drive.google.com/your-manuals-folder", use_container_width=True)
        
    with col2:
        st.markdown("""<div class="solution-card">
            <h3>📐 Drawing download</h3>
            <p>ดาวน์โหลดแบบทางวิศวกรรม (Drawing), Wiring Diagram และ 3D Models สำหรับออกแบบติดตั้ง</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("DOWNLOAD DRAWINGS", "https://drive.google.com/your-drawing-folder", use_container_width=True)
        
    with col3:
        st.markdown("""<div class="solution-card">
            <h3>🛠️ Technical Support</h3>
            <p>ดาวน์โหลดซอฟต์แวร์ อัปเดตเฟิร์มแวร์ และช่องทางติดต่อวิศวกรผู้เชี่ยวชาญ</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("DOWNLOAD SOFTWARE", "https://drive.google.com/your-software-folder", use_container_width=True)

elif st.session_state.page == "dashboard":
    st.title("📊 Production Dashboard")
    st.info("หน้านี้สำหรับติดตามประสิทธิภาพการผลิตรายวัน")
    m1, m2, m3 = st.columns(3)
    m1.metric("Overall OEE", "92.5%")
    m2.metric("Yield Rate", "99.2%")
    m3.metric("Uptime", "23h 45m")
    
    if st.button("Return to Home"): nav_to("main")

# Footer
st.markdown("<br><br><p style='text-align: center; color: #718096; font-size: 0.8rem;'>© 2026 SNAPCON AUTOMATION SOLUTION. All Rights Reserved.</p>", unsafe_allow_html=True)
