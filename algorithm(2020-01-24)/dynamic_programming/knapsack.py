class Knapsack:

    def __init__(self):
        self.memo = []

    # w 为权重数组，v 为价值数组，C 为容量
    def knapsack(self, w, v, C):
        self.memo.clear()
        n = len(w)
        # C+1 表示 [0...c] 的数组下标
        self.memo = [[-1 for _ in range(C+1)] for _ in range(n)]
        return self.recursion_best_value(w, v, n-1, C)

    # 用 [0...index] 的物品，填充容积为 c 的背包的最大价值
    def recursion_best_value(self, w, v, index, c):
        if index < 0 or c <= 0:
            return 0
        if self.memo[index][c] != -1:
            return self.memo[index][c]

        res = self.recursion_best_value(w, v, index-1, c)
        if c >= w[index]:
            res = max(res, v[index]+self.recursion_best_value(w, v, index-1, c-w[index]))
        self.memo[index][c] = res
        return res

    def dynamic_knapsack(self, w, v, C):
        assert len(w) == len(v)
        n = len(w)
        if n == 0 or C == 0:
            return 0

        memo = [[-1 for _ in range(C+1)] for _ in range(2)]
        # j 为容量列
        for j in range(C+1):
            memo[0][j] = v[0] if j >= w[0] else 0

        # i 为物品行，j 为容量列
        for i in range(1, n):
            for j in range(C+1):
                # 优化为只使用 2 行来存储
                memo[i % 2][j] = memo[(i-1) % 2][j]
                if j >= w[i]:
                    memo[i % 2][j] = max(memo[i % 2][j], v[i] + memo[(i-1) % 2][j-w[i]])
        return memo[(n-1) % 2][C]

    def optimization_dynamic_knapsack(self, w, v, C):
        assert len(w) == len(v)
        n = len(w)
        if n == 0 or C == 0:
            return 0

        memo = [-1 for i in range(C+1)]
        # 获取背包容量只放下第一个物品的值
        for j in range(C+1):
            memo[j] = v[0] if j >= w[0] else 0

        for i in range(1, n):
            for j in range(C, 0, -1):
                if j >= w[i]:
                    memo[j] = max(memo[j], v[i] + memo[j-w[i]])
                    print(memo, memo[j], j, j-w[i])
        return memo[C]


if __name__ == '__main__':
    k = Knapsack()
    w = [1, 3, 2, 4]
    v = [5, 10, 12, 16]
    c = 6
    res = k.knapsack(w, v, c)
    res2 = k.dynamic_knapsack(w, v, c)
    res3 = k.optimization_dynamic_knapsack(w, v, c)
    print(res, res2, res3)