def create_suffix_array(text):
    """
    Create a suffix array for the given text.
    
    A suffix array is a sorted array of all suffixes of a given string.
    
    Args:
        text (str): The input string to create a suffix array for.
    
    Returns:
        list: A list of indices representing the sorted suffixes.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Create a list of tuples with (suffix, original index)
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort suffixes lexicographically
    sorted_suffixes = sorted(suffixes)
    
    # Extract and return only the indices
    return [index for _, index in sorted_suffixes]

def find_substring(text, pattern):
    """
    Find all occurrences of a pattern in the text using suffix array.
    
    Args:
        text (str): The text to search in.
        pattern (str): The substring to search for.
    
    Returns:
        list: List of starting indices where the pattern is found.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If either input is empty.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Create suffix array
    suffix_array = create_suffix_array(text)
    
    # Find the pattern in the sorted suffixes
    results = []
    for suffix_index in suffix_array:
        # Check if current suffix starts with the pattern
        if text[suffix_index:].startswith(pattern):
            results.append(suffix_index)
    
    return results  # Return indices as found (matches original test case)