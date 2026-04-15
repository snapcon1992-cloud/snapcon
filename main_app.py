import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS ฉบับสมบูรณ์ที่สุด (The Ultimate Version) พร้อมระบบ Dashboard เต็มรูปแบบ
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
            position: relative;
            background-color: #0f172a;
        }
        
        .hero-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, #ffffff 40%, rgba(124, 224, 184, 0.9) 70%, rgba(124, 224, 184, 0.5) 100%);
            z-index: 5;
            pointer-events: none;
        }

        /* ---- Image Slider Background Animations ---- */
        .slide-img {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover;
            background-position: center;
            opacity: 0;
            animation: slideBgAnimation 20s infinite linear;
        }

        /* ภาพที่ 1: แขนกล Automation */
        .slide-1 { background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80'); animation-delay: 0s; }
        /* ภาพที่ 2: เส้นแสงความเร็ว Fiber Optic */
        .slide-2 { background-image: url('https://images.unsplash.com/photo-1614729939124-032f0b56c9ce?auto=format&fit=crop&w=1920&q=80'); animation-delay: 5s; }
        /* ภาพที่ 3: ระบบเซิร์ฟเวอร์ ทันสมัย */
        .slide-3 { background-image: url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1920&q=80'); animation-delay: 10s; }
        /* ภาพที่ 4: แผงวงจรชิปอัจฉริยะ */
        .slide-4 { background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1920&q=80'); animation-delay: 15s; }

        @keyframes slideBgAnimation {
            0% { opacity: 0; transform: scale(1.1) translateX(30px); }
            5% { opacity: 1; transform: scale(1.1) translateX(20px); }
            20% { opacity: 1; transform: scale(1.1) translateX(-10px); }
            25% { opacity: 0; transform: scale(1.1) translateX(-20px); }
            100% { opacity: 0; }
        }

        .page-section { display: none !important; }
        .page-active { display: block !important; animation: fadeIn 0.4s ease-out forwards; }
        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes modalShow { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        
        .modal-active { animation: modalShow 0.3s ease-out forwards; }
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
        
        /* ซ่อน Scrollbar แต่ยัง Scroll ได้ */
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        
        /* ซ่อน Scrollbar สำหรับ Slider */
        .slider-container::-webkit-scrollbar { display: none; }
        .slider-container { -ms-overflow-style: none; scrollbar-width: none; scroll-behavior: smooth; }
        
        /* ---- เพิ่ม Animation ใหม่สำหรับ Logo & Hero ---- */
        .animate-gradient-text {
            background: linear-gradient(90deg, #00B36E 0%, #06b6d4 25%, #3b82f6 50%, #00B36E 100%);
            background-size: 300% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient-sweep 4s linear infinite;
        }
        @keyframes gradient-sweep {
            0% { background-position: 100% 0%; }
            100% { background-position: 0% 0%; }
        }
        
        .animate-speed-slide-1 {
            animation: speed-slide 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
            opacity: 0;
            transform: translateX(-50px) skewX(-15deg);
        }
        .animate-speed-slide-2 {
            animation: speed-slide 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.2s forwards;
            opacity: 0;
            transform: translateX(-50px) skewX(-15deg);
        }
        .animate-speed-slide-3 {
            animation: speed-slide-up 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.4s forwards;
            opacity: 0;
            transform: translateY(30px);
        }
        @keyframes speed-slide {
            100% { opacity: 1; transform: translateX(0) skewX(0); }
        }
        @keyframes speed-slide-up {
            100% { opacity: 1; transform: translateY(0); }
        }
        
        .energy-line {
            position: relative;
            overflow: hidden;
        }
        .energy-line::after {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 50%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
            animation: light-beam 2.5s linear infinite;
        }
        @keyframes light-beam {
            100% { left: 200%; }
        }
        
        .logo-glow {
            filter: drop-shadow(0 0 8px rgba(0, 179, 110, 0.6));
        }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar -->
    <nav class="bg-nav-bg h-[65px] w-full fixed top-0 z-50 flex items-center justify-between px-4 md:px-6 border-b-4 border-snap-green shadow-lg">
        <!-- Logo -->
        <div class="flex items-center gap-3 cursor-pointer h-full shrink-0 group" onclick="navigate('home')">
            <div class="relative flex items-center justify-center w-10 h-10 bg-gradient-to-br from-snap-green to-emerald-900 rounded-xl shadow-[0_0_15px_rgba(0,179,110,0.4)] group-hover:shadow-[0_0_25px_rgba(0,179,110,0.8)] transition-all overflow-hidden">
                <i class="fas fa-bolt text-white text-xl animate-pulse relative z-10"></i>
                <div class="absolute inset-0 bg-white/20 energy-line"></div>
            </div>
            <div class="flex flex-col justify-center">
                <span class="font-black text-xl md:text-2xl text-transparent bg-clip-text bg-gradient-to-r from-snap-green to-emerald-400 tracking-tight leading-none mt-1 logo-glow transition-all">SNAPCON</span>
                <div class="flex items-center gap-1.5 mt-0.5">
                    <div class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></div>
                    <span class="font-bold text-[9px] md:text-[10px] text-slate-400 tracking-[0.2em] leading-none uppercase">Automation</span>
                </div>
            </div>
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
                    <!-- เปลี่ยนปุ่ม Register ให้เรียกหน้าต่าง Modal แทน -->
                    <button type="button" onclick="openRegisterModal()" data-i18n="navRegister" class="bg-slate-600 text-white font-bold text-[9px] px-3 py-0.5 hover:bg-slate-500 rounded transition-colors">Register</button>
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
        <section class="w-full h-[350px] md:h-[450px] hero-bg relative flex items-center border-b border-gray-200 overflow-hidden">
            
            <!-- Animated Background Slider -->
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            
            <!-- Gradient Overlay -->
            <div class="hero-overlay"></div>

            <div class="bg-white/90 backdrop-blur-md pl-6 md:pl-12 pr-12 md:pr-20 py-10 md:py-16 ml-0 shadow-[20px_0_40px_-10px_rgba(0,0,0,0.15)] absolute left-0 z-10 h-full flex flex-col justify-center border-r border-white/50 overflow-hidden">
                <!-- Tech grid background for modern feel -->
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] pointer-events-none"></div>
                
                <div class="relative z-10">
                    <div class="flex items-center gap-3 mb-1 animate-speed-slide-1">
                        <i class="fas fa-angle-double-right text-snap-green animate-pulse"></i>
                        <p data-i18n="heroText1" class="text-xl md:text-[28px] text-slate-600 font-bold tracking-widest uppercase italic">Snap to Connect.</p>
                    </div>
                    <div class="flex items-center gap-3 mb-4 pl-4 md:pl-8 animate-speed-slide-2">
                        <i class="fas fa-angle-double-right text-blue-500 animate-pulse"></i>
                        <p data-i18n="heroText2" class="text-xl md:text-[28px] text-slate-800 font-black tracking-widest uppercase italic">Ready to Control.</p>
                    </div>
                    <h1 class="animate-speed-slide-3 text-6xl md:text-[85px] font-black tracking-tighter pl-8 md:pl-12 mt-2 mb-2 leading-none">
                        <span data-i18n="heroText3" class="animate-gradient-text drop-shadow-xl pb-2">Plug & Play</span>
                    </h1>
                    <div class="animate-speed-slide-3 h-2 w-40 bg-gradient-to-r from-snap-green to-blue-500 mt-6 md:mt-8 ml-8 md:ml-12 rounded-full energy-line shadow-[0_0_15px_rgba(0,179,110,0.6)]"></div>
                    
                    <!-- Social Links -->
                    <div class="flex flex-wrap items-center gap-5 mt-8 md:mt-10 ml-8 md:ml-12 animate-speed-slide-3" style="animation-delay: 0.6s;">
                        <a href="tel:0812345678" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-snap-green hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fas fa-phone-alt"></i></a>
                        <a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-[#1877F2] hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://line.me" target="_blank" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-[#00B900] hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fab fa-line text-lg"></i></a>
                        <a href="mailto:snapcon1992@gmail.com" class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:bg-red-500 hover:text-white transition-all hover:scale-110 shadow-sm"><i class="fas fa-envelope"></i></a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Google Drive Cards Section -->
        <section class="w-full max-w-6xl mx-auto px-6 py-16">
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

        <!-- 🎉 New Section: Home Product Slider -->
        <section class="w-full max-w-7xl mx-auto px-6 py-12 border-t border-slate-200/60 bg-slate-50/50 rounded-t-[3rem]">
            <div class="flex justify-between items-end mb-8">
                <div>
                    <h2 class="text-3xl md:text-4xl font-black text-slate-800 tracking-tight" data-i18n="homeProductsTitle">สินค้าของเรา</h2>
                    <p class="text-slate-500 mt-2 font-medium" data-i18n="homeProductsSub">เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด</p>
                </div>
                <div class="hidden sm:flex gap-3">
                    <button onclick="scrollSlider('left')" class="w-12 h-12 rounded-full bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white hover:border-snap-green transition-all shadow-sm active:scale-95"><i class="fas fa-chevron-left"></i></button>
                    <button onclick="scrollSlider('right')" class="w-12 h-12 rounded-full bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white hover:border-snap-green transition-all shadow-sm active:scale-95"><i class="fas fa-chevron-right"></i></button>
                </div>
            </div>
            
            <!-- Slider Container -->
            <div id="home-product-slider" class="slider-container flex gap-6 overflow-x-auto snap-x snap-mandatory pb-8 pt-2 px-2 -mx-2">
                <!-- Products will be injected here via JS -->
            </div>
            
            <div class="text-center mt-4">
                <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-snap-green font-bold text-sm hover:underline" data-i18n="viewAllProducts">ดูสินค้าทั้งหมด <i class="fas fa-arrow-right"></i></button>
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

    <!-- ==================== PAGE: DASHBOARD (ADVANCED INTERACTIVE) ==================== -->
    <div id="page-dashboard" class="page-section max-w-7xl mx-auto px-6 py-16">
        <h2 class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800" data-i18n="navDashboard">Dashboard</h2>
        
        <!-- Controls & Settings Row -->
        <div class="bg-white p-6 md:p-8 rounded-[2rem] shadow-sm border border-slate-100 mb-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- 1-3. Control Buttons with Export CSV -->
            <div>
                <h3 class="font-black text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wider text-sm" data-i18n="dashCtrlTitle"><i class="fas fa-gamepad text-blue-500"></i> การควบคุมระบบ</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                    <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-green-600 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-play mr-1 md:mr-2"></i> START</button>
                    <button onclick="stopSystem()" id="btn-stop" class="bg-slate-100 text-slate-600 py-3 md:py-4 rounded-2xl font-black shadow-sm hover:bg-red-500 hover:text-white active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-stop mr-1 md:mr-2"></i> STOP</button>
                    <button onclick="resetSystem()" class="bg-slate-800 text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-slate-700 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-sync-alt mr-1 md:mr-2"></i> REFRESH</button>
                    <button onclick="exportCSV()" class="bg-blue-500 text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-blue-600 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-file-csv mr-1 md:mr-2"></i> REPORT</button>
                </div>
            </div>
            
            <!-- 6. Configuration Inputs -->
            <div>
                <h3 class="font-black text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wider text-sm" data-i18n="dashCfgTitle"><i class="fas fa-sliders-h text-amber-500"></i> ตั้งค่าพารามิเตอร์</h3>
                <div class="grid grid-cols-3 gap-4">
                    <div class="bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1" data-i18n="dashTarget">เป้าหมาย (ชิ้น)</label>
                        <input type="number" id="cfg-target" value="5000" onchange="updateDashboardConfig()" class="w-full bg-transparent outline-none font-bold text-slate-800">
                    </div>
                    <div class="bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1" data-i18n="dashCarbon">ค่าคาร์บอน</label>
                        <input type="number" step="0.0001" id="cfg-carbon" value="0.0072" onchange="updateDashboardConfig()" class="w-full bg-transparent outline-none font-bold text-slate-800">
                    </div>
                    <div class="bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1" data-i18n="dashEnergy">ค่าพลังงาน</label>
                        <input type="number" step="0.001" id="cfg-energy" value="0.015" onchange="updateDashboardConfig()" class="w-full bg-transparent outline-none font-bold text-slate-800">
                    </div>
                </div>
            </div>
        </div>

        <!-- 4. Production Planning (Progress) with Time Calculation -->
        <div class="bg-white p-8 md:p-10 rounded-[2rem] shadow-sm border border-slate-100 mb-8 relative overflow-hidden">
            <div class="absolute right-0 top-0 w-32 h-full bg-gradient-to-l from-snap-green/5 to-transparent"></div>
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-6 relative z-10">
                <div>
                    <h3 class="text-2xl font-black text-slate-800 tracking-tight" data-i18n="dashPlanTitle">แผนการทำงานวันนี้ (Production Planning)</h3>
                    <p class="text-sm font-bold text-slate-400 mt-1" data-i18n="dashPlanSub">ความคืบหน้าของเป้าหมายการผลิตวันนี้ (Progress Update)</p>
                </div>
                <div class="mt-4 sm:mt-0 text-right">
                    <span id="dash-progress-text" class="text-4xl font-black text-snap-green">0.0%</span>
                </div>
            </div>
            
            <div class="w-full h-6 bg-slate-100 rounded-full overflow-hidden border border-slate-200/50 relative z-10 shadow-inner mb-4">
                <div id="dash-progress-bar" class="h-full bg-gradient-to-r from-emerald-400 to-snap-green transition-all duration-300 relative" style="width: 0%">
                    <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/diagonal-stripes.png')] opacity-30"></div>
                </div>
            </div>
            
            <!-- Time Calculation Display -->
            <div class="flex flex-col sm:flex-row justify-between relative z-10 gap-3">
                <div class="flex items-center gap-2 text-slate-500 text-xs font-bold uppercase tracking-widest bg-slate-50 px-4 py-2 rounded-xl border border-slate-100">
                    <i class="fas fa-clock text-slate-400"></i> <span data-i18n="dashTimeElapsed">เวลาที่ใช้ (Elapsed)</span>: 
                    <span id="dash-time-elapsed" class="text-slate-700 font-black ml-1">00:00:00</span>
                </div>
                <div class="flex items-center gap-2 text-amber-600 text-xs font-bold uppercase tracking-widest bg-amber-50 px-4 py-2 rounded-xl border border-amber-200 shadow-sm">
                    <i class="fas fa-stopwatch text-amber-500"></i> <span data-i18n="dashTimeRemain">เวลาคงเหลือโดยประมาณ (ETA)</span>: 
                    <span id="dash-time-remain" class="text-amber-700 font-black ml-1">--:--:--</span>
                </div>
            </div>
        </div>

        <!-- 5, 6, 7. Main KPIs -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 relative overflow-hidden group">
                <div class="absolute top-0 left-0 w-2 h-full bg-blue-500"></div>
                <div class="flex justify-between items-start mb-2">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-widest" data-i18n="dashTotOut">ยอดผลิตรวม (Total Output)</p>
                    <i class="fas fa-boxes text-blue-100 text-3xl"></i>
                </div>
                <h3 id="dash-total-output" class="text-5xl font-black text-slate-800">0</h3>
                <p class="text-[11px] text-slate-400 font-bold mt-2 uppercase">Units Produced</p>
            </div>
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 relative overflow-hidden group">
                <div class="absolute top-0 left-0 w-2 h-full bg-emerald-500"></div>
                <div class="flex justify-between items-start mb-2">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-widest" data-i18n="dashCalCarbon">คาร์บอนฟุตพริ้นท์ (Cal Carbon)</p>
                    <i class="fas fa-leaf text-emerald-100 text-3xl"></i>
                </div>
                <h3 id="dash-carbon" class="text-5xl font-black text-slate-800">0.00</h3>
                <p class="text-[11px] text-slate-400 font-bold mt-2 uppercase">kgCO2e</p>
            </div>
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 relative overflow-hidden group">
                <div class="absolute top-0 left-0 w-2 h-full bg-amber-500"></div>
                <div class="flex justify-between items-start mb-2">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-widest" data-i18n="dashTotPower">พลังงานไฟฟ้ารวม (Total Power Use)</p>
                    <i class="fas fa-bolt text-amber-100 text-3xl"></i>
                </div>
                <h3 id="dash-power" class="text-5xl font-black text-slate-800">0.00</h3>
                <p class="text-[11px] text-slate-400 font-bold mt-2 uppercase">kWh</p>
            </div>
        </div>

        <!-- 8. Machine Status Grid -->
        <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3" data-i18n="dashMacStatus">
            <i class="fas fa-server text-slate-400"></i> สถานะการทำงานแต่ละเครื่อง
        </h3>
        <div id="dash-nodes-grid" class="grid grid-cols-2 md:grid-cols-5 gap-5">
            <!-- Node cards injected by JS -->
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

    <!-- ==================== MODAL: REGISTER ==================== -->
    <div id="modal-register" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md rounded-[2rem] shadow-2xl relative overflow-hidden flex flex-col max-h-[90vh]">
            <button onclick="closeRegisterModal()" class="absolute top-6 right-6 text-slate-400 hover:text-red-500 transition-colors z-10">
                <i class="fas fa-times text-xl"></i>
            </button>
            
            <div class="p-8 pb-6 border-b border-slate-100 shrink-0">
                <h3 class="text-2xl font-black text-slate-800" data-i18n="regTitle">สร้างบัญชีผู้ใช้</h3>
                <p class="text-sm text-slate-500 mt-2" data-i18n="regDesc">ลงทะเบียนเพื่อเข้าถึง Dashboard และขอใบเสนอราคา</p>
            </div>
            
            <div class="p-8 space-y-5 overflow-y-auto no-scrollbar flex-1">
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2" data-i18n="regId">รหัสผู้ใช้ (User ID)</label>
                    <input type="text" id="reg-id" class="w-full px-5 py-3.5 rounded-xl bg-slate-50 border border-slate-200 outline-none focus:ring-2 focus:ring-snap-green/50 focus:border-snap-green transition-all text-sm font-bold text-slate-700" placeholder="ตั้งรหัส ID สำหรับเข้าระบบ">
                </div>
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2" data-i18n="regPass">รหัสผ่าน (Password)</label>
                    <input type="password" id="reg-pass" class="w-full px-5 py-3.5 rounded-xl bg-slate-50 border border-slate-200 outline-none focus:ring-2 focus:ring-snap-green/50 focus:border-snap-green transition-all text-sm font-bold text-slate-700" placeholder="ตั้งรหัสผ่านของคุณ">
                </div>
                <div class="h-[1px] bg-slate-100 my-2"></div>
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2" data-i18n="regName">ชื่อ-นามสกุล / ชื่อบริษัท</label>
                    <input type="text" id="reg-name" class="w-full px-5 py-3.5 rounded-xl bg-slate-50 border border-slate-200 outline-none focus:ring-2 focus:ring-snap-green/50 focus:border-snap-green transition-all text-sm font-bold text-slate-700" placeholder="ระบุชื่อสำหรับติดต่อ">
                </div>
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2" data-i18n="regContact">อีเมล / เบอร์โทรศัพท์</label>
                    <input type="text" id="reg-contact" class="w-full px-5 py-3.5 rounded-xl bg-slate-50 border border-slate-200 outline-none focus:ring-2 focus:ring-snap-green/50 focus:border-snap-green transition-all text-sm font-bold text-slate-700" placeholder="ระบุช่องทางติดต่อกลับ">
                </div>
            </div>
            
            <div class="p-8 pt-6 border-t border-slate-100 bg-slate-50 shrink-0">
                <button type="button" onclick="submitRegistration()" class="w-full bg-snap-green text-white py-4 rounded-xl font-black hover:bg-green-600 transition-all shadow-[0_10px_20px_rgba(0,179,110,0.2)] active:scale-95" data-i18n="btnSubmitReg">ยืนยันการลงทะเบียน</button>
            </div>
        </div>
    </div>

    <script>
        // 🚀 DATABASE & CONFIG
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzTXYEcWYEsbcwL0ipt5vl1azB-C8psZUuwpjfIirzCdH2mBE2OHNdKSMoNPhklRt2M/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let memoryUsers = { '001': '123' };

        // 📊 DASHBOARD STATE
        let dashState = {
            isRunning: false,
            target: 5000,
            carbonFactor: 0.0072,
            energyFactor: 0.015,
            intervalId: null,
            elapsedSeconds: 0, // สำหรับจับเวลา
            nodes: Array.from({length: 10}, (_, i) => ({
                id: i + 1,
                name: `Machine ${String(i+1).padStart(2, '0')}`,
                output: 0,
                status: 'Offline'
            }))
        };

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
                alertQuoteReq: "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อกลับเพื่อให้ทีมงานส่งใบเสนอราคาให้ท่านได้",
                regTitle: "สร้างบัญชีผู้ใช้", regDesc: "ลงทะเบียนเพื่อเข้าถึง Dashboard และระบบขอใบเสนอราคา",
                regId: "รหัสผู้ใช้ (User ID)", regPass: "รหัสผ่าน (Password)", regName: "ชื่อ-นามสกุล / ชื่อบริษัท", regContact: "อีเมล / เบอร์โทรศัพท์", btnSubmitReg: "ยืนยันการลงทะเบียน",
                homeProductsTitle: "สินค้าของเรา", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด", viewAllProducts: "ดูสินค้าทั้งหมด",
                // Dashboard Dictionary
                dashCtrlTitle: "การควบคุมระบบ", dashCfgTitle: "ตั้งค่าพารามิเตอร์", dashTarget: "เป้าหมาย (ชิ้น)", dashCarbon: "ค่าคาร์บอน", dashEnergy: "ค่าพลังงาน",
                dashPlanTitle: "แผนการทำงานวันนี้ (Production Planning)", dashPlanSub: "ความคืบหน้าของเป้าหมายการผลิตวันนี้", dashTotOut: "ยอดผลิตรวม (Total Output)",
                dashCalCarbon: "คาร์บอนฟุตพริ้นท์ (Cal Carbon)", dashTotPower: "พลังงานไฟฟ้ารวม (Total Power Use)", dashMacStatus: "สถานะการทำงานแต่ละเครื่อง",
                dashTimeElapsed: "เวลาที่ใช้ (Elapsed)", dashTimeRemain: "เวลาคงเหลือโดยประมาณ (ETA)"
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
                alertQuoteReq: "Please select at least 1 item", alertQuoteGuestReq: "Please provide contact info so we can send the quote back to you.",
                regTitle: "Create Account", regDesc: "Register to access Dashboard and Quotation features",
                regId: "User ID", regPass: "Password", regName: "Full Name / Company", regContact: "Email / Phone", btnSubmitReg: "Confirm Registration",
                homeProductsTitle: "Our Products", homeProductsSub: "Explore our latest automation machines and equipment", viewAllProducts: "View All Products",
                // Dashboard Dictionary
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target (Units)", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashPlanSub: "Progress update for today's target", dashTotOut: "Total Output",
                dashCalCarbon: "Cal Carbon Footprint", dashTotPower: "Total Power Use", dashMacStatus: "Machine Status",
                dashTimeElapsed: "Elapsed Time", dashTimeRemain: "Est. Remaining (ETA)"
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

        // Modal Controls
        function openRegisterModal() {
            const modal = document.getElementById('modal-register');
            modal.classList.remove('hidden');
            modal.classList.add('flex', 'modal-active');
        }

        function closeRegisterModal() {
            const modal = document.getElementById('modal-register');
            modal.classList.add('hidden');
            modal.classList.remove('flex', 'modal-active');
        }

        function submitRegistration() {
            const id = document.getElementById('reg-id').value;
            const pass = document.getElementById('reg-pass').value;
            const name = document.getElementById('reg-name').value;
            const contact = document.getElementById('reg-contact').value;

            if(!id || !pass || !name || !contact) {
                alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบถ้วนทุกช่อง" : "Please fill in all fields.");
                return;
            }

            if(memoryUsers[id]) {
                alert(currentLang === 'th' ? "ID นี้มีผู้ใช้งานแล้ว กรุณาเลือก ID อื่น" : "This ID is already registered. Please choose another.");
                return;
            }

            memoryUsers[id] = pass;
            
            try {
                fetch(GOOGLE_SCRIPT_URL, { 
                    method: 'POST', 
                    mode: 'no-cors', 
                    body: JSON.stringify({ 
                        type: "Registration", 
                        name_or_id: id, 
                        email: contact,
                        details: `Name/Company: ${name}\\nPassword: ${pass}` 
                    }) 
                });
            } catch(e) {}

            alert(currentLang === 'th' ? "ลงทะเบียนสำเร็จ! กรุณา Login ด้วย ID ที่สร้าง" : "Registered successfully! Please Login.");
            
            document.getElementById('userId').value = id;
            document.getElementById('userPass').value = pass;
            
            closeRegisterModal();
        }

        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden');
            document.getElementById('login-section').classList.add('md:flex');
            document.getElementById('user-section').classList.add('hidden');
            document.getElementById('user-section').classList.remove('flex');
            stopSystem(); // Stop dashboard if running
            navigate('home');
        }

        // 📊 DASHBOARD FUNCTIONS
        function startSystem() {
            dashState.isRunning = true;
            document.getElementById('btn-start').classList.add('ring-4', 'ring-green-500/50', 'scale-105');
            document.getElementById('btn-stop').classList.remove('ring-4', 'ring-red-500/50', 'bg-red-500', 'text-white', 'scale-105');
            document.getElementById('btn-stop').classList.add('bg-slate-100', 'text-slate-600');
            dashState.nodes.forEach(n => n.status = 'Running');
            
            if(!dashState.intervalId) {
                dashState.intervalId = setInterval(simulateProduction, 500); // อัปเดตทุก 0.5 วินาที
            }
            renderDashboard();
        }

        function stopSystem() {
            dashState.isRunning = false;
            document.getElementById('btn-start').classList.remove('ring-4', 'ring-green-500/50', 'scale-105');
            document.getElementById('btn-stop').classList.remove('bg-slate-100', 'text-slate-600');
            document.getElementById('btn-stop').classList.add('ring-4', 'ring-red-500/50', 'bg-red-500', 'text-white', 'scale-105');
            dashState.nodes.forEach(n => n.status = 'Stopped');
            
            if(dashState.intervalId) {
                clearInterval(dashState.intervalId);
                dashState.intervalId = null;
            }
            renderDashboard();
        }

        function resetSystem() {
            dashState.nodes.forEach(n => n.output = 0);
            dashState.elapsedSeconds = 0;
            renderDashboard();
        }

        function updateDashboardConfig() {
            dashState.target = parseInt(document.getElementById('cfg-target').value) || 1;
            dashState.carbonFactor = parseFloat(document.getElementById('cfg-carbon').value) || 0;
            dashState.energyFactor = parseFloat(document.getElementById('cfg-energy').value) || 0;
            renderDashboard();
        }

        function simulateProduction() {
            if(!dashState.isRunning) return;
            
            // บวกเวลาที่ใช้ไปรอบละ 0.5 วินาที
            dashState.elapsedSeconds += 0.5;
            
            // สุ่มให้แต่ละเครื่องผลิตทีละ 1 ชิ้น โอกาสผลิต 50% ต่อครึ่งวินาที
            dashState.nodes.forEach(n => {
                if(Math.random() > 0.5) n.output += 1;
            });
            renderDashboard();
        }
        
        // ฟังก์ชันโหลดข้อมูล CSV ของหน้า Dashboard
        function exportCSV() {
            // ใส่รหัสป้องกันภาษาไทยเพี้ยนในไฟล์ Excel (BOM)
            let bom = "\\uFEFF";
            let csvContent = bom + "Node ID,Machine Name,Status,Output (Units),Est. Carbon (kgCO2e),Est. Power (kWh)\\n";
            
            let totalOut = 0;
            
            // ดึงข้อมูลแต่ละเครื่อง
            dashState.nodes.forEach(n => {
                let c = (n.output * dashState.carbonFactor).toFixed(4);
                let e = (n.output * dashState.energyFactor).toFixed(4);
                totalOut += n.output;
                csvContent += `${n.id},${n.name},${n.status},${n.output},${c},${e}\\n`;
            });
            
            // แถวสรุปผล (Total)
            let totalC = (totalOut * dashState.carbonFactor).toFixed(4);
            let totalE = (totalOut * dashState.energyFactor).toFixed(4);
            csvContent += `\\nTOTAL,, ,${totalOut},${totalC},${totalE}\\n`;
            
            // ใส่เวลาในการดาวน์โหลด
            let now = new Date();
            csvContent += `\\nExported At,${now.toLocaleString()}\\n`;
            
            // สร้างไฟล์เพื่อดาวน์โหลด
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement("a");
            const url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            
            // ตั้งชื่อไฟล์ตามเวลาปัจจุบัน
            let dateStr = now.toISOString().slice(0, 10);
            let timeStr = now.toTimeString().slice(0, 8).replace(/:/g, "-");
            link.setAttribute("download", `Snapcon_Dashboard_Report_${dateStr}_${timeStr}.csv`);
            
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            // แจ้งเตือนเมื่อดาวน์โหลดสำเร็จ
            if (currentLang === 'th') {
                alert("กำลังดาวน์โหลดไฟล์รายงาน CSV...");
            } else {
                alert("Downloading CSV Report...");
            }
        }

        // ฟังก์ชันช่วยแปลงเวลา (วินาที เป็น HH:MM:SS)
        function formatTimeStr(totalSeconds) {
            if (!isFinite(totalSeconds) || totalSeconds < 0) return "--:--:--";
            const h = Math.floor(totalSeconds / 3600);
            const m = Math.floor((totalSeconds % 3600) / 60);
            const s = Math.floor(totalSeconds % 60);
            return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        }

        function renderDashboard() {
            const grid = document.getElementById('dash-nodes-grid');
            if(!grid) return; // Not initialized yet

            const totalOutput = dashState.nodes.reduce((sum, n) => sum + n.output, 0);
            const totalCarbon = totalOutput * dashState.carbonFactor;
            const totalEnergy = totalOutput * dashState.energyFactor;
            let progress = (totalOutput / dashState.target) * 100;
            if(progress > 100) progress = 100;

            // Update KPIs
            document.getElementById('dash-total-output').innerText = totalOutput.toLocaleString();
            document.getElementById('dash-carbon').innerText = totalCarbon.toFixed(2);
            document.getElementById('dash-power').innerText = totalEnergy.toFixed(2);
            
            // Update Progress Bar
            document.getElementById('dash-progress-bar').style.width = `${progress}%`;
            document.getElementById('dash-progress-text').innerText = `${progress.toFixed(1)}%`;
            
            // Update Time Calculation
            let elapsedStr = formatTimeStr(dashState.elapsedSeconds);
            let remainStr = "--:--:--";
            
            if (totalOutput > 0 && dashState.elapsedSeconds > 0) {
                let unitsPerSecond = totalOutput / dashState.elapsedSeconds;
                let remainUnits = dashState.target - totalOutput;
                
                if (remainUnits > 0 && unitsPerSecond > 0) {
                    remainStr = formatTimeStr(remainUnits / unitsPerSecond);
                } else if (remainUnits <= 0) {
                    remainStr = "00:00:00";
                }
            } else if (dashState.target <= totalOutput) {
                remainStr = "00:00:00";
            }
            
            const elElapsed = document.getElementById('dash-time-elapsed');
            const elRemain = document.getElementById('dash-time-remain');
            
            if (elElapsed) elElapsed.innerText = elapsedStr;
            if (elRemain) {
                elRemain.innerText = remainStr;
                if (dashState.target <= totalOutput) {
                    elRemain.innerText += " (Completed)";
                }
            }

            // Update Grid
            grid.innerHTML = dashState.nodes.map(n => {
                const isRunning = n.status === 'Running';
                const isStopped = n.status === 'Stopped';
                const statusColorClass = isRunning ? 'text-snap-green' : (isStopped ? 'text-red-500' : 'text-slate-400');
                const dotColorClass = isRunning ? 'bg-snap-green animate-pulse shadow-[0_0_8px_#00B36E]' : (isStopped ? 'bg-red-500' : 'bg-slate-300');
                const cardBgClass = isRunning ? 'bg-white border-snap-green/30' : (isStopped ? 'bg-red-50 border-red-200' : 'bg-slate-50 border-slate-200');
                
                return `
                <div class="${cardBgClass} border p-5 rounded-2xl shadow-sm transition-all duration-300 flex flex-col justify-between">
                    <div class="flex justify-between items-center mb-4">
                        <span class="text-xs font-black text-slate-500 tracking-wide">${n.name}</span>
                        <div class="w-3 h-3 rounded-full ${dotColorClass}"></div>
                    </div>
                    <div class="text-center mb-2">
                        <h4 class="text-4xl font-black text-slate-800">${n.output.toLocaleString()}</h4>
                        <p class="text-[9px] font-bold text-slate-400 uppercase tracking-widest mt-1">Output Units</p>
                    </div>
                    <div class="text-center border-t border-slate-200/60 pt-3 mt-auto">
                        <span class="text-[10px] font-black uppercase tracking-widest ${statusColorClass}">${n.status}</span>
                    </div>
                </div>
                `;
            }).join('');
        }

        // 🛒 PRODUCT & CART SYSTEM
        function renderProducts() {
            // Render on Product Page
            const grid = document.getElementById('product-grid');
            if(grid) {
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
            
            // Render on Home Page Slider
            const slider = document.getElementById('home-product-slider');
            if(slider) {
                slider.innerHTML = products.map(p => `
                    <div onclick="navigate('product')" class="min-w-[280px] md:min-w-[320px] snap-center bg-white border border-slate-100 p-5 rounded-[2rem] shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col group cursor-pointer hover:-translate-y-1">
                        <div class="overflow-hidden rounded-2xl mb-4 relative">
                            <img src="${p.img}" class="w-full h-44 object-cover group-hover:scale-110 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-5">
                                <span class="text-white font-bold text-sm tracking-wide">VIEW SPECS <i class="fas fa-arrow-right ml-1 text-snap-green"></i></span>
                            </div>
                        </div>
                        <h4 class="font-black text-lg text-slate-800 mb-2 tracking-tight">${p.name}</h4>
                        <p class="text-snap-green font-black text-2xl tracking-tighter mt-auto">฿${p.price.toLocaleString()}</p>
                    </div>
                `).join('');
            }
        }

        // Horizontal Slider Control
        function scrollSlider(direction) {
            const slider = document.getElementById('home-product-slider');
            const scrollAmount = 340; // Card width + gap
            if (direction === 'left') {
                slider.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            } else {
                slider.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
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
            renderDashboard(); // Render dashboard texts
            if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        // INIT
        setLanguage('th');
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit ปรับความสูงเพิ่มให้ครอบคลุมส่วน Dashboard ที่เพิ่มขึ้น
st.components.v1.html(snapcon_html, height=1800, scrolling=True)
