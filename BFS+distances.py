import math, sys
from collections import deque

G = {0: {1, 3}, 1: {0}, 2: {3}, 3: {0, 2}}

start = 1
distances = {i: 0 for i in range(len(G))}
used = {start}
Q = deque([start])

def BFS(Q, used, distances):
    v = Q.popleft()
    for neighbour in G[v]:
        if neighbour not in used:
            used.add(neighbour)
            Q.append(neighbour)
            distances[neighbour]=distances[v]+1
               
        
while Q:
    BFS(Q, used, distances)

print(distances)