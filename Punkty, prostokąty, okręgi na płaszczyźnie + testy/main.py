import unittest

from circles import *
from rectangles import *


class TestRectangle(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Rectangle(0, 0, 5, 5)), "[(0, 0), (5, 5)]")
        self.assertEqual(repr(Rectangle(0, 0, 5, 5)), "Rectangle(0, 0, 5, 5)")
        self.assertEqual(str(Rectangle(-5, -5, 5, 5)), "[(-5, -5), (5, 5)]")
        self.assertEqual(repr(Rectangle(-5, -5, 5, 5)), "Rectangle(-5, -5, 5, 5)")


    def test_cmp(self):
        self.assertTrue(Rectangle(0, 0, 5, 5) == Rectangle(0, 0, 5, 5))
        self.assertFalse(Rectangle(0, 0, 5, 5) != Rectangle(0, 0, 5, 5))
        self.assertTrue(Rectangle(-5, -5, 5, 5) != Rectangle(-5, -5, 0, 0))
        self.assertFalse(Rectangle(-5, -5, 0, 0) == Rectangle(0, 0, 5, 5))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 10, 10).center(), Point(5, 5))
        self.assertEqual(Rectangle(-5, -5, 5, 5).center(), Point(0, 0))

    def test_area(self):
        self.assertEqual(Rectangle(-5, -5, 5, 5).area(), 100)
        self.assertEqual(Rectangle(0, 0, 5, -5).area(), 25)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 5, 5).move(5, 5), Rectangle(5, 5, 10, 10))
        self.assertEqual(Rectangle(-5, -5, 0, 0).move(5, 5), Rectangle(0, 0, 5, 5))

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 5, 5).intersection(Rectangle(0, 0, 5, 5)), Rectangle(0, 0, 5, 5))
        self.assertEqual(Rectangle(-5, -5, 5, 5).intersection(Rectangle(0, 0, 5, 5)), Rectangle(0, 0, 5, 5))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 5, 5).cover(Rectangle(0, 0, 5, 5)), Rectangle(0, 0, 5, 5))
        self.assertEqual(Rectangle(-5, -5, 5, 5).cover(Rectangle(0, 0, 5, 5)), Rectangle(-5, -5, 5, 5))

    def test_make4(self):
        self.assertEqual(Rectangle(0, 0, 10, 10).make4(), (Rectangle(0, 0, 5, 5), Rectangle(5, 0, 10, 5),
                                                         Rectangle(0, 5, 5, 10), Rectangle(5, 5, 10, 10)))
        self.assertEqual(Rectangle(-5, -5, 5, 5).make4(), (Rectangle(-5, -5, 0, 0), Rectangle(0, -5, 5, 0),
                                                         Rectangle(-5, 0, 0, 5), Rectangle(0, 0, 5, 5)))

class TestCircle(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(repr(Circle(0, 0, 10)), "Circle(0, 0, 10)")
        self.assertEqual(repr(Circle(-5, 5, 10)), "Circle(-5, 5, 10)")

    def test_cmp(self):
        self.assertTrue(Circle(0, 0, 10) == Circle(0, 0, 10))
        self.assertFalse(Circle(0, 0, 10) != Circle(0, 0, 10))
        self.assertTrue(Circle(-5, 5, 10) != Circle(0, 0, 10))
        self.assertFalse(Circle(-5, 5, 10) == Circle(0, 0, 10))

    def test_area(self):
        self.assertAlmostEqual(Circle(0, 0, 10).area(), 314, places=0)
        self.assertAlmostEqual(Circle(-5, 5, 5).area(), 78.54, places=2)

    def test_move(self):
        self.assertEqual(Circle(0, 0, 10).move(5, 5), Circle(5, 5, 10))
        self.assertEqual(Circle(-5, -5, 10).move(5, -5), Circle(0, -10, 10))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 10).cover(Circle(0, 0, 5)), Circle(0, 0, 10))
        self.assertEqual(Circle(-5, -5, 10).cover(Circle(-5, 5, 10)), Circle(0, 5, 15))


if __name__ == '__main__':
    unittest.main()
