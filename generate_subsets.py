from itertools import combinations

l = [1, 2, 3]
for i in range(len(l) + 1):
    print([j for j in combinations(l, i)])  # combinations(list or set or tuple, number of elements in subsets)

S = (1, 2, 3, 4, 5)
for i in range(len(S)+1):
    print([j for j in combinations(S, i)])