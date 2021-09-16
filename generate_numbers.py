import math

def generate_numbers(n: int, m: int, prefix = None): # при n<=10 будет выглядеть логичнее, но и так норм.
    if m == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()

n = int(input('Система счисления:'))
m = int(input('Длина массива:'))
generate_numbers(n, m)