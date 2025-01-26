from heap import Heap

class MaxHeap(Heap):

    def __init__(self):
        super(MaxHeap, self).__init__()

    def __change_nodes(self, index1, index2):
        value = self._list[index1]
        self._list[index2], self._list[index1] = value, self._list[index2]
        return self._list.index(value)

    def __heapfy(self, index):
        father = self.father(index)
        if father is None:
            return
        if self._list[father] < self._list[index]:
            new_index = self.__change_nodes(index, father)
            self.__heapfy(new_index)

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

    def __heapify_down(self, index):
        left_index = self.left(index)
        if left_index and self._list[left_index] > self._list[index]:
            new_index = self.__change_nodes(index, left_index)
            self.__heapify_down(new_index)
        right_index = self.right(index)
        if right_index and self._list[right_index] > self._list[index]:
            new_index = self.__change_nodes(index, right_index)
            self.__heapify_down(new_index)

    def remove(self):
        index = self.rightest_node(0)
        value = self._list[index]
        root = self._list[0]
        del self._list[index]
        if len(self) > 0:
            self._list[0] = value
            self.__heapify_down(0)
        return root
