def recursion_break(n):
    if n == 1:
        return 1

    res = -1
    for i in range(1, n):
        res = max(res, i * (n-i), i * recursion_break(n-i))
    return res


def memo_break(n):
    memo_list = [-1 for _ in range(n+1)]
    memo_list[1] = 1

    def _memo_break(n):
        if n == 1:
            return 1

        if memo_list[n] != -1:
            return memo_list[n]

        res = -1
        for i in range(1, n):
            res = max(res, i * (n-i), i * _memo_break(n-i))
        memo_list[n] = res
        return memo_list[n]
    return _memo_break(n)


def dynamic_break(n):
    assert n >= 2
    # memo_list[i] 表示将数字 i 分割(至少分割成两个部分)后得到的最大乘积
    memo_list = [-1 for _ in range(n+1)]
    memo_list[1] = 1
    for i in range(2, n+1):
        # 求解 memo[i]
        for j in range(1, i):
            # 把 n 分解成 j + (i-j)，并查看其最大值
            print('count', memo_list[i], i, j, end='')
            memo_list[i] = max(memo_list[i], j * (i-j), j * memo_list[i-j])
            print('---', memo_list[i])
    return memo_list[n]


if __name__ == '__main__':
    print('recursion_break', recursion_break(10))
    print('memo_break', memo_break(10))
    print('dynamic_break', dynamic_break(10))