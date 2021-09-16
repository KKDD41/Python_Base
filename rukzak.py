
max_Weight = int(input())

w = list(input().split())
for i in range(len(w)):
    w[i] = int(w[i])

c = list(input().split())
for i in range(len(c)):
    c[i] = int(c[i])


def max_coast(c, w, max_Weight):
    F = [[0]*(max_Weight + 1) for i in range(len(c) + 1)]
    # F[i][j] -- максимальная стоимоть из первых i элементов, где их вес равен j
    for i in range(1, len(c)+1):
        for j in range(1, max_Weight+1):
            if w[i-1] > j:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = max(F[i-1][j-w[i-1]] + c[i-1], F[i-1][j])
    k = max_Weight
    take_set = []
    for i in range(len(c), 0, -1):
        if F[i][k] != F[i-1][k]:
            take_set.append(i) 
            k -= w[i-1]
    take_set.reverse()
    return F[-1][-1], take_set


print(max_coast(c, w, max_Weight))