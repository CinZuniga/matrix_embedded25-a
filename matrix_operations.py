class MatrixOperations:
    def __init__(self):
        pass

    def read(self):
        line = input("Enter rows and columns: ").split()
        rows, cols = int(line[0]), int(line[1])

        m = []
        print("Enter the matrix row by row:")
        for i in range(rows):
            line = input().split()
            row = list(map(int, line))
            m.append(row)
        return m

    def add(self, m1, m2):
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise ValueError("Matrices must have the same dimensions to be added.")

        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                row.append(m1[i][j] + m2[i][j])
            result.append(row)
        return result
    
    def dot_product(self, m1, m2):
        if len(m1[0]) != len(m2):
            raise ValueError("Number of columns in first matrix must match number of rows in second matrix")
        
        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m2[0])):
                element = 0
                for k in range(len(m2)):
                    element += m1[i][k] * m2[k][j]
                row.append(element)
            result.append(row)
        return result