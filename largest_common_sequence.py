import math
import sys


def lcs(A: list, B: list):
    F = [['']*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + ' ' + str(A[i-1]) 
            else:
                F[i][j] = F[i-1][j] if len(F[i-1][j])>len(F[i][j-1]) else F[i][j-1]
    return F[-1][-1]



A = list(input().split())
for i in range(len(A)):
    A[i] = int(A[i])

B = list(input().split())
for i in range(len(B)):
    B[i] = int(B[i])
    
print(lcs(A, B))