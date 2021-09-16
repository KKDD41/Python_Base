import math, sys

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Alphabet = {}
for i in range(26):
    Alphabet[a[i]] = i
    Alphabet[i] = a[i]

def vigenere(word, key): 
    word_0 = ''
    for i in range(len(word)):
        word_0 = word_0 + Alphabet[ (Alphabet[word[i]] + Alphabet[ key[i % len(key)] ]) % 26 ] 
    return word_0

def decode_vigenere(word, key):
    word_0 = ''
    for i in range(len(word)):
        word_0 = word_0 + Alphabet[ (Alphabet[word[i]] - Alphabet[ key[i % len(key)] ]) % 26 ] 
    return word_0

word = input()
key = input()
print(decode_vigenere(word, key))