from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        container = set()
        rk, ret = -1, 0
        for i in range(length):
            if i != 0:
                # 向右滑动一位，删除前一位的数字
                container.remove(s[i-1])
            while rk + 1 < length and s[rk+1] not in container:
                container.add(s[rk+1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ret = max(ret, rk - i + 1)
        return ret


if __name__ == "__main__":
    s = "pwwkew"
    S = Solution()
    res1 = S.lengthOfLongestSubstring(s)
    print(res1)
    assert res1 == 3
