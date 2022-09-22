class Stack:

    def __init__(self, ultimatesize=3):
        self.items = ultimatesize * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = ultimatesize

    def __str__(self):   # podglądamy kolejkę
        return str(self.items)

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n >= self.size:
            raise ValueError("Stos pełny")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Pusty stos")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

