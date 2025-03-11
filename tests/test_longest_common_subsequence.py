import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("HELLO", "") == ""
    assert longest_common_subsequence("", "WORLD") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there is no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HeLLo", "Hello") == "HLo"

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "ABC")

def test_repeated_characters():
    """Test scenarios with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAA") == "AAAAA"
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_complex_subsequence():
    """Test more complex subsequence scenarios"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"
    assert longest_common_subsequence("XMJYAUZ", "MZJAWXU") == "MJAU"