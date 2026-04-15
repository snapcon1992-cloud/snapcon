import streamlit as st

# การตั้งค่าหน้ากระดาษ
st.set_page_config(
    page_title="SNAPCON | Enterprise Control Unit",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS เพื่อความสวยงามและแก้ปัญหาสไตล์
st.markdown("""
<style>
    /* แถบหัวข้อหลัก */
    .main-header {
        color: #009639;
        font-weight: 800;
    }
    
    /* สไตล์ปุ่ม Navigation */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        background-color: white;
        color: #1a202c;
        font-weight: 500;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        border-color: #009639;
        color: #009639;
    }

    /* แบนเนอร์หน้าหลัก */
    .hero-container {
        background-color: #f8fafc;
        padding: 60px;
        border-radius: 20px;
        margin-bottom: 40px;
        border-bottom: 5px solid #009639;
    }

    /* การ์ดโซลูชัน */
    .solution-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #edf2f7;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #009639; margin-bottom: 0;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.caption("ENTERPRISE CONTROL UNIT")
    
    st.markdown("---")
    
    # 1. ข้อมูลผู้ใช้ (ตามภาพ image_16734e.jpg)
    st.markdown("""
        <div style='background-color: #f0fff4; padding: 15px; border-radius: 10px; border: 1px solid #c6f6d5;'>
            <p style='margin:0; font-size: 0.8rem; color: #2f855a;'>Logged in as:</p>
            <p style='margin:0; font-weight: bold; color: #22543d;'>Watanabe San</p>
            <p style='margin:0; font-size: 0.8rem; color: #2f855a;'>Senior Engineer</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 2. เมนู Navigation ที่ปรับปรุงใหม่
    st.write("📂 **Navigation**")
    
    # ปุ่ม My Dashboard ปรับให้ไปหน้า Login เพื่อเข้าดูข้อมูล
    if st.button("📊 My Dashboard"):
        st.switch_page("pages/1_Monitor.py") # สมมติว่าหน้า 1 คือหน้า Login/Monitor
        
    if st.button("📞 Contact Support"):
        # ปรับให้ใช้งานได้ตามคำแนะนำ
        st.toast("Connecting to support team...")
        # st.switch_page("pages/2_Contact.py") # เปิดใช้งานเมื่อมีไฟล์หน้า contact

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ปุ่ม Logout แบบเรียบง่าย (แก้ Error style จากภาพ image_0b21aa)
    if st.button("Logout"):
        st.success("Logged out successfully")

# --- MAIN CONTENT ---

# Hero Section
st.markdown("""
    <div class="hero-container">
        <h1 style='font-size: 3.5rem; line-height: 1;'>Cool running.<br><span style='color: #009639;'>Long life.</span></h1>
        <p style='font-size: 1.2rem; color: #4a5568; margin-top: 20px; max-width: 500px;'>
            Industrial Automation Solutions for a Greener Future. 
            Optimizing energy efficiency and system longevity.
        </p>
        <div style='background: #009639; color: white; padding: 10px 25px; border-radius: 5px; display: inline-block; margin-top: 20px; font-weight: bold;'>
            Find out more
        </div>
    </div>
""", unsafe_allow_html=True)

st.subheader("Our Solutions")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="solution-card">
            <h4>📄 Data & Documents</h4>
            <p style='color: #718096; font-size: 0.9rem;'>เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัล</p>
            <p style='color: #009639; font-weight: bold; margin-top: 20px;'>Explore documents ></p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Open Documents", key="btn_docs")

with col2:
    st.markdown("""
        <div class="solution-card">
            <h4>⚙️ Product Status</h4>
            <p style='color: #718096; font-size: 0.9rem;'>ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และแผนผังทางเทคนิค</p>
            <p style='color: #009639; font-weight: bold; margin-top: 20px;'>View status ></p>
        </div>
    """, unsafe_allow_html=True)
    # ปรับเป็น Download Drawing ตาม comment
    st.button("Download Drawing", key="btn_drawings")

with col3:
    st.markdown("""
        <div class="solution-card">
            <h4>🛡️ Quality Control</h4>
            <p style='color: #718096; font-size: 0.9rem;'>วิเคราะห์รายงานคุณภาพและการใช้พลังงาน พร้อมรายละเอียดผลิตภัณฑ์</p>
            <p style='color: #009639; font-weight: bold; margin-top: 20px;'>See analysis ></p>
        </div>
    """, unsafe_allow_html=True)
    # ปรับเป็น Product Catalog ตาม comment
    st.button("Product Catalog", key="btn_catalog")

st.markdown("---")
st.caption("Auth Server: ID-SEA-01 | SNAPCON Enterprise System")
