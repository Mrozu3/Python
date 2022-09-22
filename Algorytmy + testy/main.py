import unittest
from algorithms import *


class TestClass(unittest.TestCase):

    def setUp(self): pass

    def test_P(self):
        self.assertEqual(recursion(3, 4), 0.65625)
        self.assertEqual(iteration(3, 4), 0.65625)


if __name__ == '__main__':
    unittest.main()