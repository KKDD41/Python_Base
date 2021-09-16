import math, sys
from collections import deque


def main():
    G = read_graph()
    start = 0
    finish = 2
    s = dijkstra(G, start)
    print(s)
    shortest_path = reveal_shortest_path(start, finish, s, G)
    print(shortest_path)

def read_graph():
    M = int(input())        # M -- количество ребер
    G = {}; i =0
    while i < M:
        a, b, weight = input().split()
        a = int(a); b = int(b); weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
        i+=1   
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight
    return G

def dijkstra(G, start):
    Q = deque([start])
    s = {start: 0}
    while Q:
        v = Q.popleft()
        for u in G[v]:      # ключи словаря G[v]
            if u not in s or s[v] + G[u][v] < s[u]:
                s[u] = s[v] + G[u][v]
                Q.append(u)
    return s

def reveal_shortest_path(start, finish, s, G):
    path = [finish]
    v = finish
    while v is not start:
        for n in G[v]:
            if s[v] == s[n] + G[v][n]:
                path.append(n)
                v = n
                break
    return path

    
if __name__ == '__main__':
    main()