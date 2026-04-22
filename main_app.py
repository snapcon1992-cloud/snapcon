import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
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

        /* Document Tab Animation */
        .tab-content { display: none; animation: slideDown 0.3s ease-out forwards; }
        .tab-content.active { display: block; }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
        .doc-btn.active { background-color: #f8fafc; border-color: #00B36E; color: #00B36E; }
    </style>
</head>
<body class="font-sans text-slate-800">

    <nav class="bg-snap-black h-[75px] w-full fixed top-0 z-[999] flex items-center justify-between px-4 md:px-10 shadow-md">
        <div class="flex flex-col leading-none cursor-pointer shrink-0" onclick="navigate('home')">
            <span class="font-black text-2xl md:text-3xl text-snap-green tracking-tighter">SNAPCON</span>
            <span class="text-[8px] md:text-[10px] text-white font-bold tracking-[0.3em] ml-0.5 opacity-80 uppercase">Automation</span>
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

    <div id="mobile-menu" class="fixed inset-0 bg-snap-black/95 backdrop-blur-md z-[999] hidden flex-col px-6 py-8 overflow-y-auto w-full h-full">
        <div class="flex justify-between items-center mb-10 border-b border-slate-800 pb-6 mt-2">
            <div class="flex flex-col leading-none">
                <span class="font-black text-3xl text-snap-green tracking-tighter">SNAPCON</span>
                <span class="text-[10px] text-white font-bold tracking-[0.3em] ml-0.5 opacity-80 uppercase">Automation</span>
            </div>
            <button onclick="toggleMobileMenu()" class="text-slate-400 hover:text-white text-3xl focus:outline-none"><i class="fas fa-times"></i></button>
        </div>
        
        <div id="mobile-login-section" class="flex flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full">
            <h3 class="text-white font-bold text-sm uppercase tracking-widest mb-2" data-i18n="navLogin">Login</h3>
            <input type="text" id="mobile-userId" placeholder="ID" class="w-full px-4 py-4 rounded-xl bg-slate-800/50 text-white placeholder-slate-500 outline-none focus:border-snap-green border border-slate-700">
            <input type="password" id="mobile-userPass" placeholder="Password" class="w-full px-4 py-4 rounded-xl bg-slate-800/50 text-white placeholder-slate-500 outline-none focus:border-snap-green border border-slate-700">
            <button onclick="handleLogin()" class="w-full py-4 bg-snap-green text-white font-bold rounded-xl uppercase tracking-widest mt-2 shadow-lg">Login</button>
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

        <div class="flex flex-col gap-2 w-full pb-10 text-white">
            <button onclick="navigate('home'); toggleMobileMenu();" class="text-left text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navHome">Home <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="navigate('product'); toggleMobileMenu();" class="text-left text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navProduct">Products <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="navigate('spare'); toggleMobileMenu();" class="text-left text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navSpare">Spare Parts <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="checkDashboardAuth(); toggleMobileMenu();" class="text-left text-snap-green text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navDashboard">Dashboard <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="navigate('project'); toggleMobileMenu();" class="text-left text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navProject">Projects <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="navigate('about'); toggleMobileMenu();" class="text-left text-xl font-black py-4 border-b border-slate-800 flex justify-between" data-i18n="navAbout">Company <i class="fas fa-chevron-right text-sm"></i></button>
            <button onclick="navigate('contact'); toggleMobileMenu();" class="text-left text-xl font-black py-4 hover:text-snap-green flex justify-between" data-i18n="navContact">Support <i class="fas fa-chevron-right text-sm"></i></button>
        </div>
    </div>

    <div id="page-home" class="page-section page-active">
        <section class="hero-container w-full min-h-[550px] md:min-h-[650px] flex items-center relative overflow-hidden pb-16 pt-[75px]">
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay z-0"></div>
            <div class="max-container relative z-10 flex flex-col lg:flex-row items-center justify-between gap-10 w-full pt-6 md:pt-10">
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
                    <button onclick="navigate('product')" class="w-full sm:w-auto bg-snap-black text-white px-8 py-4 rounded-xl font-bold text-sm hover:bg-snap-green flex items-center justify-center gap-2 group transition-all shadow-lg">
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

        <section class="relative z-40 max-container lg:-mt-16 mb-16 px-4 sm:px-6">
            <div class="bg-white rounded-2xl shadow-xl shadow-slate-200/50 border border-slate-100 overflow-hidden">
                <div class="grid grid-cols-3 border-b border-slate-100">
                    <button onclick="switchDocTab('datasheet')" id="btn-tab-datasheet" class="doc-btn active flex flex-col items-center justify-center p-4 sm:p-6 transition-all hover:bg-slate-50 outline-none border-b-4 border-snap-green text-snap-green font-black">
                        <i class="fas fa-file-pdf text-xl sm:text-2xl mb-2"></i>
                        <span class="text-[10px] sm:text-xs uppercase tracking-widest">Data Sheet</span>
                    </button>
                    <button onclick="switchDocTab('drawing')" id="btn-tab-drawing" class="doc-btn flex flex-col items-center justify-center p-4 sm:p-6 transition-all hover:bg-slate-50 outline-none border-b-4 border-transparent text-slate-400 hover:text-slate-600 font-bold">
                        <i class="fas fa-drafting-compass text-xl sm:text-2xl mb-2"></i>
                        <span class="text-[10px] sm:text-xs uppercase tracking-widest">Drawing</span>
                    </button>
                    <button onclick="switchDocTab('catalog')" id="btn-tab-catalog" class="doc-btn flex flex-col items-center justify-center p-4 sm:p-6 transition-all hover:bg-slate-50 outline-none border-b-4 border-transparent text-slate-400 hover:text-slate-600 font-bold">
                        <i class="fas fa-book-open text-xl sm:text-2xl mb-2"></i>
                        <span class="text-[10px] sm:text-xs uppercase tracking-widest">Catalog</span>
                    </button>
                </div>
                
                <div class="bg-slate-50 min-h-[150px] relative">
                    <div id="content-datasheet" class="tab-content active w-full p-4 sm:p-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                        <div class="col-span-full text-center py-6 text-slate-400 font-medium text-sm">กำลังโหลดข้อมูล...</div>
                    </div>
                    <div id="content-drawing" class="tab-content w-full p-4 sm:p-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"></div>
                    <div id="content-catalog" class="tab-content w-full p-4 sm:p-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"></div>
                </div>
            </div>
        </section>

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
                    </div>
                
                <div class="text-center mt-6">
                    <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-slate-500 font-bold text-xs uppercase tracking-widest hover:text-snap-green transition-colors bg-white px-6 py-3 rounded-xl border border-slate-200 hover:border-snap-green shadow-sm w-full sm:w-auto justify-center">
                        <span data-i18n="viewAllProducts">View All Products</span> <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </section>

        <section class="bg-white py-16 sm:py-24 border-t border-slate-200 mt-10">
            <div class="max-container">
                <div class="flex justify-between items-end mb-10 sm:mb-12 px-2">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight">Knowledge & Insight</h2>
                        <div class="w-16 h-1.5 bg-snap-green rounded-full mt-3 mb-2"></div>
                        <p class="text-slate-500 font-medium text-sm" data-i18n="knowledgeSub">บทความเทคนิค คลังความรู้ และวิดีโอจากวิศวกรผู้เชี่ยวชาญ</p>
                    </div>
                </div>
                <div id="article-list" class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8 px-2">
                    </div>
            </div>
        </section>
    </div>

    <div id="page-product" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageProductTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2 px-2">Conveyor Systems</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-8 ml-2"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 px-2" id="product-grid"></div>
        </div>
    </div>

    <div id="page-spare" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageSpareTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2 px-2">Spare Parts</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-8 ml-2"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4" id="spare-grid"></div>
        </div>
    </div>

    <div id="page-project" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10 px-4">
            <h2 data-i18n="pageProjectTitle" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Project Reference</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-10 sm:mb-12"></div>
            
            <h3 class="text-xl sm:text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <div class="w-10 h-10 bg-emerald-50 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-rocket text-snap-green"></i></div> 
                <span data-i18n="projPilotTitle">Pilot / Demo Project</span>
            </h3>
            <div id="project-pilot-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16"></div>
            
            <h3 class="text-xl sm:text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-industry text-blue-500"></i></div>
                <span data-i18n="projUseCaseTitle">Use Case / Application</span>
            </h3>
            <div id="project-usecase-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6"></div>
        </div>
    </div>

    <div id="page-cart" class="page-section bg-slate-50 min-h-screen pt-10">
        <div class="max-container max-w-4xl py-10 px-4">
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
                    <p class="font-bold text-slate-700 mb-4 uppercase text-[10px] sm:text-xs tracking-widest"><i class="fas fa-info-circle text-snap-green mr-1"></i> <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ</span></p>
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

    <div id="page-dashboard" class="page-section bg-slate-50 min-h-screen pt-10 px-4">
        <div class="max-container py-10">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">
                <span data-i18n="navDashboard">Dashboard</span> : <span id="dash-user-name" class="text-snap-green"></span>
            </h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-6"></div>
            <p class="text-slate-600 mb-8 text-sm sm:text-base" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm lg:col-span-2">
                    <h3 class="font-bold text-slate-800 mb-4 sm:mb-6 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-4 rounded-xl font-black text-[10px] sm:text-xs shadow-sm"><i class="fas fa-play mb-1 text-base block"></i> START</button>
                        <button onclick="stopSystem()" id="btn-stop" class="bg-slate-100 text-slate-600 py-4 rounded-xl font-black text-[10px] sm:text-xs border border-slate-200"><i class="fas fa-stop mb-1 text-base block"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-4 rounded-xl font-black text-[10px] sm:text-xs shadow-sm"><i class="fas fa-sync-alt mb-1 text-base block"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-4 rounded-xl font-black text-[10px] sm:text-xs shadow-sm"><i class="fas fa-file-csv mb-1 text-base block"></i> REPORT</button>
                    </div>
                </div>
                <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCfgTitle">Configuration</h3>
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

            <div id="dash-nodes-grid" class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-5 xl:grid-cols-10 gap-3"></div>
        </div>
    </div>

    <div id="page-about" class="page-section bg-white min-h-screen pt-10 px-4">
        <div class="max-container py-10">
            <h2 data-i18n="navAbout" class="text-2xl sm:text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Company</h2>
            <div class="w-16 h-1.5 bg-snap-green rounded-full mb-10"></div>
            <p class="text-slate-600 leading-relaxed mb-6 text-base md:text-lg font-medium" data-i18n="aboutDesc">
                Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่...
            </p>
        </div>
    </div>

    <div id="modal-register" class="fixed inset-0 bg-snap-black/90 backdrop-blur-sm z-[200] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md shadow-2xl relative p-6 sm:p-10 rounded-[2rem] max-h-[90vh] overflow-y-auto custom-scrollbar">
            <button onclick="closeRegisterModal()" class="absolute top-4 right-4 sm:top-5 sm:right-5 w-8 h-8 sm:w-10 sm:h-10 bg-slate-50 hover:bg-red-50 text-slate-400 hover:text-red-500 rounded-full flex items-center justify-center transition-colors text-base sm:text-lg focus:outline-none"><i class="fas fa-times"></i></button>
            <h3 class="text-xl sm:text-2xl font-black text-slate-900 uppercase mb-4 tracking-tight text-center" data-i18n="regTitle">CREATE ACCOUNT</h3>
            <div class="space-y-3">
                <input type="text" id="reg-id" data-i18n-placeholder="regId" placeholder="User ID" class="w-full px-4 py-3 border rounded-xl outline-none focus:border-snap-green bg-slate-50 font-bold">
                <input type="password" id="reg-pass" data-i18n-placeholder="regPass" placeholder="Password" class="w-full px-4 py-3 border rounded-xl outline-none focus:border-snap-green bg-slate-50 font-bold">
                <input type="text" id="reg-name" data-i18n-placeholder="regName" placeholder="Name" class="w-full px-4 py-3 border rounded-xl outline-none focus:border-snap-green bg-slate-50 font-bold">
                <input type="text" id="reg-contact" data-i18n-placeholder="regContact" placeholder="Contact" class="w-full px-4 py-3 border rounded-xl outline-none focus:border-snap-green bg-slate-50 font-bold">
                <button onclick="submitRegistration()" class="w-full bg-snap-green text-white py-3.5 font-bold rounded-xl mt-4" data-i18n="btnSubmitReg">Confirm</button>
            </div>
        </div>
    </div>

    <script>
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxaV4oNSs0eWV5TOsVU9Ky8pl08d7f8H4L98vb1-ZLFQn95q4Kiy15ZqC34hrKoziYl/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [], products = [], spares = [], documents = [], projects = [], articles = [], allItems = [];
        let currentUserId = null, memoryUsers = { '001': '123', 'admin': 'admin' };

        // i18n Dictionary
        const dict = {
            th: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company", navHome: "Home",
                navLogin: "เข้าสู่ระบบ", navRegister: "สมัครสมาชิก", navLogout: "ออกจากระบบ",
                heroEco: "Green Technology", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", 
                heroDesc: "เปลี่ยนความซับซ้อนให้เป็นเรื่องง่าย ด้วยระบบออโตเมชัน Plug & Play ที่พร้อมให้คุณควบคุมสายการผลิตได้ทันที",
                heroLink: "ดูสินค้าทั้งหมด",
                fs1Title: "⚡ Easy Setup (Plug & Play)", fs1Desc: "ติดตั้งง่าย ใช้งานได้ทันที",
                fs2Title: "📊 Real-Time Monitoring", fs2Desc: "แสดงผลแบบเรียลไทม์ เห็นข้อมูลทันที",
                fs3Title: "🎛 Centralized Control", fs3Desc: "ควบคุมทุกเครื่องจักรจากจุดเดียว",
                fs4Title: "🛡 Built-in Poka-Yoke", fs4Desc: "ระบบกันพลาดในตัว ป้องกันความผิดพลาดอัตโนมัติ",
                fs5Title: "☁️ Cloud Ready", fs5Desc: "รองรับการเชื่อมต่อ Cloud พร้อมใช้งาน",
                cardDataSheet: "Data Sheet", selectModel: "เลือกโมเดล", cardDrawing: "2D/3D Drawing", cardCatalog: "Catalog", btnDownload: "ดาวน์โหลด",
                homeProductsTitle: "Featured Products", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์รุ่นล่าสุด", viewAllProducts: "ดูสินค้าทั้งหมด",
                knowledgeSub: "บทความเทคนิค คลังความรู้ และวิดีโอจากผู้เชี่ยวชาญ",
                pageProductTitle: "Conveyor Systems", pageSpareTitle: "Spare Parts", pageProjectTitle: "Project Reference", 
                projPilotTitle: "Pilot / Demo Project", projUseCaseTitle: "Use Case / Application",
                pageCartTitle: "Quotation Request", cartEmpty: "ไม่มีสินค้าในรถเข็น", cartTotalLabel: "ราคากลางรวม", btnRequestQuote: "ยื่นขอใบเสนอราคา", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก",
                guestContactTitle: "ข้อมูลติดต่อกลับ", contactSub: "ศูนย์เทคนิค 24 ชั่วโมง",
                aboutVisionTitle: "Vision", aboutMissionTitle: "Mission", aboutDesc: "Snapcon Automation คือผู้นำเทคโนโลยี...",
                regTitle: "สมัครสมาชิก", btnSubmitReg: "ยืนยันการสมัคร", phId: "ID", phPass: "PW", phGuestName: "ชื่อ", phGuestContact: "อีเมล/เบอร์โทร",
                regId: "ตั้งรหัส ID", regPass: "ตั้งรหัสผ่าน", regName: "ชื่อ-บริษัท", regContact: "อีเมล/เบอร์โทร",
                dashSubTitle: "ระบบตรวจสอบระดับองค์กร", dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Total Power",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status", statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint."
            },
            en: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company", navHome: "Home",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                heroEco: "Green Technology", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", 
                heroDesc: "Turn complexity into simplicity with Plug & Play automation systems.",
                heroLink: "View Products",
                fs1Title: "⚡ Easy Setup (Plug & Play)", fs1Desc: "Easy installation, ready to use",
                fs2Title: "📊 Real-Time Monitoring", fs2Desc: "Real-time display, instant visibility",
                fs3Title: "🎛 Centralized Control", fs3Desc: "Control all machines from one point",
                fs4Title: "🛡 Built-in Poka-Yoke", fs4Desc: "Automatic error prevention system",
                fs5Title: "☁️ Cloud Ready", fs5Desc: "Cloud connection supported",
                cardDataSheet: "Data Sheet", selectModel: "Select Model", cardDrawing: "2D/3D Drawing", cardCatalog: "Catalog", btnDownload: "Download",
                homeProductsTitle: "Featured Products", homeProductsSub: "Explore our latest machines", viewAllProducts: "View All Products",
                knowledgeSub: "Articles and videos from engineers",
                pageProductTitle: "Conveyor Systems", pageSpareTitle: "Spare Parts", pageProjectTitle: "Project Reference", 
                projPilotTitle: "Pilot Project", projUseCaseTitle: "Use Case",
                pageCartTitle: "Quotation Request", cartEmpty: "Empty cart", cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "Delete",
                guestContactTitle: "Contact Info", contactSub: "Technical Support 24/7",
                aboutVisionTitle: "Vision", aboutMissionTitle: "Mission", aboutDesc: "Snapcon Automation is...",
                regTitle: "Create Account", btnSubmitReg: "Confirm", phId: "ID", phPass: "PW", phGuestName: "Name", phGuestContact: "Contact",
                regId: "Set ID", regPass: "Set Password", regName: "Name", regContact: "Contact",
                dashSubTitle: "Enterprise Monitoring System", dashCtrlTitle: "Controls", dashCfgTitle: "Config", dashTarget: "Target", dashCarbon: "Carbon", dashEnergy: "Energy",
                dashPlanTitle: "Planning", dashTotOut: "Total Output", dashCalCarbon: "Carbon", dashTotPower: "Power",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status", statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint."
            }
        };

        function setLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('[data-i18n]').forEach(el => { const k = el.getAttribute('data-i18n'); if (dict[lang][k]) el.innerHTML = dict[lang][k]; });
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => { const k = el.getAttribute('data-i18n-placeholder'); if (dict[lang][k]) el.placeholder = dict[lang][k]; });
            document.getElementById('btn-lang-th').className = lang === 'th' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            document.getElementById('btn-lang-en').className = lang === 'en' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            renderProducts(); renderProjects(); renderArticles();
        }

        function toggleMobileMenu() { const m = document.getElementById('mobile-menu'); if (m.classList.contains('hidden')) { m.classList.remove('hidden'); m.classList.add('flex'); document.body.style.overflow = 'hidden'; } else { m.classList.add('hidden'); m.classList.remove('flex'); document.body.style.overflow = ''; } }
        function scrollSlider(dir) { const s = document.getElementById('home-product-slider'); if(s) { const a = window.innerWidth > 768 ? 320 : 260; s.scrollBy({ left: dir === 'left' ? -a : a, behavior: 'smooth' }); } }
        function navigate(p) { document.querySelectorAll('.page-section').forEach(s => s.classList.remove('page-active')); const t = document.getElementById('page-'+p); if(t) t.classList.add('page-active'); window.scrollTo(0,0); if(p==='cart') renderCart(); if(p==='dashboard') renderDashboard(); }
        function getValidImageUrl(u) { if(!u) return ''; if(u.includes('drive.google.com/file/d/')) { try { const id = u.split('/d/')[1].split('/')[0]; return `https://drive.google.com/uc?export=view&id=${id}`; } catch(e) { return u; } } return u; }
        function getEmbedVideoUrl(u) { if(!u) return ''; if(u.includes('drive.google.com/file/d/')) { try { const id = u.split('/d/')[1].split('/')[0]; return `https://drive.google.com/file/d/${id}/preview`; } catch(e) { return u; } } if(u.includes('youtube.com/watch?v=')) return u.replace('watch?v=', 'embed/'); return u; }
        function normalizeKeys(arr) { if(!arr || arr.length === 0) return []; return arr.map(obj => { const n = {}; for(let k in obj) { n[k.toLowerCase().replace(/[\\s_]+/g, '')] = obj[k]; } return n; }); }
        
        async function loadDataFromSheet() {
            try {
                const r = await fetch(GOOGLE_SCRIPT_URL + "?t=" + Date.now());
                const d = await r.json();
                products = normalizeKeys(d.products); spares = normalizeKeys(d.spares); documents = normalizeKeys(d.documents); projects = normalizeKeys(d.projects); articles = normalizeKeys(d.articles);
                allItems = [...products, ...spares];
                renderProducts(); renderDocuments(); renderProjects(); renderArticles();
            } catch(e) { console.log(e); }
        }

        // --- ระบบสลับแท็บเอกสาร (TABS LOGIC) ---
        function switchDocTab(tabName) {
            document.querySelectorAll('.doc-btn').forEach(b => {
                b.classList.remove('active', 'border-snap-green', 'text-snap-green');
                b.classList.add('border-transparent', 'text-slate-400');
            });
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            
            const btn = document.getElementById('btn-tab-' + tabName);
            const content = document.getElementById('content-' + tabName);
            
            if(btn && content) {
                btn.classList.add('active', 'border-snap-green', 'text-snap-green');
                btn.classList.remove('border-transparent', 'text-slate-400');
                content.classList.add('active');
            }
        }

        function renderDocuments() {
            const makeList = (typeStr) => {
                const f = documents.filter(d => (d.type||d.category||'').toLowerCase().includes(typeStr));
                if(!f.length) return '<div class="col-span-full text-center py-8 text-slate-400 text-sm font-medium">ไม่มีไฟล์ในหมวดหมู่นี้</div>';
                return f.map(d => {
                    const n = d.modelname||d.name||d.title||'Untitled';
                    const u = d.fileurl||d.link||d.url||'#';
                    if(u==='#') return '';
                    let icon = 'fa-file';
                    if(typeStr==='datasheet') icon='fa-file-pdf text-red-400';
                    else if(typeStr==='drawing') icon='fa-file-alt text-blue-400';
                    else icon='fa-book text-amber-400';
                    
                    return `
                    <a href="${u}" target="_blank" class="flex items-center gap-3 bg-white p-4 rounded-xl shadow-sm border border-slate-100 hover:border-snap-green hover:shadow-md transition-all group">
                        <div class="w-10 h-10 bg-slate-50 rounded-lg flex items-center justify-center shrink-0 group-hover:bg-emerald-50 transition-colors"><i class="fas ${icon} text-lg group-hover:text-snap-green transition-colors"></i></div>
                        <div class="min-w-0"><p class="text-sm font-bold text-slate-800 truncate">${n}</p><p class="text-[9px] text-slate-400 uppercase tracking-widest mt-0.5">Click to Download</p></div>
                    </a>`;
                }).join('');
            };
            
            const ds = document.getElementById('content-datasheet'); if(ds) ds.innerHTML = makeList('datasheet');
            const dw = document.getElementById('content-drawing'); if(dw) dw.innerHTML = makeList('drawing');
            const ca = document.getElementById('content-catalog'); if(ca) ca.innerHTML = makeList('catalog');
        }

        function renderProducts() {
            const pGrid = document.getElementById('product-grid');
            const sGrid = document.getElementById('spare-grid');
            const slider = document.getElementById('home-product-slider');

            const makeCard = (p) => {
                let specArr = (currentLang==='th'?p.specsth:p.specsen) || p.specs || [];
                if(!Array.isArray(specArr)) specArr = typeof specArr==='string'?specArr.split(','):[specArr];
                let sHtml = specArr.length?`<div class="mb-4 flex-grow text-[10px] sm:text-xs text-slate-500 space-y-1.5">${specArr.map(s=>`<div class="truncate border-b border-slate-50 pb-1 last:border-0"><i class="fas fa-check text-emerald-400 mr-1.5"></i>${s}</div>`).join('')}</div>`:'<div class="mb-4 flex-grow"></div>';
                return `<div class="bg-white p-4 sm:p-5 flex flex-col h-full rounded-2xl shadow-sm border border-slate-100 hover:shadow-lg transition-all">
                    <div class="bg-slate-50 h-32 sm:h-40 flex items-center justify-center p-3 mb-4 rounded-xl border border-slate-100 overflow-hidden"><img src="${getValidImageUrl(p.img||p.imageurl)}" class="max-h-full max-w-full object-contain mix-blend-multiply"></div>
                    <h4 class="font-black text-xs sm:text-sm text-slate-900 mb-2 line-clamp-2">${p.name||p.title}</h4>
                    ${sHtml}
                    <div class="mt-auto pt-3 border-t border-slate-50">
                        <p class="text-snap-green font-black text-lg sm:text-xl mb-4">฿${parseFloat(p.price||0).toLocaleString()}</p>
                        <button onclick="addToCart('${p.id}')" class="w-full bg-slate-50 py-2.5 rounded-xl font-bold text-[10px] sm:text-xs hover:bg-snap-green hover:text-white transition-all border border-slate-200">ADD TO CART</button>
                    </div></div>`;
            };
            if(pGrid) pGrid.innerHTML = products.map(makeCard).join('');
            if(sGrid) sGrid.innerHTML = spares.map(makeCard).join('');
            if(slider) slider.innerHTML = products.slice(0, 10).map(p => `<div onclick="navigate('product')" class="min-w-[220px] sm:min-w-[280px] snap-center bg-white border border-slate-100 p-4 sm:p-5 rounded-[1.5rem] shadow-sm hover:shadow-xl transition-all cursor-pointer"><div class="overflow-hidden rounded-xl mb-4 h-28 sm:h-36 bg-slate-50 border border-slate-100 p-2"><img src="${getValidImageUrl(p.img||p.imageurl)}" class="w-full h-full object-contain mix-blend-multiply"></div><h4 class="font-black text-[13px] sm:text-[15px] text-slate-800 mb-1 truncate">${p.name||p.title}</h4><p class="text-snap-green font-black text-base sm:text-lg mt-auto">฿${parseFloat(p.price||0).toLocaleString()}</p></div>`).join('');
        }

        function renderProjects() {
            const pG = document.getElementById('project-pilot-grid');
            const uG = document.getElementById('project-usecase-grid');
            if(pG) pG.innerHTML = projects.filter(p=>(p.category||'').toLowerCase().includes('pilot')).map(p=>`<div class="bg-slate-50 p-6 sm:p-8 border border-slate-100 rounded-[2rem] h-full flex flex-col"><div class="w-16 h-16 sm:w-20 sm:h-20 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm overflow-hidden shrink-0">${getValidImageUrl(p.imgurl||p.img||p.icon).includes('http')?`<img src="${getValidImageUrl(p.imgurl||p.img||p.icon)}" class="w-full h-full object-contain p-2">`:`<i class="${p.icon||'fas fa-cogs'} text-3xl text-snap-green"></i>`}</div><h4 class="text-lg sm:text-xl font-black text-slate-900 mb-2">${p.title}</h4><p class="text-xs sm:text-sm text-slate-600">${currentLang==='th'?p.descriptionth:p.descriptionen}</p></div>`).join('');
            if(uG) uG.innerHTML = projects.filter(p=>(p.category||'').toLowerCase().includes('usecase')).map((p,i)=>`<div class="bg-white p-6 sm:p-8 rounded-[2rem] border-t-[6px] border-t-snap-green flex flex-col items-center text-center h-full shadow-sm"><div class="w-full h-36 sm:h-44 bg-slate-100 rounded-2xl mb-8 overflow-hidden"><img src="${getValidImageUrl(p.imgurl||p.img)}" class="w-full h-full object-cover"></div><h4 class="text-xl font-black text-slate-900 mb-3">${p.title}</h4><p class="text-sm text-slate-600">${currentLang==='th'?p.descriptionth:p.descriptionen}</p></div>`).join('');
        }

        function renderArticles() {
            const c = document.getElementById('article-list');
            if(!c || !articles.length) return;
            c.innerHTML = articles.map(art => {
                let v = art.video1 || art.youtube1; let media = v?`<iframe class="w-full h-full rounded-2xl" src="${getEmbedVideoUrl(v)}" frameborder="0" allowfullscreen></iframe>`:`<img src="${getValidImageUrl(art.imageurl||art.img)}" class="w-full h-full object-cover rounded-2xl">`;
                return `<div class="bg-white border border-slate-100 rounded-[2rem] shadow-lg hover:shadow-xl transition-all duration-300 flex flex-col h-full group p-3"><div class="aspect-video mb-4">${media}</div><div class="p-4 sm:p-6 flex flex-col flex-1"><span class="text-emerald-600 bg-emerald-50 self-start px-3 py-1 rounded-lg text-[10px] font-black uppercase mb-4">${art.category||'INSIGHT'}</span><h3 class="text-lg sm:text-xl font-black text-slate-900 mb-2 line-clamp-2">${art.title}</h3><p class="text-slate-500 text-xs sm:text-sm mb-4 line-clamp-2">${art.summary||''}</p><div class="mt-auto flex justify-between items-center pt-4 border-t border-slate-100"><span class="text-[9px] font-bold text-slate-400 uppercase">${art.date||''}</span>${art.link?`<a href="${art.link}" target="_blank" class="bg-slate-900 text-white px-5 py-2.5 rounded-xl text-[10px] font-bold hover:bg-snap-green">READ MORE</a>`:''}</div></div></div>`;
            }).join('');
        }

        // Post Data Functions
        function sendPost(payload) { setTimeout(()=>fetch(GOOGLE_SCRIPT_URL,{method:'POST',mode:'no-cors',body:JSON.stringify(payload)}),100); }
        function handleLogin() { 
            const id = document.getElementById('userId').value.trim() || document.getElementById('mobile-userId').value.trim();
            const pass = document.getElementById('userPass').value.trim() || document.getElementById('mobile-userPass').value.trim();
            if(!id || !pass) return alert("Please enter ID and PW");
            if(memoryUsers[id]===pass) { 
                isLoggedIn=true; currentUserId=id;
                document.getElementById('displayUser').innerText=id; document.getElementById('mobile-displayUser').innerText=id;
                document.getElementById('login-section').className="hidden items-center gap-2 pr-5";
                document.getElementById('user-section').className="flex items-center gap-3 pr-5";
                document.getElementById('mobile-login-section').className="hidden";
                document.getElementById('mobile-user-section').className="flex flex-col gap-4 mb-8 pb-8 border-b border-slate-800 w-full";
                const m=document.getElementById('mobile-menu'); if(!m.classList.contains('hidden')) toggleMobileMenu();
                alert(currentLang==='th'?"เข้าสู่ระบบแล้ว!":"Login Success!");
            } else alert("Invalid ID/PW");
        }
        function submitRegistration() {
            const id=document.getElementById('reg-id').value.trim(), pass=document.getElementById('reg-pass').value.trim(), name=document.getElementById('reg-name').value.trim(), contact=document.getElementById('reg-contact').value.trim();
            if(!id||!pass||!name||!contact) return alert("Fill all fields");
            memoryUsers[id]=pass; isLoggedIn=true; currentUserId=id; 
            document.getElementById('displayUser').innerText=id; document.getElementById('mobile-displayUser').innerText=id;
            document.getElementById('login-section').className="hidden"; document.getElementById('user-section').className="flex items-center gap-3 pr-5";
            closeRegisterModal(); sendPost({type:"Registration",name_or_id:id,email:contact,details:name});
            alert("Registered and Logged in!");
        }
        function handleLogout() { isLoggedIn=false; currentUserId=null; location.reload(); }
        function requestQuote() {
            const sel=cart.filter(i=>i.selected); if(!sel.length) return alert("Select item");
            const name=document.getElementById('quote-name').value.trim(), info=document.getElementById('quote-contact').value.trim();
            if(!name||!info) return alert("Enter contact info");
            sendPost({type:"Quotation",name_or_id:name,email:info,details:sel.map(i=>i.name||i.title).join(',')});
            alert("Submitted!"); cart=[]; updateBadge(); navigate('home');
        }
        function submitContactForm() {
            const n=document.getElementById('contact-name').value, i=document.getElementById('contact-info').value, m=document.getElementById('contact-message').value;
            if(!n||!i||!m) return alert("Fill all fields");
            sendPost({type:"Contact",name_or_id:n,email:i,details:m}); alert("Sent!");
        }
        function openRegisterModal() { document.getElementById('modal-register').classList.replace('hidden','flex'); }
        function closeRegisterModal() { document.getElementById('modal-register').classList.replace('flex','hidden'); }
        function checkDashboardAuth() { if(isLoggedIn) navigate('dashboard'); else alert("Please login first"); }
        function addToCart(id) { const item=allItems.find(i=>i.id===id); if(item) { const e=cart.find(i=>i.id===id); if(e) e.quantity++; else cart.push({...item,cartId:Date.now().toString(),selected:true,quantity:1}); updateBadge(); alert("Added!"); } }
        function updateBadge() { const b=document.getElementById('cart-badge'); const c=cart.reduce((s,i)=>s+i.quantity,0); b.innerText=c>99?'99+':c; b.classList.toggle('hidden',c===0); }
        function updateQuantity(cId, d) { const i=cart.find(x=>x.cartId===cId); if(i) { i.quantity=Math.max(1,i.quantity+d); renderCart(); updateBadge(); } }
        function toggleItem(cId) { const i=cart.find(x=>x.cartId===cId); if(i) { i.selected=!i.selected; renderCart(); } }
        function toggleSelectAll(v) { cart.forEach(i=>i.selected=v); renderCart(); }
        function deleteSelected() { cart=cart.filter(i=>!i.selected); updateBadge(); renderCart(); }
        function renderCart() {
            const c=document.getElementById('cart-items'); const q=document.getElementById('quote-contact-form');
            if(!c) return; if(q) q.classList.remove('hidden');
            if(!cart.length) { c.innerHTML=`<p class="text-center py-10 text-slate-400 font-bold bg-slate-50 border rounded-xl">Empty Cart</p>`; document.getElementById('cart-total').innerText='฿0'; return; }
            c.innerHTML=cart.map(i=>`<div class="flex flex-col sm:flex-row items-start sm:items-center bg-white border p-4 rounded-xl mb-3 gap-4"><div class="flex items-center gap-3 w-full sm:w-auto flex-1"><input type="checkbox" ${i.selected?'checked':''} onclick="toggleItem('${i.cartId}')" class="w-5 h-5 accent-snap-green"><img src="${getValidImageUrl(i.img||i.imageurl)}" class="w-14 h-14 object-contain border p-1 rounded"><div class="min-w-0"><span class="font-black text-sm block truncate">${i.name||i.title}</span><span class="text-[10px] text-slate-400 font-bold">${i.id}</span></div></div><div class="flex items-center gap-4"><div class="flex items-center border rounded h-9"><button onclick="updateQuantity('${i.cartId}',-1)" class="w-8 h-full bg-slate-50 font-black">-</button><span class="w-10 h-full flex items-center justify-center text-sm font-black">${i.quantity}</span><button onclick="updateQuantity('${i.cartId}',1)" class="w-8 h-full bg-slate-50 font-black">+</button></div><span class="font-black text-lg w-24 text-right">฿${((i.price||0)*i.quantity).toLocaleString()}</span></div></div>`).join('');
            document.getElementById('cart-total').innerText='฿'+cart.filter(i=>i.selected).reduce((s,i)=>s+(i.price||0)*i.quantity,0).toLocaleString();
            document.getElementById('cart-select-all').checked=cart.length>0&&cart.every(i=>i.selected);
        }

        window.onload = () => { loadDataFromSheet(); setTimeout(()=>setLanguage('th'), 200); };
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2500, scrolling=True)
