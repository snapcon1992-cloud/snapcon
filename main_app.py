import streamlit as st
import pandas as pd

st.set_page_config(page_title="Snapcon Automation", layout="wide")

# -------------------------
# STYLE (Industrial Theme)
# -------------------------
st.markdown("""
<style>
body {
    background-color: #0a1e1a;
}
.main {
    background-color: #0a1e1a;
    color: white;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(16,185,129,0.2);
}
.metric {
    font-size: 32px;
    font-weight: bold;
    color: #10b981;
}
.title {
    font-size: 42px;
    font-weight: 900;
}
.subtitle {
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER (Hero Section)
# -------------------------
st.markdown('<div class="title">SNAPCON AUTOMATION</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Intelligent Industrial Solutions</div>', unsafe_allow_html=True)

st.write("")

# -------------------------
# KPI Section
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.markdown('<div class="card"><div>OEE</div><div class="metric">94%</div></div>', unsafe_allow_html=True)
col2.markdown('<div class="card"><div>Output</div><div class="metric">4,500</div></div>', unsafe_allow_html=True)
col3.markdown('<div class="card"><div>Alerts</div><div class="metric">3</div></div>', unsafe_allow_html=True)
col4.markdown('<div class="card"><div>Uptime</div><div class="metric">99.9%</div></div>', unsafe_allow_html=True)

st.write("")

# -------------------------
# SAMPLE DATA
# -------------------------
data = [
    {"Line": "L01", "Status": "Running", "Efficiency": 98, "Output": 1250},
    {"Line": "L02", "Status": "Running", "Efficiency": 95, "Output": 1100},
    {"Line": "L03", "Status": "Warning", "Efficiency": 82, "Output": 850},
    {"Line": "L04", "Status": "Running", "Efficiency": 97, "Output": 1300},
    {"Line": "L05", "Status": "Stopped", "Efficiency": 0, "Output": 0},
]

df = pd.DataFrame(data)

# -------------------------
# TABLE (Telemetry)
# -------------------------
st.markdown("### 📊 Production Lines")

st.dataframe(df, use_container_width=True)

# -------------------------
# PROGRESS BAR (SCADA Style)
# -------------------------
st.markdown("### ⚙️ Efficiency Monitor")

for i in range(len(df)):
    st.write(f"{df.loc[i, 'Line']} - {df.loc[i, 'Efficiency']}%")
    st.progress(df.loc[i, "Efficiency"] / 100)

# -------------------------
# FOOTER
# -------------------------
st.write("---")
st.markdown("© 2026 Snapcon Automation")
