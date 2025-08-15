from datetime import date, timedelta

from seasons import calculate_minutes_lived, is_valid_date


def test_is_valid_date_valid_format():
    """Test that valid date format returns True"""
    assert is_valid_date("2023-01-01")
    assert is_valid_date("1990-12-25")
    assert is_valid_date("2000-02-29")


def test_is_valid_date_invalid_format():
    """Test that invalid date formats return False"""
    assert not is_valid_date("01-01-2023")
    assert not is_valid_date("2023/01/01")
    assert not is_valid_date("January 1, 2023")
    assert not is_valid_date("not-a-date")
    assert not is_valid_date("")


def test_edge_case_february_29_leap_year():
    """Test handling of February 29 in leap years"""
    assert is_valid_date("2020-02-29")
    assert not is_valid_date("2021-02-29")


def test_calculate_minutes_lived_one_regular_year():
    """Test calculation for one year ago (365 days = 525,600 minutes)"""
    today = date.today()
    one_year_ago = today - timedelta(days=365)
    expected_minutes = 365 * 24 * 60  # 525,600 minutes
    assert (
        calculate_minutes_lived(one_year_ago.strftime("%Y-%m-%d")) == expected_minutes
    )


def test_calculate_minutes_lived_leap_year():
    """Test calculation accounting for leap years"""
    today = date.today()
    # Test with a date that includes a leap year
    one_leap_year_ago = today - timedelta(days=366)
    expected_minutes = 366 * 24 * 60  # 527,040 minutes
    assert (
        calculate_minutes_lived(one_leap_year_ago.strftime("%Y-%m-%d"))
        == expected_minutes
    )


def test_calculate_minutes_lived_two_years():
    """Test calculation for two years ago"""
    today = date.today()
    two_years_ago = today - timedelta(days=730)  # Approximately 2 years
    expected_minutes = 730 * 24 * 60  # 1,051,200 minutes
    assert (
        calculate_minutes_lived(two_years_ago.strftime("%Y-%m-%d")) == expected_minutes
    )


def test_calculate_minutes_lived_birth_today():
    """Test calculation for someone born today (should be 0 minutes)"""
    today = date.today()
    assert calculate_minutes_lived(today.strftime("%Y-%m-%d")) == 0
