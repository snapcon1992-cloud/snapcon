import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit ให้แสดงผลเต็มจอ
st.set_page_config(
    page_title="SNAPCON | Plug & Play", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS ที่จำลองหน้าจอตรงตามรูปภาพ "image_23a9f1.jpg" 100%
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Plug & Play</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=Prompt:wght@400;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'snap-yellow': '#FFF200',
                        'snap-dark': '#2A2A2A',
                    },
                    fontFamily: {
                        sans: ['Inter', 'Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { margin: 0; padding: 0; overflow-x: hidden; scroll-behavior: smooth; background-color: #F8F9FA; }
        ::-webkit-scrollbar { display: none; }
        .hero-clip {
            /* สร้างพื้นที่สีเหลืองซ้ายมือ */
            background-color: #FFF200;
        }
        .hero-bg-image {
            /* ภาพพื้นหลัง Green Technology */
            background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
        }
        input:-webkit-autofill {
            -webkit-box-shadow: 0 0 0 30px white inset !important;
        }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar (ตามรูปเป๊ะๆ) -->
    <nav class="bg-snap-dark h-[60px] w-full fixed top-0 z-50 flex items-center justify-between shadow-md">
        
        <!-- ฝั่งซ้าย: โลโก้ และ เมนู -->
        <div class="flex items-center h-full">
            <!-- กล่อง SNAPCON สีเหลือง -->
            <div class="bg-snap-yellow h-full flex items-center justify-center px-6 min-w-[150px]">
                <span class="font-black text-2xl text-black tracking-tight">SNAPCON</span>
            </div>
            
            <!-- เมนู Products, Automation, ฯลฯ -->
            <div class="hidden lg:flex items-center gap-6 px-6 text-white font-bold text-sm">
                <a href="#" class="hover:text-snap-yellow transition-colors">Products</a>
                <a href="#" class="hover:text-snap-yellow transition-colors">Automation</a>
                <a href="#" class="hover:text-snap-yellow transition-colors">Services</a>
                <a href="#" class="hover:text-snap-yellow transition-colors">Industries</a>
            </div>
        </div>

        <!-- ฝั่งขวา: ปุ่ม Dashboard, Contact, Login Form -->
        <div class="flex items-center h-full pr-4 gap-1 sm:gap-2">
            <!-- ปุ่ม Dashboard & Contact -->
            <button onclick="alert('ไปที่หน้า Dashboard')" class="bg-snap-yellow text-black font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] hover:bg-yellow-400">Dashboard</button>
            <button onclick="alert('ไปที่หน้า Contact')" class="bg-snap-yellow text-black font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] hover:bg-yellow-400">Contact</button>
            
            <!-- ส่วน Login Form (ซ่อนเมื่อ Login สำเร็จ) -->
            <div id="loginForm" class="flex items-center gap-1 sm:gap-2 ml-2">
                <div class="bg-snap-yellow text-black font-bold text-[11px] sm:text-xs px-2 py-1.5 h-[34px] flex items-center">Login</div>
                <span class="text-snap-yellow font-bold text-xs ml-1">ID :</span>
                <input type="text" id="userId" class="h-[30px] w-16 sm:w-24 px-2 text-xs outline-none border-none">
                <span class="text-snap-yellow font-bold text-xs ml-1">Pass</span>
                <input type="password" id="userPass" class="h-[30px] w-16 sm:w-24 px-2 text-xs outline-none border-none">
                <button onclick="handleLogin()" class="bg-snap-yellow text-black font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] ml-1 hover:bg-yellow-400">Registor</button>
            </div>

            <!-- ส่วนแสดงชื่อผู้ใช้ (แสดงเมื่อ Login สำเร็จ) -->
            <div id="loggedInView" class="hidden items-center gap-3 ml-4">
                <span class="text-snap-yellow font-bold text-sm">Hello, <span class="text-white">Watanabe San</span></span>
                <button onclick="handleLogout()" class="text-white text-xs underline hover:text-red-400">Logout</button>
            </div>

            <!-- Icons (Cart & Search) -->
            <div class="flex items-center gap-3 ml-4 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 cursor-pointer hover:text-snap-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 cursor-pointer hover:text-snap-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
            </div>
        </div>
    </nav>

    <!-- 2. Hero Section (แบ่งครึ่งซ้ายเหลือง ขวาภาพ) -->
    <section class="mt-[60px] w-full h-[500px] flex flex-col md:flex-row">
        
        <!-- ฝั่งซ้าย สีเหลือง (Text) -->
        <div class="w-full md:w-[45%] lg:w-[40%] bg-snap-yellow flex flex-col justify-center items-end pr-8 lg:pr-16 py-10 relative">
            <div class="text-right">
                <p class="text-3xl md:text-4xl text-gray-800 mb-1">Snap to Connect.</p>
                <p class="text-3xl md:text-4xl text-gray-800 mb-6 mr-6">Ready to Control.</p>
                <h1 class="text-6xl md:text-7xl font-black text-black tracking-tighter mr-8">Plug & Play</h1>
            </div>
        </div>

        <!-- ฝั่งขวา ภาพพื้นหลังแนว Green Technology + กล่องแดงบนเหลือง -->
        <div class="w-full md:w-[55%] lg:w-[60%] hero-bg-image relative flex items-center justify-center">
            <!-- กล่องจำลองลายน้ำ/ข้อความบนภาพ ตามรูปภาพต้นฉบับเป๊ะๆ -->
            <div class="bg-snap-yellow py-8 px-12 text-center shadow-2xl transform rotate-0 md:-translate-y-6">
                <h2 class="text-red-600 font-black text-4xl mb-2">ภาพพื้นหลัง แนว</h2>
                <h2 class="text-red-600 font-black text-6xl tracking-tight">Green Technology</h2>
            </div>
        </div>

    </section>

    <!-- 3. Bottom Cards Section (ปุ่มดาวน์โหลด 3 กล่องสีเหลือง) -->
    <section class="w-full max-w-7xl mx-auto px-6 py-16">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            <!-- Card 1: Data sheet -->
            <button onclick="openGoogleDrive('datasheet')" class="bg-snap-yellow py-14 px-6 flex flex-col items-center justify-center shadow-md hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer">
                <h3 class="text-3xl font-bold text-black mb-2">Dowload data sheet</h3>
                <p class="text-black text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

            <!-- Card 2: Drawing -->
            <button onclick="openGoogleDrive('drawing')" class="bg-snap-yellow py-14 px-6 flex flex-col items-center justify-center shadow-md hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer">
                <h3 class="text-3xl font-bold text-black mb-2">Dowload drawing</h3>
                <p class="text-black text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

            <!-- Card 3: Catalog -->
            <button onclick="openGoogleDrive('catalog')" class="bg-snap-yellow py-14 px-6 flex flex-col items-center justify-center shadow-md hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer">
                <h3 class="text-3xl font-bold text-black mb-2">Product Catalog</h3>
                <p class="text-black text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

        </div>
    </section>

    <!-- 4. Floating Action Buttons (มุมขวาล่าง) -->
    <div class="fixed bottom-8 right-8 flex flex-col gap-4 z-50">
        <!-- Profile Picture Icon -->
        <div class="w-16 h-16 rounded-full border-4 border-red-600 overflow-hidden bg-white shadow-xl cursor-pointer hover:scale-105 transition-transform">
            <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Support" class="w-full h-full object-cover">
        </div>
        <!-- Scroll to Top Arrow Icon -->
        <button onclick="window.scrollTo(0,0)" class="w-16 h-16 rounded-full border-[3px] border-red-600 bg-white flex items-center justify-center text-red-600 shadow-xl hover:bg-red-50 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 15l7-7 7 7" />
            </svg>
        </button>
    </div>

    <!-- JavaScript Functions -->
    <script>
        // ระบบจำลอง Login (ใช้ ID: 001, Pass: 123 ตามเดิม หรือกด Registor เพื่อ Bypass เข้าสู่ระบบ)
        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            
            // อนุโลมให้กดปุ่มปุ๊บก็จำลองว่า Login สำเร็จเพื่อความรวดเร็ว หรือเช็ครหัสผ่าน
            if ((id === '001' && pass === '123') || (id === '' && pass === '')) {
                document.getElementById('loginForm').classList.add('hidden');
                document.getElementById('loggedInView').classList.remove('hidden');
                document.getElementById('loggedInView').classList.add('flex');
            } else {
                alert('⚠️ ID หรือ Password ไม่ถูกต้อง\\n(ใช้ ID: 001 และ Pass: 123)');
            }
        }

        // ระบบจำลอง Logout
        function handleLogout() {
            document.getElementById('userId').value = '';
            document.getElementById('userPass').value = '';
            document.getElementById('loginForm').classList.remove('hidden');
            document.getElementById('loggedInView').classList.add('hidden');
            document.getElementById('loggedInView').classList.remove('flex');
        }

        // ฟังก์ชันเปิดลิงก์ดาวน์โหลด Google Drive
        function openGoogleDrive(type) {
            let driveUrl = "https://drive.google.com/drive/my-drive";
            alert("กำลังเปิดไฟล์ " + type + " ใน Google Drive...");
            window.open(driveUrl, '_blank');
        }
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=1200, scrolling=True)
