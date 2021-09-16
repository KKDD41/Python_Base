import math
import numpy as np


def p_test(n):  # True, if n is prime
    assert n > 1
    i = 2
    if n == 2:
        return True
    else:
        while i <= int(math.sqrt(n)):
            if n % i == 0:
                return False
            i += 1
    return True


def find_all_primes(max_num):  # возвращает набор простых до max_num
    primes = np.arange(1, max_num + 1)
    Bool = np.ones(max_num, dtype=bool)
    Bool[0] = 0
    max_iter = int(np.sqrt(max_num))
    for i in range(2, max_iter + 1):
        if Bool[i - 1]:
            Bool[np.arange(2 * i - 1, max_num, i)] = False
    return primes[Bool]  # сет из primes[i], для которых Bool[i] == True
