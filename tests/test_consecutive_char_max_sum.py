import pytest
from src.consecutive_char_max_sum import max_consecutive_char_sum

def test_basic_consecutive_string():
    """Test a basic string with consecutive characters"""
    assert max_consecutive_char_sum("abcdef") == 6

def test_single_character():
    """Test a single character string"""
    assert max_consecutive_char_sum("a") == 1

def test_multiple_consecutive_sequences():
    """Test string with multiple consecutive sequences"""
    assert max_consecutive_char_sum("abcabcdef") == 3

def test_no_consecutive_characters():
    """Test string with no consecutive characters"""
    assert max_consecutive_char_sum("acegik") == 1

def test_repeated_consecutive_sequences():
    """Test string with repeated consecutive sequences"""
    assert max_consecutive_char_sum("abcabcabc") == 3

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        max_consecutive_char_sum(123)

def test_empty_string():
    """Test that ValueError is raised for empty string"""
    with pytest.raises(ValueError):
        max_consecutive_char_sum("")