import math

key = int(input())
A = list(input().split())
for i in range(len(A)):
    A[i] = int(A[i])

# бинарный поиск работает только с отсортированным списком

A.sort()
print(A)

def left_bound(A: list, key):
    a = -1
    b = len(A)
    while b-a > 1:
        middle = (b+a)//2
        if A[middle] < key:
            a = middle
        else:
            b = middle
    return a

def right_bound(A: list, key):
    a = -1
    b = len(A)
    while b-a > 1:
        middle = (b+a)//2
        if A[middle] <= key:
            a = middle
        else:
            b = middle
    return b


print('левый индекс:', left_bound(A, key))
print('правый индекс:', right_bound(A, key))