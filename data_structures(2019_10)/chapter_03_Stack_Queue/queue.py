class LoopQueue:

    def __init__(self, capacity=8):
        """循环队列要空出一个位置"""
        self._data = [None] * (capacity + 1)
        self._front = 0
        self._tail = 0
        self._size = 0

    def get_capacity(self):
        return len(self._data) - 1

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    def enqueue(self, e):
        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_capacity() * 2)
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Can not dequeue from an empty queue.')
        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)

    def get_front(self):
        if self.is_empty():
            raise ValueError('Can not get_front from an empty queue.')
        return self._data[self._front]

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            # 将旧队列的元素迁移到新队列，并从0开始
            new_data[i] = self._data[(i + self._front) % len(self._data)]
        self._data = new_data
        self._front = 0
        self._tail = self._size

    def __str__(self):
        if self._tail >= self._front:
            return str('<chapter_03_Stack_Queue.queue.LoopQueue> : front {} tail, capacity: {}'.format(self._data[self._front:self._tail], self.get_capacity()))
        else:
            # presentation purpose only
            return str('<chapter_03_Stack_Queue.queue.LoopQueue> : front {} tail, capacity: {}'.format(str(self._data[self._front:] + self._data[:self._tail]), self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    queue = LoopQueue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(0)
    queue.enqueue(10)
    queue.enqueue(10)
    queue.enqueue(10)
    queue.enqueue(10)
    print(queue)

    queue.dequeue()
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
