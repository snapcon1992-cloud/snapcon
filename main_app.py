import streamlit as st

st.set_page_config(layout="wide")

# -------------------------
# GLOBAL STYLE (SEW Style)
# -------------------------
st.markdown("""
<style>
body {
    margin:0;
}
.main {
    padding: 0;
}

/* HERO */
.hero {
    position: relative;
    height: 500px;
    background-image: url("https://images.unsplash.com/photo-1581092918056-0c4c3acd3789");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
}

/* overlay */
.hero-overlay {
    background: rgba(255,255,255,0.85);
    padding: 40px;
    max-width: 500px;
    margin-left: 80px;
    border-radius: 10px;
}

/* TEXT */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #333;
}
.subtitle {
    font-size: 16px;
    color: #666;
}
.cta {
    color: red;
    font-weight: bold;
    margin-top: 20px;
}

/* SECTION */
.section {
    padding: 80px 60px;
    text-align: center;
}

/* CARD */
.card {
    padding: 40px;
    border-radius: 10px;
    border: 1px solid #eee;
    transition: 0.3s;
}
.card:hover {
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown("""
<div class="hero">
    <div class="hero-overlay">
        <div class="subtitle">SNAPCON INDUSTRIAL SYSTEM</div>
        <div class="title">Compact<br>and powerful.</div>
        <div class="cta">→ Find out more</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# SPACE
# -------------------------
st.write("")

# -------------------------
# SECTION: FEATURES
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📄 Data & Documents</h3>
        <p>Technical drawings, datasheets, and system files</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>⚙️ Direct to Product</h3>
        <p>Access Snapcon modules and configurations instantly</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# SECTION: SNAPCON VALUE
# -------------------------
st.markdown("""
<div class="section">
    <h2>Smart Factory Solutions</h2>
    <p>Snapcon integrates PLC, IoT, and AI to deliver real-time industrial automation.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.write("---")
st.write("© Snapcon Automation")
