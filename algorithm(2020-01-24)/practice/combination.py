
class Combination:

    def __init__(self):
        self.res = []

    # 求解 C(n, k),
    def gen_combination(self, n, k):
        if n <= 0 or not 0 <= k <= n:
            return []

        self._gen_combination(n, k, 1, [])
        return self.res

    # 求解 C(n, k), 当前已经找到的组合存储在 c 中， 需要从 start 开始搜索新的元素
    def _gen_combination(self, n, k, start, c):
        if len(c) == k:
            self.res.append(c[:])
            return

        for i in range(start, n+1):
            c.append(i)
            self._gen_combination(n, k, i+1, c)
            c.pop()
        return


if __name__ == '__main__':
    c = Combination()
    res = c.gen_combination(5, 3)
    print(res)
