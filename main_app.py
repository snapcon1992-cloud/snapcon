import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS ฉบับสมบูรณ์ที่ปรับหน้าแรก (Animated Text Slider & Dark Dropdown Bar)
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Automation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=Prompt:wght@400;700;900&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'snap-dark': '#1e2329',
                        'snap-black': '#0f172a',
                        'snap-green': '#00B36E',
                        'snap-green-hover': '#00965c',
                        'snap-gray': '#f1f5f9',
                    },
                    fontFamily: {
                        sans: ['Inter', 'Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { margin: 0; padding: 0; background-color: #e2e8f0; overflow-x: hidden; }
        
        /* สไตล์ใหม่สำหรับ Hero Section แบบ Green Technology */
        .hero-container {
            background-image: linear-gradient(rgba(2, 44, 34, 0.7), rgba(2, 44, 34, 0.9)), url('https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
        }

        .hero-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, #ffffff 40%, rgba(16, 185, 129, 0.85) 75%, rgba(2, 44, 34, 0.6) 100%);
            z-index: 5;
            pointer-events: none;
        }

        .hero-white-box {
            background-color: white;
            border-bottom: 6px solid #00B36E;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }

        .feature-bar {
            background-color: #1e293b;
            color: white;
        }

        /* ---- Image Slider Background Animations (Green Tech Theme) ---- */
        .slide-img {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover;
            background-position: center;
            opacity: 0;
            animation: slideBgAnimation 20s infinite linear;
        }

        /* ภาพที่ 1: พลังงานแสงอาทิตย์ (Solar Energy) */
        .slide-1 { background-image: url('https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=1920&q=80'); animation-delay: 0s; }
        /* ภาพที่ 2: พลังงานลม (Wind Energy / Eco Industry) */
        .slide-2 { background-image: url('https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=1920&q=80'); animation-delay: 5s; }
        /* ภาพที่ 3: นวัตกรรมสีเขียว (Plant in lightbulb / Eco concept) */
        .slide-3 { background-image: url('https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?auto=format&fit=crop&w=1920&q=80'); animation-delay: 10s; }
        /* ภาพที่ 4: สถาปัตยกรรมสีเขียว (Eco-friendly modern factory/building) */
        .slide-4 { background-image: url('https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=1920&q=80'); animation-delay: 15s; }

        @keyframes slideBgAnimation {
            0% { opacity: 0; transform: scale(1.1) translateX(30px); }
            5% { opacity: 1; transform: scale(1.1) translateX(20px); }
            20% { opacity: 1; transform: scale(1.1) translateX(-10px); }
            25% { opacity: 0; transform: scale(1.1) translateX(-20px); }
            100% { opacity: 0; }
        }

        /* Nav & Menus */
        .nav-link {
            position: relative;
            color: white;
            font-weight: 700;
            font-size: 0.85rem;
            transition: color 0.3s;
        }
        .nav-link:hover { color: #00B36E; }
        .nav-link::after {
            content: ''; position: absolute; width: 0; height: 2px;
            bottom: -4px; left: 0; background-color: #00B36E;
            transition: width 0.3s;
        }
        .nav-link:hover::after { width: 100%; }

        /* Pages */
        .page-section { display: none !important; }
        .page-active { display: block !important; animation: fadeIn 0.4s ease-out forwards; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        /* Dropdown */
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
        
        /* Scrollbars */
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        /* Cards */
        .sharp-card {
            border-radius: 4px;
            border: 1px solid #e2e8f0;
            transition: all 0.3s;
        }
        .sharp-card:hover {
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #00B36E;
            transform: translateY(-4px);
        }
        
        .sharp-btn {
            border-radius: 2px;
            transition: all 0.2s;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .sharp-btn:active { transform: scale(0.98); }

        /* ---- Animated Text Slider (Hero Right Side) ---- */
        .feature-text-container {
            position: relative;
            height: 140px; 
            width: 100%;
            display: flex;
            align-items: center;
        }
        .feature-text-slide {
            position: absolute;
            width: 100%;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeSlideText 15s infinite;
        }
        .feature-text-slide:nth-child(1) { animation-delay: 0s; }
        .feature-text-slide:nth-child(2) { animation-delay: 3s; }
        .feature-text-slide:nth-child(3) { animation-delay: 6s; }
        .feature-text-slide:nth-child(4) { animation-delay: 9s; }
        .feature-text-slide:nth-child(5) { animation-delay: 12s; }

        @keyframes fadeSlideText {
            0% { opacity: 0; transform: translateY(30px); }
            5% { opacity: 1; transform: translateY(0); }
            15% { opacity: 1; transform: translateY(0); }
            20% { opacity: 0; transform: translateY(-30px); }
            100% { opacity: 0; }
        }
        
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
<body class="font-sans text-slate-800">

    <!-- 1. Top Navigation Bar (Dark Theme) -->
    <nav class="bg-snap-black h-[70px] w-full fixed top-0 z-50 flex items-center justify-between px-6 md:px-10 shadow-md">
        <!-- Logo -->
        <div class="flex items-center gap-2 cursor-pointer shrink-0" onclick="navigate('home')">
            <span class="font-black text-3xl text-snap-green tracking-tighter">SNAPCON</span>
        </div>
        
        <!-- Center Menus -->
        <div class="hidden md:flex items-center gap-8 ml-8">
            <button type="button" onclick="navigate('product')" data-i18n="navProduct" class="nav-link">Products</button>
            <button type="button" onclick="navigate('spare')" data-i18n="navSpare" class="nav-link">Spare Parts</button>
            <button type="button" onclick="checkDashboardAuth()" data-i18n="navDashboard" class="nav-link">Dashboard</button>
            <button type="button" onclick="navigate('about')" data-i18n="navAbout" class="nav-link">Company</button>
            <button type="button" onclick="navigate('contact')" data-i18n="navContact" class="nav-link">Support</button>
        </div>

        <!-- Right Side: Login, Lang, Cart -->
        <div class="flex items-center gap-5 shrink-0 ml-auto">
            <!-- Login Form (Desktop) -->
            <div id="login-section" class="hidden lg:flex items-center gap-2">
                <input type="text" id="userId" placeholder="ID" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <input type="password" id="userPass" placeholder="PW" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <button type="button" onclick="handleLogin()" class="h-8 px-3 bg-snap-green text-white font-bold text-xs hover:bg-snap-green-hover sharp-btn"><i class="fas fa-sign-in-alt"></i></button>
                <button type="button" onclick="openRegisterModal()" class="h-8 px-3 bg-slate-700 text-white font-bold text-xs hover:bg-slate-600 sharp-btn"><i class="fas fa-user-plus"></i></button>
            </div>
            
            <!-- User Status -->
            <div id="user-section" class="hidden items-center gap-3">
                <span class="text-white text-sm"><i class="far fa-user-circle text-snap-green mr-1"></i> <span id="displayUser" class="font-bold">User</span></span>
                <button type="button" onclick="handleLogout()" class="text-slate-400 hover:text-white text-xs underline"><i class="fas fa-sign-out-alt"></i></button>
            </div>

            <!-- Icons -->
            <div class="flex items-center gap-4 text-white text-lg border-l border-slate-700 pl-5">
                <button type="button" id="btn-lang-th" onclick="setLanguage('th')" class="text-xs font-bold text-snap-green hover:text-white">TH</button>
                <span class="text-slate-600 text-xs">|</span>
                <button type="button" id="btn-lang-en" onclick="setLanguage('en')" class="text-xs font-bold text-slate-400 hover:text-white">EN</button>
                
                <div class="relative cursor-pointer hover:text-snap-green ml-2" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 w-4 h-4 bg-snap-green text-white text-[9px] font-black flex items-center justify-center rounded-full hidden">0</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="h-[70px]"></div>

    <!-- ==================== PAGE: HOME ==================== -->
    <div id="page-home" class="page-section page-active">
        
        <!-- Hero Section (Industrial Look & Green Tech Theme) -->
        <section class="hero-container w-full min-h-[500px] md:min-h-[600px] flex items-center relative z-0 overflow-hidden">
            
            <!-- Animated Background Slider -->
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            
            <!-- Gradient Overlay (White to Emerald to Deep Forest) -->
            <div class="hero-overlay"></div>

            <div class="w-full max-w-[1400px] mx-auto px-6 md:px-12 flex flex-col md:flex-row items-center justify-between gap-10">
                
                <!-- White Box (Left) -->
                <div class="hero-white-box w-full md:w-[500px] p-10 md:p-12 z-10 mt-10 md:mt-0 relative">
                    <!-- Green Technology Badge -->
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-emerald-50 text-emerald-600 rounded-full text-[10px] font-black tracking-widest uppercase mb-4 border border-emerald-200 shadow-sm">
                        <i class="fas fa-leaf"></i> <span data-i18n="heroEco">Green Technology</span>
                    </div>
                    
                    <p class="text-slate-500 font-bold text-xs tracking-widest uppercase mb-4" data-i18n="heroSub">PLUG & PLAY AUTOMATION</p>
                    <h1 class="text-4xl md:text-5xl font-black text-slate-900 leading-[1.1] tracking-tight mb-8">
                        <span data-i18n="heroText1">Snap to Connect.</span><br>
                        <span data-i18n="heroText2">Ready to Control.</span>
                    </h1>
                    <button onclick="navigate('product')" class="text-snap-green font-bold text-lg hover:text-snap-green-hover flex items-center gap-2 group">
                        <i class="fas fa-chevron-right text-sm transition-transform group-hover:translate-x-1"></i>
                        <span data-i18n="heroLink">Find out more</span>
                    </button>
                </div>

                <!-- Animated Text Slider (Right) - Adjusted for Green Theme -->
                <div class="hidden md:flex flex-col justify-center flex-1 pl-4 lg:pl-16 z-10 w-full max-w-lg">
                    <div class="bg-emerald-950/70 backdrop-blur-md border border-emerald-500/20 p-8 md:p-10 rounded-2xl shadow-[0_20px_50px_rgba(0,179,110,0.15)]">
                        <h3 class="text-emerald-400 font-black tracking-widest uppercase text-xs mb-6 border-b border-white/10 pb-4">Why Snapcon?</h3>
                        <div class="feature-text-container">
                            <div class="feature-text-slide">
                                <h4 class="text-2xl md:text-3xl font-black text-white mb-2" data-i18n="fs1Title">⚡ Easy Setup</h4>
                                <p class="text-base md:text-lg text-emerald-400 font-medium" data-i18n="fs1Desc">Plug & Play ใช้งานได้ทันที</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-2xl md:text-3xl font-black text-white mb-2" data-i18n="fs2Title">🔗 Seamless Connection</h4>
                                <p class="text-base md:text-lg text-blue-400 font-medium" data-i18n="fs2Desc">เชื่อม PLC / Sensor ได้ง่าย</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-2xl md:text-3xl font-black text-white mb-2" data-i18n="fs3Title">📊 Real-Time Monitoring</h4>
                                <p class="text-base md:text-lg text-amber-400 font-medium" data-i18n="fs3Desc">เห็นข้อมูลทันที</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-2xl md:text-3xl font-black text-white mb-2" data-i18n="fs4Title">🎛 All-in-One Control</h4>
                                <p class="text-base md:text-lg text-purple-400 font-medium" data-i18n="fs4Desc">ควบคุมทุกเครื่องในที่เดียว</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-2xl md:text-3xl font-black text-white mb-2" data-i18n="fs5Title">💰 Cost-Effective</h4>
                                <p class="text-base md:text-lg text-green-400 font-medium" data-i18n="fs5Desc">ถูกกว่า SCADA แบบเดิม</p>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </section>

        <!-- Dark Feature Bar (Google Drive Links) -->
        <section class="feature-bar w-full relative z-40 shadow-2xl border-t border-slate-800">
            <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-white/10">
                
                <!-- Data sheet -->
                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-file-pdf text-4xl text-snap-green mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardDataSheet" class="text-xl font-black text-white tracking-wide uppercase">Data Sheet</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-snap-green transition-colors" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="https://drive.google.com/file/d/1HY0dUjYJZgxRVYYgN5DOV6Ymm9ARCGUW/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 01</a>
                        <a href="https://drive.google.com/file/d/1TC_cXAy7gbgBx0QI0TiL7Kdt1ICljnHj/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 02</a>
                        <a href="https://drive.google.com/file/d/1Yv_gJWWxTL4H_5YmCDAOCnI33gdfcj4j/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 03</a>
                        <a href="https://drive.google.com/file/d/1KtCARlKphuuIqUOU6xg5mnPf99sjCjHD/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 04</a>
                        <a href="https://drive.google.com/file/d/1dlOS1HSYy1qjWASPGQiKRvQsSyZ-lFs4/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green text-sm font-bold text-slate-700">Model 05</a>
                    </div>
                </div>

                <!-- Drawing -->
                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-drafting-compass text-4xl text-blue-500 mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardDrawing" class="text-xl font-black text-white tracking-wide uppercase">2D/3D Drawing</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-blue-400 transition-colors" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="https://drive.google.com/file/d/1CisPrHXeoJgspikAzAOwH0rdhNtQiviy/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 01</a>
                        <a href="https://drive.google.com/file/d/1Gt8onVT7dsyJQkmxdY6s1GZTX4_oUNuB/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 02</a>
                        <a href="https://drive.google.com/file/d/1zesePgsPwZDTUpKzLrmesdnuY6usfe2P/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 03</a>
                        <a href="https://drive.google.com/file/d/1I-63QRJrJksO6xQb1cCWaq9HoDZJ6qBl/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 04</a>
                        <a href="https://drive.google.com/file/d/16z8m9S06kGhyO0C6Tb0mMQ0L4bk5wTDz/view?usp=drive_link" target="_blank" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 text-sm font-bold text-slate-700">Model 05</a>
                    </div>
                </div>

                <!-- Catalog -->
                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-book-open text-4xl text-amber-500 mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardCatalog" class="text-xl font-black text-white tracking-wide uppercase">Catalog</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-amber-400 transition-colors" data-i18n="btnDownload">Download <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="https://drive.google.com/file/d/1_-OdU-N7CnKfG6qY6WV7hW59vL1LX7KD/view?usp=drive_link" target="_blank" data-i18n="cardCatalogFull" class="block px-8 py-4 hover:bg-amber-50 hover:text-amber-600 text-sm font-bold text-slate-700">Download Full Catalog</a>
                    </div>
                </div>

            </div>
        </section>
        
        <!-- Product Slider (Home Page) -->
        <section class="w-full bg-white py-16 z-10 relative">
            <div class="max-w-[1400px] mx-auto px-6">
                <div class="flex justify-between items-end mb-10">
                    <div>
                        <h2 class="text-3xl font-black text-slate-900 tracking-tight uppercase" data-i18n="homeProductsTitle">Featured Products</h2>
                        <div class="w-16 h-1 bg-snap-green mt-2 mb-3"></div>
                        <p class="text-slate-500 text-sm font-medium" data-i18n="homeProductsSub">เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด</p>
                    </div>
                    <div class="hidden sm:flex gap-3">
                        <button onclick="scrollSlider('left')" class="w-10 h-10 rounded bg-slate-100 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white transition-colors active:scale-95"><i class="fas fa-chevron-left"></i></button>
                        <button onclick="scrollSlider('right')" class="w-10 h-10 rounded bg-slate-100 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white transition-colors active:scale-95"><i class="fas fa-chevron-right"></i></button>
                    </div>
                </div>
                
                <div id="home-product-slider" class="slider-container flex gap-6 overflow-x-auto snap-x snap-mandatory pb-4">
                    <!-- Products injected by JS -->
                </div>
                
                <div class="text-center mt-8">
                    <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-slate-800 font-black text-sm uppercase tracking-widest hover:text-snap-green transition-colors" data-i18n="viewAllProducts">View All Products <i class="fas fa-arrow-right"></i></button>
                </div>
            </div>
        </section>

    </div>

    <!-- ==================== PAGE: PRODUCT ==================== -->
    <div id="page-product" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 data-i18n="pageProductTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Conveyor Systems</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-10 max-w-2xl" data-i18n="pageProductSub">รวมเครื่องจักรสายพานลำเลียงอัจฉริยะทุกรุ่นที่ครอบคลุมทุกอุตสาหกรรม</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="product-grid"></div>
        </div>
    </div>

    <!-- ==================== PAGE: SPARE PARTS ==================== -->
    <div id="page-spare" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 data-i18n="pageSpareTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Spare Parts</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-10 max-w-2xl" data-i18n="pageSpareSub">อะไหล่เครื่องจักรและชิ้นส่วนสายพานลำเลียงของแท้ 100%</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4" id="spare-grid"></div>
        </div>
    </div>

    <!-- ==================== PAGE: CART ==================== -->
    <div id="page-cart" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-w-4xl mx-auto px-6 py-10">
            <h2 data-i18n="pageCartTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Quotation Request</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            
            <div class="bg-white sharp-card p-8 md:p-10">
                <div id="cart-header" class="flex justify-between items-center mb-6 pb-4 border-b border-slate-200">
                    <div class="flex items-center gap-3">
                        <input type="checkbox" id="cart-select-all" onclick="toggleSelectAll(this.checked)" class="w-4 h-4 accent-snap-green cursor-pointer">
                        <label for="cart-select-all" class="font-bold text-slate-700 cursor-pointer text-sm" data-i18n="selectAll">เลือกทั้งหมด</label>
                    </div>
                    <button type="button" onclick="deleteSelected()" class="text-red-500 font-bold hover:underline text-sm" data-i18n="deleteSelected">ลบที่เลือก</button>
                </div>

                <div id="cart-items" class="space-y-3 mb-10 max-h-[50vh] overflow-y-auto custom-scrollbar pr-2">
                    <p data-i18n="cartEmpty" class="text-center py-10 text-slate-400 font-bold">ยังไม่มีสินค้าในรถเข็น</p>
                </div>

                <div id="guest-form" class="bg-slate-50 p-6 sharp-card mb-8 hidden">
                    <p class="font-bold text-slate-700 mb-4 uppercase text-xs tracking-widest flex items-center gap-2">
                        <i class="fas fa-info-circle text-snap-green"></i> 
                        <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ (Contact Info)</span>
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <input type="text" id="guest-name" data-i18n-placeholder="phGuestName" placeholder="ชื่อผู้ติดต่อ / ชื่อบริษัท" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green text-sm font-bold sharp-card w-full">
                        <input type="text" id="guest-contact" data-i18n-placeholder="phGuestContact" placeholder="อีเมล หรือ เบอร์โทรศัพท์" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green text-sm font-bold sharp-card w-full">
                    </div>
                </div>

                <div class="flex flex-col md:flex-row justify-between items-center border-t border-slate-200 pt-8 gap-6">
                    <div>
                        <p class="text-slate-500 text-xs font-bold uppercase tracking-widest mb-1" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                        <h3 id="cart-total" class="text-4xl font-black text-snap-green tracking-tighter">฿0</h3>
                    </div>
                    <button type="button" onclick="requestQuote()" class="w-full md:w-auto bg-snap-black text-white px-8 py-4 font-bold hover:bg-snap-green sharp-btn text-sm" data-i18n="btnRequestQuote">
                        ยื่นขอใบเสนอราคา
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: DASHBOARD ==================== -->
    <div id="page-dashboard" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2" data-i18n="navDashboard">Dashboard</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-8" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                <!-- Controls -->
                <div class="bg-white p-6 sharp-card lg:col-span-2 flex flex-col justify-center">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 font-bold hover:bg-snap-green-hover sharp-btn text-xs"><i class="fas fa-play mr-2"></i> START</button>
                        <button onclick="stopSystem()" id="btn-stop" class="bg-slate-200 text-slate-700 py-3 font-bold hover:bg-red-500 hover:text-white sharp-btn text-xs"><i class="fas fa-stop mr-2"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-3 font-bold hover:bg-slate-800 sharp-btn text-xs"><i class="fas fa-sync-alt mr-2"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-3 font-bold hover:bg-blue-700 sharp-btn text-xs"><i class="fas fa-file-csv mr-2"></i> REPORT</button>
                    </div>
                </div>
                
                <!-- Config -->
                <div class="bg-white p-6 sharp-card">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCfgTitle">Configuration</h3>
                    <div class="space-y-3">
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashTarget">Target</label>
                            <input type="number" id="cfg-target" value="50000" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashCarbon">Carbon Factor</label>
                            <input type="number" step="0.0001" id="cfg-carbon" value="0.0072" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                        <div class="flex justify-between items-center">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashEnergy">Energy Factor</label>
                            <input type="number" step="0.001" id="cfg-energy" value="0.015" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                    </div>
                </div>
            </div>

            <!-- KPIs -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card border-t-4 border-t-blue-500">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotOut">Total Output</p>
                    <h3 id="dash-total-output" class="text-4xl font-black text-slate-900 tracking-tighter">0</h3>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-snap-green">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashCalCarbon">Cal Carbon</p>
                    <h3 id="dash-carbon" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-amber-500">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotPower">Total Power</p>
                    <h3 id="dash-power" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
            </div>

            <!-- Progress -->
            <div class="bg-white p-8 sharp-card mb-8">
                <div class="flex justify-between items-end mb-4">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashPlanTitle">Production Planning</h3>
                    <span id="dash-progress-text" class="text-2xl font-black text-snap-green">0.0%</span>
                </div>
                <div class="w-full h-4 bg-slate-100 rounded-sm overflow-hidden mb-6">
                    <div id="dash-progress-bar" class="h-full bg-snap-green transition-all duration-300" style="width: 0%"></div>
                </div>
                <div class="flex justify-between text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <span><i class="far fa-clock mr-1"></i> <span data-i18n="dashTimeElapsed">Elapsed</span>: <span id="dash-time-elapsed" class="text-slate-800">00:00:00</span></span>
                    <span><i class="fas fa-hourglass-half mr-1"></i> <span data-i18n="dashTimeRemain">ETA</span>: <span id="dash-time-remain" class="text-slate-800">--:--:--</span></span>
                </div>
            </div>

            <!-- Nodes Grid -->
            <div class="bg-white p-6 sharp-card">
                <div class="flex justify-between items-center mb-6">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashMacStatus2">Machine Status</h3>
                    <div class="flex gap-4 text-[9px] font-bold uppercase tracking-widest text-slate-500">
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-snap-green"></div> <span data-i18n="statusNormal">Normal</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-amber-400"></div> <span data-i18n="statusWarning">Warning</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-red-500"></div> <span data-i18n="statusMaint">Maint.</span></span>
                    </div>
                </div>
                <div id="dash-nodes-grid" class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-10 gap-2 max-h-[60vh] overflow-y-auto custom-scrollbar p-1">
                    <!-- Nodes injected here -->
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: COMPANY (ABOUT) ==================== -->
    <div id="page-about" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1000px] mx-auto px-6 py-10">
            <h2 data-i18n="navAbout" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Company</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            
            <div class="grid md:grid-cols-2 gap-10 items-center mb-16">
                <div>
                    <h3 class="text-4xl font-black text-snap-black tracking-tighter mb-6 leading-tight">Driving the future of <span class="text-snap-green">industrial automation.</span></h3>
                    <p class="text-slate-600 leading-relaxed mb-6" data-i18n="aboutDesc">
                        Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด
                    </p>
                </div>
                <div class="bg-slate-100 h-64 sharp-card flex items-center justify-center text-slate-300">
                    <i class="fas fa-industry text-6xl"></i>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-snap-black text-white p-10 sharp-card">
                    <i class="fas fa-eye text-3xl text-snap-green mb-6"></i>
                    <h4 class="text-xl font-bold mb-4 uppercase tracking-wider" data-i18n="aboutVisionTitle">Vision</h4>
                    <p class="text-slate-400 leading-relaxed text-sm" data-i18n="aboutVisionDesc">มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้</p>
                </div>
                <div class="bg-snap-green text-white p-10 sharp-card">
                    <i class="fas fa-bullseye text-3xl text-snap-black mb-6"></i>
                    <h4 class="text-xl font-bold mb-4 uppercase tracking-wider text-snap-black" data-i18n="aboutMissionTitle">Mission</h4>
                    <p class="text-emerald-900 leading-relaxed text-sm font-medium" data-i18n="aboutMissionDesc">พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก</p>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: SUPPORT (CONTACT) ==================== -->
    <div id="page-contact" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-w-[1000px] mx-auto px-6 py-10">
            <h2 data-i18n="navContact" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Support</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            
            <div class="bg-white sharp-card p-12 text-center max-w-2xl mx-auto">
                <i class="fas fa-headset text-5xl text-snap-green mb-6"></i>
                <h3 class="text-2xl font-black text-slate-900 mb-2">Technical Support 24/7</h3>
                <p class="text-slate-500 mb-8 text-sm" data-i18n="contactSub">ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ</p>
                
                <div class="space-y-4 max-w-xs mx-auto mb-10 text-left">
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card">
                        <i class="fas fa-envelope text-slate-400"></i>
                        <span class="font-bold text-slate-700 text-sm">snapcon1992@gmail.com</span>
                    </div>
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card">
                        <i class="fab fa-line text-slate-400"></i>
                        <span class="font-bold text-slate-700 text-sm">@SnapconAuto</span>
                    </div>
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card">
                        <i class="fas fa-phone-alt text-slate-400"></i>
                        <span class="font-bold text-slate-700 text-sm">081-XXX-XXXX</span>
                    </div>
                </div>

                <button onclick="window.location.href='mailto:snapcon1992@gmail.com'" class="bg-snap-black text-white px-10 py-4 font-bold hover:bg-snap-green sharp-btn text-sm w-full max-w-xs" data-i18n="btnEmail">SEND DIRECT EMAIL</button>
            </div>
        </div>
    </div>

    <!-- ==================== MODAL: REGISTER ==================== -->
    <div id="modal-register" class="fixed inset-0 bg-snap-black/80 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md sharp-card flex flex-col shadow-2xl relative">
            <button onclick="closeRegisterModal()" class="absolute top-4 right-4 text-slate-400 hover:text-red-500"><i class="fas fa-times"></i></button>
            
            <div class="p-8 border-b border-slate-100 bg-slate-50">
                <h3 class="text-xl font-black text-slate-900 uppercase tracking-tight" data-i18n="regTitle">Create Account</h3>
                <p class="text-xs text-slate-500 mt-1" data-i18n="regDesc">ลงทะเบียนเพื่อเข้าถึงระบบและขอใบเสนอราคา</p>
            </div>
            
            <div class="p-8 space-y-4">
                <div>
                    <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regId">User ID</label>
                    <input type="text" id="reg-id" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card">
                </div>
                <div>
                    <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regPass">Password</label>
                    <input type="password" id="reg-pass" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card">
                </div>
                <div class="h-px bg-slate-100 my-4"></div>
                <div>
                    <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regName">Name / Company</label>
                    <input type="text" id="reg-name" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card">
                </div>
                <div>
                    <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regContact">Email / Phone</label>
                    <input type="text" id="reg-contact" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card">
                </div>
            </div>
            
            <div class="p-6 border-t border-slate-100 bg-slate-50">
                <button type="button" onclick="submitRegistration()" class="w-full bg-snap-green text-white py-3 font-bold hover:bg-snap-green-hover sharp-btn text-sm" data-i18n="btnSubmitReg">Confirm</button>
            </div>
        </div>
    </div>

    <!-- ==================== MODAL: SOCIAL CONTACT (TECHNICIAN) ==================== -->
    <div id="modal-social" class="fixed inset-0 bg-snap-black/80 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-sm sharp-card flex flex-col shadow-2xl relative overflow-hidden">
            <button onclick="closeSocialModal()" class="absolute top-4 right-4 text-slate-400 hover:text-red-500 transition-colors z-10">
                <i class="fas fa-times text-xl"></i>
            </button>
            
            <div class="p-8 pb-6 border-b border-slate-100 bg-slate-50 text-center">
                <div class="w-20 h-20 bg-snap-green/10 text-snap-green rounded-full flex items-center justify-center text-4xl mx-auto mb-4 border-2 border-snap-green/20 shadow-inner group-hover:scale-110 transition-transform">
                    <i class="fas fa-user-cog"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-900 uppercase tracking-tight" data-i18n="socialTitle">ติดต่อช่างผู้เชี่ยวชาญ</h3>
                <p class="text-xs text-slate-500 mt-2 font-bold" data-i18n="socialDesc">เลือกช่องทางที่สะดวกเพื่อรับคำปรึกษาทันที</p>
            </div>
            
            <div class="p-6 space-y-3 bg-white">
                <a href="tel:0812345678" class="flex items-center gap-4 p-4 rounded-2xl border border-slate-200 hover:border-snap-green hover:shadow-md transition-all group cursor-pointer bg-white hover:bg-slate-50">
                    <div class="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center text-slate-400 group-hover:bg-snap-green group-hover:text-white transition-colors text-xl shadow-sm">
                        <i class="fas fa-phone-alt"></i>
                    </div>
                    <div>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Hotline</p>
                        <p class="text-sm font-black text-slate-800">081-XXX-XXXX</p>
                    </div>
                </a>
                <a href="https://line.me" target="_blank" class="flex items-center gap-4 p-4 rounded-2xl border border-slate-200 hover:border-[#00B900] hover:shadow-md transition-all group cursor-pointer bg-white hover:bg-slate-50">
                    <div class="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center text-slate-400 group-hover:bg-[#00B900] group-hover:text-white transition-colors text-2xl shadow-sm">
                        <i class="fab fa-line"></i>
                    </div>
                    <div>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Line Official</p>
                        <p class="text-sm font-black text-slate-800">@SnapconAuto</p>
                    </div>
                </a>
                <a href="https://facebook.com" target="_blank" class="flex items-center gap-4 p-4 rounded-2xl border border-slate-200 hover:border-[#1877F2] hover:shadow-md transition-all group cursor-pointer bg-white hover:bg-slate-50">
                    <div class="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center text-slate-400 group-hover:bg-[#1877F2] group-hover:text-white transition-colors text-xl shadow-sm">
                        <i class="fab fa-facebook-f"></i>
                    </div>
                    <div>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Facebook</p>
                        <p class="text-sm font-black text-slate-800">Snapcon Automation</p>
                    </div>
                </a>
            </div>
        </div>
    </div>

    <!-- Floating Chatbot/Support Button (Technician) -->
    <button onclick="openSocialModal()" class="fixed bottom-6 right-6 w-16 h-16 bg-snap-black text-white rounded-full shadow-[0_15px_35px_rgba(0,0,0,0.4)] flex items-center justify-center text-2xl hover:bg-snap-green transition-all z-50 group border-[3px] border-white hover:scale-110 active:scale-95 cursor-pointer">
        <i class="fas fa-user-cog group-hover:animate-pulse"></i>
        <span class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 border-2 border-white rounded-full animate-bounce"></span>
    </button>

    <script>
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzTXYEcWYEsbcwL0ipt5vl1azB-C8psZUuwpjfIirzCdH2mBE2OHNdKSMoNPhklRt2M/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let memoryUsers = { '001': '123' };

        // 📊 DASHBOARD STATE (100 Machines)
        let dashState = {
            isRunning: false, target: 50000, carbonFactor: 0.0072, energyFactor: 0.015,
            intervalId: null, elapsedSeconds: 0,
            nodes: [
                { id: 1, name: "M-01 Main", output: 0, status: 'Offline', health: 100.0, wearRate: 0.3 },
                { id: 2, name: "M-02 Sort", output: 0, status: 'Offline', health: 100.0, wearRate: 0.5 },
                { id: 3, name: "M-03 Pack", output: 0, status: 'Offline', health: 100.0, wearRate: 0.2 },
                { id: 4, name: "M-04 Seal", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 },
                { id: 5, name: "M-05 Label", output: 0, status: 'Offline', health: 100.0, wearRate: 0.6 },
                { id: 6, name: "M-06 Load", output: 0, status: 'Offline', health: 100.0, wearRate: 0.3 },
                { id: 7, name: "M-07 Scan", output: 0, status: 'Offline', health: 100.0, wearRate: 0.5 },
                { id: 8, name: "M-08 Wrap", output: 0, status: 'Offline', health: 100.0, wearRate: 0.7 },
                { id: 9, name: "M-09 Stack", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 },
                { id: 10, name: "M-10 Exp", output: 0, status: 'Offline', health: 100.0, wearRate: 0.2 }
            ]
        };

        // 🔧 DATA GENERATION
        let products = [
            { id: 'M01', name: 'Snapcon Model 01 (Mini)', price: 15000, img: 'https://i.ibb.co/bZ7TKQg/01.png', specs: { th: ["L: 0.5-5m", "W: 200-400mm", "Load: 0-50kg"], en: ["L: 0.5-5m", "W: 200-400mm", "Load: 0-50kg"] } },
            { id: 'M02', name: 'Snapcon Model 02 (Std)', price: 22000, img: 'https://i.ibb.co/tTCb2j0h/02.png', specs: { th: ["L: 1-15m", "W: 300-600mm", "Load: 0-100kg"], en: ["L: 1-15m", "W: 300-600mm", "Load: 0-100kg"] } },
            { id: 'M03', name: 'Snapcon Model 03 (Heavy)', price: 28500, img: 'https://i.ibb.co/PGNt8dfj/03.png', specs: { th: ["L: 2-30m", "W: 500-1000mm", "Load: 0-300kg"], en: ["L: 2-30m", "W: 500-1000mm", "Load: 0-300kg"] } },
            { id: 'M04', name: 'Snapcon Model 04 (Speed)', price: 35000, img: 'https://i.ibb.co/mVfD9H0B/04.png', specs: { th: ["L: 1-20m", "W: 400-800mm", "Load: 0-80kg"], en: ["L: 1-20m", "W: 400-800mm", "Load: 0-80kg"] } },
            { id: 'M05', name: 'Snapcon Pro 05 (Custom)', price: 45000, img: 'https://i.ibb.co/x4SGKtb/05.png', specs: { th: ["L: Custom", "W: Custom", "Load: Custom"], en: ["L: Custom", "W: Custom", "Load: Custom"] } }
        ];

        let spares = [
            { id: 'SP001', name: 'Roller Series - P001', price: 525, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Roller", "Stock: Ready"], en: ["Type: Roller", "Stock: Ready"] } },
            { id: 'SP002', name: 'Conveyor Belt PU', price: 550, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Belt PU", "Stock: Ready"], en: ["Type: Belt PU", "Stock: Ready"] } },
            { id: 'SP003', name: 'Drive Motor AC', price: 1500, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Motor", "Stock: Ready"], en: ["Type: Motor", "Stock: Ready"] } },
            { id: 'SP004', name: 'Sensor Switch', price: 300, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Sensor", "Stock: Ready"], en: ["Type: Sensor", "Stock: Ready"] } },
            { id: 'SP005', name: 'Control Board', price: 2500, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Board", "Stock: Ready"], en: ["Type: Board", "Stock: Ready"] } }
        ];
        
        const allItems = [...products, ...spares];

        // 🌐 DICTIONARY
        const dict = {
            th: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navContact: "Support", navAbout: "Company",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroSub: "PLUG & PLAY AUTOMATION", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroLink: "> Find out more",
                
                fs1Title: "⚡ Easy Setup", fs1Desc: "Plug & Play ใช้งานได้ทันที",
                fs2Title: "🔗 Seamless Connection", fs2Desc: "เชื่อม PLC / Sensor ได้ง่าย",
                fs3Title: "📊 Real-Time Monitoring", fs3Desc: "เห็นข้อมูลทันที",
                fs4Title: "🎛 All-in-One Control", fs4Desc: "ควบคุมทุกเครื่องในที่เดียว",
                fs5Title: "💰 Cost-Effective", fs5Desc: "ถูกกว่า SCADA แบบเดิม",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", 
                cardCatalog: "Catalog", btnDownload: "Download", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "Conveyor Systems", pageProductSub: "ระบบสายพานลำเลียงอัจฉริยะสำหรับอุตสาหกรรมยุคใหม่",
                pageSpareTitle: "Spare Parts", pageSpareSub: "อะไหล่และชิ้นส่วนสายพานลำเลียงคุณภาพสูง",
                btnAddToCart: "ADD TO CART", pageCartTitle: "Quotation Request", cartEmpty: "ไม่มีสินค้าในรถเข็น",
                cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "Delete Selected", specTitle: "SPECS",
                alertLoginSuccess: "เข้าสู่ระบบสำเร็จ!", alertAddCart: "เพิ่มลงรถเข็นแล้ว", alertQuoteReq: "กรุณาเลือกสินค้า", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อ",
                contactSub: "ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ", btnEmail: "SEND DIRECT EMAIL",
                aboutDesc: "Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System",
                aboutVisionTitle: "Vision", aboutVisionDesc: "มุ่งมั่นที่จะเป็นผู้นำด้านระบบอัตโนมัติที่ล้ำสมัยที่สุดในภูมิภาค",
                aboutMissionTitle: "Mission", aboutMissionDesc: "พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาติดตั้ง และยกระดับอุตสาหกรรม",
                regTitle: "Create Account", regDesc: "ลงทะเบียนเพื่อเข้าถึงระบบ", btnSubmitReg: "CONFIRM",
                regId: "User ID", regPass: "Password", regName: "Name / Company", regContact: "Email / Phone",
                dashSubTitle: "Enterprise Monitoring & Predictive Maintenance System",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Power Use",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status",
                statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint.",
                guestContactTitle: "Contact Info", guestNotice: "ข้อมูลปลอดภัยด้วยมาตรฐาน Google",
                phId: "ID", phPass: "PW", phGuestName: "Name / Company", phGuestContact: "Email or Phone",
                phRegId: "Create ID", phRegPass: "Create PW", phRegName: "Company Name", phRegContact: "Email/Phone",
                socialTitle: "ติดต่อช่างผู้เชี่ยวชาญ", socialDesc: "เลือกช่องทางที่สะดวกเพื่อรับคำปรึกษาทันที",
                homeProductsTitle: "Featured Products", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด", viewAllProducts: "View All Products"
            },
            en: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navContact: "Support", navAbout: "Company",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroSub: "PLUG & PLAY AUTOMATION", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroLink: "> Find out more",
                
                fs1Title: "⚡ Easy Setup", fs1Desc: "Plug & Play ready to use",
                fs2Title: "🔗 Seamless Connection", fs2Desc: "Easy PLC / Sensor integration",
                fs3Title: "📊 Real-Time Monitoring", fs3Desc: "Instant data visibility",
                fs4Title: "🎛 All-in-One Control", fs4Desc: "Manage all machines in one place",
                fs5Title: "💰 Cost-Effective", fs5Desc: "More affordable than traditional SCADA",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", 
                cardCatalog: "Catalog", btnDownload: "Download", cardCatalogFull: "Download Full Catalog",
                pageProductTitle: "Conveyor Systems", pageProductSub: "Intelligent conveyor systems for modern industries.",
                pageSpareTitle: "Spare Parts", pageSpareSub: "High-quality genuine conveyor components.",
                btnAddToCart: "ADD TO CART", pageCartTitle: "Quotation Request", cartEmpty: "Your cart is empty",
                cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "Delete Selected", specTitle: "SPECS",
                alertLoginSuccess: "Login Successful!", alertAddCart: "Added to cart", alertQuoteReq: "Select an item", alertQuoteGuestReq: "Provide contact info",
                contactSub: "Official Technical Support & Inquiries", btnEmail: "SEND DIRECT EMAIL",
                aboutDesc: "Snapcon Automation is a leader in modern industrial technology, focusing on ease of connection and installation through Plug & Play Systems.",
                aboutVisionTitle: "Vision", aboutVisionDesc: "To be the leading provider of advanced automation systems in the region.",
                aboutMissionTitle: "Mission", aboutMissionDesc: "Develop innovations that reduce complexity and elevate industrial efficiency.",
                regTitle: "Create Account", regDesc: "Register to access the system", btnSubmitReg: "CONFIRM",
                regId: "User ID", regPass: "Password", regName: "Name / Company", regContact: "Email / Phone",
                dashSubTitle: "Enterprise Monitoring & Predictive Maintenance System",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Total Power Use",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status & Health",
                statusNormal: "Optimal (>70%)", statusWarning: "Warning (<70%)", statusMaint: "Maintenance (<30%)",
                guestContactTitle: "Contact Info", guestNotice: "Securely saved via Google standard",
                phId: "ID", phPass: "PW", phGuestName: "Contact Name / Company", phGuestContact: "Email or Phone Number",
                phRegId: "Create your User ID", phRegPass: "Create your Password", phRegName: "Enter your full name", phRegContact: "Enter email or phone",
                socialTitle: "Technical Support", socialDesc: "Choose a channel for immediate consultation",
                homeProductsTitle: "Featured Products", homeProductsSub: "Explore our latest automation machines and equipment", viewAllProducts: "View All Products"
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
            else { alert(currentLang === 'th' ? "กรุณา Login ก่อนเข้าสู่ Dashboard" : "Please Login to access Dashboard"); document.getElementById('userId').focus(); }
        }

        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            if (memoryUsers[id] === pass || (id==='001' && pass==='123')) {
                isLoggedIn = true;
                document.getElementById('displayUser').innerText = id || '001';
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('login-section').classList.remove('lg:flex');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                alert(dict[currentLang].alertLoginSuccess);
                document.getElementById('userId').value = ''; document.getElementById('userPass').value = '';
            } else alert(currentLang === 'th' ? "ID หรือ Password ไม่ถูกต้อง" : "Invalid ID or Password");
        }

        function openRegisterModal() { document.getElementById('modal-register').classList.replace('hidden', 'flex'); }
        function closeRegisterModal() { document.getElementById('modal-register').classList.replace('flex', 'hidden'); }

        function openSocialModal() { document.getElementById('modal-social').classList.replace('hidden', 'flex'); }
        function closeSocialModal() { document.getElementById('modal-social').classList.replace('flex', 'hidden'); }

        function submitRegistration() {
            const id = document.getElementById('reg-id').value.trim();
            const pass = document.getElementById('reg-pass').value.trim();
            const name = document.getElementById('reg-name').value.trim();
            const contact = document.getElementById('reg-contact').value.trim();
            
            if(!id || !pass || !name || !contact) return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบถ้วน" : "Please fill all fields");
            
            if(memoryUsers[id]) return alert(currentLang === 'th' ? "User ID นี้มีผู้ใช้งานแล้ว กรุณาตั้งใหม่" : "User ID already exists");
            
            // ตรวจสอบความถูกต้องของข้อมูลเบื้องต้น (อีเมล หรือ เบอร์โทร 9-10 หลัก)
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const phoneRegex = /^[0-9]{9,10}$/;
            if (!emailRegex.test(contact) && !phoneRegex.test(contact)) {
                return alert(currentLang === 'th' ? "กรุณากรอกรูปแบบอีเมลหรือเบอร์โทรศัพท์ให้ถูกต้อง" : "Please enter a valid email or phone format");
            }
            if (name.length < 2) {
                return alert(currentLang === 'th' ? "กรุณากรอกชื่อ-นามสกุล หรือชื่อบริษัทให้ชัดเจน" : "Please enter a valid name");
            }

            memoryUsers[id] = pass;
            try { fetch(GOOGLE_SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: JSON.stringify({ type: "Registration", name_or_id: id, email: contact, details: name }) }); } catch(e) {}
            
            alert(currentLang === 'th' ? "ลงทะเบียนสำเร็จ! ระบบกำลังนำเข้าสู่ระบบอัตโนมัติ..." : "Registered successfully! Auto-logging in...");
            
            // ใช้งาน Auto Login หลังจากการสมัครสมาชิก
            isLoggedIn = true;
            document.getElementById('displayUser').innerText = id;
            document.getElementById('login-section').classList.add('hidden');
            document.getElementById('login-section').classList.remove('lg:flex');
            document.getElementById('user-section').classList.remove('hidden');
            document.getElementById('user-section').classList.add('flex');
            
            // ล้างข้อมูลในช่องกรอก
            document.getElementById('reg-id').value = '';
            document.getElementById('reg-pass').value = '';
            document.getElementById('reg-name').value = '';
            document.getElementById('reg-contact').value = '';
            
            closeRegisterModal();
        }

        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden'); document.getElementById('login-section').classList.add('lg:flex');
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
            const link = document.createElement("a"); link.href = URL.createObjectURL(blob); link.download = `Snapcon_Report.csv`; link.click();
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
            document.getElementById('dash-time-remain').innerText = remainStr;

            grid.innerHTML = dashState.nodes.map(n => {
                const isRun = n.status === 'Running', isWarn = n.status === 'Warning', isMaint = n.status === 'Maintenance';
                let dotBg = 'bg-slate-300';
                if (isRun) dotBg = 'bg-snap-green animate-pulse'; else if (isWarn) dotBg = 'bg-amber-400 animate-pulse'; else if (isMaint) dotBg = 'bg-red-500';
                let healthBarCol = n.health > 70 ? 'bg-snap-green' : (n.health > 30 ? 'bg-amber-400' : 'bg-red-500');
                
                return `
                <div class="bg-slate-50 border border-slate-200 p-2 rounded-sm flex flex-col justify-between">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-[8px] font-bold text-slate-500 truncate" title="${n.name}">${n.name}</span>
                        <div class="w-1.5 h-1.5 rounded-full ${dotBg} shrink-0"></div>
                    </div>
                    <h4 class="text-sm font-black text-slate-800 text-center leading-none">${n.output}</h4>
                    <div class="w-full h-1 bg-slate-200 rounded-none overflow-hidden mt-1"><div class="h-full ${healthBarCol}" style="width: ${n.health}%"></div></div>
                </div>`;
            }).join('');
        }

        // 🛒 PRODUCT & CART SYSTEM
        function createItemCard(p) {
            return `
                <div class="bg-white sharp-card p-4 flex flex-col h-full">
                    <div class="bg-slate-50 mb-3 h-40 flex items-center justify-center p-2">
                        <img src="${p.img}" loading="lazy" class="max-h-full max-w-full object-contain mix-blend-multiply">
                    </div>
                    <h4 class="font-black text-sm text-slate-900 mb-2 truncate" title="${p.name}">${p.name}</h4>
                    <div class="bg-slate-50 p-2 mb-3 flex-grow text-[10px] text-slate-600 font-medium space-y-1">
                        ${p.specs[currentLang].map(s => `<div class="truncate border-b border-slate-200 last:border-0 pb-1 last:pb-0">${s}</div>`).join('')}
                    </div>
                    <p class="text-snap-green font-black text-lg mb-3">฿${p.price.toLocaleString()}</p>
                    <button type="button" onclick="addToCart('${p.id}')" class="w-full bg-slate-100 text-slate-700 py-2 font-bold text-xs hover:bg-snap-green hover:text-white sharp-btn border border-slate-200 hover:border-transparent">${dict[currentLang].btnAddToCart}</button>
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
            alert(dict[currentLang].alertAddCart);
        }

        function renderCart() {
            const container = document.getElementById('cart-items'); const guestForm = document.getElementById('guest-form');
            if(!container) return;
            if (isLoggedIn) guestForm.classList.add('hidden'); else guestForm.classList.remove('hidden');

            if(cart.length === 0) {
                container.innerHTML = `<p class="text-center py-8 text-slate-400 font-bold text-sm bg-slate-50 border border-slate-100">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }
            container.innerHTML = cart.map(item => `
                <div class="flex items-center bg-white border border-slate-200 p-3 sharp-card gap-4">
                    <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleItem(${item.cartId})" class="w-4 h-4 accent-snap-green shrink-0">
                    <img src="${item.img}" class="w-12 h-12 object-contain bg-slate-50 p-1 shrink-0 mix-blend-multiply">
                    <div class="flex-1 min-w-0">
                        <span class="font-bold text-slate-800 text-sm block truncate">${item.name}</span>
                        <span class="text-[10px] text-slate-500 uppercase tracking-widest">${item.id}</span>
                    </div>
                    <span class="font-black text-slate-800 text-lg">฿${item.price.toLocaleString()}</span>
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
            
            const subject = encodeURIComponent("Quotation Request - Snapcon");
            const body = "Request for Official Quotation:%0A%0AItems:%0A" + detailsForEmail + "%0A%0AEstimated Total: %E0%B8%BF" + total.toLocaleString() + "%0A%0AContact Info: " + encodeURIComponent(info);
            window.location.href = `mailto:snapcon1992@gmail.com?subject=${subject}&body=${body}`;
            
            cart = cart.filter(i => !i.selected); document.getElementById('cart-badge').innerText = cart.length; if(cart.length===0) document.getElementById('cart-badge').classList.add('hidden'); renderCart(); navigate('home');
        }

        // 🌐 LANGUAGE SYSTEM
        function setLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('[data-i18n]').forEach(el => { const key = el.getAttribute('data-i18n'); if (dict[lang][key]) el.innerHTML = dict[lang][key]; });
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => { const key = el.getAttribute('data-i18n-placeholder'); if (dict[lang][key]) el.placeholder = dict[lang][key]; });
            
            document.getElementById('btn-lang-th').className = lang === 'th' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            document.getElementById('btn-lang-en').className = lang === 'en' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            
            renderProducts(); renderDashboard(); if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        setLanguage('th');
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2100, scrolling=True)
