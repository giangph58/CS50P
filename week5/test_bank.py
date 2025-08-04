from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, newman") == 0
    assert value("HELLO") == 0


def test_h_words():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How you doing?") == 20


def test_other_greetings():
    assert value("good morning") == 100
    assert value("what's happening?") == 100
    assert value("") == 100