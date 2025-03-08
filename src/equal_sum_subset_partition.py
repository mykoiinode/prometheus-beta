from typing import List, Set
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of distinct integers
    
    Returns:
        int: Number of ways to partition the list into two subsets with equal sums
    
    Raises:
        ValueError: If input list is empty or contains duplicate numbers
    """
    # Validate input
    if not numbers:
        return 0
    
    # Check for duplicates
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input must contain only distinct numbers")
    
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0
    
    target_sum = total_sum // 2
    count = 0
    
    # Try all possible combinations 
    for r in range(1, len(numbers) // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset can form half the total sum
            if sum(subset) == target_sum:
                # Verify the complement also has the same sum
                complement = [num for num in numbers if num not in subset]
                if sum(complement) == target_sum:
                    count += 1
    
    # Divide by 2 to avoid double counting
    return count // 2