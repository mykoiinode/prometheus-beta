import pytest
from src.longest_palindrome_substring import longest_palindromic_substring

def test_basic_odd_length_palindrome():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_basic_even_length_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_multiple_palindromes():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_longer_than_one():
    assert longest_palindromic_substring("abcde") in list("abcde")

def test_repeated_characters():
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"

def test_mixed_palindromes():
    result = longest_palindromic_substring("ababaccc")
    assert result in ["ababa", "bacccab", "aba"]

def test_complex_string():
    result = longest_palindromic_substring("babadada")
    assert result in ["adada", "babab"]

def test_long_string():
    long_str = "a" * 1000 + "b" + "a" * 1000
    assert longest_palindromic_substring(long_str) == long_str

def test_case_sensitivity():
    assert longest_palindromic_substring("Abba") == "bb"