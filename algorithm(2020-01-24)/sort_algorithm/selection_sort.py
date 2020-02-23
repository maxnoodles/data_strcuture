# -*- coding:utf-8 -*-
#
# Author: chenjiaxin
# Date: 2020-02-09
import random
import time
from functools import wraps


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True


def sort_time_count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        assert is_sorted(ret)
        print(f'【{func.__name__}】time count: {end_time - start_time}')
        return ret
    return wrapper


@sort_time_count
def selection_sort(arr):
    n = len(arr)
    # 寻找 [i, n) 区间里的最小值
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


@sort_time_count
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        for j in range(i, 0, -1):
            if temp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                arr[j] = temp
                break
    return arr


def merge_insert_sort(arr, l, r):
    for i in range(l+1, r+1):
        temp = arr[i]
        for j in range(i, l, -1):
            if temp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                arr[j] = temp
                break


@sort_time_count
def merge_sort(arr):
    n = len(arr)
    __merge_sort(arr, 0, n-1)
    print(arr)
    return arr


# 递归调用归并排序，对 arr[l...r] 的范围进行排序 (前关后闭)
def __merge_sort(arr, l, r):
    # if l >= r:
    #     return
    if r-l <= 15:
        merge_insert_sort(arr, l, r)
        return

    # 避免 l + r 造成整形溢出 (python 没有这个问题)
    mid = l + (r-l) // 2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid+1, r)
    if arr[mid] > arr[mid+1]:
        __merge(arr, l, mid, r)


# 将 arr[l...mid] 和 arr[mid+1...r] 两部分进行归并
def __merge(arr, l, mid, r):
    aux = []
    i, j = l, mid+1
    for k in range(r-l+1):

        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            aux.append(arr[j])
            j += 1
        # 当 i 超过 mid 的时候说明左边的都小于右边
        elif i > mid:
            aux.append(arr[j])
            j += 1
        # 当 j 超过 r 的时候说明左边的都大于右边
        elif j > r:
            aux.append(arr[i])
            i += 1
    arr[l:r+1] = aux[:]


@sort_time_count
def merge_sort_up(arr):
    n = len(arr)
    sz = 1
    while sz < n:
        i = 0
        while i + sz < n:
            __merge(arr, i, i+sz-1, min(i+2*sz-1, n-1))
            i += 2*sz
        sz += sz
    return arr


@sort_time_count
def quick_sort(arr):
    n = len(arr)
    __quick_sort(arr, 0, n-1)
    return arr


# 对 arr[l...r] 部分进行快速排序
def __quick_sort(arr, l, r):
    if l >= r:
        return
    # p = __partition(arr, l, r)
    p = optimizer__partition(arr, l, r)
    __quick_sort(arr, l, p-1)
    __quick_sort(arr, p+1, r)


# 对 arr[l...r] 部分进行 partition 操作
# 返回 p, 使得 arr[l...p-1] < arr[p] ; arr[p+1] > arr[p]
def __partition(arr, l, r):
    # 优化点，使用数组随机的元素作为快排的标定点，这样可以避免有序数组的快排退化成链表
    random_index = random.randint(l, r)
    arr[l], arr[random_index] = arr[random_index], arr[l]

    v = arr[l]

    # arr[l+1...p] < v ; arr[p+1...i) > v
    p = l  # 从 p 开始，满足上面注释定义 [l+1...l] 不存在, [l+1...l+1) 不存在
    for i in range(l+1, r+1):
        if arr[i] < v:
            arr[i], arr[p+1] = arr[p+1], arr[i]
            p += 1
    arr[l], arr[p] = arr[p], arr[l]
    return p


# 优化含有大量重复元素的数组，尽量是快排平均切分
def optimizer__partition(arr, l, r):
    random_index = random.randint(l, r)
    arr[l], arr[random_index] = arr[random_index], arr[l]
    v = arr[l]

    i, j = l+1, r
    # arr[l+1...p] <= v ; arr[p+1...i) >= v
    while True:
        while i <= r and arr[i] < v:
            i += 1
        while j >= l+1 and arr[j] > v:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j


@sort_time_count
def python_sort(arr):
    return sorted(arr)


if __name__ == '__main__':
    n = 100000
    arr = [random.randint(0, n) for _ in range(n)]
    # arr = [i for i in range(n, 0, -1)]
    print(arr)
    # selection_sort(arr[:])
    # insertion_sort(arr[:])
    # merge_sort(arr[:])
    # python_sort(arr[:])
    # merge_sort_up(arr[:])
    # print(arr)
    quick_sort(arr[:])
