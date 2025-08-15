class Jar:
    def __init__(self, capacity: int = 12):
        if not (isinstance(capacity, int) and capacity >= 0):
            raise ValueError
        self._capacity = capacity
        self._size: int = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n: int):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n: int):
        if self._size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
