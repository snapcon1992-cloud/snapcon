import streamlit as st

st.set_page_config(layout="wide")

# -------------------------
# STATE (LOGIN)
# -------------------------
if "login" not in st.session_state:
    st.session_state.login = False

# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
body {margin:0;}
.main {padding:0;}

/* LOGIN */
.login-box {
    width: 400px;
    margin: auto;
    margin-top: 80px;
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}

.login-top {
    background: linear-gradient(135deg,#022c22,#064e3b);
    color: white;
    text-align: center;
    padding: 60px 20px;
}

.logo {
    width: 80px;
    height: 80px;
    background: #10b981;
    border-radius: 20px;
    margin: auto;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size: 40px;
    font-weight: bold;
}

.login-bottom {
    background: #f1f5f9;
    padding: 40px;
}

/* BUTTON */
.btn {
    background:#059669;
    color:white;
    padding:15px;
    border-radius:20px;
    text-align:center;
    font-weight:bold;
    cursor:pointer;
}

/* SIDEBAR */
.sidebar {
    background: linear-gradient(180deg,#022c22,#021a17);
    color:white;
    padding:20px;
    height:100vh;
}

/* CARD */
.card {
    background:white;
    padding:25px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,0.05);
}
.metric {
    font-size:32px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# LOGIN PAGE
# -------------------------
if not st.session_state.login:

    st.markdown("""
    <div class="login-box">
        <div class="login-top">
            <div class="logo">S</div>
            <h1>SNAPCON</h1>
            <p>ENTERPRISE CONTROL UNIT</p>
        </div>
        <div class="login-bottom">
    """, unsafe_allow_html=True)

    user = st.text_input("Employee ID")
    pwd = st.text_input("Access Token", type="password")

    if st.button("AUTHENTICATE"):
        st.session_state.login = True
        st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

# -------------------------
# DASHBOARD
# -------------------------
else:

    # Sidebar
    st.sidebar.markdown("## SNAPCON")
    page = st.sidebar.radio("", ["Home", "Dashboard"])

    st.title("Plant Telemetry")
    st.caption("Monitoring real-time production")

    # KPI
    c1, c2, c3, c4 = st.columns(4)

    c1.markdown('<div class="card"><div>OEE</div><div class="metric">94.2%</div></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><div>Output</div><div class="metric">4,500</div></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><div>Alerts</div><div class="metric">03</div></div>', unsafe_allow_html=True)
    c4.markdown('<div class="card"><div>Uptime</div><div class="metric">99.9%</div></div>', unsafe_allow_html=True)

    st.write("")

    # Table
    data = [
        ["L01","Running",98,1250],
        ["L02","Running",95,1100],
        ["L03","Warning",82,850],
        ["L04","Running",97,1300],
        ["L05","Stopped",0,0],
    ]

    st.table(data)
