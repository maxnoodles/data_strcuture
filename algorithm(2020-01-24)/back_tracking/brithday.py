
def birthday_candle(nums):
    if nums <= 0:
        return 0
    memo = [i for i in range(nums+1)]

    res = []
    for i in range(1, nums+1):
        for j in range(i, nums+1):
            if sum(memo[i: j+1]) == nums:
                res.append([i, j])
            elif sum(memo[i: j+1]) > nums:
                break
    return res


if __name__ == '__main__':
    res = birthday_candle(100000)
    print(res)








