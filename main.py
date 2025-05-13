from matrix_operations import MatrixOperations

def main():
    matrix_ops = MatrixOperations()
    print("Simple Matrix Operations")
    print("Reading first matrix:")
    m1 = matrix_ops.read()
    print("Reading second matrix:")
    m2 = matrix_ops.read()
    print("Adding matrices...")
    result = matrix_ops.add(m1, m2)
    print("Resultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
