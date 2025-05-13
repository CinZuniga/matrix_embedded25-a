class Matrix:
    def __init__(self):
        self.data = []
        self.rows = 0
        self.cols = 0

    def read(self):
        """Read matrix dimensions and data from user input"""
        line = input().split()
        self.rows, self.cols = int(line[0]), int(line[1])

        for i in range(self.rows):
            line = input().split()
            row = list(map(int, line))
            self.data.append(row)
        return self.data

    @staticmethod
    def add(m1, m2):
        """Add two matrices"""
        if not m1 or not m2:
            raise ValueError("Matrices cannot be empty")
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise ValueError("Matrices must have same dimensions")

        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                row.append(m1[i][j] + m2[i][j])
            result.append(row)
        return result

    def __str__(self):
        """String representation of the matrix"""
        return str(self.data)

def main():
    print("Simple Matrix")
    matrix = Matrix()
    matrix.read()
    print(matrix)

if __name__ == "__main__":
    main()

