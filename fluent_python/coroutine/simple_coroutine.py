# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-04-20


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print(f'-> coroutine received:{x}')


my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
my_coro.send(42)


