from itertools import *

graph = 'БВ ВЕ ЕД ДГ ГА АБ АВ ЖЕ ЖД'.split()
matrix = '25 137 267 56 146 345 23'.split()

print(*range(1, 8))
for i in permutations('АБВГДЖЕ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)