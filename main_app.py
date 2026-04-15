import streamlit as st
import pandas as pd
import time
import random
import plotly.express as px

# การตั้งค่าหน้าจอ
st.set_page_config(
    page_title="SNAPCON | Automation Solutions",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE สำหรับเก็บค่าการรัน ---
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'prod_counts' not in st.session_state:
    st.session_state.prod_counts = [random.randint(100, 200) for _ in range(10)]
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# CSS เพื่อเปลี่ยนสไตล์เป็นแบบสว่าง (Light Theme) ตามรูปภาพที่ส่งมา
st.markdown("""
    <style>
    /* ตั้งค่าพื้นหลังแอปเป็นสีเทาอ่อนแบบสะอาดตา */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }

    /* สไตล์ Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Card สำหรับแสดงตัวเลข KPI */
    .metric-card {
        background: #ffffff; 
        border: 1px solid #e2e8f0; 
        border-radius: 16px; 
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .metric-label {
        color: #64748b;
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        color: #0f172a;
        font-size: 2rem;
        font-weight: 800;
    }

    /* Card สำหรับ Node */
    .node-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* สไตล์ปุ่มกด */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        transition: all 0.2s;
    }
    
    /* ปุ่ม Start สีเขียว */
    .stButton>button[kind="primary"] {
        background-color: #10b981 !important;
        border: none !important;
    }

    /* แถบหัวข้อ */
    .section-header {
        border-left: 5px solid #3b82f6;
        padding-left: 15px;
        margin: 25px 0 15px 0;
        font-weight: 800;
        color: #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# --- ส่วน LOGIN ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div style='text-align:center; padding: 50px 0;'>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:#0f172a; margin-bottom:10px;'>SNAPCON</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748b;'>Industrial Automation Monitoring System</p>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("<div style='background:white; padding:30px; border-radius:20px; border:1px solid #e2e8f0;'>", unsafe_allow_html=True)
            user = st.text_input("Username", placeholder="ระบุชื่อผู้ใช้")
            pwd = st.text_input("Password", type="password", placeholder="ระบุรหัสผ่าน")
            if st.button("SIGN IN", use_container_width=True, type="primary"):
                if user == "001" and pwd == "123":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- ส่วนเนื้อหาหลัก (เมื่อ Login แล้ว) ---

# Sidebar Navigation & User Info
with st.sidebar:
    st.markdown("<h2 style='color:#0f172a;'>SNAPCON</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:0.8rem;'>V 2.5 Enterprise</p>", unsafe_allow_html=True)
    st.divider()
    
    st.write("👤 User: Admin (001)")
    if st.button("Log Out", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()
    
    st.divider()
    st.markdown("### System Controls")
    if st.button("▶ START SYSTEM", type="primary", use_container_width=True):
        st.session_state.is_running = True
    if st.button("⏹ STOP SYSTEM", use_container_width=True):
        st.session_state.is_running = False
    if st.button("🔄 RESET COUNTER", use_container_width=True):
        st.session_state.prod_counts = [0] * 10

# Header Section
h_col1, h_col2 = st.columns([3, 1])
with h_col1:
    st.markdown("<h1 style='color:#0f172a; margin-bottom:0;'>Dashboard Overview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>ติดตามสถานะการผลิตแบบเรียลไทม์</p>", unsafe_allow_html=True)

with h_col2:
    status_color = "#10b981" if st.session_state.is_running else "#ef4444"
    status_text = "Running" if st.session_state.is_running else "Stopped"
    st.markdown(f"""
        <div style="text-align:right; margin-top:20px;">
            <span style="background:{status_color}22; color:{status_color}; padding:8px 16px; border-radius:30px; font-weight:bold; font-size:0.9rem; border:1px solid {status_color}55;">
                ● {status_text}
            </span>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# Logic จำลองการผลิต (Auto rerun)
if st.session_state.is_running:
    for i in range(10):
        if random.random() > 0.4: # โอกาสเพิ่มค่า
            st.session_state.prod_counts[i] += 1
    time.sleep(1)
    st.rerun()

# --- KPI Section (Cards) ---
total_prod = sum(st.session_state.prod_counts)
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">TOTAL PRODUCTION</div>
            <div class="metric-value">{total_prod:,}</div>
            <div style="color:#10b981; font-size:0.8rem; margin-top:5px;">↑ 12% from last shift</div>
        </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">CARBON SAVING</div>
            <div class="metric-value">{total_prod * 0.0072:.2f} <span style='font-size:1rem;'>kg</span></div>
            <div style="color:#64748b; font-size:0.8rem; margin-top:5px;">Eco-Friendly Rating: A</div>
        </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">AVG MACHINE HEALTH</div>
            <div class="metric-value">98.2%</div>
            <div style="color:#10b981; font-size:0.8rem; margin-top:5px;">Optimal Condition</div>
        </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">ACTIVE NODES</div>
            <div class="metric-value">10 / 10</div>
            <div style="color:#3b82f6; font-size:0.8rem; margin-top:5px;">RS485 Connected</div>
        </div>
    """, unsafe_allow_html=True)

# --- Node Status Section ---
st.markdown("<div class='section-header'>Real-time Node Status</div>", unsafe_allow_html=True)

for r in range(2):
    row = st.columns(5)
    for c in range(5):
        idx = (r * 5) + c
        with row[c]:
            st.markdown(f"""
                <div class="node-card">
                    <div style="color:#64748b; font-size:0.75rem; font-weight:bold; margin-bottom:10px;">NODE {idx+1:02d}</div>
                    <div style="font-size:1.8rem; font-weight:800; color:#0f172a;">{st.session_state.prod_counts[idx]}</div>
                    <div style="height:4px; width:40%; background:#3b82f6; margin: 10px auto; border-radius:2px;"></div>
                    <div style="color:#10b981; font-size:0.7rem; font-weight:bold;">● Active</div>
                </div>
            """, unsafe_allow_html=True)

# --- Visualization Section ---
st.markdown("<div class='section-header'>Production Analytics</div>", unsafe_allow_html=True)
col_graph, col_table = st.columns([2, 1])

with col_graph:
    df = pd.DataFrame({
        "Node": [f"N{i+1}" for i in range(10)],
        "Output": st.session_state.prod_counts
    })
    fig = px.bar(
        df, x="Node", y="Output", 
        color="Output", 
        color_continuous_scale="Blues",
        text_auto=True
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20),
        height=350,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

with col_table:
    st.markdown("<p style='font-size:0.9rem; font-weight:bold; color:#64748b;'>Recent Log History</p>", unsafe_allow_html=True)
    log_data = {
        "Time": [time.strftime("%H:%M:%S") for _ in range(5)],
        "Event": ["Sync Data", "Health Check", "Target Reach", "Node 05 Peak", "System Init"],
        "Status": ["Success", "Success", "Warning", "Info", "Success"]
    }
    st.table(pd.DataFrame(log_data))

st.markdown("<br><hr style='border-color:#e2e8f0;'><p style='text-align:center; color:#94a3b8; font-size:0.8rem;'>SNAPCON Automation Solution © 2024</p>", unsafe_allow_html=True)
