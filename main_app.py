import streamlit as st
import pandas as pd

# 1. การตั้งค่าหน้ากระดาษ (ให้ความรู้สึกพรีเมียมแบบ SEW)
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
        color: #009639; /* สีเขียวหลักของ Snapcon */
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        border-left: 3px solid #009639;
        padding-left: 15px;
        margin-bottom: 30px;
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
    }
    .stButton > button:hover {
        border-color: #009639;
        color: #009639;
    }
    
    /* แบนเนอร์หน้าหลัก */
    .hero-section {
        background-color: #f8f9fa;
        padding: 60px 40px;
        border-radius: 10px;
        margin-bottom: 40px;
        border-bottom: 5px solid #009639;
    }
    
    /* การ์ดฟีเจอร์ */
    .feature-card {
        padding: 20px;
        background: white;
        border: 1px solid #eee;
        border-radius: 8px;
        text-align: center;
        transition: 0.3s;
    }
    .feature-card:hover {
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. การจัดการสถานะ (Session State) เพื่อเปลี่ยนหน้า
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# 4. Sidebar (จัดระเบียบใหม่ให้ไม่ซ้ำซ้อน)
with st.sidebar:
    st.markdown("<h2 style='color: #009639;'>SNAPCON</h2>", unsafe_allow_html=True)
    
    # ข้อมูลผู้ใช้งาน
    st.info("👤 **Logged in as:**\nWatanabe San\n*Senior Engineer*")
    
    st.markdown("---")
    st.write("🔍 **Navigation**")
    
    if st.button("🏠 Home"):
        st.session_state.current_page = "Home"
    if st.button("📊 My Dashboard"):
        st.session_state.current_page = "Dashboard"
    if st.button("📞 Contact Support"):
        st.session_state.current_page = "Contact"
        
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
        st.warning("Logging out...")

# 5. เนื้อหาในแต่ละหน้า
if st.session_state.current_page == "Home":
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <h1 style='font-size: 3.5rem; margin-bottom: 10px;'>Cool running. <br><span style='color: #009639;'>Long life.</span></h1>
            <p style='font-size: 1.2rem; color: #666;'>Industrial Automation Solutions for a Greener Future.</p>
            <p style='color: #009639; font-weight: bold; cursor: pointer;'>Find out more ></p>
        </div>
    """, unsafe_allow_html=True)

    # Features Grid (เหมือนในภาพ SEW)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3 style='color: #333;'>📄 Data & Documents</h3>
                <p style='color: #777; font-size: 0.9rem;'>เข้าถึงคู่มือการใช้งานและเอกสารเทคนิค</p>
                <p style='color: #009639;'>Explore v</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3 style='color: #333;'>⚙️ Product Status</h3>
                <p style='color: #777; font-size: 0.9rem;'>ตรวจสอบสถานะเครื่องจักรแบบเรียลไทม์</p>
                <p style='color: #009639;'>Monitor v</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="feature-card">
                <h3 style='color: #333;'>🛡️ Quality Control</h3>
                <p style='color: #777; font-size: 0.9rem;'>รายงานประสิทธิภาพและการใช้พลังงาน</p>
                <p style='color: #009639;'>View Reports v</p>
            </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "Dashboard":
    st.title("📊 Production Dashboard")
    # ตัวอย่างข้อมูล
    chart_data = pd.DataFrame({
        "Time": range(10),
        "Efficiency": [85, 88, 87, 90, 92, 91, 89, 93, 95, 94]
    })
    st.line_chart(chart_data, x="Time", y="Efficiency")
    st.success("All systems operational.")

elif st.session_state.current_page == "Contact":
    st.title("📞 Contact Support")
    st.write("หากพบปัญหาทางเทคนิค กรุณาติดต่อวิศวกรประจำเขตของท่าน")
    st.text_input("Subject")
    st.text_area("Message")
    if st.button("Send Message"):
        st.balloons()
