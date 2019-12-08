class SegmentTree:

    def __init__(self, arr):
        """
        线段树相当于将数组用一颗树重新表示
        """
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)

    def get_size(self):
        return len(self._data)

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def get(self, index):
        if index < 0 or index >= self.get_size():
            raise ValueError('Index is illegal')
        return self._data[index]


