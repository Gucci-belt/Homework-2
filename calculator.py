def divide(a, b):
    """
    ฟังก์ชันหารเลข (นี่คือฟังก์ชันที่มีบั๊ก)
    BUG: จะเกิดอะไรขึ้นถ้า b เป็น 0?
    """
    return a / b

if __name__ == "__main__":
    print("Calculator app started.")
    print(f"10 / 2 = {divide(10, 2)}")
    
    # บรรทัดนี้จะทำให้โปรแกรมพัง!
    print(f"10 / 0 = {divide(10, 0)}")