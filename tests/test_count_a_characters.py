import pytest
from src.count_a_characters import count_a_characters

def test_count_a_characters_basic():
    """Test basic functionality of counting 'a' characters."""
    assert count_a_characters("Apple") == 1
    assert count_a_characters("aAaA") == 4
    assert count_a_characters("hello") == 0

def test_count_a_characters_empty_string():
    """Test counting 'a' characters in an empty string."""
    assert count_a_characters("") == 0

def test_count_a_characters_case_sensitivity():
    """Verify case-insensitive counting."""
    assert count_a_characters("AbcdA") == 2

def test_count_a_characters_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_a_characters(123)
    with pytest.raises(TypeError):
        count_a_characters(None)

def test_count_a_characters_long_string():
    """Test counting 'a' in a longer string."""
    test_string = "a" * 1000 + "b" * 1000
    assert count_a_characters(test_string) == 1000

def test_count_a_characters_mixed_case():
    """Test counting 'a' in a mixed-case string."""
    assert count_a_characters("AbCdEfAaA") == 4