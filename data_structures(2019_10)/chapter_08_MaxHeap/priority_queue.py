from chapter_03_Stack_Queue.queue import LoopQueue
from chapter_08_MaxHeap.max_heap import MaxHeap


class PriorityQueue:

    def __init__(self):
        self._max_heap = MaxHeap()

    def get_size(self):
        return self._max_heap.size

    def is_empty(self):
        return self._max_heap.is_empty()

    def get_front(self):
        return self._max_heap.find_max()

    def enqueue(self, v):
        self._max_heap.add(v)

    def dequeue(self):
        return self._max_heap.extract_max()