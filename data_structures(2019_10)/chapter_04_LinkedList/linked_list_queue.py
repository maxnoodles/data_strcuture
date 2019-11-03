# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Date: 2019-11-02


class LinkedListQueue:

    class _Node:

        def __init__(self, data=None, node_next=None):
            self.data = data
            self.next = node_next

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, v):
        if self.tail is None:
            self.tail = self._Node(v)
            self.head = self.tail
        else:
            self.tail.next = self._Node(v)
            self.tail = self.tail.next
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Can not dequeue from a empty queue')
        ret_node = self.head
        self.head = self.head.next
        ret_node.next = None
        if self.head is None:
            self.tail = None
        self._size -= 1
        return ret_node.data

    def get_front(self):
        if self.is_empty():
            raise ValueError('queue is empty')
        return self.head.data

    def __str__(self):
        linked_str = 'Queue:front '
        cur = self.head

        while cur:
            linked_str += f'{cur.data} -> '
            cur = cur.next
        linked_str += ' None tail'
        return linked_str


if __name__ == '__main__':
    queue = LinkedListQueue()
    for i in range(5):
        queue.enqueue(i)
    print(queue)
    ret = queue.dequeue()
    print(queue)
    print(queue.get_front())


