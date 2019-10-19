# 构建树节点
class TreeNode:

    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.Lson = None
        self.Rson = None
        self.code = ''


# 哈弗曼树类
class HuffmanTree:

    def __init__(self):
        self.size = 0
        self.queue = []
        self.prioryDic = {}
        self.freChar(string)
        # self.create_node()

    # 根据字符频率按优先度排列
    def freChar(self, string):
        for i in string:
            if i not in self.prioryDic:
                self.prioryDic[i] = 1
            else:
                self.prioryDic[i] += 1
        return sorted(self.prioryDic.items(), key=lambda x:x[1])

    def create_node(self, string):
        if self.prioryDic == {}:
            return False
        for node in self.freChar(string):
            self.queue.append(TreeNode(node))
        self.size = len(self.queue)
        return self.queue

    def add_node(self, node):
        self.size += 1
        if len(self.queue) == 0:
            return self.queue.append(node)
        for i in range(len(self.queue)):
            # print(self.queue[i].priority)
            if self.queue[i].priority >= node.priority:
                self.queue = self.queue[:i] + [node] + self.queue[i:]
                return
        self.queue = self.queue + [node]

    def pop_node(self):
        self.size -= 1
        return self.queue.pop(0)

    def create_tree(self):
        while self.size != 1:
            node1 = self.pop_node()
            node2 = self.pop_node()
            # print(node1.priority, node2.priority)
            r = TreeNode([None, node1.priority + node2.priority])
            r.Lson = node1
            r.Rson = node2
            self.add_node(r)
        return self.queue

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.Lson)
        print(root.val)
        self.inorder(root.Rson)


encodeDic = {}
decodeDic = {}


def HuffmanCode(head, x):
    global encodeDic, decodeDic
    if head:
        HuffmanCode(head.Lson, x+'0')
        head.code += x
        if head.val:
            encodeDic[head.val] = head.code
            decodeDic[head.code] = head.val
        HuffmanCode(head.Rson, x+'1')


# 字符串编码
def huffman_encode(string):
    global encodeDic
    transcode = ''
    for c in string:
        transcode += encodeDic[c]
    return transcode


# 字符串解码
def huffman_decode(StringCode):
    global decodeDic
    code= ''
    ans = ''
    for c in StringCode:
        code += c
        if code in decodeDic:
            ans += decodeDic[code]
            code = ''
    return ans


string = "AAGGDCCCDDDGFBBBFFGGDDDDGGGEFFDDCCCCDDFGAAA"
t = HuffmanTree()
a = t.create_node(string)
b = t.create_tree()
t.inorder(t.queue[0])

HuffmanCode(t.queue[0],'')
print(encodeDic, decodeDic)
en = huffman_encode(string)
print(en)
de = huffman_decode(en)
print(de)






