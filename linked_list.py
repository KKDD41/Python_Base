import math, sys

class LinkedList:
    def __init__(self):
        self._begin = None
    def insert(self, x):
        self._begin = [x, self._begin]  # добавление элемента на 0-й уровень, со сдвигом на +1 уже имеющихся
    def pop(self):
        x = self._begin[0]              # удаление нулевого 0-го уровня
        self._begin = self._begin[1]
        return x
    def __str__(self):
        a = self._begin              # печатает
        s = ''
        while a is not None:
            s = s + str(a[0]) + ' '
            a = a[1]
        return s
    def depth(self):
        a = self._begin              # считает количество уровней
        s = 0
        while a is not None:
            s += 1
            a = a[1]
        return s