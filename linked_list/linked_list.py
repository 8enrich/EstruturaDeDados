from node import Node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0 if not head else self.count_nodes(head)

    def count_nodes(self, node):
        count = 0
        while(node):
            count += 1
            node = node.next
        return count

    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next

    def check_index_int(self, index):
        if not isinstance(index, int):
            raise ValueError("Index deve ser do tipo inteiro.")

    def check_index(self, index):
        self.check_index_int(index)

        if index >= self.size or index < 0:
            raise IndexError("Index não pode ser maior que a lista e nem menor que 0.")

    def insert(self, index, element):

        self.check_index_int(index)

        if index > self.size or index < 0:
            raise IndexError("Index não pode ser maior que a lista e nem menor que 0.")
      
        if not isinstance(element, Node):
            element = Node(element)
        
        self.size += 1

        if index == 0:
            self.head, element.next = element, self.head
            return

        for i, node in enumerate(self):
            if i == index - 1:
                element.next, node.next = node.next, element

    def append(self, element):
        self.insert(self.size, element)

    def push(self, element):
        self.insert(0, element)

    def remove(self, index):
        self.check_index(index)

        self.size -= 1

        if index == 0:
            head = self.head
            self.head = self.head.next if self.head else None
            return head
            
        for i, node in enumerate(self):
            if i == index - 1:
                node_to_remove = node.next
                node.next = node.next.next
                return node_to_remove

    def pop(self):
        try:
            return self.remove(self.size - 1)
        except IndexError:
            raise Exception("Não há elementos na lista.")

    def remove_head(self):
        try:
            return self.remove(0)
        except IndexError:
            raise Exception("Não há elementos na lista.")
       
    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self.head = None
                   
    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.slice(index)

        self.check_index(index)

        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index, element):
        self.check_index(index)

        for i, node in enumerate(self):
            if i == index:
                node.data = element

    def slice(self, indexes): 
        new_ll = LinkedList()

        begin = indexes.start if indexes.start else 0
        end = indexes.stop if indexes.stop else self.size - 1
        store = False
        step = indexes.step if indexes.step else 1
        count = None

        self.check_index(begin)
        self.check_index(end)
        if step <= 0:
            raise IndexError("Step não pode ser menor que 0.")

        for i, node in enumerate(self):
            if store and count is not None:
                count += 1
            if count is not None and count % step == 0:
                new_ll.append(Node(node.data))
            if i == begin:
                new_ll.append(Node(node.data))
                store = True
                count = 0
            if i == end:
                return new_ll

    def __repr__(self):
        string = ""
        for i, node in enumerate(self):
            string += str(node)
            if i < self.size - 1:
                string += "->"
        return string 
