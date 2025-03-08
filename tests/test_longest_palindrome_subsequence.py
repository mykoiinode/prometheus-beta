import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_longest_palindrome_subsequence():
    # Test basic cases
    assert longest_palindrome_subsequence("bbbab") == 4  # "bbbb"
    assert longest_palindrome_subsequence("cbbd") == 2   # "bb"
    
    # Test edge cases
    assert longest_palindrome_subsequence("") == 0      # Empty string
    assert longest_palindrome_subsequence("a") == 1     # Single character
    
    # More complex cases
    assert longest_palindrome_subsequence("racecar") == 7  # Entire string is palindrome
    assert longest_palindrome_subsequence("abcdef") == 1  # No palindrome longer than 1
    
    # Repeated characters
    assert longest_palindrome_subsequence("aaaaaa") == 6  # All characters same
    
    # Mixed characters
    assert longest_palindrome_subsequence("abcda") == 3   # Partial palindrome
    
    # Long string with multiple possible subsequences
    assert longest_palindrome_subsequence("abcdefghijklmnopqrstuvwxyz") == 1  # No palindrome
    
    # Advanced complex case
    assert longest_palindrome_subsequence("BBABCBCAB") == 7  # Longer subsequence