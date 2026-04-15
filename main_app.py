import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="SNAPCON | Snap to Connect",
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
    st.session_state.user_name = "Engineer Admin"

# 3. Enhanced Premium Dark Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC !important;
    }

    /* Sidebar - Ultra Dark Emerald */
    [data-testid="stSidebar"] {
        background-color: #051612 !important;
        border-right: 1px solid #102A25;
    }
    
    .brand-container {
        padding: 10px 0 30px 0;
        text-align: center;
    }
    
    .brand-name {
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0;
    }
    
    .brand-tagline {
        color: #10B981;
        font-size: 9px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* User Profile Card */
    .user-profile {
        background: linear-gradient(135deg, #0A261F 0%, #051612 100%);
        border: 1px solid #10B98133;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 25px;
    }

    /* Hero Section - Minimalist & Bold */
    .hero-section {
        background-color: white;
        padding: 80px 60px;
        border-radius: 24px;
        margin-bottom: 40px;
        border-left: 12px solid #10B981;
        box-shadow: 0 10px 30px -15px rgba(0, 0, 0, 0.1);
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 0.95;
        letter-spacing: -2px;
    }
    
    .hero-highlight {
        color: #10B981;
    }
    
    .hero-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.2rem;
        color: #64748B;
        margin-top: 25px;
        background: #F1F5F9;
        display: inline-block;
        padding: 5px 15px;
        border-radius: 6px;
    }

    /* Solution Cards */
    .card-box {
        background: white;
        padding: 35px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card-box:hover {
        border-color: #10B981;
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.1);
    }
    
    .card-title {
        color: #0F172A;
        font-weight: 800;
        font-size: 1.4rem;
        margin-bottom: 10px;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        padding: 0.7rem 1rem;
        border: none;
        background-color: #0F172A;
        color: white;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #10B981;
        color: white;
    }

    /* Custom Login Inputs */
    .stTextInput input {
        border-radius: 10px !important;
        background-color: #F1F5F9 !important;
        border: 1px solid transparent !important;
    }
    .stTextInput input:focus {
        border-color: #10B981 !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 4. SIDEBAR DESIGN
with st.sidebar:
    st.markdown("""
    <div class="brand-container">
        <p class="brand-name">SNAPCON</p>
        <p class="brand-tagline">Industrial Automation</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown(f"""
        <div class="user-profile">
            <p style="color: #94A3B8; font-size: 10px; margin-bottom: 2px; font-weight: 600;">ACTIVE SESSION</p>
            <p style="color: #F8FAFC; font-weight: 700; margin-bottom: 0; font-size: 16px;">{st.session_state.user_name}</p>
            <p style="color: #10B981; font-size: 11px;">Verified Engineer</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 HOME"): nav_to("main")
        if st.button("📊 ANALYTICS"): nav_to("dashboard")
        
        st.markdown("<div style='height: 250px'></div>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state.logged_in = False
            nav_to("main")
    else:
        st.markdown("""
        <div style="background: #0A261F; padding: 20px; border-radius: 15px; border-left: 4px solid #F59E0B;">
            <p style="color: #F59E0B; font-size: 14px; font-weight: 700; margin-bottom: 5px;">ACCESS RESTRICTED</p>
            <p style="color: #94A3B8; font-size: 11px;">Please sign in to access technical resources and drawings.</p>
        </div>
        """, unsafe_allow_html=True)

# 5. MAIN CONTENT AREA
if st.session_state.page == "main":
    # Minimal Top Bar for Login
    if not st.session_state.logged_in:
        l_col1, l_col2, l_col3, l_col4 = st.columns([5, 1.5, 1.5, 1])
        with l_col2:
            st.text_input("ID", placeholder="ID", label_visibility="collapsed")
        with l_col3:
            st.text_input("PW", type="password", placeholder="PW", label_visibility="collapsed")
        with l_col4:
            if st.button("LOGIN"):
                st.session_state.logged_in = True
                st.rerun()

    # Hero Banner
    st.markdown("""
    <div class="hero-section">
        <p style="color: #10B981; font-weight: 800; font-size: 14px; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px;">The Future of Automation</p>
        <h1 class="hero-title">Plug & Play.<br><span class="hero-highlight">Snap to Connect.</span></h1>
        <p class="hero-sub">Ready to Control.</p>
        <p style="font-size: 1.2rem; color: #475569; margin-top: 30px; max-width: 600px;">
            Experience the simplest industrial integration. No complex setup, no wasted time. 
            Just snap and take command of your production line.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3-Card Layout
    c1, c2, c3 = st.columns(3, gap="large")
    
    with c1:
        st.markdown("""<div class="card-box">
            <div>
                <div class="card-title">Data Sheet</div>
                <p style="color: #64748B; font-size: 15px;">Technical specifications, performance curves, and electrical diagrams.</p>
            </div>
            <p style="color: #10B981; font-weight: 700; font-size: 13px; margin-top: 20px;">ACCESS DATABASE →</p>
        </div>""", unsafe_allow_html=True)
        st.button("DOWNLOAD DATA", key="btn1")
        
    with c2:
        st.markdown("""<div class="card-box">
            <div>
                <div class="card-title">2D/3D Drawings</div>
                <p style="color: #64748B; font-size: 15px;">Official CAD files for mechanical design and plant layout planning.</p>
            </div>
            <p style="color: #10B981; font-weight: 700; font-size: 13px; margin-top: 20px;">VIEW DRAWINGS →</p>
        </div>""", unsafe_allow_html=True)
        st.button("DOWNLOAD CAD", key="btn2")
        
    with c3:
        st.markdown("""<div class="card-box">
            <div>
                <div class="card-title">Catalog 2026</div>
                <p style="color: #64748B; font-size: 15px;">Explore our full lineup of intelligent snap-on controllers and sensors.</p>
            </div>
            <p style="color: #10B981; font-weight: 700; font-size: 13px; margin-top: 20px;">EXPLORE RANGE →</p>
        </div>""", unsafe_allow_html=True)
        st.button("VIEW CATALOG", key="btn3")

elif st.session_state.page == "dashboard":
    st.markdown("<h1 style='color: #0F172A; font-weight: 800;'>Control Insights</h1>", unsafe_allow_html=True)
    st.divider()
    st.info("Dashboard module is active. Real-time telemetry connection: STABLE")
    if st.button("← RETURN TO FRONT DESK"): nav_to("main")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 100px; padding-bottom: 40px; color: #94A3B8; font-size: 11px; letter-spacing: 1px;">
    SNAPCON SOLUTIONS CO., LTD. | SNAP TO CONNECT. READY TO CONTROL.
</div>
""", unsafe_allow_html=True)
