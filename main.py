from matrix_operations import MatrixOperations

def main():
    matrix_ops = MatrixOperations()
    print("Simple Matrix Operations")
    print("Reading first matrix:")
    m1 = matrix_ops.read()
    matrix_ops.pretty_print(m1, "First Matrix")
    
    print("\nReading second matrix:")
    m2 = matrix_ops.read()
    matrix_ops.pretty_print(m2, "Second Matrix")
    
    print("\nAdding matrices...")
    result = matrix_ops.add(m1, m2)
    matrix_ops.pretty_print(result, "Result Matrix")

if __name__ == "__main__":
    main()
