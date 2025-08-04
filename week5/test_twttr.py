from twttr import shorten


def test_lowercase_vowels():
    assert shorten("hello") == "hll"


def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"


def test_mixed_case():
    assert shorten("HeLLo") == "HLL"


def test_no_vowels():
    assert shorten("xyz") == "xyz"


def test_only_vowels():
    assert shorten("aeiou") == ""


def test_numbers_and_punctuation():
    assert shorten("hello123!") == "hll123!"