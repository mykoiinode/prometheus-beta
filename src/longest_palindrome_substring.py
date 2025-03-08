def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    This function uses the expand around center approach, which has 
    O(n^2) time complexity and O(1) space complexity.
    
    Args:
        s (str): Input string to search for palindromes
    
    Returns:
        str: The longest palindromic substring
    
    Edge cases:
    - Empty string returns empty string
    - Single character returns that character
    - Multiple palindromes of same length returns first occurrence
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    # Initialize variables to track longest palindrome
    start, max_length = 0, 0
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> int:
        """Expand palindrome around center and return its length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    # Iterate through each character as a potential center
    for i in range(len(s)):
        # Check for odd length palindromes
        length1 = expand_around_center(i, i)
        
        # Check for even length palindromes
        length2 = expand_around_center(i, i + 1)
        
        # Take the maximum length
        curr_length = max(length1, length2)
        
        # Update start and max_length if current is longer
        if curr_length > max_length:
            start = i - (curr_length - 1) // 2
            max_length = curr_length
    
    return s[start:start + max_length]