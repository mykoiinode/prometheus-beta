import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic_true():
    """Test basic palindromes"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("") == False

def test_palindrome_basic_false():
    """Test non-palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindrome_case_sensitivity():
    """Test case-sensitive behavior"""
    assert is_palindrome("Racecar") == False
    assert is_palindrome("A") == True
    assert is_palindrome("aA") == False

def test_palindrome_special_characters():
    """Test palindromes with special characters and numbers"""
    assert is_palindrome("!@#$%^&*()") == False
    assert is_palindrome("a!b@b!a") == True
    assert is_palindrome("123321") == True

def test_palindrome_edge_cases():
    """Test edge cases"""
    assert is_palindrome(" ") == False
    assert is_palindrome("a") == True
    assert is_palindrome("aa") == True