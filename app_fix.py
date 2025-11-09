"""
Version 2: AI Fix (with new Hardcoding Bug)
AI แก้ไขโดยการ "Hardcode" คำตอบให้ Bob
แต่ลืมแก้ไขกรณีทั่วไป
"""
def greet(name):
    if name == "Bob":
        return "Hello, Bob!"  # <--- AI แก้ไข "Bob" ถูกต้อง
    else:
        # บั๊กเก่ายังคงอยู่สำหรับ "Alice"
        return f"Hi, {name}!" # <--- BUG!