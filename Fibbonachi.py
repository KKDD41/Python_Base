import math

n = int(input())

# реккурентная + супер медленная (считает отдельно F(n-1) и F(n-2))
def F1(n: int):
    if n<=1:
        return n
    else:
        return F1(n-1)+F1(n-2)


# нормальная реализация через списки
fib = [0, 1] + [0]*(n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

# пиздатая реализация через обмен (не выпонится F(0) но все равно круто)
a, b, n = 0, 1, int(input())
for i in range(2, n+1):
    a, b = b, a+b
print(b)    