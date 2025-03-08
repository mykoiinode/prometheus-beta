import pytest
from src.count_factors import count_factors

def test_count_factors_prime_number():
    """Test counting factors for a prime number"""
    assert count_factors(7) == 2

def test_count_factors_perfect_square():
    """Test counting factors for a perfect square"""
    assert count_factors(16) == 5

def test_count_factors_composite_number():
    """Test counting factors for a composite number"""
    assert count_factors(12) == 6

def test_count_factors_one():
    """Test counting factors for 1"""
    assert count_factors(1) == 1

def test_count_factors_large_number():
    """Test counting factors for a larger number"""
    assert count_factors(100) == 9

def test_invalid_input_negative():
    """Test handling of negative input"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(-5)

def test_invalid_input_zero():
    """Test handling of zero input"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(0)

def test_invalid_input_non_integer():
    """Test handling of non-integer input"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        count_factors(3.14)
    with pytest.raises(ValueError, match="Input must be an integer"):
        count_factors("not a number")