

class HashTable:
    upper_tolerance = 10
    lower_tolerance = 2
    init_capacity = 7

    def __init__(self, m=init_capacity):
        self._M = m
        self._hashtable = [dict() for _ in range(m)]
        self._size = 0

    def _hash(self, key):
        # 0x7fffffff 16进制 f 表示 1111 ,7个f 表示28个1，7 表示 3个 1
        # 一个大整数与上 31 个 1，抹除了最高位的符号位，表示取这个数的绝对值
        return hash(key) % 0x7fffffff % self._M

    def get_size(self):
        return self._size

    def add(self, key, value):
        _map = self._hashtable[self._hash(key)]
        if key in _map:
            _map[key] = value
        else:
            _map[key] = value
            self._size += 1
            if self._size >= self.upper_tolerance * self._M:
                self._resize(2 * self._M)

    def remove(self, key):
        ret = None
        _map = self._hashtable[self._hash(key)]
        if key in _map:
            ret = _map.pop(key)
            self._size -= 1
            if self._size < self.lower_tolerance * self._M and self._M // 2 >= self.init_capacity:
                self._resize(self._M // 2)
        return ret

    def __setitem__(self, key, value):
        _map = self._hashtable[self._hash(key)]
        if key not in _map:
            raise ValueError('{} doesn\'t exist!'.format(key))
        _map[key] = value

    def __getitem__(self, key):
        _map = self._hashtable[self._hash(key)]
        if key not in _map:
            raise ValueError('{} doesn\'t exist!'.format(key))
        return _map[key]

    def _resize(self, new_m):
        new_hashtable = [dict() for _ in range(new_m)]
        old_m = self._M
        self._M = new_m
        for i in range(old_m):
            _map = self._hashtable[i]
            for k, v in _map.items():
                new_hashtable[self._hash(k)][k] = v
        self._hashtable = new_hashtable

    def __str__(self):
        return f'len: {len(self._hashtable)}, _hashtable: {self._hashtable}'


if __name__ == '__main__':
    hb = HashTable()
    for i in range(100):
        hb.add(str(i), i)
    print(hb)
    print(hb['55'])
