from heap import Heap

class MinHeap(Heap):

    def __init__(self):
        super(MinHeap, self).__init__()

    def __change_nodes(self, index1, index2):
        self[index2], self[index1] = self[index1], self[index2]

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

    def rightest_node(self, index):
        height_left = self._height(self.left(index))
        height_right = self._height(self.right(index))
        if height_left > height_right:
            return self.rightest_node(self.left(index))
        if height_right == 0:
            return index
        return self.rightest_node(self.right(index))

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
