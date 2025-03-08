import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([42]) == 42

def test_alternating_positive_negative():
    """Test an array with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_large_numbers():
    """Test with large numbers."""
    assert max_subarray_sum([1000000, -500000, 600000]) == 1100000

def test_zero_included():
    """Test an array that includes zero."""
    assert max_subarray_sum([0, -1, 2, 0, 3, -2]) == 5

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_subarray_sum([])