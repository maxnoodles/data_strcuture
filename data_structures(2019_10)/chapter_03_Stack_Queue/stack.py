from chapter_02_Array.array import MyArray


class ArrayStack:

    def __init__(self, capacity=10):
        self._array = MyArray(capacity=capacity)

    def push(self, value):
        self._array.add_last(value)

    def pop(self):
        return self._array.remove_last()

    def peek(self):
        return self._array.get_first()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self._array.get_capacity()

    def __str__(self):
        return str('<chapter_03_Stack_Queue.stack.ArrayStack> : {}'.format(self._array))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':

    def is_valid(input_str):
        stack = ArrayStack()
        left_ = {'{', '(', '['}
        hash_ = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for i in input_str:
            if i in left_:
                stack.push(i)
            else:
                if stack.is_empty() or stack.pop() != hash_[i]:
                    return False
        return stack.is_empty()

    input_str1 = '[{(())}]'
    print(is_valid(input_str1))

    input_str1 = '[{(())})'
    print(is_valid(input_str1))



