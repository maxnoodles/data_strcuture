# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-02-06

from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Interval:
    start: int = 0
    end: int = 0


def dynamic_erase_overlap_intervals(intervals):

    def cmp(a, b):
        if a.start != b.start:
            return a.start - b.start
        return a.end - b.end

    if len(intervals) == 0:
        return 0
    new_intervals = sorted(intervals, key=cmp_to_key(cmp))
    memo = [1 for _ in new_intervals]
    for i in range(1, len(memo)):
        for j in range(0, i):
            if intervals[i].start >= intervals[j].end:
                memo[i] = max(memo[i], 1 + memo[j])
    return len(intervals) - max(memo)


def greedy_erase_overlap_intervals(intervals):

    def cmp(a, b):
        if a.end != b.end:
            return a.end - b.end
        return a.start - b.start

    new_intervals = sorted(intervals, key=cmp_to_key(cmp))
    res = 1
    pre = 0
    for i in range(1, len(new_intervals)):
        if intervals[i].start >= intervals[pre].end:
            pre = i
            res += 1
    return len(intervals) - res


if __name__ == '__main__':
    intervals = [Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)]
    res1 = dynamic_erase_overlap_intervals(intervals)
    res2 = greedy_erase_overlap_intervals(intervals)
    print(res1, res2)