"""
Tests for the file string replacer function.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_replace_string_in_file(tmp_path):
    """Test basic string replacement in a file."""
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello universe!")
    
    # Perform replacement
    replacements = replace_string_in_file(str(test_file), "Hello", "Hi")
    
    # Check results
    assert replacements == 2
    assert test_file.read_text() == "Hi world! Hi universe!"

def test_replace_with_empty_string(tmp_path):
    """Test replacing with an empty string."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")
    
    replacements = replace_string_in_file(str(test_file), "world", "")
    
    assert replacements == 1
    assert test_file.read_text() == "Hello !"

def test_no_replacements(tmp_path):
    """Test when no replacements are made."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")
    
    replacements = replace_string_in_file(str(test_file), "universe", "galaxy")
    
    assert replacements == 0
    assert test_file.read_text() == "Hello world!"

def test_replace_with_longer_string(tmp_path):
    """Test replacing with a longer string."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello universe!")
    
    replacements = replace_string_in_file(str(test_file), "Hello", "Greetings")
    
    assert replacements == 2
    assert test_file.read_text() == "Greetings world! Greetings universe!"

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("/path/to/nonexistent/file.txt", "old", "new")

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string(tmp_path):
    """Test handling of empty old string."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")
    
    with pytest.raises(ValueError):
        replace_string_in_file(str(test_file), "", "new")