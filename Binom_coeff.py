import math, sys

def C(n, k):
    C = [[1]*(n+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            C[i][j] = C[i-1][j-1]+C[i-1][j]
    return C[n-1][k]
