def count_a_characters(input_string: str) -> int:
    """
    Count the number of 'a' characters in a given string, ignoring case sensitivity.

    Args:
        input_string (str): The input string to count 'a' characters in.

    Returns:
        int: The number of 'a' characters in the string (case-insensitive).

    Examples:
        >>> count_a_characters("Apple")
        1
        >>> count_a_characters("aAaA")
        4
        >>> count_a_characters("hello")
        0
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower().count('a')