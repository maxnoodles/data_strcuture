

def recursion_climb(n):
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    if n == 0 or n == 1:
        return 1
    return recursion_climb(n-1) + recursion_climb(n-2)


def memory_climb(n, memo_list):
    print('memory_climb_n', n)
    if n == 0 or n == 1:
        return 1
    if memo_list[n] == -1:
        memo_list[n] = memory_climb(n-1, memo_list) + memory_climb(n-2, memo_list)
    # 第一遍计算所有子过程，后续递归加上子过程
    return memo_list[n]


def dynamic_climb(n):
    memo_list = [-1 for _ in range(n+1)]
    memo_list[0] = 1
    memo_list[1] = 1
    for i in range(2, n+1):
        memo_list[i] = memo_list[i-1] + memo_list[i-2]
    return memo_list[n]


if __name__ == '__main__':
    n = 5
    print('recursion_climb', recursion_climb(n))
    memory_list = [-1 for _ in range(n+1)]
    print('memory_climb', memory_climb(n, memory_list))
    print('dynamic_climb', dynamic_climb(n))

