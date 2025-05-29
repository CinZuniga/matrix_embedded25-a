
def calculate_matrix_mean(matrix):
    """
    Calculate the mean value of all elements in a matrix
    Args:
        matrix: A list of lists representing the matrix
    Returns:
        float: Mean value of all elements
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Calculate sum of all elements
    total_sum = 0
    element_count = 0
    
    # Iterate through each row and element
    for row in matrix:
        for element in row:
            total_sum += element
            element_count += 1
    
    # Calculate mean
    mean_value = total_sum / element_count
    
    return float(mean_value)