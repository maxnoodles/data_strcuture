import random


l = [random.randrange(0, 100) for i in range(9)]
print(l)


# 冒泡排序
def bubble_sort(list):
    for i in range(len(list)-1):
        flag = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = True
        if flag == False:
            break
    return list
# print(bubble_sort(l))


def bubble_sort2(list):
    flag = 1
    i = len(l)-1
    while flag:
        flag = 0
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = 1
        i -= 1
    return list
# print(bubble_sort2(l))


# 选择排序
def selection_sort(list):
    for i in range(len(list)-1):
        k = len(list)-1
        for j in range(i, len(list)):
            if list[j] < list[k]:
                k = j
        list[i], list[k] = list[k], list[i]
        print(list)
    return list
print(selection_sort(l))


# 快速排序
def quick_sort(list, left, right):
    if left >= right:
        return list
    key = left
    low = left
    high = right

    while left < right:
        while left < right and list[right] >= list[key]:
            right -= 1
        while left < right and list[left] <= list[key]:
            left += 1
        list[left], list[right] = list[right], list[left]
    list[key], list[left] = list[left], list[key]
    print(list)
    quick_sort(list, low, left-1)
    quick_sort(list, left+1, high)
    return list
# print(quick_sort(l, 0, len(l)-1))


def quick_sork2(l, left, right):
    if left >= right:
        return l
    key = left
    low = left
    high = right

    while left < right:
        while left < right and l[right] >= l[key]:
            right -= 1
        while left < right and l[left] <= l[key]:
            left += 1
        l[left], l[right] = l[right], l[left]
    l[key], l[left] = l[left], l[key]
    quick_sork2(l, low, left-1)
    quick_sork2(l, left+1, high)
    return l
# print(quick_sork2(l, 0, len(l)-1))


# 插入排序
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = key
    return list
# print(insertion_sort(l))


def shell_sort(list):
    step = int(len(list)/2)
    while step > 0:
        for i in range(step, len(list)):
            x = list[i]
            j = i - step
            while j >= 0 and list[j] > x:
                list[j+step] = list[j]
                j = j - step
            list[j + step] = x
        step = int(step/2)
    return list
# print(shell_sort(l))


# 归并排序
def merge_sore(list):
    if len(list) < 2:
        return list
    mid = int(len(list)/2)
    left = merge_sore(list[:mid])
    right = merge_sore(list[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
# print(merge_sore(l))