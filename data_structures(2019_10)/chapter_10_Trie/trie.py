# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-12-19


class Trie:

    class _Node:
        def __init__(self, is_word=False, _next=None):
            self.is_word = is_word
            self.next = _next or dict()

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    def get_size(self):
        return self._size


if __name__ == "__main__":
    pass

