class CanPartition:

    def __init__(self):
        self.memo = []

    def can_partition(self, nums):
        n = len(nums)
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        C = int(sums / 2)
        # memo[i][c] 表示使用索引为 [0...i] 的这些元素，是否可以完全填充一个 c 的背包
        # -1 表示未计算；0 表示不可以填充；1 表示可以填充
        self.memo = [[-1 for _ in range(C+1)] for _ in range(n)]
        return self.try_partition(nums, n-1, int(C))

    # 使用 nums[0...index]，是否可以完全填充一个容量为 sums 的背包
    def try_partition(self, nums, index, sums):
        if sums == 0:
            return True
        if sums < 0 or index < 0:
            return False
        if self.memo[index][sums] != -1:
            return self.memo[index][sums] == 1
        self.memo[index][sums] = \
            1 if (self.try_partition(nums, index-1, sums) or
                  self.try_partition(nums, index-1, sums-nums[index])) else 0
        return self.memo[index][sums] == 1

    def dynamic_can_partition(self, nums):
        n = len(nums)
        C = sum(nums)
        if C % 2 != 0:
            return False

        memo = [False for _ in range(C+1)]
        # 检测一个物品能否填满背包
        for i in range(C+1):
            memo[i] = (nums[0] == i)

        for i in range(1, n):
            for j in range(C, 0, -1):
                if j >= nums[i]:
                    # 第 i 个物品的 memo[j] 等于 第 i-1 个物品的 memo[j]
                    # 或者  memo[j-nums[i]] 能不能被填满
                    memo[j] = memo[j] or memo[j-nums[i]]
        return memo[C]


if __name__ == '__main__':
    c = CanPartition()
    nums = [1, 2, 3, 4, 5, 9]
    res = c.can_partition(nums)
    res2 = c.dynamic_can_partition(nums)
    print(res, res2)



