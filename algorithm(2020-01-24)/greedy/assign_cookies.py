# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-02-06


# g 为贪心指数， s 为饼干大小
def find_content_children(g, s):
    sort_g = sorted(g, reverse=True)
    sort_s = sorted(s, reverse=True)
    res = 0
    gi, si = 0, 0
    while gi < len(g) and si < len(s):
        if sort_s[si] >= sort_g[gi]:
            res += 1
            gi += 1
            si += 1
        else:
            gi += 1

    return res


if __name__ == '__main__':
    g = [5, 3, 1, 6, 7]
    s = [4, 2, 7, 8, 9]
    res = find_content_children(g, s)
    print(res)


