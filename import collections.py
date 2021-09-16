from collections import Counter


def test_on_digits(n, k):
    arr1 = list(str(n))
    arr2 = list(str(k))
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    for i in range(10):
        if c1[str(i)] != c2[str(i)]:
            return 0
    return 1


def test():
    i = 125872
    while True:
        print(i)
        c = 0
        for j in range(2, 7):
            if test_on_digits(i, j * i):
                c += 1
        if c == 5:
            return i
        i += 1

import itertools


def compute():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
	ans = next(i for i in itertools.count(1) if cond(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())