def input_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have {cols} elements.")
        matrix.append(row)
    return matrix

def subtract_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(matrix_a, matrix_b)):
        raise ValueError("Matrices must be of the same dimensions.")
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(matrix_a, matrix_b)]

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    A = input_matrix(rows, cols, "Matrix A")
    B = input_matrix(rows, cols, "Matrix B")
    result = subtract_matrices(A, B)
    print("Result of subtraction:")
    for row in result:
        print(row)