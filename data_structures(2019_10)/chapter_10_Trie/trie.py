# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2019-12-19
import time


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

    def add(self, word):
        cur = self._root
        for i in word:
            if not cur.next.get(i):
                cur.next[i] = self._Node()
            cur = cur.next[i]
        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        cur = self._root
        for i in word:
            if not cur.next.get(i):
                return False
            cur = cur.next[i]
        return cur.is_word

    def is_prefix(self, prefix):
        cur = self._root
        for i in prefix:
            if not cur.next.get(i):
                return False
            cur = cur.next[i]
        return True

    def search(self, word):
        return self._match(self._root, word, 0)

    def _match(self, node, word, index):
        if index == len(word):
            return node.is_word

        c = word[index]
        if c != '.':
            if not node.next.get(c):
                return False
            return self._match(node.next.get(c), word, index+1)
        else:
            for i in node.next.keys():
                return self._match(node.next.get(i), word, index+1)
            return False


    def __str__(self):
        return self.__str(self._root)

    def __str(self, node):
        if not node.next:
            return
        for k, v in node.next.items():
            print(k)
            self.__str(v)
        return ''

if __name__ == "__main__":
    from contextlib import contextmanager

    @contextmanager
    def timer(name):
        start = time.time()
        yield
        print(f'[{name}] done in {time.time() - start:.5f} s')

    trie = Trie()
    with timer('add'):
        trie.add('pan')
        trie.add('pand')
        trie.add('pbcd')
        trie.add('abcd')

    with timer('trie'):
        print(trie)

    print(trie.contains('abc'))
    print(trie.contains('pan'))
    print(trie.contains('pand'))

    print(trie.is_prefix('pas'))
    print(trie.search('p.cd'))