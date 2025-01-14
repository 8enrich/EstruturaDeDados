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
            return
        if node.data > value:
            if node.left is None:
                node.left = Node(value)
                node.left.father = node
                return
            self.__insert(node.left, value)
        if node.data < value:
            if node.right is None:
                node.right = Node(value)
                node.right.father = node
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
            before = next.father 
            data = next.data
            self.remove(next.data)
            node.data = data
            return
        before = node.father 
        self.remove_next(before, node)

    def remove_next(self, node, next):
        if not node:
            self.__remove_root(next)
            return
        if node.data < next.data:
            if next.right:
                node.right = next.right
                return
            node.right = next.left
            return
        if next.right:
            node.left = next.right
            return
        node.left = next.left
        
    def __remove_root(self, next):
        if next.right:
            self.root = next.right
            return
        self.root = next.left

    def __get_height(self, node):
        if not node:
            return 0
        return node.get_height()

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
