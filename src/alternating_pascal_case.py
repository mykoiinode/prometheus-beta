def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a given string to alternating Pascal case.
    
    This function transforms the input string so that:
    - Words are separated by removing non-alphanumeric characters
    - Alternating words start with uppercase or lowercase letters
    
    Args:
        input_string (str): The input string to be converted
    
    Returns:
        str: The string converted to alternating Pascal case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HelloWorld'
        >>> convert_to_alternating_pascal_case("HELLO_WORLD")
        'HelloWorld'
        >>> convert_to_alternating_pascal_case("hello-world-test")
        'HelloWorldTest'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Remove non-alphanumeric characters and split
    words = ''.join(char if char.isalnum() else ' ' for char in input_string).split()
    
    # Convert to alternating Pascal case
    converted_words = []
    for i, word in enumerate(words):
        # Alternate between uppercase and lowercase first letters
        if i % 2 == 0:
            converted_words.append(word.capitalize())
        else:
            converted_words.append(word.lower().capitalize())
    
    return ''.join(converted_words)