class Stack:

    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size-1

    def push(self, value):
        if self.is_full():
            return False
        self.top += 1
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return False
        self.stack.pop()
        self.top -= 1

    def get_top(self):
        return self.stack[self.top]


a = Stack(10)
print(a.is_empty())
a.push(5)
a.push(9)
a.push(23)
print(a.stack)
print(a.is_full())
print(a.get_top())

a.pop()
print(a.get_top())