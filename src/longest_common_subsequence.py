def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        'ADH'
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        'GTAB'
        >>> longest_common_subsequence("", "HELLO")
        ''
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, return empty string
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store lengths of common subsequences
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence with a preference for lexicographically earlier subsequences
    def backtrack_subsequence(str1, str2, dp):
        lcs = []
        i, j = len(str1), len(str2)
        
        # Collect all possible common subsequences with max length
        max_length = dp[-1][-1]
        possible_subsequences = []
        
        def backtrack(current_lcs, current_i, current_j):
            # If subsequence is complete
            if len(current_lcs) == max_length:
                # Store the subsequence in the list
                possible_subsequences.append(''.join(reversed(current_lcs)))
                return
            
            # Try all possible paths
            if current_i > 0 and current_j > 0 and str1[current_i-1] == str2[current_j-1]:
                backtrack(current_lcs + [str1[current_i-1]], current_i-1, current_j-1)
            
            if current_i > 0 and (current_j == 0 or dp[current_i-1][current_j] >= dp[current_i][current_j-1]):
                backtrack(current_lcs, current_i-1, current_j)
            
            if current_j > 0 and (current_i == 0 or dp[current_i][current_j-1] >= dp[current_i-1][current_j]):
                backtrack(current_lcs, current_i, current_j-1)
        
        # Start backtracking
        backtrack([], i, j)
        
        # Return the lexicographically smallest subsequence
        return min(possible_subsequences) if possible_subsequences else ''
    
    return backtrack_subsequence(str1, str2, dp)