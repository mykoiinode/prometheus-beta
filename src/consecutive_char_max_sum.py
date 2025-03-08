def max_consecutive_char_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The maximum length of consecutive characters.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> max_consecutive_char_sum("abcdef")  # Length of consecutive chars
        6
        >>> max_consecutive_char_sum("a")
        1
        >>> max_consecutive_char_sum("abcabcabc")
        3
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # If string has only one character, return 1
    if len(input_string) == 1:
        return 1
    
    # Track the max length of consecutive characters
    max_consecutive = 1
    current_consecutive = 1
    
    for i in range(1, len(input_string)):
        # Check if current character is consecutive with previous character
        if ord(input_string[i]) == ord(input_string[i-1]) + 1:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            # Reset current consecutive count if not consecutive
            current_consecutive = 1
    
    return max_consecutive