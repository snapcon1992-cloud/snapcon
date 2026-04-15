import streamlit as st
import pandas as pd
import time
import random
import plotly.express as px
import plotly.graph_objects as go

# 1. ระบบรักษาความปลอดภัย: ตรวจสอบการ Login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("⛔ เข้าถึงไม่ได้: กรุณา Login ที่หน้าแรกก่อน")
    if st.button("กลับไปหน้า Login"):
        st.switch_page("main_app.py")
    st.stop()

# 2. ตั้งค่าหน้า Dashboard
st.set_page_config(page_title="Snapcon Live Monitor", layout="wide")

# Custom CSS สำหรับ Industrial Dark Theme
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e2e8f0; }
    
    /* KPI Card Styling */
    .metric-card {
        background: #0f172a;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #1e293b;
        border-left: 5px solid #06b6d4;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-label { color: #94a3b8; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; }
    .metric-value { color: #ffffff; font-size: 1.8rem; font-weight: 800; margin-top: 4px; }
    
    /* Status Badge */
    .status-active { color: #10b981; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนหัว (Header)
col_title, col_status = st.columns([3, 1])
with col_title:
    st.title("📊 Snapcon Live Monitoring")
    st.markdown("สถานะเครือข่าย: <span class='status-active'>● Connected</span> | โปรโตคอล: RS485 Modbus RTU", unsafe_allow_html=True)

with col_status:
    st.write(f"👤 ผู้ใช้งาน: **{st.session_state.get('user_name', 'User')}**")
    if st.button("ออกจากระบบ (Logout)", use_container_width=True):
        st.session_state.logged_in = False
        st.switch_page("main_app.py")

st.divider()

# 4. จำลองข้อมูล (Simulated Data Engine)
nodes = [f"Node-{i+1:02d}" for i in range(10)]
production = [random.randint(150, 600) for _ in range(10)]
health = [random.randint(70, 100) for _ in range(10)]
temp = [random.uniform(35.0, 55.0) for _ in range(10)]

df = pd.DataFrame({
    "Node ID": nodes,
    "Output (Units)": production,
    "Health (%)": health,
    "Temp (°C)": [round(t, 1) for t in temp]
})

# 5. KPI Metrics (Top Row)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">ยอดผลิตรวม (Total)</div><div class="metric-value">{sum(production):,}</div><small>Units</small></div>', unsafe_allow_html=True)
with m2:
    avg_h = sum(health)/10
    color = "#10b981" if avg_h > 85 else "#f59e0b"
    st.markdown(f'<div class="metric-card" style="border-left-color:{color}"><div class="metric-label">ความเสถียรเฉลี่ย</div><div class="metric-value">{avg_h:.1f}%</div><small>System Health</small></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">อุณหภูมิสูงสุด</div><div class="metric-value">{max(temp):.1f}°C</div><small>Peak Temp</small></div>', unsafe_allow_html=True)
with m4:
    st.markdown(f'<div class="metric-card"><div class="metric-label">ลดการปล่อย CO2</div><div class="metric-value">{(sum(production)*0.0072):.2f}</div><small>kgCO2e</small></div>', unsafe_allow_html=True)

st.write("")

# 6. รายละเอียดข้อมูลและการวิเคราะห์ (Main Section)
tab1, tab2 = st.tabs(["📈 สรุปผลเรียลไทม์", "🛠️ สถานะรายเครื่อง (Node Analysis)"])

with tab1:
    col_chart, col_table = st.columns([2, 1])
    with col_chart:
        # กราฟแสดงผลผลิตและสุขภาพ
        fig = px.bar(df, x="Node ID", y="Output (Units)", color="Health (%)",
                     color_continuous_scale="Viridis", title="จำนวนผลผลิตแยกตาม Node (สีบ่งบอกสุขภาพเครื่อง)")
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col_table:
        st.subheader("📋 Machine Summary")
        st.dataframe(df, hide_index=True, use_container_width=True)

with tab2:
    st.subheader("🔍 วิเคราะห์พฤติกรรมเครื่องจักร (AI Insights)")
    col_info = st.columns(5)
    for i in range(10):
        with col_info[i % 5]:
            h_val = health[i]
            t_val = temp[i]
            status_color = "green" if h_val > 80 else "orange" if h_val > 60 else "red"
            
            st.markdown(f"""
            <div style="background:#1e293b; padding:10px; border-radius:10px; margin-bottom:10px; border-top: 3px solid {status_color}">
                <p style="margin:0; font-size:0.7rem; color:#94a3b8;">{nodes[i]}</p>
                <p style="margin:0; font-weight:bold; font-size:1.1rem;">{production[i]} Pcs</p>
                <div style="font-size:0.6rem;">🌡️ {t_val}°C | 💓 {h_val}%</div>
            </div>
            """, unsafe_allow_html=True)

# 7. ระบบบันทึก Log (Event Log)
with st.expander("📝 บันทึกเหตุการณ์ระบบ (System Event Log)"):
    current_time = pd.Timestamp.now().strftime('%H:%M:%S')
    st.caption(f"[{current_time}] : ระบบทำการเชื่อมต่อข้อมูลจาก Modbus Hub สำเร็จ")
    if max(temp) > 50:
        st.warning(f"⚠️ [{current_time}] : ตรวจพบอุณหภูมิสูงผิดปกติที่ {df.loc[df['Temp (°C)'].idxmax(), 'Node ID']}")

# 8. Auto-Refresh
time.sleep(5)
st.rerun()