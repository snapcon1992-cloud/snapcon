import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS สำหรับ UI ที่ตรงตามภาพและฟังก์ชัน 11 ข้อ
snapcon_html = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPCON | Automation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=Prompt:wght@400;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'nav-bg': '#333333',
                        'snap-green': '#00B36E',
                        'btn-bg': '#E0E0E0',
                        'card-gray': '#A9A9A9',
                    },
                    fontFamily: {
                        sans: ['Inter', 'Prompt', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { margin: 0; padding: 0; background-color: #F8F9FA; overflow-x: hidden; }
        .hero-bg {
            /* ใช้ภาพเครื่องจักรอุตสาหกรรมแทน */
            background-image: url('https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
        }
        /* ซ่อนหน้าอื่นๆ เริ่มต้น */
        .page-section { display: none; }
        .page-active { display: block; }
        
        /* Dropdown transition */
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar (ตามภาพเป๊ะ) -->
    <nav class="bg-nav-bg h-[70px] w-full fixed top-0 z-50 flex items-center justify-between px-6 shadow-md border-b-4 border-snap-green">
        
        <!-- Left: Logo -->
        <div class="flex flex-col cursor-pointer" onclick="navigate('home')">
            <span class="font-black text-2xl text-snap-green tracking-tight leading-none">SNAPCON</span>
            <span class="font-bold text-sm text-snap-green leading-none">Automation</span>
        </div>
        
        <!-- Center: Nav Buttons -->
        <div class="hidden lg:flex items-center gap-4">
            <button onclick="navigate('product')" class="bg-btn-bg text-black font-bold px-6 py-2 hover:bg-gray-300">Product</button>
            <button onclick="checkDashboardAuth()" class="bg-btn-bg text-black font-bold px-6 py-2 hover:bg-gray-300">Dashboard</button>
            <button onclick="navigate('contact')" class="bg-btn-bg text-black font-bold px-6 py-2 hover:bg-gray-300">Contact</button>
            <button onclick="navigate('about')" class="bg-btn-bg text-black font-bold px-6 py-2 hover:bg-gray-300">About</button>
        </div>

        <!-- Right: Login & Icons -->
        <div class="flex items-center gap-2">
            <div id="login-section" class="flex items-center gap-2">
                <span class="text-white text-xs font-bold bg-gray-700 px-2 py-1">ID :</span>
                <input type="text" id="userId" class="h-[25px] w-20 px-2 text-xs outline-none">
                <span class="text-white text-xs font-bold bg-gray-700 px-2 py-1">Pass</span>
                <input type="password" id="userPass" class="h-[25px] w-20 px-2 text-xs outline-none">
                <div class="flex flex-col gap-1">
                    <button onclick="handleLogin()" class="bg-btn-bg text-black font-bold text-[10px] px-3 py-0.5 hover:bg-gray-300">Login</button>
                    <button onclick="handleRegister()" class="bg-btn-bg text-black font-bold text-[10px] px-3 py-0.5 hover:bg-gray-300">Register</button>
                </div>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3 mr-4">
                <span class="text-snap-green font-bold text-sm">Hi, <span id="displayUser" class="text-white">User</span></span>
                <button onclick="handleLogout()" class="text-gray-400 text-xs underline hover:text-white">Logout</button>
            </div>

            <div class="flex items-center gap-4 ml-4 text-white text-xl">
                <div class="relative cursor-pointer hover:text-snap-green" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 bg-red-500 text-white text-[10px] font-bold px-1.5 rounded-full hidden">0</span>
                </div>
                <i class="fas fa-search cursor-pointer hover:text-snap-green"></i>
            </div>
        </div>
    </nav>

    <!-- SPACER สำหรับ Navbar -->
    <div class="h-[70px]"></div>

    <!-- ==================== PAGE: HOME ==================== -->
    <div id="page-home" class="page-section page-active">
        <!-- Hero Section -->
        <section class="w-full h-[450px] hero-bg relative flex items-center">
            <!-- White Overlay Text Box -->
            <div class="bg-white pl-8 pr-16 py-12 ml-0 shadow-lg absolute left-0 z-10">
                <p class="text-3xl text-black mb-2">Snap to Connect.</p>
                <p class="text-3xl text-black mb-6 pl-12">Ready to Control.</p>
                <h1 class="text-6xl font-black text-black tracking-tighter pl-20">Plug & Play</h1>
                <!-- ขีดแดงตกแต่ง -->
                <div class="h-1 w-32 bg-red-600 mt-6 ml-20"></div>
            </div>
            <!-- ภาพบังเงาเพื่อให้กลืนกัน -->
            <div class="absolute inset-0 bg-white/20"></div>
        </section>

        <!-- Bottom Cards Section (3 กล่องสีเทา + Dropdowns) -->
        <section class="w-full max-w-6xl mx-auto px-6 py-16">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                
                <!-- Card 1: Data sheet -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-16 px-4 flex items-center justify-center shadow-md hover:bg-gray-400 transition-colors">
                        <h3 class="text-2xl font-bold text-black text-center">Download data sheet</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-2xl mt-4"></i>
                    <!-- Dropdown Menu -->
                    <div class="dropdown-menu top-[140px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1HY0dUjYJZgxRVYYgN5DOV6Ymm9ARCGUW/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                        <a href="https://drive.google.com/file/d/1TC_cXAy7gbgBx0QI0TiL7Kdt1ICljnHj/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 02</a>
                        <a href="https://drive.google.com/file/d/1Yv_gJWWxTL4H_5YmCDAOCnI33gdfcj4j/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 03</a>
                        <a href="https://drive.google.com/file/d/1KtCARlKphuuIqUOU6xg5mnPf99sjCjHD/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 04</a>
                        <a href="https://drive.google.com/file/d/1dlOS1HSYy1qjWASPGQiKRvQsSyZ-lFs4/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Model 05</a>
                    </div>
                </div>

                <!-- Card 2: Drawing -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-16 px-4 flex items-center justify-center shadow-md hover:bg-gray-400 transition-colors">
                        <h3 class="text-2xl font-bold text-black text-center">Download drawing</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-2xl mt-4"></i>
                    <!-- Dropdown Menu -->
                    <div class="dropdown-menu top-[140px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1CisPrHXeoJgspikAzAOwH0rdhNtQiviy/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                        <a href="https://drive.google.com/file/d/1Gt8onVT7dsyJQkmxdY6s1GZTX4_oUNuB/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 02</a>
                        <a href="https://drive.google.com/file/d/1zesePgsPwZDTUpKzLrmesdnuY6usfe2P/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 03</a>
                        <a href="https://drive.google.com/file/d/1I-63QRJrJksO6xQb1cCWaq9HoDZJ6qBl/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 04</a>
                        <a href="https://drive.google.com/file/d/16z8m9S06kGhyO0C6Tb0mMQ0L4bk5wTDz/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Model 05</a>
                    </div>
                </div>

                <!-- Card 3: Catalog -->
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-16 px-4 flex items-center justify-center shadow-md hover:bg-gray-400 transition-colors">
                        <h3 class="text-2xl font-bold text-black text-center">Product Catalog</h3>
                    </div>
                    <i class="fas fa-chevron-down text-gray-400 text-2xl mt-4"></i>
                    <!-- Dropdown Menu -->
                    <div class="dropdown-menu top-[140px] w-full bg-white border border-gray-200 shadow-xl">
                        <a href="https://drive.google.com/file/d/1_-OdU-N7CnKfG6qY6WV7hW59vL1LX7KD/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Download Full Catalog</a>
                    </div>
                </div>

            </div>
        </section>
    </div>

    <!-- ==================== PAGE: PRODUCT ==================== -->
    <div id="page-product" class="page-section max-w-7xl mx-auto px-6 py-12">
        <h2 class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">SNAPCON Products</h2>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6" id="product-grid">
            <!-- จะถูกสร้างโดย JavaScript -->
        </div>
    </div>

    <!-- ==================== PAGE: CART ==================== -->
    <div id="page-cart" class="page-section max-w-5xl mx-auto px-6 py-12">
        <h2 class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">รถเข็นขอใบเสนอราคา</h2>
        <div class="bg-white p-6 shadow-md rounded-lg">
            <div id="cart-items" class="space-y-4">
                <!-- รายการสินค้าจะมาแสดงตรงนี้ -->
                <p class="text-gray-500">ยังไม่มีสินค้าในรถเข็น</p>
            </div>
            <div class="border-t mt-6 pt-6 flex justify-between items-center">
                <span class="text-xl font-bold">ราคากลางประเมินรวม:</span>
                <span id="cart-total" class="text-2xl font-black text-snap-green">฿0</span>
            </div>
            <button onclick="requestQuote()" class="mt-8 w-full bg-nav-bg text-white font-bold py-4 rounded hover:bg-snap-green transition-colors">
                ยื่นขอใบเสนอราคาอย่างเป็นทางการ
            </button>
        </div>
    </div>

    <!-- ==================== PAGE: DASHBOARD ==================== -->
    <div id="page-dashboard" class="page-section max-w-7xl mx-auto px-6 py-12">
        <h2 class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">Dashboard หลักของ Snapcon</h2>
        <div class="grid grid-cols-3 gap-6 mb-8">
            <div class="bg-white p-6 shadow rounded border-t-4 border-snap-green"><p class="text-gray-500">Total Output</p><h3 class="text-4xl font-black">4,520</h3></div>
            <div class="bg-white p-6 shadow rounded border-t-4 border-blue-500"><p class="text-gray-500">Active Nodes</p><h3 class="text-4xl font-black">10/10</h3></div>
            <div class="bg-white p-6 shadow rounded border-t-4 border-orange-500"><p class="text-gray-500">System Health</p><h3 class="text-4xl font-black">98.5%</h3></div>
        </div>
        <div class="bg-white p-12 shadow rounded text-center">
            <i class="fas fa-chart-line text-6xl text-gray-300 mb-4"></i>
            <p class="text-gray-500 text-lg">ระบบ Dashboard เต็มรูปแบบกำลังแสดงผลข้อมูล Real-time...</p>
        </div>
    </div>

    <!-- ==================== PAGE: CONTACT ==================== -->
    <div id="page-contact" class="page-section max-w-4xl mx-auto px-6 py-12">
        <h2 class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">ติดต่อเรา (Contact Us)</h2>
        <div class="bg-white p-8 shadow-md rounded-lg">
            <input type="text" placeholder="ชื่อ-นามสกุล" class="w-full mb-4 px-4 py-3 border rounded">
            <input type="email" placeholder="อีเมล" class="w-full mb-4 px-4 py-3 border rounded">
            <textarea placeholder="คำถามหรือข้อสงสัย..." class="w-full mb-4 px-4 py-3 border rounded h-32"></textarea>
            <button onclick="alert('ส่งข้อความสำเร็จ ทีมงานจะติดต่อกลับครับ')" class="bg-snap-green text-white font-bold px-8 py-3 rounded">ส่งข้อความ</button>
        </div>
    </div>

    <!-- ==================== PAGE: ABOUT ==================== -->
    <div id="page-about" class="page-section max-w-4xl mx-auto px-6 py-12">
        <h2 class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">เกี่ยวกับ Snapcon (About Us)</h2>
        <div class="bg-white p-8 shadow-md rounded-lg">
            <p class="text-gray-600 leading-relaxed text-lg">
                Snapcon Automation คือผู้นำด้านเทคโนโลยีอุตสาหกรรม 4.0 ที่มุ่งเน้นการพัฒนาระบบ <b>Plug & Play</b> 
                เพื่อลดความซับซ้อนในการติดตั้งและควบคุมเครื่องจักร 
                <br><br>
                <i>(ข้อมูลประวัติบริษัทเพิ่มเติมจะถูกเพิ่มเข้ามาในส่วนนี้ภายหลัง)</i>
            </p>
        </div>
    </div>

    <!-- ==================== JAVASCRIPT ==================== -->
    <script>
        // 1. ตัวแปรสถานะ
        let isLoggedIn = false;
        let cart = [];
        const products = [
            { id: 'M01', name: 'Snapcon Model 01', price: 15000, img: 'https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?w=300' },
            { id: 'M02', name: 'Snapcon Model 02', price: 22000, img: 'https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?w=300' },
            { id: 'M03', name: 'Snapcon Model 03', price: 28500, img: 'https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?w=300' },
            { id: 'M04', name: 'Snapcon Model 04', price: 35000, img: 'https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?w=300' },
            { id: 'M05', name: 'Snapcon Pro 05', price: 45000, img: 'https://images.unsplash.com/photo-1580983537233-de1f8d4e9d7c?w=300' },
        ];

        // 2. ฟังก์ชันสลับหน้าเพจ
        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            document.getElementById('page-' + pageId).classList.add('page-active');
            window.scrollTo(0,0);
        }

        // 3. ฟังก์ชันเช็ค Dashboard
        function checkDashboardAuth() {
            if (isLoggedIn) {
                navigate('dashboard');
            } else {
                alert("⚠️ กรุณา Login หรือ Register ก่อนเข้าสู่หน้า Dashboard");
                document.getElementById('userId').focus();
            }
        }

        // 4. ระบบ Login & Register
        function handleLogin() {
            const id = document.getElementById('userId').value;
            if(id !== "") {
                isLoggedIn = true;
                document.getElementById('displayUser').innerText = id;
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                alert("Login สำเร็จ! บันทึกข้อมูล Session (Simulation)");
            } else {
                alert("กรุณากรอก ID");
            }
        }
        function handleRegister() {
            alert("พาไปหน้า Register และบันทึกข้อมูลเก็บไว้ใน Google Drive / Database");
            handleLogin(); // จำลองว่าสมัครแล้วล็อกอินเลย
        }
        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden');
            document.getElementById('user-section').classList.add('hidden');
            document.getElementById('user-section').classList.remove('flex');
            navigate('home');
        }

        // 5. ระบบ Product & Cart
        function renderProducts() {
            const grid = document.getElementById('product-grid');
            grid.innerHTML = products.map(p => `
                <div class="bg-white border p-4 shadow-sm hover:shadow-md transition">
                    <img src="${p.img}" class="w-full h-40 object-cover mb-4 rounded">
                    <h4 class="font-bold text-lg">${p.name}</h4>
                    <p class="text-snap-green font-black text-xl my-2">฿${p.price.toLocaleString()}</p>
                    <button onclick="addToCart('${p.id}')" class="w-full bg-nav-bg text-white py-2 font-bold hover:bg-snap-green transition">หยิบใส่รถเข็น</button>
                </div>
            `).join('');
        }

        function addToCart(id) {
            const product = products.find(p => p.id === id);
            cart.push(product);
            
            // อัปเดตตัวเลขแจ้งเตือนที่ไอคอนตะกร้า
            const badge = document.getElementById('cart-badge');
            badge.innerText = cart.length;
            badge.classList.remove('hidden');
            
            alert(`เพิ่ม ${product.name} ลงในรถเข็นแล้ว!`);
            renderCart();
        }

        function renderCart() {
            const container = document.getElementById('cart-items');
            if(cart.length === 0) {
                container.innerHTML = '<p class="text-gray-500">ยังไม่มีสินค้าในรถเข็น</p>';
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }

            container.innerHTML = cart.map((item, index) => `
                <div class="flex justify-between items-center border-b pb-2">
                    <div class="flex items-center gap-4">
                        <span class="font-bold">${index + 1}.</span>
                        <span>${item.name}</span>
                    </div>
                    <span class="font-bold text-gray-700">฿${item.price.toLocaleString()}</span>
                </div>
            `).join('');

            const total = cart.reduce((sum, item) => sum + item.price, 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
        }

        function requestQuote() {
            if(cart.length === 0) {
                alert('ตะกร้าว่างเปล่า กรุณาเลือกสินค้าก่อนยื่นขอใบเสนอราคา');
                return;
            }
            alert('ส่งคำขอใบเสนอราคาสำเร็จ! เจ้าหน้าที่จะติดต่อกลับพร้อมใบเสนอราคาอย่างเป็นทางการครับ');
            cart = [];
            document.getElementById('cart-badge').classList.add('hidden');
            renderCart();
            navigate('home');
        }

        // เริ่มต้นเรนเดอร์สินค้า
        renderProducts();
    </script>
</body>
</html>
"""

# แสดงผลหน้าเว็บผ่าน Streamlit
st.components.v1.html(snapcon_html, height=1200, scrolling=True)
