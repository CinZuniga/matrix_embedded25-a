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

    def pretty_print(self, matrix, title="Matrix"):
        """
        Prints a matrix in a formatted way with a title
        Args:
            matrix: 2D list representing the matrix
            title: Optional string to display as matrix title
        """
        print(f"\n{title}:")
        if not matrix:
            print("Empty matrix")
            return
            
        # Find the maximum width needed for any element
        max_width = max(len(str(element)) 
                       for row in matrix 
                       for element in row)
        
        # Print the matrix with aligned columns
        for row in matrix:
            formatted_row = [str(elem).rjust(max_width) for elem in row]
            print("[" + " ".join(formatted_row) + "]")