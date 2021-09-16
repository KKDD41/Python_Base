import sys
import math

win_list = ['PR', 'SR', 'LS', 'CL', 'CP', 'LP', 'SC', 'PS', 'RC', 'RL']
def fight(m: int, n: int, A: list, tools: list):
    if tools[m]+tools[n] in win_list:
        return A[m]
    elif tools[m] != tools[n] and tools[n]+tools[m] in win_list:
        return A[n]
    else:
        z = min(A[n], A[m])
        return z
    
def round(A: list, enemy: list, tools: list):
    A_r = []           # проведенный раунд -- полученная перестановка индексов
    tools_r = []       # оставшийся набор инструментов
    enemy_r = []       # обновленный (хоуп зет почищенный) список врагов для оставшихся
    for i in range(0, len(A), 2):
        if fight(i, i+1, A, tools) == A[i]:
            A_r.append(A[i])                        # запись победителя
            enemy[i] = enemy[i] +  str(A[i+1]) + ' '       # дополнение списка врагов победителя
            enemy_r.append(enemy[i])                # добовляет список врагов победителя в массив всех врагов для оставшихся
            tools_r.append(tools[i])                # добавляет инструмент победителя
        elif fight(i, i+1, A, tools) == A[i+1]:
            A_r.append(A[i+1])
            enemy[i+1] = enemy[i+1] + str(A[i]) + ' '
            enemy_r.append(enemy[i+1])
            tools_r.append(tools[i+1])
    return A_r, enemy_r, tools_r

n = int(input())     # количество дэбилов
A = []               # изначальная перестановка игроков
tools = []           # предметы, что им раздали
enemy = ['']*n
for i in range(n):
    N, S = input().split()
    N = int(N)
    A.append(N)
    tools.append(S)

i = 0
while n//2**i != 1:
    E = list(round(A, enemy, tools))
    A = E[0]
    enemy = E[1]
    tools = E[2]
    i+=1 
print(A[0])
S = str(enemy[0])
print(S.strip()) 