import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglądamy kolejkę
        return str(self.items)

    def insert(self, item):
        self.items.append(item)

    def remove(self):    # zwraca losowy element
        size = len(self.items) - 1
        value = random.randint(0, size)
        self.items[size], self.items[value] = self.items[value], self.items[size]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):  # dynamicznie
        return False

    def clear(self):      # czyszczenie listy
        while not self.is_empty():
             self.remove()
