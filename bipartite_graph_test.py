import math, sys

def dfs(v, G: dict, used, ost_tree):
    used.add(v)
    for neighbour in G[v]:        
        if neighbour not in used:
            ost_tree[v].add(neighbour)
            ost_tree[neighbour].add(v)
            dfs(neighbour, G, used, ost_tree) 

    return ost_tree


used = set()
G = {0: {1, 0, 3}, 1: {0, 2, 3}, 2: {1, 0, 3}, 3: {1, 0, 2}}
ost_tree = {v: set() for v in range(len(G))}
for v in G.keys():
    if v not in used:
        dfs(v, G, used, ost_tree)
        
e = True
for v in G.keys():
    e = e*True if G[v] == ost_tree[v] else e*False
print(e)
