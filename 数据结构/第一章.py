import random

# list = [random.randrange(0, 100) for x in range(10)]
# # list = [6, 2, 3, 4, 5]
# print(list)
# x2 = 47
# list.append(x2)

# 快速排序
# for i in range(len(list)):
#     for j in range(i+1, len(list)):
#         if list[j] < list[i]:
#             list[j], list[i] = list[i], list[j]
#
# print(list)
#

# 二分查找
# left, right = 0, len(list)-1
# while left < right:
#     mid = int((left + right)/2)
#     print(mid)
#     if x2 == list[mid]:
#         print(list[mid])
#         break
#     elif x2 < list[mid]:
#         right = mid-1
#     else:
#         left = mid +1

# 优化的冒泡排序
# count = 0
# for i in range(len(list)):
#     t = 1
#     for j in range(len(list)-i-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
#             t = 0
#     if t == 1:
#         break
# print(list)

# 列表平移
# list = list[-3:]+ list[:-3]
# print(list)


# def gcd(a, b):
#     while a % b != 0:
#         a, b = b, b%a
#     return b

# 1到10000的同构数

# k = 10
# for i in range(1, 10000):
#     if i == k:
#         k *= 10
#     elif i == i**2%k:
#         print(i, k, i**2)

# 最大公约数
# def gcd(a, b):
#     while a % b != 0:
#         a, b = b, a % b
#     return b
#
# Por 大数质数分解
# def fec(number):
#     number = number
#     x_fixed = 2
#     cycle_size = 2
#     x = 2
#     factor = 1
#     while factor == 1:
#         count = 1
#         while count <= cycle_size and factor <= 1:
#             x = (x*x + 1) % number
#             factor = gcd(x - x_fixed, number)
#             count += 1
#         cycle_size *= 2
#         x_fixed = x
#     return factor

# t = 1103886099019437
# a = fec(t)
# print(a)
# b = int(fec(t/a))
# print(b)
# c = int(fec(t/a/b))
# print(c)

# 分解知质数
# list = []
# # def prime(n):
# #     if n < 2:
# #         list.append(n)
# #         return list
# #     else:
# #         for i in range(2, int(n**0.5)+1):
# #             if n % i == 0:
# #                 list.append(i)
# #                 # print(i, int(n / i))
# #                 return prime(n / i)
# #         list.append(int(n))
# #         return list
# #
# # print(prime(110388609901943))

# 翻转数列
# list = []
# def reverse(n, m):
#     if m <= 0:
#         return False
#     if n % 2*m == 0:
#         flag = -1
#         k = 0
#         sum = 0
#         for i in range(1, n+1):
#             if k < m :
#                 i = i * flag
#                 k += 1
#                 sum += i
#             if k == m:
#                 flag *= -1
#                 k = 0
#             list.append(i)
#         return sum
#
# a, b = input().split(' ')
# x = reverse(int(a), int(b))
# print(x)

date = [0,1,2,3,4,5,6,7,8,9,0]
print(date)
for i in range(10, 5, -1):
    print(i)
    date[i] = date[i-1]
date[5] = 44
print(date)


