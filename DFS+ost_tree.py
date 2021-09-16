import math, sys

G = {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}

def dfs(v, G: dict, used, ost_tree):
    used.add(v)
    for neighbour in G[v]:        
        if neighbour not in used:
            ost_tree[v].append(neighbour)
            ost_tree[neighbour].append(v)
            dfs(neighbour, G, used, ost_tree) 

    return ost_tree


used = set()
N = 0    # количество компонент связности G
ost_tree = {v: [] for v in range(len(G))}
for v in G.keys():
    if v not in used:
        dfs(v, G, used, ost_tree)
        N += 1

print(ost_tree)