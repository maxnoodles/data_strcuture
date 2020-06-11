class Solution:

    def __init__(self):
        self.count = 0
        self.memo = []

    def translate_num(self, num: int):
        num_str = str(num)
        self.memo = [0 for _ in range(len(num_str))]
        return self._translate_num(num_str, 0)

    def _translate_num(self, num_str, start: int):
        if start <= len(num_str) - 1 and self.memo[start]:
            return self.memo[start]

        if start >= len(num_str) - 1:
            return 1

        if 10 <= int(num_str[start] + num_str[start + 1]) <= 25:
            self.memo[start] = self._translate_num(num_str, start + 1) + self._translate_num(num_str, start + 2)
        else:
            self.memo[start] = self._translate_num(num_str, start + 1)
        return self.memo[start]

    def dp_translate_num(self, num: int):
        num_str = str(num)
        return self._dp_translate_num(num_str)

    def _dp_translate_num(self, num_str):
        n = len(num_str)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            if 10 <= int(num_str[i-2] + num_str[i-1]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    count = s.translate_num(12258)
    count2 = s.dp_translate_num(25)
    print(count, count2)

