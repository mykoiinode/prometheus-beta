from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of distinct integers
    
    Returns:
        int: Number of ways to partition the list into two subsets with equal sums
    """
    # Handle empty list or single element
    if len(numbers) <= 1:
        return 0
    
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0
    
    target_sum = total_sum // 2
    n = len(numbers)
    
    # Dynamic programming to track valid subset sums
    dp = set([0])
    unique_partitions = set()
    
    # Generate all possible subset sums
    for num in numbers:
        # Create a copy to avoid modifying the set during iteration
        current_sums = dp.copy()
        for curr_sum in current_sums:
            new_sum = curr_sum + num
            if new_sum == target_sum:
                # Find the subset that creates this sum
                subset = tuple(sorted(x for x in numbers if x in [num]))
                unique_partitions.add(frozenset([subset]))
            if new_sum <= target_sum:
                dp.add(new_sum)
    
    return len(unique_partitions)