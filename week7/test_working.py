import pytest
from working import convert


def test_9am_to_5pm():
    """Test 9 AM to 5 PM converts to 09:00 to 17:00"""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_9_00am_to_5_00pm():
    """Test 9:00 AM to 5:00 PM converts to 09:00 to 17:00"""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_10am_to_8_50pm():
    """Test 10 AM to 8:50 PM converts to 10:00 to 20:50"""
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_10_30pm_to_8am():
    """Test 10:30 PM to 8 AM converts to 22:30 to 08:00"""
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalid_minutes_raises_valueerror():
    """Test 9:60 AM to 5:60 PM raises ValueError"""
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_format_dash_raises_valueerror():
    """Test 9 AM - 5 PM raises ValueError"""
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_invalid_format_pm_after_24hour_raises_valueerror():
    """Test 09:00 AM - 17:00 PM raises ValueError"""
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")