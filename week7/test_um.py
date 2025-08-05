from um import count


def test_single_um():
    """Test that 'um' returns count of 1"""
    assert count("um") == 1


def test_um_with_punctuation():
    """Test that 'um?' returns count of 1"""
    assert count("um?") == 1


def test_um_in_sentence():
    """Test that 'Um, thanks for the album.' returns count of 1"""
    assert count("Um, thanks for the album.") == 1


def test_multiple_ums():
    """Test that 'Um, thanks, um...' returns count of 2"""
    assert count("Um, thanks, um...") == 2


def test_um_as_part_of_word():
    """Test that 'um' as part of another word doesn't count"""
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("medium") == 0
    assert count("yummy") == 0


def test_case_insensitive():
    """Test that count is case insensitive"""
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1


def test_empty_string():
    """Test that empty string returns 0"""
    assert count("") == 0


def test_no_ums():
    """Test that string with no 'um' returns 0"""
    assert count("hello world") == 0

