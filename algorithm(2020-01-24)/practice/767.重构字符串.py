class Solution(object):
    def reorganizeString(self, S):
        length = len(S)
        s_sorted = []
        res = [None] * length
        s_count = [(S.count(x), x) for x in set(S)]
        for count, s in sorted(s_count):
            if count > (length+1) / 2:
                return ''
            s_sorted.extend(s * count)
        res[::2], res[1::2] = s_sorted[length//2:], s_sorted[:length//2]
        return ''.join(res)

if __name__ == "__main__":
    s = 'accccbbbb'
    S = Solution()
    res = S.reorganizeString(s)
    print(res)