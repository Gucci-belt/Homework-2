"""
ไฟล์ทดสอบ (Unit Test) สำหรับ Greeting API
ไฟล์นี้คือ "ผู้คุมกฎ" ที่เราจะไม่แตะต้องอีกเลย
"""
import unittest
import app  # Import โค้ดหลักของเรา (app.py)

class TestApp(unittest.TestCase):
    
    def test_greet_bob(self):
        """
        กฎข้อที่ 1: ถ้าทักทาย 'Bob'
        ต้องได้ 'Hello, Bob!'
        """
        self.assertEqual(app.greet("Bob"), "Hello, Bob!")

    def test_greet_alice(self):
        """
        กฎข้อที่ 2: ถ้าทักทาย 'Alice'
        ต้องได้ 'Hello, Alice!'
        """
        self.assertEqual(app.greet("Alice"), "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()