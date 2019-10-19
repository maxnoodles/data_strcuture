import random

lists = [random.randrange(0, 100) for i in range(9)]
print(lists)


# 冒泡排序
def bubble_sort(lists):
    for i in range(len(lists)-1):
        flag = 0
        for j in range(len(lists)-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
                flag = 1
            if flag == 0:
                return lists
    return lists
# print(bubble_sort(lists))


# 选择排序
def select_sort(lists):
    length = len(lists)
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if lists[j] < lists[min_index]:
                min_index = j
        if i != min_index:
            lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists
# print(select_sort(lists))


# lists = [47, 90, 76, 34, 98, 43, 44, 44, 38]

def quick_sort(lists, left, right):
    if left > right:
        return lists
    left_ = left
    key = left
    low = left
    high = right

    while left_ < right:
        while left_ < right and lists[right] >= lists[key]:
            right -= 1
        while left_ < right and lists[left] <= lists[key]:
            left_ += 1
        lists[left_], lists[right] = lists[right], lists[left]
    lists[left_], lists[key] = lists[key], lists[left]
    quick_sort(lists, low, left_-1)
    quick_sort(lists, left_+1, high)
    return lists
# print(quick_sort(lists, 0, len(lists)-1))


def insert_sort(lists):
    for i in range(1, len(lists)):
        pre_index = i - 1
        current = lists[i]
        while pre_index >= 0 and lists[pre_index] > current:
            lists[pre_index+1] = lists[pre_index]
            pre_index -= 1
        lists[pre_index+1] = current
    return lists
print(insert_sort(lists))










