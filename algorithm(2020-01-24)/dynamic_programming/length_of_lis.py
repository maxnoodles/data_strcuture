

def length_of_lis(num_list):
    if len(num_list) == 0:
        return 0

    memo = [1 for _ in range(len(num_list))]
    for i in range(len(num_list)):
        for j in range(i):
            if num_list[j] < num_list[i]:
                memo[i] = max(memo[i], 1 + memo[j])

    return max(memo)


if __name__ == '__main__':
    lists = [10, 9, 2, 5, 3, 7, 101, 18]
    res = length_of_lis(lists)
    print(res)