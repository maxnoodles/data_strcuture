# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-03-31
import itertools
import re
import reprlib


RE_WORD = re.compile(r"\w+")


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence:

    def __init__(self, text):
        self.text = text
        # self.words = RE_WORD.findall(text)

    # def __getitem__(self, index):
    #     return self.words[index]

    # def __iter__(self):
    #     return SentenceIterator(self.words)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


def aritprog_gen(begin, step, end=None):
    # a, b = 1, 1.0
    # type(a+b) --> float()
    # float(a) --> 1.0
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, itertools.count(first, step))
    return ap_gen
    # forever = end is None
    # index = 0
    # while forever or result < end:
    #     yield result
    #     index += 1
    #     result = begin + step * index

# gen = itertools.takewhile(lambda n: n<3, itertools.count(1, 0.5))


def my_chain(*iterable):
    for i in iterable:
        yield from i


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))

    print(list(my_chain(s, range(123))))






