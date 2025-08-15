from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    
    try:
        Jar(-1)
        assert False
    except ValueError:
        pass


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    
    jar.deposit(3)
    assert jar.size == 8
    
    try:
        jar.deposit(10)  # Would exceed capacity of 12
        assert False
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    
    jar.withdraw(4)
    assert jar.size == 3
    
    try:
        jar.withdraw(5)  # Would go below 0
        assert False
    except ValueError:
        pass
