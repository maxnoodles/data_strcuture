

class Union_Find:

    def __init__(self, size):
        self._id = [i for i in range(len(size))]

    # 合并元素 p 和元素 q 所属的集合
    def union_elements(self, p, q):
        pid = self._find(p)
        qid = self._find(q)

        if pid == qid:
            return
        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid

    # 查找元素 p 所对应的集合
    def _find(self, p):
        if not 0 <= p <= len(self._id):
            raise ValueError('p is out of bound')
        return self._id[p]

    # 查看元素 p 和元素 q 是否所属同一个集合
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def get_size(self):
        return len(self._id)