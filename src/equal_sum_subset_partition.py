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
    count = 0
    
    # Try all possible subset combinations
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # If subset sum equals target sum
            if sum(subset) == target_sum:
                # Check complement 
                complement = [num for num in numbers if num not in subset]
                
                # Verify complement also sums to target
                if sum(complement) == target_sum:
                    count += 1
    
    return count // 2  # Divide by 2 to avoid double counting