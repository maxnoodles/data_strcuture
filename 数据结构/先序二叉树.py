class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.lev = 0

    def is_empty(self):
        return self.root is None

    def insert(self, value, node):
        if self.is_empty():
            self.root = Node(value)
            return
        else:
            if value <= node.data:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert(value, node.left)
            elif node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data, end=',')
            self.preorder(node.left)

            self.preorder(node.right)

    def search(self, value, node):
        if value is None:
            return None
        else:
            if value == node.data:
                return True
            elif value < node.data:
                self.search(value, node.left)
            else:
                self.search(value, node.right)

    def remove(self, value):
        if self.is_empty():
            return False
        else:
            p = None
            f = self.root
            cur = self.root.right
            while cur != None:
                if cur.data == value:
                    p = cur
                    cur = None
                else:
                    if value < cur.data:
                        f = cur
                        cur = cur.left
                    else:
                        f = cur
                        cur = cur.right
            if p is None:
                return "NOTFOUND"
            if p.right is None:
                if p == f.left:
                    f.left = p.left
                    del p
                else:
                    f.right = p.left
                    del p
            if p.left is None:
                if p == f.left:
                    f.left = p.right
                    del p
                else:
                    f.right = p.right
                    del p
            else:
                l = p.left
                if l.right is None:
                    p.data = l.data
                    p.left = l.left
                    del l
                else:
                    r = l.right
                    while r.right is not None:
                        l = r
                        r = r.right
                    p.data = r.data
                    l.right = r.left
        return True

    def level(self, node):
        if node is None:
            return 0
        i = self.level(node.left)
        j = self.level(node.right)
        if i >= j:
            i += 1
        else:
            j += 1
        p = max(i, j)

        return p





tree = BinaryTree()
list = [-1, 63, 45, 40, 30, 23, 35, 53, 51, 48, 60, 55, 57, 72, 81, 77, 95]
for i in list:
    tree.insert(i, tree.root)

# tree.remove(63)
# print(tree.root.left.left.data)
tree.preorder(tree.root)
print('\n')
print("层数为", tree.level(tree.root))