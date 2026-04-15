import streamlit as st
import pandas as pd
import time
import random
import plotly.express as px

# 1. ระบบรักษาความปลอดภัย: ตรวจสอบการ Login
# หากยังไม่ได้ Login จะถูกเด้งกลับไปหน้า main_app.py
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("⛔ เข้าถึงไม่ได้: กรุณา Login ที่หน้าแรกก่อน")
    if st.button("กลับไปหน้า Login"):
        st.switch_page("main_app.py")
    st.stop()

# 2. ตั้งค่าหน้า Dashboard (ใช้ Layout แบบกว้าง)
st.set_page_config(page_title="Snapcon Live Monitor", layout="wide")

# Custom CSS เพื่อตกแต่งให้เป็นโทน Dark Mode อุตสาหกรรม
st.markdown("""
    <style>
    /* พื้นหลังและตัวอักษร */
    .stApp { background-color: #05070a; color: #e2e8f0; }
    
    /* การ์ด KPI */
    .metric-card {
        background: #0f172a;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #1e293b;
        border-left: 5px solid #06b6d4;
        margin-bottom: 10px;
    }
    .metric-label { color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
    .metric-value { color: #ffffff; font-size: 2rem; font-weight: 800; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนหัวของหน้าจอ (Header)
col_header, col_user = st.columns([4, 1])
with col_header:
    st.title("📊 Snapcon Live Monitoring")
    st.caption(f"Network Status: Connected | RS485 Protocol Active")
with col_user:
    st.markdown(f"👤 **{st.session_state.get('user_name', 'User')}**")
    if st.button("Logout", key="logout_btn"):
        st.session_state.logged_in = False
        st.switch_page("main_app.py")

st.divider()

# 4. จำลองข้อมูล (Data Simulation)
# สร้างข้อมูล 10 โหนดเพื่อแสดงในกราฟและตาราง
nodes = [f"Node-{i+1:02d}" for i in range(10)]
# สุ่มยอดผลิตและสุขภาพเครื่องจักร
production = [random.randint(100, 500) for _ in range(10)]
health = [random.randint(85, 100) for _ in range(10)]

df = pd.DataFrame({
    "Node ID": nodes,
    "Output (Units)": production,
    "Health (%)": health
})

# 5. แสดงผล KPI Cards (แถวบนสุด)
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">ยอดผลิตรวม</div><div class="metric-value">{sum(production):,}</div><small>Units</small></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">ประสิทธิภาพเฉลี่ย</div><div class="metric-value">{sum(health)/10:.1f}%</div><small>System Health</small></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">สถานะ RS485</div><div class="metric-value" style="color:#06b6d4">Active</div><small>Speed: 9600 bps</small></div>', unsafe_allow_html=True)
with k4:
    st.markdown(f'<div class="metric-card"><div class="metric-label">CO2 Reduced</div><div class="metric-value">{(sum(production)*0.007):.2f}</div><small>kgCO2e</small></div>', unsafe_allow_html=True)

st.write("")

# 6. กราฟและตารางข้อมูล (Main Display)
c_left, c_right = st.columns([2, 1])

with c_left:
    # สร้างกราฟแท่งด้วย Plotly
    fig = px.bar(df, x="Node ID", y="Output (Units)", color="Health (%)",
                 color_continuous_scale="GnBu", title="Real-time Production per Node")
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with c_right:
    st.subheader("📋 Machine Details")
    # แสดงตารางข้อมูลดิบ
    st.dataframe(df, hide_index=True, use_container_width=True)

# 7. ระบบ Auto-Refresh (จำลองการดึงข้อมูลทุก 5 วินาที)
time.sleep(5)
st.rerun()