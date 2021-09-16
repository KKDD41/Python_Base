import math

def gcd(a: int, b: int):  # работает и для отрицательных
    a = int(math.fabs(a))
    b = int(math.fabs(b))
    if a*b == 0:
        return max(a, b)
    elif a<=b and b != 0:
        return gcd(b-a, a)
    elif b<=a and a != 0: #a<b
        return gcd(a-b, b)

print(gcd(5, 80))