import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from matrix import Matrix

class TestMatrix:

    def test_add_2x2(self):
        # setup
        m1 = Matrix()
        m1._matrix = [[1,1], [1,1,]]
        m2 = Matrix()
        m2._matrix = [[1,1], [1,1,]]

        expected = Matrix()
        expected._matrix = [[2,2], [2,2]]

        # test
        result = m1 + m2

        assert result._matrix == expected._matrix, f"Expected {expected._matrix}, but got {result._matrix}"

    def test_add_3x3(self):
        # setup
        m1 = Matrix()
        m1._matrix = [[1,2,3], [4,5,6], [7,8,9]]
        m2 = Matrix()
        m2._matrix = [[9,8,7], [6,5,4], [3,2,1]]

        expected = Matrix()
        expected._matrix = [[10,10,10], [10,10,10], [10,10,10]]

        # test
        result = m1 + m2

        assert result._matrix == expected._matrix, f"Expected {expected._matrix}, but got {result._matrix}"

    def test_add_fail_dimentions(self):
        # setup
        m1 = Matrix()
        m1._matrix = [[1,2,3], [4,5,6]]
        m2 = Matrix()
        m2._matrix = [[1,2], [3,4]]

        # test
        try:
            result = m1 + m2
            assert False, "Expected an exception but none was raised"
        except Exception as e:
            assert str(e) == "Wrong dimentions", f"Expected 'Wrong dimentions', but got {str(e)}"
    
    def test_add_empty_matrix(self):
        # setup
        m1 = Matrix()
        m1._matrix = []
        m2 = Matrix()
        m2._matrix = [[1,2,3], [4,5,6]]
        expected = Matrix()
        expected._matrix = [[1,2,3], [4,5,6]]

        # test
        try:
            result = m1 + m2
            assert False, "Expected an exception but none was raised"
        except Exception as e:
            assert str(e) == "Wrong dimentions", f"Expected 'Wrong dimentions', but got {str(e)}"

    def test_inverse_2x2(self):
        m = Matrix()
        m._matrix = [[4, 7], [2, 6]]
        inv = m.inverse()

        expected = Matrix()
        expected._matrix = [[0.6, -0.7], [-0.2, 0.4]]

        for i in range(2):
            for j in range(2):
                assert abs(inv._matrix[i][j] - expected._matrix[i][j]) < 1e-6, \
                    f"Mismatch at ({i},{j}): expected {expected._matrix[i][j]}, got {inv._matrix[i][j]}"

    def test_inverse_singular(self):
        m = Matrix()
        m._matrix = [[1, 2], [2, 4]]  # Singular matrix

        try:
            m.inverse()
            assert False, "Expected exception for singular matrix"
        except Exception as e:
            assert "singular" in str(e).lower(), f"Expected singular matrix error, got: {str(e)}"

    def test_inverse_non_square(self):
        m = Matrix()
        m._matrix = [[1, 2, 3], [4, 5, 6]]

        try:
            m.inverse()
            assert False, "Expected exception for non-square matrix"
        except Exception as e:
            assert "square" in str(e).lower(), f"Expected square matrix error, got: {str(e)}"

