import math, sys

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(word, n):
    Alphabet = {' ': ' '}
    for i in range(26):
        Alphabet[a[i]] = a[(i+n) % 26]
    word_0 = ''
    for i in range(len(word)):
        word_0 = word_0 + Alphabet[word[i]]
    return word_0

word = input()
n = int(input())
print(caesar(word, n))

