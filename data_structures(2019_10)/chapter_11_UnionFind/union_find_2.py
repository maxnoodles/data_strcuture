import random


class UnionFind2:
    def __init__(self, size: int):
        self.parent = []
        self.rank = []
        for i in range(size):
            self.parent.append(i)
            self.rank.append(1)

    def get_size(self):
        return len(self.parent)

    def _find(self, p):
        if not 0 <= p < len(self.parent):
            raise ValueError('p is out of bound')
        # while p != self.parent[p]:
        #     self.parent[p] = self.parent[self.parent[p]]
        #     p = self.parent[p]
        if p != self.parent[p]:
            self.parent[p] = self._find(self.parent[p])
        return self.parent[p]

    def union_elements(self, p, q):
        p_parent = self._find(p)
        q_parent = self._find(q)

        if p_parent == q_parent:
            return
        if self.rank[p_parent] < self.rank[q_parent]:
            self.parent[p_parent] = self.parent[q_parent]
        elif self.rank[p_parent] > self.rank[q_parent]:
            self.parent[q_parent] = self.parent[p_parent]
        else:
            self.parent[q_parent] = self.parent[p_parent]
            self.rank[p_parent] += 1


    def is_connected(self, p, q):
        return self._find(p) == self._find(q)


if __name__ == '__main__':
    size = 100000
    union_find = UnionFind2(size)
    p = random.randint(0, size-1)
    q = random.randint(0, size-1)
    print(union_find.is_connected(p, q))
    union_find.union_elements(p, q)
    print(union_find.is_connected(p, q))

