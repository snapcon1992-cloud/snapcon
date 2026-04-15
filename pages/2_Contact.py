import streamlit as st

# 1. ระบบรักษาความปลอดภัย: ตรวจสอบการ Login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("⛔ เข้าถึงไม่ได้: กรุณา Login ที่หน้าแรกก่อน")
    if st.button("กลับไปหน้า Login"):
        st.switch_page("main_app.py")
    st.stop()

# 2. ตั้งค่าหน้า Dashboard
st.set_page_config(page_title="Snapcon | Contact Support", layout="wide")

# Custom CSS สำหรับหน้า Contact
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e2e8f0; }
    .contact-card {
        background: #0f172a;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #1e293b;
        margin-bottom: 20px;
        text-align: center;
    }
    .icon-circle {
        background: #1e293b;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px auto;
        color: #06b6d4;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header
col_back, col_title = st.columns([1, 5])
with col_back:
    if st.button("⬅️ กลับหน้าหลัก"):
        st.switch_page("main_app.py")

st.title("📞 ติดต่อฝ่ายสนับสนุนเทคนิค")
st.write("หากคุณพบปัญหาในการใช้งานระบบ Snapcon หรือต้องการปรึกษาการติดตั้ง Hardware เพิ่มเติม")

st.divider()

# 4. Contact Methods
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="contact-card">
        <div class="icon-circle">📱</div>
        <h3>สายด่วนวิศวกร</h3>
        <p>081-XXX-XXXX</p>
        <p style="font-size: 0.8rem; color: #94a3b8;">จันทร์ - ศุกร์ (08:30 - 17:30)</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="contact-card">
        <div class="icon-circle">💬</div>
        <h3>Line Official</h3>
        <p>@SnapconAuto</p>
        <p style="font-size: 0.8rem; color: #94a3b8;">ตอบกลับภายใน 24 ชม.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="contact-card">
        <div class="icon-circle">📧</div>
        <h3>Email Support</h3>
        <p>support@snapcon.com</p>
        <p style="font-size: 0.8rem; color: #94a3b8;">สำหรับแจ้งปัญหาเชิงเทคนิค</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# 5. Support Form
st.subheader("🛠️ แจ้งซ่อมหรือสอบถามข้อมูลเพิ่มเติม")
with st.form("contact_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        name = st.text_input("ชื่อผู้ติดต่อ", value=st.session_state.get('user_name', ''))
        node_id = st.selectbox("เลือก Node ที่มีปัญหา", ["ทั่วไป", "Node-01", "Node-02", "Node-03", "Node-04", "Node-05", "Node-06", "Node-07", "Node-08", "Node-09", "Node-10"])
    with col_f2:
        subject = st.text_input("หัวข้อปัญหา")
        priority = st.select_slider("ระดับความเร่งด่วน", options=["ปกติ", "ปานกลาง", "เร่งด่วน"])
    
    msg = st.text_area("รายละเอียดปัญหา")
    submit = st.form_submit_button("ส่งข้อมูลไปยังวิศวกร", use_container_width=True)
    
    if submit:
        if not subject or not msg:
            st.error("กรุณากรอกหัวข้อและรายละเอียดปัญหา")
        else:
            st.success("ส่งข้อมูลสำเร็จ! ทีมวิศวกรจะติดต่อกลับหาคุณโดยเร็วที่สุด")
            # ในอนาคตสามารถเพิ่ม code ส่ง email หรือ line notify ตรงนี้ได้

# 6. Footer
st.divider()
st.caption("Snapcon Automation Solution - Industrial IoT & Predictive Maintenance")