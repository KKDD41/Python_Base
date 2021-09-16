import math, sys

def graph_to_sets(G: dict):
    edges = []
    offset = [0]
    n = len(G.keys())
    for i in range(n):
        for j in range(len(G[i])):
            edges.append(G[i][j])
        offset.append(offset[i]+len(G[i]))
    return edges, offset

n = int(input())
edg = []
for i in range(n):
    E = list(input().split())
    for i in range(len(E)):
        E[i] = int(E[i])
    edg.append(E)

V = [i for i in range(n)]
G = dict(zip(V, edg))

edges, offset = graph_to_sets(G)
print(offset)
# список вершин, смежных с i, это срез:
# edges[offset[i]: offset[i+1]]

