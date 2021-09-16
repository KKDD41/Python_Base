import math
import sys

def N(point: list):
    point = [point[0], point[1]-1]
    return point

def NE(point: list):
    point = [point[0]+1, point[1]-1]
    return point

def E(point: list):
    point = [point[0]+1, point[1]]
    return point

def SE(point: list):
    point = [point[0]+1, point[1]+1]
    return point

def S(point: list):
    point = [point[0], point[1]+1]
    return point

def SW(point: list):
    point = [point[0]-1, point[1]+1]
    return point

def W(point: list):
    point = [point[0]-1, point[1]]
    return point

def NW(point: list):
    point = [point[0]-1, point[1]-1]
    return point

a, b, x, y = map(int, input().split())
start = [x, y]
finish = [a, b]

while start[0] != a or start[1] != b:
    if start[0]>a:
        if start[1]>b:
            start = NW(start)
            print('NW')
        elif start[1]<b:
            start = SW(start)
            print('SW')
        else:
            start = W(start)
            print('W')
    elif start[0]<a:
        if start[1]>b:
            start = NE(start)
            print('NE')
        elif start[1]<b:
            start = SE(start)
            print('SE')
        else:
            start = E(start)
            print('E')
    elif start[0] == a:
        if start[1]>b:
            start = N(start)
            print('N')
        elif start[1]<b:
            start = S(start)
            print('S')

#####################################

lx, ly, x, y = [int(i) for i in input().split()]

while True:
    move  = 'N' if y>ly else 'S' if y<ly else ''
    move += 'W' if x>lx else 'E' if x<lx else ''
    
    if 'N' in move: y-=1
    if 'S' in move: y+=1
    if 'W' in move: x-=1
    if 'E' in move: x+=1

    print(move)
