import pytest
from src.list_pair_products import calculate_pair_products

def test_basic_pair_products():
    """Test basic functionality with positive integers."""
    result = calculate_pair_products([1, 2, 3])
    assert result == [1, 2, 3, 2, 4, 6, 3, 6, 9]

def test_with_zero():
    """Test list including zero."""
    result = calculate_pair_products([0, 1, 2])
    assert result == [0, 0, 0, 0, 1, 2, 0, 2, 4]

def test_with_negative_numbers():
    """Test list with negative numbers."""
    result = calculate_pair_products([-1, 0, 1])
    assert result == [1, 0, -1, 0, 0, 0, -1, 0, 1]

def test_single_element_list():
    """Test list with a single element."""
    result = calculate_pair_products([5])
    assert result == [25]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        calculate_pair_products([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_pair_products("not a list")

def test_non_integer_elements_raises_error():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3"])