import pytest
import colorama
from src.colorful_logger import log_colored_message

def test_log_colored_message_no_color():
    """Test logging a message without specifying a color."""
    message = "Hello, World!"
    assert log_colored_message(message) == message

def test_log_colored_message_supported_colors():
    """Test logging messages with supported colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    message = "Colored Message"
    
    for color in colors:
        color_code = getattr(colorama.Fore, color.upper())
        expected = f"{color_code}{message}"
        assert log_colored_message(message, color) == expected

def test_log_colored_message_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored_message("Test", "invalid_color")

def test_log_colored_message_empty_string():
    """Test logging an empty string."""
    assert log_colored_message("") == ""
    assert log_colored_message("", "green") == colorama.Fore.GREEN

def test_log_colored_message_long_message():
    """Test logging a long message with different colors."""
    long_message = "This is a very long message that tests multiple color logging scenarios."
    
    for color in ['red', 'blue', 'magenta']:
        color_code = getattr(colorama.Fore, color.upper())
        expected = f"{color_code}{long_message}"
        assert log_colored_message(long_message, color) == expected