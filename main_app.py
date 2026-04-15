import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Snap to Connect", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS สำหรับหน้าเว็บ Snapcon (Professional Version)
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Snap to Connect</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            scroll-behavior: smooth;
            margin: 0;
            padding: 0;
        }
        .gradient-text {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-bg {
            background: radial-gradient(circle at top right, rgba(16, 185, 129, 0.05), transparent),
                        radial-gradient(circle at bottom left, rgba(16, 185, 129, 0.02), transparent);
        }
        .card-hover {
            transition: all 0.3s ease;
        }
        .card-hover:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        }
        /* ซ่อน scrollbar ของ iframe */
        ::-webkit-scrollbar {
            display: none;
        }
    </style>
</head>
<body class="bg-white text-slate-900 overflow-x-hidden">

    <!-- Top Bar Login Area -->
    <div class="bg-slate-900 w-full py-2 px-6 flex justify-end items-center fixed top-0 z-[60]">
        <!-- ฟอร์ม Login -->
        <div id="loginForm" class="flex items-center gap-3 transition-opacity duration-300">
            <span class="text-xs text-slate-400 font-bold">ID:</span>
            <input type="text" id="userId" class="px-2 py-1 rounded text-xs w-24 border-none outline-none focus:ring-2 focus:ring-emerald-500" placeholder="001">
            <span class="text-xs text-slate-400 font-bold">Pass:</span>
            <input type="password" id="userPass" class="px-2 py-1 rounded text-xs w-24 border-none outline-none focus:ring-2 focus:ring-emerald-500" placeholder="***">
            <button onclick="handleLogin()" class="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-1 rounded text-xs font-bold transition-colors">Login</button>
            <button onclick="alert('ระบบลงทะเบียนผู้ใช้ใหม่ (Register) กำลังอยู่ในช่วงปรับปรุงครับ')" class="bg-slate-700 hover:bg-slate-600 text-white px-4 py-1 rounded text-xs font-bold transition-colors">Register</button>
        </div>
        
        <!-- ข้อมูลผู้ใช้เมื่อ Login สำเร็จ -->
        <div id="loggedInView" class="hidden flex items-center gap-4 transition-opacity duration-300">
            <div class="flex items-center gap-2">
                <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                <span class="text-emerald-400 font-bold text-xs">Logged in as: <span class="text-white">Watanabe San</span></span>
            </div>
            <button onclick="handleLogout()" class="text-slate-400 hover:text-white text-xs font-bold underline transition-colors">Logout</button>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="fixed w-full z-50 bg-white/80 backdrop-blur-md border-b border-slate-100 mt-9 transition-all">
        <div class="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center">
            <div class="flex items-center gap-2 cursor-pointer" onclick="window.scrollTo(0,0)">
                <div class="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center text-white font-black text-lg shadow-md shadow-emerald-200">S</div>
                <span class="text-xl font-black tracking-tighter">SNAPCON</span>
            </div>
            
            <div class="hidden md:flex items-center gap-10">
                <a href="#solutions" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">โซลูชัน</a>
                <a href="#about" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">เกี่ยวกับเรา</a>
                <button onclick="alert('📞 ติดต่อทีมวิศวกร: 081-XXX-XXXX หรือ support@snapcon.com')" class="bg-slate-900 text-white px-5 py-2 rounded-full text-sm font-bold hover:bg-emerald-600 transition-all shadow-lg shadow-slate-200">
                    ติดต่อเรา
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative pt-40 pb-24 hero-bg overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-2 gap-12 items-center">
            <div class="z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 text-emerald-600 text-xs font-bold uppercase tracking-widest mb-6">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    The Future of Connectivity
                </div>
                <h1 class="text-5xl lg:text-7xl font-black tracking-tighter leading-[1.0] mb-6">
                    Snap to <br><span class="gradient-text">Connect.</span>
                </h1>
                <p class="text-lg text-slate-500 font-medium leading-relaxed max-w-lg mb-8">
                    นวัตกรรมการเชื่อมต่อที่เปลี่ยนความซับซ้อนให้เป็นเรื่องง่าย เพิ่มประสิทธิภาพให้ธุรกิจของคุณด้วยเทคโนโลยี Plug & Play ที่ทันสมัยที่สุด
                </p>
                <div class="flex flex-wrap gap-4">
                    <a href="#solutions" class="bg-emerald-500 text-white px-8 py-4 rounded-2xl font-bold text-base hover:bg-emerald-600 hover:scale-105 transition-all shadow-xl shadow-emerald-100 inline-block text-center">
                        เริ่มต้นใช้งาน
                    </a>
                    <button onclick="alert('ข้อมูลเพิ่มเติม: SNAPCON Automation Solution สำหรับอุตสาหกรรมยุค 4.0')" class="bg-white border-2 border-slate-100 text-slate-900 px-8 py-4 rounded-2xl font-bold text-base hover:bg-slate-50 transition-all">
                        เรียนรู้เพิ่มเติม
                    </button>
                </div>
            </div>
            <div class="relative">
                <div class="absolute -inset-4 bg-emerald-100/50 rounded-[40px] blur-3xl -z-10 animate-pulse"></div>
                <div class="rounded-[40px] overflow-hidden shadow-2xl bg-slate-100 aspect-square flex flex-col items-center justify-center relative">
                    <!-- Floating Tags แบบในรูปภาพ -->
                    <div class="absolute top-10 right-10 bg-white/90 px-4 py-2 rounded-lg font-bold text-xs text-slate-700 shadow-lg backdrop-blur-sm shadow-slate-200">"Plug. Monitor. Control."</div>
                    <div class="absolute bottom-20 left-10 bg-white/90 px-4 py-2 rounded-lg font-bold text-xs text-emerald-600 shadow-lg backdrop-blur-sm shadow-slate-200">"Upgrade Your Factory"</div>
                    <div class="absolute bottom-10 right-5 bg-white/90 px-4 py-2 rounded-lg font-bold text-xs text-blue-600 shadow-lg backdrop-blur-sm shadow-slate-200">"Data-Driven Automation"</div>
                    
                    <div class="text-center p-8 z-10">
                         <div class="text-7xl mb-6 drop-shadow-xl">🔌</div>
                         <p class="text-slate-400 font-bold uppercase tracking-widest text-xs">[ภาพอุปกรณ์ Snapcon]</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats -->
    <section class="py-12 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8">
            <div class="text-center">
                <div class="text-4xl font-black mb-1">99%</div>
                <div class="text-slate-400 text-xs font-bold uppercase tracking-widest">Efficiency</div>
            </div>
            <div class="text-center">
                <div class="text-4xl font-black mb-1">200+</div>
                <div class="text-slate-400 text-xs font-bold uppercase tracking-widest">Partners</div>
            </div>
            <div class="text-center">
                <div class="text-4xl font-black mb-1">15ms</div>
                <div class="text-slate-400 text-xs font-bold uppercase tracking-widest">Response</div>
            </div>
            <div class="text-center">
                <div class="text-4xl font-black mb-1">24/7</div>
                <div class="text-slate-400 text-xs font-bold uppercase tracking-widest">Support</div>
            </div>
        </div>
    </section>

    <!-- Features / Solutions -->
    <section id="solutions" class="py-24 max-w-7xl mx-auto px-6 scroll-mt-20">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl font-black tracking-tight mb-4">Our Solutions</h2>
            <p class="text-slate-500 font-medium">เข้าถึงข้อมูลและเครื่องมือที่คุณต้องการได้อย่างรวดเร็ว เพื่อการจัดการที่มีประสิทธิภาพสูงสุด</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
            <!-- Card 1: Data Sheet -->
            <div class="p-8 rounded-[24px] bg-slate-50 card-hover border border-slate-100 flex flex-col justify-between h-full">
                <div>
                    <div class="w-12 h-12 bg-blue-100 text-blue-600 rounded-xl flex items-center justify-center text-xl mb-6">📄</div>
                    <h3 class="text-lg font-bold mb-3">Download Data Sheet</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-6">เอกสารคู่มือ ข้อมูลทางเทคนิค และคุณสมบัติของผลิตภัณฑ์อย่างละเอียดเพื่อการวิเคราะห์</p>
                </div>
                <button onclick="openGoogleDrive('datasheet')" class="w-full bg-white border border-slate-200 text-slate-800 font-bold py-3 rounded-xl hover:bg-blue-50 hover:text-blue-600 transition-colors text-sm">
                    ดาวน์โหลด Data Sheet
                </button>
            </div>

            <!-- Card 2: Drawing -->
            <div class="p-8 rounded-[24px] bg-slate-50 card-hover border border-slate-100 flex flex-col justify-between h-full">
                <div>
                    <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-xl flex items-center justify-center text-xl mb-6">📐</div>
                    <h3 class="text-lg font-bold mb-3">Download Drawing</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-6">ไฟล์ 2D/3D CAD และแบบร่างทางวิศวกรรมสำหรับนำไปใช้วางแผนการติดตั้งเครื่องจักร</p>
                </div>
                <button onclick="openGoogleDrive('drawing')" class="w-full bg-emerald-500 text-white font-bold py-3 rounded-xl hover:bg-emerald-600 transition-colors text-sm shadow-lg shadow-emerald-100">
                    ดาวน์โหลด Drawing
                </button>
            </div>

            <!-- Card 3: Catalog -->
            <div class="p-8 rounded-[24px] bg-slate-50 card-hover border border-slate-100 flex flex-col justify-between h-full">
                <div>
                    <div class="w-12 h-12 bg-purple-100 text-purple-600 rounded-xl flex items-center justify-center text-xl mb-6">📦</div>
                    <h3 class="text-lg font-bold mb-3">Product Catalog</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-6">รายละเอียดสินค้า แค็ตตาล็อกรุ่นต่างๆ และอุปกรณ์เสริมทั้งหมดของ Snapcon ปี 2026</p>
                </div>
                <button onclick="openGoogleDrive('catalog')" class="w-full bg-slate-900 text-white font-bold py-3 rounded-xl hover:bg-slate-800 transition-colors text-sm shadow-lg shadow-slate-200">
                    ดู Product Catalog
                </button>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="about" class="py-12 border-t border-slate-100 bg-white">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-slate-900 rounded-lg flex items-center justify-center text-white font-black text-sm">S</div>
                <span class="text-xl font-black tracking-tighter">SNAPCON</span>
            </div>
            <div class="flex gap-8 text-slate-400 text-xs font-bold uppercase tracking-widest">
                <a href="#" class="hover:text-emerald-500 transition-colors">Privacy</a>
                <a href="#" class="hover:text-emerald-500 transition-colors">Terms</a>
                <a href="#" class="hover:text-emerald-500 transition-colors">Contact</a>
            </div>
            <div class="text-slate-400 text-xs font-medium">
                © 2026 Snapcon Solutions. All rights reserved.
            </div>
        </div>
    </footer>

    <!-- JavaScript Functions -->
    <script>
        // ฟังก์ชันระบบ Login แบบจำลอง (Simulated Auth)
        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            
            if (id === '001' && pass === '123') {
                // หากรหัสผ่านถูกต้อง ให้สลับหน้าจอ UI ไปโหมด Logged In
                document.getElementById('loginForm').classList.add('hidden');
                document.getElementById('loggedInView').classList.remove('hidden');
            } else {
                alert('⚠️ ID หรือ Password ไม่ถูกต้อง!\\n(คำแนะนำ: ลองใช้ ID: 001 และ Pass: 123)');
            }
        }

        // ฟังก์ชัน Logout
        function handleLogout() {
            // เคลียร์ข้อมูลและสลับ UI กลับมาเป็นโหมดปกติ
            document.getElementById('userId').value = '';
            document.getElementById('userPass').value = '';
            document.getElementById('loginForm').classList.remove('hidden');
            document.getElementById('loggedInView').classList.add('hidden');
        }

        // ฟังก์ชันเปิดลิงก์ Google Drive
        function openGoogleDrive(fileType) {
            // คุณสามารถแก้ลิงก์ตรงนี้เป็น URL ของ Google Drive ของคุณได้เลย
            let driveLink = '';
            
            switch(fileType) {
                case 'datasheet':
                    driveLink = 'https://drive.google.com/drive/my-drive'; // ใส่ลิงก์ Data Sheet
                    break;
                case 'drawing':
                    driveLink = 'https://drive.google.com/drive/my-drive'; // ใส่ลิงก์ Drawing
                    break;
                case 'catalog':
                    driveLink = 'https://drive.google.com/drive/my-drive'; // ใส่ลิงก์ Catalog
                    break;
            }
            
            // ตรวจสอบสิทธิ์ว่า Login หรือยัง (ถ้าระบบบังคับ Login ค่อยปลดคอมเมนต์ด้านล่าง)
            /*
            if(document.getElementById('loggedInView').classList.contains('hidden')) {
                alert("กรุณา Login ก่อนดาวน์โหลดไฟล์");
                return;
            }
            */

            // เปิดแท็บใหม่ไปที่ Google Drive
            alert('กำลังนำคุณไปยัง Google Drive เพื่อดาวน์โหลดไฟล์...');
            window.open(driveLink, '_blank');
        }
    </script>
</body>
</html>
"""

# แสดงผล HTML ผ่าน Streamlit component
st.components.v1.html(snapcon_html, height=1400, scrolling=True)
