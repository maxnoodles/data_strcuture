
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linklist:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def printlist(self, head):
        cur = self.head
        while cur != None:
            print(cur.data, end='')
            cur = cur.next
        print(' ')
        return None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.add(value)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, key, value):
        if key < 0:
            self.add(value)
        elif key > self.length()-1:
            self.append(value)
        else:
            node = Node(value)
            cur = self.head
            count = 0
            while count == key:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, value):
        if self.is_empty():
            return False
        cur = self.head
        pre = cur.next
        if cur.data == self.head:
            p = cur
            self.head = pre
            del p
        else:
            while pre.next is not None:
                if pre.data == value:
                    cur.next = pre.next
                    del pre
                    break
                cur = pre
                pre = pre.next
            return False

    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
                return True
            cur = cur.next
        return False


l = Linklist()
print(l.is_empty())
print(l.length())

l.add(5)
l.append(2)  # 5, 2
l.insert(1, 3)
# print(l.length()) # 5, 3, 2
l.printlist(l.head)
l.remove(3)

# l.remove(5)

l.printlist(l.head)

print(l.search(2))




