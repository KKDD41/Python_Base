import math

n = int(input('Длина перестановки:'))
P = list(input().split())
for i in range(len(P)):
    P[i] = int(P[i])


# перестановки чисел от 1 до n на m позициях
def generate_permutations(n: int, m: int, prefix=None):
    m = n if m == -1 else m  # по умолчанию m = n
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for num in range(1, n + 1):
        if num in prefix:  # если убрать эту часть, 
            continue  # будет считать и с повторениями элементов
        prefix.append(num)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


# из встроенного, клепает массив перестановок
# сохраняет одинаковые перестановки
from itertools import permutations

print(list(permutations(P, n)))


#######################################################
# выкидывает одинаковые перестановки и исключает повторяющиеся элементы массива    
def clean_list(P: list):
    P_clean = []
    for x in P:
        if x in P_clean:
            pass
        else:
            P_clean.append(x)
    return P_clean
