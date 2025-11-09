def divide(a, b):
    """
    ฟังก์ชันหารเลข (เวอร์ชันแก้ไขโดย AI)
    FIX: AI ตรวจสอบว่าตัวหารเป็น 0 หรือไม่
    """
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None  # คืนค่า None แทนที่จะพัง
        
    return a / b

if __name__ == "__main__":
    print("Calculator app started (Fixed Version).")
    print(f"10 / 2 = {divide(10, 2)}")
    
    # บรรทัดนี้จะไม่พังแล้ว
    print(f"10 / 0 = {divide(10, 0)}")