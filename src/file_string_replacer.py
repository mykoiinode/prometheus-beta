"""
A module for replacing strings in files.
"""

def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.

    Returns:
        int: Number of replacements made.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If any input is not a string.
        ValueError: If old_string is empty.
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(old_string, str):
        raise TypeError("old_string must be a string")
    if not isinstance(new_string, str):
        raise TypeError("new_string must be a string")
    
    # Check for empty old_string
    if not old_string:
        raise ValueError("old_string cannot be empty")
    
    # Read the file contents
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Count and perform replacements
    replacements = content.count(old_string)
    modified_content = content.replace(old_string, new_string)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)
    
    return replacements