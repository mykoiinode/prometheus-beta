import pytest
from src.gnome_sort import gnome_sort

def test_gnome_sort_basic_list():
    """Test sorting a basic list of integers."""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = [1, 2, 5, 6, 7, 9]
    assert gnome_sort(input_list) == expected

def test_gnome_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert gnome_sort(input_list) == input_list

def test_gnome_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert gnome_sort(input_list) == expected

def test_gnome_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert gnome_sort(input_list) == expected

def test_gnome_sort_empty_list():
    """Test sorting an empty list."""
    assert gnome_sort([]) == []

def test_gnome_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert gnome_sort(input_list) == input_list

def test_gnome_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert gnome_sort(input_list) == expected

def test_gnome_sort_with_strings():
    """Test sorting a list of strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = ['apple', 'banana', 'cherry', 'date']
    assert gnome_sort(input_list) == expected

def test_gnome_sort_invalid_input():
    """Test that an error is raised for invalid input types."""
    with pytest.raises(TypeError):
        gnome_sort("not a list")
    with pytest.raises(TypeError):
        gnome_sort(123)
    with pytest.raises(TypeError):
        gnome_sort(None)