import math

n = int(input())
if n == 0:
    print('all numbers divide 0')
else:
    n = int(math.fabs(n)) # заделали инпут положительным
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ') # вывод только положительных делителей
        