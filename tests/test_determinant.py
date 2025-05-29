from matrix import Matrix

class TestDeterminant:

    def test_determinant_2x2(self):
        # setup
        m = Matrix()
        m._matrix = [[1, 2], [3, 4]]

        # test
        result = m.determinant()
        expected = -2
        assert result == expected, f"Expected {expected}, but got {result}"

    def test_determinant_3x3(self):
        # setup
        m = Matrix()
        m._matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]

        # test
        result = m.determinant()
        expected = -306
        assert result == expected, f"Expected {expected}, but got {result}"

    def test_determinant_not_square(self):
        # setup
        m = Matrix()
        m._matrix = [[1, 2, 3], [4, 5, 6]]

        # test
        try:
            m.determinant()
            assert False, "Expected an exception but none was raised"
        except Exception as e:
            assert str(e) == "Determinant can only be calculated for square matrices", f"Expected 'Determinant can only be calculated for square matrices', but got {str(e)}"