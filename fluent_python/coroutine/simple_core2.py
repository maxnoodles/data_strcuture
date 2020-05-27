# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-04-20

b = 1
def simple_coro2(a):
    global b
    print('-> Started: a =', a)
    # 先产出 a ，等下一次激活协程代码时才是为 b 赋值
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
    return 5


my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2))

print(next(my_coro2))
print(f'bbbbbb: {b}')
print(getgeneratorstate(my_coro2))

print(my_coro2.send(28))
print(f'bbbbbb2222: {b}')

print(my_coro2.send(99))
print(getgeneratorstate(my_coro2))
