import unittest
from mean import calculate_matrix_mean

class TestMatrixMean(unittest.TestCase):
    def test_basic_matrix(self):
        self.assertEqual(calculate_matrix_mean([[1, 2], [3, 4]]), 2.5)
        
    def test_float_matrix(self):
        self.assertEqual(calculate_matrix_mean([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]), 4.0)
        
    def test_single_element(self):
        self.assertEqual(calculate_matrix_mean([[0]]), 0.0)
        
    def test_same_values(self):
        self.assertEqual(calculate_matrix_mean([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 1.0)
        
    def test_negative_numbers(self):
        self.assertEqual(calculate_matrix_mean([[-1, -2], [-3, -4]]), -2.5)
        
    def test_zeros(self):
        self.assertEqual(calculate_matrix_mean([[0, 0], [0, 0]]), 0.0)
        
    def test_large_numbers(self):
        self.assertEqual(calculate_matrix_mean([[1000, 2000], [3000, 4000]]), 2500.0)
        
    def test_small_decimals(self):
        self.assertEqual(calculate_matrix_mean([[0.1, 0.2], [0.3, 0.4]]), 0.25)
        
    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            calculate_matrix_mean([])
            
    def test_empty_row(self):
        with self.assertRaises(ValueError):
            calculate_matrix_mean([[]])

if __name__ == '__main__':
    unittest.main()