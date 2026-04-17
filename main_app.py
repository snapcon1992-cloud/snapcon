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
        .max-container { max-width: 1400px; margin: 0 auto; padding: 0 1.5rem; }
        
        .hero-container { background-color: #e2e8f0; position: relative; }
        .hero-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, #ffffff 40%, rgba(16, 185, 129, 0.85) 75%, rgba(2, 44, 34, 0.6) 100%);
            z-index: 5; pointer-events: none;
        }
        .hero-white-box { background-color: white; border-bottom: 6px solid #00B36E; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15); border-radius: 4px; }
        .feature-bar { background-color: #1e293b; color: white; }

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
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        .sharp-card { border-radius: 4px; border: 1px solid #e2e8f0; transition: all 0.3s; }
        .sharp-card:hover { box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1); border-color: #00B36E; transform: translateY(-4px); }
        .sharp-btn { border-radius: 2px; transition: all 0.2s; text-transform: uppercase; letter-spacing: 0.05em; }
        
        .feature-text-slide { position: absolute; width: 100%; opacity: 0; transform: translateY(30px); animation: fadeSlideText 18s infinite; }
        @keyframes fadeSlideText { 0% { opacity: 0; transform: translateY(30px); } 4% { opacity: 1; transform: translateY(0); } 13% { opacity: 1; transform: translateY(0); } 17% { opacity: 0; transform: translateY(-30px); } 100% { opacity: 0; } }
        
        .line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    </style>
</head>
<body class="font-sans text-slate-800">

    <!-- Top Navigation -->
    <nav class="bg-snap-black h-[70px] w-full fixed top-0 z-50 flex items-center justify-between px-6 md:px-10 shadow-md">
        <div class="flex items-center gap-2 cursor-pointer shrink-0" onclick="navigate('home')">
            <span class="font-black text-3xl text-snap-green tracking-tighter">SNAPCON</span>
        </div>
        
        <div class="hidden md:flex items-center gap-8 ml-8">
            <button onclick="navigate('product')" data-i18n="navProduct" class="nav-link">Products</button>
            <button onclick="navigate('spare')" data-i18n="navSpare" class="nav-link">Spare Parts</button>
            <button onclick="checkDashboardAuth()" data-i18n="navDashboard" class="nav-link">Dashboard</button>
            <button onclick="navigate('project')" data-i18n="navProject" class="nav-link">Projects</button>
            <button onclick="navigate('about')" data-i18n="navAbout" class="nav-link">Company</button>
            <button onclick="navigate('contact')" data-i18n="navContact" class="nav-link">Support</button>
        </div>

        <div class="flex items-center gap-5 shrink-0 ml-auto">
            <div id="login-section" class="hidden lg:flex items-center gap-2">
                <input type="text" id="userId" data-i18n-placeholder="phId" placeholder="ID" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <input type="password" id="userPass" data-i18n-placeholder="phPass" placeholder="PW" class="h-8 w-20 px-2 text-xs outline-none bg-slate-800 text-white border border-slate-700 focus:border-snap-green sharp-card">
                <button onclick="handleLogin()" class="h-8 px-3 bg-snap-green text-white font-bold text-xs hover:bg-snap-green-hover sharp-btn"><i class="fas fa-sign-in-alt"></i></button>
                <button onclick="openRegisterModal()" class="h-8 px-3 bg-slate-700 text-white font-bold text-xs hover:bg-slate-600 sharp-btn"><i class="fas fa-user-plus"></i></button>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3">
                <span class="text-white text-sm"><i class="far fa-user-circle text-snap-green mr-1"></i> <span id="displayUser" class="font-bold">User</span></span>
                <button onclick="handleLogout()" class="text-slate-400 hover:text-white text-xs underline"><i class="fas fa-sign-out-alt"></i></button>
            </div>

            <div class="flex items-center gap-4 text-white text-lg border-l border-slate-700 pl-5">
                <button id="btn-lang-th" onclick="setLanguage('th')" class="text-xs font-bold text-snap-green hover:text-white">TH</button>
                <span class="text-slate-600 text-xs">|</span>
                <button id="btn-lang-en" onclick="setLanguage('en')" class="text-xs font-bold text-slate-400 hover:text-white">EN</button>
                <div class="relative cursor-pointer hover:text-snap-green ml-2" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 w-4 h-4 bg-snap-green text-white text-[9px] font-black flex items-center justify-center rounded-full hidden">0</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="h-[70px]"></div>

    <!-- PAGE: HOME -->
    <div id="page-home" class="page-section page-active">
        <section class="hero-container w-full min-h-[500px] flex items-center relative overflow-hidden">
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay"></div>
            <div class="max-container flex flex-col md:flex-row items-center justify-between gap-10 z-10">
                <div class="hero-white-box w-full md:w-[500px] p-10 md:p-12 relative">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-emerald-50 text-emerald-600 rounded-full text-[10px] font-black tracking-widest uppercase mb-4 border border-emerald-200">
                        <i class="fas fa-leaf"></i> <span data-i18n="heroEco">Green Technology</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-black text-slate-900 leading-[1.1] mb-8">
                        <span data-i18n="heroText1">Snap to Connect.</span><br>
                        <span data-i18n="heroText2">Ready to Control.</span>
                    </h1>
                    <button onclick="navigate('product')" class="text-snap-green font-bold text-lg hover:text-snap-green-hover flex items-center gap-2 group">
                        <span data-i18n="heroLink">Find out more</span>
                        <i class="fas fa-chevron-right text-sm transition-transform group-hover:translate-x-1"></i>
                    </button>
                </div>

                <div class="hidden md:flex flex-col justify-center flex-1 pl-4 lg:pl-16 z-10 w-full max-w-lg">
                    <div>
                        <h3 class="text-snap-green font-black tracking-widest uppercase text-xs mb-6 border-b border-white/20 pb-4 inline-block drop-shadow-md">Why Snapcon?</h3>
                        <div class="feature-text-container">
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs1Title">⚡ Easy Setup</h4>
                                <p class="text-lg md:text-xl text-emerald-400 font-bold" data-i18n="fs1Desc">Plug & Play ใช้งานได้ทันที</p>
                            </div>
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs2Title">🔗 Seamless Connection</h4>
                                <p class="text-lg md:text-xl text-blue-400 font-bold" data-i18n="fs2Desc">เชื่อม PLC / Sensor ได้ง่าย</p>
                            </div>
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs3Title">📊 Real-Time Monitoring</h4>
                                <p class="text-lg md:text-xl text-amber-400 font-bold" data-i18n="fs3Desc">เห็นข้อมูลทันที</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Feature Dropdowns (แก้ไขเรื่องการดึงข้อมูลจาก Sheets) -->
        <section class="feature-bar w-full relative z-40 border-t border-slate-800">
            <div class="max-container grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-white/10">
                <div tabindex="0" class="dropdown-container relative group p-8 flex flex-col items-center cursor-pointer hover:bg-slate-800 transition-colors focus:outline-none">
                    <i class="fas fa-file-pdf text-4xl text-snap-green mb-4"></i>
                    <h3 data-i18n="cardDataSheet" class="text-xl font-black text-white uppercase">Data Sheet</h3>
                    <p class="text-xs text-slate-400 mt-2" data-i18n="selectModel">Select Model <i class="fas fa-angle-down"></i></p>
                    <div class="dropdown-menu top-full left-0 w-full bg-white shadow-2xl" id="menu-datasheet"></div>
                </div>
                <div tabindex="0" class="dropdown-container relative group p-8 flex flex-col items-center cursor-pointer hover:bg-slate-800 transition-colors focus:outline-none">
                    <i class="fas fa-drafting-compass text-4xl text-blue-500 mb-4"></i>
                    <h3 data-i18n="cardDrawing" class="text-xl font-black text-white uppercase">2D/3D Drawing</h3>
                    <p class="text-xs text-slate-400 mt-2" data-i18n="selectModel">Select Model <i class="fas fa-angle-down"></i></p>
                    <div class="dropdown-menu top-full left-0 w-full bg-white shadow-2xl" id="menu-drawing"></div>
                </div>
                <div tabindex="0" class="dropdown-container relative group p-8 flex flex-col items-center cursor-pointer hover:bg-slate-800 transition-colors focus:outline-none">
                    <i class="fas fa-book-open text-4xl text-amber-500 mb-4"></i>
                    <h3 data-i18n="cardCatalog" class="text-xl font-black text-white uppercase">Catalog</h3>
                    <p class="text-xs text-slate-400 mt-2" data-i18n="btnDownload">Download <i class="fas fa-angle-down"></i></p>
                    <div class="dropdown-menu top-full left-0 w-full bg-white shadow-2xl" id="menu-catalog"></div>
                </div>
            </div>
        </section>

        <!-- Featured Products Slider -->
        <section class="bg-white py-16">
            <div class="max-container">
                <h2 class="text-3xl font-black text-slate-900 uppercase" data-i18n="homeProductsTitle">Featured Products</h2>
                <div class="w-16 h-1 bg-snap-green mt-2 mb-10"></div>
                <div id="home-product-slider" class="flex gap-6 overflow-x-auto snap-x snap-mandatory pb-4 custom-scrollbar"></div>
            </div>
        </section>

        <!-- KNOWLEDGE & INSIGHT SECTION -->
        <section class="bg-slate-50 py-20 border-t border-slate-200">
            <div class="max-container">
                <div class="flex justify-between items-end mb-12">
                    <div>
                        <h2 class="text-3xl font-black text-slate-900 uppercase">Knowledge & Insight</h2>
                        <p class="text-slate-500 font-medium" data-i18n="knowledgeSub">บทความเทคนิคและคลังความรู้จากวิศวกรผู้เชี่ยวชาญ</p>
                    </div>
                </div>
                <div id="article-list" class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Articles will load here -->
                </div>
            </div>
        </section>
    </div>

    <!-- PAGE: PRODUCT -->
    <div id="page-product" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageProductTitle" class="text-3xl font-black text-slate-900 uppercase mb-2">Conveyor Systems</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="product-grid"></div>
        </div>
    </div>

    <!-- PAGE: SPARE PARTS -->
    <div id="page-spare" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageSpareTitle" class="text-3xl font-black text-slate-900 uppercase mb-2">Spare Parts</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4" id="spare-grid"></div>
        </div>
    </div>

    <!-- PAGE: PROJECT REFERENCE -->
    <div id="page-project" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="pageProjectTitle" class="text-3xl font-black text-slate-900 uppercase mb-2">Project Reference</h2>
            <div class="w-16 h-1 bg-snap-green mb-12"></div>
            
            <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <i class="fas fa-rocket text-snap-green"></i> <span data-i18n="projPilotTitle">Pilot / Demo Project</span>
            </h3>
            <div id="project-pilot-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16"></div>
            
            <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <i class="fas fa-industry text-blue-500"></i> <span data-i18n="projUseCaseTitle">Use Case / Application</span>
            </h3>
            <div id="project-usecase-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6"></div>
        </div>
    </div>

    <!-- PAGE: CART / QUOTATION -->
    <div id="page-cart" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-container max-w-4xl py-10">
            <h2 data-i18n="pageCartTitle" class="text-3xl font-black text-slate-900 uppercase mb-2">Quotation Request</h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <div class="bg-white p-8 sharp-card">
                <div id="cart-header" class="flex justify-between items-center mb-6 pb-4 border-b">
                    <div class="flex items-center gap-3">
                        <input type="checkbox" id="cart-select-all" onclick="toggleSelectAll(this.checked)" class="w-4 h-4 accent-snap-green cursor-pointer">
                        <label for="cart-select-all" class="font-bold text-sm cursor-pointer" data-i18n="selectAll">เลือกทั้งหมด</label>
                    </div>
                    <button onclick="deleteSelected()" class="text-red-500 font-bold text-sm underline hover:text-red-700" data-i18n="deleteSelected">ลบที่เลือก</button>
                </div>
                <div id="cart-items" class="space-y-3 mb-10 max-h-[50vh] overflow-y-auto custom-scrollbar pr-2"></div>
                <div id="quote-contact-form" class="bg-slate-50 p-6 sharp-card mb-8 hidden">
                    <p class="font-bold text-slate-700 mb-4 uppercase text-xs tracking-widest"><i class="fas fa-info-circle text-snap-green"></i> <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ</span></p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <input type="text" id="quote-name" placeholder="ชื่อ / บริษัท" class="px-4 py-3 bg-white border outline-none focus:border-snap-green sharp-card">
                        <input type="text" id="quote-contact" placeholder="อีเมล / เบอร์โทร" class="px-4 py-3 bg-white border outline-none focus:border-snap-green sharp-card">
                    </div>
                </div>
                <div class="flex flex-col md:flex-row justify-between items-center pt-8 border-t gap-6">
                    <div>
                        <p class="text-slate-500 text-xs font-bold uppercase tracking-widest" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                        <h3 id="cart-total" class="text-5xl font-black text-snap-green tracking-tighter">฿0</h3>
                    </div>
                    <button onclick="requestQuote()" class="w-full md:w-auto bg-snap-black text-white px-8 py-4 font-bold hover:bg-snap-green sharp-btn" data-i18n="btnRequestQuote">ยื่นขอใบเสนอราคา</button>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: DASHBOARD -->
    <div id="page-dashboard" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">
                <span data-i18n="navDashboard">Dashboard</span> : <span id="dash-user-name" class="text-snap-green"></span>
            </h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-8" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card lg:col-span-2 flex flex-col justify-center rounded-2xl">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 font-bold hover:bg-snap-green-hover rounded-xl text-xs"><i class="fas fa-play mr-2"></i> START</button>
                        <button onclick="stopSystem()" id="btn-stop" class="bg-slate-200 text-slate-700 py-3 font-bold hover:bg-red-500 hover:text-white rounded-xl text-xs"><i class="fas fa-stop mr-2"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-3 font-bold hover:bg-slate-800 rounded-xl text-xs"><i class="fas fa-sync-alt mr-2"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-3 font-bold hover:bg-blue-700 rounded-xl text-xs"><i class="fas fa-file-csv mr-2"></i> REPORT</button>
                    </div>
                </div>
                <div class="bg-white p-6 sharp-card rounded-2xl">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCfgTitle">Configuration</h3>
                    <div class="space-y-3">
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashTarget">Target</label>
                            <input type="number" id="cfg-target" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                        <div class="flex justify-between items-center border-b border-slate-100 pb-2">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashCarbon">Carbon Factor</label>
                            <input type="number" step="0.0001" id="cfg-carbon" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                        <div class="flex justify-between items-center">
                            <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest" data-i18n="dashEnergy">Energy Factor</label>
                            <input type="number" step="0.001" id="cfg-energy" onchange="updateDashboardConfig()" class="w-24 text-right outline-none font-black text-slate-800 bg-transparent">
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card rounded-2xl border-t-4 border-t-blue-500">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotOut">Total Output</p>
                    <h3 id="dash-total-output" class="text-4xl font-black text-slate-900 tracking-tighter">0</h3>
                </div>
                <div class="bg-white p-6 sharp-card rounded-2xl border-t-4 border-t-snap-green">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashCalCarbon">Cal Carbon</p>
                    <h3 id="dash-carbon" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
                <div class="bg-white p-6 sharp-card rounded-2xl border-t-4 border-t-amber-500">
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1" data-i18n="dashTotPower">Total Power</p>
                    <h3 id="dash-power" class="text-4xl font-black text-slate-900 tracking-tighter">0.00</h3>
                </div>
            </div>

            <div class="bg-white p-8 sharp-card rounded-2xl mb-8">
                <div class="flex justify-between items-end mb-4">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashPlanTitle">Production Planning</h3>
                    <span id="dash-progress-text" class="text-2xl font-black text-snap-green">0.0%</span>
                </div>
                <div class="w-full h-4 bg-slate-100 rounded-full overflow-hidden mb-6">
                    <div id="dash-progress-bar" class="h-full bg-snap-green transition-all duration-300" style="width: 0%"></div>
                </div>
                <div class="flex justify-between text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <span><i class="far fa-clock mr-1"></i> <span data-i18n="dashTimeElapsed">Elapsed</span>: <span id="dash-time-elapsed" class="text-slate-800">00:00:00</span></span>
                    <span><i class="fas fa-hourglass-half mr-1"></i> <span data-i18n="dashTimeRemain">ETA</span>: <span id="dash-time-remain" class="text-slate-800">--:--:--</span></span>
                </div>
            </div>

            <div class="bg-white p-6 sharp-card rounded-2xl">
                <div class="flex justify-between items-center mb-6">
                    <h3 class="font-bold text-slate-800 uppercase text-xs tracking-widest" data-i18n="dashMacStatus2">Machine Status</h3>
                    <div class="flex gap-4 text-[9px] font-bold uppercase tracking-widest text-slate-500">
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-snap-green rounded-full"></div> <span data-i18n="statusNormal">Normal</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-amber-400 rounded-full"></div> <span data-i18n="statusWarning">Warning</span></span>
                        <span class="flex items-center gap-1"><div class="w-2 h-2 bg-red-500 rounded-full"></div> <span data-i18n="statusMaint">Maint.</span></span>
                    </div>
                </div>
                <div id="dash-nodes-grid" class="grid grid-cols-2 md:grid-cols-5 lg:grid-cols-10 gap-4 max-h-[60vh] overflow-y-auto custom-scrollbar p-1">
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: COMPANY (อัปเดตใหม่ สมบูรณ์แบบ) -->
    <div id="page-about" class="page-section bg-white min-h-screen pt-10">
        <div class="max-container py-10">
            <h2 data-i18n="navAbout" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Company</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            
            <div class="grid md:grid-cols-2 gap-10 items-center mb-16">
                <div>
                    <h3 class="text-4xl font-black text-snap-black tracking-tighter mb-6 leading-tight">Driving the future of <br><span class="text-snap-green">industrial automation.</span></h3>
                    <p class="text-slate-600 leading-relaxed mb-6">
                        Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System เรามุ่งมั่นที่จะพลิกโฉมวงการออโตเมชันด้วยโซลูชันที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และเพิ่มประสิทธิภาพการผลิตสูงสุด
                    </p>
                </div>
                <div class="h-64 md:h-80 sharp-card overflow-hidden relative group rounded-2xl shadow-lg border border-slate-200">
                    <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute inset-0 bg-snap-green/10 group-hover:bg-transparent transition-colors duration-500 pointer-events-none"></div>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-snap-black text-white p-10 sharp-card border-none rounded-2xl">
                    <i class="fas fa-eye text-4xl text-snap-green mb-6"></i>
                    <h4 class="text-2xl font-bold mb-4 uppercase tracking-wider">Vision</h4>
                    <p class="text-slate-400 leading-relaxed">มุ่งมั่นที่จะเป็นผู้นำอันดับหนึ่งในด้านระบบอัตโนมัติแบบ Plug & Play ที่เข้าถึงง่ายและล้ำสมัยที่สุดในภูมิภาคเอเชียตะวันออกเฉียงใต้</p>
                </div>
                <div class="bg-snap-green text-white p-10 sharp-card border-none rounded-2xl">
                    <i class="fas fa-bullseye text-4xl text-snap-black mb-6"></i>
                    <h4 class="text-2xl font-bold mb-4 uppercase tracking-wider text-snap-black">Mission</h4>
                    <p class="text-emerald-900 leading-relaxed font-medium">พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาในการติดตั้ง และยกระดับประสิทธิภาพการทำงานของอุตสาหกรรมทุกขนาดให้พร้อมแข่งขันในระดับโลก</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE: SUPPORT / CONTACT (อัปเดตใหม่ให้ใช้งานฟอร์มส่งเข้า Sheet ได้) -->
    <div id="page-contact" class="page-section bg-snap-gray min-h-screen pt-10">
        <div class="max-container max-w-5xl py-10">
            <h2 data-i18n="navContact" class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">Support</h2>
            <div class="w-16 h-1 bg-snap-green mb-10"></div>
            
            <div class="grid md:grid-cols-2 gap-8 items-start">
                <!-- ข้อมูลติดต่อด่วน -->
                <div class="bg-white sharp-card p-10 text-left rounded-2xl shadow-sm h-full border border-slate-200">
                    <i class="fas fa-headset text-5xl text-snap-green mb-6"></i>
                    <h3 class="text-2xl font-black text-slate-900 mb-2">Technical Support 24/7</h3>
                    <p class="text-slate-500 mb-8 text-sm">ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ</p>
                    
                    <div class="space-y-4 mb-10">
                        <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card rounded-xl border border-slate-100">
                            <i class="fas fa-envelope text-slate-400 text-xl"></i>
                            <span class="font-bold text-slate-700">snapcon1992@gmail.com</span>
                        </div>
                        <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card rounded-xl border border-slate-100">
                            <i class="fab fa-line text-[#00B900] text-2xl"></i>
                            <span class="font-bold text-slate-700">@SnapconAuto</span>
                        </div>
                        <div class="flex items-center gap-4 bg-slate-50 p-4 sharp-card rounded-xl border border-slate-100">
                            <i class="fas fa-phone-alt text-slate-400 text-xl"></i>
                            <span class="font-bold text-slate-700">081-XXX-XXXX</span>
                        </div>
                    </div>
                </div>

                <!-- ฟอร์มติดต่อส่งเข้า Google Sheets -->
                <div class="bg-white p-10 sharp-card shadow-sm rounded-2xl h-full border border-slate-200">
                    <h3 class="text-xl font-black text-slate-900 mb-6 uppercase tracking-widest"><i class="fas fa-paper-plane text-snap-green mr-2"></i> ส่งข้อความถึงเรา</h3>
                    <div class="space-y-5">
                        <div>
                            <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1">ชื่อ-นามสกุล / บริษัท</label>
                            <input type="text" id="contact-name" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green sharp-card text-sm rounded-lg" placeholder="กรอกชื่อของคุณ">
                        </div>
                        <div>
                            <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1">อีเมล / เบอร์โทรติดต่อกลับ</label>
                            <input type="text" id="contact-info" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green sharp-card text-sm rounded-lg" placeholder="กรอกข้อมูลติดต่อกลับ">
                        </div>
                        <div>
                            <label class="block text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1">รายละเอียด / คำถาม</label>
                            <textarea id="contact-message" rows="4" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 outline-none focus:border-snap-green sharp-card text-sm rounded-lg custom-scrollbar" placeholder="พิมพ์ข้อความของคุณที่นี่..."></textarea>
                        </div>
                        <button onclick="submitContactForm()" class="w-full bg-snap-black text-white px-8 py-4 font-bold hover:bg-snap-green sharp-btn text-sm transition-all rounded-lg mt-2">
                            SEND MESSAGE
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL: REGISTER -->
    <div id="modal-register" class="fixed inset-0 bg-snap-black/80 backdrop-blur-sm z-[100] hidden items-center justify-center p-4">
        <div class="bg-white w-full max-w-md sharp-card shadow-2xl relative p-8 rounded-2xl">
            <button onclick="closeRegisterModal()" class="absolute top-4 right-4 text-slate-400 hover:text-red-500 text-xl"><i class="fas fa-times"></i></button>
            <h3 class="text-xl font-black text-slate-900 uppercase mb-6" data-i18n="regTitle">Create Account</h3>
            <div class="space-y-4">
                <input type="text" id="reg-id" placeholder="User ID" class="w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:border-snap-green bg-slate-50">
                <input type="password" id="reg-pass" placeholder="Password" class="w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:border-snap-green bg-slate-50">
                <input type="text" id="reg-name" placeholder="Name / Company" class="w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:border-snap-green bg-slate-50">
                <input type="text" id="reg-contact" placeholder="Email / Phone" class="w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:border-snap-green bg-slate-50">
                <button onclick="submitRegistration()" class="w-full bg-snap-green text-white py-4 font-bold hover:bg-snap-green-hover rounded-lg uppercase tracking-widest mt-2" data-i18n="btnSubmitReg">Confirm</button>
            </div>
        </div>
    </div>
    
    <!-- Floating Support Button -->
    <button onclick="navigate('contact')" class="fixed bottom-6 right-6 w-16 h-16 bg-snap-black text-white rounded-full shadow-[0_15px_35px_rgba(0,0,0,0.4)] flex items-center justify-center text-2xl hover:bg-snap-green transition-all z-50 group border-[3px] border-white hover:scale-110 cursor-pointer">
        <i class="fas fa-headset group-hover:animate-pulse"></i>
    </button>

    <script>
        // =========================================================================
        // JAVASCRIPT SYSTEM (STABLE VERSION 4.0 - AUTO FALLBACK & ROBUST MAPPING)
        // =========================================================================
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxaV4oNSs0eWV5TOsVU9Ky8pl08d7f8H4L98vb1-ZLFQn95q4Kiy15ZqC34hrKoziYl/exec';
        
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [], products = [], spares = [], documents = [], projects = [], articles = [], allItems = [];
        let currentUserId = null, memoryUsers = { '001': '123', 'admin': 'admin' };

        // 1. Helper: แปลงลิงก์ Google Drive ให้เป็น Direct Image Link
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

        // Helper: จัดการหัวตารางที่มีช่องว่าง ตัวพิมพ์เล็กพิมพ์ใหญ่ ให้อ่านได้ 100%
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

        // 2. โหลดข้อมูลทั้งหมดจาก Google Sheets
        async function loadDataFromSheet() {
            try {
                console.log("Fetching data from Google Sheets...");
                const response = await fetch(GOOGLE_SCRIPT_URL + "?t=" + Date.now());
                if (!response.ok) throw new Error("Network response was not ok");
                
                const data = await response.json();
                console.log("Data successfully loaded:", data);
                
                // นำข้อมูลไป Normalize เพื่อให้โค้ดอ่านได้เสมอ ไม่ว่าผู้ใช้จะพิมพ์หัวตารางแบบไหน
                products = normalizeKeys(data.products);
                spares = normalizeKeys(data.spares);
                documents = normalizeKeys(data.documents);
                projects = normalizeKeys(data.projects);
                articles = normalizeKeys(data.articles);
                
                allItems = [...products, ...spares];
                
                // สั่ง Render หน้าจอต่างๆ
                try { renderProducts(); } catch(e) { console.error("Error products", e); }
                try { renderDocuments(); } catch(e) { console.error("Error documents", e); }
                try { renderProjects(); } catch(e) { console.error("Error projects", e); }
                try { renderArticles(); } catch(e) { console.error("Error articles", e); }
                if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
                
            } catch (e) { 
                console.error("Fetch Error:", e); 
            }
        }

        // 3. Render: สินค้าและอะไหล่
        function renderProducts() {
            const pGrid = document.getElementById('product-grid');
            const sGrid = document.getElementById('spare-grid');
            const slider = document.getElementById('home-product-slider');

            const makeCard = (p) => `
                <div class="bg-white sharp-card p-4 flex flex-col h-full rounded-2xl shadow-sm">
                    <div class="bg-slate-50 h-40 flex items-center justify-center p-2 mb-3 overflow-hidden rounded-xl border border-slate-100">
                        <img src="${getValidImageUrl(p.img || p.imageurl || p.image)}" onerror="this.src='https://via.placeholder.com/200'" class="max-h-full max-w-full object-contain mix-blend-multiply">
                    </div>
                    <h4 class="font-black text-sm text-slate-900 mb-2 truncate" title="${p.name || p.title}">${p.name || p.title}</h4>
                    <p class="text-snap-green font-black text-lg mb-4 mt-auto">฿${parseFloat(p.price || 0).toLocaleString()}</p>
                    <button onclick="addToCart('${p.id}')" class="w-full bg-slate-100 text-slate-700 py-3 rounded-lg font-bold text-xs hover:bg-snap-green hover:text-white transition-colors">ADD TO CART</button>
                </div>`;

            if(pGrid) pGrid.innerHTML = products.map(makeCard).join('');
            if(sGrid) sGrid.innerHTML = spares.map(makeCard).join('');
            if(slider) slider.innerHTML = products.slice(0, 10).map(p => `
                <div onclick="navigate('product')" class="min-w-[250px] snap-center bg-white border border-slate-100 p-4 rounded-2xl shadow-sm hover:shadow-lg transition-all cursor-pointer">
                    <div class="overflow-hidden rounded-xl mb-3 relative h-32 bg-slate-50 border border-slate-100"><img src="${getValidImageUrl(p.img || p.imageurl || p.image)}" class="w-full h-full object-contain mix-blend-multiply p-2"></div>
                    <h4 class="font-black text-sm text-slate-800 mb-1 truncate">${p.name || p.title}</h4>
                    <p class="text-snap-green font-black text-lg mt-auto">฿${parseFloat(p.price || 0).toLocaleString()}</p>
                </div>`).join('');
        }

        // 4. Render: Project Reference (แก้ปัญหารูป Pilot อัตโนมัติ)
        function renderProjects() {
            const pilotGrid = document.getElementById('project-pilot-grid');
            const usecaseGrid = document.getElementById('project-usecase-grid');

            if (pilotGrid) {
                const pilots = projects.filter(p => (p.category||'').toLowerCase().includes('pilot'));
                pilotGrid.innerHTML = pilots.map(p => {
                    let visual = '<i class="fas fa-cogs text-snap-green text-3xl"></i>';
                    
                    let imgSrc = getValidImageUrl(p.imgurl || p.img || p.icon);
                    if (imgSrc && imgSrc.includes('http')) {
                        visual = `<img src="${imgSrc}" class="w-full h-full object-contain p-2">`;
                    } else if (p.icon && !p.icon.includes('http')) {
                        visual = `<i class="${p.icon} text-3xl text-snap-green"></i>`;
                    }
                    
                    const desc = currentLang === 'th' ? (p.descriptionth || p.description) : (p.descriptionen || p.description);

                    return `
                    <div class="bg-slate-50 p-8 sharp-card border border-slate-100 rounded-2xl group flex flex-col items-start h-full">
                        <div class="w-20 h-20 bg-white border border-slate-200 rounded-2xl flex items-center justify-center mb-6 shadow-sm overflow-hidden shrink-0 group-hover:scale-110 transition-transform">
                            ${visual}
                        </div>
                        <h4 class="text-lg font-black text-slate-900 mb-3">${p.title || 'Untitled'}</h4>
                        <p class="text-sm text-slate-600">${desc || ''}</p>
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
                    <div class="bg-white p-6 sharp-card rounded-2xl shadow-sm border-t-4 ${borderCol} flex flex-col items-center text-center h-full">
                        <div class="w-full h-40 bg-slate-100 rounded-xl mb-6 overflow-hidden flex items-center justify-center">
                            <img src="${imgSrc}" class="w-full h-full object-cover mix-blend-multiply opacity-90 hover:scale-110 transition-transform duration-500">
                        </div>
                        <h4 class="text-lg font-black text-slate-900 mb-2">${p.title || 'Untitled'}</h4>
                        <p class="text-sm text-slate-600">${desc || ''}</p>
                    </div>`;
                }).join('') || '<p class="col-span-full text-slate-400 font-bold bg-slate-50 p-8 rounded-2xl text-center">ไม่มีข้อมูล (No Use Cases)</p>';
            }
        }

        // 5. Render: Articles (Knowledge & Insight)
        function renderArticles() {
            const container = document.getElementById('article-list');
            if (!container) return;
            if (!articles || articles.length === 0) {
                container.innerHTML = '<p class="col-span-full text-center text-slate-400 font-bold">กำลังอัปเดตบทความใหม่เร็วๆ นี้...</p>';
                return;
            }
            
            container.innerHTML = articles.map(art => {
                let mediaHtml = '';
                if (art.youtube1) mediaHtml += `<div class="aspect-video mb-2"><iframe class="w-full h-full rounded-xl" src="https://www.youtube.com/embed/${art.youtube1}" frameborder="0" allowfullscreen></iframe></div>`;
                if (art.youtube2) mediaHtml += `<div class="aspect-video mb-2"><iframe class="w-full h-full rounded-xl" src="https://www.youtube.com/embed/${art.youtube2}" frameborder="0" allowfullscreen></iframe></div>`;
                if (!mediaHtml) {
                    let imgSrc = getValidImageUrl(art.imageurl || art.img || art.image);
                    mediaHtml = `<img src="${imgSrc || 'https://via.placeholder.com/400x200'}" class="w-full h-44 object-cover rounded-xl border border-slate-100">`;
                }

                const articleUrl = art.link || art.url || '#';

                return `
                <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition flex flex-col h-full">
                    <div class="p-3">${mediaHtml}</div>
                    <div class="p-6 pt-2 flex flex-col flex-1">
                        <span class="text-snap-green text-[10px] font-black uppercase tracking-widest">${art.category || 'INSIGHT'}</span>
                        <h3 class="text-xl font-black text-slate-900 mt-2 mb-3 line-clamp-2">${art.title || 'Untitled'}</h3>
                        <p class="text-slate-500 text-sm mb-4 line-clamp-2 leading-relaxed">${art.summary || ''}</p>
                        <div class="mt-auto flex justify-between items-center pt-5 border-t border-slate-100">
                            <span class="text-[10px] font-bold text-slate-400 uppercase">${art.date || ''}</span>
                            ${articleUrl !== '#' ? `<a href="${articleUrl}" target="_blank" class="bg-slate-900 text-white px-5 py-2.5 rounded-lg text-xs font-bold hover:bg-snap-green transition-colors">อ่านต่อ</a>` : ''}
                        </div>
                    </div>
                </div>`;
            }).join('');
        }

        // 6. Render: Documents Dropdown (แก้ปัญหาดึงข้อมูลจาก Tab ย่อยแบบ Bulletproof)
        function renderDocuments() {
            const makeMenu = (typeStr) => {
                const filteredDocs = documents.filter(d => {
                    const t = (d.type || d.category || '').toLowerCase();
                    return t.includes(typeStr);
                });
                
                if (filteredDocs.length === 0) {
                    return '<div class="px-8 py-6 text-sm text-slate-400 font-medium text-center bg-slate-50">ไม่มีข้อมูล (No Data)</div>';
                }
                
                return filteredDocs.map(d => {
                    const name = d.modelname || d.name || d.model || d.title || 'Untitled Document';
                    const url = getValidImageUrl(d.fileurl || d.link || d.url || d.file || '#');
                    if(url === '#' || url === '') return '';
                    return `<a href="${url}" target="_blank" class="block px-8 py-4 hover:bg-emerald-50 hover:text-emerald-700 border-b border-slate-100 text-sm font-bold text-slate-700 transition-colors">${name}</a>`;
                }).join('');
            };

            const ds = document.getElementById('menu-datasheet'); if(ds) ds.innerHTML = makeMenu('datasheet');
            const dw = document.getElementById('menu-drawing'); if(dw) dw.innerHTML = makeMenu('drawing');
            const ca = document.getElementById('menu-catalog'); if(ca) ca.innerHTML = makeMenu('catalog');
        }

        // 7. Cart & Post Data System
        function addToCart(id) {
            const item = allItems.find(i => i.id === id);
            if(item) {
                const existing = cart.find(i => i.id === id);
                if(existing) existing.quantity++; else cart.push({...item, cartId: Date.now().toString(), selected: true, quantity: 1});
                updateBadge(); alert("Added to cart!");
            }
        }
        function updateBadge() { const b = document.getElementById('cart-badge'); const count = cart.reduce((s,i)=>s+i.quantity,0); b.innerText=count>99?'99+':count; b.classList.toggle('hidden',count===0); }
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
                container.innerHTML = `<p class="text-center py-10 text-slate-400 font-bold bg-slate-50 border border-slate-100 rounded-xl">ไม่มีสินค้าในรถเข็น</p>`;
                document.getElementById('cart-total').innerText = '฿0'; return;
            }
            container.innerHTML = cart.map(item => `
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center bg-white border border-slate-200 p-5 rounded-xl mb-3 shadow-sm gap-4">
                    <div class="flex items-center gap-5 w-full sm:w-auto flex-1">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleItem('${item.cartId}')" class="w-6 h-6 accent-snap-green cursor-pointer rounded">
                        <div class="w-16 h-16 bg-white border border-slate-100 rounded-lg flex items-center justify-center shrink-0 p-1"><img src="${getValidImageUrl(item.img || item.imageurl)}" class="max-w-full max-h-full object-contain"></div>
                        <div class="flex-1 min-w-0"><span class="font-black text-slate-900 block truncate">${item.name || item.title}</span><span class="text-xs text-slate-400 font-bold">${item.id}</span></div>
                    </div>
                    <div class="flex items-center justify-between w-full sm:w-auto gap-4 mt-3 sm:mt-0">
                        <div class="flex items-center border border-slate-200 rounded-lg overflow-hidden h-10 bg-white">
                            <button onclick="updateQuantity('${item.cartId}', -1)" class="w-10 h-full bg-slate-50 hover:bg-slate-100 font-black border-r border-slate-200 transition-colors">-</button>
                            <span class="w-12 h-full flex items-center justify-center text-sm font-black">${item.quantity}</span>
                            <button onclick="updateQuantity('${item.cartId}', 1)" class="w-10 h-full bg-slate-50 hover:bg-slate-100 font-black border-l border-slate-200 transition-colors">+</button>
                        </div>
                        <span class="font-black text-slate-900 text-xl w-32 text-right shrink-0">฿${(parseFloat(item.price||0) * item.quantity).toLocaleString()}</span>
                    </div>
                </div>`).join('');
            
            const total = cart.filter(i => i.selected).reduce((s, i) => s + (parseFloat(i.price||0) * i.quantity), 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
            document.getElementById('cart-select-all').checked = cart.length > 0 && cart.every(i => i.selected);
        }

        // --- ระบบส่งข้อมูลที่เสถียร ---
        async function sendDataToServer(payloadObj) {
            return fetch(GOOGLE_SCRIPT_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                body: JSON.stringify(payloadObj)
            });
        }

        async function requestQuote() {
            const selected = cart.filter(i => i.selected);
            if(selected.length === 0) return alert("กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น");
            
            const name = document.getElementById('quote-name').value.trim();
            const info = document.getElementById('quote-contact').value.trim();
            if(!name || !info) return alert("กรุณากรอกชื่อและข้อมูลติดต่อกลับให้ครบถ้วน");
            
            const detailsStr = selected.map(i => `- ${i.name||i.title} x${i.quantity} (฿${(parseFloat(i.price||0) * i.quantity).toLocaleString()})`).join('\\n');
            const total = selected.reduce((s, i) => s + (parseFloat(i.price||0) * i.quantity), 0);
            const fullDetails = `Items:\\n${detailsStr}\\n\\nTotal: ฿${total.toLocaleString()}`;
            
            try { 
                await sendDataToServer({ type: "Quotation", name_or_id: name, email: info, details: fullDetails });
                alert("ส่งข้อมูลขอใบเสนอราคาสำเร็จ! ทางเราจะรีบติดต่อกลับครับ");
                cart = cart.filter(i => !i.selected); 
                updateBadge(); renderCart(); navigate('home');
            } catch(e) { console.error("Error", e); }
        }

        async function submitRegistration() {
            const id = document.getElementById('reg-id').value.trim();
            const pass = document.getElementById('reg-pass').value.trim();
            const name = document.getElementById('reg-name').value.trim();
            const contact = document.getElementById('reg-contact').value.trim();
            if(!id || !pass || !name || !contact) return alert("กรุณากรอกข้อมูลให้ครบถ้วน");
            
            try {
                await sendDataToServer({ type: "Registration", name_or_id: id, email: contact, details: name });
                alert("ลงทะเบียนสำเร็จ!");
                closeRegisterModal();
            } catch(e) { console.error("Error", e); }
        }

        // ฟังก์ชันใหม่: สำหรับส่งฟอร์มติดต่อ (Contact Form)
        async function submitContactForm() {
            const name = document.getElementById('contact-name').value.trim();
            const info = document.getElementById('contact-info').value.trim();
            const msg = document.getElementById('contact-message').value.trim();

            if(!name || !info || !msg) return alert("กรุณากรอกข้อมูลให้ครบถ้วนก่อนส่งข้อความ");

            try {
                await sendDataToServer({ type: "Contact Support", name_or_id: name, email: info, details: msg });
                alert("ส่งข้อความสำเร็จ! ทีมงานเทคนิคจะรีบติดต่อกลับครับ");
                document.getElementById('contact-name').value = '';
                document.getElementById('contact-info').value = '';
                document.getElementById('contact-message').value = '';
            } catch(e) {
                console.error("Error", e);
                alert("เกิดข้อผิดพลาดในการส่งข้อมูล");
            }
        }

        // ==========================================
        // 8. DASHBOARD LOGIC & SIMULATION
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
                <div class="bg-slate-50 border border-slate-200 p-3 rounded-xl shadow-sm flex flex-col justify-between h-full">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-[10px] font-bold text-slate-500 truncate" title="${n.name}">${n.name}</span>
                        <div class="w-2 h-2 rounded-full ${dotBg} shrink-0"></div>
                    </div>
                    <h4 class="text-xl font-black text-slate-800 text-center my-2">${n.output}</h4>
                    <div>
                        <div class="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden mt-1">
                            <div class="h-full ${healthBarCol} transition-all duration-500" style="width: ${n.health}%"></div>
                        </div>
                        <p class="text-[9px] text-center mt-1 text-slate-400 font-bold uppercase tracking-widest">Health: ${n.health.toFixed(1)}%</p>
                    </div>
                </div>`;
            }).join('');
        }

        // 9. Navigation & UI States
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
        function setLanguage(l) { currentLang = l; renderProjects(); renderArticles(); if(document.getElementById('page-dashboard').classList.contains('page-active')) renderDashboard(); }
        
        function handleLogin() { 
            const id = document.getElementById('userId').value.trim();
            if (memoryUsers[id] === document.getElementById('userPass').value) {
                isLoggedIn = true; currentUserId = id;
                
                // Initialize Dashboard Data
                if (!userDashboards[id]) userDashboards[id] = createDefaultDash();
                
                document.getElementById('displayUser').innerText = id;
                document.getElementById('dash-user-name').innerText = id; 
                document.getElementById('login-section').classList.replace('lg:flex', 'hidden');
                document.getElementById('user-section').classList.replace('hidden', 'flex');
                alert("Login Successful");
            } else alert("Invalid ID/PW");
        }
        function handleLogout() { 
            if (currentUserId) stopSystem();
            isLoggedIn = false; currentUserId = null; 
            document.getElementById('user-section').classList.replace('flex', 'hidden'); 
            document.getElementById('login-section').classList.replace('hidden', 'lg:flex'); 
            navigate('home'); 
        }
        function checkDashboardAuth() { 
            if (isLoggedIn) navigate('dashboard'); 
            else { alert("Please Login First to access Dashboard"); document.getElementById('userId').focus(); } 
        }

        window.onload = loadDataFromSheet;
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2500, scrolling=True)
