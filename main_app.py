import streamlit as st
import pandas as pd

st.set_page_config(page_title="Snapcon Dashboard", layout="wide")

# -----------------------
# Sample Data
# -----------------------
production_lines = [
    {"Line": "L01", "Status": "Running", "Efficiency": 98, "Output": 1250, "Energy": 12},
    {"Line": "L02", "Status": "Running", "Efficiency": 95, "Output": 1100, "Energy": 14},
    {"Line": "L03", "Status": "Warning", "Efficiency": 82, "Output": 850, "Energy": 10},
    {"Line": "L04", "Status": "Running", "Efficiency": 97, "Output": 1300, "Energy": 15},
    {"Line": "L05", "Status": "Stopped", "Efficiency": 0, "Output": 0, "Energy": 1},
]

df = pd.DataFrame(production_lines)

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("SNAPCON")
page = st.sidebar.radio("Menu", ["Home", "Dashboard"])

# -----------------------
# Home Page
# -----------------------
if page == "Home":
    st.title("🏭 Snapcon Control Center")
    st.write("Real-time Production Monitoring")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("OEE", "94.2%", "+1.2%")
    col2.metric("Output", "4500", "+420")
    col3.metric("Alerts", "3", "-1")
    col4.metric("Uptime", "99.9%", "MAX")

    st.subheader("Production Lines")
    st.dataframe(df, use_container_width=True)

# -----------------------
# Dashboard Page
# -----------------------
elif page == "Dashboard":
    st.title("📊 Engineer Dashboard")

    st.subheader("Line Efficiency")

    for i in range(len(df)):
        st.progress(df.loc[i, "Efficiency"] / 100)
        st.write(f"{df.loc[i, 'Line']} - {df.loc[i, 'Efficiency']}%")
