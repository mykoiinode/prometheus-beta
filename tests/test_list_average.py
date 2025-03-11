import pytest
from src.list_average import calculate_list_average

def test_calculate_list_average_basic():
    """Test basic average calculation."""
    assert calculate_list_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_list_average_float():
    """Test average calculation with float numbers."""
    assert calculate_list_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_list_average_single_element():
    """Test average with a single element."""
    assert calculate_list_average([42]) == 42.0

def test_calculate_list_average_mixed_numbers():
    """Test average with mixed integer and float numbers."""
    assert calculate_list_average([1, 2.5, 3, 4.5]) == 2.75

def test_calculate_list_average_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_list_average([])

def test_calculate_list_average_non_numeric_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        calculate_list_average([1, 2, 'three', 4])

def test_calculate_list_average_non_list_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_list_average("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_list_average(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_list_average(None)