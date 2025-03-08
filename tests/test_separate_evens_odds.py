import pytest
from src.separate_evens_odds import separate_evens_odds

def test_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    result = separate_evens_odds([1, 2, 3, 4, 5, 6])
    assert result == ([2, 4, 6], [1, 3, 5])

def test_only_even_numbers():
    """Test with only even numbers."""
    result = separate_evens_odds([2, 4, 6, 8])
    assert result == ([2, 4, 6, 8], [])

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = separate_evens_odds([1, 3, 5, 7])
    assert result == ([], [1, 3, 5, 7])

def test_empty_list():
    """Test with an empty list."""
    result = separate_evens_odds([])
    assert result == ([], [])

def test_single_even_number():
    """Test with a single even number."""
    result = separate_evens_odds([2])
    assert result == ([2], [])

def test_single_odd_number():
    """Test with a single odd number."""
    result = separate_evens_odds([1])
    assert result == ([], [1])

def test_zero_handling():
    """Test handling of zero (which is even)."""
    result = separate_evens_odds([0, 1, 2, 3])
    assert result == ([0, 2], [1, 3])

def test_negative_numbers():
    """Test with negative numbers."""
    result = separate_evens_odds([-1, -2, -3, -4])
    assert result == ([-2, -4], [-1, -3])