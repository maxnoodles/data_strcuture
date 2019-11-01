

class LinkedList:

    class _Node:

        def __init__(self, value=None, node_next=None):
            self.value = value
            self.next = node_next

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, index, value):
        if not 0 <= index <= self._size:
            raise ValueError('Add failed. Illegal index')

        prev = self._dummy_head
        for i in range(index):
            prev = prev.next
        prev.next = self._Node(value, prev.next)
        self._size += 1

    def add_first(self, value):
        self.add(0, value)

    def add_last(self, value):
        self.add(self._size, value)

    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('Require 0 <= index < size')
        cur = self._dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.value

    def get_first(self):
        return self.get(0)

    def set(self, index, value):
        if not 0 <= index < self._size:
            raise ValueError('Require 0 <= index < size')
        cur = self._dummy_head.next
        for i in range(index):
            cur = cur.next
        cur.value = value

    def contains(self, value):
        cur = self._dummy_head
        while cur.next:
            if value == cur.value:
                return True
            cur = cur.next

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('Require 0 <= index < size')

        prev = self._dummy_head
        for i in range(index):
            prev = prev.next

        ret_node = prev.next
        prev.next = ret_node.next
        ret_node.next = None
        self._size -= 1
        return ret_node

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def __str__(self):
        linked_str = ''
        cur = self._dummy_head.next
        while cur:
            linked_str += f'{cur.value} -> '
            cur = cur.next
        linked_str += 'Null'
        return linked_str


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(5):
        linked_list.add_first(i)
        print(linked_list)
    linked_list.add(2, 555)
    print(linked_list)
    linked_list.remove(2)
    print(linked_list)
    linked_list.remove_first()
    print(linked_list)
    linked_list.remove_last()
    print(linked_list)


