from binary_tree import BinTree

class Avl(BinTree):

    def __init__(self, root=None):
        super(Avl, self).__init__(root)

    def __find_first_disbalanced(self):
        node = self.root
        side = 1
        while side != 0:
            side = self.__is_disbalanced(node)
            if side > 0:
                node = node.right
            if side < 0:
                node = node.left
        return node.father

    def __simple_rotation(self, desbalanced):
        y = self.__find_first_disbalanced() 
        z = y.father
        x = y.right
        if desbalanced > 0:
            if not z:
                self.root = x 
                x.father = None
                y.right, y.left = x.left, y.left 
                x.left = y 
                y.father = self.root
                return
            z.right, x.father = x, z 
            y.right, y.left = x.left, y.left 
            x.left = y 
            y.father = x 

    def __rotate(self, desbalanced):
        self.__simple_rotation(desbalanced)

    def insert(self, value):
        super().insert(value)
        desbalanced = self.is_disbalanced()
        if desbalanced:
            self.__rotate(desbalanced) 

    def __is_disbalanced(self, node):
        if not node:
            return 0 
        r_height = node.right.get_height() if node.right else 0
        r_left = node.left.get_height() if node.left else 0
        if abs(r_height - r_left) > 1:
            return r_height - r_left 
        return self.__is_disbalanced(node.left) + self.__is_disbalanced(node.right)

    def is_disbalanced(self):
        return self.__is_disbalanced(self.root)
