from plates import is_valid


def test_valid_plates():
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True
    assert is_valid("HELLO1") == True
    assert is_valid("CS50") == True


def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEF7") == False
    assert is_valid("TOOLONG") == False


def test_invalid_characters():
    assert is_valid("AB.123") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB!123") == False
    assert is_valid("AB@123") == False


def test_invalid_start():
    assert is_valid("1BC123") == False
    assert is_valid("12C123") == False
    assert is_valid("A1C123") == False


def test_invalid_numbers():
    assert is_valid("AB0123") == False
    assert is_valid("ABC012") == False
    assert is_valid("AB12CD") == False
    assert is_valid("AB1C23") == False


def test_edge_cases():
    assert is_valid("") == False
    assert is_valid("123456") == False
    assert is_valid("ABCDEF") == True