import math
from points import Point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):  # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return math.pi * self.radius ** 2

    def move(self, x, y):  # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):  # najmniejszy okrąg pokrywający oba
        if self.pt == other.pt:
            return Circle(self.pt.x, self.pt.y, max(self.radius, other.radius))
        else:
            radius = (((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2) ** (
                    1 / 2) + self.radius + other.radius) / 2
            x = abs(self.pt.x - other.pt.x) / 2
            y = abs(self.pt.y - other.pt.y) / 2
            return Circle(x, y, radius)
