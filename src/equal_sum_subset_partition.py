from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of integers
    
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
    count = 0
    
    # Optimization: use set to track unique partition combinations
    unique_partitions = set()
    
    # Try all possible combinations 
    for r in range(1, len(numbers) // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset can form half the total sum
            if sum(subset) == target_sum:
                # Get the complement
                complement = tuple(sorted(num for num in numbers if num not in subset))
                
                # Verify the complement also has the same sum and add to unique partitions
                if sum(complement) == target_sum:
                    # Sort to avoid duplicate counting
                    partition = tuple(sorted(subset))
                    
                    # Use frozenset to avoid duplicate partition representations
                    unique_partitions.add(frozenset([partition, complement]))
    
    return len(unique_partitions)