<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Snap to Connect. Ready to Control.</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #050b14;
            margin: 0;
            overflow: hidden; /* ล็อค Scroll จนกว่าจะเริ่มทำงาน */
            color: white;
        }

        /* --- Intro Layer --- */
        #intro-screen {
            position: fixed;
            inset: 0;
            background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: opacity 0.8s ease-out;
        }

        /* Plug & Socket Styles */
        .power-system {
            position: relative;
            height: 120px;
            display: flex;
            align-items: center;
            gap: 40px;
        }

        .socket-container {
            width: 100px;
            height: 100px;
            background: #1e293b;
            border-radius: 20px;
            border: 4px solid #334155;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            position: relative;
            box-shadow: inset 0 4px 10px rgba(0,0,0,0.5);
        }

        .socket-hole {
            width: 12px;
            height: 30px;
            background: #020617;
            border-radius: 4px;
        }

        .plug-container {
            width: 90px;
            height: 70px;
            background: #10B981;
            border-radius: 12px;
            position: relative;
            cursor: pointer;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: float 2s infinite ease-in-out;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10;
        }

        .plug-container::after, .plug-container::before {
            content: '';
            position: absolute;
            left: -18px;
            top: 15px;
            width: 18px;
            height: 8px;
            background: #94a3b8;
            border-radius: 2px 0 0 2px;
        }
        .plug-container::before { top: 45px; }

        @keyframes float {
            0%, 100% { transform: translateX(0); }
            50% { transform: translateX(15px); }
        }

        /* Rocket */
        #rocket {
            position: absolute;
            font-size: 80px;
            bottom: -150px;
            filter: drop-shadow(0 0 30px #10B981);
            transition: bottom 1.2s cubic-bezier(0.15, 0, 0.05, 1);
            z-index: 5;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .thrust {
            width: 20px;
            height: 80px;
            background: linear-gradient(to top, transparent, #10B981, #f59e0b);
            filter: blur(4px);
            margin-top: -10px;
            border-radius: 50%;
            opacity: 0;
            animation: shake 0.1s infinite;
        }

        @keyframes shake {
            from { transform: translateX(-2px); }
            to { transform: translateX(2px); }
        }

        /* --- Main Content --- */
        #main-app {
            opacity: 0;
            transform: translateY(20px);
            transition: all 1s ease;
            background: #f8fafc;
            color: #0f172a;
            min-height: 100vh;
            visibility: hidden;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.05);
        }

        .text-gradient {
            background: linear-gradient(to right, #059669, #10B981);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>
<body>

    <!-- INTRO ANIMATION SECTION -->
    <div id="intro-screen">
        <div id="intro-ui" class="text-center transition-all duration-500">
            <h1 class="text-4xl font-black tracking-tighter mb-4 text-white">SNAPCON</h1>
            <p class="text-emerald-400 font-mono text-xs tracking-widest uppercase mb-16 animate-pulse">
                Click the Plug to Start
            </p>
            
            <div class="power-system">
                <div class="socket-container">
                    <div class="socket-hole"></div>
                    <div class="socket-hole"></div>
                </div>
                <div class="plug-container" id="plug" onclick="launchSequence()">
                    <span class="text-white font-bold text-xs">SNAP</span>
                </div>
            </div>
        </div>

        <div id="rocket">
            🚀
            <div class="thrust" id="rocket-thrust"></div>
        </div>

        <div id="launch-text" class="absolute bottom-20 opacity-0 transition-opacity duration-500">
            <span class="text-emerald-500 font-bold text-2xl tracking-widest">LAUNCHING...</span>
        </div>
    </div>

    <!-- MAIN WEBSITE CONTENT -->
    <div id="main-app">
        <!-- Header -->
        <nav class="flex justify-between items-center px-8 py-6 max-w-7xl mx-auto">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center text-white font-black">S</div>
                <span class="text-2xl font-black tracking-tight">SNAPCON</span>
            </div>
            <div class="hidden md:flex gap-8 font-bold text-slate-500 text-sm uppercase tracking-wider">
                <a href="#" class="hover:text-emerald-600 transition-colors">Catalog</a>
                <a href="#" class="hover:text-emerald-600 transition-colors">Documentation</a>
                <a href="#" class="hover:text-emerald-600 transition-colors">Support</a>
            </div>
            <button class="bg-slate-950 text-white px-6 py-2.5 rounded-full font-bold text-sm hover:bg-emerald-600 transition-all">
                Contact Sales
            </button>
        </nav>

        <!-- Hero -->
        <section class="max-w-7xl mx-auto px-6 py-20 flex flex-col items-center text-center">
            <div class="inline-block px-4 py-1.5 bg-emerald-50 text-emerald-600 rounded-full text-xs font-black tracking-widest uppercase mb-6">
                Plug & Play Technology 2026
            </div>
            <h1 class="text-6xl md:text-8xl font-black tracking-tighter leading-none mb-8 text-slate-900">
                Snap to Connect.<br>
                <span class="text-gradient">Ready to Control.</span>
            </h1>
            <p class="max-w-2xl text-xl text-slate-500 font-medium leading-relaxed mb-12">
                เปลี่ยนความซับซ้อนให้เป็นเรื่องง่ายด้วยระบบควบคุมอัตโนมัติจาก SNAPCON 
                ที่ให้คุณเชื่อมต่อและเริ่มต้นใช้งานได้ทันทีในเวลาไม่กี่วินาที
            </p>
            
            <div class="flex flex-col sm:flex-row gap-4 mb-20">
                <button class="bg-emerald-500 text-white px-10 py-5 rounded-2xl font-black text-lg shadow-xl shadow-emerald-200 hover:scale-105 transition-all">
                    ดาวน์โหลดแคตตาล็อก
                </button>
                <button class="bg-white border-2 border-slate-200 text-slate-900 px-10 py-5 rounded-2xl font-black text-lg hover:bg-slate-50 transition-all">
                    ดูวิธีการติดตั้ง
                </button>
            </div>

            <!-- Dashboard Preview -->
            <div class="w-full glass-card rounded-[40px] p-4 md:p-8 aspect-video md:aspect-[21/9] flex items-center justify-center overflow-hidden relative">
                <div class="absolute inset-0 bg-gradient-to-br from-emerald-50 to-slate-50 -z-10"></div>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 w-full h-full opacity-40">
                    <div class="bg-white rounded-2xl border border-slate-100 p-6 flex flex-col justify-end">
                        <div class="w-12 h-2 bg-slate-100 mb-2"></div>
                        <div class="w-20 h-4 bg-emerald-200"></div>
                    </div>
                    <div class="bg-white rounded-2xl border border-slate-100 p-6 flex flex-col justify-end">
                        <div class="w-12 h-2 bg-slate-100 mb-2"></div>
                        <div class="w-20 h-4 bg-emerald-200"></div>
                    </div>
                    <div class="bg-white rounded-2xl border border-slate-100 p-6 flex flex-col justify-end">
                        <div class="w-12 h-2 bg-slate-100 mb-2"></div>
                        <div class="w-20 h-4 bg-emerald-200"></div>
                    </div>
                    <div class="bg-white rounded-2xl border border-slate-100 p-6 flex flex-col justify-end">
                        <div class="w-12 h-2 bg-slate-100 mb-2"></div>
                        <div class="w-20 h-4 bg-emerald-200"></div>
                    </div>
                </div>
                <div class="absolute flex flex-col items-center">
                   <div class="w-20 h-20 bg-emerald-500 rounded-full flex items-center justify-center text-white text-3xl shadow-xl shadow-emerald-200 animate-bounce">
                       ⚡
                   </div>
                   <span class="mt-4 font-black text-slate-400 uppercase tracking-widest">System Online</span>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="border-t border-slate-100 py-12 text-center text-slate-400 text-xs font-bold tracking-[0.2em] uppercase">
            © 2026 Snapcon Global Solutions Co., Ltd.
        </footer>
    </div>

    <script>
        function launchSequence() {
            const plug = document.getElementById('plug');
            const introUI = document.getElementById('intro-ui');
            const rocket = document.getElementById('rocket');
            const thrust = document.getElementById('rocket-thrust');
            const launchText = document.getElementById('launch-text');
            const introScreen = document.getElementById('intro-screen');
            const mainApp = document.getElementById('main-app');

            // 1. เสียบปลั๊ก (Action)
            plug.style.animation = 'none';
            plug.style.transform = 'translateX(-118px)'; // ขยับเข้าหา Socket
            
            setTimeout(() => {
                // 2. แสงไฟกระพริบตอนเชื่อมต่อ
                document.body.style.backgroundColor = '#10B981';
                launchText.style.opacity = '1';
                
                setTimeout(() => {
                    // 3. จรวดวิ่ง (Launch)
                    introUI.style.opacity = '0';
                    introUI.style.transform = 'scale(0.9)';
                    thrust.style.opacity = '1';
                    rocket.style.bottom = '120%'; // วิ่งขึ้นด้านบน
                    
                    // 4. เปลี่ยนหน้าจอเป็นเนื้อหาหลัก
                    setTimeout(() => {
                        introScreen.style.opacity = '0';
                        mainApp.style.visibility = 'visible';
                        mainApp.style.opacity = '1';
                        mainApp.style.transform = 'translateY(0)';
                        document.body.style.overflow = 'auto'; // อนุญาตให้ Scroll ได้
                        
                        setTimeout(() => {
                            introScreen.style.display = 'none';
                        }, 800);
                    }, 800);
                }, 600);
            }, 400);
        }
    </script>
</body>
</html>
