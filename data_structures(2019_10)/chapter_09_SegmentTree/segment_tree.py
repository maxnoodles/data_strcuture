class SegmentTree:

    def __init__(self, arr, merger):
        """
        线段树相当于将数组用一颗树重新表示
        """
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        self.build_segment_tree(0, 0, len(self._data)-1)


    # 在 treeIndex 的位置创建表示区间 [l...r] 的线段树
    def build_segment_tree(self, tree_index, l, r):
        if l == r:
            self._tree[tree_index] = self._data[l]
            return

        l_index = self._left_child(tree_index)
        r_index = self._right_child(tree_index)
        mid = l + (r - l) // 2

        self.build_segment_tree(l_index, l, mid)
        self.build_segment_tree(r_index, mid+1, r)

        self._tree[tree_index] = self._merger(self._tree[l_index], self._tree[r_index])

    def query(self, query_l, query_r):
        if query_l < 0 or query_l >= len(self._data) or \
            query_r < 0 or query_r >= len(self._data) or \
            query_l > query_r:
            raise ValueError('Index is illegal.')
        return self._query(0, 0, len(self._data)-1, query_l, query_r)

    # 在以tree_index为根的线段树中的(线段树本身)[l...r]的范围里，搜索区间(用户指定的)[query_l...query_r]的值
    def _query(self, tree_index, l, r, query_l, query_r):
        if query_l == l and query_r == r:
            return self._tree[tree_index]

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        mid = l + (r - l) // 2

        if query_l >= mid + 1:
            return self._query(right_tree_index, mid+1, r, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_tree_index, l, mid, query_l, query_r)

        left_result = self._query(left_tree_index, l, mid, query_l, mid)
        right_result = self._query(right_tree_index, mid+1, r, mid+1, query_r)

        return self._merger(left_result, right_result)

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

    def __str__(self):
        return str(self._tree)


if __name__ == "__main__":
    nums = [i for i in range(10)]
    segment_tree = SegmentTree(arr=nums, merger=lambda a, b:a+b)
    print(segment_tree)
    query_result = segment_tree.query(3, 8)
    print(query_result)

