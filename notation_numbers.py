import math 

def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base, from_base) + alphabet[n % to_base]

from_base, to_base = map(int, input().split())
num = input()

if 0<=from_base<=36 and 0<=to_base<=36:
    print(convert_base(num, to_base, from_base))
else: 
    print('begi v durku')
#я-то код починила, но как эта херота работает до сих пор не ясно...