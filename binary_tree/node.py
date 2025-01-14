
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.father = None

    def __get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def get_height(self):
        return self.__get_height(self)

    def __repr__(self):
        return str(self.data)
