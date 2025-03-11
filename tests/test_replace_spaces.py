import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_basic_space_replacement():
    """Test basic space replacement in a simple string."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_multiple_spaces():
    """Test replacement of multiple spaces."""
    assert replace_spaces_with_underscores("hello  world") == "hello__world"

def test_leading_trailing_spaces():
    """Test replacement of leading and trailing spaces."""
    assert replace_spaces_with_underscores("  spaces  ") == "__spaces__"

def test_empty_string():
    """Test behavior with an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_no_spaces():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_none_input():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)

def test_mixed_whitespace():
    """Test mixed whitespace characters."""
    assert replace_spaces_with_underscores("hello world\ttest") == "hello_world\ttest"