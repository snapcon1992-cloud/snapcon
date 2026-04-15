import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS ฉบับสมบูรณ์ที่สุด
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

        .slide-1 { background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80'); animation-delay: 0s; }
        .slide-2 { background-image: url('https://images.unsplash.com/photo-1614729939124-032f0b56c9ce?auto=format&fit=crop&w=1920&q=80'); animation-delay: 5s; }
        .slide-3 { background-image: url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1920&q=80'); animation-delay: 10s; }
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
        
        .slider-container::-webkit-scrollbar { display: none; }
        .slider-container { -ms-overflow-style: none; scrollbar-width: none; scroll-behavior: smooth; }

        /* Custom Scrollbar for Dashboard Grid & Lists */
        .custom-scrollbar::-webkit-scrollbar { width: 8px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        /* ---- Animation ---- */
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
        
        .animate-speed-slide-1 { animation: speed-slide 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; opacity: 0; transform: translateX(-50px) skewX(-15deg); }
        .animate-speed-slide-2 { animation: speed-slide 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.2s forwards; opacity: 0; transform: translateX(-50px) skewX(-15deg); }
        .animate-speed-slide-3 { animation: speed-slide-up 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.4s forwards; opacity: 0; transform: translateY(30px); }
        @keyframes speed-slide { 100% { opacity: 1; transform: translateX(0) skewX(0); } }
        @keyframes speed-slide-up { 100% { opacity: 1; transform: translateY(0); } }
        
        .long-energy-line {
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 480px; 
            height: 6px;
            background: rgba(0, 179, 110, 0.2);
            border-radius: 9999px;
            box-shadow: 0 0 15px rgba(0, 179, 110, 0.6);
        }
        .long-energy-line::after {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 60%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), #00B36E, transparent);
            animation: light-beam-fast 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }
        @keyframes light-beam-fast { 0% { left: -100%; } 100% { left: 200%; } }
        .logo-glow { filter: drop-shadow(0 0 8px rgba(0, 179, 110, 0.6)); }
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
        
        <!-- Center Menus -->
        <div class="flex items-center gap-1 md:gap-2 overflow-x-auto no-scrollbar px-2 mx-2">
            <button type="button" onclick="navigate('product')" data-i18n="navProduct" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Products</button>
            <button type="button" onclick="navigate('spare')" data-i18n="navSpare" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Spare Parts</button>
            <button type="button" onclick="checkDashboardAuth()" data-i18n="navDashboard" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Dashboard</button>
            <button type="button" onclick="navigate('contact')" data-i18n="navContact" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">Contact</button>
            <button type="button" onclick="navigate('about')" data-i18n="navAbout" class="bg-white/10 text-white font-bold text-xs md:text-sm px-4 py-2 hover:bg-white/20 rounded-lg whitespace-nowrap transition-colors">About</button>
        </div>

        <!-- Right Side: Login, Lang, Cart -->
        <div class="flex items-center gap-3 shrink-0">
            <div id="login-section" class="hidden md:flex items-center gap-2">
                <span class="text-slate-400 text-xs font-bold px-1">ID:</span>
                <input type="text" id="userId" data-i18n-placeholder="phId" placeholder="ID" class="h-[26px] w-16 px-2 text-xs outline-none text-black rounded border-none focus:ring-2 ring-snap-green">
                <span class="text-slate-400 text-xs font-bold px-1">PW:</span>
                <input type="password" id="userPass" data-i18n-placeholder="phPass" placeholder="PW" class="h-[26px] w-16 px-2 text-xs outline-none text-black rounded border-none focus:ring-2 ring-snap-green">
                <div class="flex flex-col gap-0.5 ml-1">
                    <button type="button" onclick="handleLogin()" data-i18n="navLogin" class="bg-snap-green text-white font-bold text-[9px] px-3 py-0.5 hover:bg-green-600 rounded transition-colors">Login</button>
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
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay"></div>

            <div class="bg-white/90 backdrop-blur-md pl-6 md:pl-12 pr-12 md:pr-20 py-10 md:py-16 ml-0 shadow-[20px_0_40px_-10px_rgba(0,0,0,0.15)] absolute left-0 z-10 h-full flex flex-col justify-center border-r border-white/50 overflow-hidden">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] pointer-events-none"></div>
                
                <div class="relative z-10">
                    <div class="flex items-center gap-3 mb-1 animate-speed-slide-1">
                        <i class="fas fa-angle-double-right text-snap-green animate-pulse"></i>
                        <p data-i18n="heroText1" class="text-xl md:text-[28px] text-slate-600 font-black tracking-widest uppercase italic drop-shadow-sm">Snap to Connect.</p>
                    </div>
                    <div class="flex items-center gap-3 mb-4 pl-4 md:pl-8 animate-speed-slide-2">
                        <i class="fas fa-angle-double-right text-blue-500 animate-pulse"></i>
                        <p data-i18n="heroText2" class="text-xl md:text-[28px] text-slate-800 font-black tracking-widest uppercase italic drop-shadow-sm">Ready to Control.</p>
                    </div>
                    <h1 class="animate-speed-slide-3 text-6xl md:text-[85px] font-black tracking-tighter pl-8 md:pl-12 mt-2 mb-2 leading-[1.1]">
                        <span data-i18n="heroText3" class="animate-gradient-text drop-shadow-xl pb-2">Plug & Play</span>
                    </h1>
                    
                    <div class="animate-speed-slide-3 mt-6 md:mt-8 ml-8 md:ml-12 long-energy-line"></div>
                    
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

        <!-- 🎉 Home Product Slider -->
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
            
            <div id="home-product-slider" class="slider-container flex gap-6 overflow-x-auto snap-x snap-mandatory pb-8 pt-2 px-2 -mx-2">
                <!-- Products injected by JS -->
            </div>
            
            <div class="text-center mt-4">
                <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-snap-green font-bold text-sm hover:underline" data-i18n="viewAllProducts">ดูสินค้าทั้งหมด (50 Models) <i class="fas fa-arrow-right"></i></button>
            </div>
        </section>
    </div>

    <!-- ==================== PAGE: PRODUCT ==================== -->
    <div id="page-product" class="page-section max-w-7xl mx-auto px-6 py-16">
        <h2 data-i18n="pageProductTitle" class="text-4xl font-black mb-4 border-l-8 border-snap-green pl-6 text-slate-800">SNAPCON Conveyor Systems</h2>
        <p class="text-slate-500 mb-10 pl-8 font-medium" data-i18n="pageProductSub">รวมเครื่องจักรสายพานลำเลียงอัจฉริยะกว่า 50 รุ่นที่ครอบคลุมทุกอุตสาหกรรม</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 max-h-[75vh] overflow-y-auto custom-scrollbar p-2" id="product-grid"></div>
    </div>

    <!-- ==================== PAGE: SPARE PARTS ==================== -->
    <div id="page-spare" class="page-section max-w-7xl mx-auto px-6 py-16">
        <h2 data-i18n="pageSpareTitle" class="text-4xl font-black mb-4 border-l-8 border-blue-500 pl-6 text-slate-800">SNAPCON Spare Parts</h2>
        <p class="text-slate-500 mb-10 pl-8 font-medium" data-i18n="pageSpareSub">อะไหล่เครื่องจักรและชิ้นส่วนสายพานลำเลียงกว่า 200 รายการ ของแท้ 100%</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6 max-h-[75vh] overflow-y-auto custom-scrollbar p-2" id="spare-grid"></div>
    </div>

    <!-- ==================== PAGE: CART ==================== -->
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

            <div id="cart-items" class="space-y-4 mb-10 min-h-[150px] max-h-[50vh] overflow-y-auto custom-scrollbar pr-2">
                <p data-i18n="cartEmpty" class="text-center py-10 text-slate-400 font-bold text-lg">ยังไม่มีสินค้าในรถเข็น</p>
            </div>

            <div id="guest-form" class="bg-slate-50 p-8 rounded-3xl mb-10 border-2 border-dashed border-slate-200 hidden">
                <p class="font-black text-slate-700 mb-6 uppercase text-sm tracking-widest flex items-center gap-3">
                    <span class="w-8 h-8 rounded-full bg-blue-500 text-white flex items-center justify-center"><i class="fas fa-info"></i></span> 
                    <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ (Contact Info)</span>
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <input type="text" id="guest-name" data-i18n-placeholder="phGuestName" placeholder="ชื่อผู้ติดต่อ / ชื่อบริษัท" class="px-6 py-4 rounded-2xl border-none ring-1 ring-slate-200 outline-none focus:ring-2 focus:ring-snap-green transition-all shadow-sm font-bold text-slate-700">
                    <input type="text" id="guest-contact" data-i18n-placeholder="phGuestContact" placeholder="อีเมล หรือ เบอร์โทรศัพท์" class="px-6 py-4 rounded-2xl border-none ring-1 ring-slate-200 outline-none focus:ring-2 focus:ring-snap-green transition-all shadow-sm font-bold text-slate-700">
                </div>
            </div>

            <div class="flex flex-col md:flex-row justify-between items-center border-t border-slate-100 pt-10 gap-6">
                <div class="text-center md:text-left">
                    <p class="text-slate-400 text-sm font-bold uppercase tracking-widest mb-1" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                    <h3 id="cart-total" class="text-5xl font-black text-snap-green">฿0</h3>
                </div>
                <button type="button" onclick="requestQuote()" class="w-full md:w-auto bg-nav-bg text-white px-10 py-5 rounded-2xl font-black hover:bg-snap-green transition-all shadow-xl active:scale-95 text-lg" data-i18n="btnRequestQuote">
                    ยื่นขอใบเสนอราคา
                </button>
            </div>
            <p class="text-[11px] text-slate-400 mt-6 text-center font-bold bg-slate-50 py-3 rounded-xl"><i class="fas fa-shield-alt text-snap-green mr-1"></i> <span data-i18n="guestNotice">ข้อมูลจะถูกบันทึกลงระบบ Google Drive อย่างปลอดภัย</span></p>
        </div>
    </div>

    <!-- ==================== PAGE: DASHBOARD ==================== -->
    <div id="page-dashboard" class="page-section max-w-[1600px] mx-auto px-6 py-16">
        <h2 class="text-4xl font-black mb-2 border-l-8 border-snap-green pl-6 text-slate-800" data-i18n="navDashboard">Dashboard</h2>
        <p class="text-slate-500 mb-10 pl-8 font-medium" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กร - 100 โหนดพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
        
        <div class="bg-white p-6 md:p-8 rounded-[2rem] shadow-sm border border-slate-100 mb-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div>
                <h3 class="font-black text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wider text-sm" data-i18n="dashCtrlTitle"><i class="fas fa-gamepad text-blue-500"></i> การควบคุมระบบ</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                    <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-green-600 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-play mr-1 md:mr-2"></i> START</button>
                    <button onclick="stopSystem()" id="btn-stop" class="bg-slate-100 text-slate-600 py-3 md:py-4 rounded-2xl font-black shadow-sm hover:bg-red-500 hover:text-white active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-stop mr-1 md:mr-2"></i> STOP</button>
                    <button onclick="resetSystem()" class="bg-slate-800 text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-slate-700 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-sync-alt mr-1 md:mr-2"></i> REFRESH</button>
                    <button onclick="exportCSV()" class="bg-blue-500 text-white py-3 md:py-4 rounded-2xl font-black shadow-md hover:bg-blue-600 active:scale-95 transition-all text-xs lg:text-sm"><i class="fas fa-file-csv mr-1 md:mr-2"></i> REPORT</button>
                </div>
            </div>
            
            <div>
                <h3 class="font-black text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wider text-sm" data-i18n="dashCfgTitle"><i class="fas fa-sliders-h text-amber-500"></i> ตั้งค่าพารามิเตอร์</h3>
                <div class="grid grid-cols-3 gap-4">
                    <div class="bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1" data-i18n="dashTarget">เป้าหมาย (ชิ้น)</label>
                        <input type="number" id="cfg-target" value="50000" onchange="updateDashboardConfig()" class="w-full bg-transparent outline-none font-bold text-slate-800">
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

        <div class="bg-white p-8 md:p-10 rounded-[2rem] shadow-sm border border-slate-100 mb-8 relative overflow-hidden">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-6 relative z-10">
                <div>
                    <h3 class="text-2xl font-black text-slate-800 tracking-tight" data-i18n="dashPlanTitle">แผนการทำงานวันนี้ (Production Planning)</h3>
                </div>
                <div class="mt-4 sm:mt-0 text-right">
                    <span id="dash-progress-text" class="text-4xl font-black text-snap-green">0.0%</span>
                </div>
            </div>
            
            <div class="w-full h-6 bg-slate-100 rounded-full overflow-hidden border border-slate-200/50 mb-4">
                <div id="dash-progress-bar" class="h-full bg-gradient-to-r from-emerald-400 to-snap-green transition-all duration-300 relative" style="width: 0%"></div>
            </div>
            
            <div class="flex flex-col sm:flex-row justify-between gap-3">
                <div class="flex items-center gap-2 text-slate-500 text-xs font-bold uppercase bg-slate-50 px-4 py-2 rounded-xl border border-slate-100">
                    <i class="fas fa-clock text-slate-400"></i> <span data-i18n="dashTimeElapsed">เวลาที่ใช้ (Elapsed)</span>: 
                    <span id="dash-time-elapsed" class="text-slate-700 font-black ml-1">00:00:00</span>
                </div>
                <div class="flex items-center gap-2 text-amber-600 text-xs font-bold uppercase bg-amber-50 px-4 py-2 rounded-xl border border-amber-200">
                    <i class="fas fa-stopwatch text-amber-500"></i> <span data-i18n="dashTimeRemain">เวลาคงเหลือ (ETA)</span>: 
                    <span id="dash-time-remain" class="text-amber-700 font-black ml-1">--:--:--</span>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 border-l-8 border-l-blue-500">
                <p class="text-xs text-slate-400 font-bold uppercase" data-i18n="dashTotOut">ยอดผลิตรวม (Total Output)</p>
                <h3 id="dash-total-output" class="text-5xl font-black text-slate-800 mt-2">0</h3>
            </div>
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 border-l-8 border-l-emerald-500">
                <p class="text-xs text-slate-400 font-bold uppercase" data-i18n="dashCalCarbon">คาร์บอนฟุตพริ้นท์ (Cal Carbon)</p>
                <h3 id="dash-carbon" class="text-5xl font-black text-slate-800 mt-2">0.00</h3>
            </div>
            <div class="bg-white p-8 rounded-[2rem] shadow-sm border border-slate-100 border-l-8 border-l-amber-500">
                <p class="text-xs text-slate-400 font-bold uppercase" data-i18n="dashTotPower">พลังงานไฟฟ้ารวม (Power Use)</p>
                <h3 id="dash-power" class="text-5xl font-black text-slate-800 mt-2">0.00</h3>
            </div>
        </div>

        <div class="flex justify-between items-center mb-6">
            <h3 class="text-2xl font-black text-slate-800 flex items-center gap-3">
                <i class="fas fa-server text-slate-400"></i> <span data-i18n="dashMacStatus2">สถานะการทำงานและสุขภาพเครื่อง</span>
            </h3>
            <div class="hidden sm:flex gap-3 text-[10px] font-bold uppercase tracking-widest bg-white px-4 py-2 rounded-xl border border-slate-200">
                <span class="flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-snap-green"></div> <span data-i18n="statusNormal">ปกติ (>70%)</span></span>
                <span class="flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-amber-400"></div> <span data-i18n="statusWarning">เฝ้าระวัง (<70%)</span></span>
                <span class="flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-red-500"></div> <span data-i18n="statusMaint">ซ่อมบำรุง (<30%)</span></span>
            </div>
        </div>
        <div class="bg-slate-50/50 p-4 rounded-3xl border border-slate-200">
            <div id="dash-nodes-grid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 lg:grid-cols-8 xl:grid-cols-10 gap-3 max-h-[65vh] overflow-y-auto custom-scrollbar p-2">
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: CONTACT ==================== -->
    <div id="page-contact" class="page-section max-w-4xl mx-auto px-6 py-16 text-center">
        <h2 class="text-4xl font-black mb-12 text-slate-800" data-i18n="navContact">Contact Us</h2>
        <div class="bg-white p-16 rounded-[4rem] shadow-2xl border border-slate-100 relative overflow-hidden">
            <div class="absolute -top-20 -right-20 w-64 h-64 bg-snap-green/10 blur-[80px] rounded-full"></div>
            <div class="w-24 h-24 bg-snap-green/10 text-snap-green rounded-[2rem] flex items-center justify-center text-4xl mx-auto mb-8 relative z-10 shadow-inner border border-snap-green/20">
                <i class="fas fa-envelope-open-text"></i>
            </div>
            <p class="text-3xl font-black text-slate-800 mb-4 relative z-10">snapcon1992@gmail.com</p>
            <p class="text-slate-500 font-medium mb-12 relative z-10 text-lg" data-i18n="contactSub">ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ</p>
            <button onclick="window.location.href='mailto:snapcon1992@gmail.com'" class="relative z-10 bg-snap-green text-white px-14 py-5 rounded-2xl font-black text-lg hover:bg-green-600 transition-all shadow-[0_15px_30px_rgba(0,179,110,0.3)] active:scale-95 tracking-wide" data-i18n="btnEmail">ส่งอีเมลติดต่อเรา</button>
        </div>
    </div>

    <!-- ==================== PAGE: ABOUT US ==================== -->
    <div id="page-about" class="page-section max-w-5xl mx-auto px-6 py-16">
        <h2 class="text-4xl font-black mb-10 border-l-8 border-snap-green pl-6 text-slate-800" data-i18n="navAbout">เกี่ยวกับเรา</h2>
        <div class="bg-white p-12 md:p-16 rounded-[4rem] shadow-xl border border-slate-100 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-64 h-64 bg-snap-green/5 blur-[80px] rounded-full -mr-20 -mt-20"></div>
            
            <p class="text-3xl font-black text-slate-900 mb-6 leading-tight">
                SNAPCON AUTOMATION
            </p>
            <p class="text-lg text-slate-600 leading-relaxed mb-12 font-medium" data-i18n="aboutDesc">
                Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด เพื่อเตรียมความพร้อมอุตสาหกรรมสู่อนาคต
            </p>

            <div class="grid md:grid-cols-2 gap-8">
                <!-- Vision Card -->
                <div class="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:border-snap-green transition-colors group">
                    <div class="w-14 h-14 bg-snap-green/10 text-snap-green rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h3 class="text-2xl font-black text-slate-800 mb-4" data-i18n="aboutVisionTitle">วิสัยทัศน์ (Vision)</h3>
                    <p class="text-slate-500 font-medium leading-relaxed" data-i18n="aboutVisionDesc">มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้</p>
                </div>
                <!-- Mission Card -->
                <div class="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:border-blue-500 transition-colors group">
                    <div class="w-14 h-14 bg-blue-500/10 text-blue-500 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-bullseye"></i>
                    </div>
                    <h3 class="text-2xl font-black text-slate-800 mb-4" data-i18n="aboutMissionTitle">พันธกิจ (Mission)</h3>
                    <p class="text-slate-500 font-medium leading-relaxed" data-i18n="aboutMissionDesc">พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก</p>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== MODAL: REGISTER ==================== -->
    <div id="modal-register" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md rounded-[2rem] shadow-2xl relative overflow-hidden flex flex-col max-h-[90vh]">
            <button onclick="closeRegisterModal()" class="absolute top-6 right-6 text-slate-400 hover:text-red-500 transition-colors z-10"><i class="fas fa-times text-xl"></i></button>
            <div class="p-8 pb-6 border-b border-slate-100 shrink-0">
                <h3 class="text-2xl font-black text-slate-800" data-i18n="regTitle">สร้างบัญชีผู้ใช้</h3>
            </div>
            <div class="p-8 space-y-5 overflow-y-auto no-scrollbar flex-1">
                <div><label class="block text-[10px] font-black text-slate-400 uppercase mb-2" data-i18n="regId">User ID</label><input type="text" id="reg-id" data-i18n-placeholder="phRegId" class="w-full px-5 py-3 rounded-xl bg-slate-50 border outline-none focus:ring-2 focus:border-snap-green"></div>
                <div><label class="block text-[10px] font-black text-slate-400 uppercase mb-2" data-i18n="regPass">Password</label><input type="password" id="reg-pass" data-i18n-placeholder="phRegPass" class="w-full px-5 py-3 rounded-xl bg-slate-50 border outline-none focus:ring-2 focus:border-snap-green"></div>
                <div><label class="block text-[10px] font-black text-slate-400 uppercase mb-2" data-i18n="regName">Name / Company</label><input type="text" id="reg-name" data-i18n-placeholder="phRegName" class="w-full px-5 py-3 rounded-xl bg-slate-50 border outline-none focus:ring-2 focus:border-snap-green"></div>
                <div><label class="block text-[10px] font-black text-slate-400 uppercase mb-2" data-i18n="regContact">Email / Phone</label><input type="text" id="reg-contact" data-i18n-placeholder="phRegContact" class="w-full px-5 py-3 rounded-xl bg-slate-50 border outline-none focus:ring-2 focus:border-snap-green"></div>
            </div>
            <div class="p-8 pt-6 border-t bg-slate-50 shrink-0">
                <button type="button" onclick="submitRegistration()" class="w-full bg-snap-green text-white py-4 rounded-xl font-black hover:bg-green-600" data-i18n="btnSubmitReg">ยืนยันลงทะเบียน</button>
            </div>
        </div>
    </div>

    <script>
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzTXYEcWYEsbcwL0ipt5vl1azB-C8psZUuwpjfIirzCdH2mBE2OHNdKSMoNPhklRt2M/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let memoryUsers = { '001': '123' };

        let dashState = {
            isRunning: false, target: 50000, carbonFactor: 0.0072, energyFactor: 0.015,
            intervalId: null, elapsedSeconds: 0,
            nodes: Array.from({length: 100}, (_, i) => ({
                id: i + 1, name: `Node ${String(i+1).padStart(3, '0')}`, output: 0, status: 'Offline',
                health: 100.0, wearRate: 0.2 + (Math.random() * 0.6)
            }))
        };

        let products = [];
        let spares = [];
        
        const baseImgs = ['https://i.ibb.co/bZ7TKQg/01.png', 'https://i.ibb.co/tTCb2j0h/02.png', 'https://i.ibb.co/PGNt8dfj/03.png', 'https://i.ibb.co/mVfD9H0B/04.png', 'https://i.ibb.co/x4SGKtb/05.png'];
        const cTypes = ['Mini', 'Standard', 'Heavy Duty', 'High Speed', 'Food Grade', 'Incline', 'Modular', 'Roller System', 'Eco Line', 'Flex Track'];
        
        for(let i=1; i<=50; i++) {
            let t = cTypes[i % cTypes.length];
            products.push({
                id: 'M' + String(i).padStart(2, '0'), name: `Snapcon Model ${String(i).padStart(2, '0')} (${t})`, price: 15000 + (i * 800),
                img: i <= 5 ? baseImgs[i-1] : `https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=400&q=80&sig=${i}`,
                specs: { th: [`L: ${1+(i%15)}m`, `W: ${300+(i*10)}mm`, `Load: ${50+(i*10)}kg`, `Speed: ${15+(i%5)}m/min`], en: [`L: ${1+(i%15)}m`, `W: ${300+(i*10)}mm`, `Load: ${50+(i*10)}kg`, `Speed: ${15+(i%5)}m/min`] }
            });
        }

        const sTypes = ['Roller Series', 'Conveyor Belt PU', 'Drive Motor AC', 'Sensor Switch', 'Control Board', 'Bearing Unit', 'Bracket Set', 'Emergency Stop', 'Power Supply 24V', 'Inverter VFD'];
        for(let i=1; i<=200; i++) {
            let t = sTypes[i % sTypes.length];
            spares.push({
                id: 'SP' + String(i).padStart(3, '0'), name: `${t} - P${String(i).padStart(3, '0')}`, price: 500 + (i * 25),
                img: `https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80&sig=${i+100}`,
                specs: { th: [`Type: ${t}`, "Status: Ready"], en: [`Type: ${t}`, "Status: Ready"] }
            });
        }
        
        const allItems = [...products, ...spares];

        // 🌐 DICTIONARY: ระบบภาษาที่สมบูรณ์ 100%
        const dict = {
            th: {
                navProduct: "Products (50)", navSpare: "Spares (200)", navDashboard: "Dashboard (100)", navContact: "Contact", navAbout: "About Us",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroText3: "Plug & Play",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "SNAPCON Conveyor Systems", pageProductSub: "รวมเครื่องจักรสายพานลำเลียงอัจฉริยะกว่า 50 รุ่นที่ครอบคลุมทุกอุตสาหกรรม",
                pageSpareTitle: "SNAPCON Spare Parts", pageSpareSub: "อะไหล่เครื่องจักรและชิ้นส่วนสายพานลำเลียงกว่า 200 รายการ ของแท้ 100%",
                btnAddToCart: "หยิบใส่รถเข็น",
                pageCartTitle: "รถเข็นขอใบเสนอราคา", cartEmpty: "ยังไม่มีสินค้าในรถเข็น", cartTotalLabel: "ราคากลางประเมินรวม:",
                btnRequestQuote: "ยื่นขอใบเสนอราคา", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก", specTitle: "สเปค:",
                alertLoginSuccess: "เข้าสู่ระบบสำเร็จ!", alertAddCart: "เพิ่มลงรถเข็นแล้ว!",
                alertQuoteReq: "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อกลับ",
                
                // Contact & About
                contactSub: "ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ", btnEmail: "ส่งอีเมลติดต่อเรา",
                aboutDesc: "Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด เพื่อเตรียมความพร้อมอุตสาหกรรมสู่อนาคต",
                aboutVisionTitle: "วิสัยทัศน์ (Vision)", aboutVisionDesc: "มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้",
                aboutMissionTitle: "พันธกิจ (Mission)", aboutMissionDesc: "พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก",

                regTitle: "สร้างบัญชีผู้ใช้", regDesc: "ลงทะเบียนเพื่อเข้าถึงระบบและขอใบเสนอราคา", btnSubmitReg: "ยืนยันการลงทะเบียน",
                regId: "รหัสผู้ใช้ (User ID)", regPass: "รหัสผ่าน (Password)", regName: "ชื่อ-นามสกุล / ชื่อบริษัท", regContact: "อีเมล / เบอร์โทรศัพท์",
                
                homeProductsTitle: "สินค้าของเรา", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด", viewAllProducts: "ดูสินค้าทั้งหมด (50 Models)",
                
                // Dashboard
                dashSubTitle: "ระบบตรวจสอบระดับองค์กร - 100 โหนดพร้อมระบบซ่อมบำรุงเชิงคาดการณ์",
                dashCtrlTitle: "การควบคุมระบบ", dashCfgTitle: "ตั้งค่าพารามิเตอร์", dashTarget: "เป้าหมาย (ชิ้น)", dashCarbon: "ค่าคาร์บอน", dashEnergy: "ค่าพลังงาน",
                dashPlanTitle: "แผนการทำงานวันนี้ (Production Planning)", dashTotOut: "ยอดผลิตรวม", dashCalCarbon: "คาร์บอน (Cal Carbon)", dashTotPower: "พลังงานรวม (Power)",
                dashTimeElapsed: "เวลาที่ใช้ (Elapsed)", dashTimeRemain: "เวลาคงเหลือ (ETA)", dashMacStatus2: "สถานะการทำงานและสุขภาพเครื่อง",
                statusNormal: "ปกติ (>70%)", statusWarning: "เฝ้าระวัง (<70%)", statusMaint: "ซ่อมบำรุง (<30%)",
                
                // Cart Guests
                guestContactTitle: "ข้อมูลติดต่อกลับ (Contact Info)", guestNotice: "ข้อมูลจะถูกบันทึกลงระบบ Google Drive อย่างปลอดภัย",
                
                // Placeholders
                phId: "ID", phPass: "PW",
                phGuestName: "ชื่อผู้ติดต่อ / ชื่อบริษัท", phGuestContact: "อีเมล หรือ เบอร์โทรศัพท์",
                phRegId: "ตั้งรหัส ID สำหรับเข้าระบบ", phRegPass: "ตั้งรหัสผ่านของคุณ", phRegName: "ระบุชื่อสำหรับติดต่อ", phRegContact: "ระบุช่องทางติดต่อกลับ"
            },
            en: {
                navProduct: "Products (50)", navSpare: "Spares (200)", navDashboard: "Dashboard (100)", navContact: "Contact", navAbout: "About Us",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroText3: "Plug & Play",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "SNAPCON Conveyor Systems", pageProductSub: "Explore over 50 intelligent conveyor models covering all industries.",
                pageSpareTitle: "SNAPCON Spare Parts", pageSpareSub: "Over 200 genuine spare parts and conveyor components. 100% Authentic.",
                btnAddToCart: "Add to Cart",
                pageCartTitle: "Quotation Cart", cartEmpty: "Your cart is empty", cartTotalLabel: "Estimated Total:",
                btnRequestQuote: "Submit Quotation Request", selectAll: "Select All", deleteSelected: "Delete Selected", specTitle: "Specs:",
                alertLoginSuccess: "Login Successful!", alertAddCart: "Added to cart!",
                alertQuoteReq: "Please select at least 1 item", alertQuoteGuestReq: "Please provide contact info.",
                
                // Contact & About
                contactSub: "Official Technical Support & Inquiries", btnEmail: "SEND DIRECT EMAIL",
                aboutDesc: "Snapcon Automation is a leader in modern industrial technology, focusing on ease of connection and installation through Plug & Play Systems. We are committed to revolutionizing the automation industry with solutions that reduce complexity, minimize installation time, and maximize production efficiency.",
                aboutVisionTitle: "Our Vision", aboutVisionDesc: "To be the leading provider of the most accessible and advanced Plug & Play automation systems in Southeast Asia.",
                aboutMissionTitle: "Our Mission", aboutMissionDesc: "Develop innovations that reduce complexity, minimize installation time, and elevate the operational efficiency of industries of all sizes to compete globally.",

                regTitle: "Create Account", regDesc: "Register to access the system and request quotes", btnSubmitReg: "Confirm Registration",
                regId: "User ID", regPass: "Password", regName: "Full Name / Company", regContact: "Email / Phone",
                
                homeProductsTitle: "Our Products", homeProductsSub: "Explore our latest automation machines and equipment", viewAllProducts: "View All Products (50 Models)",
                
                // Dashboard
                dashSubTitle: "Enterprise Monitoring System - 100 Active Nodes with Predictive Maintenance",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target (Units)", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon Footprint", dashTotPower: "Total Power Use",
                dashTimeElapsed: "Elapsed Time", dashTimeRemain: "Est. Remaining (ETA)", dashMacStatus2: "Machine Status & Health",
                statusNormal: "Optimal (>70%)", statusWarning: "Warning (<70%)", statusMaint: "Maintenance (<30%)",
                
                // Cart Guests
                guestContactTitle: "Contact Info", guestNotice: "Information will be securely saved to Google Drive",
                
                // Placeholders
                phId: "ID", phPass: "PW",
                phGuestName: "Contact Name / Company", phGuestContact: "Email or Phone Number",
                phRegId: "Create your User ID", phRegPass: "Create your Password", phRegName: "Enter your full name", phRegContact: "Enter email or phone"
            }
        };

        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            const target = document.getElementById('page-' + pageId);
            if(target) target.classList.add('page-active');
            if(pageId === 'cart') renderCart();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function checkDashboardAuth() {
            if (isLoggedIn) navigate('dashboard');
            else { alert(currentLang === 'th' ? "กรุณา Login ก่อน" : "Please Login first"); document.getElementById('userId').focus(); }
        }

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
                document.getElementById('userId').value = ''; document.getElementById('userPass').value = '';
            } else alert(currentLang === 'th' ? "ID/Pass ไม่ถูกต้อง" : "Invalid ID/Pass");
        }

        function openRegisterModal() { document.getElementById('modal-register').classList.replace('hidden', 'flex'); }
        function closeRegisterModal() { document.getElementById('modal-register').classList.replace('flex', 'hidden'); }

        function submitRegistration() {
            const id = document.getElementById('reg-id').value;
            const pass = document.getElementById('reg-pass').value;
            const name = document.getElementById('reg-name').value;
            const contact = document.getElementById('reg-contact').value;
            if(!id || !pass || !name || !contact) return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบ" : "Please fill all fields");
            if(memoryUsers[id]) return alert(currentLang === 'th' ? "ID นี้มีผู้ใช้งานแล้ว" : "ID already exists");
            
            memoryUsers[id] = pass;
            try { fetch(GOOGLE_SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: JSON.stringify({ type: "Registration", name_or_id: id, email: contact, details: name }) }); } catch(e) {}
            
            alert(currentLang === 'th' ? "ลงทะเบียนสำเร็จ!" : "Registered successfully!");
            document.getElementById('userId').value = id; document.getElementById('userPass').value = pass;
            closeRegisterModal();
        }

        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden'); document.getElementById('login-section').classList.add('md:flex');
            document.getElementById('user-section').classList.add('hidden'); document.getElementById('user-section').classList.remove('flex');
            stopSystem(); navigate('home');
        }

        // ================= DASHBOARD CORE LOGIC =================
        function startSystem() {
            dashState.isRunning = true;
            dashState.nodes.forEach(n => { if(n.health > 30) n.status = 'Running'; else n.status = 'Maintenance'; });
            if(!dashState.intervalId) dashState.intervalId = setInterval(simulateProduction, 500);
            renderDashboard();
        }
        function stopSystem() {
            dashState.isRunning = false;
            dashState.nodes.forEach(n => { if(n.status !== 'Maintenance') n.status = 'Stopped'; });
            if(dashState.intervalId) { clearInterval(dashState.intervalId); dashState.intervalId = null; }
            renderDashboard();
        }
        function resetSystem() { 
            dashState.nodes.forEach(n => { n.output = 0; n.health = 100.0; n.status = dashState.isRunning ? 'Running' : 'Offline'; }); 
            dashState.elapsedSeconds = 0; renderDashboard(); 
        }
        function updateDashboardConfig() {
            dashState.target = parseInt(document.getElementById('cfg-target').value) || 1;
            dashState.carbonFactor = parseFloat(document.getElementById('cfg-carbon').value) || 0;
            dashState.energyFactor = parseFloat(document.getElementById('cfg-energy').value) || 0;
            renderDashboard();
        }
        function simulateProduction() {
            if(!dashState.isRunning) return;
            dashState.elapsedSeconds += 0.5;
            dashState.nodes.forEach(n => { 
                if(n.status === 'Running' || n.status === 'Warning') {
                    if(Math.random() > 0.5) { n.output += 1; n.health -= n.wearRate; if(n.health < 0) n.health = 0; }
                    if(n.health <= 30) n.status = 'Maintenance'; else if (n.health <= 70) n.status = 'Warning';
                }
            });
            renderDashboard();
        }
        function exportCSV() {
            let bom = "\\uFEFF";
            let csvContent = bom + "Node ID,Machine Name,Status,Output (Units),Health (%),Est. Carbon (kgCO2e),Est. Power (kWh)\\n";
            let totalOut = 0;
            dashState.nodes.forEach(n => {
                let c = (n.output * dashState.carbonFactor).toFixed(4); let e = (n.output * dashState.energyFactor).toFixed(4); totalOut += n.output;
                csvContent += `${n.id},${n.name},${n.status},${n.output},${n.health.toFixed(2)},${c},${e}\\n`;
            });
            csvContent += `\\nTOTAL,, ,${totalOut},-,${(totalOut * dashState.carbonFactor).toFixed(4)},${(totalOut * dashState.energyFactor).toFixed(4)}\\n`;
            
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement("a"); link.href = URL.createObjectURL(blob); link.download = `Snapcon_100Nodes_Report.csv`; link.click();
        }
        function formatTimeStr(totalSecs) {
            if (!isFinite(totalSecs) || totalSecs < 0) return "--:--:--";
            const h = Math.floor(totalSecs / 3600); const m = Math.floor((totalSecs % 3600) / 60); const s = Math.floor(totalSecs % 60);
            return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        }
        function renderDashboard() {
            const grid = document.getElementById('dash-nodes-grid'); if(!grid) return;
            const totalOutput = dashState.nodes.reduce((sum, n) => sum + n.output, 0);
            document.getElementById('dash-total-output').innerText = totalOutput.toLocaleString();
            document.getElementById('dash-carbon').innerText = (totalOutput * dashState.carbonFactor).toFixed(2);
            document.getElementById('dash-power').innerText = (totalOutput * dashState.energyFactor).toFixed(2);
            
            let progress = (totalOutput / dashState.target) * 100; if(progress > 100) progress = 100;
            document.getElementById('dash-progress-bar').style.width = `${progress}%`;
            document.getElementById('dash-progress-text').innerText = `${progress.toFixed(1)}%`;
            
            let elapsedStr = formatTimeStr(dashState.elapsedSeconds), remainStr = "--:--:--";
            if (totalOutput > 0 && dashState.elapsedSeconds > 0) {
                let ups = totalOutput / dashState.elapsedSeconds, remainUnits = dashState.target - totalOutput;
                if (remainUnits > 0 && ups > 0) remainStr = formatTimeStr(remainUnits / ups); else if (remainUnits <= 0) remainStr = "00:00:00";
            }
            document.getElementById('dash-time-elapsed').innerText = elapsedStr;
            document.getElementById('dash-time-remain').innerText = remainStr + (dashState.target <= totalOutput && totalOutput > 0 ? " (Completed)" : "");

            grid.innerHTML = dashState.nodes.map(n => {
                const isRun = n.status === 'Running', isWarn = n.status === 'Warning', isMaint = n.status === 'Maintenance';
                let dotBg = 'bg-slate-300', borderCol = 'border-slate-200', alertOverlay = '';
                if (isRun) { dotBg = 'bg-snap-green animate-pulse'; borderCol = 'hover:border-snap-green'; }
                else if (isWarn) { dotBg = 'bg-amber-400 animate-pulse'; borderCol = 'border-amber-300'; alertOverlay = '<div class="absolute inset-0 bg-amber-400/5 z-0 pointer-events-none"></div>'; }
                else if (isMaint) { dotBg = 'bg-red-500'; borderCol = 'border-red-300'; alertOverlay = '<div class="absolute inset-0 bg-red-500/10 z-0 pointer-events-none"></div>'; }
                let healthBarCol = n.health > 70 ? 'bg-snap-green' : (n.health > 30 ? 'bg-amber-400' : 'bg-red-500');

                let statusLoc = isRun ? dict[currentLang].statusNormal : (isWarn ? dict[currentLang].statusWarning : (isMaint ? dict[currentLang].statusMaint : n.status));
                
                return `
                <div class="bg-white border ${borderCol} p-3 rounded-xl shadow-sm flex flex-col justify-between transition-all relative overflow-hidden">
                    ${alertOverlay}
                    <div class="flex justify-between items-center mb-2 relative z-10">
                        <span class="text-[10px] font-black text-slate-500">${n.name}</span>
                        <div class="w-2 h-2 rounded-full ${dotBg}" title="${statusLoc}"></div>
                    </div>
                    <h4 class="text-xl font-black text-slate-800 text-center relative z-10">${n.output.toLocaleString()}</h4>
                    <div class="mt-3 relative z-10">
                        <div class="flex justify-between items-end mb-1">
                            <span class="text-[8px] font-bold uppercase tracking-wider ${isMaint ? 'text-red-500' : 'text-slate-400'}">Health</span>
                            <span class="text-[9px] font-black ${isMaint ? 'text-red-500' : 'text-slate-600'}">${n.health.toFixed(0)}%</span>
                        </div>
                        <div class="w-full h-1.5 bg-slate-100 rounded-full overflow-hidden"><div class="h-full ${healthBarCol} transition-all duration-300" style="width: ${n.health}%"></div></div>
                    </div>
                </div>`;
            }).join('');
        }

        // 🛒 PRODUCT & CART SYSTEM
        function createItemCard(p) {
            return `
                <div class="bg-white border border-slate-100 p-5 rounded-[1.5rem] shadow-sm hover:shadow-lg transition-all flex flex-col h-full group hover:-translate-y-1">
                    <div class="overflow-hidden rounded-xl mb-4 h-32 relative bg-slate-50">
                        <img src="${p.img}" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500 mix-blend-multiply">
                    </div>
                    <h4 class="font-black text-sm text-slate-800 mb-3 tracking-tight truncate" title="${p.name}">${p.name}</h4>
                    <div class="bg-slate-50 p-3 rounded-xl mb-4 flex-grow border border-slate-100/50">
                        <ul class="text-[10px] text-slate-500 space-y-1 font-medium">
                            ${p.specs[currentLang].map(s => `<li class="truncate">• ${s}</li>`).join('')}
                        </ul>
                    </div>
                    <p class="text-snap-green font-black text-xl mb-3">฿${p.price.toLocaleString()}</p>
                    <button type="button" onclick="addToCart('${p.id}')" class="w-full bg-nav-bg text-white py-2.5 rounded-xl font-black text-xs hover:bg-snap-green transition-all active:scale-95">${dict[currentLang].btnAddToCart}</button>
                </div>
            `;
        }

        function renderProducts() {
            const pGrid = document.getElementById('product-grid'); if(pGrid) pGrid.innerHTML = products.map(p => createItemCard(p)).join('');
            const sGrid = document.getElementById('spare-grid'); if(sGrid) sGrid.innerHTML = spares.map(p => createItemCard(p)).join('');
            const slider = document.getElementById('home-product-slider');
            if(slider) {
                slider.innerHTML = products.slice(0, 10).map(p => `
                    <div onclick="navigate('product')" class="min-w-[250px] snap-center bg-white border border-slate-100 p-4 rounded-[1.5rem] shadow-sm hover:shadow-lg transition-all cursor-pointer">
                        <div class="overflow-hidden rounded-xl mb-3 relative h-32 bg-slate-50">
                            <img src="${p.img}" class="w-full h-full object-cover group-hover:scale-110 transition-transform mix-blend-multiply">
                        </div>
                        <h4 class="font-black text-sm text-slate-800 mb-1 truncate">${p.name}</h4>
                        <p class="text-snap-green font-black text-lg mt-auto">฿${p.price.toLocaleString()}</p>
                    </div>
                `).join('');
            }
        }

        function scrollSlider(dir) {
            const slider = document.getElementById('home-product-slider');
            slider.scrollBy({ left: dir === 'left' ? -300 : 300, behavior: 'smooth' });
        }

        function addToCart(id) {
            const p = allItems.find(i => i.id === id);
            cart.push({ ...p, cartId: Date.now() + Math.random(), selected: true });
            const b = document.getElementById('cart-badge'); b.innerText = cart.length; b.classList.remove('hidden');
            b.classList.add('animate-bounce'); setTimeout(() => b.classList.remove('animate-bounce'), 1000);
            alert(dict[currentLang].alertAddCart);
        }

        function renderCart() {
            const container = document.getElementById('cart-items'); const guestForm = document.getElementById('guest-form');
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
            document.getElementById('cart-select-all').checked = cart.length > 0 && cart.every(i => i.selected);
        }

        function toggleItem(cartId) { const item = cart.find(i => i.cartId === cartId); if(item) item.selected = !item.selected; renderCart(); }
        function toggleSelectAll(val) { cart.forEach(i => i.selected = val); renderCart(); }
        function deleteSelected() { cart = cart.filter(i => !i.selected); document.getElementById('cart-badge').innerText = cart.length; if(cart.length === 0) document.getElementById('cart-badge').classList.add('hidden'); renderCart(); }

        function requestQuote() {
            const selected = cart.filter(i => i.selected);
            if(selected.length === 0) return alert(dict[currentLang].alertQuoteReq);
            let name = isLoggedIn ? document.getElementById('displayUser').innerText : document.getElementById('guest-name').value;
            let info = isLoggedIn ? "Registered Account" : document.getElementById('guest-contact').value;
            if(!isLoggedIn && (!name || !info)) return alert(dict[currentLang].alertQuoteGuestReq);
            
            let detailsForEmail = selected.map(i => `- ${i.name} (%E0%B8%BF${i.price.toLocaleString()})`).join('%0A');
            let detailsForDB = selected.map(i => `- ${i.name} (฿${i.price.toLocaleString()})`).join('\\n');
            let total = selected.reduce((s, i) => s + i.price, 0);
            
            try { fetch(GOOGLE_SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: JSON.stringify({ type: "Quotation", name_or_id: name, email: info, details: `Items:\\n${detailsForDB}\\n\\nTotal: ฿${total.toLocaleString()}` }) }); } catch(e) {}
            
            const subject = encodeURIComponent("Quotation Request - Snapcon (" + name + ")");
            const body = "Request for Official Quotation:%0A%0AItems:%0A" + detailsForEmail + "%0A%0AEstimated Total: %E0%B8%BF" + total.toLocaleString() + "%0A%0AContact Info: " + encodeURIComponent(info);
            window.location.href = `mailto:snapcon1992@gmail.com?subject=${subject}&body=${body}`;
            
            cart = cart.filter(i => !i.selected); document.getElementById('cart-badge').innerText = cart.length; if(cart.length === 0) document.getElementById('cart-badge').classList.add('hidden'); renderCart(); navigate('home');
        }

        // 🌐 LANGUAGE SYSTEM
        function setLanguage(lang) {
            currentLang = lang;
            // Update Texts
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[lang][key]) el.innerHTML = dict[lang][key];
            });
            // Update Placeholders
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (dict[lang][key]) el.placeholder = dict[lang][key];
            });
            // Update Lang Buttons Style
            document.getElementById('btn-lang-th').className = lang === 'th' ? "text-[9px] font-bold px-2.5 py-1 rounded-full bg-snap-green text-white transition-colors" : "text-[9px] font-bold px-2.5 py-1 rounded-full text-slate-400 hover:text-white transition-colors";
            document.getElementById('btn-lang-en').className = lang === 'en' ? "text-[9px] font-bold px-2.5 py-1 rounded-full bg-snap-green text-white transition-colors" : "text-[9px] font-bold px-2.5 py-1 rounded-full text-slate-400 hover:text-white transition-colors";
            
            renderProducts();
            renderDashboard(); // Update dashboard localization
            if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        // INIT
        setLanguage('th');
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2100, scrolling=True)
