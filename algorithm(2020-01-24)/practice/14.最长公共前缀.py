from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        first_str = strs[0]
        for i in range(len(first_str)):
            for string in strs[1:]:
                if i == len(string) or string[i] != first_str[i]:
                    return first_str[:i]
        return first_str if first_str else ''


if __name__ == "__main__":
    strs = ["aa", "aa"]
    S = Solution()
    ret = S.longestCommonPrefix(strs)
    print(ret)
    assert ret == 'aa'
