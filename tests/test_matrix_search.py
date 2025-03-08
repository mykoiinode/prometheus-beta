import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    """Test basic matrix search scenarios"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Test finding existing elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 17) == True
    
    # Test for non-existing elements
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 18) == False

def test_search_matrix_edge_cases():
    """Test edge cases for matrix search"""
    # Single element matrix
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 6) == False
    
    # Single row matrix
    matrix_single_row = [[1, 2, 3, 4, 5]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 6) == False
    
    # Single column matrix
    matrix_single_col = [[1], [2], [3], [4], [5]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 6) == False

def test_search_matrix_input_validation():
    """Test input validation and error handling"""
    # Empty matrix
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    # None input
    with pytest.raises(ValueError):
        search_matrix(None, 5)
    
    # Irregular matrix
    with pytest.raises(TypeError):
        search_matrix([[1, 2], [3]], 5)

def test_search_matrix_large():
    """Test search in a larger matrix"""
    large_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    
    # Test various positions
    assert search_matrix(large_matrix, 5) == True
    assert search_matrix(large_matrix, 30) == True
    assert search_matrix(large_matrix, 1) == True
    assert search_matrix(large_matrix, 25) == False