from node import Node

class RbNode(Node):

    RED = 0
    BLACK = 1

    def __init__(self, data=None, color=RED):
        super(RbNode, self).__init__(data)
        self.color = color # 0 representa vermelho e 1 representa preto
        self.father = None

    def get_grandfather(self):
        if not self.father:
            return None
        return self.father.father

    def get_uncle(self):
        grandfather = self.get_grandfather()
        if not grandfather:
            return None
        return grandfather.right if self.father == grandfather.left else grandfather.left
