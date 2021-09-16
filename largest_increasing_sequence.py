import math, sys
 
def lis(A: list):
    f = [0]*len(A)  # f[i] -- длина возрастающей последовательности, что заканчивается на A[i]
    for i in range(len(A)):
        m = ''
        for j in range(i):
            if A[i] > A[j] and f[j] > m:
                m = f[j]
        f[i] = m + ' ' + str(A[i])
    max_sequence = ''
    for i in range(len(A)):
        max_sequence = f[i] if len(f[i])>len(max_sequence) else max_sequence
    return max_sequence.strip()


A = list(input().split())
for i in range(len(A)):
    A[i] = int(A[i])

print(lis(A))