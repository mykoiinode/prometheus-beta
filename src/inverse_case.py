def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case (swap uppercase and lowercase).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to inverse case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_inverse_case("Hello World")
        'hELLO wORLD'
        >>> convert_to_inverse_case("PyTHON")
        'pYthon'
        >>> convert_to_inverse_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a list comprehension with swapcase to handle each character
    return ''.join(char.swapcase() for char in input_string)