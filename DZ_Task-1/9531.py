from itertools import permutations

graph = 'аб бд де еж жз за вб ва вг гд ез'.split()
matrix = '345 35 128 156 124 478 68 367'.split()

for i in permutations('абвгдежз'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i, sep='')

# бгдавзже