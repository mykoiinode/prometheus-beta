def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of unique integers 
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or None
        TypeError: If the input is not a valid matrix of integers
    
    Time Complexity: O(T * R), where T is number of rows and R is number of columns
    Space Complexity: O(1)
    """
    # Validate input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Check if matrix is valid (all rows have same length)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Matrix must be rectangular")
    
    # Linear search through the matrix
    for row in matrix:
        for cell in row:
            if cell == target:
                return True
    
    return False