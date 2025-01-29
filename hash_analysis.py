from functools import reduce
from typing import Counter

strings = [ "apple", "voadora", "banjo", "banana", "cherry", "date",
"elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
"mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
"raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
"IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco" ]

def hash_somatorio(key):
    return sum(map(ord, key))

def hash_polinomial(key):
    return sum(map(lambda x: ord(x[1]) * 5**x[0], enumerate(key)))

def hash_cicle(key):
    return sum(map(lambda x: ord(x[1]) ^ ord(key[x[0] - 1]), enumerate(key)))

def divisao(code):
    return code % 32

def dobra(code):
    arr = list(map(int, str(code)))
    while len(arr) > 2:
        digit0 = (arr[0] + arr[3])%10 if len(arr) > 3 else arr[0]
        digit1 = (arr[1] + arr[2])%10
        arr = [digit1, digit0] + arr[3:]
    num = reduce(lambda x, y: x * 10 + y, arr)
    return divisao(num)

def mad(code):
    return divisao((2 * code + 1) % 3923)

hash_funcs = [hash_somatorio, hash_polinomial, hash_cicle]
compress_funcs = [divisao, dobra, mad]

for hf in hash_funcs:
    for cf in compress_funcs:
        results = []
        for word in strings:
            value = hf(word)
            results.append(cf(value))
        print(hf.__name__, cf.__name__, "colisões: ", sum(map(lambda x: x - 1, Counter(results).values())))
