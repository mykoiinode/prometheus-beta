import pytest
from src.email_validator import validate_email

def test_valid_email_addresses():
    """Test that valid email addresses are correctly validated."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@example-domain.com",
        "user+tag@example.com",
        "user.name@example.org"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_email_addresses():
    """Test that invalid email addresses are rejected."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "user@",  # No domain
        "@example.com",  # No local part
        "user@example",  # Missing top-level domain
        "user@.com",  # Invalid domain
        "user@example..com",  # Double dot in domain
        "very_long_email_" + "a"*250 + "@example.com"  # Too long
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test various edge cases for email validation."""
    # Test case sensitivity
    assert validate_email("USER@EXAMPLE.COM") is True
    assert validate_email("user@Example.Com") is True

    # Test special characters in local part
    special_char_emails = [
        "user.name+tag@example.com",
        "user_name-tag@example.com"
    ]
    for email in special_char_emails:
        assert validate_email(email) is True