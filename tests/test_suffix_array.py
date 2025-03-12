import pytest
from src.suffix_array import create_suffix_array, find_substring

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    text = "banana"
    expected = [5, 3, 1, 0, 4, 2]  # Indices of lexicographically sorted suffixes
    assert create_suffix_array(text) == expected

def test_create_suffix_array_single_char():
    """Test suffix array for single character string"""
    text = "a"
    assert create_suffix_array(text) == [0]

def test_create_suffix_array_repeated_chars():
    """Test suffix array with repeated characters"""
    text = "aaa"
    assert create_suffix_array(text) == [2, 1, 0]

def test_create_suffix_array_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        create_suffix_array(123)
    
    with pytest.raises(ValueError):
        create_suffix_array("")

def test_find_substring_basic():
    """Test basic substring search"""
    text = "banana"
    pattern = "ana"
    assert find_substring(text, pattern) == [1, 3]

def test_find_substring_no_match():
    """Test substring search with no matches"""
    text = "hello world"
    pattern = "xyz"
    assert find_substring(text, pattern) == []

def test_find_substring_single_match():
    """Test substring search with single match"""
    text = "programming"
    pattern = "gram"
    assert find_substring(text, pattern) == [5]

def test_find_substring_full_match():
    """Test substring search where pattern is the entire text"""
    text = "hello"
    pattern = "hello"
    assert find_substring(text, pattern) == [0]

def test_find_substring_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_substring(123, "test")
    
    with pytest.raises(TypeError):
        find_substring("test", 123)
    
    with pytest.raises(ValueError):
        find_substring("", "test")
    
    with pytest.raises(ValueError):
        find_substring("test", "")