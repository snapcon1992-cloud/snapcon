🛠 Snapcon Deployment Guide

คู่มือการติดตั้งระบบจัดการ Automation และ Dashboard

1. การเตรียมสภาพแวดล้อม (Prerequisites)

ติดตั้ง Python 3.9 ขึ้นไป

ติดตั้ง Library ที่จำเป็น:

pip install streamlit pandas plotly


2. โครงสร้างโปรเจกต์ (Structure)

เพื่อให้ระบบเรียกหน้าย่อยได้ถูกต้อง ต้องจัดโครงสร้างดังนี้:

/main_app.py

/Logo.png

/pages/1_Monitor.py

/pages/2_Contact.py

/documents/ (เก็บไฟล์นี้)

3. การรันระบบ (Execution)

รันคำสั่งที่ Terminal ในโฟลเดอร์หลัก:

python -m streamlit run main_app.py


4. บัญชีเข้าใช้งานเริ่มต้น (Default Users)

User: 001 | Pass: 123

User: admin | Pass: admin