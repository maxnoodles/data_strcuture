
class AVLTree:

    class _Node:
        def __init__(self, v):
            self.v = v
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __contains__(self, item):
        return self._contains(self.root, item)

    def _contains(self, node, e):
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)
    # 判断是否是二分搜索树
    def is_bst(self):
        values = []
        self.in_order(self.root, values)
        for i in range(1, len(values)):
            if values[i-1] > values[i]:
                return False
        return True

    def is_balance(self):
        return self._is_balance(self.root)

    def _is_balance(self, node):
        if node is None:
            return True
        if abs(self.get_balance_factor(node)) > 1:
            return False
        return self._is_balance(node.left) and self._is_balance(node.right)

    def in_order(self, node, values):
        if node is None:
            return
        self.in_order(node.left, values)
        values.append(node.v)
        self.in_order(node.right, values)

    # 获取节点 node 的平衡因子
    def get_height(self, node: _Node):
        if node is None:
            return 0
        return node.height

    # 获得节点 node 的平衡因子
    def get_balance_factor(self, node: _Node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 对节点 y 进行右旋转， 返回旋转后新的根节点x
    #        y                                  x
    #      /   \                              /    \
    #     x    T4       向右旋转 (y)           z      y
    #    /  \       - - - - - - - - - >     /  \   /  \
    #   z   T3                             T1  T2  T3 T4
    #  /  \
    # T1  T2
    def right_rotate(self, y: _Node):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        # 更新 height
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    # 对节点 y 进行左旋转， 返回旋转后新的根节点x
    #      y                                   x
    #    /   \                               /    \
    #   T1    x       向左旋转 (y)            y      z
    #       /   \   - - - - - - - - - >    /  \   /  \
    #      T2    z                        T1  T2 T3  T4
    #           /  \
    #          T3   T4
    def left_rotate(self, y: _Node):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        # 更新 height
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def add(self, v):
        self.root = self._add(self.root, v)

    def _add(self, node, v):
        if node is None:
            self._size += 1
            node = self._Node(v)
            return node
        if v == node.v:
            return node
        if v < node.v:
            node.left = self._add(node.left, v)
        else:
            node.right = self._add(node.right, v)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # 计算平衡因子
        balance_factor = self.get_balance_factor(node)
        if abs(balance_factor) > 1:
            print(f'unbalanced: {balance_factor}')

        # LL
        if balance_factor > 1 and self.get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # RR
        if balance_factor < -1 and self.get_balance_factor(node.left) >= 0:
            return self.left_rotate(node)

        # LR
        if balance_factor > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance_factor < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node is None:
            return
        print(node.v, end=' ')
        self._pre_order(node.left)
        self._pre_order(node.right)

    # def in_order(self):
    #     self._in_order(self.root)
    #
    # def _in_order(self, node):
    #     if node is None:
    #         return
    #     self._in_order(node.left)
    #     print(node.v, end=' ')
    #     self._in_order(node.right)

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
    
        ret_node = node
        if v < node.v:
            node.left = self._remove(node.left, v)
            ret_node = node
        elif v > node.v:
            node.right = self._remove(node.right, v)
            ret_node = node
        else:  # v == node.v
            if node.left is None:
                right_node = node.right
                node.right = None
                self._size -= 1
                ret_node = right_node

            elif node.right is None:
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node

            else:
                # 如果左右子树均不为空
                # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
                # 用这个节点顶替待删除节点的位置
                successor = self._minimum(node.right)
                successor.right = self._remove(node.right, successor.v)
                successor.left = node.left
                node.left = node.right = None
                ret_node = successor

            if ret_node is None:
                return ret_node

            ret_node.height = 1 + max(self.get_height(ret_node.left),
                                  self.get_height(ret_node.right))

            # 计算平衡因子
            balance_factor = self.get_balance_factor(ret_node)
            if abs(balance_factor) > 1:
                print(f'unbalanced: {balance_factor}')

            # LL
            if balance_factor > 1 and self.get_balance_factor(ret_node.left) >= 0:
                return self.right_rotate(ret_node)

            # RR
            if balance_factor < -1 and self.get_balance_factor(ret_node.left) >= 0:
                return self.left_rotate(ret_node)

            # LR
            if balance_factor > 1 and self.get_balance_factor(ret_node.left) < 0:
                ret_node.left = self.left_rotate(ret_node.left)
                return self.right_rotate(ret_node)

            if balance_factor < -1 and self.get_balance_factor(ret_node.right) > 0:
                ret_node.right = self.right_rotate(ret_node.right)
                return self.left_rotate(ret_node)
            
            return ret_node
        
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
    avl = AVLTree()
    num_str = '123456789'
    for i in num_str:
        avl.add(int(i))

    print(avl)
    print('size:', avl.get_size())
    print('pre_order: ', avl.pre_order())
    print('post_order: ', avl.post_order())
    print('min', avl.minimum())
    print('max', avl.maximum())
    print('remove min')
    avl.remove_min()
    print(avl.pre_order())
    print('remove max')
    avl.remove_max()
    print(avl.pre_order())
    avl.remove(3)
    print(avl.pre_order())

    print('is_bst: {}'.format(avl.is_bst()))
    print('is_balance: {}'.format(avl.is_balance()))

    for i in num_str:
        avl.remove(int(i))
        if not avl.is_balance() or not avl.is_bst():
            raise ValueError('error')


