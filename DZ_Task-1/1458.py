from itertools import permutations

graph = 'аб бе еж жд дв ав аг гв гб гд бд де'.split()
matrix = '256 13467 2456 237 136 1235 24'.split()

print(*range(1, 8))
for i in permutations('абвгдеж'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# ВДБЕАГЖ