
class BST:

    class _Node:
        def __init__(self, v):
            self.v = v
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, v):
        if self.root is None:
            self.root = self._Node(v)
        else:
            self._add(self.root, v)

    def _add(self, node, v):
        if node.v == v:
            return
        elif v < node.v and node.left is None:
            node.left = self._Node(v)
            self._size += 1
            return
        elif v > node.v and node.right is None:
            node.right = self._Node(v)
            self._size += 1
            return

        if v < node.v:
            self._add(node.left, v)
        else:
            self._add(node.right, v)



if __name__ == '__main__':
    a = BST()





