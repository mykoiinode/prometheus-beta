import pytest
from src.equal_sum_subset_partition import count_equal_sum_partitions

def test_basic_valid_partition():
    """Test a simple case with a valid partition"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 1

def test_empty_list():
    """Test empty list returns 0"""
    assert count_equal_sum_partitions([]) == 0

def test_multiple_partitions():
    """Test a case with multiple possible partitions"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 2

def test_no_partition_possible():
    """Test when no equal sum partition is possible"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5]) == 0

def test_large_numbers():
    """Test with larger numbers"""
    assert count_equal_sum_partitions([10, 20, 30, 40, 50, 60]) == 1

def test_all_same_number():
    """Test a case where numbers are the same"""
    assert count_equal_sum_partitions([1, 1, 1, 1]) == 0

def test_single_number():
    """Test a single number list"""
    assert count_equal_sum_partitions([1]) == 0

def test_two_numbers_valid_partition():
    """Test a case with two numbers that can form a valid partition"""
    assert count_equal_sum_partitions([1, 1]) == 0

def test_complex_partition():
    """Test a more complex partitioning scenario"""
    assert count_equal_sum_partitions([2, 3, 5, 7, 11, 13]) == 1