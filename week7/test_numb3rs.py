from numb3rs import validate


def test_valid_localhost():
    """Test that 127.0.0.1 returns True"""
    assert validate("127.0.0.1") == True


def test_valid_max_address():
    """Test that 255.255.255.255 returns True"""
    assert validate("255.255.255.255") == True


def test_invalid_over_255():
    """Test that 512.512.512.512 returns False"""
    assert validate("512.512.512.512") == False


def test_invalid_last_octet_over_255():
    """Test that 1.2.3.1000 returns False"""
    assert validate("1.2.3.1000") == False


def test_invalid_leading_zero():
    """Test that 192.168.001.1 returns False (leading zero)"""
    assert validate("192.168.001.1") == False


def test_invalid_non_numeric():
    """Test that 'cat' returns False"""
    assert validate("cat") == False


# Additional edge case tests
def test_valid_zero_address():
    """Test that 0.0.0.0 returns True"""
    assert validate("0.0.0.0") == True


def test_invalid_negative():
    """Test that negative numbers return False"""
    assert validate("-1.0.0.1") == False


def test_invalid_too_few_octets():
    """Test that addresses with fewer than 4 octets return False"""
    assert validate("192.168.1") == False


def test_invalid_too_many_octets():
    """Test that addresses with more than 4 octets return False"""
    assert validate("192.168.1.1.1") == False


def test_invalid_empty_string():
    """Test that empty string returns False"""
    assert validate("") == False


def test_invalid_double_dots():
    """Test that double dots return False"""
    assert validate("192..1.1") == False


def test_invalid_trailing_dot():
    """Test that trailing dot returns False"""
    assert validate("192.168.1.1.") == False


def test_invalid_leading_dot():
    """Test that leading dot returns False"""
    assert validate(".192.168.1.1") == False


def test_invalid_spaces():
    """Test that spaces in address return False"""
    assert validate("192.168.1. 1") == False


def test_invalid_letters_mixed():
    """Test that mixed letters and numbers return False"""
    assert validate("192.168.a.1") == False