import streamlit as st

# ⚙️ 1. ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation Solution", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 🌐 2. โค้ด HTML/CSS/JS ฉบับ Master (รวมทุกฟีเจอร์)
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
        
        /* --- Hero Section --- */
        .hero-container { background-color: #1e293b; position: relative; }
        .hero-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.7) 50%, rgba(2, 44, 34, 0.8) 100%);
            z-index: 5; pointer-events: none;
        }
        .hero-white-box {
            background-color: white; border-bottom: 8px solid #00B36E;
            box-shadow: 15px 15px 40px rgba(0, 0, 0, 0.3); border-radius: 0px; 
        }

        /* --- Background Animation --- */
        .slide-img {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover; background-position: center; opacity: 0;
            animation: slideBgAnimation 20s infinite linear;
        }
        .slide-1 { background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80'); animation-delay: 0s; }
        .slide-2 { background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1920&q=80'); animation-delay: 5s; }
        .slide-3 { background-image: url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1920&q=80'); animation-delay: 10s; }
        .slide-4 { background-image: url('https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?auto=format&fit=crop&w=1920&q=80'); animation-delay: 15s; }

        @keyframes slideBgAnimation {
            0% { opacity: 0; transform: scale(1.05) translateX(20px); }
            5% { opacity: 1; transform: scale(1.05) translateX(15px); }
            20% { opacity: 1; transform: scale(1.05) translateX(-5px); }
            25% { opacity: 0; transform: scale(1.05) translateX(-10px); }
            100% { opacity: 0; }
        }

        /* --- Navigation --- */
        .nav-link { position: relative; color: white; font-weight: 700; font-size: 0.85rem; transition: color 0.3s; }
        .nav-link:hover { color: #00B36E; }
        .nav-link::after {
            content: ''; position: absolute; width: 0; height: 2px;
            bottom: -4px; left: 0; background-color: #00B36E; transition: width 0.3s;
        }
        .nav-link:hover::after { width: 100%; }

        /* --- Global UI --- */
        .page-section { display: none !important; }
        .page-active { display: block !important; animation: fadeIn 0.4s ease-out forwards; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
        
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        .sharp-card { border-radius: 4px; border: 1px solid #e2e8f0; transition: all 0.3s; }
        .sharp-card:hover { box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1); border-color: #00B36E; transform: translateY(-4px); }
        .sharp-btn { border-radius: 2px; transition: all 0.2s; text-transform: uppercase; letter-spacing: 0.05em; }
        .sharp-btn:active { transform: scale(0.98); }

        /* --- Animated Text Slider (6 Items) --- */
        .feature-text-container { position: relative; height: 140px; width: 100%; display: flex; align-items: center; }
        .feature-text-slide {
            position: absolute; width: 100%; opacity: 0; transform: translateY(30px);
            animation: fadeSlideText 18s infinite;
        }
        .feature-text-slide:nth-child(1) { animation-delay: 0s; }
        .feature-text-slide:nth-child(2) { animation-delay: 3s; }
        .feature-text-slide:nth-child(3) { animation-delay: 6s; }
        .feature-text-slide:nth-child(4) { animation-delay: 9s; }
        .feature-text-slide:nth-child(5) { animation-delay: 12s; }
        .feature-text-slide:nth-child(6) { animation-delay: 15s; }

        @keyframes fadeSlideText {
            0% { opacity: 0; transform: translateY(30px); }
            4% { opacity: 1; transform: translateY(0); }
            13% { opacity: 1; transform: translateY(0); }
            17% { opacity: 0; transform: translateY(-30px); }
            100% { opacity: 0; }
        }
    </style>
</head>
<body class="font-sans text-slate-800">

    <nav class="bg-snap-black h-[70px] w-full fixed top-0 z-50 flex items-center justify-between px-6 md:px-10 shadow-md border-b border-white/10">
        <div class="flex items-center gap-2 cursor-pointer shrink-0" onclick="navigate('home')">
            <span class="font-black text-3xl text-snap-green tracking-tighter">SNAPCON</span>
        </div>
        
        <div class="hidden md:flex items-center gap-8 ml-8">
            <button type="button" onclick="navigate('product')" data-i18n="navProduct" class="nav-link">Products</button>
            <button type="button" onclick="navigate('spare')" data-i18n="navSpare" class="nav-link">Spare Parts</button>
            <button type="button" onclick="checkDashboardAuth()" data-i18n="navDashboard" class="nav-link">Dashboard</button>
            <button type="button" onclick="navigate('project')" data-i18n="navProject" class="nav-link">Projects</button>
            <button type="button" onclick="navigate('about')" data-i18n="navAbout" class="nav-link">Company</button>
            <button type="button" onclick="navigate('contact')" data-i18n="navContact" class="nav-link">Support</button>
        </div>

        <div class="flex items-center gap-5 shrink-0 ml-auto">
            <div id="login-section" class="hidden lg:flex items-center gap-2">
                <input type="text" id="userId" data-i18n-placeholder="phId" placeholder="ID" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <input type="password" id="userPass" data-i18n-placeholder="phPass" placeholder="PW" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <button type="button" onclick="handleLogin()" class="h-8 px-3 bg-snap-green text-white font-bold text-xs hover:bg-snap-green-hover sharp-btn"><i class="fas fa-sign-in-alt"></i></button>
                <button type="button" onclick="openRegisterModal()" class="h-8 px-3 bg-slate-700 text-white font-bold text-xs hover:bg-slate-600 sharp-btn"><i class="fas fa-user-plus"></i></button>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3">
                <span class="text-white text-sm"><i class="far fa-user-circle text-snap-green mr-1"></i> <span id="displayUser" class="font-bold">User</span></span>
                <button type="button" onclick="handleLogout()" class="text-slate-400 hover:text-white text-xs underline"><i class="fas fa-sign-out-alt"></i></button>
            </div>

            <div class="flex items-center gap-4 text-white text-lg border-l border-slate-700 pl-5">
                <button type="button" id="btn-lang-th" onclick="setLanguage('th')" class="text-xs font-bold text-snap-green hover:text-white transition-colors">TH</button>
                <span class="text-slate-600 text-xs">|</span>
                <button type="button" id="btn-lang-en" onclick="setLanguage('en')" class="text-xs font-bold text-slate-400 hover:text-white transition-colors">EN</button>
                
                <div class="relative cursor-pointer hover:text-snap-green ml-2 transition-transform hover:scale-110" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 w-4 h-4 bg-snap-green text-white text-[9px] font-black flex items-center justify-center rounded-full hidden shadow-md">0</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="h-[70px]"></div>

    <div id="page-home" class="page-section page-active">
        
        <section class="hero-container w-full min-h-[500px] md:min-h-[600px] flex items-center relative z-0 overflow-hidden">
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div><div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div><div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay"></div>

            <div class="w-full max-w-[1400px] mx-auto px-6 md:px-12 flex flex-col md:flex-row items-center justify-between gap-10">
                
                <div class="hero-white-box w-full md:w-[500px] p-10 md:p-12 z-10 mt-10 md:mt-0 relative">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-emerald-50 text-emerald-600 rounded-full text-[10px] font-black tracking-widest uppercase mb-4 border border-emerald-200">
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

                <div class="hidden md:flex flex-col justify-center flex-1 pl-4 lg:pl-16 z-10 w-full max-w-lg">
                    <div>
                        <h3 class="text-snap-green font-black tracking-widest uppercase text-xs mb-6 border-b border-white/20 pb-4 inline-block drop-shadow-md">Why Snapcon?</h3>
                        <div class="feature-text-container">
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs1Title">⚡ Easy Setup</h4><p class="text-lg md:text-xl text-emerald-400 font-bold" data-i18n="fs1Desc">Plug & Play ใช้งานได้ทันที</p></div>
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs2Title">🔗 Seamless Connection</h4><p class="text-lg md:text-xl text-blue-400 font-bold" data-i18n="fs2Desc">เชื่อม PLC / Sensor ได้ง่าย</p></div>
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs3Title">📊 Real-Time Monitoring</h4><p class="text-lg md:text-xl text-amber-400 font-bold" data-i18n="fs3Desc">เห็นข้อมูลทันที</p></div>
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs4Title">🎛 All-in-One Control</h4><p class="text-lg md:text-xl text-purple-400 font-bold" data-i18n="fs4Desc">ควบคุมทุกเครื่องในที่เดียว</p></div>
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs5Title">💰 Cost-Effective</h4><p class="text-lg md:text-xl text-emerald-400 font-bold" data-i18n="fs5Desc">ถูกกว่า SCADA แบบเดิม</p></div>
                            <div class="feature-text-slide drop-shadow-xl"><h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs6Title">🛡️ Built-in Poka-Yoke</h4><p class="text-lg md:text-xl text-rose-400 font-bold" data-i18n="fs6Desc">ระบบป้องกันความผิดพลาดของคน</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="bg-snap-black w-full relative z-40 shadow-2xl border-t border-slate-800">
            <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-white/10">
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
        
        <div id="loading-spinner" class="w-full text-center py-10 hidden">
            <i class="fas fa-circle-notch fa-spin text-3xl text-snap-green mb-3"></i>
            <p class="text-slate-500 font-bold text-sm" data-i18n="loadingData">กำลังเชื่อมต่อข้อมูลจากระบบ...</p>
        </div>

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
                    </div>
                
                <div class="text-center mt-8">
                    <button onclick="navigate('product')" class="inline-flex items-center gap-2 text-slate-800 font-black text-sm uppercase tracking-widest hover:text-snap-green transition-colors" data-i18n="viewAllProducts">View All Products <i class="fas fa-arrow-right"></i></button>
                </div>
            </div>
        </section>
    </div>

    <div id="page-product" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 data-i18n="pageProductTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Conveyor Systems</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-10 max-w-2xl" data-i18n="pageProductSub">รวมเครื่องจักรสายพานลำเลียงอัจฉริยะทุกรุ่นที่ครอบคลุมทุกอุตสาหกรรม</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="product-grid"></div>
        </div>
    </div>

    <div id="page-spare" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 data-i18n="pageSpareTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Spare Parts</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-10 max-w-2xl" data-i18n="pageSpareSub">อะไหล่เครื่องจักรและชิ้นส่วนสายพานลำเลียงของแท้ 100%</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4" id="spare-grid"></div>
        </div>
    </div>

    <div id="page-project" class="page-section bg-white min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 data-i18n="pageProjectTitle" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Project Reference</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-12 max-w-2xl font-medium" data-i18n="pageProjectSub">รวมผลงานการติดตั้งและตัวอย่างการประยุกต์ใช้งานระบบ Snapcon ในอุตสาหกรรมจริง</p>

            <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <i class="fas fa-rocket text-snap-green"></i> <span data-i18n="projPilotTitle">Pilot / Demo Project</span>
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
                <div class="bg-slate-50 p-8 sharp-card group">
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-snap-green text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform"><i class="fas fa-network-wired"></i></div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot1Title">Snapcon V1</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot1Desc">Multi-machine control demo ควบคุมเครื่องจักรหลายตัวพร้อมกันผ่านศูนย์กลางเดียว</p>
                </div>
                <div class="bg-slate-50 p-8 sharp-card group">
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-blue-500 text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform"><i class="fas fa-chart-line"></i></div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot2Title">Real-time Monitoring</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot2Desc">ติดตามสถานะอุณหภูมิ (Temperature), ความเร็ว (Speed), และยอดผลิต (Output) ทันที</p>
                </div>
                <div class="bg-slate-50 p-8 sharp-card group">
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-rose-500 text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform"><i class="fas fa-shield-alt"></i></div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot3Title">Poka-Yoke Integrated</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot3Desc">ระบบป้องกันความผิดพลาดจากมนุษย์ แจ้งเตือนและหยุดเครื่องจักรเมื่อพบความผิดปกติ</p>
                </div>
            </div>

            <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <i class="fas fa-industry text-blue-500"></i> <span data-i18n="projUseCaseTitle">Use Case / Application</span>
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white p-6 sharp-card border-t-4 border-t-amber-500 flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden"><img src="https://images.unsplash.com/photo-1589792923962-537704632910?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500"></div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase1Title">Packaging Line Automation</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase1Desc">ระบบออโตเมชันสำหรับสายงานบรรจุภัณฑ์อัตโนมัติ ลดเวลาและเพิ่มความแม่นยำ</p>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-snap-green flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden"><img src="https://images.unsplash.com/photo-1513828583688-c52646db42da?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500"></div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase2Title">Conveyor System Control</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase2Desc">ระบบควบคุมสายพานลำเลียงอัจฉริยะ ปรับความเร็วอัตโนมัติตามโหลดงาน</p>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-blue-500 flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden"><img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500"></div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase3Title">Machine Health Monitoring</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase3Desc">ระบบเฝ้าระวังสภาพเครื่องจักรเชิงคาดการณ์ แจ้งเตือนก่อนเกิดความเสียหายหนัก</p>
                </div>
            </div>
        </div>
    </div>

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
                <div class="h-64 md:h-80 sharp-card overflow-hidden relative group rounded-2xl shadow-lg">
                    <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute inset-0 bg-snap-green/10 group-hover:bg-transparent transition-colors duration-500 pointer-events-none"></div>
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

    <div id="page-contact" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-w-[1000px] mx-auto px-6 py-10">
            <h2 data-i18n="navContact" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Support</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            
            <div class="bg-white sharp-card p-12 text-center max-w-2xl mx-auto">
                <i class="fas fa-headset text-5xl text-snap-green mb-6"></i>
                <h3 class="text-2xl font-black text-slate-900 mb-2">Technical Support 24/7</h3>
                <p class="text-slate-500 mb-8 text-sm" data-i18n="contactSub">ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ</p>
                
                <div class="space-y-4 max-w-xs mx-auto mb-10 text-left">
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card"><i class="fas fa-envelope text-slate-400"></i><span class="font-bold text-slate-700 text-sm">snapcon1992@gmail.com</span></div>
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card"><i class="fab fa-line text-slate-400"></i><span class="font-bold text-slate-700 text-sm">@SnapconAuto</span></div>
                    <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card"><i class="fas fa-phone-alt text-slate-400"></i><span class="font-bold text-slate-700 text-sm">081-XXX-XXXX</span></div>
                </div>
                <button onclick="window.location.href='mailto:snapcon1992@gmail.com'" class="bg-snap-black text-white px-10 py-4 font-bold hover:bg-snap-green sharp-btn text-sm w-full max-w-xs" data-i18n="btnEmail">SEND DIRECT EMAIL</button>
            </div>
        </div>
    </div>

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
                    <p class="font-bold text-slate-700 mb-4 uppercase text-xs tracking-widest flex items-center gap-2"><i class="fas fa-info-circle text-snap-green"></i><span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ</span></p>
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
                    <button type="button" onclick="requestQuote()" class="w-full md:w-auto bg-snap-black text-white px-8 py-4 font-bold hover:bg-snap-green sharp-btn text-sm" data-i18n="btnRequestQuote">ยื่นขอใบเสนอราคา</button>
                </div>
            </div>
        </div>
    </div>

    <div id="page-dashboard" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-w-[1400px] mx-auto px-6 py-10">
            <h2 class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2"><span data-i18n="navDashboard">Dashboard</span> : <span id="dash-user-name" class="text-snap-green"></span></h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-8" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์ (แสดงข้อมูลเฉพาะบัญชีของคุณ)</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card lg:col-span-2 flex flex-col justify-center">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button onclick="startSystem()" class="bg-snap-green text-white py-3 font-bold hover:bg-snap-green-hover sharp-btn text-xs"><i class="fas fa-play mr-2"></i> START</button>
                        <button onclick="stopSystem()" class="bg-slate-200 text-slate-700 py-3 font-bold hover:bg-red-500 hover:text-white sharp-btn text-xs"><i class="fas fa-stop mr-2"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-3 font-bold hover:bg-slate-800 sharp-btn text-xs"><i class="fas fa-sync-alt mr-2"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-3 font-bold hover:bg-blue-700 sharp-btn text-xs"><i class="fas fa-file-csv mr-2"></i> REPORT</button>
                    </div>
                </div>
                
                <div class="bg-white p-6 sharp-card">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCfgTitle">Configuration</h3>
                    <div class="space-y-3">
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2"><label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashTarget">Target</label><input type="number" id="cfg-target" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent"></div>
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2"><label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashCarbon">Carbon Factor</label><input type="number" step="0.0001" id="cfg-carbon" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent"></div>
                        <div class="flex justify-between items-center"><label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashEnergy">Energy Factor</label><input type="number" step="0.001" id="cfg-energy" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent"></div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card border-t-4 border-t-blue-500"><p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotOut">Total Output</p><h3 id="dash-total-output" class="text-4xl font-black text-slate-900 tracking-tighter">0</h3></div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-snap-green"><p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashCalCarbon">Cal Carbon</p><h3 id="dash-carbon" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3></div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-amber-500"><p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotPower">Total Power</p><h3 id="dash-power" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3></div>
            </div>

            <div class="bg-white p-8 sharp-card mb-8">
                <div class="flex justify-between items-end mb-4"><h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashPlanTitle">Production Planning</h3><span id="dash-progress-text" class="text-2xl font-black text-snap-green">0.0%</span></div>
                <div class="w-full h-4 bg-slate-100 rounded-sm overflow-hidden mb-6"><div id="dash-progress-bar" class="h-full bg-snap-green transition-all duration-300" style="width: 0%"></div></div>
                <div class="flex justify-between text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <span><i class="far fa-clock mr-1"></i> <span data-i18n="dashTimeElapsed">Elapsed</span>: <span id="dash-time-elapsed" class="text-slate-800">00:00:00</span></span>
                    <span><i class="fas fa-hourglass-half mr-1"></i> <span data-i18n="dashTimeRemain">ETA</span>: <span id="dash-time-remain" class="text-slate-800">--:--:--</span></span>
                </div>
            </div>

            <div class="bg-white p-6 sharp-card">
                <div class="flex justify-between items-center mb-6">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashMacStatus2">Machine Status</h3>
                    <div class="flex gap-4 text-[9px] font-bold uppercase tracking-widest text-slate-500">
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-snap-green"></div> <span data-i18n="statusNormal">Normal</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-amber-400"></div> <span data-i18n="statusWarning">Warning</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-red-500"></div> <span data-i18n="statusMaint">Maint.</span></span>
                    </div>
                </div>
                <div id="dash-nodes-grid" class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-10 gap-2 max-h-[60vh] overflow-y-auto custom-scrollbar p-1"></div>
            </div>
        </div>
    </div>

    <div id="modal-register" class="fixed inset-0 bg-snap-black/80 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md sharp-card flex flex-col shadow-2xl relative">
            <button onclick="closeRegisterModal()" class="absolute top-4 right-4 text-slate-400 hover:text-red-500"><i class="fas fa-times"></i></button>
            <div class="p-8 border-b border-slate-100 bg-slate-50"><h3 class="text-xl font-black text-slate-900 uppercase tracking-tight" data-i18n="regTitle">Create Account</h3><p class="text-xs text-slate-500 mt-1" data-i18n="regDesc">ลงทะเบียนเพื่อเข้าถึงระบบและขอใบเสนอราคา</p></div>
            <div class="p-8 space-y-4">
                <div><label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regId">User ID</label><input type="text" id="reg-id" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card"></div>
                <div><label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1" data-i18n="regPass">Password</label><input type="password" id="reg-pass" class="w-full px-3 py-2 bg-white border border-slate-300 outline-none focus:border-snap-green text-sm font-bold sharp-card"></div>
                <div class="h-px bg-slate-1
