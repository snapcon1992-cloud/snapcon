
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
# HTML TEMPLATES
# ==========================================
class HTMLTemplates:
    @staticmethod
    def get_css():
        return """
        <style>
            /* Base Reset */
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Inter', 'Prompt', sans-serif; background: #f8fafc; }
            
            /* Loading Skeleton */
            .skeleton {
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
                border-radius: 8px;
            }
            @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
            
            /* Toast Notifications */
            .toast-container { position: fixed; top: 80px; right: 20px; z-index: 10000; display: flex; flex-direction: column; gap: 10px; }
            .toast { padding: 16px 24px; border-radius: 12px; color: white; font-weight: 600; font-size: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); animation: slideInRight 0.3s ease; min-width: 300px; backdrop-filter: blur(10px); }
            .toast.success { background: #059669; border-left: 4px solid #047857; }
            .toast.error { background: #dc2626; border-left: 4px solid #b91c1c; }
            .toast.warning { background: #d97706; border-left: 4px solid #b45309; }
            .toast.info { background: #2563eb; border-left: 4px solid #1d4ed8; }
            @keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
            
            /* Mobile Menu */
            .mobile-menu-overlay {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.9); z-index: 1000; transform: translateX(100%);
                transition: transform 0.3s ease-in-out;
            }
            .mobile-menu-overlay.open { transform: translateX(0); }
            
            /* Card Hover Effects */
            .product-card {
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                cursor: pointer;
            }
            .product-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0,179,110,0.1);
            }
            
            /* Custom Scrollbar */
            ::-webkit-scrollbar { width: 8px; height: 8px; }
            ::-webkit-scrollbar-track { background: #f1f5f9; }
            ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
            ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
            
            /* Progress Bar Animation */
            .progress-bar { transition: width 0.5s ease-in-out; }
            
            /* Modal Backdrop */
            .modal-backdrop {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.7); z-index: 2000; display: flex;
                align-items: center; justify-content: center; animation: fadeIn 0.2s ease;
            }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        </style>
        """
    
    @staticmethod
    def get_loading_skeleton():
        return """
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 p-4">
            <div class="skeleton h-64"></div>
            <div class="skeleton h-64"></div>
            <div class="skeleton h-64"></div>
            <div class="skeleton h-64"></div>
        </div>
        """

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
                ],
                'spares': [
                    {'id': 's1', 'name': 'Belt PVC 600mm', 'price': 2500, 'category': 'belt',
                     'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400&h=300&fit=crop',
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
            # ใน production ส่งผ่าน Google Apps Script
            timestamp = datetime.now().isoformat()
            data = {
                'type': data_type,
                'payload': payload,
                'timestamp': timestamp,
                'csrf_token': StateManager.get('csrf_token')
            }
            
            # จำลองการส่งข้อมูลสำเร็จ
            print(f"Data sent to sheets: {json.dumps(data, ensure_ascii=False)}")
            return True
            
        except Exception as e:
            print(f"Error sending data: {str(e)}")
            return False

data_manager = DataManager()

# ==========================================
# COMPONENT RENDERER
# ==========================================
class ComponentRenderer:
    @staticmethod
    def render_product_card(product):
        """แสดงการ์ดสินค้า"""
        return f"""
        <div class="product-card bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
            <div class="bg-gray-50 h-48 rounded-xl mb-4 flex items-center justify-center overflow-hidden">
                <img src="{product.get('image', 'https://via.placeholder.com/400x300')}" 
                     alt="{product.get('name', 'Product')}"
                     class="w-full h-full object-cover"
                     loading="lazy">
            </div>
            <h3 class="font-bold text-lg text-gray-900 mb-2">{product.get('name', 'Product')}</h3>
            <p class="text-green-600 font-bold text-xl mb-4">฿{product.get('price', 0):,}</p>
            <button onclick="addToCart('{product.get('id')}')" 
                    class="w-full bg-gray-900 text-white py-3 rounded-xl font-bold hover:bg-green-600 transition-colors">
                <i class="fas fa-cart-plus mr-2"></i> เพิ่มลงตะกร้า
            </button>
        </div>
        """
    
    @staticmethod
    def render_dashboard_node(node):
        """แสดงสถานะเครื่องจักรใน Dashboard"""
        status_color = {'Running': 'green', 'Warning': 'yellow', 'Maintenance': 'red', 'Offline': 'gray'}
        color = status_color.get(node.get('status', 'Offline'), 'gray')
        
        return f"""
        <div class="bg-white rounded-xl p-3 shadow-sm border border-gray-200">
            <div class="flex justify-between items-center mb-2">
                <span class="text-xs font-bold text-gray-500">{node.get('name', 'Node')}</span>
                <div class="w-2 h-2 bg-{color}-500 rounded-full animate-pulse"></div>
            </div>
            <h4 class="text-xl font-black text-center my-2">{node.get('output', 0)}</h4>
            <div class="w-full h-2 bg-gray-200 rounded-full">
                <div class="h-full bg-{color}-500 rounded-full transition-all" 
                     style="width: {node.get('health', 100)}%"></div>
            </div>
            <p class="text-xs text-center mt-1 text-gray-500">Health: {node.get('health', 100):.1f}%</p>
        </div>
        """

# ==========================================
# JAVASCRIPT INJECTOR
# ==========================================
class JSInjector:
    @staticmethod
    def get_core_scripts():
        """ส่ง JavaScript หลักไปยังหน้าเว็บ"""
        return f"""
        <script>
            // Toast Notification System
            function showToast(message, type='info') {{
                const container = document.getElementById('toast-container');
                if (!container) return;
                
                const toast = document.createElement('div');
                toast.className = `toast ${{type}}`;
                toast.innerHTML = message;
                container.appendChild(toast);
                
                setTimeout(() => {{
                    toast.style.animation = 'slideInRight 0.3s ease reverse';
                    setTimeout(() => toast.remove(), 300);
                }}, 3000);
            }}
            
            // Cart Management
            function addToCart(productId) {{
                const event = new CustomEvent('snapcon:addToCart', {{ detail: {{ id: productId }} }});
                window.dispatchEvent(event);
                showToast('✓ เพิ่มสินค้าลงตะกร้าแล้ว!', 'success');
            }}
            
            // Language Switcher
            function switchLanguage(lang) {{
                const event = new CustomEvent('snapcon:switchLang', {{ detail: {{ lang: lang }} }});
                window.dispatchEvent(event);
            }}
            
            // Mobile Menu Toggle
            function toggleMobileMenu() {{
                const menu = document.getElementById('mobile-menu');
                menu.classList.toggle('open');
            }}
            
            // Initialize
            document.addEventListener('DOMContentLoaded', () => {{
                console.log('SNAPCON System Initialized');
                
                // Listen for Streamlit events
                window.addEventListener('snapcon:updateCart', (e) => {{
                    const cartCount = e.detail.count;
                    const badge = document.getElementById('cart-badge');
                    if (badge) {{
                        badge.textContent = cartCount;
                        badge.style.display = cartCount > 0 ? 'flex' : 'none';
                    }}
                }});
            }});
            
            // Error Handler
            window.onerror = function(msg, url, line, col, error) {{
                console.error('SNAPCON Error:', {{ msg, url, line, error }});
                showToast('เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง', 'error');
                return true;
            }};
        </script>
        """
    
    @staticmethod
    def get_csrf_token_script():
        """ส่ง CSRF Token"""
        return f"""
        <script>
            window.CSRF_TOKEN = '{StateManager.get('csrf_token')}';
        </script>
        """

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
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h1 style="color: #00B36E; font-size: 28px; font-weight: 900;">SNAPCON</h1>
            <p style="color: #64748b; font-size: 12px;">Automation Solution</p>
        </div>
        """, unsafe_allow_html=True)
        
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
            with st.expander("🔐 เข้าสู่ระบบ", expanded=False):
                user_id = st.text_input("User ID", key="login_id")
                password = st.text_input("Password", type="password", key="login_password")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("เข้าสู่ระบบ", use_container_width=True):
                        if user_id and password:
                            # Hash password (ใน production ควร verify กับ server)
                            hashed, salt = security.hash_password(password)
                            StateManager.set('is_logged_in', True)
                            StateManager.set('user_id', user_id)
                            StateManager.set('session_token', security.generate_session_token(user_id))
                            st.success(f"ยินดีต้อนรับ, {user_id}!")
                            st.rerun()
                        else:
                            st.error("กรุณากรอกข้อมูลให้ครบถ้วน")
                with col2:
                    if st.button("สมัครสมาชิก", use_container_width=True):
                        st.info("กรุณากรอกข้อมูลด้านล่าง")
        else:
            st.success(f"👤 {StateManager.get('user_id')}")
            if st.button("ออกจากระบบ", use_container_width=True):
                StateManager.set('is_logged_in', False)
                StateManager.set('user_id', None)
                StateManager.set('session_token', None)
                st.rerun()
        
        # Language Switcher
        st.divider()
        lang_col1, lang_col2 = st.columns(2)
        with lang_col1:
            if st.button("🇹🇭 TH", use_container_width=True):
                StateManager.set('language', 'th')
        with lang_col2:
            if st.button("🇬🇧 EN", use_container_width=True):
                StateManager.set('language', 'en')
    
    # Main Content Area
    st.markdown(HTMLTemplates.get_css(), unsafe_allow_html=True)
    st.markdown('<div id="toast-container" class="toast-container"></div>', unsafe_allow_html=True)
    st.components.v1.html(JSInjector.get_core_scripts(), height=0)
    
    # Page Router
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
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 80px 0; text-align: center; margin: -4rem -4rem 2rem -4rem;">
        <h1 style="color: white; font-size: 48px; font-weight: 900; margin-bottom: 16px;">
            Snap to Connect.<br><span style="color: #00B36E;">Ready to Control.</span>
        </h1>
        <p style="color: #94a3b8; font-size: 18px; max-width: 600px; margin: 0 auto;">
            ระบบออโตเมชัน Plug & Play ที่พร้อมให้คุณควบคุมสายการผลิตได้ทันที
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured Products
    st.header("🌟 สินค้าแนะนำ")
    products = data.get('products', []) if data else []
    
    if products:
        cols = st.columns(4)
        for idx, product in enumerate(products[:4]):
            with cols[idx % 4]:
                st.markdown(f"""
                <div style="background: white; border-radius: 16px; padding: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
                    <img src="{product.get('image', 'https://via.placeholder.com/400x300')}" 
                         style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 12px;">
                    <h3 style="font-weight: 700; margin-bottom: 8px;">{product.get('name', 'Product')}</h3>
                    <p style="color: #00B36E; font-weight: 700; font-size: 20px; margin-bottom: 12px;">฿{product.get('price', 0):,}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("กำลังโหลดข้อมูลสินค้า...")
    
    # Quick Stats
    st.header("📊 สถิติของเรา")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("โปรเจคที่ทำเสร็จ", "150+")
    with col2:
        st.metric("ลูกค้าที่ไว้วางใจ", "80+")
    with col3:
        st.metric("ปีประสบการณ์", "10+")
    with col4:
        st.metric("การรับประกัน", "2 ปี")

def render_products_page(data):
    """Render Products Page"""
    st.header("📦 ผลิตภัณฑ์ของเรา")
    
    # Search and Filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input("🔍 ค้นหาสินค้า", placeholder="พิมพ์ชื่อสินค้า...")
    with col2:
        sort_by = st.selectbox("เรียงตาม", ["ล่าสุด", "ราคาต่ำ-สูง", "ราคาสูง-ต่ำ"])
    
    # Product Grid
    products = data.get('products', []) if data else []
    
    if search_query:
        products = [p for p in products if search_query.lower() in p.get('name', '').lower()]
    
    if products:
        cols = st.columns(3)
        for idx, product in enumerate(products):
            with cols[idx % 3]:
                with st.container():
                    st.markdown(f"""
                    <div style="background: white; border-radius: 16px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;">
                        <img src="{product.get('image', 'https://via.placeholder.com/400x300')}" 
                             style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
                        <h3 style="font-weight: 700; font-size: 18px; margin-bottom: 8px;">{product.get('name', 'Product')}</h3>
                        <p style="color: #00B36E; font-weight: 700; font-size: 24px; margin-bottom: 16px;">฿{product.get('price', 0):,}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"เพิ่มลงตะกร้า - {product.get('name')}", key=f"add_{product.get('id')}", use_container_width=True):
                        cart = StateManager.get('cart', [])
                        cart.append(product)
                        StateManager.set('cart', cart)
                        st.success(f"เพิ่ม {product.get('name')} ลงตะกร้าแล้ว!")
                        st.rerun()
    else:
        st.warning("ไม่พบสินค้าที่ค้นหา")

def render_spares_page(data):
    """Render Spare Parts Page"""
    st.header("🔧 อะไหล่และอุปกรณ์เสริม")
    
    spares = data.get('spares', []) if data else []
    
    if spares:
        cols = st.columns(4)
        for idx, spare in enumerate(spares):
            with cols[idx % 4]:
                st.markdown(f"""
                <div style="background: white; border-radius: 16px; padding: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <img src="{spare.get('image', 'https://via.placeholder.com/400x300')}" 
                         style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 12px;">
                    <h3 style="font-weight: 700; font-size: 16px; margin-bottom: 8px;">{spare.get('name', 'Spare Part')}</h3>
                    <p style="color: #00B36E; font-weight: 700; font-size: 18px;">฿{spare.get('price', 0):,}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("ไม่มีข้อมูลอะไหล่ในขณะนี้")

def render_dashboard_page():
    """Render Dashboard Page"""
    if not StateManager.get('is_logged_in'):
        st.warning("⚠️ กรุณาเข้าสู่ระบบก่อนเข้าใช้งาน Dashboard")
        return
    
    st.header("📊 Dashboard")
    st.markdown(f"ยินดีต้อนรับ, **{StateManager.get('user_id')}**!")
    
    # Dashboard Controls
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("▶️ START", use_container_width=True, type="primary"):
            st.success("System Started!")
    with col2:
        if st.button("⏹️ STOP", use_container_width=True):
            st.error("System Stopped!")
    with col3:
        if st.button("🔄 REFRESH", use_container_width=True):
            st.info("System Refreshed!")
    with col4:
        if st.button("📥 EXPORT CSV", use_container_width=True):
            st.download_button("Download Report", "data", "report.csv")
    
    # Metrics
    st.subheader("📈 ภาพรวมการผลิต")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Output", "12,450", "+8%")
    with col2:
        st.metric("Carbon Footprint", "245.6 kgCO2e", "-5%")
    with col3:
        st.metric("Energy Used", "1,234 kWh", "+2%")
    
    # Production Progress
    st.subheader("🎯 เป้าหมายการผลิต")
    progress = 65
    st.progress(progress / 100)
    st.caption(f"Progress: {progress}% | Elapsed: 8h 30m | ETA: 4h 15m")
    
    # Machine Status
    st.subheader("🖥️ สถานะเครื่องจักร")
    machine_cols = st.columns(5)
    for i, col in enumerate(machine_cols):
        with col:
            statuses = ['Running', 'Running', 'Warning', 'Running', 'Maintenance']
            colors = ['green', 'green', 'orange', 'green', 'red']
            st.metric(f"Machine {i+1}", statuses[i], delta=None)
            st.markdown(f"<div style='width: 100%; height: 4px; background: {colors[i]}; border-radius: 2px;'></div>", unsafe_allow_html=True)

def render_projects_page(data):
    """Render Projects Page"""
    st.header("📋 ผลงานและโปรเจคของเรา")
    
    projects = data.get('projects', []) if data else []
    
    if projects:
        for project in projects:
            with st.expander(f"📌 {project.get('title', 'Project')}"):
                st.markdown(f"**Category:** {project.get('category', 'N/A')}")
                st.markdown(f"**Description:** {project.get('description', 'No description')}")
    else:
        st.info("ไม่มีข้อมูลโปรเจคในขณะนี้")
    
    # Contact for Custom Project
    st.divider()
    st.subheader("💡 สนใจให้เราออกแบบระบบให้คุณ?")
    with st.form("project_inquiry"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("ชื่อ-นามสกุล")
            email = st.text_input("อีเมล")
        with col2:
            phone = st.text_input("เบอร์โทรศัพท์")
            budget = st.selectbox("งบประมาณ", ["< 100,000", "100,000 - 500,000", "500,000 - 1,000,000", "> 1,000,000"])
        
        details = st.text_area("รายละเอียดโปรเจค")
        
        if st.form_submit_button("ส่งคำขอ", use_container_width=True):
            if name and email and details:
                data_manager.send_to_sheets("project_inquiry", {
                    'name': name, 'email': email, 'phone': phone,
                    'budget': budget, 'details': details
                })
                st.success("✅ ส่งคำขอเรียบร้อย! เราจะติดต่อกลับภายใน 24 ชั่วโมง")
            else:
                st.error("กรุณากรอกข้อมูลให้ครบถ้วน")

def render_about_page():
    """Render About Page"""
    st.header("🏢 เกี่ยวกับเรา")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### วิสัยทัศน์ของเรา
        มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play 
        ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้
        
        ### พันธกิจของเรา
        พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง 
        และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาด
        """)
    
    with col2:
        st.markdown("""
        ### ทำไมต้องเลือก SNAPCON?
        - ✅ **10+ ปี** ประสบการณ์ในอุตสาหกรรม
        - ✅ **150+ โปรเจค** ที่ประสบความสำเร็จ
        - ✅ **80+ ลูกค้า** ที่ไว้วางใจ
        - ✅ **รับประกัน 2 ปี** ทุกผลิตภัณฑ์
        - ✅ **บริการหลังการขาย** ตลอด 24 ชม.
        """)
    
    # Team Section
    st.subheader("👥 ทีมงานของเรา")
    team_cols = st.columns(4)
    for i, col in enumerate(team_cols):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <div style="width: 100px; height: 100px; background: #e2e8f0; border-radius: 50%; margin: 0 auto 12px;"></div>
                <h4 style="font-weight: 700;">Team Member {i+1}</h4>
                <p style="color: #64748b; font-size: 14px;">Position</p>
            </div>
            """, unsafe_allow_html=True)

def render_contact_page():
    """Render Contact Page"""
    st.header("📞 ติดต่อเรา")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ข้อมูลติดต่อ
        - 📧 **Email:** snapcon1992@gmail.com
        - 📱 **Line:** @SnapconAuto
        - 📞 **Tel:** 081-XXX-XXXX
        - 📍 **ที่อยู่:** กรุงเทพมหานคร, ประเทศไทย
        
        ### เวลาทำการ
        - จันทร์ - ศุกร์: 8:00 - 17:30
        - เสาร์: 8:00 - 12:00
        - อาทิตย์: หยุด
        """)
    
    with col2:
        st.subheader("📝 ส่งข้อความถึงเรา")
        with st.form("contact_form"):
            name = st.text_input("ชื่อ-นามสกุล / บริษัท")
            email = st.text_input("อีเมล")
            phone = st.text_input("เบอร์โทรศัพท์")
            subject = st.selectbox("หัวข้อ", ["สอบถามข้อมูลสินค้า", "ขอใบเสนอราคา", "ปัญหาทางเทคนิค", "อื่นๆ"])
            message = st.text_area("ข้อความ", height=150)
            
            if st.form_submit_button("ส่งข้อความ", use_container_width=True):
                if name and email and message:
                    data_manager.send_to_sheets("contact", {
                        'name': name, 'email': email, 'phone': phone,
                        'subject': subject, 'message': message
                    })
                    st.success("✅ ส่งข้อความเรียบร้อย! เราจะติดต่อกลับภายใน 24 ชั่วโมง")
                else:
                    st.error("กรุณากรอกข้อมูลให้ครบถ้วน")

def render_cart_page():
    """Render Cart Page"""
    st.header("🛒 ตะกร้าสินค้า")
    
    cart = StateManager.get('cart', [])
    
    if not cart:
        st.warning("🛒 ตะกร้าสินค้าว่างเปล่า")
        if st.button("เลือกดูสินค้า"):
            st.rerun()
        return
    
    # Display Cart Items
