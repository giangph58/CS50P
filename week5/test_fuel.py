import pytest
from fuel import convert, gauge


def test_convert_valid_fractions():
    """Test convert function with valid fractions."""
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 66
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_convert_edge_cases():
    """Test convert function with edge cases."""
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert(" 1 / 2 ") == 50
    assert convert("50/100") == 50


def test_convert_invalid_format():
    """Test convert function with invalid format inputs."""
    with pytest.raises(ValueError, match="Invalid format. Use X/Y format"):
        convert("1")
    
    with pytest.raises(ValueError, match="Invalid format. Use X/Y format"):
        convert("1/2/3")
    
    with pytest.raises(ValueError, match="Invalid format. Use X/Y format"):
        convert("abc")
    
    with pytest.raises(ValueError, match="Invalid format. Use X/Y format"):
        convert("")


def test_convert_non_integer_values():
    """Test convert function with non-integer numerator/denominator."""
    with pytest.raises(ValueError, match="Numerator and denominator must be integers"):
        convert("1.5/2")
    
    with pytest.raises(ValueError, match="Numerator and denominator must be integers"):
        convert("1/2.5")
    
    with pytest.raises(ValueError, match="Numerator and denominator must be integers"):
        convert("a/2")
    
    with pytest.raises(ValueError, match="Numerator and denominator must be integers"):
        convert("1/b")


def test_convert_zero_denominator():
    """Test convert function with zero denominator."""
    with pytest.raises(ZeroDivisionError, match="Denominator cannot be zero"):
        convert("1/0")
    
    with pytest.raises(ZeroDivisionError, match="Denominator cannot be zero"):
        convert("5/0")


def test_convert_numerator_greater_than_denominator():
    """Test convert function when numerator > denominator."""
    with pytest.raises(ValueError, match="Numerator cannot be greater than denominator"):
        convert("5/4")
    
    with pytest.raises(ValueError, match="Numerator cannot be greater than denominator"):
        convert("10/3")
    
    with pytest.raises(ValueError, match="Numerator cannot be greater than denominator"):
        convert("100/99")


def test_gauge_empty():
    """Test gauge function for empty fuel (E)."""
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    """Test gauge function for full fuel (F)."""
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    """Test gauge function for percentage display."""
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"


def test_gauge_edge_cases():
    """Test gauge function with edge cases."""
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"