import copy

N, k = map(int, (input().split()))


def merge_tuples(*t):
    # это два и больше тапла в один последовательно скливает, здесь не нужно от слова совсем, но пусть будет
    return (j for i in t for j in (i if isinstance(i, tuple) else (i,)))


def generate_terms(N, k):  # выдает разбиение на слагаемые (упорядоченным набором) сумма N, кол-во слагаемых k
    assert k > 0
    if k == 1:
        return [[N]]
    if k > 1:
        f = [[[]] * k for i in range(N + 1)]
        for i in range(N + 1):
            f[i][0] = [[i]]
        for i in range(k):
            f[0][i] = [[0 * j for j in range(i + 1)]]
        for i in range(1, N + 1):
            for j in range(1, k):
                S = []
                for t in range(i):
                    for s in f[i - t][j - 1]:
                        ss = copy.deepcopy(s)
                        if ss[-1] >= t:
                            ss.append(t)
                            S.append(ss)
                f[i][j] = S
        return f[N][k - 1]


print(generate_terms(N, k))

