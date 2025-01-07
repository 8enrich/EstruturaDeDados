from node import Node

class BinTree:

    def __init__(self, root=None):
        self.root = root
        self.size = 1 if root else 0

    def __search(self, node, value):
        if node is None or node.data == value:
            return node
        if node.data > value:
            return self.__search(node.left, value)
        return self.__search(node.right, value)

    def search(self, value):
        return self.__search(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return
        if node.data > value:
            if node.left is None:
                node.left = Node(value)
                return
            self.__insert(node.left, value)
        if node.data < value:
            if node.right is None:
                node.right = Node(value)
                return
            self.__insert(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self.__insert(self.root, value)

    def __next(self, node):
        if node is None or node.left is None:
            return node
        return self.__next(node.left)

    def next(self, value): 
        node = self.search(value)
        return None if not node else self.__next(node.right)

    def remove(self, value): 
        node = self.search(value)
        if not node:
            return
        next = self.next(value)
        if next:
            before = self.before(next.data)
            self.remove_next(before, next)
            node.data = next.data
            return
        before = self.before(node.data)
        self.remove_next(before, node)

    def remove_next(self, node, next):
        if node is None:
            return
        if node.right:
            node.right = next.right if node.right.data == next.data else node.right
            return
        node.left = next.left if node.left.data == next.data else node.left

    def __before(self, node, value):
        if node is None:
            return 
        if node.right:
            if node.right.data == value:
                return node
            if node.data < value:
                return self.__before(node.right, value)
        if node.left:
            if node.left.data == value:
                return node
            if node.data > value:
                return self.__before(node.left, value)

    def before(self, value):
        return self.__before(self.root, value)

    def __repr(self, node, level):
        string = ""
        if node:
            string += str(node)
            string += "\n" + "|  " * level + "|- " + self.__repr(node.left, level + 1)
            if node.right:
                string += "\n" + "|  " * level + "|"
            string += "\n" + "|  " * level + "|- " +self.__repr(node.right, level + 1)
        return string 

    def __repr__(self):
        return self.__repr(self.root, 0)
