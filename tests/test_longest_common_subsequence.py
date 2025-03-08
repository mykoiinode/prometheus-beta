import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_subsequence():
    """Test basic longest common subsequence"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test handling of empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("ABC", "ABC") == "ABC"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("XYZ", "ABC") == ""

def test_partial_subsequence():
    """Test partial subsequence scenarios"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BDAB"

def test_single_character_subsequence():
    """Test subsequence with single character"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("AbC", "aBc") == ""
    assert longest_common_subsequence("abc", "abc") == "abc"

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCABC", "ABCABC") == "ABCABC"