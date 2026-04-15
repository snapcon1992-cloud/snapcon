 Snapcon Enterprise V1.5

Smart Production Monitoring & AI Predictive Maintenance

ระบบบริหารจัดการและติดตามผลการผลิตอัจฉริยะ รองรับการเชื่อมต่อกับอุปกรณ์ Industrial IoT ผ่านโปรโตคอล RS485 (Modbus RTU) พร้อมระบบวิเคราะห์สุขภาพเครื่องจักรด้วย AI

🚀 คุณสมบัติเด่น (Features)

Real-time Dashboard: ติดตามยอดผลิต พลังงาน และค่าคาร์บอนฟุตพริ้นท์

Multi-Node Monitoring: รองรับการจัดการข้อมูลได้สูงสุด 10 Nodes พร้อมกันผ่านระบบจำลอง

Predictive Maintenance: แสดงสถานะสุขภาพเครื่องจักร (Health Score) พร้อมระบบแจ้งเตือนสีตามเกณฑ์ความเสี่ยง

Responsive UI: พัฒนาด้วย Streamlit ให้รองรับการใช้งานผ่านมือถือและแท็บเล็ตหน้างาน

📂 โครงสร้างโปรเจกต์ (Project Structure)

main_app.py: ไฟล์หลักสำหรับระบบ Login และตัวเลือกเมนูเข้าสู่ระบบ

pages/:

1_Monitor.py: หน้าแสดงผล Dashboard กราฟ และสถานะ Node 1-10

2_Contact.py: หน้าข้อมูลการติดต่อทีมสนับสนุน

documents/:

deploy_guide.md: คู่มือการติดตั้งระบบ

standard_factors.md: เกณฑ์มาตรฐานค่าคาร์บอนและพลังงานที่ใช้อ้างอิง

mock_data.csv: ฐานข้อมูลจำลองรายชื่อเครื่องจักรและสถานที่ติดตั้ง

system_logs.txt: บันทึกเหตุการณ์จำลองที่เกิดขึ้นในระบบ

🛠 การติดตั้งเพื่อใช้งานในเครื่อง (Local Setup)

Clone repository นี้: git clone https://github.com/snapcon1992-cloud/snapcon.git

ติดตั้ง Library: pip install -r requirements.txt

รันโปรแกรม: python -m streamlit run main_app.py

© 2024 Snapcon Automation Solution | Smart Industry 4.0
