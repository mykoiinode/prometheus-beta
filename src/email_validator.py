import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validation criteria:
    - Must have a local part (before @)
    - Must have a domain part (after @)
    - Local part can contain letters, digits, and some special characters
    - Domain must have at least one dot
    - Total length should not exceed 254 characters
    """
    # Check overall length
    if not email or len(email) > 254:
        return False

    # Regular expression for email validation
    # Breaks down to:
    # 1. Local part: allow letters, digits, and some special characters
    # 2. @ symbol
    # 3. Domain: allows letters, digits, hyphens, subdomains
    # 4. Top-level domain: at least 2 characters, letters only
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    return bool(re.match(email_regex, email))