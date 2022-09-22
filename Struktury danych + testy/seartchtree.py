class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def insert(self, node):
        if node.data < self.data:  # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:  # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def bst_max(self):
        if self is None:
            raise ValueError
        else:
            maxright = self
            while maxright.right is not None:
                maxright = maxright.right
            return maxright

    def bst_min(self):
        if self is None:
            raise ValueError
        else:
            minleft = self
            while minleft.left is not None:
                minleft = minleft.left
            return minleft
