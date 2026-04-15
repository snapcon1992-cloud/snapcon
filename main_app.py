import streamlit as st
import pandas as pd
import time
import random
import plotly.express as px

# การตั้งค่าหน้าจอ
st.set_page_config(
    page_title="SNAPCON | Automation Solutions",
    page_icon="🌿",
    layout="wide"
)

# --- SESSION STATE สำหรับเก็บค่าการรัน ---
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'prod_counts' not in st.session_state:
    st.session_state.prod_counts = [random.randint(100, 200) for _ in range(10)]
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# CSS เพื่อความสวยงาม (อิงจากแบบเดิมที่คุณชอบ)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    .metric-card {
        background: #161b22; 
        border: 1px solid #30363d; 
        border-radius: 12px; 
        padding: 1.5rem;
        border-left: 5px solid #22d3ee;
    }
    .node-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- ส่วน LOGIN ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align:center;'>SNAPCON LOGIN</h1>", unsafe_allow_html=True)
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("เข้าสู่ระบบ"):
            if user == "001" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("รหัสผ่านไม่ถูกต้อง")
    st.stop()

# --- ส่วนเนื้อหาหลักเมื่อ Login แล้ว ---
# Header
h_col1, h_col2 = st.columns([3, 1])
with h_col1:
    st.title("🔌 SNAPCON CONTROL PANEL")
    st.write("Smart Production Monitoring System")

with h_col2:
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

st.divider()

# Control Buttons (ปุ่ม Start/Stop/Reset ที่กลับมาใช้ได้)
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("▶ START SYSTEM", type="primary"):
        st.session_state.is_running = True
with c2:
    if st.button("⏹ STOP SYSTEM"):
        st.session_state.is_running = False
with c3:
    if st.button("🔄 RESET COUNTER"):
        st.session_state.prod_counts = [0] * 10
with c4:
    status_text = "🟢 ONLINE" if st.session_state.is_running else "🔴 OFFLINE"
    st.markdown(f"### {status_text}")

# Logic จำลองการผลิต
if st.session_state.is_running:
    for i in range(10):
        if random.random() > 0.5:
            st.session_state.prod_counts[i] += 1
    time.sleep(0.5)
    st.rerun()

# แสดงผล KPI
total_prod = sum(st.session_state.prod_counts)
k1, k2, k3 = st.columns(3)
with k1:
    st.markdown(f'<div class="metric-card"><div>Total Production</div><div style="font-size:2rem; font-weight:bold;">{total_prod:,}</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="metric-card"><div>Carbon Saving</div><div style="font-size:2rem; font-weight:bold;">{total_prod * 0.0072:.2f} kg</div></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="metric-card"><div>System Health</div><div style="font-size:2rem; font-weight:bold;">98.5%</div></div>', unsafe_allow_html=True)

st.write("")
st.subheader("🌐 Real-time Node Status")

# แสดงผลราย Node
for r in range(2):
    row = st.columns(5)
    for c in range(5):
        idx = (r * 5) + c
        with row[c]:
            st.markdown(f"""
                <div class="node-card">
                    <div style="color:#94a3b8; font-size:0.8rem;">Node {idx+1:02d}</div>
                    <div style="font-size:1.5rem; font-weight:bold;">{st.session_state.prod_counts[idx]}</div>
                    <div style="color:#10b981; font-size:0.7rem;">● Connected</div>
                </div>
            """, unsafe_allow_html=True)

# กราฟสรุปผล
st.write("")
df = pd.DataFrame({
    "Node": [f"N{i+1}" for i in range(10)],
    "Output": st.session_state.prod_counts
})
fig = px.bar(df, x="Node", y="Output", title="Production Overview per Node", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)
