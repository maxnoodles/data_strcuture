

class LinkedList:

    class _Node:

        def __init__(self, value=None, node_next=None):
            self.value = value
            self.next = node_next

        def __str__(self):
            return str(self.next)

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, index, value):
        if not 0 < index <= self._size:
            raise ValueError('Add failed. Illegal index')

        prev = self._dummy_head
        for i in range(index-1):
            prev = prev.next
        prev.next = self._Node(value, prev.next)
        self._size += 1

    def add_first(self, value):
        self.add(0, value)

    def add_last(self, value):
        self.add(self._size, value)


