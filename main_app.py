import streamlit as st
import pandas as pd
import time
import random
import plotly.express as px

# การตั้งค่าหน้าจอ
st.set_page_config(
    page_title="SNAPCON | Green Solutions",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE ---
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'prod_counts' not in st.session_state:
    st.session_state.prod_counts = [random.randint(100, 200) for _ in range(10)]
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# CSS Style ปรับเป็นสีเขียว SNAPCON (Green, Dark Gray, White)
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #ffffff;
        color: #333333;
    }
    
    /* Green Banner Style */
    .hero-section {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%); /* Green Gradient */
        padding: 60px 40px;
        color: white;
        border-radius: 0 0 50px 0;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2);
    }
    
    /* Navigation Bar */
    .nav-mimic {
        background: #1f2937;
        padding: 10px 40px;
        color: white;
        font-size: 0.8rem;
        display: flex;
        justify-content: space-between;
    }

    /* Metric Boxes */
    .metric-box {
        background: white;
        border-top: 4px solid #10b981;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .metric-label {
        color: #6b7280;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        color: #111827;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 10px 0;
    }

    /* Side Tab Active Style */
    .nav-btn {
        text-align: left;
        padding: 10px;
        margin-bottom: 5px;
        cursor: pointer;
        border-radius: 4px;
    }

    /* Buttons */
    div.stButton > button {
        border-radius: 4px !important;
        text-transform: uppercase;
        font-weight: bold !important;
    }
    .stButton>button[kind="primary"] {
        background-color: #10b981 !important;
        border: none !important;
    }

    /* User Profile Card */
    .user-card {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN SECTION ---
if not st.session_state.logged_in:
    col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
    with col_l2:
        st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
        st.markdown("""
            <div style='text-align:center; margin-bottom:30px;'>
                <h1 style='color:#10b981; font-weight:900; letter-spacing:-2px; font-size:3.5rem;'>SNAPCON</h1>
                <p style='color:#374151; font-weight:bold;'>THE GREEN FUTURE OF AUTOMATION</p>
            </div>
        """, unsafe_allow_html=True)
        with st.form("login_form"):
            user = st.text_input("Personnel ID")
            pwd = st.text_input("Access Code", type="password")
            if st.form_submit_button("SYSTEM LOGIN", use_container_width=True):
                if user == "admin" or user == "001":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Authentication Failed")
    st.stop()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:#10b981;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="user-card">
            <small>Logged in as:</small><br>
            <strong>Watanabe San</strong><br>
            <small>Senior Engineer</small>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "Home"
    if st.button("📊 My Dashboard", use_container_width=True):
        st.session_state.current_page = "My Dashboard"
    
    st.write("---")
    st.subheader("System Control")
    if st.button("▶ START SYSTEM", type="primary", use_container_width=True):
        st.session_state.is_running = True
    if st.button("⏹ STOP SYSTEM", use_container_width=True):
        st.session_state.is_running = False
    
    if st.button("Logout", style="margin-top:50px;"):
        st.session_state.logged_in = False
        st.rerun()

# Logic Auto-update
if st.session_state.is_running:
    for i in range(10):
        st.session_state.prod_counts[i] += random.randint(0, 3)
    time.sleep(1)
    st.rerun()

# --- HEADER (Navigation Mimic) ---
st.markdown("""
    <div class="nav-mimic">
        <div>DASHBOARDS | ANALYTICS | PREDICTIVE MAINTENANCE | SETTINGS</div>
        <div>REGION: SOUTHEAST ASIA (TH)</div>
    </div>
""", unsafe_allow_html=True)

# --- PAGE ROUTING ---
if st.session_state.current_page == "Home":
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <p style="text-transform:uppercase; letter-spacing:2px; font-size:0.9rem; margin-bottom:5px;">Factory Overview</p>
            <h1 style="font-size:3rem; font-weight:800; margin-top:0;">Sustainable Intelligence.</h1>
            <p style="font-size:1.2rem; opacity:0.9;">Real-time monitoring for your smart factory ecosystem.</p>
        </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Total Production</div><div class="metric-value">{sum(st.session_state.prod_counts):,}</div><small style="color:green">Efficiency 100%</small></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Global OEE</div><div class="metric-value">92.4%</div><small style="color:green">Optimal Range</small></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Active Robots</div><div class="metric-value">12 Units</div><small style="color:blue">Synchronized</small></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-box"><div class="metric-label">CO2 Saving</div><div class="metric-value">14.2 <span style="font-size:1rem">kg</span></div><small style="color:green">Eco Mode Active</small></div>', unsafe_allow_html=True)

    st.markdown("<h3 style='border-left: 5px solid #10b981; padding-left:15px; margin-top:20px;'>Live Production Line</h3>", unsafe_allow_html=True)
    df = pd.DataFrame({
        "Line": [f"LINE-{i+1:02d}" for i in range(10)],
        "Output": st.session_state.prod_counts
    })
    fig = px.bar(df, x="Line", y="Output", color="Output", color_continuous_scale='Greens')
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.current_page == "My Dashboard":
    st.markdown(f"<h1 style='color:#10b981;'>Welcome back, Watanabe San</h1>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("### 🔔 Personalized Alerts")
        st.warning("Maintenance due for Line 04 in 2 days.")
        st.success("Your energy optimization target was met!")
        st.info("System update scheduled for Sunday.")
        
        st.markdown("### ⚙️ Quick Actions")
        st.button("Download My Last Report", use_container_width=True)
        st.button("View Team Tasks", use_container_width=True)

    with c2:
        st.markdown("### 📈 My Focus KPIs")
        # สร้างกราฟจำลองของตัวเอง
        my_data = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Personal Task Comp.": [80, 95, 70, 85, 90, 60, 40]
        })
        fig2 = px.line(my_data, x="Day", y="Personal Task Comp.", markers=True)
        fig2.update_traces(line_color='#10b981')
        st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("### 📋 Recent Activities")
        st.table(pd.DataFrame({
            "Time": ["10:45", "09:30", "Yesterday"],
            "Activity": ["Checked Line 02 Logs", "System Start", "Quarterly Report Created"]
        }))

# Footer
st.markdown("<br><div style='background:#f9fafb; border-top:1px solid #eee; color:#9ca3af; padding:20px; text-align:center; font-size:0.8rem;'>© 2024 SNAPCON GREEN SOLUTIONS - DRIVING SUSTAINABILITY THROUGH AUTOMATION</div>", unsafe_allow_html=True)
