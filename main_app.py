import streamlit as st

# 1. การตั้งค่าหน้าจอเบื้องต้น (Green Industrial Theme)
st.set_page_config(
    page_title="SNAPCON | Green Automation",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ตรวจสอบสถานะการเข้าสู่ระบบ
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 3. CSS Custom Design (Green Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Sarabun:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Roboto', 'Sarabun', sans-serif;
        color: #2d3436;
    }
    
    .stApp {
        background-color: #f0f4f0; /* Soft Green Background */
    }
    
    /* Corporate Header Bar - Green */
    .corp-header {
        background-color: #ffffff;
        border-bottom: 4px solid #27ae60; /* Industrial Green */
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Hero Box with Green Accent */
    .hero-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 8px;
        border-left: 10px solid #27ae60;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    
    /* Input Fields */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 4px !important;
    }
    
    /* Green Button Style */
    .stButton>button {
        background-color: #27ae60 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        font-weight: bold !important;
        padding: 0.6rem 2rem !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #219150 !important;
        box-shadow: 0 4px 12px rgba(39, 174, 96, 0.2) !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1e272e !important; /* Dark Blue-Gray */
    }
    [data-testid="stSidebar"] * {
        color: #ecf0f1 !important;
    }
    
    .footer-text {
        text-align: center;
        color: #7f8c8d;
        font-size: 0.8rem;
        margin-top: 50px;
        padding: 20px;
    }
    
    /* Action Cards */
    .action-card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        border-top: 4px solid #27ae60;
        text-align: center;
        transition: 0.3s;
    }
    .action-card:hover {
        transform: translateY(-5px);
    }
    </style>
""", unsafe_allow_html=True)

# 4. TOP NAVIGATION BAR
st.markdown("""
    <div class="corp-header">
        <div style="display:flex; align-items:center; gap:15px;">
            <span style="font-size:1.8rem; font-weight:900; color:#27ae60; letter-spacing:-1px;">SNAPCON</span>
            <span style="border-left:1px solid #ddd; padding-left:15px; color:#666; font-size:0.9rem;">Green Technology & Automation</span>
        </div>
        <div style="font-size:0.8rem; color:#999; font-weight:bold;">SUSTAINABILITY FIRST</div>
    </div>
""", unsafe_allow_html=True)

# 5. SIDEBAR (Updated Menus)
with st.sidebar:
    st.markdown("### 🟢 NAVIGATION")
    if st.button("🏠 Main", use_container_width=True):
        st.switch_page("main_app.py")
    
    if st.session_state.get('logged_in', False):
        if st.button("📊 My Dashboard", use_container_width=True):
            st.switch_page("pages/1_Monitor.py")
            
    if st.button("📞 Contact Support", use_container_width=True):
        st.switch_page("pages/2_Contact.py")
    
    st.markdown("---")
    if st.session_state.logged_in:
        st.success("Status: Connected")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.info("Sign in for technical docs.")

# 6. MAIN CONTENT
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.markdown("""
        <div class="hero-box">
            <h1 style="font-size:2.5rem; font-weight:900; color:#2c3e50; margin-bottom:10px;">
                Eco-Friendly Engineering.
            </h1>
            <p style="font-size:1.1rem; color:#7f8c8d; line-height:1.6;">
                ยกระดับอุตสาหกรรมด้วยโซลูชันสีเขียว SNAPCON ช่วยให้คุณควบคุมการผลิต 
                พร้อมลดการปล่อยคาร์บอนด้วยระบบ Automation ที่แม่นยำที่สุด
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Section สำหรับ Drawing และ Data Sheet (New Features)
    st.markdown("### 📂 Technical Resources")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown('<div class="action-card">', unsafe_allow_html=True)
        st.markdown("#### 📐 Drawing Files")
        st.info("CAD / Blueprints (.dwg, .pdf)")
        if st.button("View Drawings", key="btn_draw"):
            st.write("Redirecting to Drawing server...")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with d2:
        st.markdown('<div class="action-card">', unsafe_allow_html=True)
        st.markdown("#### 📑 Data Sheets")
        st.info("Technical Specifications")
        if st.button("Download Specs", key="btn_data"):
            st.write("Loading data sheets...")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if not st.session_state.logged_in:
        st.markdown("""
            <div style="background:white; padding:30px; border-radius:8px; border:1px solid #ddd;">
                <h3 style="margin-top:0; color:#27ae60;">Portal Login</h3>
                <p style="font-size:0.8rem; color:#666;">เข้าสู่ระบบเพื่อเข้าถึง My Dashboard และไฟล์เทคนิค</p>
            </div>
        """, unsafe_allow_html=True)
        
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        
        if st.button("LOGIN TO SYSTEM"):
            if user == "001" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Username or Password")
    else:
        st.markdown("""
            <div style="background:#e8f6ef; padding:30px; border-radius:8px; border:1px solid #27ae60;">
                <h3 style="color:#27ae60; margin-top:0;">Welcome back!</h3>
                <p>ระบบพร้อมใช้งานแล้ว คุณสามารถจัดการ Dashboard และดาวน์โหลดข้อมูลเทคนิคได้ทันที</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to My Dashboard", use_container_width=True):
            st.switch_page("pages/1_Monitor.py")

# 7. FOOTER
st.markdown("""
    <div class="footer-text">
        © 2024 SNAPCON GREEN SOLUTION | Driving Industrial Sustainability<br>
        <span style="font-size:0.7rem;">Main | My Dashboard | Drawing | Data Sheet</span>
    </div>
""", unsafe_allow_html=True)
