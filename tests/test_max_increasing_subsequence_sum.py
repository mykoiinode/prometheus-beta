import pytest
from src.max_increasing_subsequence_sum import max_increasing_subsequence_sum

def test_basic_increasing_sequence():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255

def test_decreasing_sequence():
    assert max_increasing_subsequence_sum([5, 4, 3, 2, 1]) == 5

def test_empty_list():
    assert max_increasing_subsequence_sum([]) == 0

def test_single_element():
    assert max_increasing_subsequence_sum([42]) == 42

def test_repeated_elements():
    assert max_increasing_subsequence_sum([1, 1, 1, 1, 1]) == 1

def test_negative_numbers():
    assert max_increasing_subsequence_sum([-1, -2, -3, -4, -5]) == -1

def test_mixed_positive_and_negative():
    assert max_increasing_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 7

def test_large_sequence():
    large_seq = list(range(1, 1001))
    assert max_increasing_subsequence_sum(large_seq) == sum(range(1, 1001))

def test_invalid_input():
    with pytest.raises(TypeError):
        max_increasing_subsequence_sum(None)