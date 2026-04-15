import streamlit as st

# 1. การตั้งค่าหน้ากระดาษ (Home Page)
st.set_page_config(
    page_title="SNAPCON | Green Technology & Automation",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS เพื่อปรับสไตล์ให้เหมือน SEW-EURODRIVE
st.markdown("""
<style>
    /* แถบเมนูด้านบน */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #009639;
        margin-bottom: 0px;
    }
    
    /* สไตล์ปุ่ม Navigation ใน Sidebar */
    .stButton > button {
        width: 100%;
        border-radius: 4px;
        height: 3em;
        background-color: white;
        color: #333;
        border: 1px solid #ddd;
        transition: all 0.3s;
        font-weight: 500;
        text-align: left;
        padding-left: 20px;
    }
    .stButton > button:hover {
        border-color: #009639;
        color: #009639;
        background-color: #f0fdf4;
    }
    
    /* แบนเนอร์หน้าหลัก */
    .hero-section {
        background-color: #f8f9fa;
        padding: 80px 60px;
        border-radius: 15px;
        margin-bottom: 40px;
        border-bottom: 6px solid #009639;
        background-image: linear-gradient(to right, #f8f9fa, #e2e8f0);
    }
    
    /* การ์ดฟีเจอร์ */
    .feature-card {
        padding: 30px;
        background: white;
        border: 1px solid #eee;
        border-radius: 12px;
        text-align: left;
        transition: 0.3s;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .feature-card:hover {
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border-color: #009639;
        transform: translateY(-5px);
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 10px;
    }
    
    .card-text {
        color: #718096;
        font-size: 0.95rem;
    }

    .card-link {
        color: #009639;
        font-weight: 700;
        margin-top: 15px;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar (ปรับให้ใช้ st.switch_page ตามโครงสร้างโฟลเดอร์จริง)
with st.sidebar:
    st.markdown("<h2 style='color: #009639;'>SNAPCON</h2>", unsafe_allow_html=True)
    
    # ข้อมูลผู้ใช้งาน
    st.info("👤 **Logged in as:**\nWatanabe San\n*Senior Engineer*")
    
    st.markdown("---")
    st.write("🔍 **Navigation**")
    
    # ใช้ปุ่มธรรมดาเรียก switch_page เพื่อไปหน้าต่างๆ ในโฟลเดอร์ /pages
    if st.button("🏠 Home"):
        st.rerun() # อยู่หน้าเดิม
        
    if st.button("📊 My Dashboard"):
        try:
            st.switch_page("pages/1_Monitor.py")
        except:
            st.error("ไม่พบไฟล์ Dashboard ในระบบ")
            
    if st.button("📞 Contact Support"):
        try:
            st.switch_page("pages/2_Contact.py")
        except:
            st.error("ไม่พบไฟล์ Contact ในระบบ")
        
    st.markdown("---")
    st.write("⚙️ **System Control**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start", key="start_btn"):
            st.toast("System Starting...")
    with col2:
        if st.button("⏹️ Stop", key="stop_btn"):
            st.toast("System Stopping...")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# 4. เนื้อหาหน้าหลัก (Home Page)
# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1 style='font-size: 4rem; margin-bottom: 15px; font-weight: 800; line-height: 1.1;'>Cool running. <br><span style='color: #009639;'>Long life.</span></h1>
        <p style='font-size: 1.4rem; color: #4a5568; max-width: 600px; margin-bottom: 30px;'>
            Industrial Automation Solutions for a Greener Future. 
            Optimizing energy efficiency and system longevity.
        </p>
        <div style='background: #009639; color: white; padding: 12px 25px; border-radius: 5px; display: inline-block; font-weight: bold; cursor: pointer;'>
            Find out more
        </div>
    </div>
""", unsafe_allow_html=True)

# Features Grid
st.markdown("<h3 style='margin-bottom: 25px;'>Our Solutions</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div>
                <div class="card-title">📄 Data & Documents</div>
                <div class="card-text">เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัลครบวงจร</div>
            </div>
            <div class="card-link">Explore documents ></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Open Documents", key="btn_docs"):
        st.info("กำลังเปิดฐานข้อมูลเอกสาร...")
    
with col2:
    st.markdown("""
        <div class="feature-card">
            <div>
                <div class="card-title">⚙️ Product Status</div>
                <div class="card-text">ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และแจ้งเตือนการซ่อมบำรุงแบบ Real-time</div>
            </div>
            <div class="card-link">View status ></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Monitor", key="btn_status"):
        st.switch_page("pages/1_Monitor.py")
    
with col3:
    st.markdown("""
        <div class="feature-card">
            <div>
                <div class="card-title">🛡️ Quality Control</div>
                <div class="card-text">วิเคราะห์รายงานคุณภาพและการใช้พลังงาน เพื่อลดคาร์บอนฟุตพริ้นท์ตามมาตรฐานสากล</div>
            </div>
            <div class="card-link">See analysis ></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("View Analysis", key="btn_qc"):
        st.switch_page("pages/1_Monitor.py")

# Footer เล็กๆ
st.markdown("---")
st.caption("© 2024 SNAPCON Automation | Standardized by Industrial IoT Protocols")
