# def Perm(arrs):
#     # 若输入 [1,2,3]，则先取出1，将剩余的 [2,3]全排列得到 [[2,3],[3,2]]，
#     #               再将 1加到全排列 [[2,3],[3,2]]上变成 [[1,2,3],[1,3,2]]
#     # 同理，取出2或者3时，得到的分别是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
#     if len(arrs)==1:
#         return [arrs]
#     result = []  # 最终的结果（即全排列的各种情况）
#     for i in range(len(arrs)):
#         rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
#         rest_lists = Perm(rest_arrs)   # 剩余的元素完成全排列
#         lists = []
#         for term in rest_lists:
#             lists.append(arrs[i:i+1]+term)  # 将取出的第 i个元素加到剩余全排列的前面
#         result += lists
#     return result
#
#
# print(Perm([1,2,3]))

import numpy as np

np.random.randint(0, 10, (4, 3, 2))