# 自建列表
class MyList():

    def __init__(self, max=8):
        self.max = max  # python列表默认8字节
        self.num = 0
        self.data = [None] * self.max

    # 列表判空
    def is_empty(self):
        return self.num is 0

    # 列表判满
    def is_full(self):
        return self.num is self.max

    # 获得某个位置的值
    def __getitem__(self, key):
        if not isinstance(key, int):
            return TypeError
        if 0 < key < self.num:
            return self.data[key]
        else:
            raise IndexError

    # 设置某个位置的值
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            return TypeError
        # 只能访问列表里已有的元素,self.num=0时，一个都不能访问,self.num=1时，只能访问0
        if 0 <= key < self.max:
            self.data[key] = value
        else:
            raise IndexError

    # 清空列表
    def clear(self):
        self.__init__()

    # 获取长度
    def __len__(self):
        return self.num

    # 在结尾插入
    def append(self, value):
        if self.is_full():
            self.max *= 2
            for i in range(self.num + 1, self.max):
                self.data[i] = None
            return
        else:
            self.data[self.num] = value
            self.num += 1

    # 在指定中间插入
    def insert(self, key, value):
        if not isinstance(key, int):
            return TypeError
        if key < 0:
            raise IndexError
        if key >= self.num:
            self.append(value)
        else:
            for i in range(self.num, key, -1):
                self.data[i] = self.data[i-1]
            self.data[key] = value
            self.num += 1

    # 删除元素
    def pop(self, key=-1):
        if not isinstance(key, int):
            return TypeError
        if self.is_empty():
            raise IndexError
        elif key == -1:
            self.num -= 1
        else:
            for i in range(key, self.num-1):
                self.data[i] = self.data[i+1]
            self.num -= 1

    # 获得索引
    def index(self, value):
        # for i in range(self.num):
        #     if value == self.data[i]:
        #         return
        left, right = 0, self.num
        while left < right:
            mid = int((left + right)/2)
            if value == self.data[mid]:
                return mid
            elif value < self.data[mid]:
                right = mid-1
            else:
                left = mid+1
        raise ValueError

    # 翻转数组
    def reversed(self):
        i, j = 0, self.num
        while i < j:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i, j = i+1, j-1

if __name__ == '__main__':
    a = MyList()
    print(a.data)
    print(a.is_empty())
    a.append(2)
    a.append(3)
    a.append(4)
    print(a.data, a.num, a.max)
    a.insert(0, 0)
    print(a.data)
    a[1] = 1
    print(a.data, len(a))
    print('索引为', a.index(4))

    a.pop()
    print(a.data, a.num)
    a.reversed()
    print(a.data)