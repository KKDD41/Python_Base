import numpy as np


def factorize(p, primes, cache):  # возвращает все возможные разложения на множители числа p
    if p in primes:
        cache[p] = {(p,)}
        return cache[p]
    ways = cache.get(p, set())
    if len(ways):
        return ways
    for i in range(2, int(np.sqrt(p)) + 1):
        q, r = divmod(p, i)
        if r == 0:
            part1 = factorize(i, primes, cache)
            part2 = factorize(q, primes, cache)
            for p1 in part1:
                for p2 in part2:
                    tmp = list(p1 + p2)
                    tmp.sort()
                    ways.add(tuple(tmp))
    ways.add((p,))
    cache[p] = ways
    return ways


print(factorize(10, [2, 3, 5, 7], {}))