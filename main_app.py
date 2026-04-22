import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# SNAPCON MASTER HTML/CSS/JS (PRODUCTION READY)
# ==========================================
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
        body { margin: 0; padding: 0; background-color: #f8fafc; overflow-x: hidden; -webkit-tap-highlight-color: transparent; }
        .max-container { max-width: 1400px; margin: 0 auto; padding: 0 1.5rem; }
        
        .hero-container { background-color: #e2e8f0; position: relative; }
        .hero-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, #ffffff 40%, rgba(16, 185, 129, 0.9) 65%, rgba(2, 44, 34, 0.95) 100%);
            z-index: 5; pointer-events: none;
        }
        @media (max-width: 768px) {
            .hero-overlay {
                background: linear-gradient(to bottom, rgba(255,255,255,0.95) 0%, rgba(16, 185, 129, 0.9) 50%, rgba(2, 44, 34, 0.95) 100%);
            }
        }
        .hero-white-box { background-color: white; border-bottom: 6px solid #00B36E; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15); border-radius: 1rem; }

        .slide-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; animation: slideBgAnimation 20s infinite linear; }
        .slide-1 { background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80'); animation-delay: 0s; }
        .slide-2 { background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1920&q=80'); animation-delay: 5s; }
        .slide-3 { background-image: url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1920&q=80'); animation-delay: 10s; }
        .slide-4 { background-image: url('https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?auto=format&fit=crop&w=1920&q=80'); animation-delay: 15s; }
        @keyframes slideBgAnimation { 0% { opacity: 0; transform: scale(1.05) translateX(20px); } 5% { opacity: 1; transform: scale(1.05) translateX(15px); } 20% { opacity: 1; transform: scale(1.05) translateX(-5px); } 25% { opacity: 0; transform: scale(1.05) translateX(-10px); } 100% { opacity: 0; } }

        .nav-link { position: relative; color: white; font-weight: 700; font-size: 0.85rem; transition: color 0.3s; }
        .nav-link:hover { color: #00B36E; }
        .nav-link::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: #00B36E; transition: width 0.3s; }
        .nav-link:hover::after { width: 100%; }

        .page-section { display: none !important; }
        .page-active { display: block !important; animation: fadeIn 0.4s ease-out forwards; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu, .dropdown-container:focus-within .dropdown-menu { display: block; }
        
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        .sharp-card { border-radius: 1rem; transition: all 0.3s; }
        .sharp-card:hover { box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05); transform: translateY(-4px); }
        
        .feature-text-container { position: relative; height: 120px; width: 100%; display: flex; align-items: flex-start; }
        .feature-text-slide { position: absolute; width: 100%; opacity: 0; transform: translateY(20px); animation: fadeSlideText 25s infinite; }
        .feature-text-slide:nth-child(1) { animation-delay: 0s; } 
        .feature-text-slide:nth-child(2) { animation-delay: 5s; } 
        .feature-text-slide:nth-child(3) { animation-delay: 10s; }
        .feature-text-slide:nth-child(4) { animation-delay: 15s; }
        .feature-text-slide:nth-child(5) { animation-delay: 20s; }
        @keyframes fadeSlideText { 
            0% { opacity: 0; transform: translateY(20px); } 
            4% { opacity: 1; transform: translateY(0); } 
            16% { opacity: 1; transform: translateY(0); } 
            20% { opacity: 0; transform: translateY(-20px); } 
            100% { opacity: 0; transform: translateY(-20px); } 
        }
        
        .line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    </style>
</head>
<body class="font-sans text-slate-800">

    <!-- Top Navigation -->
    <nav class="bg-snap-black h-[70px] w-full fixed top-0 z-[999] flex items-center justify-between px-4 md:px-10 shadow-md">
        <div class="flex items-center gap-2 cursor-pointer shrink-0" onclick="navigate('home')">
            <span class="font-black text-2xl md:text-3xl text-snap-green tracking-tighter">SNAPCON</span>
        </div>
        
        <div class="hidden lg:flex items-center gap-8 ml-8">
            <button onclick="navigate('product')" data-i18n="navProduct" class="nav-link">Products</button>
            <button onclick="navigate('spare')" data-i18n="navSpare" class="nav-link">Spare Parts</button>
            <button onclick="checkDashboardAuth()" data-i18n="navDashboard" class="nav-link">Dashboard</button>
            <button onclick="navigate('project')" data-i18n="navProject" class="nav-link">Projects</button>
            <button onclick="navigate('about')" data-i18n="navAbout" class="nav-link">Company</button>
            <button onclick="navigate('contact')" data-i18n="navContact" class="nav-link">Support</button>
        </div>

        <div class="flex items-center shrink-0 ml-auto">
            <div id="login-section" class="hidden lg:flex items-center gap-2 pr-5">
                <input type="text" id="userId" data-i18n-placeholder="phId" placeholder="ID" class="h-9 w-24 px-3 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green rounded-lg transition-colors">
                <input type="password" id="userPass" data-i18n-placeholder="phPass" placeholder="PW" class="h-9 w-24 px-3 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green rounded-lg transition-colors">
                <button onclick="handleLogin()" class="h-9 px-4 bg-snap-green text-white font-bold text-xs hover:bg-snap-green-hover rounded-lg transition-colors"><i class="fas fa-sign-in-alt"></i></button>
                <button onclick="openRegisterModal()" class="h-9 px-4 bg-slate-700 text-white font-bold text-xs hover:bg-slate-600 rounded-lg transition-colors"><i class="fas fa-user-plus"></i></button>
            </div>
            
            <div id="user-section" class="hidden lg:hidden items-center gap-3 pr-5">
                <span class="text-white text-sm"><i class="far fa-user-circle text-snap-green mr-1 text-lg"></i> <span id="displayUser" class="font-bold">User</span></span>
                <button onclick="handleLogout()" class="text-slate-400 hover:text-red-400 text-xs ml-2 bg-slate-800 px-3 py-1.5 rounded-lg transition-colors"><i class="fas fa-sign-out-alt mr-1"></i> ออกจากระบบ</button>
            </div>

            <div class="flex items-center gap-3 text-white text-base md:text-lg border-l border-slate-700 pl-4 ml-1 md:ml-0">
                <button id="btn-lang-th" onclick="setLanguage('th')" class="text-xs font-bold text-snap-green hover:text-white transition-colors">TH</button>
                <span class="text-slate-600 text-xs">|</span>
                <button id="btn-lang-en" onclick="setLanguage('en')" class="text-xs font-bold text-slate-400 hover:text-white transition-colors">EN</button>
                <div class="relative cursor-pointer hover:text-snap-green ml-1 transition-colors" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart text-xl"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 w-4 h-4 bg-red-500 text-white text-[9px] font-black flex items-center justify-center rounded-full hidden border border-snap-black">0</span>
                </div>
            </div>

            <button onclick="toggleMobileMenu()" class="lg:hidden text-slate-300 hover:text-white text-2xl ml-5 focus:outline-none">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </nav>

    <!-- MOBILE MENU -->
    <div id="mobile-menu" class="fixed inset-0 bg-snap-black/95 backdrop-blur-md z-[999] hidden flex-col px-6 py-8 overflow-y-auto w-full h-full">
        <div class="flex justify-between items-center mb-10 border-b border-slate-800 pb-6 mt-2">
            <span class="font-black text-3xl text-snap-green tracking-tighter">SNAPCON</span>
            <button onclick="toggleMobileMenu()" class="text-slate-400 hover:text-white text-3xl focus:outline-none"><i class="fas fa-times"></i></button>
        </div>
        
        <div id="mobile-login-section" class="flex flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full">
            <h3 class="text-white font-bold text-sm uppercase tracking-widest mb-2" data-i18n="navLogin">เข้าสู่ระบบ (Login)</h3>
            <input type="text" id="mobile-userId" placeholder="ID" class="w-full px-4 py-4 rounded-xl bg-slate-800/50 text-white placeholder-slate-500 outline-none focus:border-snap-green border border-slate-700">
            <input type="password" id="mobile-userPass" placeholder="Password" class="w-full px-4 py-4 rounded-xl bg-slate-800/50 text-white placeholder-slate-500 outline-none focus:border-snap-green border border-slate-700">
            <button onclick="handleLogin()" class="w-full py-4 bg-snap-green text-white font-bold rounded-xl uppercase tracking-widest mt-2 shadow-lg shadow-snap-green/20">Login</button>
            <button onclick="openRegisterModal(); toggleMobileMenu();" class="w-full py-4 bg-slate-800 text-white font-bold rounded-xl uppercase tracking-widest border border-slate-700">Register</button>
        </div>
        
        <div id="mobile-user-section" class="hidden flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full">
            <div class="flex items-center gap-4 text-white p-4 bg-slate-800/50 rounded-2xl border border-slate-700">
                <div class="w-12 h-12 bg-snap-green/20 rounded-full flex items-center justify-center">
                    <i class="far fa-user text-snap-green text-2xl"></i>
                </div>
                <div>
                    <p class="text-[10px] text-slate-400 font-bold uppercase tracking-widest">Signed in as</p>
                    <span id="mobile-displayUser" class="font-black text-xl">User</span>
                </div>
            </div>
            <button onclick="handleLogout()" class="w-full py-4 bg-red-500/10 text-red-400 font-bold rounded-xl border border-red-500/20 uppercase tracking-widest mt-2"><i class="fas fa-sign-out-alt mr-2"></i> Logout</button>
        </div>

        <div class="flex flex-col gap-2 w-full pb-10">
            <button onclick="navigate('home'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 border-b border-slate-800 hover:text-snap-green flex justify-between" data-i18n="navHome">Home <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
            <button onclick="navigate('product'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 border-b border-slate-800 hover:text-snap-green flex justify-between" data-i18n="navProduct">Products <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
            <button onclick="navigate('spare'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 border-b border-slate-800 hover:text-snap-green flex justify-between" data-i18n="navSpare">Spare Parts <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
            <button onclick="checkDashboardAuth(); toggleMobileMenu();" class="text-left text-snap-green text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navDashboard">Dashboard <i class="fas fa-chevron-right text-sm text-snap-green"></i></button>
            <button onclick="navigate('project'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 border-b border-slate-800 hover:text-snap-green flex justify-between" data-i18n="navProject">Projects <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
            <button onclick="navigate('about'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 border-b border-slate-800 hover:text-snap-green flex justify-between" data-i18n="navAbout">Company <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
            <button onclick="navigate('contact'); toggleMobileMenu();" class="text-left text-white text-xl font-black py-4 hover:text-snap-green flex justify-between" data-i18n="navContact">Support <i class="fas fa-chevron-right text-sm text-slate-600"></i></button>
        </div>
    </div>

    <!-- PAGE: HOME -->
    <div id="page-home" class="page-section page-active">
        <section class="hero-container w-full min-h-[550px] md:min-h-[650px] flex items-center relative overflow-hidden pb-16">
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay z-0"></div>
            <div class="max-container relative z-10 flex flex-col lg:flex-row items-center justify-between gap-10 w-full pt-20">
                <div class="hero-white-box w-full lg:w-[520px] p-8 sm:p-10 md:p-12 bg-white/95 backdrop-blur-sm">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-emerald-50 text-emerald-600 rounded-full text-[10px] font-black tracking-widest uppercase mb-4 border border-emerald-200">
                        <i class="fas fa-leaf"></i> <span data-i18n="heroEco">Green Technology</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-black text-slate-900 leading-[1.1] mb-6">
                        <span data-i18n="heroText1">Snap to Connect.</span><br>
                        <span data-i18n="heroText2" class="text-snap-green">Ready to Control.</span>
                    </h1>
                    <p class="text-slate-500 font-medium text-sm mb-8 leading-relaxed" data-i18n="heroDesc">
                        เปลี่ยนความซับซ้อนให้เป็นเรื่องง่าย ด้วยระบบออโตเมชัน Plug & Play ที่พร้อมให้คุณควบคุมสายการผลิตได้ทันที
                    </p>
                    <button onclick="navigate('product')" class="w-full sm:w-auto bg-snap-black text-white px-8 py-4 rounded-xl font-bold text-sm hover:bg-snap-green flex items-center justify-center gap-2 group transition-all shadow-lg hover:shadow-snap-green/30">
                        <span data-i18n="heroLink">ดูสินค้าทั้งหมด</span>
                        <i class="fas fa-arrow-right text-xs transition-transform group-hover:translate-x-1"></i>
                    </button>
                </div>

                <div class="flex flex-col justify-center flex-1 w-full lg:pl-16 mt-6 lg:mt-0">
                    <div class="bg-snap-black/70 backdrop-blur-md border border-white/20 p-6 sm:p-8 md:p-10 rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.4)] relative overflow-hidden">
                        <div class="absolute -top-10 -right-10 w-40 h-40 bg-emerald-500/30 blur-[50px] rounded-full pointer-events-none"></div>
                        <h3 class="text-emerald-400 font-black tracking-widest uppercase text-[10px] sm:text-xs mb-6 sm:mb-8 border-b border-white/10 pb-3 sm:pb-4 inline-block relative z-10">Why Snapcon?</h3>
                        <div class="feature-text-container relative z-10">
                            <div class="feature-text-slide">
                                <h4 class="text-xl sm:text-2xl md:text-3xl font-black text-white mb-2 tracking-tight" data-i18n="fs1Title">⚡ Easy Setup (Plug & Play)</h4>
                                <p class="text-sm sm:text-base md:text-lg text-emerald-300 font-medium" data-i18n="fs1Desc">ติดตั้งง่าย ใช้งานได้ทันที</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-xl sm:text-2xl md:text-3xl font-black text-white mb-2 tracking-tight" data-i18n="fs2Title">📊 Real-Time Monitoring</h4>
                                <p class="text-sm sm:text-base md:text-lg text-blue-300 font-medium" data-i18n="fs2Desc">แสดงผลแบบเรียลไทม์ เห็นข้อมูลทันที</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-xl sm:text-2xl md:text-3xl font-black text-white mb-2 tracking-tight" data-i18n="fs3Title">🎛 Centralized Control</h4>
                                <p class="text-sm sm:text-base md:text-lg text-amber-300 font-medium" data-i18n="fs3Desc">ควบคุมทุกเครื่องจักรจากจุดเดียว</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-xl sm:text-2xl md:text-3xl font-black text-white mb-2 tracking-tight" data-i18n="fs4Title">🛡 Built-in Poka-Yoke</h4>
                                <p class="text-sm sm:text-base md:text-lg text-rose-300 font-medium" data-i18n="fs4Desc">ระบบกันพลาดในตัว ป้องกันความผิดพลาดอัตโนมัติ</p>
                            </div>
                            <div class="feature-text-slide">
                                <h4 class="text-xl sm:text-2xl md:text-3xl font-black text-white mb-2 tracking-tight" data-i18n="fs5Title">☁️ Cloud Ready</h4>
                                <p class="text-sm sm:text-base md:text-lg text-cyan-300 font-medium" data-i18n="fs5Desc">รองรับการเชื่อมต่อ Cloud พร้อมใช้งาน</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Feature Dropdowns -->
        <div class="relative z-40 max-container lg:-mt-16 mb-16 px-4 sm:px-6">
            <div class="bg-white rounded-2xl shadow-xl shadow-slate-200/50 border border-slate-100 grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-slate-100">
                <div tabindex="0" class="dropdown-container relative group p-6 sm:p-8 flex flex-col items-center cursor-pointer hover:bg-slate-50 transition-colors focus:outline-none rounded-t-2xl md:rounded-l-2xl md:rounded-tr-none">
                    <div class="w-14 h-14 sm:w-16 sm:h-16 bg-emerald-50 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fas fa-file-pdf text-2xl sm:text-3xl text-snap-green"></i>
                    </div>
                    <h3 data-i18n="cardDataSheet" class="text-base sm:text-lg font-black text-slate-800 uppercase tracking-tight">Data Sheet</h3>
                    <p class="text-[10px] text-slate-400 mt-2 font-bold uppercase tracking-widest flex items-center" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    <div class="dropdown-menu md:absolute top-full left-0 w-full bg-slate-50 md:bg-white md:shadow-2xl border-t border-slate-100 md:border md:border-slate-100 rounded-b-2xl overflow-hidden mt-4 md:mt-1 z-50" id="menu-datasheet"></div>
                </div>
                <div tabindex="0" class="dropdown-container relative group p-6 sm:p-8 flex flex-col items-center cursor-pointer hover:bg-slate-50 transition-colors focus:outline-none">
                    <div class="w-14 h-14 sm:w-16 sm:h-16 bg-blue-50 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fas fa-drafting-compass text-2xl sm:text-3xl text-blue-500"></i>
                    </div>
                    <h3 data-i18n="cardDrawing" class="text-base sm:text-lg font-black text-slate-800 uppercase tracking-tight">2D/3D Drawing</h3>
                    <p class="text-[10px] text-slate-400 mt-2 font-bold uppercase tracking-widest flex items-center" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    <div class="dropdown-menu md:absolute top-full left-0 w-full bg-slate-50 md:bg-white md:shadow-2xl border-t border-slate-100 md:border md:border-slate-100 rounded-b-2xl overflow-hidden mt-4 md:mt-1 z-50" id="menu-drawing"></div>
                </div>
                <div tabindex="0" class="dropdown-container relative group p-6 sm:p-8 flex flex-col items-center cursor-pointer hover:bg-slate-50 transition-colors focus:outline-none rounded-b-2xl md:rounded-r-2xl md:rounded-bl-none">
                    <div class="w-14 h-14 sm:w-16 sm:h-16 bg-amber-50 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fas fa-book-open text-2xl sm:text-3xl text-amber-500"></i>
                    </div>
                    <h3 data-i18n="cardCatalog" class="text-base sm:text-lg font-black text-slate-800 uppercase tracking-tight">Catalog</h3>
                    <p class="text-[10px] text-slate-400 mt-2 font-bold uppercase tracking-widest flex items-center" data-i18n="btnDownload">Download <i class="fas fa-angle-down ml-1"></i></p>
                    <div class="dropdown-menu md:absolute top-full left-0 w-full bg-slate-50 md:bg-white md:shadow-2xl border-t border-slate-100 md:border md:border-slate-100 rounded-b-2xl overflow-hidden mt-4 md:mt-1 z-50" id="menu-catalog"></div>
                </div>
            </div>
        </div>

        <!-- Featured Products Slider -->
        <section class="bg-transparent py-10">
            <div class="max-container">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-8 gap-4">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight" data-i18n="homeProductsTitle">Featured Products</h2>
                        <div class="w-16 h-1.5 bg-snap-green rounded-full mt-3 mb-2"></div>
                        <p class="text-slate-500 text-sm font-medium" data-i18n="homeProductsSub">เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด</p>
                    </div>
                    <div class="hidden sm:flex gap-2">
                        <button onclick="scrollSlider('left')" class="w-10 h-10 rounded-xl bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white hover:border-snap-green transition-colors shadow-sm active:scale-95"><i class="fas fa-chevron-left"></i></button>
                        <button onclick="scrollSlider('right')" class="w-10 h-10 rounded-xl bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-snap-green hover:text-white hover:border-snap-green transition-colors shadow-sm active:scale-95"><i class="fas fa-chevron-right"></i></button>
                    </div>
                </div>
                
                <div id="home-product-slider" class="flex gap-4 sm:gap-6 overflow-x-auto snap-x snap-mandatory pb-6 custom-scrollbar px-1 sm:px-2">
                    <!-- Products inject here -->
                </div>
                
                <div class="text-center mt-6">
                    <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-slate-500 font-bold text-xs uppercase tracking-widest hover:text-snap-green transition-colors bg-white px-6 py-3 rounded-full border border-slate-200 hover:border-snap-green shadow-sm w-full sm:w-auto justify-center">
                        <span data-i18n="viewAllProducts">View All Products</span> <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </section>

        <!-- KNOWLEDGE & INSIGHT SECTION -->
        <section class="bg-white py-16 sm:py-24 border-t border-slate-200 mt-10">
            <div class="max-container">
                <div class="flex justify-between items-end mb-10 sm:mb-12">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight">Knowledge & Insight</h2>
                        <div class="w-16 h-1.5 bg-snap-green rounded-full mt-3 mb-2"></div>
                        <p class="text-slate-500 font-medium text-sm" data-i18n="knowledgeSub">บทความเทคนิค คลังความรู้ และวิดีโอจากวิศวกรผู้เชี่ยวชาญ</p>
                    </div>
                </div>
                <div id="article-list" class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
                    <!-- Articles will load here -->
                </div>
            </div>
        </section>
    </div>

    <!-- PAGE: PRODUCT -->
    <div id="page-product" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageProductTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Conveyor Systems</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-8"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6" id="product-grid"></div>
        </div>
    </div>

    <!-- PAGE: SPARE PARTS -->
    <div id="page-spare" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageSpareTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Spare Parts</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-8"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4" id="spare-grid"></div>
        </div>
    </div>

    <!-- PAGE: PROJECT REFERENCE -->
    <div id="page-project" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageProjectTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Project Reference</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-10 sm:mb-12"></div>
            
            <h3 class="text-xl sm:text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <div class="w-10 h-10 bg-emerald-50 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-rocket text-snap-green"></i></div> 
                <span data-i18n="projPilotTitle">Pilot / Demo Project</span>
            </h3>
            <div id="project-pilot-grid" class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 mb-16"></div>
            
            <h3 class="text-xl sm:text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-industry text-blue-500"></i></div>
                <span data-i18n="projUseCaseTitle">Use Case / Application</span>
            </h3>
            <div id="project-usecase-grid" class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6"></div>
        </div>
    </div>

    <!-- PAGE: CART / QUOTATION -->
    <div id="page-cart" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container max-w-4xl py-10">
            <h2 data-i18n="pageCartTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Quotation Request</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-8"></div>
            <div class="bg-white p-4 sm:p-8 rounded-2xl sm:rounded-3xl shadow-sm border border-slate-200">
                <div id="cart-header" class="flex justify-between items-center mb-6 pb-4 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <input type="checkbox" id="cart-select-all" onclick="toggleSelectAll(this.checked)" class="w-5 h-5 accent-snap-green cursor-pointer rounded">
                        <label for="cart-select-all" class="font-bold text-sm cursor-pointer" data-i18n="selectAll">เลือกทั้งหมด</label>
                    </div>
                    <button onclick="deleteSelected()" class="text-red-500 font-bold text-sm hover:bg-red-50 px-3 py-1.5 rounded-lg transition-colors" data-i18n="deleteSelected"><i class="fas fa-trash-alt mr-1"></i> ลบที่เลือก</button>
                </div>
                <div id="cart-items" class="space-y-4 mb-10 max-h-[50vh] overflow-y-auto custom-scrollbar pr-1 sm:pr-2"></div>
                <div id="quote-contact-form" class="bg-slate-50 p-4 sm:p-6 rounded-xl sm:rounded-2xl border border-slate-100 mb-8 hidden">
                    <p class="font-bold text-slate-700 mb-4 uppercase text-xs tracking-widest"><i class="fas fa-info-circle text-snap-green mr-1"></i> <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ</span></p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <input type="text" id="quote-name" data-i18n-placeholder="phGuestName" placeholder="ชื่อ / บริษัท" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green rounded-xl text-sm font-bold text-slate-700 shadow-sm transition-colors">
                        <input type="text" id="quote-contact" data-i18n-placeholder="phGuestContact" placeholder="อีเมล / เบอร์โทร" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green rounded-xl text-sm font-bold text-slate-700 shadow-sm transition-colors">
                    </div>
                </div>
                <div class="flex flex-col sm:flex-row justify-between items-center pt-6 sm:pt-8 border-t border-slate-100 gap-6">
                    <div class="w-full sm:w-auto text-center sm:text-left">
                        <p class="text-slate-500 text-[10px] font-bold uppercase tracking-widest mb-1" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                        <h3 id="cart-total" class="text-4xl sm:text-5xl font-black text-snap-green tracking-tighter">฿0</h3>
                    </div>
                    <button onclick="requestQuote()" class="w-full sm:w-auto bg-snap-black text-white px-10 py-4 font-bold hover:bg-snap-green rounded-xl transition-colors shadow-lg shadow-snap-black/20 uppercase tracking-widest text-sm" data-i18n="btnRequestQuote"><i class="fas fa-paper-plane mr-2"></i> ยื่นขอใบเสนอราคา</button>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: DASHBOARD -->
    <div id="page-dashboard" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">
                <span data-i18n="navDashboard">Dashboard</span> : <span id="dash-user-name" class="text-snap-green"></span>
            </h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-6"></div>
            <p class="text-slate-600 mb-8 text-sm sm:text-base" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6 mb-8">
                <div class="bg-white p-6 sm:p-8 sharp-card lg:col-span-2 flex flex-col justify-center rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm">
                    <h3 class="font-bold text-slate-800 mb-4 sm:mb-6 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
                        <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 sm:py-4 font-bold hover:bg-snap-green-hover rounded-xl text-[10px] sm:text-xs transition-colors shadow-sm"><i class="fas fa-play mb-1 text-base sm:text-lg block"></i> START</button>
                        <button onclick="stopSystem()" id="btn-stop" class="bg-slate-100 text-slate-600 py-3 sm:py-4 font-bold hover:bg-red-500 hover:text-white rounded-xl text-[10px] sm:text-xs transition-colors shadow-sm border border-slate-200 hover:border-red-500"><i class="fas fa-stop mb-1 text-base sm:text-lg block"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-3 sm:py-4 font-bold hover:bg-slate-800 rounded-xl text-[10px] sm:text-xs transition-colors shadow-sm"><i class="fas fa-sync-alt mb-1 text-base sm:text-lg block"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-3 sm:py-4 font-bold hover:bg-blue-700 rounded-xl text-[10px] sm:text-xs transition-colors shadow-sm"><i class="fas fa-file-csv mb-1 text-base sm:text-lg block"></i> REPORT</button>
                    </div>
                </div>
                <div class="bg-white p-6 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm">
                    <h3 class="font-bold text-slate-800 mb-4 sm:mb-6 uppercase text-xs tracking-widest" data-i18n="dashCfgTitle">Configuration</h3>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashTarget">Target</label>
                            <input type="number" id="cfg-target" onchange="updateDashboardConfig()" class="w-20 sm:w-24 text-right outline-none font-black text-slate-800 bg-slate-50 px-2 py-1 rounded">
                        </div>
                        <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashCarbon">Carbon Factor</label>
                            <input type="number" step="0.0001" id="cfg-carbon" onchange="updateDashboardConfig()" class="w-20 sm:w-24 text-right outline-none font-black text-slate-800 bg-slate-50 px-2 py-1 rounded">
                        </div>
                        <div class="flex justify-between items-center">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashEnergy">Energy Factor</label>
                            <input type="number" step="0.001" id="cfg-energy" onchange="updateDashboardConfig()" class="w-20 sm:w-24 text-right outline-none font-black text-slate-800 bg-slate-50 px-2 py-1 rounded">
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 mb-8">
                <div class="bg-white p-6 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-16 h-16 bg-blue-50 rounded-bl-[100px] flex items-top justify-right p-4"><i class="fas fa-box text-blue-500 text-xl opacity-50"></i></div>
                    <p class="text-[10px] text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotOut">Total Output</p>
                    <h3 id="dash-total-output" class="text-4xl sm:text-5xl font-black text-slate-900 tracking-tighter">0</h3>
                </div>
                <div class="bg-white p-6 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-16 h-16 bg-emerald-50 rounded-bl-[100px] flex items-top justify-right p-4"><i class="fas fa-leaf text-emerald-500 text-xl opacity-50"></i></div>
                    <p class="text-[10px] text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashCalCarbon">Cal Carbon</p>
                    <h3 id="dash-carbon" class="text-4xl sm:text-5xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
                <div class="bg-white p-6 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-16 h-16 bg-amber-50 rounded-bl-[100px] flex items-top justify-right p-4"><i class="fas fa-bolt text-amber-500 text-xl opacity-50"></i></div>
                    <p class="text-[10px] text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotPower">Total Power</p>
                    <h3 id="dash-power" class="text-4xl sm:text-5xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
            </div>

            <div class="bg-white p-6 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm mb-8">
                <div class="flex justify-between items-end mb-4">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashPlanTitle">Production Planning</h3>
                    <span id="dash-progress-text" class="text-xl sm:text-2xl font-black text-snap-green">0.0%</span>
                </div>
                <div class="w-full h-4 sm:h-5 bg-slate-100 rounded-full overflow-hidden mb-4 sm:mb-6 border border-slate-200">
                    <div id="dash-progress-bar" class="h-full bg-snap-green transition-all duration-300 relative" style="width: 0%">
                        <div class="absolute inset-0 bg-white/20 w-full h-full" style="background-image: linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent); background-size: 1rem 1rem;"></div>
                    </div>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between gap-2 text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <span><i class="far fa-clock mr-1"></i> <span data-i18n="dashTimeElapsed">Elapsed</span>: <span id="dash-time-elapsed" class="text-slate-800">00:00:00</span></span>
                    <span><i class="fas fa-hourglass-half mr-1"></i> <span data-i18n="dashTimeRemain">ETA</span>: <span id="dash-time-remain" class="text-slate-800">--:--:--</span></span>
                </div>
            </div>

            <div class="bg-white p-4 sm:p-8 sharp-card rounded-2xl sm:rounded-3xl border border-slate-200 shadow-sm">
                <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 pb-4 border-b border-slate-100 gap-4">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashMacStatus2">Machine Status</h3>
                    <div class="flex flex-wrap gap-3 sm:gap-4 text-[9px] sm:text-[10px] font-bold uppercase tracking-widest text-slate-500 bg-slate-50 px-4 py-2 rounded-full w-fit">
                        <span class="flex items-center gap-1.5"><div class="w-2.5 h-2.5 bg-snap-green rounded-full shadow-sm"></div> <span data-i18n="statusNormal">Normal</span></span>
                        <span class="flex items-center gap-1.5"><div class="w-2.5 h-2.5 bg-amber-400 rounded-full shadow-sm"></div> <span data-i18n="statusWarning">Warning</span></span>
                        <span class="flex items-center gap-1.5"><div class="w-2.5 h-2.5 bg-red-500 rounded-full shadow-sm"></div> <span data-i18n="statusMaint">Maint.</span></span>
                    </div>
                </div>
                <div id="dash-nodes-grid" class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-5 xl:grid-cols-10 gap-3 sm:gap-4 max-h-[60vh] overflow-y-auto custom-scrollbar p-1">
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: COMPANY -->
    <div id="page-about" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="navAbout" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Company</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-10"></div>
            
            <div class="grid md:grid-cols-2 gap-8 md:gap-12 items-center mb-16 md:mb-20">
                <div>
                    <h3 class="text-3xl sm:text-4xl md:text-5xl font-black text-snap-black tracking-tighter mb-6 md:mb-8 leading-[1.1]">Driving the future of <br><span class="text-snap-green">industrial automation.</span></h3>
                    <p class="text-slate-500 leading-relaxed mb-6 text-base md:text-lg font-medium" data-i18n="aboutDesc">
                        Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด
                    </p>
                </div>
                <div class="h-64 sm:h-80 md:h-[400px] overflow-hidden relative group rounded-[2rem] shadow-2xl shadow-slate-200">
                    <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-snap-black/60 to-transparent"></div>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-6 md:gap-8">
                <div class="bg-snap-black text-white p-8 md:p-12 border-none rounded-[2rem] relative overflow-hidden group">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-bl-[100px] transition-transform group-hover:scale-110"></div>
                    <i class="fas fa-eye text-4xl md:text-5xl text-snap-green mb-6 md:mb-8 relative z-10 drop-shadow-md"></i>
                    <h4 class="text-2xl md:text-3xl font-black mb-3 md:mb-4 uppercase tracking-wider relative z-10" data-i18n="aboutVisionTitle">Vision</h4>
                    <p class="text-slate-400 leading-relaxed text-base md:text-lg relative z-10 font-medium" data-i18n="aboutVisionDesc">มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้</p>
                </div>
                <div class="bg-snap-green text-white p-8 md:p-12 border-none rounded-[2rem] relative overflow-hidden group shadow-xl shadow-snap-green/20">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-black/10 rounded-bl-[100px] transition-transform group-hover:scale-110"></div>
                    <i class="fas fa-bullseye text-4xl md:text-5xl text-snap-black mb-6 md:mb-8 relative z-10 drop-shadow-md"></i>
                    <h4 class="text-2xl md:text-3xl font-black mb-3 md:mb-4 uppercase tracking-wider text-snap-black relative z-10" data-i18n="aboutMissionTitle">Mission</h4>
                    <p class="text-emerald-900 leading-relaxed text-base md:text-lg font-bold relative z-10" data-i18n="aboutMissionDesc">พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: SUPPORT / CONTACT -->
    <div id="page-contact" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container max-w-5xl py-10">
            <h2 data-i18n="navContact" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Support</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-10"></div>
            
            <div class="grid md:grid-cols-2 gap-8 md:gap-10 items-start">
                <!-- ข้อมูลติดต่อด่วน -->
                <div class="bg-white p-8 md:p-10 text-left rounded-[2rem] shadow-sm h-full border border-slate-200">
                    <div class="w-16 h-16 md:w-20 md:h-20 bg-emerald-50 rounded-2xl flex items-center justify-center mb-6 md:mb-8">
                        <i class="fas fa-headset text-3xl md:text-4xl text-snap-green"></i>
                    </div>
                    <h3 class="text-2xl md:text-3xl font-black text-slate-900 mb-2 md:mb-3 tracking-tight">Technical Support</h3>
                    <p class="text-slate-500 mb-8 md:mb-10 text-sm font-medium" data-i18n="contactSub">ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ พร้อมให้บริการคุณตลอด 24 ชั่วโมง</p>
                    
                    <div class="space-y-3 md:space-y-4 mb-6">
                        <div class="flex items-center gap-4 md:gap-5 bg-slate-50 p-4 md:p-5 rounded-2xl border border-slate-100 hover:border-snap-green hover:shadow-md transition-all cursor-pointer group">
                            <div class="w-10 h-10 md:w-12 md:h-12 bg-white rounded-xl flex items-center justify-center shadow-sm group-hover:bg-snap-green group-hover:text-white transition-colors shrink-0"><i class="fas fa-envelope text-slate-400 group-hover:text-white text-lg md:text-xl"></i></div>
                            <div class="min-w-0">
                                <p class="text-[9px] md:text-[10px] font-bold text-slate-400 uppercase tracking-widest">Email</p>
                                <span class="font-black text-slate-800 text-sm md:text-base truncate block">snapcon1992@gmail.com</span>
                            </div>
                        </div>
                        <div class="flex items-center gap-4 md:gap-5 bg-slate-50 p-4 md:p-5 rounded-2xl border border-slate-100 hover:border-[#00B900] hover:shadow-md transition-all cursor-pointer group">
                            <div class="w-10 h-10 md:w-12 md:h-12 bg-white rounded-xl flex items-center justify-center shadow-sm group-hover:bg-[#00B900] group-hover:text-white transition-colors shrink-0"><i class="fab fa-line text-[#00B900] group-hover:text-white text-xl md:text-2xl"></i></div>
                            <div class="min-w-0">
                                <p class="text-[9px] md:text-[10px] font-bold text-slate-400 uppercase tracking-widest">Line Official</p>
                                <span class="font-black text-slate-800 text-sm md:text-base truncate block">@SnapconAuto</span>
                            </div>
                        </div>
                        <div class="flex items-center gap-4 md:gap-5 bg-slate-50 p-4 md:p-5 rounded-2xl border border-slate-100 hover:border-blue-500 hover:shadow-md transition-all cursor-pointer group">
                            <div class="w-10 h-10 md:w-12 md:h-12 bg-white rounded-xl flex items-center justify-center shadow-sm group-hover:bg-blue-500 group-hover:text-white transition-colors shrink-0"><i class="fas fa-phone-alt text-slate-400 group-hover:text-white text-lg md:text-xl"></i></div>
                            <div class="min-w-0">
                                <p class="text-[9px] md:text-[10px] font-bold text-slate-400 uppercase tracking-widest">Hotline</p>
                                <span class="font-black text-slate-800 text-sm md:text-base truncate block">081-XXX-XXXX</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ฟอร์มติดต่อส่งเข้า Google Sheets -->
                <div class="bg-white p-8 md:p-10 shadow-sm rounded-[2rem] h-full border border-slate-200">
                    <h3 class="text-lg md:text-xl font-black text-slate-900 mb-6 md:mb-8 uppercase tracking-widest flex items-center gap-3">
                        <div class="w-8 h-8 md:w-10 md:h-10 bg-emerald-50 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-paper-plane text-snap-green"></i></div>
                        ส่งข้อความถึงเรา
                    </h3>
                    <div class="space-y-4 md:space-y-6">
                        <div>
                            <label class="block text-[9px] md:text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1.5 md:mb-2 ml-1">ชื่อ-นามสกุล / บริษัท</label>
                            <input type="text" id="contact-name" class="w-full px-4 md:px-5 py-3 md:py-4 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green focus:bg-white transition-colors text-sm font-bold text-slate-700 rounded-xl" placeholder="กรอกชื่อของคุณ">
                        </div>
                        <div>
                            <label class="block text-[9px] md:text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1.5 md:mb-2 ml-1">อีเมล / เบอร์โทรติดต่อกลับ</label>
                            <input type="text" id="contact-info" class="w-full px-4 md:px-5 py-3 md:py-4 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green focus:bg-white transition-colors text-sm font-bold text-slate-700 rounded-xl" placeholder="กรอกข้อมูลติดต่อกลับ">
                        </div>
                        <div>
                            <label class="block text-[9px] md:text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1.5 md:mb-2 ml-1">รายละเอียด / คำถาม</label>
                            <textarea id="contact-message" rows="4" class="w-full px-4 md:px-5 py-3 md:py-4 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green focus:bg-white transition-colors text-sm font-bold text-slate-700 rounded-xl custom-scrollbar" placeholder="พิมพ์ข้อความของคุณที่นี่..."></textarea>
                        </div>
                        <button onclick="submitContactForm()" class="w-full bg-snap-black text-white px-6 md:px-8 py-4 font-bold hover:bg-snap-green text-xs md:text-sm transition-all rounded-xl mt-2 shadow-lg shadow-snap-black/20 uppercase tracking-widest">
                            SEND MESSAGE
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL: REGISTER -->
    <div id="modal-register" class="fixed inset-0 bg-snap-black/90 backdrop-blur-sm z-[200] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md shadow-2xl relative p-6 sm:p-10 rounded-[2rem] max-h-[90vh] overflow-y-auto custom-scrollbar">
            <button onclick="closeRegisterModal()" class="absolute top-4 right-4 sm:top-5 sm:right-5 w-8 h-8 sm:w-10 sm:h-10 bg-slate-50 hover:bg-red-50 text-slate-400 hover:text-red-500 rounded-full flex items-center justify-center transition-colors text-base sm:text-lg focus:outline-none"><i class="fas fa-times"></i></button>
            
            <div class="w-12 h-12 sm:w-16 sm:h-16 bg-emerald-50 rounded-xl sm:rounded-2xl flex items-center justify-center mb-4 sm:mb-6 mx-auto sm:mx-0">
                <i class="fas fa-user-plus text-2xl sm:text-3xl text-snap-green"></i>
            </div>
            <h3 class="text-xl sm:text-2xl font-black text-slate-900 uppercase mb-2 tracking-tight text-center sm:text-left" data-i18n="regTitle">CREATE ACCOUNT</h3>
            <p class="text-slate-500 text-xs sm:text-sm font-medium mb-6 sm:mb-8 text-center sm:text-left">ลงทะเบียนเพื่อเข้าถึงระบบ Dashboard และขอใบเสนอราคา</p>
            
            <div class="space-y-3 sm:space-y-4">
                <div class="relative">
                    <i class="fas fa-user absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"></i>
                    <input type="text" id="reg-id" data-i18n-placeholder="regId" placeholder="User ID" class="w-full pl-10 sm:pl-12 pr-4 py-3 sm:py-4 border border-slate-200 rounded-xl outline-none focus:border-snap-green focus:bg-white bg-slate-50 text-sm font-bold transition-colors">
                </div>
                <div class="relative">
                    <i class="fas fa-lock absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"></i>
                    <input type="password" id="reg-pass" data-i18n-placeholder="regPass" placeholder="Password" class="w-full pl-10 sm:pl-12 pr-4 py-3 sm:py-4 border border-slate-200 rounded-xl outline-none focus:border-snap-green focus:bg-white bg-slate-50 text-sm font-bold transition-colors">
                </div>
                <div class="h-px w-full bg-slate-100 my-2"></div>
                <div class="relative">
                    <i class="fas fa-building absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"></i>
                    <input type="text" id="reg-name" data-i18n-placeholder="regName" placeholder="Name / Company" class="w-full pl-10 sm:pl-12 pr-4 py-3 sm:py-4 border border-slate-200 rounded-xl outline-none focus:border-snap-green focus:bg-white bg-slate-50 text-sm font-bold transition-colors">
                </div>
                <div class="relative">
                    <i class="fas fa-envelope absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"></i>
                    <input type="text" id="reg-contact" data-i18n-placeholder="regContact" placeholder="Email / Phone" class="w-full pl-10 sm:pl-12 pr-4 py-3 sm:py-4 border border-slate-200 rounded-xl outline-none focus:border-snap-green focus:bg-white bg-slate-50 text-sm font-bold transition-colors">
                </div>
                <button onclick="submitRegistration()" class="w-full bg-snap-green text-white py-3.5 sm:py-4.5 font-bold hover:bg-snap-green-hover rounded-xl uppercase tracking-widest mt-4 shadow-lg shadow-snap-green/30 transition-all active:scale-95 text-xs sm:text-sm" data-i18n="btnSubmitReg">CONFIRM REGISTRATION</button>
            </div>
        </div>
    </div>

    <script>
        // =========================================================================
        // JAVASCRIPT SYSTEM (STABLE & BULLETPROOF VERSION)
        // =========================================================================
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxaV4oNSs0eWV5TOsVU9Ky8pl08d7f8H4L98vb1-ZLFQn95q4Kiy15ZqC34hrKoziYl/exec';
        
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [], products = [], spares = [], documents = [], projects = [], articles = [], allItems = [];
        
        let currentUserId = null, memoryUsers = { '001': '123', 'admin': 'admin' };
        let activeDashInterval = null;

        // ดักจับ Error กะทันหัน ป้องกันระบบค้าง
        window.onerror = function(message, source, lineno, colno, error) {
            console.log("System Caught an Error: ", message);
            return true; // ป้องกันบราวเซอร์ขึ้นหน้าแดง
        };

        // Mobile Menu Toggle
        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            if (menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
                menu.classList.add('flex');
                document.body.style.overflow = 'hidden'; 
            } else {
                menu.classList.add('hidden');
                menu.classList.remove('flex');
                document.body.style.overflow = '';
            }
        }

        // Slider Function (ฟังก์ชันที่หายไปก่อนหน้า ตอนนี้เพิ่มให้แล้วครับ)
        function scrollSlider(dir) {
            const slider = document.getElementById('home-product-slider');
            if (slider) {
                const scrollAmount = window.innerWidth > 768 ? 320 : 260;
                slider.scrollBy({ left: dir === 'left' ? -scrollAmount : scrollAmount, behavior: 'smooth' });
            }
        }

        // -------------------------------------------------------------------------
        // DICTIONARY FOR i18n
        // -------------------------------------------------------------------------
        const dict = {
            th: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company", navHome: "Home",
                navLogin: "เข้าสู่ระบบ (Login)", navRegister: "สมัครสมาชิก", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", 
                heroDesc: "เปลี่ยนความซับซ้อนให้เป็นเรื่องง่าย ด้วยระบบออโตเมชัน Plug & Play ที่พร้อมให้คุณควบคุมสายการผลิตได้ทันที",
                heroLink: "ดูสินค้าทั้งหมด",
                
                fs1Title: "⚡ Easy Setup (Plug & Play)", fs1Desc: "ติดตั้งง่าย ใช้งานได้ทันที",
                fs2Title: "📊 Real-Time Monitoring", fs2Desc: "แสดงผลแบบเรียลไทม์ เห็นข้อมูลทันที",
                fs3Title: "🎛 Centralized Control", fs3Desc: "ควบคุมทุกเครื่องจักรจากจุดเดียว",
                fs4Title: "🛡 Built-in Poka-Yoke", fs4Desc: "ระบบกันพลาดในตัว ป้องกันความผิดพลาดอัตโนมัติ",
                fs5Title: "☁️ Cloud Ready", fs5Desc: "รองรับการเชื่อมต่อ Cloud พร้อมใช้งาน",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", cardCatalog: "Catalog", btnDownload: "Download",
                
                homeProductsTitle: "Featured Products", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด", viewAllProducts: "View All Products",
                knowledgeSub: "บทความเทคนิค คลังความรู้ และวิดีโอจากวิศวกรผู้เชี่ยวชาญ",
                
                pageProductTitle: "Conveyor Systems", pageSpareTitle: "Spare Parts", 
                pageProjectTitle: "Project Reference", projPilotTitle: "Pilot / Demo Project", projUseCaseTitle: "Use Case / Application",
                
                pageCartTitle: "Quotation Request", cartEmpty: "ไม่มีสินค้าในรถเข็น",
                cartTotalLabel: "ราคากลางประเมินรวม", btnRequestQuote: "ยื่นขอใบเสนอราคา", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก",
                guestContactTitle: "ข้อมูลติดต่อกลับ",
                
                contactSub: "ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ พร้อมให้บริการคุณตลอด 24 ชั่วโมง",
                aboutVisionTitle: "Vision", aboutVisionDesc: "มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้",
                aboutMissionTitle: "Mission", aboutMissionDesc: "พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก",
                aboutDesc: "Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด",
                
                regTitle: "CREATE ACCOUNT", btnSubmitReg: "CONFIRM REGISTRATION",
                phId: "ID", phPass: "PW", phGuestName: "ชื่อ / บริษัท", phGuestContact: "อีเมล / เบอร์โทร",
                regId: "ตั้งรหัส User ID", regPass: "ตั้งรหัส Password", regName: "ชื่อ-นามสกุล / ชื่อบริษัท", regContact: "อีเมล / เบอร์โทรศัพท์",
                
                dashSubTitle: "ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Total Power",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status",
                statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint."
            },
            en: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company", navHome: "Home",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroText1: "Snap to Connect.", heroText2: "Ready to Control.", 
                heroDesc: "Turn complexity into simplicity with Plug & Play automation systems, ready for you to control your production line instantly.",
                heroLink: "View All Products",
                
                fs1Title: "⚡ Easy Setup (Plug & Play)", fs1Desc: "Easy installation, ready to use",
                fs2Title: "📊 Real-Time Monitoring", fs2Desc: "Real-time display, instant data visibility",
                fs3Title: "🎛 Centralized Control", fs3Desc: "Control all machines from a single point",
                fs4Title: "🛡 Built-in Poka-Yoke", fs4Desc: "Built-in mistake-proofing, automatic error prevention",
                fs5Title: "☁️ Cloud Ready", fs5Desc: "Cloud connection supported, ready to use",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", cardCatalog: "Catalog", btnDownload: "Download",
                
                homeProductsTitle: "Featured Products", homeProductsSub: "Explore our latest automation machines and equipment", viewAllProducts: "View All Products",
                knowledgeSub: "Technical articles, knowledge base, and videos from expert engineers",
                
                pageProductTitle: "Conveyor Systems", pageSpareTitle: "Spare Parts", 
                pageProjectTitle: "Project Reference", projPilotTitle: "Pilot / Demo Project", projUseCaseTitle: "Use Case / Application",
                
                pageCartTitle: "Quotation Request", cartEmpty: "Your cart is empty",
                cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "Delete Selected",
                guestContactTitle: "Contact Info",
                
                contactSub: "Official Technical Support & Inquiries, available 24/7.",
                aboutVisionTitle: "Vision", aboutVisionDesc: "To be the leading provider of advanced and accessible Plug & Play automation systems in Southeast Asia.",
                aboutMissionTitle: "Mission", aboutMissionDesc: "Develop innovations that reduce complexity, minimize installation time, and elevate industrial efficiency for global competitiveness.",
                aboutDesc: "Snapcon Automation is a leader in modern industrial technology, focusing on ease of connection and installation through Plug & Play Systems. We are committed to revolutionizing the automation industry with solutions that reduce complexity, save time, and maximize production efficiency.",
                
                regTitle: "CREATE ACCOUNT", btnSubmitReg: "CONFIRM REGISTRATION",
                phId: "ID", phPass: "PW", phGuestName: "Name / Company", phGuestContact: "Email / Phone",
                regId: "Create User ID", regPass: "Create Password", regName: "Full Name / Company Name", regContact: "Email / Phone Number",
                
                dashSubTitle: "Enterprise Monitoring & Predictive Maintenance System",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Total Power",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status",
                statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint."
            }
        };

        function setLanguage(lang) {
            try {
                currentLang = lang;
                document.querySelectorAll('[data-i18n]').forEach(el => {
                    const key = el.getAttribute('data-i18n');
                    if (dict[lang][key]) el.innerHTML = dict[lang][key];
                });
                document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                    const key = el.getAttribute('data-i18n-placeholder');
                    if (dict[lang][key]) el.placeholder = dict[lang][key];
                });
                
                document.getElementById('btn-lang-th').className = lang === 'th' ? "text-xs font-bold text-snap-green transition-colors" : "text-xs font-bold text-slate-400 hover:text-white transition-colors";
                document.getElementById('btn-lang-en').className = lang === 'en' ? "text-xs font-bold text-snap-green transition-colors" : "text-xs font-bold text-slate-400 hover:text-white transition-colors";
                
                renderProjects(); 
                renderArticles(); 
                if(document.getElementById('page-dashboard').classList.contains('page-active')) renderDashboard();
            } catch(e) { console.log(e) }
        }
        
        // -------------------------------------------------------------------------
        function createDefaultDash() {
            return {
                isRunning: false, target: 10000, carbonFactor: 0.0070, energyFactor: 0.015, elapsedSeconds: 0,
                nodes: [
                    { id: 1, name: "Node-01 Main", output: 0, status: 'Offline', health: 100.0, wearRate: 0.3 },
                    { id: 2, name: "Node-02 Sub", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 },
                    { id: 3, name: "Node-03 Pack", output: 0, status: 'Offline', health: 100.0, wearRate: 0.2 },
                    { id: 4, name: "Node-04 Seal", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 },
                    { id: 5, name: "Node-05 Label", output: 0, status: 'Offline', health: 100.0, wearRate: 0.6 }
                ]
            };
        }

        let userDashboards = { '001': createDefaultDash(), 'admin': createDefaultDash() };

        function getDash() {
            if (!currentUserId || !userDashboards[currentUserId]) return null;
            return userDashboards[currentUserId];
        }

        function getValidImageUrl(url) {
            if (!url) return '';
            if (url.includes('drive.google.com/file/d/')) {
                try {
                    const fileId = url.split('/d/')[1].split('/')[0];
                    return `https://drive.google.com/uc?export=view&id=${fileId}`;
                } catch(e) { return url; }
            }
            return url;
        }

        function getEmbedVideoUrl(url) {
            if (!url) return '';
            if (url.includes('drive.google.com/file/d/')) {
                try {
                    const fileId = url.split('/d/')[1].split('/')[0];
                    return `https://drive.google.com/file/d/${fileId}/preview`;
                } catch(e) { return url; }
            }
            if (url.includes('youtube.com/watch?v=')) return url.replace('watch?v=', 'embed/');
            if (url.length === 11 && !url.includes('/')) return `https://www.youtube.com/embed/${url}`;
            return url;
        }

        function normalizeKeys(arr) {
            if (!arr || arr.length === 0) return [];
            return arr.map(obj => {
                const newObj = {};
                for (let key in obj) {
                    const cleanKey = key.toLowerCase().replace(/[\s_]+/g, '');
                    newObj[cleanKey] = obj[key];
                }
                return newObj;
            });
        }

        async function loadDataFromSheet() {
            try {
                console.log("Fetching data from Google Sheets...");
                const response = await fetch(GOOGLE_SCRIPT_URL + "?t=" + Date.now());
                if (!response.ok) throw new Error("Network response was not ok");
                const data = await response.json();
                
                products = normalizeKeys(data.products);
                spares = normalizeKeys(data.spares);
                documents = normalizeKeys(data.documents);
                projects = normalizeKeys(data.projects);
                articles = normalizeKeys(data.articles);
                allItems = [...products, ...spares];
                
                try { renderProducts(); } catch(e) {}
                try { renderDocuments(); } catch(e) {}
                try { renderProjects(); } catch(e) {}
                try { renderArticles(); } catch(e) {}
                if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
                
            } catch (e) { console.log("Fetch Warning (Using Local Fallback):", e); }
        }

        function renderProducts() {
            const pGrid = document.getElementById('product-grid');
            const sGrid = document.getElementById('spare-grid');
            const slider = document.getElementById('home-product-slider');

            const makeCard = (p) => {
                // 1. จัดการข้อมูลรายละเอียดสินค้า (Specs) ให้ออกมาเป็น Array
                let specArray = [];
                if (currentLang === 'th') specArray = p.specsth || p.specs_th || p.specs || [];
                else specArray = p.specsen || p.specs_en || p.specs || [];
                
                // 2. Fallback: ถ้าไม่มีคอลัมน์ Specs ให้ลองดึงคอลัมน์ Description แทน
                if (!specArray || specArray.length === 0) {
                    const desc = currentLang === 'th' ? (p.descriptionth || p.description) : (p.descriptionen || p.description);
                    if (desc) specArray = [desc];
                }
                
                // 3. ทำให้แน่ใจว่าเป็น Array เสมอ (ถ้าใน Sheet พิมพ์คั่นด้วยลูกน้ำ ระบบจะตัดขึ้นบรรทัดใหม่ให้)
                if (!Array.isArray(specArray)) {
                    specArray = typeof specArray === 'string' ? specArray.split(',') : [specArray];
                }

                // 4. สร้าง HTML สำหรับแสดงรายการ Specs พร้อมไอคอนติ๊กถูก
                let specsHtml = '';
                if (specArray.length > 0 && specArray[0] && specArray[0].trim() !== '') {
                    specsHtml = `<div class="mb-4 flex-grow text-[10px] sm:text-xs text-slate-500 space-y-1.5">` + 
                        specArray.map(s => `<div class="truncate border-b border-slate-50 pb-1.5 last:border-0 last:pb-0 font-medium tracking-tight"><i class="fas fa-check text-emerald-400 mr-1.5"></i> ${s.trim()}</div>`).join('') +
                        `</div>`;
                } else {
                    specsHtml = `<div class="mb-4 flex-grow"></div>`; // ดันปุ่มและราคาไปด้านล่างสุดกรณีไม่มีข้อมูล
                }

                return `
                <div class="bg-white sharp-card p-4 sm:p-5 flex flex-col h-full rounded-2xl sm:rounded-[1.5rem] shadow-sm border border-slate-100 hover:shadow-lg transition-all">
                    <div class="bg-slate-50 h-32 sm:h-40 flex items-center justify-center p-3 mb-4 overflow-hidden rounded-xl border border-slate-100 shrink-0">
                        <img src="${getValidImageUrl(p.img || p.imageurl || p.image)}" onerror="this.src='https://via.placeholder.com/200'" class="max-h-full max-w-full object-contain mix-blend-multiply">
                    </div>
                    <h4 class="font-black text-sm sm:text-base text-slate-900 mb-3 line-clamp-2" title="${p.name || p.title}">${p.name || p.title}</h4>
                    
                    ${specsHtml}
                    
                    <div class="mt-auto pt-3 border-t border-slate-50">
                        <p class="text-snap-green font-black text-lg sm:text-xl mb-4">฿${parseFloat(p.price || 0).toLocaleString()}</p>
                        <button onclick="addToCart('${p.id}')" class="w-full bg-slate-50 text-slate-700 py-2.5 sm:py-3 rounded-xl font-bold text-[10px] sm:text-xs hover:bg-snap-green hover:text-white transition-all border border-slate-200 hover:border-transparent active:scale-95 shadow-sm"><i class="fas fa-cart-plus mr-1"></i> ADD TO CART</button>
                    </div>
                </div>`;
            };

            if(pGrid) pGrid.innerHTML = products.map(makeCard).join('');
            if(sGrid) sGrid.innerHTML = spares.map(makeCard).join('');
            if(slider) slider.innerHTML = products.slice(0, 10).map(p => `
                <div onclick="navigate('product')" class="min-w-[220px] sm:min-w-[280px] snap-center bg-white border border-slate-100 p-4 sm:p-5 rounded-[1.5rem] shadow-sm hover:shadow-xl transition-all cursor-pointer">
                    <div class="overflow-hidden rounded-xl mb-4 relative h-28 sm:h-36 bg-slate-50 border border-slate-100"><img src="${getValidImageUrl(p.img || p.imageurl || p.image)}" class="w-full h-full object-contain mix-blend-multiply p-2 sm:p-3"></div>
                    <h4 class="font-black text-[13px] sm:text-[15px] text-slate-800 mb-1 truncate">${p.name || p.title}</h4>
                    <p class="text-snap-green font-black text-base sm:text-lg mt-auto">฿${parseFloat(p.price || 0).toLocaleString()}</p>
                </div>`).join('');
        }

        function renderProjects() {
            const pilotGrid = document.getElementById('project-pilot-grid');
            const usecaseGrid = document.getElementById('project-usecase-grid');

            if (pilotGrid) {
                const pilots = projects.filter(p => (p.category||'').toLowerCase().includes('pilot'));
                pilotGrid.innerHTML = pilots.map(p => {
                    let visual = '<i class="fas fa-cogs text-snap-green text-3xl sm:text-4xl"></i>';
                    let imgSrc = getValidImageUrl(p.imgurl || p.img || p.icon);
                    if (imgSrc && imgSrc.includes('http')) {
                        visual = `<img src="${imgSrc}" class="w-full h-full object-contain p-2">`;
                    } else if (p.icon && !p.icon.includes('http')) {
                        visual = `<i class="${p.icon} text-3xl sm:text-4xl text-snap-green"></i>`;
                    }
                    const desc = currentLang === 'th' ? (p.descriptionth || p.description) : (p.descriptionen || p.description);

                    return `
                    <div class="bg-slate-50 p-6 sm:p-8 sharp-card border border-slate-100 rounded-[2rem] group flex flex-col items-start h-full">
                        <div class="w-16 h-16 sm:w-20 sm:h-20 bg-white border border-slate-200 rounded-2xl flex items-center justify-center mb-6 sm:mb-8 shadow-sm overflow-hidden shrink-0 group-hover:scale-110 transition-transform">
                            ${visual}
                        </div>
                        <h4 class="text-lg sm:text-xl font-black text-slate-900 mb-2 sm:mb-3 leading-tight">${p.title || 'Untitled'}</h4>
                        <p class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">${desc || ''}</p>
                    </div>`;
                }).join('') || '<p class="col-span-full text-slate-400 font-bold bg-slate-50 p-8 rounded-2xl text-center">ไม่มีข้อมูล (No Pilot Projects)</p>';
            }

            if (usecaseGrid) {
                const usecases = projects.filter(p => (p.category||'').toLowerCase().includes('usecase'));
                usecaseGrid.innerHTML = usecases.map((p, idx) => {
                    let borderCol = ['border-t-amber-500', 'border-t-snap-green', 'border-t-blue-500'][idx % 3];
                    let imgSrc = getValidImageUrl(p.imgurl || p.img || p.icon);
                    if(!imgSrc || !imgSrc.includes('http')) imgSrc = 'https://images.unsplash.com/photo-1589792923962-537704632910?auto=format&fit=crop&w=600&q=80';
                    const desc = currentLang === 'th' ? (p.descriptionth || p.description) : (p.descriptionen || p.description);

                    return `
                    <div class="bg-white p-6 sm:p-8 sharp-card rounded-[2rem] shadow-sm border-t-[6px] ${borderCol} flex flex-col items-center text-center h-full">
                        <div class="w-full h-36 sm:h-44 bg-slate-100 rounded-2xl mb-6 sm:mb-8 overflow-hidden flex items-center justify-center">
                            <img src="${imgSrc}" class="w-full h-full object-cover mix-blend-multiply opacity-90 hover:scale-110 transition-transform duration-500">
                        </div>
                        <h4 class="text-lg sm:text-xl font-black text-slate-900 mb-2 sm:mb-3 leading-tight">${p.title || 'Untitled'}</h4>
                        <p class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">${desc || ''}</p>
                    </div>`;
                }).join('') || '<p class="col-span-full text-slate-400 font-bold bg-slate-50 p-8 rounded-2xl text-center">ไม่มีข้อมูล (No Use Cases)</p>';
            }
        }

        function renderArticles() {
            const container = document.getElementById('article-list');
            if (!container) return;
            if (!articles || articles.length === 0) {
                container.innerHTML = '<p class="col-span-full text-center text-slate-400 font-bold bg-white border border-slate-100 py-10 rounded-2xl">กำลังอัปเดตบทความใหม่เร็วๆ นี้...</p>';
                return;
            }
            
            container.innerHTML = articles.map(art => {
                let mediaHtml = '';
                const vid1 = art.video1 || art.youtube1 || art.video;
                const vid2 = art.video2 || art.youtube2;

                if (vid1) {
                    const embed1 = getEmbedVideoUrl(vid1);
                    mediaHtml += `<div class="aspect-video mb-4"><iframe class="w-full h-full rounded-2xl shadow-sm border border-slate-100" src="${embed1}" frameborder="0" allowfullscreen></iframe></div>`;
                }
                if (vid2) {
                    const embed2 = getEmbedVideoUrl(vid2);
                    mediaHtml += `<div class="aspect-video mb-4"><iframe class="w-full h-full rounded-2xl shadow-sm border border-slate-100" src="${embed2}" frameborder="0" allowfullscreen></iframe></div>`;
                }
                
                if (!mediaHtml) {
                    let imgSrc = getValidImageUrl(art.imageurl || art.img || art.image);
                    mediaHtml = `<div class="aspect-video mb-4"><img src="${imgSrc || 'https://via.placeholder.com/400x200'}" class="w-full h-full object-cover rounded-2xl shadow-sm border border-slate-100"></div>`;
                }

                const articleUrl = art.link || art.url || '#';

                return `
                <div class="bg-white border border-slate-100 rounded-[2rem] overflow-hidden shadow-lg shadow-slate-200/50 hover:shadow-xl hover:shadow-snap-green/10 hover:-translate-y-2 transition-all duration-300 flex flex-col h-full group p-3">
                    ${mediaHtml}
                    <div class="p-4 sm:p-6 pt-2 flex flex-col flex-1">
                        <span class="text-emerald-600 bg-emerald-50 self-start px-3 py-1 rounded-lg text-[10px] font-black uppercase tracking-widest mb-3 sm:mb-4">${art.category || 'INSIGHT'}</span>
                        <h3 class="text-lg sm:text-xl font-black text-slate-900 mb-2 sm:mb-3 line-clamp-2 leading-tight group-hover:text-snap-green transition-colors">${art.title || 'Untitled'}</h3>
                        <p class="text-slate-500 text-xs sm:text-sm mb-4 sm:mb-6 line-clamp-2 leading-relaxed font-medium">${art.summary || ''}</p>
                        <div class="mt-auto flex justify-between items-center pt-4 sm:pt-5 border-t border-slate-100">
                            <span class="text-[9px] sm:text-[10px] font-bold text-slate-400 uppercase tracking-widest"><i class="far fa-calendar-alt mr-1"></i> ${art.date || 'Update'}</span>
                            ${articleUrl !== '#' ? `<a href="${articleUrl}" target="_blank" class="bg-slate-900 text-white px-4 sm:px-5 py-2 sm:py-2.5 rounded-xl text-[10px] sm:text-xs font-bold hover:bg-snap-green transition-colors shadow-md active:scale-95">อ่านบทความ</a>` : ''}
                        </div>
                    </div>
                </div>`;
            }).join('');
        }

        function renderDocuments() {
            const makeMenu = (typeStr) => {
                const filteredDocs = documents.filter(d => {
                    const t = (d.type || d.category || '').toLowerCase();
                    if (typeStr === 'drawing') return t.includes('drawing') || t.includes('cad') || t.includes('2d') || t.includes('3d') || t.includes('model');
                    return t.includes(typeStr);
                });
                if (filteredDocs.length === 0) return '<div class="px-6 sm:px-8 py-4 sm:py-6 text-[11px] sm:text-sm text-slate-400 font-medium text-center bg-slate-50">ไม่มีข้อมูล (No Data)</div>';
                
                return filteredDocs.map(d => {
                    const name = d.modelname || d.name || d.model || d.title || 'Untitled Document';
                    const url = d.fileurl || d.link || d.url || d.file || '#'; 
                    if(url === '#' || url === '') return '';
                    return `<a href="${url}" target="_blank" class="block px-6 sm:px-8 py-3 sm:py-4 hover:bg-emerald-50 hover:text-emerald-700 border-b border-slate-100 text-[11px] sm:text-sm font-bold text-slate-700 transition-colors"><i class="fas fa-file-download mr-2 text-slate-400"></i> ${name}</a>`;
                }).join('');
            };

            const ds = document.getElementById('menu-datasheet'); if(ds) ds.innerHTML = makeMenu('datasheet');
            const dw = document.getElementById('menu-drawing'); if(dw) dw.innerHTML = makeMenu('drawing');
            const ca = document.getElementById('menu-catalog'); if(ca) ca.innerHTML = makeMenu('catalog');
        }

        function addToCart(id) {
            const item = allItems.find(i => i.id === id);
            if(item) {
                const existing = cart.find(i => i.id === id);
                if(existing) existing.quantity++; else cart.push({...item, cartId: Date.now().toString(), selected: true, quantity: 1});
                updateBadge(); alert(currentLang === 'th' ? "เพิ่มสินค้าลงตะกร้าแล้ว!" : "Added to cart!");
            }
        }
        function updateBadge() { 
            const b = document.getElementById('cart-badge'); 
            const count = cart.reduce((s,i)=>s+i.quantity,0); 
            b.innerText=count>99?'99+':count; 
            b.classList.toggle('hidden',count===0); 
        }
        function updateQuantity(cartId, delta) { const item = cart.find(i => i.cartId === cartId); if(item) { item.quantity = Math.max(1, item.quantity + delta); renderCart(); updateBadge(); } }
        function toggleItem(cartId) { const item = cart.find(i => i.cartId === cartId); if(item) { item.selected = !item.selected; renderCart(); } }
        function toggleSelectAll(val) { cart.forEach(i => i.selected = val); renderCart(); }
        function deleteSelected() { cart = cart.filter(i => !i.selected); updateBadge(); renderCart(); }

        function renderCart() {
            const container = document.getElementById('cart-items'); 
            const quoteForm = document.getElementById('quote-contact-form');
            if(!container) return;
            
            if (quoteForm) quoteForm.classList.remove('hidden');

            if(cart.length === 0) {
                container.innerHTML = `<p class="text-center py-10 text-slate-400 font-bold bg-slate-50 border border-slate-100 rounded-xl">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0'; return;
            }
            container.innerHTML = cart.map(item => `
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center bg-white border border-slate-200 p-4 sm:p-5 rounded-xl mb-3 shadow-sm gap-4">
                    <div class="flex items-center gap-3 sm:gap-5 w-full sm:w-auto flex-1">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleItem('${item.cartId}')" class="w-5 h-5 sm:w-6 sm:h-6 accent-snap-green cursor-pointer rounded">
                        <div class="w-14 h-14 sm:w-16 sm:h-16 bg-white border border-slate-100 rounded-lg flex items-center justify-center shrink-0 p-1"><img src="${getValidImageUrl(item.img || item.imageurl)}" class="max-w-full max-h-full object-contain"></div>
                        <div class="flex-1 min-w-0"><span class="font-black text-slate-900 text-sm sm:text-base block truncate">${item.name || item.title}</span><span class="text-[10px] sm:text-xs text-slate-400 font-bold">${item.id}</span></div>
                    </div>
                    <div class="flex items-center justify-between w-full sm:w-auto gap-4 mt-2 sm:mt-0">
                        <div class="flex items-center border border-slate-200 rounded-lg overflow-hidden h-9 sm:h-10 bg-white">
                            <button onclick="updateQuantity('${item.cartId}', -1)" class="w-8 sm:w-10 h-full bg-slate-50 hover:bg-slate-100 font-black border-r border-slate-200 transition-colors">-</button>
                            <span class="w-10 sm:w-12 h-full flex items-center justify-center text-xs sm:text-sm font-black">${item.quantity}</span>
                            <button onclick="updateQuantity('${item.cartId}', 1)" class="w-8 sm:w-10 h-full bg-slate-50 hover:bg-slate-100 font-black border-l border-slate-200 transition-colors">+</button>
                        </div>
                        <span class="font-black text-slate-900 text-lg sm:text-xl w-24 sm:w-32 text-right shrink-0">฿${(parseFloat(item.price||0) * item.quantity).toLocaleString()}</span>
                    </div>
                </div>`).join('');
            
            const total = cart.filter(i => i.selected).reduce((s, i) => s + (parseFloat(i.price||0) * i.quantity), 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
            document.getElementById('cart-select-all').checked = cart.length > 0 && cart.every(i => i.selected);
        }

        // ==========================================
        // 🚀 FIRE AND FORGET SYNC SYSTEM 
        // ==========================================
        function sendDataToServer(payloadObj) {
            setTimeout(() => {
                fetch(GOOGLE_SCRIPT_URL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                    body: JSON.stringify(payloadObj)
                }).catch(e => console.log("Sync done"));
            }, 100);
        }

        function requestQuote() {
            try {
                const selected = cart.filter(i => i.selected);
                if(selected.length === 0) return alert(currentLang === 'th' ? "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น" : "Please select at least 1 item");
                
                const name = document.getElementById('quote-name').value.trim();
                const info = document.getElementById('quote-contact').value.trim();
                if(!name || !info) return alert(currentLang === 'th' ? "กรุณากรอกชื่อและข้อมูลติดต่อกลับให้ครบถ้วน" : "Please fill your contact info");
                
                const detailsStr = selected.map(i => `- ${i.name||i.title} x${i.quantity} (฿${(parseFloat(i.price||0) * i.quantity).toLocaleString()})`).join('\\n');
                const total = selected.reduce((s, i) => s + (parseFloat(i.price||0) * i.quantity), 0);
                const fullDetails = `Items:\\n${detailsStr}\\n\\nTotal: ฿${total.toLocaleString()}`;
                
                alert(currentLang === 'th' ? "ส่งข้อมูลขอใบเสนอราคาสำเร็จ! ทางเราจะรีบติดต่อกลับครับ" : "Quotation request submitted! We will contact you soon.");
                cart = cart.filter(i => !i.selected); 
                updateBadge(); 
                renderCart(); 
                navigate('home');

                sendDataToServer({ type: "Quotation", name_or_id: name, email: info, details: fullDetails });
            } catch(e) { console.log(e); }
        }

        function submitRegistration() {
            try {
                const id = document.getElementById('reg-id').value.trim();
                const pass = document.getElementById('reg-pass').value.trim();
                const name = document.getElementById('reg-name').value.trim();
                const contact = document.getElementById('reg-contact').value.trim();
                
                if(!id || !pass || !name || !contact) return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบถ้วน" : "Please fill all fields");
                
                memoryUsers[id] = pass;
                isLoggedIn = true;
                currentUserId = id;
                if (!userDashboards[id]) userDashboards[id] = createDefaultDash();
                
                document.getElementById('displayUser').innerText = id;
                document.getElementById('dash-user-name').innerText = id; 
                
                const loginSec = document.getElementById('login-section');
                const userSec = document.getElementById('user-section');
                loginSec.className = "hidden lg:flex items-center gap-2";
                userSec.className = "flex items-center gap-3";
                
                closeRegisterModal();
                document.getElementById('reg-id').value = '';
                document.getElementById('reg-pass').value = '';
                document.getElementById('reg-name').value = '';
                document.getElementById('reg-contact').value = '';

                alert(currentLang === 'th' ? "ลงทะเบียนสำเร็จ! ระบบพาคุณเข้าสู่ระบบอัตโนมัติแล้ว" : "Registration complete! You are now logged in.");
                
                const mobileMenu = document.getElementById('mobile-menu');
                if(!mobileMenu.classList.contains('hidden')) toggleMobileMenu();

                sendDataToServer({ type: "Registration", name_or_id: id, email: contact, details: name });
            } catch(e) { console.log(e); }
        }

        function handleLogin() { 
            try {
                const id = document.getElementById('userId').value.trim() || document.getElementById('mobile-userId').value.trim();
                const pass = document.getElementById('userPass').value.trim() || document.getElementById('mobile-userPass').value.trim();
                
                if(!id || !pass) return alert(currentLang === 'th' ? "กรุณากรอก ID และ Password" : "Please fill ID and Password");

                if (memoryUsers[id] === pass) {
                    isLoggedIn = true; currentUserId = id;
                    if (!userDashboards[id]) userDashboards[id] = createDefaultDash();
                    
                    document.getElementById('displayUser').innerText = id;
                    document.getElementById('dash-user-name').innerText = id; 
                    
                    document.getElementById('login-section').className = "hidden lg:flex items-center gap-2";
                    document.getElementById('user-section').className = "flex items-center gap-3";
                    
                    document.getElementById('mobile-displayUser').innerText = id;
                    document.getElementById('mobile-login-section').className = "hidden";
                    document.getElementById('mobile-user-section').className = "flex flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full";
                    
                    document.getElementById('userId').value = ''; document.getElementById('userPass').value = '';
                    document.getElementById('mobile-userId').value = ''; document.getElementById('mobile-userPass').value = '';
                    
                    alert(currentLang === 'th' ? "เข้าสู่ระบบสำเร็จ!" : "Login Successful");
                    
                    const mobileMenu = document.getElementById('mobile-menu');
                    if(!mobileMenu.classList.contains('hidden')) toggleMobileMenu();
                } else alert(currentLang === 'th' ? "ID หรือรหัสผ่านไม่ถูกต้อง" : "Invalid ID or Password");
            } catch(e) { console.log(e); }
        }

        function handleLogout() { 
            try {
                if (currentUserId) stopSystem();
                isLoggedIn = false; currentUserId = null; 
                
                document.getElementById('user-section').className = "hidden lg:hidden items-center gap-3 pr-5";
                document.getElementById('login-section').className = "hidden lg:flex items-center gap-2 pr-5";
                
                document.getElementById('mobile-user-section').className = "hidden";
                document.getElementById('mobile-login-section').className = "flex flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full";
                
                navigate('home'); 
                
                const mobileMenu = document.getElementById('mobile-menu');
                if(!mobileMenu.classList.contains('hidden')) toggleMobileMenu();
            } catch(e) { console.log(e); }
        }

        function submitContactForm() {
            try {
                const name = document.getElementById('contact-name').value.trim();
                const info = document.getElementById('contact-info').value.trim();
                const msg = document.getElementById('contact-message').value.trim();

                if(!name || !info || !msg) return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบถ้วนก่อนส่งข้อความ" : "Please fill all fields");

                alert(currentLang === 'th' ? "ส่งข้อความสำเร็จ! ทีมงานเทคนิคจะรีบติดต่อกลับครับ" : "Message sent! We will contact you soon.");
                document.getElementById('contact-name').value = '';
                document.getElementById('contact-info').value = '';
                document.getElementById('contact-message').value = '';

                sendDataToServer({ type: "Contact Support", name_or_id: name, email: info, details: msg });
            } catch(e) { console.log(e); }
        }

        // ==========================================
        // 8. DASHBOARD LOGIC
        // ==========================================
        function startSystem() {
            let dash = getDash(); if(!dash) return;
            dash.isRunning = true;
            dash.nodes.forEach(n => { if(n.health > 30) n.status = 'Running'; else n.status = 'Maintenance'; });
            if(!activeDashInterval) activeDashInterval = setInterval(simulateProduction, 500);
            renderDashboard();
        }
        function stopSystem() {
            let dash = getDash(); if(!dash) return;
            dash.isRunning = false;
            dash.nodes.forEach(n => { if(n.status !== 'Maintenance') n.status = 'Stopped'; });
            if(activeDashInterval) { clearInterval(activeDashInterval); activeDashInterval = null; }
            renderDashboard();
        }
        function resetSystem() { 
            let dash = getDash(); if(!dash) return;
            dash.nodes.forEach(n => { n.output = 0; n.health = 100.0; n.status = dash.isRunning ? 'Running' : 'Offline'; }); 
            dash.elapsedSeconds = 0; renderDashboard(); 
        }
        function updateDashboardConfig() {
            let dash = getDash(); if(!dash) return;
            dash.target = parseInt(document.getElementById('cfg-target').value) || 1;
            dash.carbonFactor = parseFloat(document.getElementById('cfg-carbon').value) || 0;
            dash.energyFactor = parseFloat(document.getElementById('cfg-energy').value) || 0;
            renderDashboard();
        }
        function simulateProduction() {
            let dash = getDash(); if(!dash || !dash.isRunning) return;
            dash.elapsedSeconds += 0.5;
            dash.nodes.forEach(n => { 
                if(n.status === 'Running' || n.status === 'Warning') {
                    if(Math.random() > 0.5) { n.output += 1; n.health -= n.wearRate; if(n.health < 0) n.health = 0; }
                    if(n.health <= 30) n.status = 'Maintenance'; else if (n.health <= 70) n.status = 'Warning';
                }
            });
            if(document.getElementById('page-dashboard').classList.contains('page-active')) {
                renderDashboard();
            }
        }
        function exportCSV() {
            let dash = getDash(); if(!dash) return;
            let bom = "\uFEFF";
            let csvContent = bom + "Node ID,Machine Name,Status,Output (Units),Health (%),Est. Carbon (kgCO2e),Est. Power (kWh)\\n";
            let totalOut = 0;
            dash.nodes.forEach(n => {
                let c = (n.output * dash.carbonFactor).toFixed(4); let e = (n.output * dash.energyFactor).toFixed(4); totalOut += n.output;
                csvContent += `${n.id},${n.name},${n.status},${n.output},${n.health.toFixed(2)},${c},${e}\\n`;
            });
            csvContent += `\\nTOTAL,, ,${totalOut},-,${(totalOut * dash.carbonFactor).toFixed(4)},${(totalOut * dash.energyFactor).toFixed(4)}\\n`;
            
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement("a"); link.href = URL.createObjectURL(blob); link.download = `Snapcon_Report_${currentUserId}.csv`; link.click();
        }
        function formatTimeStr(totalSecs) {
            if (!isFinite(totalSecs) || totalSecs < 0) return "--:--:--";
            const h = Math.floor(totalSecs / 3600); const m = Math.floor((totalSecs % 3600) / 60); const s = Math.floor(totalSecs % 60);
            return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        }
        function renderDashboard() {
            try {
                const grid = document.getElementById('dash-nodes-grid'); if(!grid) return;
                let dash = getDash(); if (!dash) return;

                const cfgTarget = document.getElementById('cfg-target');
                const cfgCarbon = document.getElementById('cfg-carbon');
                const cfgEnergy = document.getElementById('cfg-energy');
                if (cfgTarget) cfgTarget.value = dash.target;
                if (cfgCarbon) cfgCarbon.value = dash.carbonFactor;
                if (cfgEnergy) cfgEnergy.value = dash.energyFactor;

                const totalOutput = dash.nodes.reduce((sum, n) => sum + n.output, 0);
                
                const dashTotalOutput = document.getElementById('dash-total-output');
                const dashCarbon = document.getElementById('dash-carbon');
                const dashPower = document.getElementById('dash-power');
                
                if(dashTotalOutput) dashTotalOutput.innerText = totalOutput.toLocaleString();
                if(dashCarbon) dashCarbon.innerText = (totalOutput * dash.carbonFactor).toFixed(2);
                if(dashPower) dashPower.innerText = (totalOutput * dash.energyFactor).toFixed(2);
                
                let progress = dash.target > 0 ? (totalOutput / dash.target) * 100 : 0; 
                if(progress > 100) progress = 100;
                
                const dashProgressBar = document.getElementById('dash-progress-bar');
                const dashProgressText = document.getElementById('dash-progress-text');
                if(dashProgressBar) dashProgressBar.style.width = `${progress}%`;
                if(dashProgressText) dashProgressText.innerText = `${progress.toFixed(1)}%`;
                
                let elapsedStr = formatTimeStr(dash.elapsedSeconds), remainStr = "--:--:--";
                if (totalOutput > 0 && dash.elapsedSeconds > 0) {
                    let ups = totalOutput / dash.elapsedSeconds, remainUnits = dash.target - totalOutput;
                    if (remainUnits > 0 && ups > 0) remainStr = formatTimeStr(remainUnits / ups); else if (remainUnits <= 0) remainStr = "00:00:00";
                }
                
                const dashTimeElapsed = document.getElementById('dash-time-elapsed');
                const dashTimeRemain = document.getElementById('dash-time-remain');
                if(dashTimeElapsed) dashTimeElapsed.innerText = elapsedStr;
                if(dashTimeRemain) dashTimeRemain.innerText = remainStr;

                grid.innerHTML = dash.nodes.map(n => {
                    const isRun = n.status === 'Running', isWarn = n.status === 'Warning', isMaint = n.status === 'Maintenance';
                    let dotBg = 'bg-slate-300';
                    if (isRun) dotBg = 'bg-snap-green animate-pulse'; else if (isWarn) dotBg = 'bg-amber-400 animate-pulse'; else if (isMaint) dotBg = 'bg-red-500';
                    let healthBarCol = n.health > 70 ? 'bg-snap-green' : (n.health > 30 ? 'bg-amber-400' : 'bg-red-500');
                    
                    return `
                    <div class="bg-slate-50 border border-slate-200 p-2 sm:p-3 rounded-xl shadow-sm flex flex-col justify-between h-full">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-[9px] sm:text-[10px] font-bold text-slate-500 truncate" title="${n.name}">${n.name}</span>
                            <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full ${dotBg} shrink-0"></div>
                        </div>
                        <h4 class="text-lg sm:text-xl font-black text-slate-800 text-center my-1 sm:my-2">${n.output}</h4>
                        <div>
                            <div class="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden mt-1">
                                <div class="h-full ${healthBarCol} transition-all duration-500" style="width: ${n.health}%"></div>
                            </div>
                            <p class="text-[8px] sm:text-[9px] text-center mt-1 text-slate-400 font-bold uppercase tracking-widest">Health: ${n.health.toFixed(1)}%</p>
                        </div>
                    </div>`;
                }).join('');
            } catch(e) { console.log(e); }
        }

        function navigate(p) { 
            document.querySelectorAll('.page-section').forEach(s => s.classList.remove('page-active')); 
            const t = document.getElementById('page-'+p); 
            if(t) t.classList.add('page-active'); 
            window.scrollTo(0,0); 
            if(p==='cart') renderCart(); 
            if(p==='dashboard') renderDashboard(); 
        }
        function openRegisterModal() { document.getElementById('modal-register').classList.replace('hidden', 'flex'); }
        function closeRegisterModal() { document.getElementById('modal-register').classList.replace('flex', 'hidden'); }
        function checkDashboardAuth() { 
            if (isLoggedIn) navigate('dashboard'); 
            else { alert(currentLang === 'th' ? "กรุณาเข้าสู่ระบบก่อนเข้าใช้งาน Dashboard" : "Please Login First to access Dashboard"); document.getElementById('userId').focus(); } 
        }

        window.onload = () => {
            try {
                loadDataFromSheet();
                setTimeout(() => setLanguage('th'), 100);
            } catch(e) { console.log(e); }
        };
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2500, scrolling=True)
