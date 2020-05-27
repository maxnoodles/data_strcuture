# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-04-20


def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = average()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))


