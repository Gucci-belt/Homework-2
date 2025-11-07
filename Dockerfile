# 1. ใช้ Base Image
FROM python:3.10-slim

# 2. ตั้งค่า Working Directory
WORKDIR /app

# 3. คัดลอกโค้ด
# เราจะคัดลอก calculator.py (ซึ่งใน CI จะเป็นเวอร์ชันที่แก้แล้ว)
COPY calculator.py .

# 4. คำสั่งสำหรับ Run
# เมื่อรัน Container มันจะรันไฟล์ calculator.py
CMD ["python", "calculator.py"]