import colorama
from typing import Optional, Literal

# Initialize colorama for cross-platform color support
colorama.init(autoreset=True)

def log_colored_message(
    message: str, 
    color: Optional[Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']] = None
) -> str:
    """
    Log a message in a specified color.

    Args:
        message (str): The message to be logged.
        color (Optional[str]): The color to use for logging. 
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
            If None, returns the message without color.

    Returns:
        str: The colored message or original message if no color specified.

    Raises:
        ValueError: If an unsupported color is provided.
    """
    # Color mapping
    color_map = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'blue': colorama.Fore.BLUE,
        'magenta': colorama.Fore.MAGENTA,
        'cyan': colorama.Fore.CYAN,
        'white': colorama.Fore.WHITE
    }

    # Validate color input
    if color is not None and color not in color_map:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_map.keys())}")

    # Return colored message or original message
    if color is None:
        return message
    
    return f"{color_map[color]}{message}"