import math
import sys

# кузнечик прыгает по строке, на некоторые клетки вставать нельзя.
# у кузнечика есть набор возможных действий, начальная и конечные позиции.
#    тут: +1, +2, +3
#    
#

# требуется найти количество возможных путей от начальной до конечнойdatetime 

# массив буллей 
N = int(input())
allowed = []
for i in range(N):
    allowed.append(int(input()))

# вычисление 

def count_tr(N, allowed: list):
    K = [0, 1, int(allowed[2])] + [0]*(N-3)
    for i in range(3, N+1):
        if allowed[i] == 1:
            K[i] = K[i-1]+K[i-2]+K[i-3]
        elif allowed[i] == 0:
            K[i] = 0
    return K(N)


print(count_tr(N, allowed))