
class Heap:

    def __init__(self):
        self._list = []

    def left(self, index):
        left = 2 * index + 1
        return left if left < len(self) else None

    def right(self, index):
        right = 2 * index + 2
        return right if right < len(self) else None

    def father(self, index):
        father = (index + 1)//2 - 1
        return father if father >= 0 else None

    def add(self, value):
        self._list.append(value)

    def remove(self):
        return self._list.pop(0)

    def __len__(self):
        return len(self._list)

    def _height(self, index):
        if index is None:
            return 0
        return 1 + max(self._height(self.left(index)), self._height(self.right(index)))

    def height(self):
        return self._height(0)

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError
        return self._list[index]

    def __setitem__(self, index, value):
        if index > len(self):
            raise IndexError
        self._list[index] = value

    def __repr(self, index):
        if index is None:
            return ""
        string = str(self._list[index])
        left = self.__repr(self.left(index))
        right = self.__repr(self.right(index))
        string += "\n├── "
        for i in right.splitlines():
            string += i + "\n│   "
        string += "\n└── "
        for i in left.splitlines():
            string += i + "\n    "
        return string 

    def __repr__(self):
        if len(self) > 0:
            return self.__repr(0).strip()
        return ""
