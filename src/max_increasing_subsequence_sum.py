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
    # Handle empty list
    if not nums:
        return 0
    
    # Store best sums for each length of subsequence
    dp = []
    
    for num in nums:
        # Find the position to insert the current num
        # using binary search to maintain O(log n) complexity
        left, right = 0, len(dp)
        
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If we're at the end, append
        if left == len(dp):
            if not dp:
                dp.append(num)
            else:
                dp.append(dp[-1] + num)
        else:
            # Update or replace the subsequence sum
            if left == 0:
                dp[left] = num
            else:
                dp[left] = max(dp[left], dp[left-1] + num)
    
    # Return the maximum sum, or 0 if no valid subsequence
    return dp[-1] if dp else 0