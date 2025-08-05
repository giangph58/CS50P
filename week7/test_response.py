from response import is_valid


def test_valid_malan_email():
    """Test that malan@harvard.edu is valid"""
    assert is_valid("malan@harvard.edu") == "Valid"


def test_valid_standard_email():
    """Test that standard email formats are valid"""
    assert is_valid("user@example.com") == "Valid"
    assert is_valid("test@domain.org") == "Valid"
    assert is_valid("name.surname@company.co.uk") == "Valid"


def test_invalid_multiple_at_signs():
    """Test that malan@@@harvard.edu is invalid"""
    assert is_valid("malan@@@harvard.edu") == "Invalid"


def test_invalid_extra_dot_before_extension():
    """Test that email with extra dot before .com is invalid"""
    assert is_valid("user@example..com") == "Invalid"
    assert is_valid("test@domain..org") == "Invalid"


def test_invalid_missing_at_sign():
    """Test that email without @ is invalid"""
    assert is_valid("userdomain.com") == "Invalid"


def test_invalid_missing_domain():
    """Test that email without domain is invalid"""
    assert is_valid("user@") == "Invalid"
    assert is_valid("user@.com") == "Invalid"


def test_invalid_missing_local_part():
    """Test that email without local part is invalid"""
    assert is_valid("@domain.com") == "Invalid"


def test_invalid_empty_string():
    """Test that empty string is invalid"""
    assert is_valid("") == "Invalid"


def test_invalid_no_extension():
    """Test that email without extension is invalid"""
    assert is_valid("user@domain") == "Invalid"