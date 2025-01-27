from heap import Heap

class MinHeap(Heap):

    def __init__(self):
        super(MinHeap, self).__init__()

    def __heapfy(self, index):
        father = self.father(index)
        if father is None:
            return
        if self[father] > self[index]:
            self.__change_nodes(index, father)
            self.__heapfy(father)

    def add(self, value):
        super().add(value)
        self.__heapfy(len(self) - 1)

    def __heapfy_down(self, index):
        left_index = self.left(index)
        if left_index and self[left_index] < self[index]:
            self.__change_nodes(index, left_index)
            self.__heapfy_down(left_index)
        right_index = self.right(index)
        if right_index and self[right_index] < self[index]:
            self.__change_nodes(index, right_index)
            self.__heapfy_down(right_index)

    def remove(self):
        index = self.rightest_node(0)
        value = self[index]
        root = self[0]
        self._list.pop(index)
        if len(self) > 0:
            self[0] = value
            self.__heapfy_down(0)
        return root
