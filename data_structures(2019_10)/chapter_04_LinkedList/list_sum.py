
def arr_sum(arr: list, i: int) -> int:
    if i == len(arr):
        return 0
    return arr[i] + arr_sum(arr, i+1)


arr_list = [i for i in range(100)]
print(arr_sum(arr_list, 0))
