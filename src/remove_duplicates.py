def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers.
    
    This function efficiently removes duplicates from a pre-sorted list 
    by keeping only the first occurrence of each unique value.
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is not sorted
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 1, 2, 3, 3, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([5])
        [5]
    """
    # Check input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not sorted_list:
        return []
    
    # Validate sorted order
    for i in range(1, len(sorted_list)):
        if sorted_list[i] < sorted_list[i-1]:
            raise ValueError("Input list must be sorted in ascending order")
    
    # Remove duplicates
    unique_list = []
    for num in sorted_list:
        # Add only if list is empty or number is different from last added
        if not unique_list or num != unique_list[-1]:
            unique_list.append(num)
    
    return unique_list