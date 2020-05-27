# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-04-17
import contextlib


@contextlib.contextmanager
def aaa(x):
    print(f'>>>>>>>', x+1)
    yield x
    print(f'<<<<<<<', x-1)


with aaa(5) as a:
    print(a)
