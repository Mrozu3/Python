# Zestaw 12 Mróz Kamil
from search import *
import unittest


class TestSearch(unittest.TestCase):

    def setUp(self): pass

    def test_binarne_rek(self):
        L = [5, 10, 100, 500, 1000, 1800, 2130]
        maxsize = len(L) - 1
        self.assertEqual(binarne_rek(L, 0, maxsize, 5), 0)
        self.assertEqual(binarne_rek(L, 1, 4, 500), 3)
        self.assertEqual(binarne_rek(L, 3, maxsize, 2130), 6)
        self.assertEqual(binarne_rek(L, 0, maxsize, 5000), None)

    def test_lider_py(self):
        L = [10, 20, 30, 40, 50, 50, 70, 80, 90, 100]
        maxsize = len(L) - 1
        self.assertEqual(lider_py(L, 0, maxsize), None)
        self.assertEqual(lider_py(L, 2, 6), None)
        self.assertEqual(lider_py(L, 3, 6), 50)

        L = [10, 20, 20, 40, 20, 20, 70, 20, 90, 100]
        maxsize = len(L) - 1
        self.assertEqual(lider_py(L, 0, maxsize), 20)
        self.assertEqual(lider_py(L, 0, 3), 20)
        self.assertEqual(lider_py(L, 7, 9), None)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
