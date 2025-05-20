from matrix import Matrix

def main():
    m1 = Matrix()
    m1.read()
    print("Matrix 1:")
    print(m1)

    m2 = Matrix()
    m2.read()
    print("Matrxi 2:")
    print(m2)

    m3 = m1 + m2
    print("Result:")
    print(m3)

if __name__ == "__main__":
    main()
