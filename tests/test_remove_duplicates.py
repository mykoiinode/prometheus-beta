import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal in a sorted list"""
    assert remove_duplicates([1, 1, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_empty_list():
    """Test handling of an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test list with a single element"""
    assert remove_duplicates([5]) == [5]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([2, 2, 2, 2]) == [2]

def test_remove_duplicates_invalid_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_unsorted_list():
    """Test handling of an unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        remove_duplicates([3, 1, 2, 4])

def test_remove_duplicates_negative_numbers():
    """Test list with negative numbers"""
    assert remove_duplicates([-3, -3, -1, 0, 0, 2, 2]) == [-3, -1, 0, 2]