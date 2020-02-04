class Rob:

    def __init__(self):
        # memo[i] 表示考虑抢劫 nums[i...n] 所能获得的最大收益
        self.memo = []

    def rob(self, nums):
        self.memo = []
        self.memo = [-1 for _ in range(len(nums))]
        return self.try_rob(nums, 0)

    # 考虑抢劫 nums[index...len(nums)] 这个范围的所有房子
    def try_rob(self, nums, index):
        if index >= len(nums):
            return 0

        if self.memo[index] != -1:
            return self.memo[index]
        res = 0
        for i in range(index, len(nums)):
            res = max(res, nums[i] + self.try_rob(nums, i+2))
        self.memo[index] = res
        return res

    # 偷取 [x...n-1] 范围里的房子
    def dynamic_rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        memo = [-1 for _ in range(n)]
        memo[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                memo[i] = max(memo[i], nums[j] + (memo[j+2] if j+2 < n else 0))
        return memo[0]

    # 偷取 [0...x] 范围里的房子
    def dynamic_rob2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        memo = [-1 for _ in range(n)]
        memo[0] = nums[0]
        # 偷取 x 到 x-1 号房
        for i in range(1, n):
            for j in range(i, -1, -1):
                memo[i] = max(memo[i], nums[j] + (memo[j-2] if j-2 >= 0 else 0))
        return memo[n-1]


if __name__ == '__main__':
    r = Rob()
    nums = [3, 4, 1, 2, 6, 7, 9, 2]
    nums2 = [4, 3, 1, 2, 5, 6, 3, 2]
    for i in [nums, nums2]:
        print(r.rob(i))
        print(r.dynamic_rob(i))
        print(r.dynamic_rob2(i))


