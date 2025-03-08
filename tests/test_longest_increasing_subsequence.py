import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_length():
    """Test basic functionality of returning length"""
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_basic_sequence():
    """Test returning the actual subsequence"""
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60], return_sequence=True) == [10, 22, 33, 50, 60]

def test_empty_list():
    """Test empty list handling"""
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([], return_sequence=True) == []

def test_single_element():
    """Test list with single element"""
    assert longest_increasing_subsequence([5]) == 1
    assert longest_increasing_subsequence([5], return_sequence=True) == [5]

def test_non_increasing_list():
    """Test list with no increasing subsequence"""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subsequence([5, 4, 3, 2, 1], return_sequence=True) == [5]

def test_fully_increasing_list():
    """Test fully increasing list"""
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence([1, 2, 3, 4, 5], return_sequence=True) == [1, 2, 3, 4, 5]

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")
    with pytest.raises(TypeError):
        longest_increasing_subsequence(123)
    with pytest.raises(TypeError):
        longest_increasing_subsequence(None)