import math

A = list(input().split())
for i in range(len(A)):
    A[i] = int(A[i])

# квадратичные:
def insert_sort(A, n): 
    n = len(A)
    for i in range(1, n):
        k = i
        while k>0 and A[k-1]>A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k-=1
    return A

def choise_sort(A, n):
    for i in range(0, n-1):
        for k in range(i+1, n):
            if A[k]<A[i]:
                A[k], A[i] = A[i], A[k]
    return A

def bubble_sort(A, n):
    for i in range(1, n):
        for k in range(0, n-i):
            if A[k]>A[k+1]:
                A[k], A[k+1] = A[k+1], A[k] 
    return A

#print(insert_sort(A, n), choise_sort(A, n), bubble_sort(A, n))

# однопроходный (для фиксированной и небольшой области значений)
# !!!ЗДЕСЬ ОБЛ ЗНАЧЕНИЙ ПРИНИМАЕТ ТОЛЬКО НЕОТРИЦАТЕЛЬНЫЕ ЗНАЧЕНИЯ!!!

n = int(input('максимум из области значений:'))
L = int(input('количество вводимых символов:'))
F = [0]*n
for i in range(L):
    x = int(input())
    if x <= n:
        F[x]+=1
    else:
       print('недопустимое число')
       quit()
for x in range(n):
    print(str(x)*F[x], end='')

# реккурентные сортировки:
# квик сорт + хоар сорт, изи пизи лемон сквизи
