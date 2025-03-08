def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward.
    This implementation is case-sensitive and considers all characters.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        False
        >>> is_palindrome("12321")
        True
    """
    # Trim whitespace and handle empty string or single space case
    s = s.strip()
    if not s:
        return False
    
    # Compare the string with its reverse
    return s == s[::-1]