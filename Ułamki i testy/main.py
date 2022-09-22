#ZESTAW 5 MRÓZ KAMIL
from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [-1, 2]  # -1/2
        self.f2 = [0, 1]  # zero
        self.f3 = [3, 1]  # 3
        self.f4 = [6, 2]  # 3 (niejednoznaczność)
        self.f5 = [0, 2]  # zero (niejednoznaczność)

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertFalse(is_positive(self.f1))
        self.assertTrue(is_positive(self.f3))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertTrue(is_zero(self.f2))
        self.assertTrue(is_zero(self.f5))
        self.assertFalse(is_zero(self.f4))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f5), -1)
        self.assertEqual(cmp_frac(self.f3, self.f4), 0)
        self.assertEqual(cmp_frac(self.f3, self.f1), 1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.f1), (-0.5), places=2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy