# 链式列表
# class Node:
#
#     def __init__(self, data=None):
#         self.next = None
#         self.data = data
#
# class Queue:
#
#     def __init__(self, size):
#         self.first = Node()
#         self.last = self.first
#
#     def is_empty(self):
#         return self.first is self.last
#
#     def enter(self, value):
#         node = Node(value)
#         self.last.next = node
#         self.last = node
#
#     def quit(self):
#         if self.is_empty():
#             return False
#         else:
#             q = self.first.next
#             self.first.next = q.next
#             x = q.data
#             del q
#             return x
#
#     def printquene(self):
#         cur = self.first.next
#         while cur != None:
#             print(cur.data)
#             cur = cur.next
#         return None
#
# q = Quene(5)
# q.enter(2)
# q.enter(6)
# q.enter(90)
# q.printquene()
#
# q.quit()
# q.quit()
# q.printquene()


# 循环队列
class LoopQueue:

    def __init__(self, size):
        self.first = 0
        self.last = 0
        self.size = size
        self.data = [None] * size

    def is_empty(self):
        return self.first == self.last

    def is_full(self):
        return (self.last + 1) % self.size == self.first

    def enter(self, x):
        if self.is_full():
            return False
        else:
            self.data[self.last] = x
            self.last = (self.last + 1) % self.size

    def quit(self):
        if self.is_empty():
            return False
        else:
            x = self.data[self.first]
            self.data[self.first] = None
            self.first = (self.first + 1) % self.size
            return x


l = LoopQueue(4)
print(l.is_empty())
print(l.is_full())
l.enter(2)
l.enter(4)
print(l.data)
l.enter(0)
l.enter(-4)
print(l.data)
print(l.is_empty())
print(l.is_full())
l.quit()
l.quit()
print(l.data)
l.quit()
print(l.data)
print(l.is_empty())
