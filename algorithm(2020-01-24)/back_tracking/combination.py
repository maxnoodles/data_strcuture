class Combination:

    def __init__(self):
        self.res = []

    def combination(self, n, k):
        if n <= 0 and not 0 <= k <= n:
            return []
        c = []
        self._generate_combinations(n, k, 1, c)
        return self.res

    # 求解 C(n, k), 当前已经找到的组合存储在 c 中， 需要从 start 开始搜索新的元素
    def _generate_combinations(self, n, k, start, c):
        if len(c) == k:
            self.res.append(c[:])
            return

        # 剪枝: 还有k - c.size()个空位，所以 [i...n] 中至少需要 k-len(c)个元素
        # i 最多为 n - (k-len(c)) + 1
        for i in range(start, (n+1 - (k-len(c) + 1))):
            print(start, i)
            c.append(i)
            self._generate_combinations(n, k, i+1, c)
            c.pop()

        return


if __name__ == '__main__':
    c = Combination()
    res = c.combination(5, 3)
    print(res)



