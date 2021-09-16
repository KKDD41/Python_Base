import math

def array_search(A, n, x):
    B = []
    top_B = 0
    for i in range(n):
        if A[i] == x:
            B.append(i+1)
            top_B+=1
    if top_B == 0:
        return 'в массиве А такого числа нет'
    else:
        return list(B)
   
n, x = map(int, input().split()) # n = len(A) -- количество элементов в массиве A
if n<0:
    print('Длина массива отрицательная, ты шо дурак?')
else:
    A = list(input().split())
    for i in range(len(A)):
        A[i] = int(A[i])
    print('Исходный массив:', A)
    print('Индексы искомого числа', x, ' в массиве A:', array_search(A, n, x))

