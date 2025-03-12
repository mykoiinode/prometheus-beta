import pytest
from src.alternating_pascal_case import convert_to_alternating_pascal_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating Pascal case."""
    assert convert_to_alternating_pascal_case("hello world") == "HelloWorld"
    assert convert_to_alternating_pascal_case("hello-world") == "HelloWorld"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert convert_to_alternating_pascal_case("hello world test") == "HelloWorldTest"
    assert convert_to_alternating_pascal_case("hello-world-test") == "HelloWorldTest"

def test_mixed_case_input():
    """Test input with mixed case and separators."""
    assert convert_to_alternating_pascal_case("HELLO_world") == "HelloWorld"
    assert convert_to_alternating_pascal_case("hello_WORLD") == "HelloWorld"

def test_alternating_case():
    """Test that words alternate between starting with uppercase and lowercase."""
    assert convert_to_alternating_pascal_case("first second third") == "FirstSecondThird"
    assert convert_to_alternating_pascal_case("first-second-third") == "FirstSecondThird"

def test_edge_cases():
    """Test edge cases like empty string and single word."""
    assert convert_to_alternating_pascal_case("") == ""
    assert convert_to_alternating_pascal_case("single") == "Single"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(None)

def test_special_characters():
    """Test handling of special characters and multiple separators."""
    assert convert_to_alternating_pascal_case("hello!!world") == "HelloWorld"
    assert convert_to_alternating_pascal_case("hello@#$world") == "HelloWorld"