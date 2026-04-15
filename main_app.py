import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="SNAPCON | Industrial AI Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. State Management
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Watanabe San"

# 3. Enhanced Premium Dark Theme CSS
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC !important;
    }

    /* Sidebar - Ultra Dark Emerald */
    [data-testid="stSidebar"] {
        background-color: #051612 !important;
        border-right: 1px solid #102A25;
    }
    
    .sidebar-content {
        padding: 20px;
    }
    
    .brand-container {
        padding: 10px 0 30px 0;
    }
    
    .brand-name {
        color: #FFFFFF;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0;
    }
    
    .brand-tagline {
        color: #10B981;
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* User Profile Card in Sidebar */
    .user-profile {
        background: linear-gradient(135deg, #0A261F 0%, #051612 100%);
        border: 1px solid #10B98133;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 25px;
    }

    /* Hero Section */
    .hero-section {
        background-color: white;
        padding: 60px;
        border-radius: 24px;
        margin-bottom: 40px;
        border-bottom: 8px solid #10B981;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1;
    }
    
    .hero-highlight {
        color: #10B981;
    }

    /* Solution Cards */
    .card-box {
        background: white;
        padding: 30px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .card-box:hover {
        border-color: #10B981;
        transform: translateY(-5px);
        box-shadow: 0 12px 20px -10px rgba(16, 185, 129, 0.2);
    }
    
    /* Custom Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1rem;
        transition: all 0.2s;
    }

    /* Login Input Styles */
    .stTextInput input {
        border-radius: 8px !important;
        background-color: #F1F5F9 !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Helper
def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 4. SIDEBAR DESIGN
with st.sidebar:
    st.markdown("""
    <div class="brand-container">
        <p class="brand-name">SNAPCON</p>
        <p class="brand-tagline">Industrial AI Solution</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown(f"""
        <div class="user-profile">
            <p style="color: #94A3B8; font-size: 11px; margin-bottom: 4px;">SYSTEM OPERATOR</p>
            <p style="color: #F8FAFC; font-weight: 700; margin-bottom: 0;">{st.session_state.user_name}</p>
            <p style="color: #10B981; font-size: 11px; font-weight: 600;">SENIOR LEAD ENGINEER</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 HOME"): nav_to("main")
        if st.button("📊 MY DASHBOARD"): nav_to("dashboard")
        if st.button("📞 CONTACT SUPPORT"): st.toast("Connecting to support team...")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("🚪 SIGN OUT SYSTEM"):
            st.session_state.logged_in = False
            nav_to("main")
    else:
        st.markdown("""
        <div style="background: #0A261F; padding: 15px; border-radius: 10px; border-left: 4px solid #F59E0B;">
            <p style="color: #F59E0B; font-size: 13px; font-weight: 600; margin-bottom: 0;">
                🔒 Authentication Required
            </p>
            <p style="color: #94A3B8; font-size: 11px; margin-top: 5px;">
                Please login to access engineering files and production data.
            </p>
        </div>
        """, unsafe_allow_html=True)

# 5. MAIN CONTENT AREA
if st.session_state.page == "main":
    # Top Login Bar (Matches latest UI)
    if not st.session_state.logged_in:
        l_col1, l_col2, l_col3, l_col4, l_col5 = st.columns([4, 1.5, 1.5, 0.8, 0.8])
        with l_col2:
            u_id = st.text_input("ID", value="001", label_visibility="collapsed")
        with l_col3:
            u_pw = st.text_input("PW", type="password", value="****", label_visibility="collapsed")
        with l_col4:
            if st.button("LOGIN"):
                st.session_state.logged_in = True
                st.rerun()
        with l_col5:
            st.button("REGISTOR")

    # Hero Banner
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Plug & Play.<br><span class="hero-highlight">Control Made Easy.</span></h1>
        <p style="font-size: 1.6rem; color: #1E293B; margin-top: 20px; font-weight: 700;">
            “Just Connect. Just Control.”
        </p>
        <p style="font-size: 1.1rem; color: #64748B;">Easy Setup. Instant Control. No complex configuration needed.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Solutions Grid
    st.markdown("<h3 style='color: #0F172A; margin-bottom: 25px;'>SNAPCON Digital Solutions</h3>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="card-box">
            <h4 style="color: #0F172A;">📂 Data & Documents</h4>
            <p style="color: #64748B; font-size: 14px;">เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัลครบวงจร</p>
            <p style="color: #10B981; font-weight: 600; font-size: 13px; margin-top: 20px;">Download data sheet ></p>
        </div>""", unsafe_allow_html=True)
        st.link_button("OPEN DOCUMENTS", "https://drive.google.com", use_container_width=True)
        
    with c2:
        st.markdown("""<div class="card-box">
            <h4 style="color: #0F172A;">📐 Drawing download</h4>
            <p style="color: #64748B; font-size: 14px;">ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และแจ้งเตือนการซ่อมบำรุงแบบ Real-time</p>
            <p style="color: #10B981; font-weight: 600; font-size: 13px; margin-top: 20px;">Download drawing ></p>
        </div>""", unsafe_allow_html=True)
        st.link_button("DOWNLOAD DRAWINGS", "https://drive.google.com", use_container_width=True)
        
    with c3:
        st.markdown("""<div class="card-box">
            <h4 style="color: #0F172A;">🛠️ Product Catalog</h4>
            <p style="color: #64748B; font-size: 14px;">วิเคราะห์รายงานคุณภาพและการใช้พลังงาน เพื่อลดคาร์บอนฟุตพริ้นท์ตามมาตรฐานสากล</p>
            <p style="color: #10B981; font-weight: 600; font-size: 13px; margin-top: 20px;">Product Catalog ></p>
        </div>""", unsafe_allow_html=True)
        st.link_button("VIEW CATALOG", "https://drive.google.com", use_container_width=True)

elif st.session_state.page == "dashboard":
    # Dashboard Page Implementation
    st.markdown("<h2 style='color: #0F172A;'>Plant Telemetry</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B;'>Monitoring real-time production efficiency and node stability.</p>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1: st.metric("OEE PERFORMANCE", "94.2%", "+1.2%")
    with col_m2: st.metric("SHIFT OUTPUT", "4,500", "+420")
    with col_m3: st.metric("ACTIVE ALERTS", "03", "-1")
    with col_m4: st.metric("UPTIME RATIO", "99.9%", "MAX")
    
    st.divider()
    if st.button("← Back to Home"): nav_to("main")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 80px; padding: 20px; color: #94A3B8; font-size: 12px; border-top: 1px solid #E2E8F0;">
    © 2026 SNAPCON AUTOMATION SOLUTION | ENTERPRISE CONTROL UNIT | PRIVACY POLICY
</div>
""", unsafe_allow_html=True)
