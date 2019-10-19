import random

a = [random.randrange(0, 100) for x1 in range(5)]
a.sort()
print(a)

b= [random.randrange(0, 100) for x2 in range(10)]
b.sort()
print(b)

i = 0
def merge_sort(a, b):
    c = []
    i = j = 0
    while len(a) > i and len(b) > j:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if len(a) > i:
        c += a[i:]
    if len(b) > j:
        c += b[j:]

    return c
print(merge_sort(a, b))