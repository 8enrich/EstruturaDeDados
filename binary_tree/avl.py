from binary_tree import BinTree

class Avl(BinTree):

    def __init__(self, root=None):
        super(Avl, self).__init__(root)

    def __find_deepest_disbalanced(self, node):
        if self.__is_disbalanced(node.left):
            node.left = self.__find_deepest_disbalanced(node.left)
            return node
        if self.__is_disbalanced(node.right):
            node.right = self.__find_deepest_disbalanced(node.right)
            return node
        return self.__do_rotate(node) 

    def __do_rotate(self, z):
        y = self.__find_highest_son(z)
        x = self.__find_highest_son(y)
        if((z.left == y and y.left == x) or (z.right == y and y.right == x)):
            return self.__single_rotation(x, y, z)
        return self.__double_rotation(x, y, z)

    def __find_highest_son(self, node):
        if not node:
            return node 
        r_height, l_height = self.__get_heights(node) 
        return node.left if l_height > r_height else node.right

    def __left_left(self, x, y, z):
        t3 = y.right
        y.left, y.right = x, z
        z.left = t3 
        return y

    def __right_right(self, x, y, z):
        t2 = y.left
        y.left, y.right = z, x
        z.right = t2 
        return y

    def __left_right(self, x, y, z):
        t2, t3 = x.left, x.right
        x.left, x.right = y, z
        y.right = t2
        z.left = t3
        return x

    def __right_left(self, x, y, z):
        t2, t3 = x.left, x.right
        x.left, x.right = z, y
        z.right = t2
        y.left = t3
        return x

    def __single_rotation(self, x, y, z):
        if z.left == y:
            return self.__left_left(x, y, z)
        return self.__right_right(x, y, z)

    def __double_rotation(self, x, y, z):
        if z.left == y:
            return self.__left_right(x, y, z)
        return self.__right_left(x, y, z)

    def __rotate(self):
        self.root = self.__find_deepest_disbalanced(self.root)

    def insert(self, value):
        super().insert(value)
        if self.__is_disbalanced(self.root):
            self.__rotate() 

    def remove(self, value):
        super().remove(value)
        while self.__is_disbalanced(self.root):
            self.__rotate()
            
    def __get_heights(self, node):
        r_height = node.right.get_height() if node.right else 0
        l_height = node.left.get_height() if node.left else 0
        return r_height, l_height

    def __is_disbalanced(self, node):
        if not node:
            return 0 
        r_height, l_height = self.__get_heights(node)
        if abs(r_height - l_height) > 1:
            return r_height - l_height
        return self.__is_disbalanced(node.left) + self.__is_disbalanced(node.right)

    def is_desbalanced(self):
        return self.__is_disbalanced(self.root)
