import math, sys

votes = {}
N = int(input())
for i in range(N):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

print(votes.keys())
print(votes.values())
print(votes.items())