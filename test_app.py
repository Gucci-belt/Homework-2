"""
ไฟล์ทดสอบ (Unit Test) สำหรับ Greeting API
ไฟล์นี้คือ "ผู้คุมกฎ" ที่เราจะไม่แตะต้องอีกเลย
"""
import unittest
import app  

class TestApp(unittest.TestCase):
    
    def test_greet_bob(self):
        
        self.assertEqual(app.greet("Bob"), "Hello, Bob!")

    def test_greet_alice(self):
        
        self.assertEqual(app.greet("Alice"), "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()