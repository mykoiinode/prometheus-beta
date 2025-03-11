import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_case():
    """Test a typical array with positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    """Test an array with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    """Test an array with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test an array with a single element"""
    assert max_subarray_sum([42]) == 42

def test_mixed_numbers():
    """Test an array with mixed positive and negative numbers"""
    assert max_subarray_sum([1, -3, 2, 1, -1]) == 3

def test_zero_included():
    """Test an array that includes zero"""
    assert max_subarray_sum([-1, 0, -2]) == 0

def test_invalid_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test that an empty list raises ValueError"""
    with pytest.raises(ValueError):
        max_subarray_sum([])