import math

n = int(input()) # от 2 до n не включительно!!!
primes_n = []
composite_n = []
if n<=1:
    print('number must be at least 2')
else:
    A = [True]*n
    A[0] = A[1] = False
    for i in range(n):
        if A[i]:
            for k in range(2*i, n, i):
                A[k] = False
    for i in range(2, n):
        if A[i]:
            primes_n.append(i)
        else:
            composite_n.append(i)
    print('primes:', primes_n)
    print('composite numbers:', composite_n)