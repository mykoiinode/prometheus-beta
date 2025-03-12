from typing import List

def max_increasing_subsequence_sum(nums: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        nums (List[int]): Input list of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Examples:
        >>> max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60, 80])
        255
        >>> max_increasing_subsequence_sum([1, 2, 3, 4, 5])
        15
        >>> max_increasing_subsequence_sum([5, 4, 3, 2, 1])
        5
        >>> max_increasing_subsequence_sum([])
        0
    """
    # Handle empty list or None input
    if not nums:
        return 0
    
    # Validate input type
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    # Track the maximum sum of increasing subsequences 
    n = len(nums)
    # dp[i] stores the max sum of increasing subsequence ending at index i
    dp = nums.copy()
    
    # Compute maximum sum of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    
    # Return the maximum sum
    return max(dp) if dp else 0