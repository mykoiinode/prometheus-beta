def max_consecutive_char_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The maximum sum of consecutive characters.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> max_consecutive_char_sum("abcdef")  # All chars are consecutive
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
    
    # If string has only one character, return its ASCII value
    if len(input_string) == 1:
        return ord(input_string[0])
    
    # Track the max sum of consecutive characters
    max_sum = 0
    current_sum = ord(input_string[0])
    
    for i in range(1, len(input_string)):
        # Check if current character is consecutive with previous character
        if ord(input_string[i]) == ord(input_string[i-1]) + 1:
            current_sum += ord(input_string[i])
        else:
            # Reset current sum if not consecutive
            max_sum = max(max_sum, current_sum)
            current_sum = ord(input_string[i])
    
    # Final check to update max_sum
    max_sum = max(max_sum, current_sum)
    
    return max_sum