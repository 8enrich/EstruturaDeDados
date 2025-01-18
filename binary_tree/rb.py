from binary_tree import BinTree
from rb_node import RbNode

class RedBlack(BinTree):

    RESET = "\033[0m"
    RED = "\033[31m"
    BLACK = "\033[90m"

    def __init__(self, root=None):
        super(RedBlack, self).__init__(root)

    def __insert_new_node(self, node, new_node):
        new_node.father = node
        if node.data > new_node.data:
            node.left = new_node
            return
        node.right = new_node

    def __insert(self, node, new_node):
        if not node:
            return new_node
        if node.data > new_node.data:
            left_node = self.__insert(node.left, new_node)
            self.__insert_new_node(node, left_node)
        if node.data < new_node.data:
            right_node = self.__insert(node.right, new_node)
            self.__insert_new_node(node, right_node)
        return node

    def insert(self, value):
        new_node = RbNode(value)
        self.root = self.__insert(self.root, new_node)
        self.__insert_case_1(new_node)

    def __insert_case_1(self, node):
        if node.father is None:
            node.color = node.BLACK
            return
        self.__insert_case_2(node)

    def __insert_case_2(self, node):
        if node.father.color == node.BLACK:
            return
        self.__insert_case_3(node)

    def __insert_case_3(self, node):
        u = node.get_uncle()
        if u and u.color == node.RED:
            g = node.get_grandfather()
            self.__change_colors(node.father, u, g)
            return self.__insert_case_1(g)
        self.__insert_case_4(node)

    def __insert_case_4(self, node):
        g = node.get_grandfather()
        f = node.father
        if((g.left == f and f.left == node) or (g.right == f and f.right == node)):
            self.__simple_rotation(node, f, g)
            self.__change_colors(f, g)
            return self.__insert_case_2(node)
        self.__double_rotation(node, f, g)
        self.__change_colors(g, node)
        return self.__insert_case_2(node)

    def __simple_rotation(self, x, y, z):
        if z.left == y:
            return self.__left_left(x, y, z)
        self.__right_right(x, y, z)

    def __double_rotation(self, x, y, z):
        if z.left == y:
            return self.__left_right(x, y, z)
        self.__right_left(x, y, z)

    def __left_left(self, x, y, z):
        t3 = y.right
        gg = z.father
        self.__insert_new_node(y, x)
        self.__insert_new_node(y, z)
        z.left = self.__insert_sub_tree(t3, z)
        self.__change_grandgrandfather(gg, y)

    def __right_right(self, x, y, z):
        t2 = y.left
        gg = z.father
        self.__insert_new_node(y, z)
        self.__insert_new_node(y, x)
        z.right = self.__insert_sub_tree(t2, z)
        self.__change_grandgrandfather(gg, y)

    def __left_right(self, x, y, z):
        t2, t3 = x.left, x.right
        gg = z.father
        self.__insert_new_node(x, y)
        self.__insert_new_node(x, z)
        y.right = self.__insert_sub_tree(t2, y)
        z.left = self.__insert_sub_tree(t3, z)
        self.__change_grandgrandfather(gg, x)

    def __right_left(self, x, y, z):
        t2, t3 = x.left, x.right
        gg = z.father
        self.__insert_new_node(x, z)
        self.__insert_new_node(x, y)
        z.right = self.__insert_sub_tree(t2, z)
        y.left = self.__insert_sub_tree(t3, y)
        self.__change_grandgrandfather(gg, x)

    def __insert_sub_tree(self, sub_tree, node):
        if sub_tree:
            sub_tree.father = node
        return sub_tree

    def __change_grandgrandfather(self, gg, y):
        if not gg:
            self.root = y
            y.father = None
            return
        self.__insert_new_node(gg, y)
        
    def __change_colors(self, *args):
        for node in args:
            self.__change_color(node)

    def __change_color(self, node):
        node.color = 1 - node.color

    def __repr(self, node):
        if not node:
            return ""
        color = self.RED if node.color == node.RED else self.BLACK
        string = color + str(node.data) + self.RESET
        left = self.__repr(node.left)
        right = self.__repr(node.right)
        string += "\n├── "
        for i in right.splitlines():
            string += i + "\n│   "
        string += "\n└── "
        for i in left.splitlines():
            string += i + "\n    "
        return string 

    def __repr__(self):
        return self.__repr(self.root).strip()
