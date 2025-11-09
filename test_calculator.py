import unittest
import calculator  # Import ไฟล์ calculator.py ของคุณ

class TestCalculator(unittest.TestCase):
    
    def test_divide_normal(self):
        """
        ทดสอบการหารปกติ
        """
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """
        [นี่คือส่วนที่แก้ไข]
        ทดสอบการหารด้วยศูนย์
        เราคาดหวังว่าฟังก์ชันจะ "คืนค่า None" (ตามที่ AI แก้ไข)
        แทนที่จะ "พัง"
        """
        
        # ใช้ assertIsNone เพื่อตรวจสอบว่าผลลัพธ์คือ None
        self.assertIsNone(calculator.divide(10, 0), "การหารด้วย 0 ควรจะคืนค่า None")
        
        # (หรือจะใช้แบบนี้ก็ได้: self.assertEqual(calculator.divide(10, 0), None))

# --- ส่วนอื่นๆ ของไฟล์เทส (ถ้ามี) ---
# def test_add(self):
#     ...
# def test_subtract(self):
#     ...

if __name__ == '__main__':
    unittest.main()