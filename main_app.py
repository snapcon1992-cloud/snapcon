import streamlit as st
import hashlib
import hmac
import json
from datetime import datetime, timedelta
import secrets

# ==========================================
# CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="SNAPCON | Automation Solution",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Google Sheets Configuration (ใช้ Streamlit Secrets)
GOOGLE_SCRIPT_URL = st.secrets.get("GOOGLE_SCRIPT_URL", "YOUR_GOOGLE_SCRIPT_URL")
API_SECRET_KEY = st.secrets.get("API_SECRET_KEY", secrets.token_hex(32))

# ==========================================
# SECURITY UTILITIES
# ==========================================
class SecurityManager:
    @staticmethod
    def generate_csrf_token():
        return secrets.token_hex(32)
    
    @staticmethod
    def hash_password(password, salt=None):
        if salt is None:
            salt = secrets.token_hex(16)
        return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex(), salt
    
    @staticmethod
    def generate_session_token(user_id):
        payload = f"{user_id}:{datetime.now().timestamp()}:{secrets.token_hex(16)}"
        signature = hmac.new(API_SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()
        return f"{payload}:{signature}"
    
    @staticmethod
    def verify_session_token(token):
        try:
            parts = token.split(':')
            if len(parts) != 3:
                return None
            payload = f"{parts[0]}:{parts[1]}"
            signature = hmac.new(API_SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()
            if signature != parts[2]:
                return None
            timestamp = float(parts[1])
            if datetime.now().timestamp() - timestamp > 86400:  # 24 hours
                return None
            return parts[0]
        except:
            return None

security = SecurityManager()

# ==========================================
# CACHE MANAGER
# ==========================================
class CacheManager:
    def __init__(self):
        if 'cache' not in st.session_state:
            st.session_state.cache = {}
    
    def get(self, key):
        if key in st.session_state.cache:
            data, expiry = st.session_state.cache[key]
            if datetime.now().timestamp() < expiry:
                return data
            else:
                del st.session_state.cache[key]
        return None
    
    def set(self, key, data, ttl_seconds=3600):
        st.session_state.cache[key] = (data, datetime.now().timestamp() + ttl_seconds)
    
    def clear(self):
        st.session_state.cache = {}

cache = CacheManager()

# ==========================================
# STATE MANAGER
# ==========================================
class StateManager:
    @staticmethod
    def init_state():
        defaults = {
            'language': 'th',
            'is_logged_in': False,
            'user_id': None,
            'session_token': None,
            'cart': [],
            'products': [],
            'spares': [],
            'documents': [],
            'projects': [],
            'articles': [],
            'user_dashboards': {},
            'csrf_token': security.generate_csrf_token()
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    @staticmethod
    def get(key, default=None):
        return st.session_state.get(key, default)
    
    @staticmethod
    def set(key, value):
        st.session_state[key] = value

StateManager.init_state()

# ==========================================
# DATA MANAGER
# ==========================================
class DataManager:
    @staticmethod
    def fetch_from_sheets():
        """ดึงข้อมูลจาก Google Sheets พร้อม Cache"""
        cached_data = cache.get('sheet_data')
        if cached_data:
            return cached_data
        
        try:
            # ใน production ใช้ fetch API ผ่าน JavaScript injection
            # สำหรับตัวอย่างนี้ ใช้ข้อมูลจำลอง
            mock_data = {
                'products': [
                    {'id': '1', 'name': 'Belt Conveyor BC-100', 'price': 250000, 'category': 'conveyor', 
                     'image': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&h=300&fit=crop',
                     'specs': ['Load: 100kg', 'Speed: 0.5-2 m/s', 'Width: 600mm']},
                    {'id': '2', 'name': 'Roller Conveyor RC-200', 'price': 180000, 'category': 'conveyor',
                     'image': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=300&fit=crop',
                     'specs': ['Load: 200kg', 'Speed: 0.3-1.5 m/s', 'Width: 800mm']},
                    {'id': '3', 'name': 'Modular Conveyor MC-300', 'price': 320000, 'category': 'conveyor',
                     'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400&h=300&fit=crop',
                     'specs': ['Load: 300kg', 'Speed: 0.2-2.5 m/s', 'Width: 1000mm']},
                ],
                'spares': [
                    {'id': 's1', 'name': 'Belt PVC 600mm', 'price': 2500, 'category': 'belt',
                     'image': 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=400&h=300&fit=crop',
                     'specs': ['Width: 600mm', 'Thickness: 3mm', 'Material: PVC']},
                ],
                'documents': [
                    {'id': 'd1', 'name': 'BC-100 Datasheet', 'type': 'datasheet', 'url': '#'},
                    {'id': 'd2', 'name': 'RC-200 Drawing', 'type': 'drawing', 'url': '#'},
                ],
                'projects': [
                    {'id': 'p1', 'title': 'Automotive Assembly Line', 'category': 'pilot',
                     'description': 'Complete conveyor system for automotive parts assembly'},
                ],
                'articles': [
                    {'id': 'a1', 'title': 'การเลือกสายพานให้เหมาะกับงาน', 'category': 'Knowledge',
                     'summary': 'บทความแนะนำการเลือกสายพานที่เหมาะสมกับการใช้งาน'},
                ]
            }
            
            cache.set('sheet_data', mock_data, ttl_seconds=1800)  # Cache 30 minutes
            return mock_data
            
        except Exception as e:
            st.error(f"ไม่สามารถโหลดข้อมูลได้: {str(e)}")
            return None

    @staticmethod
    def send_to_sheets(data_type, payload):
        """ส่งข้อมูลไป Google Sheets"""
        try:
            timestamp = datetime.now().isoformat()
            data = {
                'type': data_type,
                'payload': payload,
                'timestamp': timestamp,
                'csrf_token': StateManager.get('csrf_token')
            }
            
            # ใน production: ส่งข้อมูลผ่าน Google Apps Script
            # import requests
            # response = requests.post(GOOGLE_SCRIPT_URL, json=data)
            
            print(f"Data sent to sheets: {json.dumps(data, ensure_ascii=False)}")
            return True
            
        except Exception as e:
            print(f"Error sending data: {str(e)}")
            return False

data_manager = DataManager()

# ==========================================
# MAIN APPLICATION
# ==========================================
def main():
    """Main Streamlit Application"""
    
    # Initialize data
    data = data_manager.fetch_from_sheets()
    if data:
        StateManager.set('products', data.get('products', []))
        StateManager.set('spares', data.get('spares', []))
        StateManager.set('documents', data.get('documents', []))
        StateManager.set('projects', data.get('projects', []))
        StateManager.set('articles', data.get('articles', []))
    
    # Custom CSS
    st.markdown("""
    <style>
        /* Main Styles */
        .main-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 60px 0;
            text-align: center;
            border-radius: 20px;
            margin-bottom: 30px;
        }
        .product-card {
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            margin-bottom: 20px;
            height: 100%;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,179,110,0.15);
        }
        .stat-card {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            border: 1px solid #bbf7d0;
        }
        .price-tag {
            color: #00B36E;
            font-weight: 800;
            font-size: 24px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h1 style="color: #00B36E; font-size: 32px; font-weight: 900; margin-bottom: 0;">SNAPCON</h1>
            <p style="color: #64748b; font-size: 12px; margin-top: 0;">Automation Solution</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Navigation Menu
        menu_options = {
            "🏠 หน้าแรก": "home",
            "📦 สินค้า": "products",
            "🔧 อะไหล่": "spares",
            "📊 Dashboard": "dashboard",
            "📋 โปรเจค": "projects",
            "🏢 เกี่ยวกับเรา": "about",
            "📞 ติดต่อ": "contact",
            "🛒 ตะกร้าสินค้า": "cart"
        }
        
        selected = st.radio("Navigation", list(menu_options.keys()), label_visibility="collapsed")
        current_page = menu_options[selected]
        
        st.divider()
        
        # Login Section
        if not StateManager.get('is_logged_in'):
            with st.expander("🔐 เข้าสู่ระบบ", expanded=True):
                user_id = st.text_input("User ID", key="login_id", placeholder="กรอก User ID")
                password = st.text_input("Password", type="password", key="login_password", placeholder="กรอกรหัสผ่าน")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("เข้าสู่ระบบ", use_container_width=True, type="primary"):
                        if user_id and password:
                            # Simple validation (ใน production ควร verify กับฐานข้อมูล)
                            hashed, salt = security.hash_password(password)
                            StateManager.set('is_logged_in', True)
                            StateManager.set('user_id', user_id)
                            StateManager.set('session_token', security.generate_session_token(user_id))
                            st.success(f"✅ ยินดีต้อนรับ, {user_id}!")
                            st.rerun()
                        else:
                            st.error("❌ กรุณากรอกข้อมูลให้ครบถ้วน")
                with col2:
                    if st.button("สมัครสมาชิก", use_container_width=True):
                        st.info("📝 กรุณากรอกข้อมูลด้านล่าง")
                        
                        with st.form("register_form"):
                            reg_name = st.text_input("ชื่อ-นามสกุล / บริษัท")
                            reg_email = st.text_input("อีเมล")
                            reg_phone = st.text_input("เบอร์โทรศัพท์")
                            
                            if st.form_submit_button("ลงทะเบียน", use_container_width=True):
                                if reg_name and reg_email:
                                    data_manager.send_to_sheets("registration", {
                                        'name': reg_name, 'email': reg_email, 'phone': reg_phone
                                    })
                                    st.success("✅ ลงทะเบียนสำเร็จ!")
                                    st.rerun()
                                else:
                                    st.error("❌ กรุณากรอกข้อมูลให้ครบถ้วน")
        else:
            st.success(f"👤 **{StateManager.get('user_id')}**")
            st.caption(f"Session: {StateManager.get('session_token', '')[:20]}...")
            
            if st.button("🚪 ออกจากระบบ", use_container_width=True):
                StateManager.set('is_logged_in', False)
                StateManager.set('user_id', None)
                StateManager.set('session_token', None)
                cache.clear()
                st.rerun()
        
        # Language Switcher
        st.divider()
        st.caption("🌐 ภาษา / Language")
        lang_col1, lang_col2 = st.columns(2)
        current_lang = StateManager.get('language', 'th')
        with lang_col1:
            if st.button("🇹🇭 ไทย", use_container_width=True, 
                        type="primary" if current_lang == 'th' else "secondary"):
                StateManager.set('language', 'th')
                st.rerun()
        with lang_col2:
            if st.button("🇬🇧 EN", use_container_width=True,
                        type="primary" if current_lang == 'en' else "secondary"):
                StateManager.set('language', 'en')
                st.rerun()
    
    # Main Content Area - Page Router
    if current_page == "home":
        render_home_page(data)
    elif current_page == "products":
        render_products_page(data)
    elif current_page == "spares":
        render_spares_page(data)
    elif current_page == "dashboard":
        render_dashboard_page()
    elif current_page == "projects":
        render_projects_page(data)
    elif current_page == "about":
        render_about_page()
    elif current_page == "contact":
        render_contact_page()
    elif current_page == "cart":
        render_cart_page()

def render_home_page(data):
    """Render Home Page"""
    # Hero Section
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; font-size: 48px; font-weight: 900; margin-bottom: 16px;">
            Snap to Connect.<br>
            <span style="color: #00B36E;">Ready to Control.</span>
        </h1>
        <p style="color: #94a3b8; font-size: 18px; max-width: 600px; margin: 0 auto;">
            ระบบออโตเมชัน Plug & Play ที่พร้อมให้คุณควบคุมสายการผลิตได้ทันที
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h3 style="font-size: 32px; color: #00B36E; margin: 0;">150+</h3>
            <p style="color: #64748b; margin: 0;">โปรเจคที่ทำเสร็จ</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h3 style="font-size: 32px; color: #00B36E; margin: 0;">80+</h3>
            <p style="color: #64748b; margin: 0;">ลูกค้าที่ไว้วางใจ</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h3 style="font-size: 32px; color: #00B36E; margin: 0;">10+</h3>
            <p style="color: #64748b; margin: 0;">ปีประสบการณ์</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="stat-card">
            <h3 style="font-size: 32px; color: #00B36E; margin: 0;">2 ปี</h3>
            <p style="color: #64748b; margin: 0;">การรับประกัน</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Featured Products
    st.header("🌟 สินค้าแนะนำ")
    products = data.get('products', []) if data else []
    
    if products:
        cols = st.columns(3)
        for idx, product in enumerate(products[:3]):
            with cols[idx]:
                st.markdown(f"""
                <div class="product-card">
                    <img src="{product.get('image', 'https://via.placeholder.com/400x300')}" 
                         style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
                    <h3 style="font-weight: 700; font-size: 18px; margin-bottom: 8px;">{product.get('name', 'Product')}</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="price-tag">฿{product.get('price', 0):,}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"เพิ่มลงตะกร้า", key=f"home_add_{product.get('id')}", use_container_width=True):
                    cart = StateManager.get('cart', [])
                    cart.append(product)
                    StateManager.set('cart', cart)
                    st.success(f"✅ เพิ่ม {product.get('name')} ลงตะกร้าแล้ว!")
    else:
        st.info("กำลังโหลดข้อมูลสินค้า...")

def render_products_page(data):
    """Render Products Page"""
    st.header("📦 ผลิตภัณฑ์ของเรา")
    
    # Search and Filter
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 ค้นหาสินค้า", placeholder="พิมพ์ชื่อสินค้า...")
    with col2:
        category_filter = st.selectbox("ประเภท", ["ทั้งหมด", "สายพาน", "โรลเลอร์", "โมดูลาร์"])
    with col3:
        sort_by = st.selectbox("เรียงตาม", ["ล่าสุด", "ราคาต่ำ-สูง", "ราคาสูง-ต่ำ"])
    
    st.divider()
    
    # Product Grid
    products = data.get('products', []) if data else []
    
    if search_query:
        products = [p for p in products if search_query.lower() in p.get('name', '').lower()]
    
    if not products:
        st.warning("🔍 ไม่พบสินค้าที่ค้นหา")
        return
    
    # Display products in grid
    for i in range(0, len(products), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(products):
                product = products[idx]
                with cols[j]:
                    st.markdown(f"""
                    <div class="product-card">
                        <img src="{product.get('image', 'https://via.placeholder.com/400x300')}" 
                             style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
                        <h3 style="font-weight: 700; font-size: 18px; margin-bottom: 8px;">{product.get('name', 'Product')}</h3>
                        <p style="color: #64748b; font-size: 14px; margin-bottom: 12px;">{', '.join(product.get('specs', []))}</p>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="price-tag">฿{product.get('price', 0):,}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button(f"🛒 เพิ่ม", key=f"prod_add_{product.get('id')}", use_container_width=True):
                            cart = StateManager.get('cart', [])
                            cart.append(product)
                            StateManager.set('cart', cart)
                            st.success(f"✅ เพิ่ม {product.get('name')} ลงตะกร้าแล้ว!")
                            st.rerun()
                    with col_btn2:
                        if st.button(f"📋 ดูรายละเอียด", key=f"prod_detail_{product.get('id')}", use_container_width=True):
                            with st.expander(f"รายละเอียด: {product.get('name')}", expanded=True):
                                st.write(f"**รหัสสินค้า:** {product.get('id')}")
                                st.write(f"**ราคา:** ฿{product.get('price', 0):,}")
                                st.write("**สเปค:**")
                                for spec in product.get('specs', []):
                                    st.write(f"- {spec}")

def render_spares_page(data):
    """Render Spare Parts Page"""
    st.header("🔧 อะไหล่และอุปกรณ์เสริม")
    
    spares = data.get('spares', []) if data else []
    
    if not spares:
        st.info("📦 กำลังปรับปรุงข้อมูลอะไหล่")
        return
    
    cols = st.columns(3)
    for idx, spare in enumerate(spares):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{spare.get('image', 'https://via.placeholder.com/400x300')}" 
                     style="width: 100%; height: 180px; object-fit: cover; border-radius: 12px; margin-bottom: 12px;">
                <h3 style="font-weight: 700; font-size: 16px; margin-bottom: 8px;">{spare.get('name', 'Spare Part')}</h3>
                <span class="price-tag">฿{spare.get('price', 0):,}</span>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"เพิ่มลงตะกร้า", key=f"spare_add_{spare.get('id')}", use_container_width=True):
                cart = StateManager.get('cart', [])
                cart.append(spare)
                StateManager.set('cart', cart)
                st.success(f"✅ เพิ่ม {spare.get('name')} ลงตะกร้าแล้ว!")

def render_dashboard_page():
    """Render Dashboard Page"""
    if not StateManager.get('is_logged_in'):
        st.warning("⚠️ กรุณาเข้าสู่ระบบก่อนเข้าใช้งาน Dashboard")
        return
    
    st.header("📊 Dashboard")
    st.success(f"👤 ยินดีต้อนรับ, **{StateManager.get('user_id')}**!")
    
    # Dashboard Controls
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("▶️ START", use_container_width=True, type="primary"):
            st.toast("System Started!", icon="✅")
    with col2:
        if st.button("⏹️ STOP", use_container_width=True):
            st.toast("System Stopped!", icon="⏹️")
    with col3:
        if st.button("🔄 REFRESH", use_container_width=True):
            st.toast("System Refreshed!", icon="🔄")
    with col4:
        report_data = "Date,Output,Carbon,Energy\n2024-01-01,1000,50.5,200.3"
        st.download_button(
            "📥 EXPORT CSV",
            report_data,
            "snapcon_report.csv",
            "text/csv",
            use_container_width=True
        )
    
    st.divider()
    
    # Metrics
    st.subheader("📈 ภาพรวมการผลิต")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Output", "12,450", "+8%")
    with col2:
        st.metric("Carbon Footprint", "245.6 kgCO2e", "-5%")
    with col3:
        st.metric("Energy Used", "1,234 kWh", "+2%")
    with col4:
        st.metric("Efficiency", "94.2%", "+1.5%")
    
    # Production Progress
    st.subheader("🎯 เป้าหมายการผลิต")
    progress = 65
    col1, col2 = st.columns([3, 1])
    with col1:
        st.progress(progress / 100)
    with col2:
        st.markdown(f"### {progress}%")
    st.caption("⏱️ Elapsed: 8h 30m | ⏳ ETA: 4h 15m")
    
    # Machine Status
    st.subheader("🖥️ สถานะเครื่องจักร")
    machine_cols = st.columns(5)
    statuses = ['Running', 'Running', 'Warning', 'Running', 'Maintenance']
    colors = ['🟢', '🟢', '🟡', '🟢', '🔴']
    
    for i, col in enumerate(machine_cols):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 16px; background: white; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="font-size: 24px; margin-bottom: 8px;">{colors[i]}</div>
                <h4 style="font-size: 14px; margin: 0;">Machine {i+1}</h4>
                <p style="color: #64748b; font-size: 12px; margin: 4px 0;">{statuses[i]}</p>
                <p style="color: #00B36E; font-weight: 700; margin: 0;">{1000 + i*200:,} units</p>
            </div>
            """, unsafe_allow_html=True)

def render_projects_page(data):
    """Render Projects Page"""
    st.header("📋 ผลงานและโปรเจคของเรา")
    
    projects = data.get('projects', []) if data else []
    
    if projects:
        for project in projects:
            with st.expander(f"📌 {project.get('title', 'Project')}"):
                st.markdown(f"**ประเภท:** {project.get('category', 'N/A')}")
                st.markdown(f"**รายละเอียด:** {project.get('description', 'No description')}")
    else:
        st.info("ไม่มีข้อมูลโปรเจคในขณะนี้")
    
    st.divider()
    
    # Custom Project Inquiry
    st.subheader("💡 สนใจให้เราออกแบบระบบให้คุณ?")
    with st.form("project_inquiry"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("ชื่อ-นามสกุล")
            email = st.text_input("อีเมล")
        with col2:
            phone = st.text_input("เบอร์โทรศัพท์")
            budget = st.selectbox("งบประมาณ", ["< 100,000", "100,000 - 500,000", "500,000 - 1,000,000", "> 1,000,000"])
        
        details = st.text_area("รายละเอียดโปรเจค", height=150)
        
        if st.form_submit_button("📤 ส่งคำขอ", use_container_width=True):
            if name and email and details:
                data_manager.send_to_sheets("project_inquiry", {
                    'name': name, 'email': email, 'phone': phone,
                    'budget': budget, 'details': details
                })
                st.success("✅ ส่งคำขอเรียบร้อย! เราจะติดต่อกลับภายใน 24 ชั่วโมง")
            else:
                st.error("❌ กรุณากรอกข้อมูลให้ครบถ้วน")

def render_about_page():
    """Render About Page"""
    st.header("🏢 เกี่ยวกับเรา")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 วิสัยทัศน์ของเรา
        มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play 
        ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้
        
        ### 🚀 พันธกิจของเรา
        พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง 
        และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาด
        """)
    
    with col2:
        st.markdown("""
        ### ⭐ ทำไมต้องเลือก SNAPCON?
        - ✅ **10+ ปี** ประสบการณ์ในอุตสาหกรรม
        - ✅ **150+ โปรเจค** ที่ประสบความสำเร็จ
        - ✅ **80+ ลูกค้า** ที่ไว้วางใจ
        - ✅ **รับประกัน 2 ปี** ทุกผลิตภัณฑ์
        - ✅ **บริการหลังการขาย** ตลอด 24 ชม.
        - ✅ **ทีมวิศวกร** ผู้เชี่ยวชาญ
        """)
    
    st.divider()
    
    # Team Section
    st.subheader("👥 ทีมงานของเรา")
    team_cols = st.columns(4)
    roles = ["CEO & Founder", "CTO", "Head of Sales", "Lead Engineer"]
    for i, col in enumerate(team_cols):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #00B36E, #0f172a); 
                     border-radius: 50%; margin: 0 auto 12px; display: flex; align-items: center; justify-content: center;
                     color: white; font-size: 32px; font-weight: bold;">
                    {['S', 'C', 'T', 'E'][i]}
                </div>
                <h4 style="font-weight: 700; margin-bottom: 4px;">Team Member {i+1}</h4>
                <p style="color: #64748b; font-size: 13px;">{roles[i]}</p>
            </div>
            """, unsafe_allow_html=True)

def render_contact_page():
    """Render Contact Page"""
    st.header("📞 ติดต่อเรา")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📍 ข้อมูลติดต่อ
        - 📧 **Email:** snapcon1992@gmail.com
        - 📱 **Line Official:** @SnapconAuto
        - 📞 **โทรศัพท์:** 081-XXX-XXXX
        - 📍 **ที่อยู่:** กรุงเทพมหานคร, ประเทศไทย
        
        ### 🕐 เวลาทำการ
        - จันทร์ - ศุกร์: 8:00 - 17:30
        - เสาร์: 8:00 - 12:00
        - อาทิตย์: หยุดทำการ
        """)
    
    with col2:
        st.subheader("📝 ส่งข้อความถึงเรา")
        with st.form("contact_form"):
            name = st.text_input("ชื่อ-นามสกุล / บริษัท")
            email = st.text_input("อีเมล")
            phone = st.text_input("เบอร์โทรศัพท์")
            subject = st.selectbox("หัวข้อ", ["สอบถามข้อมูลสินค้า", "ขอใบเสนอราคา", "ปัญหาทางเทคนิค", "อื่นๆ"])
            message = st.text_area("ข้อความ", height=150)
            
            if st.form_submit_button("📤 ส่งข้อความ", use_container_width=True):
                if name and email and message:
                    data_manager.send_to_sheets("contact", {
                        'name': name, 'email': email, 'phone': phone,
                        'subject': subject, 'message': message
                    })
                    st.success("✅ ส่งข้อความเรียบร้อย! เราจะติดต่อกลับภายใน 24 ชั่วโมง")
                else:
                    st.error("❌ กรุณากรอกข้อมูลให้ครบถ้วน")

def render_cart_page():
    """Render Cart Page"""
    st.header("🛒 ตะกร้าสินค้า")
    
    cart = StateManager.get('cart', [])
    
    if not cart:
        st.warning("🛒 ตะกร้าสินค้าว่างเปล่า")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🛍️ เลือกดูสินค้า", use_container_width=True, type="primary"):
                st.rerun()
        return
    
    # Display Cart Items
    total_price = 0
    for i, item in enumerate(cart):
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 3, 2, 1])
            with col1:
                st.image(item.get('image', 'https://via.placeholder.com/200'), width=120)
            with col2:
                st.markdown(f"**{item.get('name', 'Product')}**")
                st.caption(f"รหัส: {item.get('id', 'N/A')}")
            with col3:
                quantity = st.number_input(f"จำนวน", min_value=1, value=1, key=f"qty_{i}")
                price = item.get('price', 0) * quantity
                total_price += price
                st.markdown(f"**฿{price:,}**")
            with col4:
                if st.button("🗑️", key=f"remove_{i}"):
                    cart.pop(i)
                    StateManager.set('cart', cart)
                    st.rerun()
            st.divider()
    
    # Cart Summary
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### 💰 ราคารวมทั้งสิ้น")
    with col2:
        st.markdown(f"## ฿{total_price:,}")
    
    # Checkout
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📋 ขอใบเสนอราคา", use_container_width=True, type="primary"):
            if StateManager.get('is_logged_in'):
                data_manager.send_to_sheets("quotation", {
                    'user_id': StateManager.get('user_id'),
                    'cart': cart,
                    'total': total_price
                })
                StateManager.set('cart', [])
                st.success("✅ ส่งคำขอใบเสนอราคาเรียบร้อย! เราจะติดต่อกลับภายใน 24 ชั่วโมง")
                st.balloons()
                st.rerun()
            else:
                st.warning("⚠️ กรุณาเข้าสู่ระบบก่อนขอใบเสนอราคา")

# ==========================================
# RUN APPLICATION
# ==========================================
if __name__ == "__main__":
    main()
