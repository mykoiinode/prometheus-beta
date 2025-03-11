def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.

    Gnome Sort (Stupid Sort) is a simple sorting algorithm that works similar to 
    how a gnome would sort a line of flower pots. It works by moving an element 
    to its proper place by comparing adjacent elements and swapping them if they 
    are in the wrong order.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: A new sorted list in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Strict type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Create a new list to avoid modifying the original
    arr = list(arr)

    # If the list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Check if all elements are comparable
    try:
        test_comparison = all(a <= b for a, b in zip(arr, arr[1:]))
    except TypeError:
        raise TypeError("List contains elements that cannot be compared")

    # Start from the second element (index 1)
    i = 1
    while i < len(arr):
        # If this is the first element or previous element is in correct order, move forward
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            # If current element is smaller, swap with previous element
            arr[i], arr[i-1] = arr[i-1], arr[i]
            # Move back to check if this swap disrupted previous ordering
            i -= 1

    return arr