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

    <!-- Navigation -->
    <nav class="fixed w-full z-50 bg-white/80 backdrop-blur-md border-b border-slate-100">
        <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <div class="w-10 h-10 bg-emerald-500 rounded-xl flex items-center justify-center text-white font-black text-xl">S</div>
                <span class="text-2xl font-black tracking-tighter">SNAPCON</span>
            </div>
            
            <div class="hidden md:flex items-center gap-10">
                <a href="#solutions" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">โซลูชัน</a>
                <a href="#products" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">สินค้า</a>
                <a href="#about" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">เกี่ยวกับเรา</a>
                <a href="#contact" class="bg-slate-900 text-white px-6 py-2.5 rounded-full text-sm font-bold hover:bg-emerald-600 transition-all shadow-lg shadow-slate-200">
                    ติดต่อเรา
                </a>
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
                <h1 class="text-6xl lg:text-8xl font-black tracking-tighter leading-[0.9] mb-8">
                    Snap to <br><span class="gradient-text">Connect.</span>
                </h1>
                <p class="text-xl text-slate-500 font-medium leading-relaxed max-w-lg mb-10">
                    นวัตกรรมการเชื่อมต่อที่เปลี่ยนความซับซ้อนให้เป็นเรื่องง่าย เพิ่มประสิทธิภาพให้ธุรกิจของคุณด้วยเทคโนโลยี Plug & Play ที่ทันสมัยที่สุด
                </p>
                <div class="flex flex-wrap gap-4">
                    <button class="bg-emerald-500 text-white px-8 py-4 rounded-2xl font-bold text-lg hover:bg-emerald-600 hover:scale-105 transition-all shadow-xl shadow-emerald-100">
                        เริ่มต้นใช้งาน
                    </button>
                    <button class="bg-white border-2 border-slate-100 text-slate-900 px-8 py-4 rounded-2xl font-bold text-lg hover:bg-slate-50 transition-all">
                        เรียนรู้เพิ่มเติม
                    </button>
                </div>
            </div>
            <div class="relative">
                <div class="absolute -inset-4 bg-emerald-100/50 rounded-[40px] blur-3xl -z-10 animate-pulse"></div>
                <div class="rounded-[40px] overflow-hidden shadow-2xl bg-slate-100 aspect-square flex items-center justify-center">
                    <div class="text-center p-8">
                         <div class="text-6xl mb-6">🔌</div>
                         <p class="text-slate-400 font-bold uppercase tracking-widest text-sm">[รูปภาพอุปกรณ์ Snapcon]</p>
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

    <!-- Features -->
    <section id="solutions" class="py-24 max-w-7xl mx-auto px-6">
        <div class="text-center max-w-3xl mx-auto mb-20">
            <h2 class="text-4xl font-black tracking-tight mb-4">ทำไมต้องเลือก SNAPCON?</h2>
            <p class="text-slate-500 font-medium">เราออกแบบทุกอย่างโดยคำนึงถึงความเร็ว ความปลอดภัย และความง่ายในการใช้งาน</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
            <div class="p-10 rounded-[32px] bg-slate-50 card-hover border border-transparent hover:border-emerald-100">
                <div class="text-4xl mb-8">⚡</div>
                <h3 class="text-xl font-bold mb-4">ติดตั้งรวดเร็ว</h3>
                <p class="text-slate-500 leading-relaxed">ระบบ Plug & Play ที่แท้จริง ไม่ต้องตั้งค่าให้ยุ่งยาก</p>
            </div>
            <div class="p-10 rounded-[32px] bg-slate-50 card-hover border border-transparent hover:border-emerald-100">
                <div class="text-4xl mb-8">🛡️</div>
                <h3 class="text-xl font-bold mb-4">ความปลอดภัยสูงสุด</h3>
                <p class="text-slate-500 leading-relaxed">การเข้ารหัสข้อมูลระดับสูงและการป้องกันที่รัดกุม</p>
            </div>
            <div class="p-10 rounded-[32px] bg-slate-50 card-hover border border-transparent hover:border-emerald-100">
                <div class="text-4xl mb-8">📈</div>
                <h3 class="text-xl font-bold mb-4">ขยายขนาดได้ง่าย</h3>
                <p class="text-slate-500 leading-relaxed">พร้อมที่จะเติบโตไปพร้อมกับธุรกิจของคุณทุกระดับ</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 border-t border-slate-100 bg-white">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-slate-900 rounded-lg flex items-center justify-center text-white font-black text-sm">S</div>
                <span class="text-xl font-black tracking-tighter">SNAPCON</span>
            </div>
            <div class="text-slate-400 text-sm">
                © 2026 Snapcon Solutions. All rights reserved.
            </div>
        </div>
    </footer>

</body>
</html>
"""

# แสดงผล HTML ผ่าน Streamlit component
st.components.v1.html(snapcon_html, height=2200, scrolling=True)
