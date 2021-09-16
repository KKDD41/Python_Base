import math, sys

n = int(input())
P = []
for i in range(n):
    p = int(input())
    P.append(p)
    
P.sort() # упорядочиваю силы лошадок
D = []
for i in range(len(P)-1):
    D.append(P[i+1] - P[i]) # создаю массив разностей (между упорядоченными)

print(min(D)) # беру из них минимум