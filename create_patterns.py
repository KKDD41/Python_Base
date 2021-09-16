import math

# ввод линейного массива
A = list(input().split())
for i in range(len(A)):
    A[i] = int(A[i])

m = n = 1; i = j = 1
# массив массивов m x n
A_ij = A[i*m + j] 
# или
A = [[0]*m for i in range(n)]
# где A_ij = A[j].[i]

# считывание взвешенного графа
def read_graph():
    M = int(input())        # M -- количество ребер
    G = {}
    i = 0
    while i<M:
        a, b, weight = input().split()
        a = int(a); b = int(b); weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)   
        i+=1
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

