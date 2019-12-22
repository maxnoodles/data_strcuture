

class MapSum():

    class _Node:
        def __init__(self, value=0, _next=None):
            self.value = value
            self.next = _next or dict()

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, word, val):
        cur = self._root
        for i in word:
            if not cur.next.get(i):
                cur.next[i] = self._Node()
            cur = cur.next[i]
        cur.value = val
        self._size += 1

    def sum(self, prefix):
        cur = self._root
        for i in prefix:
            if not cur.next.get(i):
                return 0
            cur = cur.next[i]
        return self._sum(cur)

    def _sum(self, node):
        res = node.value
        for i in node.next:
            res += self._sum(node.next[i])
        return res


if __name__ == '__main__':
    map_sum = MapSum()
    map_sum.add('ab', 1)
    map_sum.add('abc', 2)
    map_sum.add('abcd', 3)

    print(map_sum.sum('abc'))
