import pytest
from src.even_sum_odd_count import analyze_list_numbers

def test_mixed_list():
    """Test a list with mixed even and odd numbers."""
    result = analyze_list_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_all_even_list():
    """Test a list containing only even numbers."""
    result = analyze_list_numbers([2, 4, 6, 8, 10])
    assert result == (30, 0)

def test_all_odd_list():
    """Test a list containing only odd numbers."""
    result = analyze_list_numbers([1, 3, 5, 7, 9])
    assert result == (0, 5)

def test_empty_list():
    """Test an empty list."""
    result = analyze_list_numbers([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test a list with negative numbers."""
    result = analyze_list_numbers([-1, -2, -3, -4, -5])
    assert result == (-6, 3)

def test_mixed_negative_positive():
    """Test a list with mixed negative and positive numbers."""
    result = analyze_list_numbers([-2, 1, 3, -4, 5, 6])
    assert result == (0, 3)

def test_invalid_input_not_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_list_numbers("not a list")

def test_invalid_input_non_integer():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        analyze_list_numbers([1, 2, "3", 4])