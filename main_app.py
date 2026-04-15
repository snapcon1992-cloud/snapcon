import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS สำหรับ UI ที่ตรงตามภาพ ฟังก์ชัน 11 ข้อ และระบบ 2 ภาษา (พร้อมสเปคแยกรายรุ่น)
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Automation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=Prompt:wght@400;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'nav-bg': '#2b3035',
                        'snap-green': '#00B36E',
                        'btn-bg': '#e2e2e2',
                        'card-gray': '#a8a8a8',
                    },
                    fontFamily: {
                        sans: ['Inter', 'Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { margin: 0; padding: 0; background-color: #F8F9FA; overflow-x: hidden; }
        .hero-bg {
            background: linear-gradient(to right, #ffffff 35%, rgba(124, 224, 184, 0.9) 65%, rgba(124, 224, 184, 0.6) 100%), 
                        url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center right;
        }
        .page-section { display: none; }
        .page-active { display: block; }
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar -->
    <nav class="bg-nav-bg h-[60px] w-full fixed top-0 z-50 flex items-center justify-between px-6 border-b-4 border-snap-green shadow-sm">
        
        <!-- Left: Logo -->
        <div class="flex flex-col cursor-pointer justify-center h-full" onclick="navigate('home')">
            <span class="font-black text-2xl text-snap-green tracking-tight leading-none mt-1">SNAPCON</span>
            <span class="font-bold text-[10px] text-snap-green leading-none">Automation</span>
        </div>
        
        <!-- Center: Nav Buttons -->
        <div class="hidden lg:flex items-center gap-2">
            <button onclick="navigate('product')" data-i18n="navProduct" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300">Product</button>
            <button onclick="checkDashboardAuth()" data-i18n="navDashboard" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300">Dashboard</button>
            <button onclick="navigate('contact')" data-i18n="navContact" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300">Contact</button>
            <button onclick="navigate('about')" data-i18n="navAbout" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300">About</button>
        </div>

        <!-- Right: Login, Icons, Language Switch -->
        <div class="flex items-center gap-3">
            <div id="login-section" class="flex items-center gap-2">
                <span class="text-[#8e9caf] text-xs font-bold px-1">ID :</span>
                <input type="text" id="userId" class="h-[22px] w-16 px-2 text-xs outline-none text-black">
                <span class="text-[#8e9caf] text-xs font-bold px-1">Pass</span>
                <input type="password" id="userPass" class="h-[22px] w-16 px-2 text-xs outline-none text-black">
                <div class="flex flex-col gap-0.5 ml-1">
                    <button onclick="handleLogin()" data-i18n="navLogin" class="bg-btn-bg text-black font-bold text-[9px] px-3 py-0.5 hover:bg-gray-300">Login</button>
                    <button onclick="handleRegister()" data-i18n="navRegister" class="bg-btn-bg text-black font-bold text-[9px] px-3 py-0.5 hover:bg-gray-300">Register</button>
                </div>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3 mr-4">
                <span class="text-snap-green font-bold text-sm">Hi, <span id="displayUser" class="text-white">User</span></span>
                <button onclick="handleLogout()" data-i18n="navLogout" class="text-gray-400 text-xs underline hover:text-white">Logout</button>
            </div>

            <!-- Language Switch -->
            <div class="flex items-center bg-[#1c2126] rounded-full p-0.5 ml-1 border border-gray-600">
                <button id="btn-lang-th" onclick="setLanguage('th')" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-snap-green text-white transition-colors">TH</button>
                <button id="btn-lang-en" onclick="setLanguage('en')" class="text-[9px] font-bold px-2 py-0.5 rounded-full text-gray-400 hover:text-white transition-colors">EN</button>
            </div>

            <!-- Icons -->
            <div class="flex items-center gap-4 ml-2 text-white text-lg">
                <div class="relative cursor-pointer hover:text-snap-green" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 bg-red-500 text-white text-[9px] font-bold px-1.5 rounded-full hidden">0</span>
                </div>
                <i class="fas fa-search cursor-pointer hover:text-snap-green"></i>
            </div>
        </div>
    </nav>

    <!-- SPACER สำหรับ Navbar -->
    <div class="h-[60px]"></div>

    <!-- ==================== PAGE: HOME ==================== -->
    <div id="page-home" class="page-section page-active">
        <!-- Hero Section -->
        <section class="w-full h-[400px] hero-bg relative flex items-center border-b border-gray-100">
            <div class="bg-white pl-8 pr-16 py-12 ml-0 shadow-[10px_0_15px_-3px_rgba(0,0,0,0.05)] absolute left-0 z-10 h-full flex flex-col justify-center">
                <p data-i18n="heroText1" class="text-[26px] text-black mb-1 font-normal tracking-wide">Snap to Connect.</p>
                <p data-i18n="heroText2" class="text-[26px] text-black mb-4 pl-8 font-normal tracking-wide">Ready to Control.</p>
                <h1 data-i18n="heroText3" class="text-6xl font-black text-black tracking-tighter pl-12">Plug & Play</h1>
                <div class="h-1 w-16 bg-red-600 mt-4 ml-12"></div>
                
                <!-- Social Media & Contact Links -->
                <div class="flex flex-wrap items-center gap-6 mt-8 ml-12">
                    <a href="tel:0812345678" target="_blank" class="flex items-center gap-2 text-sm font-bold text-gray-500 hover:text-snap-green transition-colors group">
                        <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center group-hover:bg-snap-green group-hover:text-white transition-colors">
                            <i class="fas fa-phone-alt"></i>
                        </div>
                        <span class="hidden sm:block">081-XXX-XXXX</span>
                    </a>
                    <a href="https://facebook.com" target="_blank" class="flex items-center gap-2 text-sm font-bold text-gray-500 hover:text-[#1877F2] transition-colors group">
                        <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center group-hover:bg-[#1877F2] group-hover:text-white transition-colors">
                            <i class="fab fa-facebook-f"></i>
                        </div>
                        <span class="hidden sm:block">Snapcon Automation</span>
                    </a>
                    <a href="https://line.me" target="_blank" class="flex items-center gap-2 text-sm font-bold text-gray-500 hover:text-[#00B900] transition-colors group">
                        <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center group-hover:bg-[#00B900] group-hover:text-white transition-colors">
                            <i class="fab fa-line text-lg"></i>
                        </div>
                        <span class="hidden sm:block">@SnapconAuto</span>
                    </a>
                    <a href="https://youtube.com" target="_blank" class="flex items-center gap-2 text-sm font-bold text-gray-500 hover:text-[#FF0000] transition-colors group">
                        <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center group-hover:bg-[#FF0000] group-hover:text-white transition-colors">
                            <i class="fab fa-youtube"></i>
                        </div>
                        <span class="hidden sm:block">Snapcon Channel</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- Bottom Cards Section -->
        <section class="w-full max-w-5xl mx-auto px-6 py-16">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                
                <!-- Card 1: Data sheet -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition-colors shadow-sm">
                        <h3 data-i18n="cardDataSheet" class="text-xl font-bold text-black text-center tracking-wide">Download data sheet</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-xl mt-3"></i>
                    <div class="dropdown-menu top-[120px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1HY0dUjYJZgxRVYYgN5DOV6Ymm9ARCGUW/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                        <a href="https://drive.google.com/file/d/1TC_cXAy7gbgBx0QI0TiL7Kdt1ICljnHj/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 02</a>
                        <a href="https://drive.google.com/file/d/1Yv_gJWWxTL4H_5YmCDAOCnI33gdfcj4j/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 03</a>
                        <a href="https://drive.google.com/file/d/1KtCARlKphuuIqUOU6xg5mnPf99sjCjHD/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 04</a>
                        <a href="https://drive.google.com/file/d/1dlOS1HSYy1qjWASPGQiKRvQsSyZ-lFs4/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Model 05</a>
                    </div>
                </div>

                <!-- Card 2: Drawing -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition-colors shadow-sm">
                        <h3 data-i18n="cardDrawing" class="text-xl font-bold text-black text-center tracking-wide">Download drawing</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-xl mt-3"></i>
                    <div class="dropdown-menu top-[120px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1CisPrHXeoJgspikAzAOwH0rdhNtQiviy/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                        <a href="https://drive.google.com/file/d/1Gt8onVT7dsyJQkmxdY6s1GZTX4_oUNuB/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 02</a>
                        <a href="https://drive.google.com/file/d/1zesePgsPwZDTUpKzLrmesdnuY6usfe2P/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 03</a>
                        <a href="https://drive.google.com/file/d/1I-63QRJrJksO6xQb1cCWaq9HoDZJ6qBl/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 04</a>
                        <a href="https://drive.google.com/file/d/16z8m9S06kGhyO0C6Tb0mMQ0L4bk5wTDz/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Model 05</a>
                    </div>
                </div>

                <!-- Card 3: Catalog -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition-colors shadow-sm">
                        <h3 data-i18n="cardCatalog" class="text-xl font-bold text-black text-center tracking-wide">Product Catalog</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-xl mt-3"></i>
                    <div class="dropdown-menu top-[120px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1_-OdU-N7CnKfG6qY6WV7hW59vL1LX7KD/view?usp=drive_link" target="_blank" data-i18n="cardCatalogFull" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Download Full Catalog</a>
                    </div>
                </div>

            </div>
        </section>
    </div>

    <!-- ==================== PAGE: PRODUCT ==================== -->
    <div id="page-product" class="page-section max-w-7xl mx-auto px-6 py-12">
        <h2 data-i18n="pageProductTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">SNAPCON Products</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6" id="product-grid">
            <!-- จะถูกสร้างโดย JavaScript -->
        </div>
    </div>

    <!-- ==================== PAGE: CART ==================== -->
    <div id="page-cart" class="page-section max-w-5xl mx-auto px-6 py-12">
        <h2 data-i18n="pageCartTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">รถเข็นขอใบเสนอราคา</h2>
        <div class="bg-white p-6 shadow-md rounded-lg">
            <div id="cart-items" class="space-y-4">
                <p data-i18n="cartEmpty" class="text-gray-500 py-8 text-center text-lg">ยังไม่มีสินค้าในรถเข็น</p>
            </div>
            <div class="border-t mt-6 pt-6 flex justify-between items-center">
                <span data-i18n="cartTotalLabel" class="text-xl font-bold">ราคากลางประเมินรวม:</span>
                <span id="cart-total" class="text-2xl font-black text-snap-green">฿0</span>
            </div>
            <button onclick="requestQuote()" data-i18n="btnRequestQuote" class="mt-8 w-full bg-nav-bg text-white font-bold py-4 rounded hover:bg-snap-green transition-colors">
                ยื่นขอใบเสนอราคาอย่างเป็นทางการ
            </button>
        </div>
    </div>

    <!-- ==================== PAGE: DASHBOARD ==================== -->
    <div id="page-dashboard" class="page-section max-w-7xl mx-auto px-6 py-12">
        <h2 data-i18n="pageDashTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">Dashboard หลักของ Snapcon</h2>
        <div class="grid grid-cols-3 gap-6 mb-8">
            <div class="bg-white p-6 shadow rounded border-t-4 border-snap-green"><p class="text-gray-500">Total Output</p><h3 class="text-4xl font-black">4,520</h3></div>
            <div class="bg-white p-6 shadow rounded border-t-4 border-blue-500"><p class="text-gray-500">Active Nodes</p><h3 class="text-4xl font-black">10/10</h3></div>
            <div class="bg-white p-6 shadow rounded border-t-4 border-orange-500"><p class="text-gray-500">System Health</p><h3 class="text-4xl font-black">98.5%</h3></div>
        </div>
        <div class="bg-white p-12 shadow rounded text-center">
            <i class="fas fa-chart-line text-6xl text-gray-300 mb-4"></i>
            <p data-i18n="dashDesc" class="text-gray-500 text-lg">ระบบ Dashboard เต็มรูปแบบกำลังแสดงผลข้อมูล Real-time...</p>
        </div>
    </div>

    <!-- ==================== PAGE: CONTACT ==================== -->
    <div id="page-contact" class="page-section max-w-4xl mx-auto px-6 py-12">
        <h2 data-i18n="pageContactTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">ติดต่อเรา (Contact Us)</h2>
        <div class="bg-white p-8 shadow-md rounded-lg">
            <input type="text" data-i18n-placeholder="phName" placeholder="ชื่อ-นามสกุล" class="w-full mb-4 px-4 py-3 border rounded">
            <input type="email" data-i18n-placeholder="phEmail" placeholder="อีเมล" class="w-full mb-4 px-4 py-3 border rounded">
            <textarea data-i18n-placeholder="phMessage" placeholder="คำถามหรือข้อสงสัย..." class="w-full mb-4 px-4 py-3 border rounded h-32"></textarea>
            <button onclick="sendContact()" data-i18n="btnSendMsg" class="bg-snap-green text-white font-bold px-8 py-3 rounded">ส่งข้อความ</button>
        </div>
    </div>

    <!-- ==================== PAGE: ABOUT ==================== -->
    <div id="page-about" class="page-section max-w-4xl mx-auto px-6 py-12">
        <h2 data-i18n="pageAboutTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">เกี่ยวกับ Snapcon (About Us)</h2>
        <div class="bg-white p-8 shadow-md rounded-lg">
            <p class="text-gray-600 leading-relaxed text-lg">
                <span data-i18n="aboutDesc1">Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรม 4.0 ที่มุ่งเน้นการพัฒนาระบบ</span> <b>Plug & Play</b> 
                <span data-i18n="aboutDesc2">เพื่อลดความซับซ้อนในการติดตั้งและควบคุมเครื่องจักร</span> 
                <br><br>
                <i data-i18n="aboutDesc3">(ข้อมูลประวัติบริษัทเพิ่มเติมจะถูกเพิ่มเข้ามาในส่วนนี้ภายหลัง)</i>
            </p>
        </div>
    </div>

    <!-- ==================== JAVASCRIPT ==================== -->
    <script>
        // --- 0. ระบบแปลภาษา (Translations) ---
        let currentLang = 'th';
        
        const dict = {
            th: {
                navProduct: "Product", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroText3: "Plug & Play",
                cardDataSheet: "Download data sheet", cardDrawing: "Download drawing", cardCatalog: "Product Catalog", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "หยิบใส่รถเข็น",
                pageCartTitle: "รถเข็นขอใบเสนอราคา", cartEmpty: "ยังไม่มีสินค้าในรถเข็น", cartTotalLabel: "ราคากลางประเมินรวม:",
                btnRequestQuote: "ยื่นขอใบเสนอราคาอย่างเป็นทางการ", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก",
                pageDashTitle: "Dashboard หลักของ Snapcon", dashDesc: "ระบบ Dashboard เต็มรูปแบบกำลังแสดงผลข้อมูล Real-time...",
                pageContactTitle: "ติดต่อเรา (Contact Us)", phName: "ชื่อ-นามสกุล", phEmail: "อีเมล", phMessage: "คำถามหรือข้อสงสัย...", btnSendMsg: "ส่งข้อความ",
                pageAboutTitle: "เกี่ยวกับ Snapcon (About Us)",
                aboutDesc1: "Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรม 4.0 ที่มุ่งเน้นการพัฒนาระบบ",
                aboutDesc2: "เพื่อลดความซับซ้อนในการติดตั้งและควบคุมเครื่องจักร",
                aboutDesc3: "(ข้อมูลประวัติบริษัทเพิ่มเติมจะถูกเพิ่มเข้ามาในส่วนนี้ภายหลัง)",
                alertLoginFail: "⚠️ ID หรือ Password ไม่ถูกต้อง\\n(ใช้ ID: 001 และ Pass: 123)",
                alertLoginReq: "⚠️ กรุณา Login หรือ Register ก่อนเข้าสู่หน้า Dashboard",
                alertLoginSuccess: "Login สำเร็จ! บันทึกข้อมูล Session (Simulation)",
                alertRegister: "พาไปหน้า Register และบันทึกข้อมูลเก็บไว้ใน Google Drive / Database",
                alertAddCart: "เพิ่มสินค้าลงในรถเข็นแล้ว!",
                alertQuoteReq: "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้นเพื่อยื่นขอใบเสนอราคา",
                alertQuoteSuccess: "ส่งคำขอใบเสนอราคาสำหรับสินค้า {n} รายการ สำเร็จ! เจ้าหน้าที่จะติดต่อกลับพร้อมใบเสนอราคาอย่างเป็นทางการครับ",
                alertContact: "ส่งข้อความสำเร็จ ทีมงานจะติดต่อกลับครับ",
                
                specTitle: "รายละเอียดสำหรับสั่งทำ (Customizable):"
            },
            en: {
                navProduct: "Products", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroText3: "Plug & Play",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "Add to Cart",
                pageCartTitle: "Quotation Cart", cartEmpty: "Your cart is currently empty", cartTotalLabel: "Total Estimated Price:",
                btnRequestQuote: "Submit Official Quotation Request", selectAll: "Select All", deleteSelected: "Delete Selected",
                pageDashTitle: "Snapcon Main Dashboard", dashDesc: "Full Dashboard system is displaying real-time data...",
                pageContactTitle: "Contact Us", phName: "Full Name", phEmail: "Email Address", phMessage: "Questions or Inquiries...", btnSendMsg: "Send Message",
                pageAboutTitle: "About Snapcon",
                aboutDesc1: "Snapcon Automation is a leader in Industry 4.0 technology, focusing on",
                aboutDesc2: "systems to simplify the installation and control of machinery.",
                aboutDesc3: "(Additional company history will be added here later)",
                alertLoginFail: "⚠️ Invalid ID or Password\\n(Use ID: 001 and Pass: 123)",
                alertLoginReq: "⚠️ Please Login or Register to access the Dashboard",
                alertLoginSuccess: "Login Successful! Session data saved (Simulation)",
                alertRegister: "Redirecting to Register page and saving data to Google Drive / Database",
                alertAddCart: "Item added to your cart!",
                alertQuoteReq: "Please select at least 1 item to request a quotation.",
                alertQuoteSuccess: "Quotation request for {n} items submitted successfully! Our team will contact you shortly.",
                alertContact: "Message sent successfully! Our team will get back to you.",
                
                specTitle: "Customizable Specifications:"
            }
        };

        function setLanguage(lang) {
            currentLang = lang;
            
            // สลับสีปุ่ม TH/EN
            const btnTh = document.getElementById('btn-lang-th');
            const btnEn = document.getElementById('btn-lang-en');
            
            if(lang === 'th') {
                btnTh.className = "text-[9px] font-bold px-2 py-0.5 rounded-full bg-snap-green text-white transition-colors";
                btnEn.className = "text-[9px] font-bold px-2 py-0.5 rounded-full text-gray-400 hover:text-white transition-colors";
            } else {
                btnEn.className = "text-[9px] font-bold px-2 py-0.5 rounded-full bg-snap-green text-white transition-colors";
                btnTh.className = "text-[9px] font-bold px-2 py-0.5 rounded-full text-gray-400 hover:text-white transition-colors";
            }

            // อัปเดตข้อความคงที่
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[lang][key]) el.innerHTML = dict[lang][key];
            });

            // อัปเดต Placeholder
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (dict[lang][key]) el.placeholder = dict[lang][key];
            });

            // เรนเดอร์ส่วนไดนามิกใหม่เพื่อให้เปลี่ยนภาษา
            renderProducts();
            renderCart();
        }

        // --- 1. ตัวแปรสถานะทั่วไปและข้อมูลสินค้า (แยกสเปคแต่ละรุ่น) ---
        let isLoggedIn = false;
        let cart = [];
        
        const products = [
            { 
                id: 'M01', name: 'Snapcon Model 01 (Mini)', price: 15000, img: '<img src="<a href="https://ibb.co/vGDpjVx"><img src="https://i.ibb.co/bZ7TKQg/01.png" alt="01" border="0"></a>',
                specs: {
                    th: { s1: "1. ความยาว (L): 0.5 - 5 m", s2: "2. ความสูง (H): 0.3 - 1 m", s3: "3. ความกว้าง (W): 200 - 400 mm", s4: "4. น้ำหนักลำเลียง: 0 - 50 kg", s5: "5. ความเร็ว: 5 - 20 m/min", s6: "6. วัสดุ: เหล็กพ่นสี / อลูมิเนียม" },
                    en: { s1: "1. Length (L): 0.5 - 5 m", s2: "2. Height (H): 0.3 - 1 m", s3: "3. Width (W): 200 - 400 mm", s4: "4. Payload: 0 - 50 kg", s5: "5. Speed: 5 - 20 m/min", s6: "6. Material: Painted Steel / AL" }
                }
            },
            { 
                id: 'M02', name: 'Snapcon Model 02 (Std)', price: 22000, img: '<a href="https://ibb.co/v6zJdyNB"><img src="https://i.ibb.co/tTCb2j0h/02.png" alt="02" border="0"></a>',
                specs: {
                    th: { s1: "1. ความยาว (L): 1 - 15 m", s2: "2. ความสูง (H): 0.5 - 1.2 m", s3: "3. ความกว้าง (W): 300 - 600 mm", s4: "4. น้ำหนักลำเลียง: 0 - 100 kg", s5: "5. ความเร็ว: 10 - 30 m/min", s6: "6. วัสดุ: เหล็ก / สแตนเลส (เพิ่มล้อได้)" },
                    en: { s1: "1. Length (L): 1 - 15 m", s2: "2. Height (H): 0.5 - 1.2 m", s3: "3. Width (W): 300 - 600 mm", s4: "4. Payload: 0 - 100 kg", s5: "5. Speed: 10 - 30 m/min", s6: "6. Material: Steel / SUS (Wheeled opt.)" }
                }
            },
            { 
                id: 'M03', name: 'Snapcon Model 03 (Heavy)', price: 28500, img: '<a href="https://ibb.co/4R7JxH5t"><img src="https://i.ibb.co/PGNt8dfj/03.png" alt="03" border="0"></a>',
                specs: {
                    th: { s1: "1. ความยาว (L): 2 - 30 m", s2: "2. ความสูง (H): 0.5 - 1.5 m", s3: "3. ความกว้าง (W): 500 - 1000 mm", s4: "4. น้ำหนักลำเลียง: 0 - 300 kg", s5: "5. ความเร็ว: 5 - 25 m/min", s6: "6. วัสดุ: เหล็กหนาพิเศษเสริมคาน" },
                    en: { s1: "1. Length (L): 2 - 30 m", s2: "2. Height (H): 0.5 - 1.5 m", s3: "3. Width (W): 500 - 1000 mm", s4: "4. Payload: 0 - 300 kg", s5: "5. Speed: 5 - 25 m/min", s6: "6. Material: Reinforced Heavy Steel" }
                }
            },
            { 
                id: 'M04', name: 'Snapcon Model 04 (Speed)', price: 35000, img: '<a href="https://ibb.co/67jnH48Z"><img src="https://i.ibb.co/mVfD9H0B/04.png" alt="04" border="0"></a>',
                specs: {
                    th: { s1: "1. ความยาว (L): 1 - 20 m", s2: "2. ความสูง (H): 0.8 - 1.5 m", s3: "3. ความกว้าง (W): 400 - 800 mm", s4: "4. น้ำหนักลำเลียง: 0 - 80 kg", s5: "5. ความเร็ว: 20 - 60 m/min", s6: "6. วัสดุ: สแตนเลส 304 ฟู้ดเกรด" },
                    en: { s1: "1. Length (L): 1 - 20 m", s2: "2. Height (H): 0.8 - 1.5 m", s3: "3. Width (W): 400 - 800 mm", s4: "4. Payload: 0 - 80 kg", s5: "5. Speed: 20 - 60 m/min", s6: "6. Material: SUS 304 Food Grade" }
                }
            },
            { 
                id: 'M05', name: 'Snapcon Pro 05 (Custom)', price: 45000, img: '<a href="https://ibb.co/Q5Fn73V"><img src="https://i.ibb.co/x4SGKtb/05.png" alt="05" border="0"></a>',
                specs: {
                    th: { s1: "1. ความยาว (L): 5 - 100 m", s2: "2. ความสูง (H): 0.1 - 2 m", s3: "3. ความกว้าง (W): 500 - 1500 mm", s4: "4. น้ำหนักลำเลียง: 0 - 400 kg", s5: "5. ความเร็ว: 1 - 50 m/min", s6: "6. วัสดุ: ปรับแต่งได้ตามต้องการ (Full Custom)" },
                    en: { s1: "1. Length (L): 5 - 100 m", s2: "2. Height (H): 0.1 - 2 m", s3: "3. Width (W): 500 - 1500 mm", s4: "4. Payload: 0 - 400 kg", s5: "5. Speed: 1 - 50 m/min", s6: "6. Material: Fully Customizable Options" }
                }
            }
        ];

        // --- 2. ฟังก์ชัน Navigation ---
        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            document.getElementById('page-' + pageId).classList.add('page-active');
            window.scrollTo(0,0);
        }

        function checkDashboardAuth() {
            if (isLoggedIn) {
                navigate('dashboard');
            } else {
                alert(dict[currentLang].alertLoginReq);
                document.getElementById('userId').focus();
            }
        }

        // --- 3. ระบบ Login & Register ---
        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            if ((id === '001' && pass === '123') || (id === '' && pass === '')) {
                isLoggedIn = true;
                document.getElementById('displayUser').innerText = id || 'Admin';
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                alert(dict[currentLang].alertLoginSuccess);
            } else {
                alert(dict[currentLang].alertLoginFail);
            }
        }
        function handleRegister() {
            alert(dict[currentLang].alertRegister);
            handleLogin(); 
        }
        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden');
            document.getElementById('user-section').classList.add('hidden');
            document.getElementById('user-section').classList.remove('flex');
            navigate('home');
        }

        // --- 4. ระบบ Product & Cart ---
        function renderProducts() {
            const grid = document.getElementById('product-grid');
            grid.innerHTML = products.map(p => {
                const sp = p.specs[currentLang]; // ดึงสเปคตามภาษาที่เลือก
                return `
                <div class="bg-white border p-5 shadow-sm hover:shadow-md transition flex flex-col h-full rounded-xl">
                    <img src="${p.img}" class="w-full h-40 object-cover mb-4 rounded-lg border border-gray-100">
                    <h4 class="font-bold text-lg text-nav-bg">${p.name}</h4>
                    
                    <!-- ส่วนข้อมูลรายละเอียดเครื่องจักรที่แตกต่างกันในแต่ละ Model -->
                    <div class="my-3 flex-grow bg-gray-50 p-3 rounded-lg border border-gray-100">
                        <p class="text-[11px] font-bold text-snap-green mb-1.5">${dict[currentLang].specTitle}</p>
                        <ul class="text-[10px] text-gray-600 list-none space-y-1">
                            <li>${sp.s1}</li>
                            <li>${sp.s2}</li>
                            <li>${sp.s3}</li>
                            <li>${sp.s4}</li>
                            <li>${sp.s5}</li>
                            <li>${sp.s6}</li>
                        </ul>
                    </div>
                    
                    <p class="text-snap-green font-black text-2xl my-3">฿${p.price.toLocaleString()}</p>
                    <button onclick="addToCart('${p.id}')" class="w-full bg-nav-bg text-white py-2.5 rounded font-bold hover:bg-snap-green transition mt-auto">
                        ${dict[currentLang].btnAddToCart}
                    </button>
                </div>
                `;
            }).join('');
        }

        function addToCart(id) {
            const product = products.find(p => p.id === id);
            cart.push({ ...product, cartId: Date.now() + Math.random(), selected: true });
            
            const badge = document.getElementById('cart-badge');
            badge.innerText = cart.length;
            badge.classList.remove('hidden');
            
            alert(dict[currentLang].alertAddCart);
            renderCart();
        }

        function toggleSelect(cartId) {
            const item = cart.find(i => i.cartId === cartId);
            if(item) item.selected = !item.selected;
            renderCart();
        }

        function toggleSelectAll(checked) {
            cart.forEach(item => item.selected = checked);
            renderCart();
        }

        function deleteSelected() {
            cart = cart.filter(item => !item.selected);
            const badge = document.getElementById('cart-badge');
            badge.innerText = cart.length;
            if (cart.length === 0) badge.classList.add('hidden');
            renderCart();
        }

        function renderCart() {
            const container = document.getElementById('cart-items');
            if(cart.length === 0) {
                container.innerHTML = `<p class="text-gray-500 py-8 text-center text-lg">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }

            const allSelected = cart.length > 0 && cart.every(i => i.selected);

            let html = `
                <div class="flex justify-between items-center border-b pb-4 mb-4 bg-gray-50 p-4 rounded">
                    <div class="flex items-center gap-3">
                        <input type="checkbox" id="selectAll" ${allSelected ? 'checked' : ''} onclick="toggleSelectAll(this.checked)" class="w-5 h-5 accent-snap-green cursor-pointer">
                        <label for="selectAll" class="font-bold cursor-pointer">${dict[currentLang].selectAll} (${cart.length})</label>
                    </div>
                    <button onclick="deleteSelected()" class="text-red-500 hover:text-red-700 font-bold text-sm"><i class="fas fa-trash-alt mr-1"></i> ${dict[currentLang].deleteSelected}</button>
                </div>
            `;

            html += cart.map((item, index) => `
                <div class="flex justify-between items-center border-b pb-4 mb-4 hover:bg-gray-50 p-2 rounded transition-colors">
                    <div class="flex items-center gap-4">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleSelect(${item.cartId})" class="w-5 h-5 accent-snap-green cursor-pointer">
                        <img src="${item.img}" class="w-16 h-16 object-cover rounded border">
                        <div>
                            <span class="font-bold block">${item.name}</span>
                            <span class="text-xs text-gray-500">Model: ${item.id}</span>
                        </div>
                    </div>
                    <span class="font-bold text-gray-700 text-lg">฿${item.price.toLocaleString()}</span>
                </div>
            `).join('');

            container.innerHTML = html;

            const total = cart.filter(i => i.selected).reduce((sum, item) => sum + item.price, 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
        }

        function requestQuote() {
            const selectedItems = cart.filter(i => i.selected);
            if(selectedItems.length === 0) {
                alert(dict[currentLang].alertQuoteReq);
                return;
            }
            alert(dict[currentLang].alertQuoteSuccess.replace('{n}', selectedItems.length));
            
            cart = cart.filter(i => !i.selected);
            const badge = document.getElementById('cart-badge');
            badge.innerText = cart.length;
            if (cart.length === 0) badge.classList.add('hidden');
            
            renderCart();
            navigate('home');
        }

        function sendContact() {
            alert(dict[currentLang].alertContact);
        }

        // โหลดข้อมูลเริ่มต้นและแปลภาษาครั้งแรก (ค่าเริ่มต้นภาษาไทย)
        setLanguage('th');

    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=1400, scrolling=True)
