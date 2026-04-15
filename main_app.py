import streamlit as st

# 1. การตั้งค่าหน้ากระดาษ
st.set_page_config(
    page_title="SNAPCON | Enterprise Control Unit",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. จัดการ Session State สำหรับ Login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# 3. Custom CSS
st.markdown("""
<style>
    .main-header { color: #009639; font-weight: 800; }
    div.stButton > button {
        width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;
        background-color: white; color: #1a202c; font-weight: 500; height: 3em;
    }
    div.stButton > button:hover { border-color: #009639; color: #009639; background-color: #f0fdf4; }
    .hero-container {
        background-color: #f8fafc; padding: 60px; border-radius: 20px;
        margin-bottom: 40px; border-bottom: 6px solid #009639;
    }
    .solution-card {
        background: white; padding: 25px; border-radius: 15px;
        border: 1px solid #edf2f7; height: 280px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #009639; margin-bottom: 0;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.caption("ENTERPRISE CONTROL UNIT")
    st.markdown("---")
    
    if not st.session_state.logged_in:
        # ส่วนของฟอร์ม Login ใน Sidebar
        st.write("🔐 **System Login**")
        user_input = st.text_input("Username")
        pass_input = st.text_input("Password", type="password")
        if st.button("Login"):
            if user_input == "001" and pass_input == "123":
                st.session_state.logged_in = True
                st.session_state.user_name = "Watanabe San"
                st.rerun()
            else:
                st.error("Invalid credentials")
    else:
        # ส่วนแสดงข้อมูลผู้ใช้เมื่อ Login แล้ว
        st.markdown(f"""
            <div style='background-color: #f0fff4; padding: 15px; border-radius: 10px; border: 1px solid #c6f6d5;'>
                <p style='margin:0; font-size: 0.8rem; color: #2f855a;'>Logged in as:</p>
                <p style='margin:0; font-weight: bold; color: #22543d;'>{st.session_state.user_name}</p>
                <p style='margin:0; font-size: 0.8rem; color: #2f855a;'>Senior Engineer</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.write("📂 **Navigation**")
        
        if st.button("📊 My Dashboard"):
            st.switch_page("pages/1_Monitor.py")
            
        if st.button("📞 Contact Support"):
            st.switch_page("pages/2_Contact.py")

        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

# --- MAIN CONTENT ---

# Hero Section
st.markdown("""
    <div class="hero-container">
        <h1 style='font-size: 3.5rem; line-height: 1; font-weight: 800;'>Cool running.<br><span style='color: #009639;'>Long life.</span></h1>
        <p style='font-size: 1.2rem; color: #4a5568; margin-top: 20px; max-width: 550px;'>
            Industrial Automation Solutions for a Greener Future. 
            Optimizing energy efficiency and system longevity with AI Predictive Maintenance.
        </p>
    </div>
""", unsafe_allow_html=True)

st.subheader("Our Solutions")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="solution-card">
            <div>
                <h4 style='color: #1a202c;'>📄 Data & Documents</h4>
                <p style='color: #718096; font-size: 0.9rem;'>เข้าถึงคู่มือการใช้งาน เอกสารเทคนิค และแค็ตตาล็อกสินค้าแบบดิจิทัลที่อัปเดตล่าสุด</p>
            </div>
            <p style='color: #009639; font-weight: bold;'>Explore documents ></p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Open Documents", key="btn_docs"):
        st.info("กำลังเปิดคลังเอกสารเทคนิค...")

with col2:
    st.markdown("""
        <div class="solution-card">
            <div>
                <h4 style='color: #1a202c;'>⚙️ Product Status</h4>
                <p style='color: #718096; font-size: 0.9rem;'>ตรวจสอบสถานะเครื่องจักร ประสิทธิภาพการผลิต และดาวน์โหลดแผนผังทางเทคนิค (Drawing)</p>
            </div>
            <p style='color: #009639; font-weight: bold;'>View drawings ></p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Download Drawing", key="btn_drawings"):
        st.toast("เตรียมไฟล์ Drawing สำหรับดาวน์โหลด...")

with col3:
    st.markdown("""
        <div class="solution-card">
            <div>
                <h4 style='color: #1a202c;'>🛡️ Quality Control</h4>
                <p style='color: #718096; font-size: 0.9rem;'>วิเคราะห์รายงานคุณภาพและการใช้พลังงาน พร้อมดูแค็ตตาล็อกสินค้าเพื่อการอัปเกรดระบบ</p>
            </div>
            <p style='color: #009639; font-weight: bold;'>See products ></p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Product Catalog", key="btn_catalog"):
        st.toast("กำลังเปิดหน้า Catalog...")

st.markdown("---")
st.caption("Auth Server: ID-SEA-01 | SNAPCON Enterprise System | Environment: Production")
