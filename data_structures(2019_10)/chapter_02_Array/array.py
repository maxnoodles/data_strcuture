class MyArray:

    def __init__(self, arr=None, capacity=10):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
        else:
            self._data = [None] * capacity
            self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('Require 0 <= index < array size')
        return self._data[index]

    def get_last(self):
        return self.get(self._size-1)

    def get_first(self):
        return self.get(0)

    def set(self, index, value):
        if not 0 <= index < self._size:
            raise ValueError('Require 0 <= index < array size')
        self._data[index] = value

    def add(self, index, value):
        """线型表插入索引后的元素都要后移一位"""
        if not 0 <= index <= self._size:
            raise ValueError('add failed. Require 0 <= index <= array size')

        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        for i in range(self._size-1, index-1, -1):
            self._data[i+1] = self._data[i]
        self._data[index] = value
        self._size += 1

    def add_last(self, value):
        self.add(self._size, value)

    def add_first(self, value):
        self.add(0, value)

    def find_index(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def contains(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return True
        return False

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Require 0 < index < array size')

        ret = self._data[index]
        for i in range(index, self._size):
            self._data[i] = self._data[i + 1]
        self._size -= 1

        # 因为 // 是向下取整的，如果 size 为 1, 1 // 4 等于 0，不能将 capacity 缩融为 0，这样无法增长。
        if self._size == len(self._data) // 4 and self._size // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, value):
        index = self.find_index(value)
        if index != -1:
            self.remove(index)
            return True
        return False

    def _resize(self, capacity):
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def __str__(self):
        return str(f'Array: size = {self._size}, capcatiy = {len(self._data)}, {self._data}')

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    arr = MyArray()

    for i in range(10):
        arr.add_last(i)
    print(arr.get_capacity())
    arr.add_last('zhe')
    # arr.add_last('wang')
    # arr.add_last('zwang')

    arr.add(1, 'zwang')
    print(arr)

    arr.remove_element('zwang')
    print(arr)

    arr.add_first(-1)
    print(arr)

    arr.remove_element(8)
    print(arr)

    arr.remove_last()
    print(arr)