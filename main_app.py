import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Snapcon Dashboard",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for UI Enhancement
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #061a16;
        color: white;
    }
    .resource-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .resource-icon {
        background: rgba(16, 185, 129, 0.2);
        padding: 5px 10px;
        border-radius: 5px;
        color: #10b981;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sample Data
production_lines = [
    {"Line": "L01", "Status": "Running", "Efficiency": 98, "Output": 1250, "Energy": 12},
    {"Line": "L02", "Status": "Running", "Efficiency": 95, "Output": 1100, "Energy": 14},
    {"Line": "L03", "Status": "Warning", "Efficiency": 82, "Output": 850, "Energy": 10},
    {"Line": "L04", "Status": "Running", "Efficiency": 97, "Output": 1300, "Energy": 15},
    {"Line": "L05", "Status": "Stopped", "Efficiency": 0, "Output": 0, "Energy": 1},
]
df = pd.DataFrame(production_lines)

# 4. Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='color: white;'>SNAPCON</h1>", unsafe_allow_html=True)
    page = st.radio("Menu", ["Home", "Dashboard"])
    
    st.markdown("---")
    st.markdown("<p style='color: #64748b; font-size: 0.8rem;'>RESOURCES</p>", unsafe_allow_html=True)
    
    resources = [
        {"name": "Manual.pdf", "icon": "📄"},
        {"name": "Map.dwg", "icon": "📐"},
        {"name": "ISO_9001.pdf", "icon": "🛡️"}
    ]
    
    for res in resources:
        st.markdown(f"""
            <div class="resource-card">
                <div class="resource-icon">{res['icon']}</div>
                <div style="color: white; font-size: 0.8rem;">{res['name']}</div>
            </div>
        """, unsafe_allow_html=True)

# 5. Main Content Logic
if page == "Home":
    st.title("🏭 Snapcon Control Center")
    st.write("Real-time Production Monitoring")

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("OEE", "94.2%", "1.2%")
    m2.metric("Output", "4,500 units", "420")
    m3.metric("Alerts", "3", "-1", delta_color="inverse")
    m4.metric("Uptime", "99.9%", "MAX")

    st.subheader("Current Status of Production Lines")
    
    # Define color logic for the Status column
    def apply_color(row):
        val = row['Status']
        color = '#2ecc71' if val == 'Running' else '#f1c40f' if val == 'Warning' else '#e74c3c'
        return [f'color: {color}; font-weight: bold' if i == 1 else '' for i, _ in enumerate(row)]

    # Use style.apply for row-level or column-level formatting
    styled_df = df.style.apply(apply_color, axis=1)

    st.dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )

elif page == "Dashboard":
    st.title("📊 Engineer Dashboard")
    st.subheader("Line Efficiency Analysis")

    # Detailed Progress Bars
    cols = st.columns(len(df))
    for i in range(len(df)):
        with cols[i]:
            line_data = df.iloc[i]
            st.write(f"**{line_data['Line']}**")
            st.progress(int(line_data['Efficiency']))
            st.caption(f"Efficiency: {line_data['Efficiency']}%")
            
            if line_data['Efficiency'] < 85 and line_data['Efficiency'] > 0:
                st.warning("Maintenance")
            elif line_data['Efficiency'] == 0:
                st.error("Offline")
            else:
                st.success("Optimal")

    st.divider()
    st.subheader("Energy vs Output Correlation")
    st.scatter_chart(df, x="Output", y="Energy", color="Line", size="Efficiency")
