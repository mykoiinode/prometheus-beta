def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, return the actual subsequence. 
                                          If False, return the length. Defaults to False.
    
    Returns:
        int or list: Length of the longest increasing subsequence, 
                     or the subsequence itself depending on return_sequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60])
        5
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60], return_sequence=True)
        [10, 22, 33, 50, 60]
        >>> longest_increasing_subsequence([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return [] if return_sequence else 0
    
    # Length of the array
    n = len(arr)
    
    # Dynamic programming arrays
    # lengths tracks the length of LIS ending at each index
    lengths = [1] * n
    
    # predecessors tracks the previous index in the subsequence
    predecessors = [None] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            # If current element can extend previous subsequence
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
        
        # Update max length
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # If we just want the length
    if not return_sequence:
        return max_length
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current is not None:
        subsequence.append(arr[current])
        current = predecessors[current]
    
    # Reverse to get correct order
    return list(reversed(subsequence))