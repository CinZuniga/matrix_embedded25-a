import unittest
from substract import substract

class TestSubstract(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(substract(10, 5), 5)
        self.assertEqual(substract(100, 50), 50)
        self.assertEqual(substract(7, 3), 4)
        self.assertEqual(substract(20, 10), 10)

    def test_negative_numbers(self):
        self.assertEqual(substract(-10, -5), -5)
        self.assertEqual(substract(-7, -3), -4)
        self.assertEqual(substract(-20, 10), -30)
        self.assertEqual(substract(10, -20), 30)

    def test_zero(self):
        self.assertEqual(substract(0, 0), 0)
        self.assertEqual(substract(0, 5), -5)
        self.assertEqual(substract(5, 0), 5)
        self.assertEqual(substract(-5, 0), -5)

    def test_mixed_types(self):
        self.assertEqual(substract(5.5, 2.2), 3.3)
        self.assertEqual(substract(-5.5, 2.2), -7.7)
        self.assertEqual(substract(5, 2.2), 2.8)
        self.assertEqual(substract(2.2, 5), -2.8)

if __name__ == '__main__':
    unittest.main()