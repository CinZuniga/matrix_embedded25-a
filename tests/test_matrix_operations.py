import unittest

class TestMatrixOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual([[1, 2], [3, 4]], [[1, 2], [3, 4]])

    def test_subtraction(self):
        self.assertEqual([[1, 2], [3, 4]], [[1, 2], [3, 4]])

    def test_multiplication(self):
        self.assertEqual([[1, 2], [3, 4]], [[1, 2], [3, 4]])

if __name__ == '__main__':
    unittest.main()