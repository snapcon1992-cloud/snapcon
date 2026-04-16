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

        .feature-text-container { position: relative; height: 140px; width: 100%; display: flex; align-items: center; }
        .feature-text-slide { position: absolute; width: 100%; opacity: 0; transform: translateY(30px); animation: fadeSlideText 18s infinite; }
        .feature-text-slide:nth-child(1) { animation-delay: 0s; } .feature-text-slide:nth-child(2) { animation-delay: 3s; } .feature-text-slide:nth-child(3) { animation-delay: 6s; }
        .feature-text-slide:nth-child(4) { animation-delay: 9s; } .feature-text-slide:nth-child(5) { animation-delay: 12s; } .feature-text-slide:nth-child(6) { animation-delay: 15s; }
        @keyframes fadeSlideText { 0% { opacity: 0; transform: translateY(30px); } 4% { opacity: 1; transform: translateY(0); } 13% { opacity: 1; transform: translateY(0); } 17% { opacity: 0; transform: translateY(-30px); } 100% { opacity: 0; } }
    </style>
</head>
<body class="font-sans text-slate-800">

    <!-- Top Navigation Bar -->
    <nav class="bg-snap-black h-[70px] w-full fixed top-0 z-50 flex items-center justify-between px-6 md:px-10 shadow-md">
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
        <section class="hero-container w-full min-h-[500px] md:min-h-[600px] flex items-center relative z-0 overflow-hidden">
            <div class="absolute inset-0 z-0">
                <div class="slide-img slide-1"></div>
                <div class="slide-img slide-2"></div>
                <div class="slide-img slide-3"></div>
                <div class="slide-img slide-4"></div>
            </div>
            <div class="hero-overlay"></div>

            <div class="w-full max-w-[1400px] mx-auto px-6 md:px-12 flex flex-col md:flex-row items-center justify-between gap-10">
                <div class="hero-white-box w-full md:w-[500px] p-10 md:p-12 z-10 mt-10 md:mt-0 relative">
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
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs4Title">🎛 All-in-One Control</h4>
                                <p class="text-lg md:text-xl text-purple-400 font-bold" data-i18n="fs4Desc">ควบคุมทุกเครื่องในที่เดียว</p>
                            </div>
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs5Title">💰 Cost-Effective</h4>
                                <p class="text-lg md:text-xl text-emerald-400 font-bold" data-i18n="fs5Desc">ถูกกว่า SCADA แบบเดิม</p>
                            </div>
                            <div class="feature-text-slide drop-shadow-xl">
                                <h4 class="text-3xl md:text-4xl font-black text-white mb-2" data-i18n="fs6Title">🛡️ Built-in Poka-Yoke</h4>
                                <p class="text-lg md:text-xl text-rose-400 font-bold" data-i18n="fs6Desc">ระบบป้องกันความผิดพลาดของคน</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Dark Feature Bar -->
        <section class="feature-bar w-full relative z-40 shadow-2xl border-t border-slate-800">
            <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-white/10">
                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-file-pdf text-4xl text-snap-green mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardDataSheet" class="text-xl font-black text-white tracking-wide uppercase">Data Sheet</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-snap-green transition-colors" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="#" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 01</a>
                        <a href="#" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green border-b border-slate-100 text-sm font-bold text-slate-700">Model 02</a>
                        <a href="#" class="block px-8 py-4 hover:bg-slate-50 hover:text-snap-green text-sm font-bold text-slate-700">Model 03</a>
                    </div>
                </div>

                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-drafting-compass text-4xl text-blue-500 mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardDrawing" class="text-xl font-black text-white tracking-wide uppercase">2D/3D Drawing</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-blue-400 transition-colors" data-i18n="selectModel">Select Model <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="#" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 01</a>
                        <a href="#" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-100 text-sm font-bold text-slate-700">Model 02</a>
                        <a href="#" class="block px-8 py-4 hover:bg-blue-50 hover:text-blue-600 text-sm font-bold text-slate-700">Model 03</a>
                    </div>
                </div>

                <div class="dropdown-container relative flex flex-col group">
                    <div class="p-8 md:p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-800 transition-colors h-full">
                        <i class="fas fa-book-open text-4xl text-amber-500 mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 data-i18n="cardCatalog" class="text-xl font-black text-white tracking-wide uppercase">Catalog</h3>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-widest mt-2 group-hover:text-amber-400 transition-colors" data-i18n="btnDownload">Download <i class="fas fa-angle-down ml-1"></i></p>
                    </div>
                    <div class="dropdown-menu top-[100%] left-0 w-full bg-white border border-slate-200 shadow-2xl z-50">
                        <a href="#" data-i18n="cardCatalogFull" class="block px-8 py-4 hover:bg-amber-50 hover:text-amber-600 text-sm font-bold text-slate-700">Download Full Catalog</a>
                    </div>
                </div>
            </div>
        </section>
        
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

                <div id="quote-contact-form" class="bg-slate-50 p-6 sharp-card mb-8 hidden">
                    <p class="font-bold text-slate-700 mb-4 uppercase text-xs tracking-widest flex items-center gap-2">
                        <i class="fas fa-info-circle text-snap-green"></i> 
                        <span data-i18n="guestContactTitle">ข้อมูลติดต่อกลับ (Contact Info)</span>
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <input type="text" id="quote-name" data-i18n-placeholder="phGuestName" placeholder="ชื่อผู้ติดต่อ / ชื่อบริษัท" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green text-sm font-bold sharp-card w-full">
                        <input type="text" id="quote-contact" data-i18n-placeholder="phGuestContact" placeholder="อีเมล หรือ เบอร์โทรศัพท์" class="px-4 py-3 bg-white border border-slate-200 outline-none focus:border-snap-green text-sm font-bold sharp-card w-full">
                    </div>
                </div>

                <div class="flex flex-col md:flex-row justify-between items-center border-t border-slate-200 pt-8 gap-6">
                    <div>
                        <p class="text-slate-500 text-xs font-bold uppercase tracking-widest mb-1" data-i18n="cartTotalLabel">ราคากลางประเมินรวม</p>
                        <h3 id="cart-total" class="text-5xl font-black text-snap-green tracking-tighter">฿0</h3>
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
            <h2 class="text-3xl font-black text-slate-900 uppercase tracking-tight mb-2">
                <span data-i18n="navDashboard">Dashboard</span> : <span id="dash-user-name" class="text-snap-green"></span>
            </h2>
            <div class="w-16 h-1 bg-snap-green mb-8"></div>
            <p class="text-slate-600 mb-8" data-i18n="dashSubTitle">ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์</p>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 sharp-card lg:col-span-2 flex flex-col justify-center">
                    <h3 class="font-bold text-slate-800 mb-4 uppercase text-xs tracking-widest" data-i18n="dashCtrlTitle">System Controls</h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button onclick="startSystem()" id="btn-start" class="bg-snap-green text-white py-3 font-bold hover:bg-snap-green-hover sharp-btn text-xs"><i class="fas fa-play mr-2"></i> START</button>
                        <button onclick="stopSystem()" id="btn-stop" class="bg-slate-200 text-slate-700 py-3 font-bold hover:bg-red-500 hover:text-white sharp-btn text-xs"><i class="fas fa-stop mr-2"></i> STOP</button>
                        <button onclick="resetSystem()" class="bg-snap-black text-white py-3 font-bold hover:bg-slate-800 sharp-btn text-xs"><i class="fas fa-sync-alt mr-2"></i> REFRESH</button>
                        <button onclick="exportCSV()" class="bg-blue-600 text-white py-3 font-bold hover:bg-blue-700 sharp-btn text-xs"><i class="fas fa-file-csv mr-2"></i> REPORT</button>
                    </div>
                </div>
                <div class="bg-white p-6 sharp-card">
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
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE: PROJECT REFERENCE ==================== -->
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
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-snap-green text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                        <i class="fas fa-network-wired"></i>
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot1Title">Snapcon V1</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot1Desc">Multi-machine control demo ควบคุมเครื่องจักรหลายตัวพร้อมกันผ่านศูนย์กลางเดียว</p>
                </div>
                <div class="bg-slate-50 p-8 sharp-card group">
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-blue-500 text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot2Title">Real-time Monitoring</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot2Desc">ติดตามสถานะอุณหภูมิ (Temperature), ความเร็ว (Speed), และยอดผลิต (Output) ทันที</p>
                </div>
                <div class="bg-slate-50 p-8 sharp-card group">
                    <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-rose-500 text-xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-3" data-i18n="pilot3Title">Poka-Yoke Integrated</h4>
                    <p class="text-sm text-slate-600" data-i18n="pilot3Desc">ระบบป้องกันความผิดพลาดจากมนุษย์ แจ้งเตือนและหยุดเครื่องจักรเมื่อพบความผิดปกติ</p>
                </div>
            </div>

            <h3 class="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
                <i class="fas fa-industry text-blue-500"></i> <span data-i18n="projUseCaseTitle">Use Case / Application</span>
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white p-6 sharp-card border-t-4 border-t-amber-500 flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1589792923962-537704632910?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500">
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase1Title">Packaging Line Automation</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase1Desc">ระบบออโตเมชันสำหรับสายงานบรรจุภัณฑ์อัตโนมัติ ลดเวลาและเพิ่มความแม่นยำ</p>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-snap-green flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1513828583688-c52646db42da?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500">
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase2Title">Conveyor System Control</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase2Desc">ระบบควบคุมสายพานลำเลียงอัจฉริยะ ปรับความเร็วอัตโนมัติตามโหลดงาน</p>
                </div>
                <div class="bg-white p-6 sharp-card border-t-4 border-t-blue-500 flex flex-col items-center text-center">
                    <div class="w-full h-40 bg-slate-100 rounded-lg mb-4 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=600&q=80" class="w-full h-full object-cover mix-blend-multiply opacity-80 hover:scale-110 transition-transform duration-500">
                    </div>
                    <h4 class="text-lg font-black text-slate-900 mb-2" data-i18n="usecase3Title">Machine Health Monitoring</h4>
                    <p class="text-sm text-slate-600" data-i18n="usecase3Desc">ระบบเฝ้าระวังสภาพเครื่องจักรเชิงคาดการณ์ แจ้งเตือนก่อนเกิดความเสียหายหนัก</p>
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
                <div class="h-64 md:h-80 sharp-card overflow-hidden relative group rounded-2xl shadow-lg">
                    <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80" alt="Snapcon Automation Facility" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
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

    <!-- ==================== MODALS ==================== -->
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

    <!-- Floating Support Button -->
    <button onclick="openSocialModal()" class="fixed bottom-6 right-6 w-16 h-16 bg-snap-black text-white rounded-full shadow-[0_15px_35px_rgba(0,0,0,0.4)] flex items-center justify-center text-2xl hover:bg-snap-green transition-all z-50 group border-[3px] border-white hover:scale-110 active:scale-95 cursor-pointer">
        <i class="fas fa-user-cog group-hover:animate-pulse"></i>
        <span class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 border-2 border-white rounded-full animate-bounce"></span>
    </button>

    <script>
        // ==========================================
        // 1. GLOBAL VARIABLES & CONFIG
        // ==========================================
        // อัปเดตลิงก์ Google App Script ล่าสุดที่นี่
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyX2EvZJ-lYI54hJpL78sSS8KM2FYsS8_05uQO63iIa-TGzvYXQyCKtUDPP__CtZmhy/exec';
        
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let products = [];
        let spares = [];
        let allItems = [];
        
        // ==========================================
        // 2. USER ISOLATION & MOCK DATA
        // ==========================================
        let currentUserId = null;
        let activeDashInterval = null;
        let memoryUsers = { '001': '123', 'admin': 'admin' };
        
        let userDashboards = {
            '001': {
                isRunning: false, target: 50000, carbonFactor: 0.0072, energyFactor: 0.015, elapsedSeconds: 0,
                nodes: [
                    { id: 1, name: "M-01 Main", output: 0, status: 'Offline', health: 100.0, wearRate: 0.3 },
                    { id: 2, name: "M-02 Sort", output: 0, status: 'Offline', health: 100.0, wearRate: 0.5 },
                    { id: 3, name: "M-03 Pack", output: 0, status: 'Offline', health: 100.0, wearRate: 0.2 },
                    { id: 4, name: "M-04 Seal", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 },
                    { id: 5, name: "M-05 Label", output: 0, status: 'Offline', health: 100.0, wearRate: 0.6 }
                ]
            },
            'admin': {
                isRunning: false, target: 150000, carbonFactor: 0.0050, energyFactor: 0.010, elapsedSeconds: 0,
                nodes: [
                    { id: 1, name: "Admin-Line 1", output: 5000, status: 'Offline', health: 95.0, wearRate: 0.1 },
                    { id: 2, name: "Admin-Line 2", output: 4200, status: 'Offline', health: 88.0, wearRate: 0.2 }
                ]
            }
        };

        function createDefaultDash() {
            return {
                isRunning: false, target: 10000, carbonFactor: 0.0070, energyFactor: 0.015, elapsedSeconds: 0,
                nodes: [
                    { id: 1, name: "Node-01 Main", output: 0, status: 'Offline', health: 100.0, wearRate: 0.3 },
                    { id: 2, name: "Node-02 Sub", output: 0, status: 'Offline', health: 100.0, wearRate: 0.4 }
                ]
            };
        }

        function getDash() {
            if (!currentUserId || !userDashboards[currentUserId]) return null;
            return userDashboards[currentUserId];
        }

        // ==========================================
        // 3. FETCH DYNAMIC DATA (GOOGLE SHEETS)
        // ==========================================
        async function loadDataFromSheet() {
            try {
                // เติมพารามิเตอร์ป้องกัน Cache ของ Browser
                const fetchUrl = GOOGLE_SCRIPT_URL + "?t=" + new Date().getTime();
                console.log("Fetching dynamic data from Google Sheets...");
                
                const response = await fetch(fetchUrl, { redirect: "follow" });
                
                if (!response.ok) throw new Error("Network response was not ok");
                
                const data = await response.json();
                console.log("Raw data from Google Sheets:", data);
                
                if (data.products && data.products.length > 0) {
                    products = data.products.map(p => ({
                        id: p.id || p.ID || p.Id || "N/A",
                        name: p.name || p.Name || "Unnamed",
                        price: parseFloat(p.price || p.Price) || 0,
                        img: p.img || p.Img || p.IMG || "https://i.ibb.co/bZ7TKQg/01.png",
                        specs: { 
                            th: Array.isArray(p.specs_th) ? p.specs_th : (typeof p.specs_th === 'string' ? p.specs_th.split(',') : ["-"]), 
                            en: Array.isArray(p.specs_en) ? p.specs_en : (typeof p.specs_en === 'string' ? p.specs_en.split(',') : ["-"]) 
                        }
                    }));
                }
                
                if (data.spares && data.spares.length > 0) {
                    spares = data.spares.map(s => ({
                        id: s.id || s.ID || "N/A",
                        name: s.name || s.Name || "Unnamed",
                        price: parseFloat(s.price || s.Price) || 0,
                        img: s.img || s.Img || "https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80",
                        specs: { 
                            th: Array.isArray(s.specs_th) ? s.specs_th : (typeof s.specs_th === 'string' ? s.specs_th.split(',') : ["-"]), 
                            en: Array.isArray(s.specs_en) ? s.specs_en : (typeof s.specs_en === 'string' ? s.specs_en.split(',') : ["-"]) 
                        }
                    }));
                }
                
                console.log("Data mapped successfully.");
                allItems = [...products, ...spares];
                
                if (products.length > 0 || spares.length > 0) {
                    renderProducts();
                    if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
                    return; 
                }
                
            } catch (e) {
                console.error("Fetch Error: ไม่สามารถเชื่อมต่อ Google Sheets ได้", e);
                alert("⚠️ ระบบไม่สามารถดึงข้อมูลสินค้าจาก Google Sheets ได้\\nกำลังใช้ข้อมูลจำลอง (Mock Data)\\n\\nกรุณาตรวจสอบว่า App Script ของคุณ:\\n1. ตั้งค่า Deploy ให้เข้าถึงโดย 'Anyone' (ทุกคน) หรือไม่\\n2. ฟังก์ชัน doGet ทำงานถูกต้องหรือไม่");
            }
            
            console.warn("Using fallback mock data due to empty sheet or fetch error.");
            products = [
                { id: 'M01', name: 'Snapcon Model 01 (Mini)', price: 15000, img: 'https://i.ibb.co/bZ7TKQg/01.png', specs: { th: ["L: 0.5-5m", "W: 200-400mm", "Load: 0-50kg"], en: ["L: 0.5-5m", "W: 200-400mm", "Load: 0-50kg"] } },
                { id: 'M02', name: 'Snapcon Model 02 (Std)', price: 22000, img: 'https://i.ibb.co/tTCb2j0h/02.png', specs: { th: ["L: 1-15m", "W: 300-600mm", "Load: 0-100kg"], en: ["L: 1-15m", "W: 300-600mm", "Load: 0-100kg"] } }
            ];
            spares = [
                { id: 'SP001', name: 'Roller Series - P001', price: 525, img: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=400&q=80', specs: { th: ["Type: Roller", "Stock: Ready"], en: ["Type: Roller", "Stock: Ready"] } }
            ];
            
            allItems = [...products, ...spares];
            renderProducts();
            if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        // ==========================================
        // 4. DICTIONARY (i18n)
        // ==========================================
        const dict = {
            th: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroSub: "PLUG & PLAY AUTOMATION", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroLink: "Find out more",
                
                fs1Title: "⚡ Easy Setup", fs1Desc: "Plug & Play ใช้งานได้ทันที",
                fs2Title: "🔗 Seamless Connection", fs2Desc: "เชื่อม PLC / Sensor ได้ง่าย",
                fs3Title: "📊 Real-Time Monitoring", fs3Desc: "เห็นข้อมูลทันที",
                fs4Title: "🎛 All-in-One Control", fs4Desc: "ควบคุมทุกเครื่องในที่เดียว",
                fs5Title: "💰 Cost-Effective", fs5Desc: "ถูกกว่า SCADA แบบเดิม",
                fs6Title: "🛡️ Built-in Poka-Yoke", fs6Desc: "ระบบป้องกันความผิดพลาดของคน",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", 
                cardCatalog: "Catalog", btnDownload: "Download", cardCatalogFull: "Download Full Catalog",
                
                pageProductTitle: "Conveyor Systems", pageProductSub: "ระบบสายพานลำเลียงอัจฉริยะสำหรับอุตสาหกรรมยุคใหม่",
                pageSpareTitle: "Spare Parts", pageSpareSub: "อะไหล่และชิ้นส่วนสายพานลำเลียงคุณภาพสูง",
                pageProjectTitle: "Project Reference", pageProjectSub: "รวมผลงานการติดตั้งและตัวอย่างการประยุกต์ใช้งานระบบ Snapcon ในอุตสาหกรรมจริง",
                projPilotTitle: "Pilot / Demo Project",
                pilot1Title: "Snapcon V1", pilot1Desc: "Multi-machine control demo ควบคุมเครื่องจักรหลายตัวพร้อมกันผ่านศูนย์กลางเดียว",
                pilot2Title: "Real-time Monitoring", pilot2Desc: "ติดตามสถานะอุณหภูมิ (Temperature), ความเร็ว (Speed), และยอดผลิต (Output) ทันที",
                pilot3Title: "Poka-Yoke Integrated", pilot3Desc: "ระบบป้องกันความผิดพลาดจากมนุษย์ แจ้งเตือนและหยุดเครื่องจักรเมื่อพบความผิดปกติ",
                projUseCaseTitle: "Use Case / Application",
                usecase1Title: "Packaging Line Automation", usecase1Desc: "ระบบออโตเมชันสำหรับสายงานบรรจุภัณฑ์อัตโนมัติ ลดเวลาและเพิ่มความแม่นยำ",
                usecase2Title: "Conveyor System Control", usecase2Desc: "ระบบควบคุมสายพานลำเลียงอัจฉริยะ ปรับความเร็วอัตโนมัติตามโหลดงาน",
                usecase3Title: "Machine Health Monitoring", usecase3Desc: "ระบบเฝ้าระวังสภาพเครื่องจักรเชิงคาดการณ์ แจ้งเตือนก่อนเกิดความเสียหายหนัก",
                
                btnAddToCart: "ADD TO CART", pageCartTitle: "Quotation Request", cartEmpty: "ไม่มีสินค้าในรถเข็น",
                cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "ลบที่เลือก", specTitle: "SPECS",
                alertLoginSuccess: "เข้าสู่ระบบสำเร็จ!", alertAddCart: "เพิ่มลงรถเข็นแล้ว", alertQuoteReq: "กรุณาเลือกสินค้า", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อกลับ",
                
                contactSub: "ศูนย์ช่วยเหลือและสนับสนุนด้านเทคนิคอย่างเป็นทางการ", btnEmail: "SEND DIRECT EMAIL",
                aboutDesc: "Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรมยุคใหม่ ที่เน้นความง่ายในการเชื่อมต่อและการติดตั้งในรูปแบบ Plug & Play System",
                aboutVisionTitle: "Vision", aboutVisionDesc: "มุ่งมั่นที่จะเป็นผู้นำด้านระบบอัตโนมัติที่ล้ำสมัยที่สุดในภูมิภาค",
                aboutMissionTitle: "Mission", aboutMissionDesc: "พัฒนานวัตกรรมที่ลดความซับซ้อน ลดเวลาติดตั้ง และยกระดับอุตสาหกรรม",
                
                regTitle: "Create Account", regDesc: "ลงทะเบียนเพื่อเข้าถึงระบบ", btnSubmitReg: "CONFIRM",
                regId: "User ID", regPass: "Password", regName: "Name / Company", regContact: "Email / Phone",
                
                dashSubTitle: "ระบบตรวจสอบระดับองค์กรพร้อมระบบซ่อมบำรุงเชิงคาดการณ์ (แสดงข้อมูลเฉพาะบัญชีของคุณ)",
                dashCtrlTitle: "System Controls", dashCfgTitle: "Configuration", dashTarget: "Target", dashCarbon: "Carbon Factor", dashEnergy: "Energy Factor",
                dashPlanTitle: "Production Planning", dashTotOut: "Total Output", dashCalCarbon: "Cal Carbon", dashTotPower: "Power Use",
                dashTimeElapsed: "Elapsed", dashTimeRemain: "ETA", dashMacStatus2: "Machine Status",
                statusNormal: "Normal", statusWarning: "Warning", statusMaint: "Maint.",
                
                guestContactTitle: "ข้อมูลติดต่อกลับ (Contact Info)", guestNotice: "ข้อมูลปลอดภัยด้วยมาตรฐาน Google",
                phId: "ID", phPass: "PW", phGuestName: "ชื่อผู้ติดต่อ / ชื่อบริษัท", phGuestContact: "อีเมล หรือ เบอร์โทรศัพท์",
                phRegId: "ตั้งรหัส ID สำหรับเข้าระบบ", phRegPass: "ตั้งรหัสผ่านของคุณ", phRegName: "ชื่อ-นามสกุล หรือชื่อบริษัท", phRegContact: "อีเมล หรือ เบอร์โทรศัพท์",
                socialTitle: "ติดต่อช่างผู้เชี่ยวชาญ", socialDesc: "เลือกช่องทางที่สะดวกเพื่อรับคำปรึกษาทันที",
                homeProductsTitle: "Featured Products", homeProductsSub: "เลือกดูเครื่องจักรและอุปกรณ์ออโตเมชันรุ่นล่าสุด", viewAllProducts: "View All Products"
            },
            en: {
                navProduct: "Products", navSpare: "Spare Parts", navDashboard: "Dashboard", navProject: "Projects", navContact: "Support", navAbout: "Company",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                
                heroEco: "Green Technology",
                heroSub: "PLUG & PLAY AUTOMATION", heroText1: "Snap to Connect.", heroText2: "Ready to Control.", heroLink: "Find out more",
                
                fs1Title: "⚡ Easy Setup", fs1Desc: "Plug & Play ready to use",
                fs2Title: "🔗 Seamless Connection", fs2Desc: "Easy PLC / Sensor integration",
                fs3Title: "📊 Real-Time Monitoring", fs3Desc: "Instant data visibility",
                fs4Title: "🎛 All-in-One Control", fs4Desc: "Manage all machines in one place",
                fs5Title: "💰 Cost-Effective", fs5Desc: "More affordable than traditional SCADA",
                fs6Title: "🛡️ Built-in Poka-Yoke", fs6Desc: "Fool-proof system to prevent human errors",
                
                cardDataSheet: "Data Sheet", selectModel: "Select Model",
                cardDrawing: "2D/3D Drawing", 
                cardCatalog: "Catalog", btnDownload: "Download", cardCatalogFull: "Download Full Catalog",
                
                pageProductTitle: "Conveyor Systems", pageProductSub: "Intelligent conveyor systems for modern industries.",
                pageSpareTitle: "Spare Parts", pageSpareSub: "High-quality genuine conveyor components.",
                pageProjectTitle: "Project Reference", pageProjectSub: "Showcasing Snapcon installations and real-world industrial applications.",
                projPilotTitle: "Pilot / Demo Project",
                pilot1Title: "Snapcon V1", pilot1Desc: "Multi-machine control demo managing multiple units from a single hub.",
                pilot2Title: "Real-time Monitoring", pilot2Desc: "Instant tracking of Temperature, Speed, and Output status.",
                pilot3Title: "Poka-Yoke Integrated", pilot3Desc: "Human error prevention system. Alerts and halts machinery upon detecting anomalies.",
                projUseCaseTitle: "Use Case / Application",
                usecase1Title: "Packaging Line Automation", usecase1Desc: "Automated packaging line systems to reduce time and increase precision.",
                usecase2Title: "Conveyor System Control", usecase2Desc: "Intelligent conveyor control system adjusting speed automatically based on workload.",
                usecase3Title: "Machine Health Monitoring", usecase3Desc: "Predictive machine health monitoring. Alerts before critical failures occur.",

                btnAddToCart: "ADD TO CART", pageCartTitle: "Quotation Request", cartEmpty: "Your cart is empty",
                cartTotalLabel: "ESTIMATED TOTAL", btnRequestQuote: "SUBMIT REQUEST", selectAll: "Select All", deleteSelected: "Delete Selected", specTitle: "SPECS",
                alertLoginSuccess: "Login Successful!", alertAddCart: "Added to cart", alertQuoteReq: "Select an item", alertQuoteGuestReq: "Provide contact info",
                
                contactSub: "Official Technical Support & Inquiries", btnEmail: "SEND DIRECT EMAIL",
                aboutDesc: "Snapcon Automation is a leader in modern industrial technology, focusing on ease of connection and installation through Plug & Play Systems.",
                aboutVisionTitle: "Vision", aboutVisionDesc: "To be the leading provider of advanced automation systems in the region.",
                aboutMissionTitle: "Mission", aboutMissionDesc: "Develop innovations that reduce complexity and elevate industrial efficiency.",
                
                regTitle: "Create Account", regDesc: "Register to access the system", btnSubmitReg: "CONFIRM",
                regId: "User ID", regPass: "Password", regName: "Name / Company", regContact: "Email / Phone",
                
                dashSubTitle: "Enterprise Monitoring & Predictive Maintenance System (Private View)",
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

        // ==========================================
        // 5. NAVIGATION & MODALS
        // ==========================================
        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            const target = document.getElementById('page-' + pageId);
            if(target) target.classList.add('page-active');
            if(pageId === 'cart') renderCart();
            if(pageId === 'dashboard') {
                if(!isLoggedIn) {
                    navigate('home');
                    checkDashboardAuth();
                    return;
                }
                renderDashboard();
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function checkDashboardAuth() {
            if (isLoggedIn) navigate('dashboard');
            else { alert(currentLang === 'th' ? "กรุณา Login ก่อนเข้าสู่ Dashboard" : "Please Login to access Dashboard"); document.getElementById('userId').focus(); }
        }

        function openRegisterModal() { document.getElementById('modal-register').classList.replace('hidden', 'flex'); }
        function closeRegisterModal() { document.getElementById('modal-register').classList.replace('flex', 'hidden'); }

        function openSocialModal() { document.getElementById('modal-social').classList.replace('hidden', 'flex'); }
        function closeSocialModal() { document.getElementById('modal-social').classList.replace('flex', 'hidden'); }

        // ==========================================
        // 6. AUTHENTICATION (LOGIN / REGISTER)
        // ==========================================
        function handleLogin() {
            const id = document.getElementById('userId').value.trim();
            const pass = document.getElementById('userPass').value.trim();
            
            if (memoryUsers[id] === pass) {
                isLoggedIn = true;
                currentUserId = id;
                
                if (!userDashboards[id]) userDashboards[id] = createDefaultDash();

                document.getElementById('displayUser').innerText = id;
                document.getElementById('dash-user-name').innerText = id; 
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('login-section').classList.remove('lg:flex');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                
                alert(dict[currentLang].alertLoginSuccess);
                document.getElementById('userId').value = ''; document.getElementById('userPass').value = '';
            } else {
                alert(currentLang === 'th' ? "ID หรือ Password ไม่ถูกต้อง" : "Invalid ID or Password");
            }
        }

        function submitRegistration() {
            const id = document.getElementById('reg-id').value.trim();
            const pass = document.getElementById('reg-pass').value.trim();
            const name = document.getElementById('reg-name').value.trim();
            const contact = document.getElementById('reg-contact').value.trim();
            
            if(!id || !pass || !name || !contact) return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลให้ครบถ้วน" : "Please fill all fields");
            if(memoryUsers[id]) return alert(currentLang === 'th' ? "User ID นี้มีผู้ใช้งานแล้ว กรุณาตั้งใหม่" : "User ID already exists");
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const phoneRegex = /^[0-9]{9,10}$/;
            if (!emailRegex.test(contact) && !phoneRegex.test(contact)) {
                return alert(currentLang === 'th' ? "กรุณากรอกรูปแบบอีเมลหรือเบอร์โทรศัพท์ให้ถูกต้อง" : "Please enter a valid email or phone format");
            }
            if (name.length < 2) {
                return alert(currentLang === 'th' ? "กรุณากรอกชื่อให้ชัดเจน" : "Please enter a valid name");
            }

            memoryUsers[id] = pass;
            userDashboards[id] = createDefaultDash(); 

            try { fetch(GOOGLE_SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: JSON.stringify({ type: "Registration", name_or_id: id, email: contact, details: name }) }); } catch(e) {}
            
            alert(currentLang === 'th' ? "ลงทะเบียนสำเร็จ! ระบบกำลังนำเข้าสู่ระบบอัตโนมัติ..." : "Registered successfully! Auto-logging in...");
            
            isLoggedIn = true;
            currentUserId = id;
            document.getElementById('displayUser').innerText = id;
            document.getElementById('dash-user-name').innerText = id;
            document.getElementById('login-section').classList.add('hidden');
            document.getElementById('login-section').classList.remove('lg:flex');
            document.getElementById('user-section').classList.remove('hidden');
            document.getElementById('user-section').classList.add('flex');
            
            document.getElementById('reg-id').value = '';
            document.getElementById('reg-pass').value = '';
            document.getElementById('reg-name').value = '';
            document.getElementById('reg-contact').value = '';
            
            closeRegisterModal();
        }

        function handleLogout() {
            if (currentUserId) stopSystem();
            isLoggedIn = false;
            currentUserId = null;
            document.getElementById('login-section').classList.remove('hidden'); document.getElementById('login-section').classList.add('lg:flex');
            document.getElementById('user-section').classList.add('hidden'); document.getElementById('user-section').classList.remove('flex');
            navigate('home');
        }

        // ==========================================
        // 7. DASHBOARD LOGIC
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
            let bom = "\\uFEFF";
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

            document.getElementById('cfg-target').value = dash.target;
            document.getElementById('cfg-carbon').value = dash.carbonFactor;
            document.getElementById('cfg-energy').value = dash.energyFactor;

            const totalOutput = dash.nodes.reduce((sum, n) => sum + n.output, 0);
            document.getElementById('dash-total-output').innerText = totalOutput.toLocaleString();
            document.getElementById('dash-carbon').innerText = (totalOutput * dash.carbonFactor).toFixed(2);
            document.getElementById('dash-power').innerText = (totalOutput * dash.energyFactor).toFixed(2);
            
            let progress = (totalOutput / dash.target) * 100; if(progress > 100) progress = 100;
            document.getElementById('dash-progress-bar').style.width = `${progress}%`;
            document.getElementById('dash-progress-text').innerText = `${progress.toFixed(1)}%`;
            
            let elapsedStr = formatTimeStr(dash.elapsedSeconds), remainStr = "--:--:--";
            if (totalOutput > 0 && dash.elapsedSeconds > 0) {
                let ups = totalOutput / dash.elapsedSeconds, remainUnits = dash.target - totalOutput;
                if (remainUnits > 0 && ups > 0) remainStr = formatTimeStr(remainUnits / ups); else if (remainUnits <= 0) remainStr = "00:00:00";
            }
            document.getElementById('dash-time-elapsed').innerText = elapsedStr;
            document.getElementById('dash-time-remain').innerText = remainStr;

            grid.innerHTML = dash.nodes.map(n => {
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

        // ==========================================
        // 8. E-COMMERCE / CART LOGIC
        // ==========================================
        function updateBadge() {
            const b = document.getElementById('cart-badge');
            const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
            if (totalItems > 0) {
                b.innerText = totalItems > 99 ? '99+' : totalItems;
                b.classList.remove('hidden');
            } else {
                b.classList.add('hidden');
            }
        }

        function createItemCard(p) {
            return `
                <div class="bg-white sharp-card p-4 flex flex-col h-full">
                    <div class="bg-slate-50 mb-3 h-40 flex items-center justify-center p-2">
                        <img src="${p.img}" loading="lazy" class="max-h-full max-w-full object-contain mix-blend-multiply">
                    </div>
                    <h4 class="font-black text-sm text-slate-900 mb-2 truncate" title="${p.name}">${p.name}</h4>
                    <div class="bg-slate-50 p-2 mb-3 flex-grow text-[10px] text-slate-600 font-medium space-y-1">
                        ${(p.specs[currentLang] || []).map(s => `<div class="truncate border-b border-slate-200 last:border-0 pb-1 last:pb-0">${s}</div>`).join('')}
                    </div>
                    <p class="text-snap-green font-black text-lg mb-3">฿${(p.price || 0).toLocaleString()}</p>
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
                        <p class="text-snap-green font-black text-lg mt-auto">฿${(p.price || 0).toLocaleString()}</p>
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
            if(!p) return;
            const existing = cart.find(i => i.id === id);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({ ...p, cartId: Date.now() + Math.random(), selected: true, quantity: 1 });
            }
            updateBadge();
            const b = document.getElementById('cart-badge');
            b.classList.add('animate-bounce'); 
            setTimeout(() => b.classList.remove('animate-bounce'), 1000);
            alert(dict[currentLang].alertAddCart);
        }

        function updateQuantity(cartId, delta) {
            const item = cart.find(i => i.cartId === cartId);
            if(item) {
                item.quantity += delta;
                if(item.quantity < 1) item.quantity = 1; 
                renderCart();
                updateBadge();
            }
        }

        function renderCart() {
            const container = document.getElementById('cart-items'); 
            const quoteForm = document.getElementById('quote-contact-form');
            if(!container) return;
            
            if (quoteForm) {
                quoteForm.classList.remove('hidden');
                if (isLoggedIn) {
                    const nameInput = document.getElementById('quote-name');
                    if (nameInput && !nameInput.value) {
                        nameInput.value = document.getElementById('displayUser').innerText;
                    }
                }
            }

            if(cart.length === 0) {
                container.innerHTML = `<p class="text-center py-8 text-slate-400 font-bold text-sm bg-slate-50 border border-slate-100">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }
            container.innerHTML = cart.map(item => `
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center bg-white border border-slate-200 p-5 rounded-xl mb-3 shadow-sm hover:border-snap-green transition-all gap-4">
                    <div class="flex items-center gap-5 w-full sm:w-auto flex-1">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} onclick="toggleItem(${item.cartId})" class="w-6 h-6 accent-snap-green shrink-0 cursor-pointer rounded">
                        <div class="w-16 h-16 bg-white border border-slate-100 rounded-lg flex items-center justify-center shrink-0 p-1">
                            <img src="${item.img}" class="max-w-full max-h-full object-contain mix-blend-multiply">
                        </div>
                        <div class="flex-1 min-w-0 pr-4">
                            <span class="font-black text-slate-900 text-base block truncate">${item.name}</span>
                            <span class="text-xs text-slate-400 font-bold uppercase tracking-widest">${item.id}</span>
                        </div>
                    </div>
                    
                    <div class="flex items-center justify-between w-full sm:w-auto sm:gap-8 pl-14 sm:pl-0 mt-3 sm:mt-0">
                        <div class="flex items-center border border-slate-200 rounded-lg overflow-hidden shrink-0 h-10 shadow-sm bg-white">
                            <button onclick="updateQuantity(${item.cartId}, -1)" class="w-10 h-full bg-slate-50 hover:bg-slate-200 text-slate-600 transition-colors font-black border-r border-slate-200">-</button>
                            <span class="w-12 h-full flex items-center justify-center text-sm font-black text-slate-900">${item.quantity}</span>
                            <button onclick="updateQuantity(${item.cartId}, 1)" class="w-10 h-full bg-slate-50 hover:bg-slate-200 text-slate-600 transition-colors font-black border-l border-slate-200">+</button>
                        </div>
                        <span class="font-black text-slate-900 text-xl w-32 text-right shrink-0">฿${(item.price * item.quantity).toLocaleString()}</span>
                    </div>
                </div>
            `).join('');
            
            const total = cart.filter(i => i.selected).reduce((s, i) => s + (i.price * i.quantity), 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
            document.getElementById('cart-select-all').checked = cart.length > 0 && cart.every(i => i.selected);
        }

        function toggleItem(cartId) { const item = cart.find(i => i.cartId === cartId); if(item) item.selected = !item.selected; renderCart(); }
        function toggleSelectAll(val) { cart.forEach(i => i.selected = val); renderCart(); }
        function deleteSelected() { 
            cart = cart.filter(i => !i.selected); 
            updateBadge();
            renderCart(); 
        }

        async function requestQuote() {
            const selected = cart.filter(i => i.selected);
            if(selected.length === 0) return alert(dict[currentLang].alertQuoteReq);
            
            let name = document.getElementById('quote-name').value.trim();
            let info = document.getElementById('quote-contact').value.trim();
            
            if(!name || !info) {
                return alert(currentLang === 'th' ? "กรุณากรอกข้อมูลติดต่อกลับให้ครบถ้วน" : "Please provide your contact info.");
            }
            
            let detailsForDB = selected.map(i => `- ${i.name} x${i.quantity} (฿${(i.price * i.quantity).toLocaleString()})`).join('\\n');
            let total = selected.reduce((s, i) => s + (i.price * i.quantity), 0);
            
            try { 
                await fetch(GOOGLE_SCRIPT_URL, { 
                    method: 'POST', 
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                    body: JSON.stringify({ 
                        type: "Quotation", 
                        name_or_id: name, 
                        email: info, 
                        details: `Items:\\n${detailsForDB}\\n\\nTotal: ฿${total.toLocaleString()}` 
                    }) 
                }); 
                
                alert(currentLang === 'th' ? "ส่งข้อมูลสำเร็จ! ทางเราจะติดต่อกลับโดยเร็วที่สุด" : "Successfully submitted! We will contact you shortly.");
            } catch(e) { 
                console.error("Error sending to sheets", e); 
                alert(currentLang === 'th' ? "ส่งข้อมูลสำเร็จ! ทางเราจะติดต่อกลับโดยเร็วที่สุด" : "Successfully submitted! We will contact you shortly.");
            }
            
            cart = cart.filter(i => !i.selected); 
            updateBadge(); 
            renderCart(); 
            navigate('home');
        }

        // ==========================================
        // 9. INITIALIZATION & I18N
        // ==========================================
        function setLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('[data-i18n]').forEach(el => { const key = el.getAttribute('data-i18n'); if (dict[lang][key]) el.innerHTML = dict[lang][key]; });
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => { const key = el.getAttribute('data-i18n-placeholder'); if (dict[lang][key]) el.placeholder = dict[lang][key]; });
            
            document.getElementById('btn-lang-th').className = lang === 'th' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            document.getElementById('btn-lang-en').className = lang === 'en' ? "text-xs font-bold text-snap-green" : "text-xs font-bold text-slate-400 hover:text-white";
            
            renderProducts(); 
            if(document.getElementById('page-dashboard').classList.contains('page-active')) renderDashboard(); 
            if(document.getElementById('page-cart').classList.contains('page-active')) renderCart();
        }

        // โหลดข้อมูลอัตโนมัติเมื่อเปิดเว็บ
        window.onload = () => {
            loadDataFromSheet();
            setLanguage('th');
        };
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=2100, scrolling=True)
