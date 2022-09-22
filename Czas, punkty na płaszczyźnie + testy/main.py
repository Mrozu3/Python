#Zestaw 6 Mróz Kamil
from times import *
from points import *
import unittest

class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(3723)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.t1), "01:02:03")
        self.assertEqual(repr(self.t1), "Time(3723)")
        self.assertEqual(str(Time(723)), "00:12:03")
        self.assertEqual(repr(Time(723)), "Time(723)")


    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(723) + self.t1, Time(4446))
        self.assertEqual(self.t1 + Time(0), self.t1)

    def test_int(self):
        self.assertEqual(int(self.t1), 3723)
        self.assertEqual(int(Time(723)), 723)

    def tearDown(self): pass

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, -2)), "(1, -2)")
        self.assertEqual(repr(Point(1, -2)), "Point(1, -2)")
        self.assertEqual(str(Point(7.23, 37.23)), "(7.23, 37.23)")
        self.assertEqual(repr(Point(7.23, 37.23)), "Point(7.23, 37.23)")

    def test_cmp(self):
        self.assertTrue(Point(1, -2) == Point(1, -2))
        self.assertFalse(Point(1, -2) == Point(1, 2))
        self.assertTrue(Point(1, -2) != Point(1, 2))
        self.assertFalse(Point(1, -2) != Point(1, -2))

    def test_add(self):
        self.assertEqual(Point(1, -2) + Point(1, 2), Point(2, 0))
        self.assertEqual(Point(1, -2) + Point(7.23, 37.23), Point(8.23, 35.23))

    def test_sub(self):
        self.assertEqual(Point(1, -2) - Point(1, 2), Point(0, -4))
        self.assertEqual(Point(7.23, 37.23) - Point(1, 2), Point(6.23, 35.23))

    def test_mul(self):
        self.assertEqual(Point(1, -2) * Point(1, 2), -3)
        self.assertEqual(Point(1, 0) * Point(0, -2), 0)

    def test_cross(self):
        self.assertEqual(Point(1, -2).cross(Point(1, 2)), 4)
        self.assertEqual(Point(1, 0).cross(Point(0, -2)), -2)

    def test_length(self):
        self.assertEqual(Point(1, -2).length(), 5 ** (1/2))
        self.assertEqual(Point(1, 0).length(), 1)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy