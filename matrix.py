class Matrix:
    _matrix = None

    def __init__(self):
        self._matrix = []

    def read(self):
        line = input("Enter rows and columns: ").split()
        rows, cols = int(line[0]), int(line[1])

        self._matrix = []
        print("Enter the matrix row by row:")
        for i in range(rows):
            line = input().split()
            row = list(map(int, line))
            self._matrix.append(row)

        return self

    def __add__(self, other):
        return self.add(self, other)
    
    def no_rows(self):
        return len(self._matrix)
    
    def no_cols(self):
        return len(self._matrix[0])

    def add(self, m1, m2):
        if m1.no_rows() != m2.no_rows() or m1.no_cols() != m2.no_cols():
            raise Exception("Wrong dimentions")

        result = Matrix()
        for i in range(m1.no_rows()):
            row = []
            for j in range(m1.no_cols()):
                row.append(m1._matrix[i][j] + m2._matrix[i][j])
            result._matrix.append(row)

        return result

    def __str__(self):
        return self.pretty_print()

    def pretty_print(self):
        """
        Overloads the string operator to return a formatted string representation of the matrix
        Returns:
            str: Formatted string representing the matrix
        """
        if not self._matrix:
            return "Empty matrix"
            
        # Find the maximum width for proper alignment
        max_width = 0
        for row in self._matrix:
            for elem in row:
                width = len(str(elem))
                if width > max_width:
                    max_width = width
        
        # Build the formatted string
        matrix_str = ""
        for i, row in enumerate(self._matrix):
            # Format each number with consistent spacing
            formatted_row = [str(num).rjust(max_width) for num in row]
            matrix_str += "[" + " ".join(formatted_row) + "]"
            if i < len(self._matrix) - 1:
                matrix_str += "\n"
                
        return matrix_str
    
    def __repr__(self):
        return self.pretty_print(self, '')
    
    def __utf__(self):
        return self.pretty_print(self, '')
    
    def determinant(self):
        if self.no_rows() != self.no_cols():
            raise Exception("Determinant can only be calculated for square matrices")

        def compute_determinant(matrix):
            # Base case for 2x2 matrix
            if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

            # Recursive case for larger matrices
            determinant = 0
            for col in range(len(matrix)):
                sub_matrix = [
                    [matrix[row][sub_col] for sub_col in range(len(matrix)) if sub_col != col]
                    for row in range(1, len(matrix))
                ]
                determinant += ((-1) ** col) * matrix[0][col] * compute_determinant(sub_matrix)
            return determinant

        return compute_determinant(self._matrix)