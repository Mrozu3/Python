# Zestaw 10 Mróz Kamil
from stack import *
from queue import *
from randomqueue import *
import unittest


class TestStacks(unittest.TestCase):

    def setUp(self): pass

    def test_push_full(self):
        astack = Stack()
        for item in ["a", 2, 3.5]:
            astack.push(item)
        self.assertEqual(str(astack), "['a', 2, 3.5]")
        self.assertTrue(astack.is_full())

    def test_pop_empty(self):
        astack = Stack()
        for item in ["a", 2, 3.5]:
            astack.push(item)
        self.assertEqual(astack.pop(), 3.5)
        self.assertEqual(astack.pop(), 2)
        self.assertEqual(astack.pop(), 'a')
        self.assertTrue(astack.is_empty())

    def tearDown(self): pass


class TestQueue(unittest.TestCase):

    def setUp(self): pass

    def test_cmp(self):
        pq = PriorityQueue(cmp)
        for item in [5, 3, 8]:
            pq.insert(item)
        pq.remove()
        self.assertEqual(str(pq), "[5, 3]")

    def test_cmp2(self):
        pq = PriorityQueue(cmp2)
        for item in [5, 3, 8]:
            pq.insert(item)
        pq.remove()
        self.assertEqual(str(pq), "[5, 8]")

    def tearDown(self): pass


class TestRandomqueue(unittest.TestCase):

    def setUp(self): pass

    def test_all(self):
        rq = RandomQueue()
        for item in [1, 2, 3, 4, 5, 6, 7, 8]:
            rq.insert(item)
        self.assertFalse(rq.is_full())
        print("Usunięty losowy element:", rq.remove())
        print("Kolejka losowa: ", str(rq))
        rq.clear()
        self.assertTrue(rq.is_empty())

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
