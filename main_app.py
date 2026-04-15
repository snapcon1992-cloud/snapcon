import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit ให้แสดงผลเต็มจอ
st.set_page_config(
    page_title="SNAPCON | Plug & Play", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS โทนสีใหม่แบบ Dark Tech (#0e1117)
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
                        'main-bg': '#0e1117',
                        'card-bg': '#1c1f26',
                        'primary': '#00d4ff',
                        'text-main': '#ffffff',
                        'success': '#00ff88',
                        'alert': '#ff4d4d'
                    },
                    fontFamily: {
                        sans: ['Inter', 'Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { 
            margin: 0; 
            padding: 0; 
            overflow-x: hidden; 
            scroll-behavior: smooth; 
            background-color: #0e1117; /* Background */
            color: #ffffff; /* Text */
        }
        ::-webkit-scrollbar { display: none; }
        .hero-bg-image {
            /* ภาพพื้นหลังอุตสาหกรรม/เทคโนโลยี */
            background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
        }
        input:-webkit-autofill {
            -webkit-box-shadow: 0 0 0 30px #0e1117 inset !important;
            -webkit-text-fill-color: #ffffff !important;
        }
    </style>
</head>
<body class="bg-main-bg text-text-main">

    <!-- 1. Top Navigation Bar -->
    <nav class="bg-card-bg h-[60px] w-full fixed top-0 z-50 flex items-center justify-between shadow-[0_4px_20px_rgba(0,0,0,0.5)] border-b border-gray-800">
        
        <!-- ฝั่งซ้าย: โลโก้ และ เมนู -->
        <div class="flex items-center h-full">
            <!-- กล่อง SNAPCON -->
            <div class="bg-primary h-full flex items-center justify-center px-6 min-w-[150px]">
                <span class="font-black text-2xl text-main-bg tracking-tight">SNAPCON</span>
            </div>
            
            <!-- เมนู Products, Automation, ฯลฯ -->
            <div class="hidden lg:flex items-center gap-6 px-6 font-bold text-sm text-text-main">
                <a href="#" class="hover:text-primary transition-colors">Products</a>
                <a href="#" class="hover:text-primary transition-colors">Automation</a>
                <a href="#" class="hover:text-primary transition-colors">Services</a>
                <a href="#" class="hover:text-primary transition-colors">Industries</a>
            </div>
        </div>

        <!-- ฝั่งขวา: ปุ่ม Dashboard, Contact, Login Form -->
        <div class="flex items-center h-full pr-4 gap-1 sm:gap-2">
            <!-- ปุ่ม Dashboard & Contact -->
            <button onclick="alert('ไปที่หน้า Dashboard')" class="bg-primary text-main-bg font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] rounded hover:opacity-80 transition-opacity">Dashboard</button>
            <button onclick="alert('ไปที่หน้า Contact')" class="bg-primary text-main-bg font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] rounded hover:opacity-80 transition-opacity">Contact</button>
            
            <!-- ส่วน Login Form (ซ่อนเมื่อ Login สำเร็จ) -->
            <div id="loginForm" class="flex items-center gap-1 sm:gap-2 ml-2">
                <div class="bg-primary text-main-bg font-bold text-[11px] sm:text-xs px-2 py-1.5 h-[34px] flex items-center rounded">Login</div>
                <span class="text-primary font-bold text-xs ml-1">ID :</span>
                <input type="text" id="userId" class="h-[30px] w-16 sm:w-24 px-2 text-xs outline-none bg-main-bg border border-gray-700 rounded text-text-main focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                <span class="text-primary font-bold text-xs ml-1">Pass</span>
                <input type="password" id="userPass" class="h-[30px] w-16 sm:w-24 px-2 text-xs outline-none bg-main-bg border border-gray-700 rounded text-text-main focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                <button onclick="handleLogin()" class="bg-primary text-main-bg font-bold text-[11px] sm:text-xs px-2 sm:px-4 py-1.5 h-[34px] ml-1 rounded hover:opacity-80 transition-opacity">Registor</button>
            </div>

            <!-- ส่วนแสดงชื่อผู้ใช้ (แสดงเมื่อ Login สำเร็จ) -->
            <div id="loggedInView" class="hidden items-center gap-3 ml-4">
                <span class="text-primary font-bold text-sm">Hello, <span class="text-text-main">Watanabe San</span></span>
                <button onclick="handleLogout()" class="text-gray-400 text-xs underline hover:text-alert transition-colors">Logout</button>
            </div>

            <!-- Icons (Cart & Search) -->
            <div class="flex items-center gap-3 ml-4 text-text-main">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 cursor-pointer hover:text-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 cursor-pointer hover:text-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
            </div>
        </div>
    </nav>

    <!-- 2. Hero Section -->
    <section class="mt-[60px] w-full h-[500px] flex flex-col md:flex-row border-b border-gray-800">
        
        <!-- ฝั่งซ้าย: พื้นหลังสี Card (#1c1f26) -->
        <div class="w-full md:w-[45%] lg:w-[40%] bg-card-bg flex flex-col justify-center items-end pr-8 lg:pr-16 py-10 relative">
            <div class="text-right z-10">
                <p class="text-3xl md:text-4xl text-text-main mb-1">Snap to Connect.</p>
                <p class="text-3xl md:text-4xl text-text-main mb-6 mr-6">Ready to Control.</p>
                <!-- เน้นคำด้วยสี Primary (#00d4ff) -->
                <h1 class="text-6xl md:text-7xl font-black text-primary tracking-tighter mr-8 drop-shadow-[0_0_15px_rgba(0,212,255,0.3)]">Plug & Play</h1>
            </div>
            <!-- เงาสะท้อนตกแต่ง -->
            <div class="absolute bottom-0 right-0 w-64 h-64 bg-primary rounded-full blur-[100px] opacity-10 pointer-events-none"></div>
        </div>

        <!-- ฝั่งขวา: ภาพพื้นหลัง (ลบข้อความออกตามคำสั่ง) -->
        <div class="w-full md:w-[55%] lg:w-[60%] hero-bg-image relative flex items-center justify-center">
            <!-- Overlay เพื่อให้ภาพกลมกลืนกับธีมมืด -->
            <div class="absolute inset-0 bg-gradient-to-r from-card-bg to-transparent opacity-80"></div>
        </div>

    </section>

    <!-- 3. Bottom Cards Section -->
    <section class="w-full max-w-7xl mx-auto px-6 py-16">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            <!-- Card 1: Data sheet -->
            <button onclick="openGoogleDrive('datasheet')" class="bg-card-bg border border-gray-800 rounded-2xl py-14 px-6 flex flex-col items-center justify-center hover:shadow-[0_0_20px_rgba(0,212,255,0.15)] hover:border-primary hover:-translate-y-1 transition-all cursor-pointer group w-full">
                <h3 class="text-2xl font-bold text-text-main mb-2 group-hover:text-primary transition-colors">Download data sheet</h3>
                <p class="text-gray-400 text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

            <!-- Card 2: Drawing -->
            <button onclick="openGoogleDrive('drawing')" class="bg-card-bg border border-gray-800 rounded-2xl py-14 px-6 flex flex-col items-center justify-center hover:shadow-[0_0_20px_rgba(0,212,255,0.15)] hover:border-primary hover:-translate-y-1 transition-all cursor-pointer group w-full">
                <h3 class="text-2xl font-bold text-text-main mb-2 group-hover:text-primary transition-colors">Download drawing</h3>
                <p class="text-gray-400 text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

            <!-- Card 3: Catalog -->
            <button onclick="openGoogleDrive('catalog')" class="bg-card-bg border border-gray-800 rounded-2xl py-14 px-6 flex flex-col items-center justify-center hover:shadow-[0_0_20px_rgba(0,212,255,0.15)] hover:border-primary hover:-translate-y-1 transition-all cursor-pointer group w-full">
                <h3 class="text-2xl font-bold text-text-main mb-2 group-hover:text-primary transition-colors">Product Catalog</h3>
                <p class="text-gray-400 text-sm font-medium">(ใช้ไฟล์จริงใน Google drive)</p>
            </button>

        </div>
    </section>

    <!-- 4. Floating Action Buttons (มุมขวาล่าง) -->
    <div class="fixed bottom-8 right-8 flex flex-col gap-4 z-50">
        <!-- Profile Picture Icon -->
        <div class="w-16 h-16 rounded-full border-2 border-primary overflow-hidden bg-card-bg shadow-[0_0_15px_rgba(0,212,255,0.3)] cursor-pointer hover:scale-105 transition-transform">
            <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80" alt="Support" class="w-full h-full object-cover">
        </div>
        <!-- Scroll to Top Arrow Icon -->
        <button onclick="window.scrollTo(0,0)" class="w-16 h-16 rounded-full border-2 border-primary bg-card-bg flex items-center justify-center text-primary shadow-[0_0_15px_rgba(0,212,255,0.3)] hover:bg-primary hover:text-main-bg transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 15l7-7 7 7" />
            </svg>
        </button>
    </div>

    <!-- JavaScript Functions -->
    <script>
        // ระบบจำลอง Login
        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            
            if ((id === '001' && pass === '123') || (id === '' && pass === '')) {
                document.getElementById('loginForm').classList.add('hidden');
                document.getElementById('loggedInView').classList.remove('hidden');
                document.getElementById('loggedInView').classList.add('flex');
            } else {
                alert('⚠️ ID หรือ Password ไม่ถูกต้อง\\n(ใช้ ID: 001 และ Pass: 123)');
            }
        }

        function handleLogout() {
            document.getElementById('userId').value = '';
            document.getElementById('userPass').value = '';
            document.getElementById('loginForm').classList.remove('hidden');
            document.getElementById('loggedInView').classList.add('hidden');
            document.getElementById('loggedInView').classList.remove('flex');
        }

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
