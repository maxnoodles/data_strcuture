from chapter_04_LinkedList.linked_list import LinkedList


class LinkedListStack:

    def __init__(self):
        self.list = LinkedList()

    def get_size(self):
        return self.list.get_size()

    def is_empty(self):
        return self.list.is_empty()

    def push(self, value):
        return self.list.add_first(value)

    def pop(self):
        return self.list.remove_first()

    def peek(self):
        return self.list.get_first()

    def __str__(self):
        linked_str = ''
        print(f'Stack :top {self.list}')
        return linked_str


if __name__ == "__main__":
    stack = LinkedListStack()
    for i in range(5):
        stack.push(i)
        print(stack)
    stack.pop()
    print(stack)


