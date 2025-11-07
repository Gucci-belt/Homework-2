import unittest
from calculator import divide

class TestCalculator(unittest.TestCase):

    def test_divide_success(self):
        """
        เทสกรณีปกติ: 10 / 2 ควรได้ 5
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        เทสกรณีที่มีบั๊ก: 10 / 0
        เราคาดหวังว่าฟังก์ชันที่แก้แล้วจะคืนค่า None
        """
        self.assertIsNone(divide(10, 0))

if __name__ == '__main__':
    unittest.main()