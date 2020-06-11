from typing import List


class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        stack = []
        result = [0] * length
        for i in range(length):
            while stack and T[i] > T[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    res = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(res)
