import streamlit as st

# ตั้งค่าหน้าหลักของ Streamlit
st.set_page_config(
    page_title="SNAPCON | Automation", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# โค้ด HTML/CSS/JS สำหรับ UI ที่ตรงตามภาพ ฟังก์ชัน 11 ข้อ และระบบ 2 ภาษา
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
                        'nav-bg': '#2b3035',
                        'snap-green': '#00B36E',
                        'btn-bg': '#e2e2e2',
                        'card-gray': '#a8a8a8',
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
            background: linear-gradient(to right, #ffffff 35%, rgba(124, 224, 184, 0.9) 65%, rgba(124, 224, 184, 0.6) 100%), 
                        url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center right;
        }
        .page-section { display: none !important; }
        .page-active { display: block !important; }
        .dropdown-menu { display: none; position: absolute; z-index: 50; }
        .dropdown-container:hover .dropdown-menu { display: block; }
    </style>
</head>
<body>

    <!-- 1. Top Navigation Bar -->
    <nav class="bg-nav-bg h-[60px] w-full fixed top-0 z-50 flex items-center justify-between px-6 border-b-4 border-snap-green shadow-sm">
        <div class="flex flex-col cursor-pointer justify-center h-full" onclick="navigate('home')">
            <span class="font-black text-2xl text-snap-green tracking-tight leading-none mt-1">SNAPCON</span>
            <span class="font-bold text-[10px] text-snap-green leading-none">Automation</span>
        </div>
        
        <div class="hidden lg:flex items-center gap-2">
            <button type="button" onclick="navigate('product')" data-i18n="navProduct" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300 rounded">Product</button>
            <button type="button" onclick="checkDashboardAuth()" data-i18n="navDashboard" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300 rounded">Dashboard</button>
            <button type="button" onclick="navigate('contact')" data-i18n="navContact" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300 rounded">Contact</button>
            <button type="button" onclick="navigate('about')" data-i18n="navAbout" class="bg-btn-bg text-black font-bold text-sm px-6 py-1.5 hover:bg-gray-300 rounded">About</button>
        </div>

        <div class="flex items-center gap-3">
            <div id="login-section" class="flex items-center gap-2">
                <span class="text-[#8e9caf] text-xs font-bold px-1">ID :</span>
                <input type="text" id="userId" class="h-[22px] w-16 px-2 text-xs outline-none text-black rounded-sm">
                <span class="text-[#8e9caf] text-xs font-bold px-1">Pass</span>
                <input type="password" id="userPass" class="h-[22px] w-16 px-2 text-xs outline-none text-black rounded-sm">
                <div class="flex flex-col gap-0.5 ml-1">
                    <button type="button" onclick="handleLogin()" data-i18n="navLogin" class="bg-btn-bg text-black font-bold text-[9px] px-3 py-0.5 hover:bg-gray-300 rounded-sm">Login</button>
                    <button type="button" onclick="handleRegister()" data-i18n="navRegister" class="bg-btn-bg text-black font-bold text-[9px] px-3 py-0.5 hover:bg-gray-300 rounded-sm">Register</button>
                </div>
            </div>
            
            <div id="user-section" class="hidden items-center gap-3 mr-4">
                <span class="text-snap-green font-bold text-sm">Hi, <span id="displayUser" class="text-white">User</span></span>
                <button type="button" onclick="handleLogout()" data-i18n="navLogout" class="text-gray-400 text-xs underline hover:text-white">Logout</button>
            </div>

            <div class="flex items-center bg-[#1c2126] rounded-full p-0.5 ml-1 border border-gray-600">
                <button type="button" id="btn-lang-th" onclick="setLanguage('th')" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-snap-green text-white transition-colors">TH</button>
                <button type="button" id="btn-lang-en" onclick="setLanguage('en')" class="text-[9px] font-bold px-2 py-0.5 rounded-full text-gray-400 hover:text-white transition-colors">EN</button>
            </div>

            <div class="flex items-center gap-4 ml-2 text-white text-lg">
                <div class="relative cursor-pointer hover:text-snap-green" onclick="navigate('cart')">
                    <i class="fas fa-shopping-cart"></i>
                    <span id="cart-badge" class="absolute -top-2 -right-2 bg-red-500 text-white text-[9px] font-bold px-1.5 rounded-full hidden">0</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="h-[60px]"></div>

    <!-- PAGE: HOME -->
    <div id="page-home" class="page-section page-active">
        <section class="w-full h-[400px] hero-bg relative flex items-center border-b border-gray-100">
            <div class="bg-white pl-8 pr-16 py-12 ml-0 shadow-lg absolute left-0 z-10 h-full flex flex-col justify-center">
                <p data-i18n="heroText1" class="text-[26px] text-black mb-1 font-normal tracking-wide">Snap to Connect.</p>
                <p data-i18n="heroText2" class="text-[26px] text-black mb-4 pl-8 font-normal tracking-wide">Ready to Control.</p>
                <h1 data-i18n="heroText3" class="text-6xl font-black text-black tracking-tighter pl-12">Plug & Play</h1>
                <div class="h-1 w-16 bg-red-600 mt-4 ml-12"></div>
            </div>
        </section>
        <!-- Cards Section -->
        <section class="w-full max-w-5xl mx-auto px-6 py-16">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition shadow-sm">
                        <h3 data-i18n="cardDataSheet" class="text-xl font-bold text-black text-center tracking-wide">Download data sheet</h3>
                    </div>
                    <div class="dropdown-menu top-[120px] w-full bg-white border shadow-xl">
                        <a href="https://drive.google.com/file/d/1HY0dUjYJZgxRVYYgN5DOV6Ymm9ARCGUW/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                        <a href="https://drive.google.com/file/d/1TC_cXAy7gbgBx0QI0TiL7Kdt1ICljnHj/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 02</a>
                    </div>
                </div>
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition shadow-sm">
                        <h3 data-i18n="cardDrawing" class="text-xl font-bold text-black text-center tracking-wide">Download drawing</h3>
                    </div>
                    <div class="dropdown-menu top-[120px] w-full bg-white border shadow-xl">
                        <a href="https://drive.google.com/file/d/1CisPrHXeoJgspikAzAOwH0rdhNtQiviy/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white border-b text-sm font-bold">Model 01</a>
                    </div>
                </div>
                <div class="dropdown-container relative flex flex-col items-center cursor-pointer">
                    <div class="bg-card-gray w-full py-14 px-4 flex items-center justify-center hover:bg-gray-400 transition shadow-sm">
                        <h3 data-i18n="cardCatalog" class="text-xl font-bold text-black text-center tracking-wide">Product Catalog</h3>
                    </div>
                    <div class="dropdown-menu top-[120px] w-full bg-white border shadow-xl">
                        <a href="https://drive.google.com/file/d/1_-OdU-N7CnKfG6qY6WV7hW59vL1LX7KD/view?usp=drive_link" target="_blank" class="block px-6 py-3 hover:bg-snap-green hover:text-white text-sm font-bold">Full Catalog</a>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- PAGE: PRODUCT -->
    <div id="page-product" class="page-section max-w-7xl mx-auto px-6 py-12">
        <h2 data-i18n="pageProductTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">SNAPCON Products</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6" id="product-grid"></div>
    </div>

    <!-- PAGE: CART -->
    <div id="page-cart" class="page-section max-w-5xl mx-auto px-6 py-12">
        <h2 data-i18n="pageCartTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">รถเข็นขอใบเสนอราคา</h2>
        <div class="bg-white p-6 shadow-md rounded-lg">
            <div id="cart-items" class="space-y-4 mb-6"></div>
            
            <!-- ส่วนข้อมูลติดต่อเพิ่มเติม (จะแสดงถ้ายังไม่ได้ Login) -->
            <div id="guest-contact-form" class="bg-gray-50 p-6 rounded-xl border-2 border-dashed border-gray-200 mb-6 hidden">
                <p class="font-bold text-slate-700 mb-3"><i class="fas fa-info-circle text-blue-500 mr-2"></i> กรุณากรอกข้อมูลติดต่อกลับเพื่อรับใบเสนอราคา</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input type="text" id="quote-contact-name" placeholder="ชื่อผู้ติดต่อ / บริษัท" class="px-4 py-3 border rounded-lg outline-none focus:ring-2 ring-snap-green/30">
                    <input type="text" id="quote-contact-email" placeholder="อีเมล หรือ เบอร์โทรศัพท์" class="px-4 py-3 border rounded-lg outline-none focus:ring-2 ring-snap-green/30">
                </div>
            </div>

            <div class="border-t pt-6 flex justify-between items-center">
                <span data-i18n="cartTotalLabel" class="text-xl font-bold">ราคากลางประเมินรวม:</span>
                <span id="cart-total" class="text-2xl font-black text-snap-green">฿0</span>
            </div>
            <button type="button" onclick="requestQuote()" data-i18n="btnRequestQuote" class="mt-8 w-full bg-nav-bg text-white font-bold py-4 rounded-xl hover:bg-snap-green transition shadow-lg">
                ยื่นขอใบเสนอราคาอย่างเป็นทางการ
            </button>
            <p class="text-[10px] text-gray-400 mt-3 text-center">* ข้อมูลจะถูกบันทึกลง Google Drive: snapcon1992</p>
        </div>
    </div>

    <!-- PAGE: CONTACT -->
    <div id="page-contact" class="page-section max-w-4xl mx-auto px-6 py-12">
        <h2 data-i18n="pageContactTitle" class="text-3xl font-black mb-8 border-l-4 border-snap-green pl-4">ติดต่อเรา</h2>
        <div class="bg-white p-8 shadow-md rounded-lg text-center">
            <p class="text-lg font-black text-slate-800 mb-4">snapcon1992@gmail.com</p>
            <button onclick="sendContact()" data-i18n="btnSendMsg" class="bg-snap-green text-white font-bold px-8 py-3 rounded-xl hover:bg-green-600 transition shadow-lg">ส่งข้อความ</button>
        </div>
    </div>

    <script>
        const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzTXYEcWYEsbcwL0ipt5vl1azB-C8psZUuwpjfIirzCdH2mBE2OHNdKSMoNPhklRt2M/exec';
        let currentLang = 'th';
        let isLoggedIn = false;
        let cart = [];
        let memoryUsers = { '001': '123' };

        const dict = {
            th: {
                navProduct: "Product", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                cardDataSheet: "Download data sheet", cardDrawing: "Download drawing", cardCatalog: "Product Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "หยิบใส่รถเข็น",
                pageCartTitle: "รถเข็นขอใบเสนอราคา", cartEmpty: "ยังไม่มีสินค้าในรถเข็น", cartTotalLabel: "ราคากลางรวม:",
                btnRequestQuote: "ยื่นขอใบเสนอราคาอย่างเป็นทางการ", selectAll: "เลือกทั้งหมด", deleteSelected: "ลบที่เลือก",
                pageContactTitle: "ติดต่อเรา", btnSendMsg: "ส่งข้อความ",
                alertLoginSuccess: "Login สำเร็จ!", alertAddCart: "เพิ่มลงรถเข็นแล้ว!",
                alertQuoteReq: "กรุณาเลือกสินค้าอย่างน้อย 1 ชิ้น", alertQuoteGuestReq: "กรุณากรอกข้อมูลติดต่อกลับ (อีเมล/เบอร์โทร) เพื่อให้ทีมงานส่งใบเสนอราคาให้ท่านได้",
                alertQuoteSuccess: "ระบบกำลังส่งคำขอใบเสนอราคาไปยัง snapcon1992...",
                specTitle: "สเปคสั่งทำ (Custom):"
            },
            en: {
                navProduct: "Products", navDashboard: "Dashboard", navContact: "Contact", navAbout: "About",
                navLogin: "Login", navRegister: "Register", navLogout: "Logout",
                cardDataSheet: "Download Data Sheet", cardDrawing: "Download Drawing", cardCatalog: "Product Catalog",
                pageProductTitle: "SNAPCON Products", btnAddToCart: "Add to Cart",
                pageCartTitle: "Quote Request Cart", cartEmpty: "Cart is empty", cartTotalLabel: "Estimated Total:",
                btnRequestQuote: "Submit Official Quote Request", selectAll: "Select All", deleteSelected: "Delete Selected",
                pageContactTitle: "Contact Us", btnSendMsg: "Send Message",
                alertLoginSuccess: "Login Successful!", alertAddCart: "Added to cart!",
                alertQuoteReq: "Please select at least 1 item", alertQuoteGuestReq: "Please provide contact info (Email/Phone) so we can send the quote back to you.",
                alertQuoteSuccess: "Sending quote request to snapcon1992...",
                specTitle: "Custom Specs:"
            }
        };

        const products = [
            { id: 'M01', name: 'Snapcon Model 01 (Mini)', price: 15000, img: 'https://i.ibb.co/bZ7TKQg/01.png', specs: { th: { s1: "L: 0.5-5m" }, en: { s1: "L: 0.5-5m" } } },
            { id: 'M02', name: 'Snapcon Model 02 (Std)', price: 22000, img: 'https://i.ibb.co/tTCb2j0h/02.png', specs: { th: { s1: "L: 1-15m" }, en: { s1: "L: 1-15m" } } }
        ];

        function navigate(pageId) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('page-active'));
            document.getElementById('page-' + pageId).classList.add('page-active');
            if(pageId === 'cart') renderCart();
        }

        function handleLogin() {
            const id = document.getElementById('userId').value;
            const pass = document.getElementById('userPass').value;
            if (memoryUsers[id] === pass) {
                isLoggedIn = true;
                document.getElementById('displayUser').innerText = id;
                document.getElementById('login-section').classList.add('hidden');
                document.getElementById('user-section').classList.remove('hidden');
                document.getElementById('user-section').classList.add('flex');
                alert(dict[currentLang].alertLoginSuccess);
                renderCart(); // อัปเดตฟอร์มในหน้าตะกร้า
            } else { alert("ID/Pass Wrong"); }
        }

        function handleLogout() {
            isLoggedIn = false;
            document.getElementById('login-section').classList.remove('hidden');
            document.getElementById('user-section').classList.add('hidden');
            navigate('home');
        }

        function renderProducts() {
            const grid = document.getElementById('product-grid');
            grid.innerHTML = products.map(p => `
                <div class="bg-white border p-5 shadow-sm rounded-xl flex flex-col h-full">
                    <img src="${p.img}" class="w-full h-40 object-cover mb-4 rounded-lg">
                    <h4 class="font-bold text-lg text-nav-bg">${p.name}</h4>
                    <p class="text-snap-green font-black text-2xl my-3">฿${p.price.toLocaleString()}</p>
                    <button type="button" onclick="addToCart('${p.id}')" class="w-full bg-nav-bg text-white py-2.5 rounded-lg font-bold hover:bg-snap-green transition">
                        ${dict[currentLang].btnAddToCart}
                    </button>
                </div>
            `).join('');
        }

        function addToCart(id) {
            const p = products.find(i => i.id === id);
            cart.push({ ...p, cartId: Date.now(), selected: true });
            document.getElementById('cart-badge').innerText = cart.length;
            document.getElementById('cart-badge').classList.remove('hidden');
            alert(dict[currentLang].alertAddCart);
        }

        function renderCart() {
            const container = document.getElementById('cart-items');
            const guestForm = document.getElementById('guest-contact-form');
            
            // แสดงฟอร์มติดต่อกลับ เฉพาะกรณีที่ยังไม่ได้ Login
            if (isLoggedIn) {
                guestForm.classList.add('hidden');
            } else {
                guestForm.classList.remove('hidden');
            }

            if(cart.length === 0) {
                container.innerHTML = `<p class="text-gray-500 py-8 text-center">${dict[currentLang].cartEmpty}</p>`;
                document.getElementById('cart-total').innerText = '฿0';
                return;
            }

            container.innerHTML = cart.map(item => `
                <div class="flex justify-between items-center border-b pb-4">
                    <div class="flex items-center gap-4">
                        <input type="checkbox" ${item.selected ? 'checked' : ''} class="w-5 h-5 accent-snap-green">
                        <img src="${item.img}" class="w-12 h-12 object-cover rounded">
                        <span class="font-bold">${item.name}</span>
                    </div>
                    <span class="font-bold">฿${item.price.toLocaleString()}</span>
                </div>
            `).join('');

            const total = cart.filter(i => i.selected).reduce((s, i) => s + i.price, 0);
            document.getElementById('cart-total').innerText = '฿' + total.toLocaleString();
        }

        function requestQuote() {
            const selectedItems = cart.filter(i => i.selected);
            if(selectedItems.length === 0) { alert(dict[currentLang].alertQuoteReq); return; }

            let contactName = isLoggedIn ? document.getElementById('displayUser').innerText : document.getElementById('quote-contact-name').value;
            let contactInfo = isLoggedIn ? "Registered Account" : document.getElementById('quote-contact-email').value;

            // ถ้ายังไม่ได้ Login ต้องบังคับกรอกข้อมูลติดต่อ
            if (!isLoggedIn && (!contactName || !contactInfo)) {
                alert(dict[currentLang].alertQuoteGuestReq);
                document.getElementById('quote-contact-name').focus();
                return;
            }

            alert(dict[currentLang].alertQuoteSuccess);
            
            let itemList = selectedItems.map(i => `- ${i.name} (฿${i.price.toLocaleString()})`).join('\\n');
            let total = selectedItems.reduce((s, i) => s + i.price, 0);
            
            // บันทึกไป Google Sheet อัตโนมัติ
            fetch(GOOGLE_SCRIPT_URL, {
                method: 'POST',
                mode: 'no-cors',
                body: JSON.stringify({
                    type: "Quotation Request",
                    name_or_id: contactName,
                    email: contactInfo,
                    details: `Items:\\n${itemList}\\nTotal: ฿${total.toLocaleString()}`
                })
            });

            // เปิดหน้าต่าง Email ให้ลูกค้ากดส่งเพื่อเป็นหลักฐาน
            const subject = encodeURIComponent(`Requesting Quote for Snapcon Products`);
            const body = encodeURIComponent(`Name: ${contactName}\nContact: ${contactInfo}\n\nItems Requested:\n${itemList}\n\nEstimated Total: ฿${total.toLocaleString()}`);
            window.location.href = `mailto:snapcon1992@gmail.com?subject=${subject}&body=${body}`;

            cart = cart.filter(i => !i.selected);
            document.getElementById('cart-badge').innerText = cart.length;
            renderCart();
            navigate('home');
        }

        function setLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[lang][key]) el.innerHTML = dict[lang][key];
            });
            renderProducts();
        }

        setLanguage('th');
    </script>
</body>
</html>
"""

# แสดงผลผ่าน Streamlit
st.components.v1.html(snapcon_html, height=1400, scrolling=True)
