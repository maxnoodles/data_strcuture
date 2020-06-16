from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = dict()
        for i, v in enumerate(nums):
            if not mapper.get(target-v) is None:
                return [mapper[target-v], i]
            if not mapper.get(v):
                mapper[v] = i


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)
