# Zestaw 9 Mróz Kamil
from singlelist import *
from seartchtree import *
import unittest


class TestLists(unittest.TestCase):

    def setUp(self): pass

    def test_remove_tail(self):
        alist = SingleList()
        alist.insert_head(Node(10))
        alist.insert_head(Node(5))
        alist.insert_tail(Node(20))
        alist.insert_tail(Node(30))
        alist.remove_tail()
        self.assertEqual(alist.tail, Node(20))
        self.assertEqual(alist.length, 3)

    def test_join(self):
        selflist = SingleList()
        selflist.insert_head(Node(10))
        selflist.insert_head(Node(5))
        selflist.insert_tail(Node(20))
        selflist.insert_tail(Node(30))

        otherlist = SingleList()
        otherlist.insert_head(Node(50))
        otherlist.insert_head(Node(40))
        otherlist.insert_tail(Node(60))
        otherlist.insert_tail(Node(70))

        selflist.join(otherlist)

        self.assertEqual(selflist.tail, Node(70))
        self.assertEqual(selflist.length, 8)
        self.assertTrue(otherlist.is_empty())

    def test_clear(self):
        alist = SingleList()
        alist.insert_head(Node(5))
        alist.insert_head(Node(10))
        alist.insert_tail(Node(20))
        alist.insert_tail(Node(30))
        alist.clear()
        self.assertTrue(alist.is_empty())

    def tearDown(self): pass


class TestTrees(unittest.TestCase):

    def setUp(self): pass

    def test_bst_max(self):
        root = Node(10)
        root.insert(Node(5))
        root.insert(Node(10))
        root.insert(Node(15))
        root.insert(Node(20))
        root.insert(Node(30))
        root.insert(Node(25))
        root.insert(Node(0))

        self.assertEqual(root.bst_max(), Node(30))

    def test_bst_min(self):
        root = Node(10)
        root.insert(Node(5))
        root.insert(Node(10))
        root.insert(Node(15))
        root.insert(Node(20))
        root.insert(Node(30))
        root.insert(Node(25))
        root.insert(Node(0))

        self.assertEqual(root.bst_min(), Node(0))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
