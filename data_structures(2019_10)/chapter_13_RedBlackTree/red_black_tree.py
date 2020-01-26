from enum import Enum


class Color(Enum):
    Red: bool = True
    Black: bool = False


class RBTree:

    class _Node:
        RED = True
        BALCK = False

        def __init__(self, v: int):
            self.v = v
            self.left = None
            self.right = None
            self.color = self.RED

    def __init__(self):
        self.root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # 空节点为黑色
    def is_red(self, node: _Node):
        return node.color if node else self._Node.BALCK

    # 对节点 node 进行左旋转， 返回旋转后新的根节点x
    #     node                                 x
    #    /   \                               /    \
    #   T1    x       向左旋转 (y)           node   T3
    #       /   \   - - - - - - - - - >    /  \
    #      T2    z                        T1  T2
    def _left_rotate(self, node: _Node):
        x = node.right
        # 左旋转
        node.right = x.left
        x.left = node

        x.color = node.color
        node.color = self._Node.RED
        return x

    # 对节点 y 进行右旋转， 返回旋转后新的根节点x
    #      node                                  x
    #      /   \                              /   \
    #     x    T2       向右旋转 (y)           y    node
    #    /  \       - - - - - - - - - >            /  \
    #   y   T1                                    T1  T2
    def _right_rotate(self, node: _Node):
        x = node.left
        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = self._Node.RED
        return x

    def _flip_colors(self, node):
        node.color = self._Node.RED
        node.left.color = self._Node.BALCK
        node.right.color = self._Node.BALCK

    # 向红黑树添加元素
    def add(self, v: int):
        self.root = self._add(self.root, v)
        # 根节点为黑色
        self.root.color = self._Node.BALCK

    def _add(self, node, v) -> _Node:
        if node is None:
            self._size += 1
            node = self._Node(v)  # 默认插入红节点
            return node
        if v == node.v:
            return node
        if v < node.v:
            node.left = self._add(node.left, v)
        else:
            node.right = self._add(node.right, v)

        # 左旋转 -> 右旋转 -> 颜色翻转
        # 添加节点右边在叶子节点的右边
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self._left_rotate(node)

        # 添加节点右边在叶子节点的左边
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self._right_rotate(node)

        if self.is_red(node.left) and self.is_red(node.right):
            self._flip_colors(node)

        return node

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node is None:
            return
        print(node.v, end=' ')
        self._pre_order(node.left)
        self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node is None:
            return
        self._in_order(node.left)
        print(node.v, end=' ')
        self._in_order(node.right)

    def post_order(self):
        # 应用点：用于程序释放内存
        self._post_order(self.root)

    def _post_order(self, node):
        if node is None:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.v, end=' ')

    def minimum(self):
        node = self._minimum(self.root)
        return node.v

    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def maximum(self):
        node = self._maximum(self.root)
        return node.v

    def _maximum(self, node):
        if node.right is None:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        self.root = self._remove_min(self.root)

    def _remove_min(self, node):
        """
        删除以 node 为根的二分搜索树中的最小节点
        放回删除节点后新的二分搜索树的根
        :return:
        """
        if node.left is None:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        self.root = self._remove_max(self.root)

    def _remove_max(self, node):
        """
        删除以 node 为根的二分搜索树中的最小节点
        放回删除节点后新的二分搜索树的根
        :return:
        """
        if node.right is None:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def remove(self, v):
        self.root = self._remove(self.root, v)

    def _remove(self, node, v):
        if node is None:
            return None

        if v < node.v:
            node.left = self._remove(node.left, v)
            return node
        elif v > node.v:
            node.right = self._remove(node.right, v)
            return node
        else:  # v == node.v
            if node.left is None:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            if node.right is None:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            # 如果左右子树均不为空
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)

            successor.left = node.left
            node.left = node.right = None
            return successor

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_bst_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.v) + '\n')
        self._generate_bst_string(node.left, depth + 1, res)
        self._generate_bst_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_bst_string(self.root, 0, res)
        return '<chapter_06_BST.avl.BST>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    bst = RBTree()
    num_str = '9534165874'
    for i in num_str:
        bst.add(int(i))

    print(bst)
    print('size:', bst.get_size())
    print(bst.pre_order())
    print(bst.in_order())
    print(bst.post_order())
    print('min', bst.minimum())
    print('max', bst.maximum())
    print('remove min')
    bst.remove_min()
    print(bst.pre_order())
    print('remove max')
    bst.remove_max()
    print(bst.pre_order())
    bst.remove(3)
    print(bst.pre_order())





