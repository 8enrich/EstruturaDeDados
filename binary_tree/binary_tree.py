from node import Node

class BinTree:

    def __init__(self, root=None):
        self.root = root

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
            return Node(value)
        if node.data > value:
            node.left = self.__insert(node.left, value)
        if node.data < value:
            node.right = self.__insert(node.right, value)
        return node

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __next(self, node):
        if node is None or node.left is None:
            return node
        return self.__next(node.left)

    def next(self, value): 
        node = self.search(value)
        return None if not node else self.__next(node.right)

    def __remove(self, node, value):
        if node is None:
            return None 
        if node.data > value:
            node.left = self.__remove(node.left, value)
        if node.data < value:
            node.right = self.__remove(node.right, value)
        if node.data == value:
            if not node.left or not node.right:
                return node.left if node.left else node.right
            next = self.__next(node.right)
            self.__remove(node, next.data)
            next.left, next.right = node.left, node.right
            return next
        return node

    def remove(self, value): 
        self.root = self.__remove(self.root, value)

    def __get_height(self, node):
        return 0 if not node else node.get_height()

    def get_height(self):
        return self.__get_height(self.root)

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
