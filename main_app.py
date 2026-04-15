import streamlit as st

# 1. การตั้งค่าหน้าจอเบื้องต้น (Industrial Theme)
st.set_page_config(
    page_title="SNAPCON | Driving the Future",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ตรวจสอบสถานะการเข้าสู่ระบบ
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 3. CSS Custom Design (Inspired by SEW-EURODRIVE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Sarabun:wght@400;700&display=swap');
    
    /* Global Reset */
    html, body, [class*="st-"] {
        font-family: 'Roboto', 'Sarabun', sans-serif;
        color: #333333;
    }
    
    /* Background */
    .stApp {
        background-color: #f4f4f4;
    }
    
    /* Corporate Header Bar */
    .corp-header {
        background-color: #ffffff;
        border-bottom: 3px solid #ce000c; /* SEW Red */
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Hero Section */
    .hero-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 4px;
        border-left: 8px solid #ce000c;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    
    /* Industrial Input Fields */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 2px !important;
        border: 1px solid #cccccc !important;
    }
    
    /* SEW Red Button Style */
    .stButton>button {
        background-color: #ce000c !important;
        color: white !important;
        border: none !important;
        border-radius: 2px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 0.6rem 2rem !important;
        transition: background 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background-color: #a0000a !important;
        box-shadow: 0 4px 8px rgba(206, 0, 12, 0.2) !important;
    }
    
    /* Secondary/White Button */
    .secondary-btn button {
        background-color: #ffffff !important;
        color: #ce000c !important;
        border: 1px solid #ce000c !important;
    }
    
    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #2b2b2b !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    .footer-text {
        text-align: center;
        color: #999999;
        font-size: 0.8rem;
        margin-top: 50px;
        border-top: 1px solid #ddd;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. TOP NAVIGATION BAR (Fake UI for Branding)
st.markdown("""
    <div class="corp-header">
        <div style="display:flex; align-items:center; gap:15px;">
            <span style="font-size:1.8rem; font-weight:900; color:#ce000c; letter-spacing:-1px;">SNAPCON</span>
            <span style="border-left:1px solid #ddd; padding-left:15px; color:#666; font-size:0.9rem;">Solutions for Automation</span>
        </div>
        <div style="font-size:0.8rem; color:#999; font-weight:bold;">Thailand | Global Presence</div>
    </div>
""", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.image("https://www.sew-eurodrive.com/static/media/sew-logo.3188d3d9.svg", width=150) # ตัวอย่างการใส่โลโก้ถ้ามี URL หรือใช้ Logo.png
    st.markdown("### ONLINE SERVICES")
    if st.button("🏠 Home / Products", use_container_width=True):
        st.switch_page("main_app.py")
    if st.button("📞 Support & Contact", use_container_width=True):
        st.switch_page("pages/2_Contact.py")
    
    st.markdown("---")
    if st.session_state.logged_in:
        st.success("Authorized: Admin")
        if st.button("📊 Digital Dashboard", use_container_width=True):
            st.switch_page("pages/1_Monitor.py")
        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.info("Please sign in to access engineering tools.")

# 6. MAIN CONTENT
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.markdown("""
        <div class="hero-box">
            <h1 style="font-size:2.8rem; font-weight:900; margin-bottom:10px;">Engineering your success.</h1>
            <p style="font-size:1.2rem; color:#666; line-height:1.6;">
                สัมผัสนวัตกรรมการขับเคลื่อนและระบบควบคุมอัจฉริยะจาก SNAPCON 
                ที่ช่วยเพิ่มประสิทธิภาพการผลิต (OEE) และลดการใช้พลังงานในอุตสาหกรรมยุค 4.0
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://img.freepik.com/free-photo/automation-industrial-concept-mechanical-arm-working-smart-factory-industry-4-0_1214-5310.jpg?t=st=1710000000&exp=1710003600&hmac=placeholder", caption="Industrial Automation Solutions")

with col2:
    if not st.session_state.logged_in:
        st.markdown("""
            <div style="background:white; padding:30px; border:1px solid #ddd; border-top:4px solid #333;">
                <h3 style="margin-top:0;">Customer Sign-In</h3>
                <p style="font-size:0.8rem; color:#666;">เข้าสู่ระบบเพื่อใช้งานระบบติดตามผลการผลิตแบบ Real-time</p>
            </div>
        """, unsafe_allow_html=True)
        
        username = st.text_input("Username / E-mail")
        password = st.text_input("Password", type="password")
        
        if st.button("SIGN IN"):
            if username == "001" and password == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials.")
        
        st.markdown("---")
        st.markdown("#### Don't have an account?")
        st.markdown("Please contact our sales representative to request system access for your facility.")
        if st.button("Request Access", key="req_btn"):
             st.switch_page("pages/2_Contact.py")
    else:
        st.markdown(f"""
            <div style="background:white; padding:30px; border:1px solid #ddd; border-top:4px solid #ce000c;">
                <h3 style="color:#ce000c;">Welcome back, Admin</h3>
                <p>คุณได้เข้าสู่ระบบในฐานะผู้ควบคุมระบบวิศวกรรม</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Monitor Dashboard", use_container_width=True):
            st.switch_page("pages/1_Monitor.py")

# 7. PRODUCT CARDS (SEW STYLE)
st.markdown("### Featured Solutions")
p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("""
        <div style="background:white; padding:20px; border:1px solid #eee;">
            <h4 style="color:#ce000c;">Drive Systems</h4>
            <p style="font-size:0.85rem;">ระบบขับเคลื่อนประสิทธิภาพสูง รองรับมาตรฐาน IE4/IE5</p>
        </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
        <div style="background:white; padding:20px; border:1px solid #eee;">
            <h4 style="color:#ce000c;">Control Technology</h4>
            <p style="font-size:0.85rem;">PLC และระบบควบคุมแบบ Decentralized ติดตั้งง่าย รวดเร็ว</p>
        </div>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
        <div style="background:white; padding:20px; border:1px solid #eee;">
            <h4 style="color:#ce000c;">Cloud Services</h4>
            <p style="font-size:0.85rem;">การวิเคราะห์ข้อมูลผ่าน Cloud และ Predictive Maintenance</p>
        </div>
    """, unsafe_allow_html=True)

# 8. FOOTER
st.markdown("""
    <div class="footer-text">
        © 2024 SNAPCON ENTERPRISE SOLUTION | A Global Industry Partner<br>
        <span style="font-size:0.7rem;">Terms of Use | Privacy Policy | Legal Info</span>
    </div>
""", unsafe_allow_html=True)
