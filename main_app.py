import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS ฉบับสมบูรณ์ที่สุด (The Ultimate Version)
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
                        'nav-bg': '#1e2329',
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
        .page-section { display: none !important; }
        .page-active { display: block !important; animation: fadeIn 0.4s ease-out forwards; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
        
        /* ซ่อน Scrollbar แต่ยัง Scroll ได้ */
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar -->
    <nav class="bg-nav-bg h-[65px] w-full fixed top-0 z-50 flex items-center justify-between px-4 md:px-6 border-b-4 border-snap-green shadow-lg">
        <!-- Logo -->
        <div class="flex flex-col cursor-pointer justify-center h-full shrink-0" onclick="navigate('home')">
            <span class="font-black text-xl md:text-2xl text-snap-green tracking-tight leading-none mt-1">SNAPCON</span>
            <span class="font-bold text-[9px] md:text-[10px] text-snap-green leading-none">Automation</span>
        </div>
        
        <!-- Center Menus (Responsive Scroll) -->
        <div class="flex items-center gap-1 md:gap-2 overflow-x-auto no-scrollbar px-2 mx-2">
            <button type="button" onclick="navigate('product')" data-i18n="navProduct" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 md:px-6 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Product</button>
            <button type="button" onclick="checkDashboardAuth()" data-i18n="navDashboard" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 md:px-6 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Dashboard</button>
            <button type="button" onclick="navigate('contact')" data-i18n="navContact" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 md:px-6 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Contact</button>
            <button type="button" onclick="navigate('about')" data-i18n="navAbout" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 md:px-6 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">About</button>
        </div>

        <!-- Right Side: Login, Lang, Cart -->
        <div class="flex items-center gap-3 shrink-0">
            <div id="login-section" class="hidden md:flex items-center gap-2">
                <span class="text-slate-400 text-xs font-bold px-1">ID:</span>
                <input type="text" id="userId" class="h-[26px] w-16 px-2 text-xs outline-none text-black rounded border-none focus:ring-2 ring-snap-green">
                <span class="text-slate-400 text-xs font-bold px-1">PW:</span>
                <input type="password" id="userPass" class="h-[26px] w-16 px-2 text-xs outline-none text-black rounded border-none focus:ring-2 ring-snap-green">
                <div class="flex flex-col gap-0.5 ml-1">
                    <button type="button" onclick="handleLogin()" data-i18n="navLogin" class="bg-snap-green text-white font-bold text-[9px] px-3 py-0.5 hover:bg-green-600 rounded transition-colors">Login</button>
                    <button type="button" onclick="handleRegister()" data-i18n="navRegister" class="bg-slate-600 text-white font-bold text-[9px] px-3 py-0.5 hover:bg-slate-500 rounded transition-colors">Register</button>
                </div>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3 mr-2 bg-white/5 px-3 py-1 rounded-full border border-white/10">
                <span class="text-snap-green font-bold text-xs">Hi, <span id="displayUser" class="text-white">User</span></span>
                <button type="button" onclick="handleLogout()" data-i18n="navLogout" class="text-slate-400 text-[10px] font-bold uppercase hover:text-white transition-colors">Logout</button>
            </div>

            <!-- Lang Switch -->
            <div class="flex items-center bg-black/30 rounded-full p-0.5 border border-white/10">
                <button type="button" id="btn-lang-th" onclick="setLanguage('th')" class="text-[9px] font-bold px-2.5 py-1 rounded-full bg-snap-green text-white transition-colors">TH</button>
                <button type="button" id="btn-lang-en" onclick="setLanguage('en')" class="text-[9px] font-bold px-2.5 py-1 rounded-full text-slate-400 hover:text-white transition-colors">EN</button>
            </div>

            <!-- Cart Icon -->
            <div class="flex items-center gap-4 ml-1 text-white text-lg">
                <div class="relative cursor-pointer hover:text-snap-green transition-transform hover:scale-110" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2.5 -right-2.5 w-4 h-4 bg-red-500 text-white text-[9px] font-black flex items-center justify-center rounded-full border-2 border-nav-bg hidden shadow-lg">0</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="h-[65px]"></div>

    <!-- ==================== PAGE: HOME ==================== -->
    <div id="page-home" class="page-section page-active">
        <section class="w-full h-[350px] md:h-[450px] hero-bg relative flex items-center border-b border-gray-200">
            <div class="bg-white/95 backdrop-blur-sm pl-6 md:pl-12 pr-12 md:pr-20 py-10 md:py-16 ml-0 shadow-[15px_0_30px_-5px_rgba(0,0,0,0.1)] absolute left-0 z-10 h-full flex flex-col justify-center border-r border-white/50">
                <p data-i18n="heroText1" class="text-xl md:text-[28px] text-slate-800 mb-1 font-medium tracking-wide">Snap to Connect.</p>
                <p data-i18n="heroText2" class="text-xl md:text-[28px] text-slate-800 mb-4 pl-4 md:pl-8 font-medium tracking-wide">Ready to Control.</p>
                <h1 data-i18n="heroText3" class="text-5xl md:text-7xl font-black text-slate-900 tracking-tighter pl-8 md:pl-12">Plug & Play</h1>
                <div class="h-1.5 w-20 bg-snap-green mt-6 md:mt-8 ml-8 md:ml-12 rounded-full"></div>
                
                <!-- Social Links -->
                <div class="flex flex-wrap items-center gap-5 mt-8 md:mt-10 ml-8 md:ml-12">
                    <a href="tel:0812345678" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-snap-green hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fas fa-phone-alt"></i></a>
                    <a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-[#1877F2] hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://line.me" target="_blank" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-[#00B900] hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fab fa-line text-lg"></i></a>
                    <a href="mailto:snapcon1992@gmail.com" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-red-500 hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
        </section>

        <!-- Google Drive Cards Section -->
        <section class="w-full max-w-6xl mx-auto px-6 py-20">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                
                <!-- Data sheet -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer group">
                    <div class="bg-white border-2 border-slate-100 w-full py-16 px-6 flex flex-col items-center justify-center group-hover:border-snap-green group-hover:shadow-[0_20px_40px_rgba(0,179,110,0.1)] transition-all rounded-[2rem] shadow-sm">
                        <div class="w-16 h-16 bg-snap-green/10 text-snap-green rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform"><i class="fas fa-file-pdf"></i></div>
                        <h3 data-i18n="cardDataSheet" class="text-xl font-black text-slate-800 tracking-tight">Download Data Sheet</h3>
                    </div>
                    <div class="dropdown-menu top-[180px] w-11/12 bg-white border border-slate-100 shadow-2xl rounded-2xl overflow-hidden py-2">
                        <a href="https://drive.google.com/file/d/1HY0dUjYJZgxRVYYgN5DOV6Ymm9ARCGUW/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green/10 hover:text-snap-green border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 01</a>
                        <a href="https://drive.google.com/file/d/1TC_cXAy7gbgBx0QI0TiL7Kdt1ICljnHj/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green/10 hover:text-snap-green border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 02</a>
                        <a href="https://drive.google.com/file/d/1Yv_gJWWxTL4H_5YmCDAOCnI33gdfcj4j/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green/10 hover:text-snap-green border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 03</a>
                        <a href="https://drive.google.com/file/d/1KtCARlKphuuIqUOU6xg5mnPf99sjCjHD/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green/10 hover:text-snap-green border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 04</a>
                        <a href="https://drive.google.com/file/d/1dlOS1HSYy1qjWASPGQiKRvQsSyZ-lFs4/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green/10 hover:text-snap-green text-sm font-bold text-slate-600 transition-colors">Model 05</a>
                    </div>
                </div>

                <!-- Drawing -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer group">
                    <div class="bg-white border-2 border-slate-100 w-full py-16 px-6 flex flex-col items-center justify-center group-hover:border-blue-500 group-hover:shadow-[0_20px_40px_rgba(59,130,246,0.1)] transition-all rounded-[2rem] shadow-sm">
                        <div class="w-16 h-16 bg-blue-500/10 text-blue-500 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform"><i class="fas fa-drafting-compass"></i></div>
                        <h3 data-i18n="cardDrawing" class="text-xl font-black text-slate-800 tracking-tight">Download Drawing</h3>
                    </div>
                    <div class="dropdown-menu top-[180px] w-11/12 bg-white border border-slate-100 shadow-2xl rounded-2xl overflow-hidden py-2">
                        <a href="https://drive.google.com/file/d/1CisPrHXeoJgspikAzAOwH0rdhNtQiviy/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 01</a>
                        <a href="https://drive.google.com/file/d/1Gt8onVT7dsyJQkmxdY6s1GZTX4_oUNuB/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 02</a>
                        <a href="https://drive.google.com/file/d/1zesePgsPwZDTUpKzLrmesdnuY6usfe2P/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 03</a>
                        <a href="https://drive.google.com/file/d/1I-63QRJrJksO6xQb1cCWaq9HoDZJ6qBl/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 text-sm font-bold text-slate-600 transition-colors">Model 04</a>
                        <a href="https://drive.google.com/file/d/16z8m9S06kGhyO0C6Tb0mMQ0L4bk5wTDz/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-blue-50 hover:text-blue-600 text-sm font-bold text-slate-600 transition-colors">Model 05</a>
                    </div>
                </div>

                <!-- Catalog -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer group">
                    <div class="bg-white border-2 border-slate-100 w-full py-16 px-6 flex flex-col items-center justify-center group-hover:border-amber-500 group-hover:shadow-[0_20px_40px_rgba(245,158,11,0.1)] transition-all rounded-[2rem] shadow-sm">
                        <div class="w-16 h-16 bg-amber-500/10 text-amber-500 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform"><i class="fas fa-book-open"></i></div>
                        <h3 data-i18n="cardCatalog" class="text-xl font-black text-slate-800 tracking-tight">Product Catalog</h3>
                    </div>
                    <div class="dropdown-menu top-[180px] w-11/12 bg-white border border-slate-100 shadow-2xl rounded-2xl overflow-hidden py-2">
                        <a href="https://drive.google.com/file/d/1_-OdU-N7CnKfG6qY6WV7hW59vL1LX7KD/view?usp=drive_link" target="_blank" data-i18n="cardCatalogFull" class="block px-6 py-3 hover:bg-amber-50 hover:text-amber-600 text-sm font-bold text-slate-600 transition-colors">Download Full Catalog</a>
                    </div>
                </div>

            </div>
        </section>
    </div>

    <!-- ==================== PAGE: PRODUCT ==================== -->
    <div id="page-product" class="page-section max-w-7xl mx-auto px-6 py-16">
        <h2 data-i18n="pageProductTitle" class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800">SNAPCON Products</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8" id="product-grid"></div>
    </div>

    <!-- ==================== PAGE: CART (Shopee Style) ==================== -->
    <div id="page-cart" class="page-section max-w-5xl mx-auto px-6 py-16">
        <h2 data-i18n="pageCartTitle" class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800">รถเข็นขอใบเสนอราคา</h2>
        <div class="bg-white p-8 md:p-10 rounded-[2.5rem] shadow-xl shadow-slate-200/50 border border-slate-100">
            
            <div id="cart-header" class="flex justify-between items-center mb-8 pb-6 border-b border-slate-100">
                <div class="flex items-center gap-3">
                    <input type="checkbox" id="cart-select-all" onclick="toggleSelectAll(this.checked)" class="w-6 h-6 accent-snap-green cursor-pointer rounded">
                    <label for="cart-select-all" class="font-black text-slate-700 cursor-pointer text-lg" data-i18n="selectAll">เลือกทั้งหมด</label>
                </div>
                <button type="button" onclick="deleteSelected()" class="text-red-500 font-bold hover:text-red-600 transition-colors flex items-center gap-2 bg-red-50 px-4 py-2 rounded-xl" data-i18n="deleteSelected">
                    <i class="fas fa-trash-alt"></i> ลบที่เลือก
                </button>
            </div>

            <div id="cart-items" class="space-y-4 mb-10 min-h-[150px]">
                <p data-i18n="cartEmpty" class="text-center py-10 text-slate-400 font-bold text-lg">ยังไม่มีสินค้าในรถเข็น</p>
            </div>

            <!-- Guest Contact Form -->
            <div id="guest-form" class="bg-slate-50 p-8 rounded-3xl mb-10 border-2 border-dashed border-slate-200 hidden">
                <p class="font-black text-slate-700 mb-6 uppercase text-sm tracking-widest flex items-center gap-3">
                    <span class="w-8 h-8 rounded-full bg-blue-500 text-white flex items-center justify-center"><i class="fas fa-info"></i></span> 
                    ข้อมูลติดต่อกลับ (Contact Info)
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <input type="text" id="guest-name" placeholder="ชื่อผู้ติดต่อ / ชื่อบริษัท" class="px-6 py-4 rounded-2xl border-none ring-1 ring-slate-200 outline-none focus:ring-2 focus:ring-snap-green transition-all shadow-sm font-bold text-slate-700">
                    <input type="text" id="guest-contact" placeholder="อีเมล หรือ เบอร์โทรศัพท์" class="px-6 py-4 rounded-2xl border-none ring-1 ring-slate-200 outline-none focus:ring-2 focus:ring-snap-green transition-all shadow-sm font-bold text-slate-700">
                </div>
            </div>

            <div class="flex flex-col md:flex-row justify-between items-center border-t border-slate-100 pt-10 gap-6">
                <div class="text-center md:text-left">
                    <p class="text-slate-400 text-sm font-bold uppercase tracking-widest mb-1" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                    <h3 id="cart-total" class="text-5xl font-black text-snap-green">฿0</h3>
                </div>
                <button type="button" onclick="requestQuote()" class="w-full md:w-auto bg-nav-bg text-white px-10 py-5 rounded-2xl font-black hover:bg-snap-green transition-all shadow-xl active:scale-95 text-lg" data-i18n="btnRequestQuote">
                    ยื่นขอใบเสนอราคาอย่างเป็นทางการ
                </button>
            </div>
            <p class="text-[11px] text-slate-400 mt-6 text-center font-bold bg-slate-50 py-3 rounded-xl"><i class="fas fa-shield-alt text-snap-green mr-1"></i> ข้อมูลจะถูกบันทึกลงระบบ Google Drive: snapcon1992 อย่างปลอดภัย</p>
        </div>
    </div>

    <!-- ==================== PAGE: DASHBOARD ==================== -->
    <div id="page-dashboard" class="page-section max-w-7xl mx-auto px-6 py-16">
        <h2 class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800" data-i18n="navDashboard">Dashboard</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <div class="bg-white p-10 rounded-[2.5rem] shadow-lg border border-slate-100 relative overflow-hidden group">
                <div class="absolute top-0 left-0 w-2 h-full bg-snap-green"></div>
                <p class="text-sm text-slate-400 font-bold uppercase tracking-widest mb-3">Total Output</p>
                <h3 class="text-5xl font-black text-slate-800">4,520 <span class="text-lg text-slate-400">PCS</span></h3>
            </div>
            <div class="bg-white p-10 rounded-[2.5rem] shadow-lg border border-slate-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-2 h-full bg-blue-500"></div>
                <p class="text-sm text-slate-400 font-bold uppercase tracking-widest mb-3">Active Nodes</p>
                <h3 class="text-5xl font-black text-slate-800">10 / 10</h3>
            </div>
            <div class="bg-white p-10 rounded-[2.5rem] shadow-lg border border-slate-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-2 h-full bg-amber-500"></div>
                <p class="text-sm text-slate-400 font-bold uppercase tracking-widest mb-3">System Health</p>
                <h3 class="text-5xl font-black text-slate-800">98.5%</h3>
            </div>
        </div>
        <div class="bg-[#1e2329] p-24 rounded-[3rem] text-center text-white shadow-2xl relative overflow-hidden">
            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10"></div>
            <div class="relative z-10">
                <i class="fas fa-microchip text-7xl text-snap-green mb-8 animate-pulse"></i>
                <h3 class="text-3xl font-black tracking-tight mb-4">Real-time Telemetry Live</h3>
                <p class="text-slate-400 text-lg">Dashboard Pro is monitoring network connectivity via RS485</p>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: CONTACT & ABOUT ==================== -->
    <div id="page-contact" class="page-section max-w-4xl mx-auto px-6 py-16 text-center">
        <h2 class="text-4xl font-black mb-12 text-slate-800" data-i18n="navContact">Contact Us</h2>
        <div class="bg-white p-16 rounded-[4rem] shadow-2xl border border-slate-100 relative overflow-hidden">
            <div class="absolute -top-20 -right-20 w-64 h-64 bg-snap-green/10 blur-[80px] rounded-full"></div>
            <div class="w-24 h-24 bg-snap-green/10 text-snap-green rounded-[2rem] flex items-center justify-center text-4xl mx-auto mb-8 relative z-10 shadow-inner border border-snap-green/20">
                <i class="fas fa-envelope-open-text"></i>
            </div>
            <p class="text-3xl font-black text-slate-800 mb-4 relative z-10">snapcon1992@gmail.com</p>
            <p class="text-slate-500 font-medium mb-12 relative z-10 text-lg">Official Technical Support & Inquiries</p>
            <button onclick="window.location.href='mailto:snapcon1992@gmail.com'" class="relative z-10 bg-snap-green text-white px-14 py-5 rounded-2xl font-black text-lg hover:bg-green-600 transition-all shadow-[0_15px_30px_rgba(0,179,110,0.3)] active:scale-95 tracking-wide">SEND DIRECT EMAIL</button>
        </div>
    </div>

    <div id="page-about" class="page-section max-w-4xl mx-auto px-6 py-16">
        <h2 class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800" data-i18n="navAbout">About Us</h2>
        <div class="bg-white p-16 rounded-[4rem] shadow-xl border border-slate-100 leading-loose text-slate-600 text-xl font-medium">
            <p class="mb-8"><strong class="text-slate-900 font-black text-2xl">Snapcon Automation</strong> คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ <strong>Plug & Play System</strong></p>
            <p>เรามุ่งมั่นพัฒนาโซลูชันที่ช่วยลดระยะเวลาในการเซ็ตอัพเครื่องจักร ลดความยุ่งยากของระบบสายไฟ และเพิ่มประสิทธิภาพการผลิตได้สูงสุดด้วยระบบติดตามผลอัจฉริยะ (Smart Dashboard)</p>
        </div>
    </div>

    <script>
        // 🚀 DATABASE & CONFIG
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzTXYEcWYEsbcwL0ipt5vl1azB-C8psZUuwpjfIirzCdH2mBE2OHNdKSMoNPhklRt2M/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let memoryUsers = { '001': '123' };

        const dict = {
            th: {
                navProduct: "Products", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About Us",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "หยิบใส่รถเข็น",
                pageCartTitle: "รถเข็นขอใบเสนอราคา", cartEmpty: "ยังไม่มีสินค้าในรถเข็น", cartTotalLabel: "ราคากลางประเมินรวม:",
                btnRequestQuote: "ยื่นขอใบเสนอราคาอย่างเป็นทางการ", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก",
                specTitle: "รายละเอียดสำหรับสั่งทำ (Customizable):",
                alertLoginSuccess: "เข้าสู่ระบบสำเร็จ!", alertAddCart: "เพิ่มลงรถเข็นแล้ว!",
                alertQuoteReq: "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อกลับเพื่อให้ทีมงานส่งใบเสนอราคาให้ท่านได้"
            },
            en: {
                navProduct: "Products", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About Us",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "Add to Cart",
                pageCartTitle: "Quotation Cart", cartEmpty: "Your cart is empty", cartTotalLabel: "Estimated Total:",
                btnRequestQuote: "Submit Official Quotation Request", selectAll: "Select All", deleteSelected: "Delete Selected",
                specTitle: "Specifications (Custom):",
                alertLoginSuccess: "Login Successful!", alertAddCart: "Added to cart!",
                alertQuoteReq: "Please select at least 1 item", alertQuoteGuestReq: "Please provide contact info so we can send the quote back to you."
            }
        };

        const products = [
            { 
                id: 'M01', name: 'Snapcon Model 01 (Mini)', price: 15000, img: 'https://i.ibb.co/bZ7TKQg/01.png',
                specs: { th: ["L: 0.5-5m", "H: 0.3-1m", "W: 200-400mm", "Load: 0-50kg", "Speed: 5-20m/min", "Material: Painted/AL"],
                         en: ["L: 0.5-5m", "H: 0.3-1m", "W: 200-400mm", "Load: 0-50kg", "Speed: 5-20m/min", "Material: Painted/AL"] }
            },
            { 
                id: 'M02', name: 'Snapcon Model 02 (Std)', price: 22000, img: 'https://i.ibb.co/tTCb2j0h/02.png',
                specs: { th: ["L: 1-15m", "H: 0.5-1.2m", "W: 300-600mm", "Load: 0-100kg", "Speed: 10-30m/min", "Material: Steel/SUS"],
                         en: ["L: 1-15m", "H: 0.5-1.2m", "W: 300-600mm", "Load: 0-100kg", "Speed: 10-30m/min", "Material: Steel/SUS"] }
            },
            { 
                id: 'M03', name: 'Snapcon Model 03 (Heavy)', price: 28500, img: 'https://i.ibb.co/PGNt8dfj/03.png',
                specs: { th: ["L: 2-30m", "H: 0.5-1.5m", "W: 500-1000mm", "Load: 0-300kg", "Speed: 5-25m/min", "Material: Heavy Steel"],
                         en: ["L: 2-30m", "H: 0.5-1.5m", "W: 500-1000mm", "Load: 0-300kg", "Speed: 5-25m/min", "Material: Heavy Steel"] }
            },
            { 
                id: 'M04', name: 'Snapcon Model 04 (Speed)', price: 35000, img: 'https://i.ibb.co/mVfD9H0B/04.png',
                specs: { th: ["L: 1-20m", "H: 0.8-1.5m", "W: 400-800mm", "Load: 0-80kg", "Speed: 20-60m/min", "Material: SUS 304"],
                         en: ["L: 1-20m", "H: 0.8-1.5m", "W: 400-800mm", "Load: 0-80kg", "Speed: 20-60m/min", "Material: SUS 304"] }
            },
            { 
                id: 'M05', name: 'Snapcon Pro 05 (Custom)', price: 45000, img: 'https://i.ibb.co/x4SGKtb/05.png',
                specs: { th: ["L: 5-100m", "H: 0.1-2m", "W: 500-1500mm", "Load: 0-400kg", "Speed: 1-50m/min", "Material: Full Custom"],
                         en: ["L: 5-100m", "H: 0.1-2m", "W: 500-1500mm", "Load: 0-400kg", "Speed: 1-50m/min", "Material: Full Custom"] }
            }
        ];

        // 🧭 NAVIGATION
        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            const target = document.getElementById('page-' + pageId);
            if(target) target.classList.add('page-active');
            if(pageId === 'cart') renderCart();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function checkDashboardAuth() {
            if (isLoggedIn) navigate('dashboard');
            else { alert(dict[currentLang].alertLoginReq || "Please Login first"); document.getElementById('userId').focus(); }
        }

        // 🔐 AUTH SYSTEM
        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            if (memoryUsers[id] === pass || (id==='001' && pass==='123')) {
                isLoggedIn = true;
                document.getElementById('displayUser').innerText = id || '001';
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('login-section').classList.remove('md:flex');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                alert(dict[currentLang].alertLoginSuccess);
                
                // Clear input
                document.getElementById('userId').value = '';
                document.getElementById('userPass').value = '';
            } else alert("Invalid ID/Pass");
        }

        function handleRegister() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            if(id && pass) {
                memoryUsers[id] = pass;
                alert("Registered! Now please Login.");
                try {
                    fetch(GOOGLE_SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: JSON.stringify({ type: "Registration", name_or_id: id, details: "New Account Created" }) });
                } catch(e) {}
            } else alert("Fill all fields");
        }

        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden');
            document.getElementById('login-section').classList.add('md:flex');
            document.getElementById('user-section').classList.add('hidden');
            document.getElementById('user-section').classList.remove('flex');
            navigate('home');
        }

        // 🛒 PRODUCT & CART SYSTEM
        function renderProducts() {
            const grid = document.getElementById('product-grid');
            if(!grid) return;
            grid.innerHTML = products.map(p => `
                <div class="bg-white border border-slate-100 p-6 rounded-[2rem] shadow-sm hover:shadow-[0_20px_40px_rgba(0,0,0,0.08)] transition-all duration-300 flex flex-col h-full group hover:-translate-y-2">
                    <div class="overflow-hidden rounded-2xl mb-5">
                        <img src="${p.img}" class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-500">
                    </div>
                    <h4 class="font-black text-xl text-slate-800 mb-4 tracking-tight">${p.name}</h4>
                    <div class="bg-slate-50 p-4 rounded-2xl mb-6 flex-grow border border-slate-100/50">
                        <p class="text-[10px] font-black text-snap-green uppercase tracking-widest mb-3 flex items-center gap-2"><i class="fas fa-sliders-h"></i> ${dict[currentLang].specTitle}</p>
                        <ul class="text-[11px] text-slate-500 space-y-2 font-medium">
                            ${p.specs[currentLang].map(s => `<li class="flex items-start gap-2"><span class="text-snap-green mt-0.5">•</span> ${s}</li>`).join('')}
                        </ul>
                    </div>
                    <p class="text-snap-green font-black text-3xl mb-5 tracking-tighter">฿${p.price.toLocaleString()}</p>
                    <button type="button" onclick="addToCart('${p.id}')" class="w-full bg-nav-bg text-white py-4 rounded-2xl font-black text-sm hover:bg-snap-green transition-all shadow-lg active:scale-95 tracking-wide">${dict[currentLang].btnAddToCart}</button>
                </div>
            `).join('');
        }

        function addToCart(id) {
            const p = products.find(i => i.id === id);
            cart.push({ ...p, cartId: Date.now() + Math.random(), selected: true });
            const b = document.getElementById('cart-badge');
            b.innerText = cart.length; b.classList.remove('hidden');
            
            // Animation for cart badge
            b.classList.add('animate-bounce');
            setTimeout(() => b.classList.remove('animate-bounce'), 1000);
            
            alert(dict[currentLang].alertAddCart);
        }

        function renderCart() {
            const container = document.getElementById('cart-items');
            const guestForm = document.getElementById('guest-form');
            if(!container) return;

            if (isLoggedIn) guestForm.classList.add('hidden'); else guestForm.classList.remove('hidden');

            if(cart.length === 0) {
                container.innerHTML = `<p class="text-center py-12 text-slate-400 font-bold text-lg bg-slate-50 rounded-3xl border border-dashed border-slate-200">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }

            container.innerHTML = cart.map(item => `
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center bg-white border border-slate-100 shadow-sm p-4 md:p-6 rounded-2xl gap-4 hover:shadow-md transition-shadow">
                    <div class="flex items-center gap-4 w-full sm:w-auto">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleItem(${item.cartId})" class="w-6 h-6 accent-snap-green cursor-pointer shrink-0 rounded">
                        <img src="${item.img}" class="w-20 h-20 object-cover rounded-xl shadow-sm border border-slate-100 shrink-0">
                        <div>
                            <span class="font-black text-slate-800 text-lg block leading-tight mb-1">${item.name}</span>
                            <span class="text-xs text-slate-400 font-bold uppercase tracking-widest bg-slate-50 px-2 py-1 rounded-md">MODEL: ${item.id}</span>
                        </div>
                    </div>
                    <span class="font-black text-slate-700 text-2xl self-end sm:self-auto">฿${item.price.toLocaleString()}</span>
                </div>
            `).join('');

            const total = cart.filter(i => i.selected).reduce((s, i) => s + i.price, 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
            
            // Check 'select all' box state
            const allSelected = cart.length > 0 && cart.every(i => i.selected);
            document.getElementById('cart-select-all').checked = allSelected;
        }

        function toggleItem(cartId) {
            const item = cart.find(i => i.cartId === cartId);
            if(item) item.selected = !item.selected;
            renderCart();
        }

        function toggleSelectAll(val) {
            cart.forEach(i => i.selected = val);
            renderCart();
        }

        function deleteSelected() {
            cart = cart.filter(i => !i.selected);
            document.getElementById('cart-badge').innerText = cart.length;
            if(cart.length === 0) document.getElementById('cart-badge').classList.add('hidden');
            renderCart();
        }

        function requestQuote() {
            const selected = cart.filter(i => i.selected);
            if(selected.length === 0) { alert(dict[currentLang].alertQuoteReq); return; }

            let name = isLoggedIn ? document.getElementById('displayUser').innerText : document.getElementById('guest-name').value;
            let info = isLoggedIn ? "Registered Account: " + name : document.getElementById('guest-contact').value;

            if(!isLoggedIn && (!name || !info)) { alert(dict[currentLang].alertQuoteGuestReq); return; }

            let detailsForEmail = selected.map(i => `- ${i.name} (%E0%B8%BF${i.price.toLocaleString()})`).join('%0A');
            let detailsForDB = selected.map(i => `- ${i.name} (฿${i.price.toLocaleString()})`).join('\\n');
            let total = selected.reduce((s, i) => s + i.price, 0);

            // 1. Send to Google Sheets (Background)
            try {
                fetch(GOOGLE_SCRIPT_URL, { 
                    method: 'POST', 
                    mode: 'no-cors', 
                    body: JSON.stringify({ 
                        type: "Quotation", 
                        name_or_id: name, 
                        email: info, 
                        details: `Items:\\n${detailsForDB}\\n\\nTotal: ฿${total.toLocaleString()}` 
                    }) 
                });
            } catch(e) {}

            // 2. Open Mailto (Official)
            const subject = encodeURIComponent("Quotation Request - Snapcon (" + name + ")");
            const body = "Request for Official Quotation:%0A%0AItems:%0A" + detailsForEmail + "%0A%0AEstimated Total: %E0%B8%BF" + total.toLocaleString() + "%0A%0AContact Info: " + encodeURIComponent(info) + "%0A%0A* Auto-generated by Snapcon System *";
            window.location.href = `mailto:snapcon1992@gmail.com?subject=${subject}&body=${body}`;

            alert("Processing Quote Request...");
            cart = cart.filter(i => !i.selected);
            document.getElementById('cart-badge').innerText = cart.length;
            if(cart.length === 0) document.getElementById('cart-badge').classList.add('hidden');
            renderCart();
            navigate('home');
        }

        // 🌐 LANGUAGE SYSTEM
        function setLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[lang][key]) el.innerHTML = dict[lang][key];
            });
            // Update Lang Buttons Style
            document.getElementById('btn-lang-th').className = lang === 'th' ? "text-[9px] font-bold px-2.5 py-1 rounded-full bg-snap-green text-white transition-colors" : "text-[9px] font-bold px-2.5 py-1 rounded-full text-slate-400 hover:text-white transition-colors";
            document.getElementById('btn-lang-en').className = lang === 'en' ? "text-[9px] font-bold px-2.5 py-1 rounded-full bg-snap-green text-white transition-colors" : "text-[9px] font-bold px-2.5 py-1 rounded-full text-slate-400 hover:text-white transition-colors";
            renderProducts();
            if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        // INIT
        setLanguage('th');
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=1400, scrolling=True)
